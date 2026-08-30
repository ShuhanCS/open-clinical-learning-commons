"""Build APP-1 Module 02 longitudinal and six-site teaching outputs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
import sys
import tempfile
from decimal import Decimal
from pathlib import Path
from statistics import median


MODULE_ROOT = Path(__file__).resolve().parent
SQL_DIR = MODULE_ROOT / "sql"
CONTRACT_PATH = MODULE_ROOT / "extension-contract.json"
DATABASE_BYTES = 141_234_176
DATABASE_SHA256 = "1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a"
QUERIES = {
    "index-cohort": "01-index-cohort.sql",
    "event-audit": "02-event-audit.sql",
    "longitudinal-cohort": "03-longitudinal-cohort.sql",
    "query-checks": "04-validation.sql",
}
REFERENCE_CHECKS = {
    "source people": 1171,
    "source encounters": 53346,
    "initial cohort": 518,
    "unique initial patients": 518,
    "index deaths": 9,
    "early deaths": 8,
    "early acute returns": 25,
    "branch overlaps": 0,
    "landmark eligible": 476,
    "scheduled followup": 129,
    "no scheduled followup": 347,
    "later acute returns": 87,
    "exposed later acute returns": 25,
    "unexposed later acute returns": 62,
    "administrative censored": 389,
    "competing death censored": 0,
    "later deaths recognized": 3,
    "source organizations": 64,
    "invalid index order": 0,
    "invalid followup time": 0,
    "invalid early acute time": 0,
    "invalid later acute time": 0,
    "landmark conservation": 518,
    "outcome conservation": 476,
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
    if not sql.endswith(";") or "with " not in first[:300]:
        raise ValueError(f"Expected one read-only WITH query: {path}")
    lowered = " " + " ".join(line.split("--", 1)[0] for line in sql.lower().splitlines())
    forbidden = (" insert ", " update ", " delete ", " drop ", " alter ", " attach ", " pragma ")
    if any(token in lowered for token in forbidden):
        raise ValueError(f"Query contains a write or database-control statement: {path}")
    return sql


def write_rows(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def file_record(path: Path) -> dict[str, object]:
    rows = read_rows(path) if path.suffix == ".csv" else []
    fields = len(rows[0]) if rows else (len(next(csv.reader(path.open(encoding="utf-8")))) if path.suffix == ".csv" else None)
    return {"rows": len(rows), "fields": fields, "bytes": path.stat().st_size, "sha256": sha256(path)}


def assign_sites(rows: list[dict[str, str]], contract: dict[str, object]) -> list[dict[str, object]]:
    eligible = [row for row in rows if row["landmark_eligible_flag"] == "1"]
    scores = {
        row["patient_id"]:
            int(row["age_at_index"])
            + 12 * int(row["prior_365d_acute_count"])
            + 3 * int(row["prior_365d_condition_count"])
            + 8 * (row["index_encounter_class"] == "inpatient")
        for row in eligible
    }
    ranked = sorted(
        eligible,
        key=lambda row: (
            scores[row["patient_id"]],
            hashlib.sha256(f"{contract['risk_rank_tie_break_seed']}|{row['patient_id']}".encode()).hexdigest(),
        ),
    )
    ranks = {row["patient_id"]: index + 1 for index, row in enumerate(ranked)}
    sites = list(contract["sites"])
    assignments: list[dict[str, object]] = []
    for row in eligible:
        rank = ranks[row["patient_id"]]
        tier = ("low", "medium", "high")[min(2, ((rank - 1) * 3) // len(eligible))]
        digest = hashlib.sha256(f"{contract['seed']}|{row['patient_id']}".encode()).digest()
        hash_prefix = digest[:8].hex()
        uniform = Decimal(int.from_bytes(digest[:8], "big")) / Decimal(2**64)
        probabilities = contract["probabilities"][tier]
        if sum(Decimal(probability) for probability in probabilities) != Decimal("1.00"):
            raise ValueError(f"Invalid site probability contract for {tier}")
        cumulative = Decimal("0")
        site = ""
        for candidate, probability in zip(sites, probabilities, strict=True):
            cumulative += Decimal(probability)
            if uniform < cumulative:
                site = candidate
                break
        if not site:
            raise ValueError(f"Site assignment failed for {row['patient_id']}")
        assignments.append({
            "patient_id": row["patient_id"],
            "baseline_risk_score": scores[row["patient_id"]],
            "baseline_risk_rank": rank,
            "baseline_risk_tier": tier,
            "assignment_hash_prefix": hash_prefix,
            "assignment_uniform": format(uniform, ".17f"),
            "teaching_site_id": site,
            "extension_seed": contract["seed"],
            "extension_version": contract["version"],
            "field_class": contract["field_class"],
        })
    return sorted(assignments, key=lambda row: str(row["patient_id"]))


def build(database: Path, target: Path, sql_dir: Path = SQL_DIR, enforce_reference: bool = True) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if not database.is_file():
        raise FileNotFoundError(f"Database not found: {database}")
    database_hash = sha256(database)
    if enforce_reference and (database.stat().st_size != DATABASE_BYTES or database_hash != DATABASE_SHA256):
        raise ValueError("Database does not match the accepted FND-1 source release")
    target.mkdir(parents=True)
    connection = sqlite3.connect(f"file:{database.resolve().as_posix()}?mode=ro", uri=True)
    try:
        for name, filename in QUERIES.items():
            cursor = connection.execute(read_query(sql_dir / filename))
            fields = [item[0] for item in cursor.description]
            rows = [dict(zip(fields, row, strict=True)) for row in cursor.fetchall()]
            write_rows(target / f"{name}.csv", fields, rows)
    finally:
        connection.close()

    checks = {row["check_name"]: int(row["observed_value"]) for row in read_rows(target / "query-checks.csv")}
    if enforce_reference:
        changed = {name: checks.get(name) for name, value in REFERENCE_CHECKS.items() if checks.get(name) != value}
        if changed:
            raise ValueError(f"Reference cohort checks changed: {changed}")

    flow = [
        {"step": 1, "state": "initial adult index cohort", "starting": checks["initial cohort"], "branched_or_excluded": 0, "remaining": checks["initial cohort"], "rule": "first qualifying adult acute encounter"},
        {"step": 2, "state": "index death", "starting": checks["initial cohort"], "branched_or_excluded": checks["index deaths"], "remaining": checks["initial cohort"] - checks["index deaths"], "rule": "death date on or before discharge date"},
        {"step": 3, "state": "early post-discharge death", "starting": checks["initial cohort"] - checks["index deaths"], "branched_or_excluded": checks["early deaths"], "remaining": checks["initial cohort"] - checks["index deaths"] - checks["early deaths"], "rule": "death date after discharge through day 30"},
        {"step": 4, "state": "early acute return", "starting": checks["initial cohort"] - checks["index deaths"] - checks["early deaths"], "branched_or_excluded": checks["early acute returns"], "remaining": checks["landmark eligible"], "rule": "first acute return after discharge through day 30"},
        {"step": 5, "state": "day-30 landmark risk set", "starting": checks["landmark eligible"], "branched_or_excluded": 0, "remaining": checks["landmark eligible"], "rule": "no index death early death or early acute return"},
    ]
    write_rows(target / "cohort-flow.csv", list(flow[0]), flow)

    longitudinal = read_rows(target / "longitudinal-cohort.csv")
    censor_rows: list[dict[str, object]] = []
    for exposure in ("1", "0"):
        for reason in ("event", "competing_death", "administrative_end"):
            group = [row for row in longitudinal if row["landmark_exposure"] == exposure and row["censor_reason"] == reason]
            times = [float(row["observed_time_days"]) for row in group]
            censor_rows.append({
                "landmark_exposure": exposure,
                "disposition": reason,
                "people": len(group),
                "minimum_observed_days": f"{min(times):.8f}" if times else "",
                "median_observed_days": f"{median(times):.8f}" if times else "",
                "maximum_observed_days": f"{max(times):.8f}" if times else "",
            })
    write_rows(target / "censoring-summary.csv", list(censor_rows[0]), censor_rows)

    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    assignments = assign_sites(longitudinal, contract)
    write_rows(target / "site-assignment.csv", list(assignments[0]), assignments)
    assignment_by_patient = {str(row["patient_id"]): row for row in assignments}
    analysis_rows: list[dict[str, object]] = []
    for row in longitudinal:
        if row["landmark_eligible_flag"] != "1":
            continue
        extension = assignment_by_patient[row["patient_id"]]
        clean_row = {key: value for key, value in row.items()}
        clean_row.update({key: value for key, value in extension.items() if key != "patient_id"})
        analysis_rows.append(clean_row)
    write_rows(target / "analysis-cohort.csv", list(analysis_rows[0]), analysis_rows)

    support_rows: list[dict[str, object]] = []
    for site in contract["sites"]:
        group = [row for row in analysis_rows if row["teaching_site_id"] == site]
        people = len(group)
        exposed = sum(row["landmark_exposure"] == "1" for row in group)
        events = sum(row["event_indicator"] == "1" for row in group)
        support_rows.append({
            "teaching_site_id": site,
            "people": people,
            "exposed": exposed,
            "unexposed": people - exposed,
            "later_events": events,
            "exposed_events": sum(row["landmark_exposure"] == "1" and row["event_indicator"] == "1" for row in group),
            "unexposed_events": sum(row["landmark_exposure"] == "0" and row["event_indicator"] == "1" for row in group),
            "low_risk": sum(row["baseline_risk_tier"] == "low" for row in group),
            "medium_risk": sum(row["baseline_risk_tier"] == "medium" for row in group),
            "high_risk": sum(row["baseline_risk_tier"] == "high" for row in group),
            "mean_age": f"{sum(int(row['age_at_index']) for row in group) / people:.8f}" if people else "",
            "prior_acute_total": sum(int(row["prior_365d_acute_count"]) for row in group),
            "followup_percent": f"{100 * exposed / people:.8f}" if people else "",
            "raw_event_percent": f"{100 * events / people:.8f}" if people else "",
            "known_direct_site_effect": "0",
        })
    write_rows(target / "site-support.csv", list(support_rows[0]), support_rows)

    output_names = [f"{name}.csv" for name in QUERIES] + [
        "cohort-flow.csv", "censoring-summary.csv", "site-assignment.csv",
        "analysis-cohort.csv", "site-support.csv",
    ]
    report = {
        "schema_version": "1.0.0",
        "module": "oclc-app1-02",
        "module_version": "0.1.0",
        "commons_release": "0.50.0",
        "source_database": {"bytes": database.stat().st_size, "sha256": database_hash},
        "extension": {"id": contract["extension_id"], "version": contract["version"], "seed": contract["seed"]},
        "outputs": {name: file_record(target / name) for name in output_names},
        "checks": checks,
        "environment": {"python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version, "external_python_dependencies": 0},
    }
    report_path = target / "build-report.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return report


def self_check() -> None:
    for filename in QUERIES.values():
        assert read_query(SQL_DIR / filename).endswith(";")
    with tempfile.TemporaryDirectory(prefix="app1-module02-build-") as temp_dir:
        base = Path(temp_dir)
        database = base / "fixture.sqlite"
        connection = sqlite3.connect(database)
        connection.executescript("""
            CREATE TABLE patients (id TEXT PRIMARY KEY, birthdate TEXT NOT NULL, deathdate TEXT, gender TEXT, race TEXT, ethnicity TEXT);
            CREATE TABLE encounters (id TEXT PRIMARY KEY, start TEXT NOT NULL, stop TEXT NOT NULL, patient TEXT NOT NULL, organization TEXT NOT NULL, encounterclass TEXT NOT NULL);
            CREATE TABLE conditions (start TEXT, patient TEXT, encounter TEXT);
            CREATE TABLE procedures (date TEXT, patient TEXT, encounter TEXT);
            INSERT INTO patients VALUES
              ('p1','1980-01-01',NULL,'F','white','nonhispanic'),
              ('p2','1980-01-01',NULL,'M','black','nonhispanic'),
              ('p3','1980-01-01','2018-01-20','F','asian','nonhispanic'),
              ('p4','1980-01-01',NULL,'M','white','hispanic'),
              ('p5','1980-01-01','2018-01-02','F','white','nonhispanic');
            INSERT INTO encounters VALUES
              ('i1','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p1','o1','inpatient'),
              ('f1','2018-01-10T00:00:00Z','2018-01-10T01:00:00Z','p1','o1','outpatient'),
              ('a1','2018-02-15T00:00:00Z','2018-02-15T01:00:00Z','p1','o1','emergency'),
              ('i2','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p2','o1','inpatient'),
              ('a2','2018-01-15T00:00:00Z','2018-01-15T01:00:00Z','p2','o1','emergency'),
              ('i3','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p3','o2','inpatient'),
              ('i4','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p4','o2','inpatient'),
              ('i5','2018-01-01T00:00:00Z','2018-01-02T00:00:00Z','p5','o3','inpatient');
        """)
        connection.close()
        first, second = base / "first", base / "second"
        report = build(database, first, enforce_reference=False)
        second_report = build(database, second, enforce_reference=False)
        assert report["checks"]["initial cohort"] == 5
        assert report["checks"]["index deaths"] == 1
        assert report["checks"]["early deaths"] == 1
        assert report["checks"]["early acute returns"] == 1
        assert report["checks"]["landmark eligible"] == 2
        assert report["checks"]["later acute returns"] == 1
        assert report["outputs"] == second_report["outputs"]
        try:
            build(database, first, enforce_reference=False)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
    print("APP-1 Module 02 builder self-check passed: death branches, landmark, exposure, outcome, extension, determinism, and overwrite rules.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--sql-dir", type=Path, default=SQL_DIR)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.database or not args.target:
        parser.error("--database and --target are required")
    try:
        report = build(args.database.resolve(), args.target.resolve(), args.sql_dir.resolve())
    except (OSError, ValueError, KeyError, sqlite3.Error) as error:
        parser.exit(1, f"Build failed: {error}\n")
    print(
        "APP-1 Module 02 build passed: "
        f"{report['checks']['initial cohort']} initial people, "
        f"{report['checks']['landmark eligible']} landmark people, and "
        f"{report['checks']['later acute returns']} later events."
    )


if __name__ == "__main__":
    main()
