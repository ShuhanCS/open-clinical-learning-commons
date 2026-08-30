"""Run named read-only SQL blocks and write one CSV per query."""

from __future__ import annotations

import argparse
import csv
import sqlite3
import tempfile
from pathlib import Path


def parse_queries(path: Path) -> list[tuple[str, str]]:
    queries: list[tuple[str, str]] = []
    name: str | None = None
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("-- query: "):
            if name is not None:
                queries.append((name, "\n".join(lines).strip()))
            name = line.removeprefix("-- query: ").strip()
            lines = []
        elif name is not None:
            lines.append(line)
    if name is not None:
        queries.append((name, "\n".join(lines).strip()))
    if not queries or any(not name or not sql for name, sql in queries):
        raise ValueError("SQL must contain nonempty '-- query: name' blocks.")
    if len({name for name, _ in queries}) != len(queries):
        raise ValueError("Query names must be unique.")
    for name, sql in queries:
        if not name.replace("-", "").isalnum():
            raise ValueError(f"Unsafe query name: {name}")
        if not sql.lstrip().upper().startswith(("SELECT", "WITH")):
            raise ValueError(f"Query {name} must be read-only SELECT or WITH SQL.")
        if ";" in sql.rstrip(";"):
            raise ValueError(f"Query {name} must contain one statement.")
    return queries


def run(database: Path, sql_path: Path, output_dir: Path) -> dict[str, int]:
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(f"Refusing to overwrite nonempty output directory: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    counts: dict[str, int] = {}
    for name, sql in parse_queries(sql_path):
        cursor = connection.execute(sql)
        fields = [item[0] for item in cursor.description]
        rows = cursor.fetchall()
        with (output_dir / f"{name}.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(fields)
            writer.writerows(rows)
        counts[name] = len(rows)
    connection.close()
    return counts


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-module02-query-") as temp_dir:
        root = Path(temp_dir)
        database = root / "test.sqlite"
        connection = sqlite3.connect(database)
        connection.execute("CREATE TABLE demo (id INTEGER PRIMARY KEY, value TEXT NOT NULL)")
        connection.executemany("INSERT INTO demo VALUES (?, ?)", [(1, "a"), (2, "b")])
        connection.commit()
        connection.close()
        sql_path = root / "queries.sql"
        sql_path.write_text("-- query: demo-rows\nSELECT id, value FROM demo ORDER BY id;\n", encoding="utf-8")
        counts = run(database, sql_path, root / "outputs")
        assert counts == {"demo-rows": 2}
        try:
            run(database, sql_path, root / "outputs")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Query runner did not protect existing outputs.")
    print("FND-1 Module 02 query-runner self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path)
    parser.add_argument("--sql", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.database or not args.sql or not args.output_dir:
        parser.error("--database, --sql, and --output-dir are required")
    try:
        counts = run(args.database, args.sql, args.output_dir)
    except (FileExistsError, OSError, sqlite3.Error, ValueError) as exc:
        parser.exit(1, f"Query run failed: {exc}\n")
    print("Query run passed: " + ", ".join(f"{name}={count}" for name, count in counts.items()))


if __name__ == "__main__":
    main()
