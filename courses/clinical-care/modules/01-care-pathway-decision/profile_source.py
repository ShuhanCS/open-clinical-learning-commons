"""Profile the pinned Synthea source for the APP-1 care-pathway decision."""

from __future__ import annotations

import argparse
import csv
import sqlite3
import tempfile
from pathlib import Path


FIELDS = ["metric_id", "metric", "value", "unit", "rule", "decision_use"]
EXPECTED = {
    "F01": "1171", "F02": "518", "F03": "8", "F04": "25", "F05": "485",
    "F06": "129", "F07": "87", "F08": "25", "F09": "62", "F10": "64",
    "F11": "not ready",
}
QUERY = """
WITH eligible AS (
  SELECT e.*, p.birthdate, p.deathdate,
         CAST(strftime('%Y', e.start) AS INTEGER)
         - CAST(strftime('%Y', p.birthdate) AS INTEGER)
         - CASE WHEN strftime('%m-%d', e.start) < strftime('%m-%d', p.birthdate) THEN 1 ELSE 0 END AS age
  FROM encounters e
  JOIN patients p ON p.id = e.patient
  WHERE e.encounterclass IN ('emergency', 'inpatient')
    AND e.start >= '2010-01-01T00:00:00Z'
    AND e.start < '2019-04-01T00:00:00Z'
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY patient ORDER BY start, id) AS rn
  FROM eligible
  WHERE age >= 18
), cohort AS (
  SELECT * FROM ranked WHERE rn = 1
), pathway AS (
  SELECT c.patient, c.organization,
         CASE WHEN c.deathdate IS NOT NULL
                    AND julianday(c.deathdate) > julianday(c.stop)
                    AND julianday(c.deathdate) <= julianday(c.stop) + 30
              THEN 1 ELSE 0 END AS early_death,
         EXISTS(
           SELECT 1 FROM encounters a
           WHERE a.patient = c.patient
             AND julianday(a.start) > julianday(c.stop)
             AND julianday(a.start) <= julianday(c.stop) + 30
             AND a.encounterclass IN ('emergency', 'inpatient')
         ) AS early_acute,
         EXISTS(
           SELECT 1 FROM encounters f
           WHERE f.patient = c.patient
             AND julianday(f.start) > julianday(c.stop)
             AND julianday(f.start) <= julianday(c.stop) + 30
             AND f.encounterclass IN ('ambulatory', 'outpatient', 'wellness')
         ) AS followup,
         EXISTS(
           SELECT 1 FROM encounters a
           WHERE a.patient = c.patient
             AND julianday(a.start) > julianday(c.stop) + 30
             AND julianday(a.start) <= julianday(c.stop) + 365
             AND a.encounterclass IN ('emergency', 'inpatient')
         ) AS outcome
  FROM cohort c
)
SELECT
  (SELECT COUNT(*) FROM patients) AS source_people,
  COUNT(*) AS initial_cohort,
  SUM(early_death) AS early_deaths,
  SUM(early_acute) AS early_acute_returns,
  SUM(CASE WHEN early_death = 0 AND early_acute = 0 THEN 1 ELSE 0 END) AS landmark_eligible,
  SUM(CASE WHEN early_death = 0 AND early_acute = 0 THEN followup ELSE 0 END) AS scheduled_followup,
  SUM(CASE WHEN early_death = 0 AND early_acute = 0 THEN outcome ELSE 0 END) AS later_returns,
  SUM(CASE WHEN early_death = 0 AND early_acute = 0 AND followup = 1 THEN outcome ELSE 0 END) AS exposed_returns,
  SUM(CASE WHEN early_death = 0 AND early_acute = 0 AND followup = 0 THEN outcome ELSE 0 END) AS unexposed_returns,
  COUNT(DISTINCT CASE WHEN early_death = 0 AND early_acute = 0 THEN organization END) AS organizations
FROM pathway
"""


