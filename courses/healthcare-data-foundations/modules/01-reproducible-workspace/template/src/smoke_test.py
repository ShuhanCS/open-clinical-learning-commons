"""Run the FND-1 Python and SQLite workspace smoke test."""

from __future__ import annotations

import csv
import json
import sqlite3
import sys
from pathlib import Path


EXPECTED_COLUMNS = ["record_id", "source_label", "event_count"]
EXPECTED_RESULT = {
    "row_count": 3,
    "event_count_total": 15,
    "event_count_minimum": 3,
    "event_count_maximum": 7,
}


def run_smoke_test(root: Path) -> dict[str, object]:
    """Load CSV rows, execute the supplied SQL, and return checked facts."""
    data_path = root / "data" / "workspace_smoke_test.csv"
    sql_path = root / "sql" / "00-smoke-test.sql"
    if not data_path.is_file() or not sql_path.is_file():
        raise FileNotFoundError("Run from a complete Module 01 learner workspace.")

    with data_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Unexpected columns: {reader.fieldnames}")
        rows = list(reader)

    if len(rows) != 3:
        raise ValueError(f"Expected 3 smoke-test rows; found {len(rows)}.")
    if len({row["record_id"] for row in rows}) != len(rows):
        raise ValueError("record_id must be unique.")

    typed_rows = []
    for row in rows:
        event_count = int(row["event_count"])
        if event_count < 0:
            raise ValueError("event_count must be nonnegative.")
        typed_rows.append((row["record_id"], row["source_label"], event_count))

    with sqlite3.connect(":memory:") as connection:
        connection.executescript(sql_path.read_text(encoding="utf-8"))
        connection.executemany(
            "INSERT INTO workspace_smoke VALUES (?, ?, ?)",
            typed_rows,
        )
        row = connection.execute(
            """
            SELECT COUNT(*), SUM(event_count), MIN(event_count), MAX(event_count)
            FROM workspace_smoke
            """
        ).fetchone()

    result = dict(zip(EXPECTED_RESULT, row, strict=True))
    if result != EXPECTED_RESULT:
        raise AssertionError(f"Smoke-test result changed: {result}")

    summary = {
        "status": "pass",
        "result": result,
        "environment": {
            "python": sys.version.split()[0],
            "sqlite": sqlite3.sqlite_version,
        },
    }
    output = root / "outputs" / "python-sql-smoke.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    summary = run_smoke_test(root)
    result = summary["result"]
    print(
        "WORKSPACE_SMOKE_TEST_PASS "
        f"rows={result['row_count']} total={result['event_count_total']}"
    )


if __name__ == "__main__":
    main()
