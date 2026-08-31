"""Build and independently verify APP-5 Module 02 population measures with SQLite."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import sqlite3
import tempfile
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SQL_FILES = (
    "01-link-sources-and-build-denominators.sql",
    "02-link-events-and-separate-public-measure.sql",
    "03-calculate-rates-and-direct-standardization.sql",
    "04-indirect-standardization-and-validation.sql",
)
OUTPUT_TABLES = {
    "tract-linkage-audit.csv": "tract_linkage_audit",
    "age-band-denominators.csv.gz": "adult_age_denominators",
    "synthetic-event-linkage.csv.gz": "linked_synthetic_events",
    "age-specific-rates.csv.gz": "age_specific_rates",
    "standard-population.csv": "standard_population",
    "tract-rate-summary.csv": "tract_rate_summary",
    "indirect-standardization.csv": "indirect_standardization",
    "public-modeled-prevalence.csv": "public_modeled_prevalence",
    "source-reconciliation.csv": "source_reconciliation",
    "query-checks.csv": "query_checks",
}


class BuildError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BuildError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def deterministic_gzip(raw: bytes) -> bytes:
    output = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
        zipped.write(raw)
    return output.getvalue()


def format_value(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.10f}".rstrip("0").rstrip(".")
    return str(value)


def wilson(count: object, denominator: object, multiplier: object, upper: bool) -> float | None:
    n = int(denominator)
    if n <= 0:
        return None
    x = int(count)
    z = 1.959963984540054
    proportion = x / n
    denominator_term = 1 + z * z / n
    center = (proportion + z * z / (2 * n)) / denominator_term
    half = z * math.sqrt((proportion * (1 - proportion) + z * z / (4 * n)) / n) / denominator_term
    bound = center + half if upper else center - half
    return max(0.0, min(1.0, bound)) * float(multiplier)


def ratio_bound(count: object, expected: object, upper: bool) -> float | None:
    observed = int(count)
    expected_value = float(expected)
    if expected_value <= 0:
        return None
    if observed == 0:
        return 2.995732273553991 / expected_value if upper else 0.0
    ratio = observed / expected_value
    return ratio * math.exp((1.959963984540054 / math.sqrt(observed)) * (1 if upper else -1))


def open_source(path: Path):
    return gzip.open(path, "rt", encoding="utf-8", newline="") if path.suffix == ".gz" else path.open(encoding="utf-8", newline="")


def load_csv_table(connection: sqlite3.Connection, table: str, path: Path) -> tuple[int, int]:
    with open_source(path) as handle:
        reader = csv.reader(handle)
        fields = next(reader)
        require(len(fields) == len(set(fields)), f"Duplicate source field in {path.name}")
        connection.execute(f'DROP TABLE IF EXISTS "{table}"')
        columns = ", ".join(f'"{field}" TEXT' for field in fields)
        connection.execute(f'CREATE TABLE "{table}" ({columns})')
        placeholders = ", ".join("?" for _ in fields)
        count = 0
        batch = []
        for row in reader:
            require(len(row) == len(fields), f"Source row width changed in {path.name}")
            batch.append(row)
            count += 1
            if len(batch) == 2000:
                connection.executemany(f'INSERT INTO "{table}" VALUES ({placeholders})', batch)
                batch.clear()
        if batch:
            connection.executemany(f'INSERT INTO "{table}" VALUES ({placeholders})', batch)
    return count, len(fields)


def load_sources(connection: sqlite3.Connection, root: Path) -> dict[str, dict[str, int]]:
    public = root / "upstream/module01-reference/data"
    sources = {
        "raw_acs_b01001": public / "acs-b01001-ma-tract-2024.csv",
        "raw_places": public / "places-diabetes-ma-tract-2025.csv",
        "raw_svi": public / "svi2022-ma-tract.csv",
        "raw_age_band_crosswalk": root / "data/age-band-crosswalk.csv",
        "raw_synthetic_events": root / "data/raw/synthetic-events.csv.gz",
    }
    loaded = {}
    for table, path in sources.items():
        rows, columns = load_csv_table(connection, table, path)
        loaded[table] = {"rows": rows, "columns": columns}

    crosswalk = connection.execute(
        "SELECT age_band_id, age_band, band_order, sex, source_age_label, acs_estimate_field, acs_moe_field FROM raw_age_band_crosswalk ORDER BY CAST(band_order AS INTEGER), acs_estimate_field"
    ).fetchall()
    acs_cursor = connection.execute("SELECT * FROM raw_acs_b01001 ORDER BY tract_fips")
    acs_fields = [description[0] for description in acs_cursor.description or []]
    connection.execute("DROP TABLE IF EXISTS raw_acs_age_cells")
    connection.execute(
        "CREATE TABLE raw_acs_age_cells (tract_fips TEXT, age_band_id TEXT, age_band TEXT, band_order INTEGER, sex TEXT, source_age_label TEXT, estimate_field TEXT, moe_field TEXT, estimate INTEGER, moe REAL)"
    )
    batch = []
    for values in acs_cursor:
        row = dict(zip(acs_fields, values))
        for age_id, age_band, order, sex, label, estimate_field, moe_field in crosswalk:
            batch.append((row["tract_fips"], age_id, age_band, int(order), sex, label, estimate_field, moe_field, int(row[estimate_field]), float(row[moe_field])))
            if len(batch) == 5000:
                connection.executemany("INSERT INTO raw_acs_age_cells VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", batch)
                batch.clear()
    if batch:
        connection.executemany("INSERT INTO raw_acs_age_cells VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", batch)
    cell_rows = connection.execute("SELECT COUNT(*) FROM raw_acs_age_cells").fetchone()[0]
    require(cell_rows == 61560, "Normalized ACS age-cell count changed")
    loaded["raw_acs_age_cells"] = {"rows": cell_rows, "columns": 10}
    return loaded


def execute_sql(connection: sqlite3.Connection, sql_root: Path) -> dict[str, str]:
    hashes = {}
    for filename in SQL_FILES:
        path = sql_root / filename
        require(path.is_file(), f"SQL file is missing: {filename}")
        text = path.read_text(encoding="utf-8")
        require("REPLACE" not in text, f"SQL file is incomplete: {filename}")
        connection.executescript(text)
        hashes[filename] = sha256(path)
    return hashes


def query_csv(connection: sqlite3.Connection, table: str) -> tuple[bytes, int, int]:
    cursor = connection.execute(f'SELECT * FROM "{table}"')
    fields = [description[0] for description in cursor.description or []]
    rows = cursor.fetchall()
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(fields)
    writer.writerows([[format_value(value) for value in row] for row in rows])
    return output.getvalue().encode("utf-8"), len(rows), len(fields)


def close(left: object, right: object, tolerance: float = 0.000001) -> bool:
    if left is None or right is None:
        return left is None and right is None
    return abs(float(left) - float(right)) <= tolerance


def independent_findings(connection: sqlite3.Connection) -> dict[str, object]:
    checks = connection.execute("SELECT check_id, check_name, observed_value, expected_value, status FROM query_checks ORDER BY check_id").fetchall()
    require(len(checks) == 30 and all(row[4] == "pass" for row in checks), "One or more SQL query checks failed")
    denominator_rows = connection.execute("SELECT tract_fips, age_band_id, denominator_estimate FROM adult_age_denominators ORDER BY tract_fips, band_order").fetchall()
    event_rows = connection.execute("SELECT tract_fips, age_band_id, synthetic_event_count, denominator_estimate FROM linked_synthetic_events ORDER BY tract_fips, band_order").fetchall()
    rate_rows = connection.execute("SELECT tract_fips, age_band_id, synthetic_event_count, denominator_estimate, age_specific_rate_per_100k, rate_low_95, rate_high_95 FROM age_specific_rates ORDER BY tract_fips, band_order").fetchall()
    require(len(denominator_rows) == len(event_rows) == len(rate_rows) == 7985, "Age-band output shape changed")
    require(sum(int(row[2]) for row in denominator_rows) == 5679768, "Python denominator reconciliation failed")
    require(sum(int(row[2]) for row in event_rows) == 283614, "Python event reconciliation failed")
    for tract, age_id, count, denominator, rate, low, high in rate_rows:
        n = int(denominator)
        x = int(count)
        expected_rate = 100000.0 * x / n if n else None
        require(close(rate, expected_rate), f"Python age-specific rate check failed: {tract} {age_id}")
        require(close(low, wilson(x, n, 100000.0, False)) and close(high, wilson(x, n, 100000.0, True)), f"Python Wilson interval check failed: {tract} {age_id}")

    standards = {
        row[0]: {"weight": float(row[1]), "rate": float(row[2]), "population": int(row[3]), "events": int(row[4])}
        for row in connection.execute("SELECT age_band_id, standard_weight, statewide_synthetic_rate_per_100k, standard_population, statewide_synthetic_events FROM standard_population")
    }
    require(len(standards) == 5 and close(sum(row["weight"] for row in standards.values()), 1.0, 0.000000001), "Python standard-weight check failed")
    require(sum(row["population"] for row in standards.values()) == 5679768 and sum(row["events"] for row in standards.values()) == 283614, "Python standard population totals failed")

    by_tract: dict[str, list[tuple[str, int, int]]] = defaultdict(list)
    for tract, age_id, count, denominator in event_rows:
        by_tract[tract].append((age_id, int(count), int(denominator)))
    summaries = {
        row[0]: row[1:]
        for row in connection.execute("SELECT tract_fips, synthetic_event_count, adult_denominator_estimate, crude_rate_per_100k, direct_standardized_rate_per_100k, guided_indirect_required FROM tract_rate_summary")
    }
    indirect = {
        row[0]: row[1:]
        for row in connection.execute("SELECT tract_fips, synthetic_event_count, expected_synthetic_events, standardized_event_ratio FROM indirect_standardization")
    }
    require(len(by_tract) == len(summaries) == len(indirect) == 1597, "Tract summary shape changed")
    direct_available = 0
    indirect_required = 0
    for tract, rows in by_tract.items():
        events = sum(row[1] for row in rows)
        population = sum(row[2] for row in rows)
        crude = 100000.0 * events / population
        direct = None if any(row[2] == 0 for row in rows) else 100000.0 * sum((row[1] / row[2]) * standards[row[0]]["weight"] for row in rows)
        expected = sum(row[2] * standards[row[0]]["rate"] / 100000.0 for row in rows)
        ratio = events / expected
        summary = summaries[tract]
        indirect_row = indirect[tract]
        require(int(summary[0]) == events and int(summary[1]) == population and close(summary[2], crude), f"Python crude-rate check failed: {tract}")
        require(close(summary[3], direct), f"Python direct-standardization check failed: {tract}")
        require(int(indirect_row[0]) == events and close(indirect_row[1], expected, 0.00001) and close(indirect_row[2], ratio, 0.000001), f"Python indirect-standardization check failed: {tract}")
        direct_available += direct is not None
        indirect_required += min(row[2] for row in rows) < 50
    require(direct_available == 1576 and indirect_required == 80, "Python support-state counts changed")

    public_fields = {description[0] for description in connection.execute("SELECT * FROM public_modeled_prevalence LIMIT 0").description or []}
    synthetic_fields = {description[0] for description in connection.execute("SELECT * FROM tract_rate_summary LIMIT 0").description or []}
    require("synthetic_event_count" not in public_fields and "modeled_crude_prevalence_percent" not in synthetic_fields, "Public and synthetic measure schemas were blended")
    return {
        "query_checks": len(checks),
        "failed_query_checks": 0,
        "tract_union": 1620,
        "measure_tracts": len(by_tract),
        "age_band_rows": len(rate_rows),
        "adult_denominator": 5679768,
        "synthetic_events": 283614,
        "direct_rates_available": direct_available,
        "direct_rates_unavailable": len(by_tract) - direct_available,
        "guided_indirect_required": indirect_required,
        "public_modeled_rows": connection.execute("SELECT COUNT(*) FROM public_modeled_prevalence").fetchone()[0],
    }


def build(root: Path, sql_root: Path, output_root: Path) -> dict[str, object]:
    import freeze_upstream
    import generate_synthetic_events

    root = root.resolve()
    sql_root = sql_root.resolve()
    output_root = output_root.resolve()
    if output_root.exists() and any(output_root.iterdir()):
        raise FileExistsError(f"Refusing to overwrite nonempty output target: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)
    handoff = freeze_upstream.verify(root)
    source = generate_synthetic_events.verify(root)
    with tempfile.TemporaryDirectory(prefix="app5-module02-db-") as temp_dir:
        database = Path(temp_dir) / "population-measures.sqlite"
        connection = sqlite3.connect(database)
        connection.create_function("SQRT", 1, math.sqrt)
        connection.create_function("WILSON_LOW", 3, lambda x, n, m: wilson(x, n, m, False))
        connection.create_function("WILSON_HIGH", 3, lambda x, n, m: wilson(x, n, m, True))
        connection.create_function("RATIO_LOW", 2, lambda x, expected: ratio_bound(x, expected, False))
        connection.create_function("RATIO_HIGH", 2, lambda x, expected: ratio_bound(x, expected, True))
        try:
            loaded = load_sources(connection, root)
            sql_hashes = execute_sql(connection, sql_root)
            findings = independent_findings(connection)
            outputs = {}
            for filename, table in OUTPUT_TABLES.items():
                raw, rows, columns = query_csv(connection, table)
                value = deterministic_gzip(raw) if filename.endswith(".gz") else raw
                path = output_root / filename
                path.write_bytes(value)
                outputs[filename] = {
                    "rows": rows,
                    "columns": columns,
                    "bytes": len(value),
                    "sha256": sha256_bytes(value),
                    "content_bytes": len(raw),
                    "content_sha256": sha256_bytes(raw),
                }
        finally:
            connection.close()
    report = {
        "schema_version": "1.0.0",
        "module_id": "oclc-app5-02",
        "module_version": "0.1.0",
        "commons_release": "0.88.0",
        "source_release": "fma-dp-01-measures-v1",
        "handoff": handoff,
        "source": source,
        "loaded": loaded,
        "sql_sha256": sql_hashes,
        "outputs": outputs,
        "findings": findings,
        "interpretation_status": "population-measure release only; no disparity, ranking, targeting, allocation, intervention, real-community, implementation, or deployment conclusion",
    }
    (output_root / "build-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return report


def verify_committed(root: Path = ROOT) -> dict[str, object]:
    output_root = root.resolve() / "outputs"
    report = json.loads((output_root / "build-report.json").read_text(encoding="utf-8"))
    require(report["module_id"] == "oclc-app5-02" and report["module_version"] == "0.1.0" and report["commons_release"] == "0.88.0", "Committed build-report identity changed")
    require(report["source_release"] == "fma-dp-01-measures-v1", "Committed source release changed")
    for filename, metadata in report["outputs"].items():
        path = output_root / filename
        require(path.is_file() and path.stat().st_size == metadata["bytes"] and sha256(path) == metadata["sha256"], f"Committed output identity changed: {filename}")
    findings = report["findings"]
    require(findings["query_checks"] == 30 and findings["failed_query_checks"] == 0, "Committed query checks changed")
    return {
        "outputs": len(report["outputs"]),
        "measure_tracts": findings["measure_tracts"],
        "age_band_rows": findings["age_band_rows"],
        "adult_denominator": findings["adult_denominator"],
        "synthetic_events": findings["synthetic_events"],
        "query_checks": findings["query_checks"],
    }


def self_check() -> None:
    committed = verify_committed(ROOT)
    with tempfile.TemporaryDirectory(prefix="app5-module02-measures-") as temp_dir:
        base = Path(temp_dir)
        first = build(ROOT, ROOT / "reference/sql", base / "first")
        second = build(ROOT, ROOT / "reference/sql", base / "second")
        require(first["findings"] == second["findings"] and first["outputs"] == second["outputs"], "Two measure builds differ")
        for filename in first["outputs"]:
            require((base / "first" / filename).read_bytes() == (base / "second" / filename).read_bytes(), f"Two measure outputs differ: {filename}")
            require((base / "first" / filename).read_bytes() == (ROOT / "outputs" / filename).read_bytes(), f"Committed measure output differs: {filename}")
        try:
            build(ROOT, ROOT / "reference/sql", base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Measure builder did not protect a nonempty target")
    print(f"APP-5 Module 02 measure-builder self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--sql-root", type=Path)
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.write:
            print(json.dumps(build(args.root, args.sql_root or (args.root / "reference/sql"), args.output_root or (args.root / "outputs")), indent=2, sort_keys=True))
        else:
            print(json.dumps(verify_committed(args.root), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, sqlite3.Error, BuildError) as error:
        parser.exit(1, f"Measure build failed: {error}\n")


if __name__ == "__main__":
    main()