def profile(connection: sqlite3.Connection) -> list[dict[str, str]]:
    required = {"patients", "encounters"}
    tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    if not required <= tables:
        raise ValueError("Database must contain patients and encounters tables")
    row = connection.execute(QUERY).fetchone()
    if row is None:
        raise ValueError("Feasibility query returned no row")
    values = [str(value or 0) for value in row]
    facts = (
        ("F01", "source synthetic people", values[0], "people", "all rows in patients", "confirms full source population"),
        ("F02", "initial adult index cohort", values[1], "people", "first emergency or inpatient encounter age 18 or older from 2010-01-01 through 2019-03-31", "defines pathway entry"),
        ("F03", "early deaths", values[2], "people", "death after discharge and through day 30", "remains visible and is excluded from landmark"),
        ("F04", "early acute returns", values[3], "people", "emergency or inpatient return after discharge and through day 30", "remains visible and is excluded from landmark"),
        ("F05", "day-30 landmark eligible", values[4], "people", "alive and without an early acute return through day 30", "defines comparison risk set"),
        ("F06", "scheduled follow-up", values[5], "people", "ambulatory outpatient or wellness encounter after discharge and through day 30", "defines exposure at landmark"),
        ("F07", "later acute returns", values[6], "events", "first emergency or inpatient return after day 30 and through day 365", "primary time-to-event outcome count"),
        ("F08", "exposed later acute returns", values[7], "events", "later acute return among scheduled follow-up group", "requires later adjusted comparison"),
        ("F09", "unexposed later acute returns", values[8], "events", "later acute return among no-scheduled-follow-up group", "requires later adjusted comparison"),
        ("F10", "distinct index organizations", values[9], "organizations", "organizations among landmark-eligible people", "too sparse for raw organization ranking"),
        ("F11", "raw site comparison readiness", "not ready", "status", f"{values[9]} sparse source organizations", "requires deterministic six-site teaching extension in Module 02"),
    )
    return [dict(zip(FIELDS, fact, strict=True)) for fact in facts]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing output: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app1-profile-") as temp_dir:
        database = Path(temp_dir) / "fixture.sqlite"
        connection = sqlite3.connect(database)
        connection.executescript("""
            CREATE TABLE patients (id TEXT PRIMARY KEY, birthdate TEXT NOT NULL, deathdate TEXT);
            CREATE TABLE encounters (id TEXT PRIMARY KEY, start TEXT NOT NULL, stop TEXT NOT NULL, patient TEXT NOT NULL, organization TEXT NOT NULL, encounterclass TEXT NOT NULL);
            INSERT INTO patients VALUES
              ('p1','1980-01-01',NULL),('p2','1980-01-01',NULL),
              ('p3','1980-01-01','2018-01-20'),('p4','1980-01-01',NULL);
            INSERT INTO encounters VALUES
              ('i1','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p1','o1','inpatient'),
              ('f1','2018-01-10T00:00:00Z','2018-01-10T01:00:00Z','p1','o1','outpatient'),
              ('a1','2018-02-15T00:00:00Z','2018-02-15T01:00:00Z','p1','o1','emergency'),
              ('i2','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p2','o1','inpatient'),
              ('a2','2018-01-15T00:00:00Z','2018-01-15T01:00:00Z','p2','o1','emergency'),
              ('i3','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p3','o2','inpatient'),
              ('i4','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p4','o2','inpatient');
        """)
        rows = profile(connection)
        connection.close()
        values = {row["metric_id"]: row["value"] for row in rows}
        assert values == {
            "F01": "4", "F02": "4", "F03": "1", "F04": "1", "F05": "2",
            "F06": "1", "F07": "1", "F08": "1", "F09": "0", "F10": "2",
            "F11": "not ready",
        }
        output = Path(temp_dir) / "profile.csv"
        write_csv(output, rows)
        assert len(list(csv.DictReader(output.open(encoding="utf-8")))) == 11
        try:
            write_csv(output, rows)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Profiler overwrote an existing output")
    print("APP-1 Module 01 source profiler self-check passed: landmark, early-event, exposure, outcome, and overwrite rules.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database", nargs="?", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.database or not args.output:
        parser.error("database and --output are required unless --self-check is used")
    connection = sqlite3.connect(f"file:{args.database.resolve().as_posix()}?mode=ro", uri=True)
    try:
        rows = profile(connection)
    finally:
        connection.close()
    values = {row["metric_id"]: row["value"] for row in rows}
    if values != EXPECTED:
        raise SystemExit(f"Reference source profile changed: {values}")
    write_csv(args.output.resolve(), rows)
    print("APP-1 Module 01 source profile passed: 11 registered feasibility facts.")


if __name__ == "__main__":
    main()
