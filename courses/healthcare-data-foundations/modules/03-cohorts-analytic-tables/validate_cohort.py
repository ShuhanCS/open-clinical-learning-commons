"""Validate and reproduce the FND-1 Module 03 cohort package."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sqlite3
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path

import build_cohort


MODULE_ROOT = Path(__file__).resolve().parent
EXPECTED_DATABASE_BYTES = 141_234_176
EXPECTED_DATABASE_SHA256 = "1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a"
OUTPUT_HEADERS = {
    "eligible-events.csv": [
        "patient_id", "birth_date", "death_date", "age_at_event", "gender", "race", "ethnicity",
        "eligible_encounter_id", "eligible_start", "eligible_stop", "eligible_class", "eligible_code",
        "eligible_description", "eligible_reason_code", "eligible_reason_description",
    ],
    "index-cohort.csv": [
        "patient_id", "birth_date", "death_date", "age_at_index", "gender", "race", "ethnicity",
        "index_encounter_id", "index_start", "index_stop", "index_class", "index_code",
        "index_description", "index_reason_code", "index_reason_description",
    ],
    "analytic-table.csv": [
        "patient_id", "birth_date", "death_date", "age_at_index", "gender", "race", "ethnicity",
        "index_encounter_id", "index_start", "index_stop", "index_class", "index_code",
        "index_description", "index_reason_code", "index_reason_description",
        "prior_365d_encounter_count", "prior_365d_acute_count", "prior_365d_condition_count",
        "prior_365d_medication_count", "next_30d_state", "next_30d_encounter_id", "next_30d_start",
        "next_30d_days_after_index_stop", "acute_return_90d", "death_90d", "endpoint_90d",
        "followup_90d_complete", "source_release", "cohort_definition_version",
    ],
    "cohort-flow.csv": ["step", "starting", "excluded", "remaining", "rule"],
    "query-checks.csv": ["check_id", "check_name", "observed_value", "expected_value", "status"],
}
EXPECTED_ROWS = {
    "eligible-events.csv": 1_048,
    "index-cohort.csv": 374,
    "analytic-table.csv": 374,
    "cohort-flow.csv": 4,
    "query-checks.csv": 16,
}


class ValidationError(RuntimeError):
    pass


def require(condition: bool, label: str, checks: list[str]) -> None:
    if not condition:
        raise ValidationError(label)
    checks.append(label)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def validate(workspace: Path, database: Path | None = None, submission: bool = False) -> dict[str, object]:
    checks: list[str] = []
    submission_files = (
        "README.md", "VERSION", "ai-use.md", "cohort-spec.md", "data-dictionary.csv",
        "reproducibility-check.md", "source-record.yml", "table-spec.md", "transformation-record.md",
        "sql/01-eligible-events.sql", "sql/02-index-cohort.sql",
        "sql/03-analytic-table.sql", "sql/04-validation.sql",
    ) + tuple(f"outputs/{name}" for name in OUTPUT_HEADERS)
    release_files = (
        ".gitattributes", "assessment.md", "build_cohort.py", "instructor-notes.md", "release.json",
        "validate_cohort.py",
    )
    required_files = submission_files if submission else submission_files + release_files
    for name in required_files:
        require((workspace / name).is_file(), f"Required file exists: {name}", checks)
    require((workspace / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0", checks)

    contract_files = [workspace / name for name in required_files if not name.startswith("outputs/")]
    for path in contract_files:
        if path.suffix.lower() not in {".csv", ".json", ".md", ".sql", ".yml"}:
            continue
        content = path.read_text(encoding="utf-8")
        require(not re.search(r"[\u2013\u2014]", content), f"Plain ASCII punctuation: {path.name}", checks)
        require(not re.search(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)", content), f"No personal absolute path: {path.name}", checks)
        if submission:
            require("[REPLACE:" not in content, f"Learner record is complete: {path.name}", checks)

    release_path = MODULE_ROOT / "release.json" if submission else workspace / "release.json"
    release = json.loads(release_path.read_text(encoding="utf-8"))
    require(release["status"] == "runnable-release-candidate", "Release status is runnable-release-candidate", checks)
    require(release["module"]["version"] == "0.1.0", "Release module version matches", checks)
    require(release["module"]["commons_release"] == "0.30.0", "Commons release is 0.30.0", checks)
    require(release["module"]["hours"] == 16.5, "Module workload is 16.5 hours", checks)
    require(release["upstream"]["database_sha256"] == EXPECTED_DATABASE_SHA256, "Upstream fingerprint is registered", checks)
    require(release["cohort"]["included_patients"] == 374, "Release registers 374 included patients", checks)
    require(release["analytic_table"]["fields"] == 29, "Release registers 29 analytic fields", checks)

    outputs: dict[str, list[dict[str, str]]] = {}
    for filename, expected_header in OUTPUT_HEADERS.items():
        path = workspace / "outputs" / filename
        header, rows = read_csv(path)
        outputs[filename] = rows
        registered = release["outputs"][filename]
        require(header == expected_header, f"Exact header: {filename}", checks)
        require(len(rows) == EXPECTED_ROWS[filename] == registered["rows"], f"Exact row count: {filename}", checks)
        require(path.stat().st_size == registered["bytes"], f"Exact byte count: {filename}", checks)
        require(build_cohort.sha256(path) == registered["sha256"], f"Exact SHA-256: {filename}", checks)

    eligible = outputs["eligible-events.csv"]
    require(len({row["eligible_encounter_id"] for row in eligible}) == 1_048, "Eligible encounter IDs are unique", checks)
    require(len({row["patient_id"] for row in eligible}) == 374, "Eligible events represent 374 adults", checks)
    require(all(int(row["age_at_event"]) >= 18 for row in eligible), "All eligible ages are at least 18", checks)
    require(all(row["eligible_class"] in {"emergency", "inpatient"} for row in eligible), "Eligible classes are acute", checks)
    require(all("2015-01-01T00:00:00Z" <= row["eligible_start"] < "2020-01-01T00:00:00Z" for row in eligible), "Eligible dates are in bounds", checks)
    require(all(row["patient_id"] and row["eligible_encounter_id"] for row in eligible), "Eligible keys are non-null", checks)

    indexes = outputs["index-cohort.csv"]
    require(len({row["patient_id"] for row in indexes}) == 374, "One index row per patient", checks)
    require(len({row["index_encounter_id"] for row in indexes}) == 374, "Index encounters are unique", checks)
    eligible_first: dict[str, tuple[str, str]] = {}
    for row in eligible:
        value = (row["eligible_start"], row["eligible_encounter_id"])
        eligible_first[row["patient_id"]] = min(value, eligible_first.get(row["patient_id"], value))
    require(
        all(eligible_first[row["patient_id"]] == (row["index_start"], row["index_encounter_id"]) for row in indexes),
        "Every index is the deterministic first eligible event",
        checks,
    )
    require(all(timestamp(row["index_stop"]) >= timestamp(row["index_start"]) for row in indexes), "Index stop is not before start", checks)

    analytic = outputs["analytic-table.csv"]
    index_keys = {(row["patient_id"], row["index_encounter_id"]) for row in indexes}
    analytic_keys = {(row["patient_id"], row["index_encounter_id"]) for row in analytic}
    require(analytic_keys == index_keys, "Analytic rows match the index cohort", checks)
    history_fields = (
        "prior_365d_encounter_count", "prior_365d_acute_count",
        "prior_365d_condition_count", "prior_365d_medication_count",
    )
    require(all(int(row[field]) >= 0 for row in analytic for field in history_fields), "History counts are nonnegative", checks)
    require(all(int(row["prior_365d_acute_count"]) <= int(row["prior_365d_encounter_count"]) for row in analytic), "Acute history does not exceed encounter history", checks)
    expected_history = {
        "prior_365d_encounter_count": (0, 187, 2_138),
        "prior_365d_acute_count": (0, 13, 113),
        "prior_365d_condition_count": (0, 5, 468),
        "prior_365d_medication_count": (0, 185, 1_007),
    }
    for field, expected in expected_history.items():
        values = [int(row[field]) for row in analytic]
        require((min(values), max(values), sum(values)) == expected, f"History distribution matches: {field}", checks)

    state_counts = Counter(row["next_30d_state"] for row in analytic)
    require(state_counts == Counter({"No encounter recorded": 263, "Scheduled care": 92, "Urgent care": 4, "Acute return": 15}), "Thirty-day states reconcile", checks)
    for row in analytic:
        if row["next_30d_state"] == "No encounter recorded":
            require(not row["next_30d_encounter_id"] and not row["next_30d_start"] and not row["next_30d_days_after_index_stop"], f"No-next fields are null: {row['patient_id']}", checks)
        else:
            elapsed = (timestamp(row["next_30d_start"]) - timestamp(row["index_stop"])).total_seconds() / 86_400
            require(0 < elapsed <= 30, f"Next encounter is within window: {row['patient_id']}", checks)
            require(abs(elapsed - float(row["next_30d_days_after_index_stop"])) < 0.000001, f"Next elapsed days reconcile: {row['patient_id']}", checks)

    require(Counter(row["acute_return_90d"] for row in analytic) == Counter({"0": 338, "1": 36}), "Ninety-day acute-return flags reconcile", checks)
    require(Counter(row["death_90d"] for row in analytic) == Counter({"0": 366, "1": 8}), "Ninety-day death flags reconcile", checks)
    require(Counter(row["endpoint_90d"] for row in analytic) == Counter({"Death": 8, "Acute return": 36, "No acute return recorded": 330}), "Ninety-day endpoints reconcile", checks)
    require(all(row["endpoint_90d"] == "Death" for row in analytic if row["death_90d"] == "1"), "Death has endpoint precedence", checks)
    require(all(row["followup_90d_complete"] == "1" for row in analytic), "Source covers every 90-day endpoint", checks)
    require(all(row["source_release"] == "synthea-csv-apr2020" for row in analytic), "Source release labels match", checks)
    require(all(row["cohort_definition_version"] == "0.1.0" for row in analytic), "Cohort versions match", checks)

    flow = outputs["cohort-flow.csv"]
    expected_flow = [("1", "1171", "0", "1171"), ("2", "1171", "690", "481"), ("3", "481", "107", "374"), ("4", "374", "0", "374")]
    require([(row["step"], row["starting"], row["excluded"], row["remaining"]) for row in flow] == expected_flow, "Four-step flow matches", checks)
    require(all(int(row["starting"]) - int(row["excluded"]) == int(row["remaining"]) for row in flow), "Every flow row conserves", checks)

    query_checks = outputs["query-checks.csv"]
    require(all(row["status"] == "pass" for row in query_checks), "All query checks pass", checks)
    require(all(row["observed_value"] == row["expected_value"] for row in query_checks), "Observed and expected query values match", checks)

    dictionary_header, dictionary = read_csv(workspace / "data-dictionary.csv")
    require(dictionary_header == ["position", "field_name", "timing", "data_type", "nullable", "allowed_values_or_rule", "description"], "Dictionary header matches", checks)
    require(len(dictionary) == 29, "Dictionary has 29 fields", checks)
    require([row["field_name"] for row in dictionary] == OUTPUT_HEADERS["analytic-table.csv"], "Dictionary order matches analytic table", checks)
    require({row["timing"] for row in dictionary} == {"key", "source", "index", "pre-index", "post-index", "metadata"}, "Dictionary timing labels are complete", checks)

    if submission:
        readme = (workspace / "README.md").read_text(encoding="utf-8").lower()
        require(any(disposition in readme for disposition in ("accept with conditions", "accept", "revise", "refer")), "Submission includes a release disposition", checks)

    reproduced = False
    if database:
        require(database.is_file(), "Upstream database exists", checks)
        require(database.stat().st_size == EXPECTED_DATABASE_BYTES, "Upstream database byte count matches", checks)
        require(build_cohort.sha256(database) == EXPECTED_DATABASE_SHA256, "Upstream database SHA-256 matches", checks)
        connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
        try:
            require(connection.execute("PRAGMA integrity_check").fetchone()[0] == "ok", "Upstream database integrity is ok", checks)
            for table, count in (("patients", 1_171), ("encounters", 53_346), ("conditions", 8_376), ("medications", 42_989)):
                require(connection.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0] == count, f"Upstream row count matches: {table}", checks)
        finally:
            connection.close()
        with tempfile.TemporaryDirectory(prefix="fnd1-module03-reproduce-") as temp_dir:
            target = Path(temp_dir) / "outputs"
            build_cohort.build(database, target, workspace / "sql")
            for filename in OUTPUT_HEADERS:
                require((target / filename).read_bytes() == (workspace / "outputs" / filename).read_bytes(), f"SQL rerun reproduces: {filename}", checks)
        reproduced = True

    report = {
        "status": "pass",
        "checks_passed": len(checks),
        "checks": checks,
        "output_rows": EXPECTED_ROWS,
        "database_reproduced": reproduced,
    }
    print(f"FND-1 Module 03 validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    validate(MODULE_ROOT)
    with tempfile.TemporaryDirectory(prefix="fnd1-module03-invalid-") as temp_dir:
        fixture = Path(temp_dir) / "module"
        shutil.copytree(MODULE_ROOT, fixture, ignore=shutil.ignore_patterns("__pycache__"))
        (fixture / "outputs" / "analytic-table.csv").unlink()
        try:
            validate(fixture)
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted an incomplete package.")
    print("FND-1 Module 03 validator self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--database", type=Path)
    parser.add_argument("--submission", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        workspace = (args.workspace or MODULE_ROOT).resolve()
        validate(workspace, args.database.resolve() if args.database else None, args.submission)
    except (OSError, ValueError, KeyError, sqlite3.Error, ValidationError) as exc:
        parser.exit(1, f"Validation failed: {exc}\n")


if __name__ == "__main__":
    main()
