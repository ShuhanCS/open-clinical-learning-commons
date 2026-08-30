"""Build the APP-3 Module 02 clean operational measure release with SQLite."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import sqlite3
import statistics
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SQL_FILES = (
    "01-clean-operational-sources.sql", "02-encounter-measures.sql",
    "03-operational-measures.sql", "04-validation-and-defects.sql",
)
OUTPUT_TABLES = {
    "source-reconciliation.csv": "source_reconciliation",
    "encounter-measures.csv.gz": "encounter_measures",
    "shift-metrics.csv": "shift_metrics",
    "weekly-metrics.csv": "weekly_metrics",
    "safety-diagnostics.csv": "safety_diagnostics",
    "subgroup-support.csv": "subgroup_support",
    "defect-impact.csv": "defect_impact",
    "query-checks.csv": "query_checks",
}


class BuildError(RuntimeError):
    pass


class Median:
    def __init__(self) -> None:
        self.values: list[float] = []

    def step(self, value: object) -> None:
        if value is not None and str(value) != "":
            self.values.append(float(value))

    def finalize(self) -> float | None:
        return round(statistics.median(self.values), 3) if self.values else None


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
        return str(round(value, 6))
    return str(value)


def query_csv(connection: sqlite3.Connection, table: str) -> tuple[bytes, int, int]:
    cursor = connection.execute(f'SELECT * FROM "{table}"')
    fields = [description[0] for description in cursor.description or []]
    rows = cursor.fetchall()
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(fields)
    for row in rows:
        writer.writerow([format_value(value) for value in row])
    return output.getvalue().encode("utf-8"), len(rows), len(fields)


def load_raw(connection: sqlite3.Connection, root: Path) -> dict[str, int]:
    manifest_path = root / "data/operational-source-manifest.csv"
    with manifest_path.open(encoding="utf-8", newline="") as handle:
        manifest = list(csv.DictReader(handle))
    if len(manifest) != 9:
        raise BuildError("Expected nine raw source tables")
    counts = {}
    for source in manifest:
        relative = source["relative_path"]
        path = root / relative
        with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
            reader = csv.reader(handle)
            fields = next(reader)
            table = "raw_" + Path(relative).name.removesuffix(".csv.gz").replace("-", "_")
            connection.execute(f'DROP TABLE IF EXISTS "{table}"')
            columns = ", ".join(f'"{field}" TEXT' for field in fields)
            connection.execute(f'CREATE TABLE "{table}" ({columns})')
            placeholders = ", ".join("?" for _ in fields)
            batch = []
            count = 0
            for row in reader:
                batch.append(row)
                count += 1
                if len(batch) == 5000:
                    connection.executemany(f'INSERT INTO "{table}" VALUES ({placeholders})', batch)
                    batch.clear()
            if batch:
                connection.executemany(f'INSERT INTO "{table}" VALUES ({placeholders})', batch)
            if count != int(source["rows"]) or len(fields) != int(source["columns"]):
                raise BuildError(f"Loaded shape mismatch: {table}")
            counts[table] = count
    return counts


def execute_sql(connection: sqlite3.Connection, sql_root: Path) -> dict[str, str]:
    hashes = {}
    for filename in SQL_FILES:
        path = sql_root / filename
        if not path.is_file():
            raise BuildError(f"Missing SQL file: {filename}")
        text = path.read_text(encoding="utf-8")
        if "REPLACE" in text:
            raise BuildError(f"Incomplete SQL file: {filename}")
        connection.executescript(text)
        hashes[filename] = sha256(path)
    return hashes


def exact_findings(connection: sqlite3.Connection) -> dict[str, object]:
    checks = connection.execute("SELECT check_id, check_name, observed_value, expected_value FROM query_checks ORDER BY check_id").fetchall()
    failed = [row for row in checks if str(row[2]) != str(row[3])]
    if failed:
        raise BuildError(f"Query checks failed: {failed[:3]}")
    overall = connection.execute("SELECT completed_encounters, known_true_events, trigger_true_positives, incident_true_positives, trigger_false_positives, trigger_sensitivity_percent, incident_capture_percent, trigger_specificity_percent FROM safety_diagnostics WHERE event_class = 'overall'").fetchone()
    totals = connection.execute("SELECT COUNT(*), SUM(completed_flag), SUM(left_before_seen_flag), SUM(return_within_72h_flag), SUM(clinician_available_flag), SUM(valid_event_sequence_flag) FROM encounter_measures").fetchone()
    medians = connection.execute("SELECT median(arrival_to_triage_minutes), median(arrival_to_clinician_minutes), median(arrival_to_departure_minutes) FROM encounter_measures").fetchone()
    shifts = connection.execute("SELECT COUNT(*), SUM(arrivals), SUM(completed_encounters), ROUND(SUM(overtime_hours), 3), MAX(max_queue_end) FROM shift_metrics").fetchone()
    return {
        "accepted_encounters": totals[0], "completed_encounters": totals[1],
        "left_before_seen": totals[2], "return_within_72h": totals[3],
        "clinician_time_available": totals[4], "valid_event_sequences": totals[5],
        "median_arrival_to_triage_minutes": medians[0],
        "median_arrival_to_clinician_minutes": medians[1],
        "median_arrival_to_departure_minutes": medians[2],
        "shift_rows": shifts[0], "shift_arrivals": shifts[1],
        "shift_completed_encounters": shifts[2], "overtime_hours": shifts[3],
        "maximum_queue_end": shifts[4],
        "safety": {
            "eligible_completed_encounters": overall[0], "known_true_events": overall[1],
            "trigger_true_positives": overall[2], "incident_true_positives": overall[3],
            "trigger_false_positives": overall[4], "trigger_sensitivity_percent": overall[5],
            "incident_capture_percent": overall[6], "trigger_specificity_percent": overall[7],
        },
        "query_checks": len(checks), "failed_query_checks": len(failed),
    }


def build(root: Path, sql_root: Path, output_root: Path) -> dict[str, object]:
    import generate_operational_release

    root = root.resolve()
    sql_root = sql_root.resolve()
    output_root = output_root.resolve()
    if output_root.exists() and any(output_root.iterdir()):
        raise FileExistsError(f"Refusing to overwrite nonempty output target: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)
    source_summary = generate_operational_release.verify(root)
    with tempfile.TemporaryDirectory(prefix="app3-module02-db-") as temp_dir:
        database = Path(temp_dir) / "operational.db"
        connection = sqlite3.connect(database)
        connection.create_aggregate("median", 1, Median)
        try:
            loaded = load_raw(connection, root)
            sql_hashes = execute_sql(connection, sql_root)
            findings = exact_findings(connection)
            outputs = {}
            for filename, table in OUTPUT_TABLES.items():
                raw, rows, columns = query_csv(connection, table)
                value = deterministic_gzip(raw) if filename.endswith(".gz") else raw
                path = output_root / filename
                path.write_bytes(value)
                outputs[filename] = {
                    "rows": rows, "columns": columns, "bytes": len(value),
                    "sha256": sha256_bytes(value),
                    "raw_bytes": len(raw), "raw_sha256": sha256_bytes(raw),
                }
        finally:
            connection.close()
    report = {
        "schema_version": "1.0.0", "module_id": "oclc-app3-02",
        "module_version": "0.1.0", "commons_release": "0.67.0",
        "source_release": "cgh-ed-01-operational-v1",
        "source_manifest_sha256": sha256(root / "data/operational-source-manifest.csv"),
        "source_summary": source_summary, "loaded_rows": loaded,
        "sql_sha256": sql_hashes, "outputs": outputs, "findings": findings,
        "interpretation_status": "measure release only; no bottleneck, staffing, causal, clinical, or implementation conclusion",
    }
    (output_root / "build-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return report


def verify_committed(root: Path = ROOT) -> dict[str, object]:
    output_root = root / "outputs"
    report = json.loads((output_root / "build-report.json").read_text(encoding="utf-8"))
    if report["module_id"] != "oclc-app3-02" or report["commons_release"] != "0.67.0":
        raise BuildError("Committed build-report identity mismatch")
    for filename, metadata in report["outputs"].items():
        path = output_root / filename
        if not path.is_file() or path.stat().st_size != metadata["bytes"] or sha256(path) != metadata["sha256"]:
            raise BuildError(f"Committed output identity mismatch: {filename}")
    return {"outputs": len(report["outputs"]), "accepted_encounters": report["findings"]["accepted_encounters"], "query_checks": report["findings"]["query_checks"]}


def self_check() -> None:
    committed = verify_committed()
    with tempfile.TemporaryDirectory(prefix="app3-module02-build-") as temp_dir:
        base = Path(temp_dir)
        first = build(ROOT, ROOT / "reference/sql", base / "first")
        second = build(ROOT, ROOT / "reference/sql", base / "second")
        if first["outputs"] != second["outputs"] or first["findings"] != second["findings"]:
            raise AssertionError("Two independent measure builds differ")
        for filename in first["outputs"]:
            if (base / "first" / filename).read_bytes() != (ROOT / "outputs" / filename).read_bytes():
                raise AssertionError(f"Regenerated output differs: {filename}")
        try:
            build(ROOT, ROOT / "reference/sql", base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect a nonempty output target")
    print(f"APP-3 Module 02 measure-builder self-check passed: {json.dumps(committed, sort_keys=True)}")


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
            sql_root = args.sql_root or (args.root / "reference/sql")
            output_root = args.output_root or (args.root / "outputs")
            print(json.dumps(build(args.root, sql_root, output_root), indent=2))
        else:
            print(json.dumps(verify_committed(args.root.resolve()), indent=2))
    except (OSError, ValueError, KeyError, sqlite3.Error, BuildError) as error:
        parser.exit(1, f"Measure build failed: {error}\n")


if __name__ == "__main__":
    main()
