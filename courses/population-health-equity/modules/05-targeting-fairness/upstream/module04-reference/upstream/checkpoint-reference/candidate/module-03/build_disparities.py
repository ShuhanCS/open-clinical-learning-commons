"""Build and independently verify APP-5 Module 03 disparity evidence with SQLite."""

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
    "01-link-equity-margins-and-reconcile.sql",
    "02-build-group-age-rates.sql",
    "03-standardize-and-compare-references.sql",
    "04-audit-missingness-bias-and-suppression.sql",
)
OUTPUT_TABLES = {
    "equity-margin-reconciliation.csv": "source_reconciliation",
    "group-age-rates.csv": "group_age_rates",
    "standardized-group-rates.csv": "standardized_group_rates",
    "disparity-comparisons.csv": "disparity_comparisons",
    "summary-disparities.csv": "summary_disparities",
    "missingness-audit.csv": "missingness_audit",
    "representation-audit.csv": "representation_audit",
    "published-tract-group-rates.csv.gz": "published_tract_group_rates",
    "complementary-suppression-audit.csv": "complementary_suppression_audit",
    "bias-register.csv": "bias_register",
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
        batch = []
        count = 0
        for row in reader:
            require(len(row) == len(fields), f"Source row width changed in {path.name}")
            batch.append(row)
            count += 1
            if len(batch) == 5000:
                connection.executemany(f'INSERT INTO "{table}" VALUES ({placeholders})', batch)
                batch.clear()
        if batch:
            connection.executemany(f'INSERT INTO "{table}" VALUES ({placeholders})', batch)
    return count, len(fields)
def load_sources(connection: sqlite3.Connection, root: Path) -> dict[str, dict[str, int]]:
    sources = {
        "raw_equity_margins": root / "data/raw/synthetic-equity-margins.csv.gz",
        "raw_field_completeness": root / "data/raw/synthetic-field-completeness.csv.gz",
        "raw_group_contract": root / "data/equity-group-contract.csv",
        "raw_standard_population": root / "upstream/module02-reference/outputs/standard-population.csv",
        "raw_upstream_denominators": root / "upstream/module02-reference/outputs/age-band-denominators.csv.gz",
        "raw_upstream_events": root / "upstream/module02-reference/outputs/synthetic-event-linkage.csv.gz",
    }
    loaded = {}
    for table, path in sources.items():
        rows, columns = load_csv_table(connection, table, path)
        loaded[table] = {"rows": rows, "columns": columns}
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
    checks = connection.execute("SELECT check_id, status FROM query_checks ORDER BY check_id").fetchall()
    require(len(checks) == 36 and all(row[1] == "pass" for row in checks), "One or more SQL query checks failed")
    reconciliations = connection.execute("SELECT check_id, status FROM source_reconciliation ORDER BY check_id").fetchall()
    require(len(reconciliations) == 12 and all(row[1] == "pass" for row in reconciliations), "One or more source reconciliation checks failed")

    standards = {
        row[0]: float(row[1])
        for row in connection.execute("SELECT age_band_id, standard_weight FROM raw_standard_population")
    }
    require(len(standards) == 5 and close(sum(standards.values()), 1.0, 0.000000001), "Standard population weights changed")

    age_rows = connection.execute(
        "SELECT equity_dimension, group_id, age_band_id, population_count, synthetic_event_count, age_specific_rate_per_100k, rate_low_95, rate_high_95 FROM group_age_rates ORDER BY equity_dimension, group_order, band_order"
    ).fetchall()
    require(len(age_rows) == 110, "Group-age rate shape changed")
    by_group: dict[tuple[str, str], list[tuple[str, int, int]]] = defaultdict(list)
    for dimension, group, age_id, population, events, rate, low, high in age_rows:
        n = int(population)
        x = int(events)
        require(close(rate, 100000.0 * x / n), f"Age-specific group rate changed: {dimension} {group} {age_id}")
        require(close(low, wilson(x, n, 100000.0, False)) and close(high, wilson(x, n, 100000.0, True)), f"Group interval changed: {dimension} {group} {age_id}")
        by_group[(dimension, group)].append((age_id, n, x))

    standardized_rows = connection.execute(
        "SELECT equity_dimension, group_id, direct_standardized_rate_per_100k, direct_rate_low_95, direct_rate_high_95, support_state FROM standardized_group_rates ORDER BY equity_dimension, group_order"
    ).fetchall()
    require(len(standardized_rows) == 22, "Standardized group rate shape changed")
    standardized: dict[tuple[str, str], tuple[float, float, float]] = {}
    for dimension, group, rate, low, high, state in standardized_rows:
        rows = by_group[(dimension, group)]
        expected = 100000.0 * sum((events / population) * standards[age_id] for age_id, population, events in rows)
        variance = 100000.0 * 100000.0 * sum(
            standards[age_id] ** 2 * (events / population) * (1 - events / population) / population
            for age_id, population, events in rows
        )
        expected_low = max(0.0, expected - 1.959963984540054 * math.sqrt(variance))
        expected_high = expected + 1.959963984540054 * math.sqrt(variance)
        require(close(rate, expected) and close(low, expected_low) and close(high, expected_high), f"Direct group standardization changed: {dimension} {group}")
        require(state in {"supported_for_synthetic_comparison", "missingness_audit_only", "overall_reported_reference"}, f"Unexpected group support state: {dimension} {group}")
        standardized[(dimension, group)] = (float(rate), float(low), float(high))

    primary_refs = {
        row[0]: row[1]
        for row in connection.execute("SELECT equity_dimension, group_id FROM standardized_group_rates WHERE primary_reference = 1")
    }
    comparisons = connection.execute(
        "SELECT equity_dimension, group_id, reference_choice, reference_group_id, rate_difference_per_100k, rate_ratio FROM disparity_comparisons ORDER BY equity_dimension, reference_choice, group_id"
    ).fetchall()
    require(len(comparisons) == 32 and len(primary_refs) == 3, "Reference comparison shape changed")
    comparison_map: dict[tuple[str, str], list[tuple[str, float, float]]] = defaultdict(list)
    for dimension, group, choice, reference_group, difference, ratio in comparisons:
        expected_reference = primary_refs[dimension] if choice == "predeclared_group" else "overall_reported"
        require(reference_group == expected_reference, f"Reference group changed: {dimension} {choice}")
        group_rate = standardized[(dimension, group)][0]
        reference_rate = standardized[(dimension, reference_group)][0]
        require(close(difference, group_rate - reference_rate) and close(ratio, group_rate / reference_rate), f"Disparity comparison changed: {dimension} {group} {choice}")
        comparison_map[(dimension, choice)].append((group, float(difference), float(ratio)))

    summaries = connection.execute(
        "SELECT equity_dimension, reference_choice, comparison_groups, summary_absolute_rate_difference_per_100k, summary_rate_ratio FROM summary_disparities ORDER BY equity_dimension, reference_choice"
    ).fetchall()
    require(len(summaries) == 6, "Summary disparity shape changed")
    for dimension, choice, count, difference, ratio in summaries:
        values = comparison_map[(dimension, choice)]
        if choice == "predeclared_group":
            values = [value for value in values if value[0] != primary_refs[dimension]]
        expected_difference = sum(abs(value[1]) for value in values) / len(values)
        expected_ratio = sum(value[2] if value[2] >= 1 else 1 / value[2] for value in values) / len(values)
        require(int(count) == len(values) and close(difference, expected_difference) and close(ratio, expected_ratio), f"Summary disparity changed: {dimension} {choice}")

    missing_columns = {
        "race": "race_missing_count",
        "ethnicity": "ethnicity_missing_count",
        "primary_language": "primary_language_missing_count",
        "disability_status": "disability_status_missing_count",
        "tract_geography": "tract_geography_missing_count",
    }
    missingness = {}
    for field, column in missing_columns.items():
        expected = connection.execute(f"SELECT SUM(CAST({column} AS INTEGER)) FROM raw_field_completeness").fetchone()[0]
        observed = connection.execute("SELECT missing_records FROM missingness_audit WHERE field_id = ?", (field,)).fetchone()[0]
        require(int(observed) == int(expected), f"Missingness audit changed: {field}")
        missingness[field] = int(observed)
    require(missingness["tract_geography"] == 0 and all(missingness[field] > 0 for field in missingness if field != "tract_geography"), "Missingness truth pattern changed")

    representation = connection.execute("SELECT equity_dimension, SUM(population_share), SUM(event_share) FROM representation_audit GROUP BY equity_dimension").fetchall()
    require(len(representation) == 3 and all(close(row[1], 1.0) and close(row[2], 1.0) for row in representation), "Representation shares do not reconcile")

    raw_groups: dict[tuple[str, str], list[tuple[str, int, int, int]]] = defaultdict(list)
    for tract, dimension, group, order, population, events in connection.execute(
        "SELECT tract_fips, equity_dimension, group_id, group_order, population_count, synthetic_event_count FROM tract_group_base ORDER BY tract_fips, equity_dimension, group_order"
    ):
        raw_groups[(tract, dimension)].append((group, int(order), int(population), int(events)))
    published = {
        (row[0], row[1], row[2]): row[3:]
        for row in connection.execute(
            "SELECT tract_fips, equity_dimension, group_id, support_state, published_population_count, published_synthetic_event_count, published_crude_rate_per_100k FROM published_tract_group_rates"
        )
    }
    primary_count = 0
    complementary_count = 0
    publishable_count = 0
    for key, groups in raw_groups.items():
        primary = {group for group, _, population, events in groups if events < 16 or population < 100}
        complement = None
        if len(primary) == 1:
            candidates = [value for value in groups if value[0] not in primary]
            complement = min(candidates, key=lambda value: (value[3], value[2], value[1]))[0]
        for group, _, population, events in groups:
            state, published_population, published_events, published_rate = published[(key[0], key[1], group)]
            expected_state = "primary_suppressed" if group in primary else ("complementary_suppressed" if group == complement else "publishable")
            require(state == expected_state, f"Suppression state changed: {key} {group}")
            if expected_state == "publishable":
                require(int(published_population) == population and int(published_events) == events and close(published_rate, 100000.0 * events / population), f"Published rate changed: {key} {group}")
                publishable_count += 1
            else:
                require(published_population is None and published_events is None and published_rate is None, f"Suppressed value exposed: {key} {group}")
                primary_count += expected_state == "primary_suppressed"
                complementary_count += expected_state == "complementary_suppressed"
    require(len(published) == 30343, "Published tract-group output shape changed")
    suppression_audits = connection.execute("SELECT COUNT(*), SUM(CASE WHEN status <> 'pass' THEN 1 ELSE 0 END) FROM complementary_suppression_audit").fetchone()
    require(suppression_audits == (4791, 0), "Complementary suppression audit failed")
    require(connection.execute("SELECT COUNT(*) FROM bias_register").fetchone()[0] == 8, "Bias register shape changed")

    highest = max(
        (row for row in standardized_rows if row[5] == "supported_for_synthetic_comparison"),
        key=lambda row: float(row[2]),
    )
    return {
        "query_checks": len(checks),
        "failed_query_checks": 0,
        "source_reconciliation_checks": len(reconciliations),
        "failed_source_reconciliation_checks": 0,
        "margin_rows": 151715,
        "completeness_rows": 7985,
        "group_age_rates": len(age_rows),
        "standardized_group_rates": len(standardized_rows),
        "disparity_comparisons": len(comparisons),
        "summary_disparities": len(summaries),
        "missingness": missingness,
        "representation_rows": 19,
        "published_tract_group_rows": len(published),
        "primary_suppressed_cells": primary_count,
        "complementary_suppressed_cells": complementary_count,
        "publishable_cells": publishable_count,
        "highest_supported_group": {"dimension": highest[0], "group_id": highest[1], "rate_per_100k": float(highest[2])},
        "bias_register_rows": 8,
    }


def build(root: Path, sql_root: Path, output_root: Path) -> dict[str, object]:
    import freeze_upstream
    import generate_equity_layer

    root = root.resolve()
    sql_root = sql_root.resolve()
    output_root = output_root.resolve()
    if output_root.exists() and any(output_root.iterdir()):
        raise FileExistsError(f"Refusing to overwrite nonempty output target: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)
    handoff = freeze_upstream.verify(root)
    source = generate_equity_layer.verify(root)
    with tempfile.TemporaryDirectory(prefix="app5-module03-db-") as temp_dir:
        connection = sqlite3.connect(Path(temp_dir) / "disparities.sqlite")
        connection.create_function("SQRT", 1, math.sqrt)
        connection.create_function("WILSON_LOW", 3, lambda x, n, m: wilson(x, n, m, False))
        connection.create_function("WILSON_HIGH", 3, lambda x, n, m: wilson(x, n, m, True))
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
        "module_id": "oclc-app5-03",
        "module_version": "0.1.0",
        "commons_release": "0.89.0",
        "source_release": "fma-dp-01-equity-v1",
        "handoff": handoff,
        "source": source,
        "loaded": loaded,
        "sql_sha256": sql_hashes,
        "outputs": outputs,
        "findings": findings,
        "interpretation_status": "synthetic disparity and data-limit release only; no real disparity, mapping, ranking, targeting, allocation, intervention, community, implementation, or deployment conclusion",
    }
    (output_root / "build-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return report


def verify_committed(root: Path = ROOT) -> dict[str, object]:
    output_root = root.resolve() / "outputs"
    report = json.loads((output_root / "build-report.json").read_text(encoding="utf-8"))
    require(report["module_id"] == "oclc-app5-03" and report["module_version"] == "0.1.0" and report["commons_release"] == "0.89.0", "Committed build-report identity changed")
    require(report["source_release"] == "fma-dp-01-equity-v1", "Committed source release changed")
    for filename, metadata in report["outputs"].items():
        path = output_root / filename
        require(path.is_file() and path.stat().st_size == metadata["bytes"] and sha256(path) == metadata["sha256"], f"Committed output identity changed: {filename}")
    findings = report["findings"]
    require(findings["query_checks"] == 36 and findings["failed_query_checks"] == 0, "Committed query checks changed")
    return {
        "outputs": len(report["outputs"]),
        "margin_rows": findings["margin_rows"],
        "group_age_rates": findings["group_age_rates"],
        "disparity_comparisons": findings["disparity_comparisons"],
        "published_tract_group_rows": findings["published_tract_group_rows"],
        "primary_suppressed_cells": findings["primary_suppressed_cells"],
        "complementary_suppressed_cells": findings["complementary_suppressed_cells"],
        "query_checks": findings["query_checks"],
    }


def self_check() -> None:
    committed = verify_committed(ROOT)
    with tempfile.TemporaryDirectory(prefix="app5-module03-disparities-") as temp_dir:
        base = Path(temp_dir)
        first = build(ROOT, ROOT / "reference/sql", base / "first")
        second = build(ROOT, ROOT / "reference/sql", base / "second")
        require(first["findings"] == second["findings"] and first["outputs"] == second["outputs"], "Two disparity builds differ")
        for filename in first["outputs"]:
            require((base / "first" / filename).read_bytes() == (base / "second" / filename).read_bytes(), f"Two disparity outputs differ: {filename}")
            require((base / "first" / filename).read_bytes() == (ROOT / "outputs" / filename).read_bytes(), f"Committed disparity output differs: {filename}")
        try:
            build(ROOT, ROOT / "reference/sql", base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Disparity builder did not protect a nonempty target")
    print(f"APP-5 Module 03 disparity-builder self-check passed: {json.dumps(committed, sort_keys=True)}")


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
        parser.exit(1, f"Disparity build failed: {error}\n")


if __name__ == "__main__":
    main()
