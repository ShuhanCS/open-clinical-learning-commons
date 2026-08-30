"""Build the FND-1 Module 03 reference cohort outputs from a Module 02 database."""

from __future__ import annotations

import argparse
import csv
import hashlib
import sqlite3
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
SQL_DIR = MODULE_ROOT / "sql"
QUERIES = {
    "eligible-events": "01-eligible-events.sql",
    "index-cohort": "02-index-cohort.sql",
    "analytic-table": "03-analytic-table.sql",
    "query-checks": "04-validation.sql",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_query(path: Path) -> str:
    sql = path.read_text(encoding="utf-8").strip()
    first = sql.lstrip("- \r\n").lower()
    if not sql.endswith(";") or "with " not in first[:200]:
        raise ValueError(f"Expected one read-only WITH query: {path}")
    forbidden = ("insert ", "update ", "delete ", "drop ", "alter ", "attach ", "pragma ")
    lowered = " " + " ".join(line.split("--", 1)[0] for line in sql.lower().splitlines())
    if any(token in lowered for token in forbidden):
        raise ValueError(f"Query contains a write or database-control statement: {path}")
    return sql


def write_rows(path: Path, columns: list[str], rows: list[tuple[object, ...]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)


def build(database: Path, target: Path, sql_dir: Path = SQL_DIR) -> dict[str, dict[str, object]]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    target.mkdir(parents=True)
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    results: dict[str, dict[str, object]] = {}
    try:
        for name, filename in QUERIES.items():
            cursor = connection.execute(read_query(sql_dir / filename))
            columns = [item[0] for item in cursor.description]
            rows = cursor.fetchall()
            output = target / f"{name}.csv"
            write_rows(output, columns, rows)
            results[name] = {"rows": len(rows), "bytes": output.stat().st_size, "sha256": sha256(output)}

        checks = {
            row["check_name"]: int(row["observed_value"])
            for row in csv.DictReader((target / "query-checks.csv").open(encoding="utf-8", newline=""))
        }
        flow = [
            (1, checks["source patients"], 0, checks["source patients"], "All source patients"),
            (2, checks["source patients"], checks["patients without an acute event"], checks["patients with any acute event"], "Has emergency or inpatient encounter in index period"),
            (3, checks["patients with any acute event"], checks["patients with only under-18 acute events"], checks["included adult patients"], "Has at least one qualifying event at age 18 or older"),
            (4, checks["included adult patients"], 0, checks["included adult patients"], "Select first eligible event per patient"),
        ]
        flow_path = target / "cohort-flow.csv"
        write_rows(flow_path, ["step", "starting", "excluded", "remaining", "rule"], flow)
        results["cohort-flow"] = {"rows": len(flow), "bytes": flow_path.stat().st_size, "sha256": sha256(flow_path)}
    except Exception:
        # Preserve the new target for diagnosis; never overwrite or hide partial evidence.
        raise
    finally:
        connection.close()
    return results


def self_check() -> None:
    for filename in QUERIES.values():
        assert read_query(SQL_DIR / filename).endswith(";")
    with tempfile.TemporaryDirectory(prefix="fnd1-module03-build-") as temp_dir:
        target = Path(temp_dir)
        try:
            build(Path("missing.sqlite"), target)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target.")
    print("FND-1 Module 03 builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, help="Accepted Module 02 SQLite database")
    parser.add_argument("--target", type=Path, help="New output directory")
    parser.add_argument("--sql-dir", type=Path, default=SQL_DIR, help="Directory containing the four SQL files")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.database or not args.target:
        parser.error("--database and --target are required")
    try:
        results = build(args.database.resolve(), args.target.resolve(), args.sql_dir.resolve())
    except (OSError, ValueError, sqlite3.Error) as exc:
        parser.exit(1, f"Build failed: {exc}\n")
    print(
        "FND-1 Module 03 build passed: "
        f"{results['eligible-events']['rows']} eligible events, "
        f"{results['analytic-table']['rows']} analytic rows, and "
        f"{results['query-checks']['rows']} query checks."
    )


if __name__ == "__main__":
    main()
