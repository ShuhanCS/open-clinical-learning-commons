"""Build the FND-1 Module 04 deterministic data-quality defect release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sqlite3
import tempfile
from copy import deepcopy
from datetime import datetime, timedelta
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
EXPECTED_SOURCE_BYTES = 121_787
EXPECTED_SOURCE_SHA256 = "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"
EXPECTED_SOURCE_ROWS = 374
EXPECTED_SOURCE_FIELDS = 29


def rule(issue_id: str, category: str, scope: str, field: str, text: str, count: int, severity: str, blocking: str, consequence: str, response: str, purpose: str) -> dict[str, object]:
    return {
        "issue_id": issue_id,
        "category": category,
        "table_scope": scope,
        "field_name": field,
        "rule": text,
        "expected_count": count,
        "severity": severity,
        "blocking": blocking,
        "likely_cause": "deterministic teaching defect" if issue_id.startswith("D") else "accepted synthetic source characteristic",
        "analytic_consequence": consequence,
        "expected_response": response,
        "owner": "learner data analyst" if issue_id.startswith("D") else "Module 05 clinical analytics reviewer",
        "teaching_purpose": purpose,
    }


RULES = (
    rule("D01", "uniqueness", "defective", "patient_id", "Exact duplicate person rows beyond the first patient row.", 5, "blocking", "yes", "Changes person denominators and weights duplicated people twice.", "Remove only manifest-appended duplicates and verify one row per patient.", "Grain determines whether repetition is a defect."),
    rule("D02", "completeness", "defective", "index_encounter_id", "Required index encounter ID is blank.", 3, "blocking", "yes", "Breaks index traceability and key completeness.", "Restore the accepted index key.", "Required keys cannot be imputed or left blank."),
    rule("D03", "validity", "defective", "age_at_index", "Age at index is below 18.", 3, "blocking", "yes", "Contradicts cohort eligibility.", "Restore the accepted age.", "A derived value must remain consistent with inclusion rules."),
    rule("D04", "validity", "defective", "age_at_index", "Age at index exceeds 120.", 2, "blocking", "yes", "Implausible teaching value distorts age summaries.", "Restore the accepted age.", "Validity bounds differ from review thresholds."),
    rule("D05", "conformance", "defective", "index_start", "Index start is not a parseable UTC timestamp.", 3, "blocking", "yes", "Breaks time zero and temporal analysis.", "Restore the accepted timestamp.", "A string can be nonblank but nonconforming."),
    rule("D06", "temporal consistency", "defective", "index_stop", "Index stop occurs before index start.", 3, "blocking", "yes", "Produces an impossible encounter interval and invalid follow-up origin.", "Restore the accepted stop timestamp.", "Cross-field order matters after type checks pass."),
    rule("D07", "vocabulary validity", "defective", "index_class", "Index class is outside the acute vocabulary even after case normalization.", 2, "blocking", "yes", "Contradicts cohort eligibility and grouping.", "Restore the accepted class.", "Unknown codes differ from case drift."),
    rule("D08", "coding drift", "defective", "index_class", "Index class has a noncanonical case variant.", 3, "material", "no", "Splits groups in case-sensitive analysis.", "Restore canonical lowercase and document drift.", "Standardization must be explicit and reversible."),
    rule("D09", "validity", "defective", "prior_365d_encounter_count", "Encounter-history count is negative.", 3, "blocking", "yes", "Invalidates history summaries.", "Restore the accepted nonnegative count.", "Counts have domain constraints."),
    rule("D10", "cross-field consistency", "defective", "prior_365d_acute_count", "Acute-history count exceeds all encounter history.", 3, "blocking", "yes", "Violates numerator-parent count logic.", "Restore the accepted count pair.", "Valid single fields can conflict together."),
    rule("D11", "completeness", "defective", "gender", "Required source gender is blank.", 4, "material", "yes", "Creates unsupported missingness and changes subgroup denominators.", "Restore the accepted value.", "Required and optional missingness need different responses."),
    rule("D12", "vocabulary validity", "defective", "gender", "Gender value is outside M or F in this pinned source contract.", 3, "material", "yes", "Creates an unregistered category.", "Restore the accepted value and preserve source meaning.", "Vocabulary checks are release-specific, not universal identity rules."),
    rule("D13", "cross-field consistency", "defective", "next_30d_state", "No-encounter state has one or more next-event companion values.", 3, "blocking", "yes", "Contradicts explicit absence and can double-count follow-up.", "Restore all three blank companion fields.", "Missingness must agree with the state label."),
    rule("D14", "cross-field consistency", "defective", "next_30d_state", "Recorded next state lacks one or more required companion values.", 3, "blocking", "yes", "Prevents timing and event traceability.", "Restore all accepted companion fields.", "A label alone is not a complete event record."),
    rule("D15", "temporal validity", "defective", "next_30d_days_after_index_stop", "Next-event elapsed days are at or below zero.", 2, "blocking", "yes", "Places follow-up at or before the follow-up origin.", "Restore the accepted elapsed value.", "Open-left boundaries require greater than zero."),
    rule("D16", "temporal validity", "defective", "next_30d_days_after_index_stop", "Next-event elapsed days exceed 30.", 2, "blocking", "yes", "Places an event outside the declared window.", "Restore the accepted elapsed value.", "Closed-right boundaries still need an upper limit."),
    rule("D17", "vocabulary validity", "defective", "acute_return_90d", "Acute-return flag is outside 0 or 1.", 3, "blocking", "yes", "Breaks binary summaries and endpoint logic.", "Restore the accepted flag.", "Numeric-looking flags still need vocabulary checks."),
    rule("D18", "endpoint consistency", "defective", "endpoint_90d", "Death flag equals 1 but endpoint is not Death.", 2, "blocking", "yes", "Violates declared endpoint precedence.", "Restore the accepted endpoint.", "Precedence is a cross-field rule, not a label preference."),
    rule("D19", "provenance conformance", "defective", "source_release", "Source-release label differs from synthea-csv-apr2020.", 2, "blocking", "yes", "Breaks provenance and may mix releases silently.", "Restore the accepted source label.", "Version fields are analytic data, not decoration."),
    rule("D20", "version conformance", "defective", "cohort_definition_version", "Cohort-definition version differs from 0.1.0.", 2, "blocking", "yes", "Breaks the frozen cohort contract.", "Restore the accepted cohort version.", "Downstream work must pin the definition it uses."),
    rule("N01", "structural optionality", "accepted", "death_date", "Death date is blank in the accepted table.", 343, "condition", "no", "Death-specific denominators differ from the full cohort.", "Retain missing values and state the denominator.", "High missingness can be correct for an optional event."),
    rule("N02", "structural optionality", "accepted", "index_reason_code", "Index reason code and description are both blank.", 226, "condition", "no", "Reason-specific descriptions have a smaller available denominator.", "Retain paired missingness and document availability.", "Optional paired fields need consistency, not imputation."),
    rule("N03", "structural consistency", "accepted", "next_30d_state", "No-encounter state has all three companion fields blank.", 263, "condition", "no", "The source cannot establish whether care occurred elsewhere.", "Retain explicit state and blank companions.", "Explicit absence differs from no care."),
    rule("N04", "extreme review", "accepted", "age_at_index", "Age at index is at least 100.", 5, "review", "no", "Extreme ages may influence summaries.", "Review against source and retain unless disproven.", "Extreme is not automatically invalid."),
    rule("N05", "extreme review", "accepted", "prior_365d_encounter_count", "Prior encounter count exceeds 100.", 2, "review", "no", "A small number of rows may dominate count summaries.", "Review source history and retain with robust summaries.", "High utilization is not automatically a duplicate."),
    rule("N06", "extreme review", "accepted", "prior_365d_medication_count", "Prior medication count exceeds 100.", 1, "review", "no", "One row may dominate count summaries.", "Review source rows and retain with a condition.", "Row counts are not necessarily unique therapies."),
    rule("N07", "small-cell caution", "accepted", "race", "Rows belong to race categories with fewer than 10 cohort rows.", 6, "condition", "no", "Public display may expose unstable or overinterpreted tiny groups.", "Retain internally and apply audience-specific display caution.", "Rare categories are not data errors."),
    rule("N08", "small-cell caution", "accepted", "next_30d_state|endpoint_90d", "Rows belong to urgent-care next state or Death endpoint cells.", 12, "condition", "no", "Small outcome cells can be overinterpreted.", "Retain exact internal counts and limit claims and display.", "A teaching threshold is not a universal suppression law."),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_source(source: Path) -> tuple[list[str], list[dict[str, str]]]:
    if source.stat().st_size != EXPECTED_SOURCE_BYTES or sha256(source) != EXPECTED_SOURCE_SHA256:
        raise ValueError("Accepted analytic-table bytes or SHA-256 changed.")
    with source.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fields = list(reader.fieldnames or [])
    if len(rows) != EXPECTED_SOURCE_ROWS or len(fields) != EXPECTED_SOURCE_FIELDS:
        raise ValueError("Accepted analytic-table shape changed.")
    if len({row["patient_id"] for row in rows}) != EXPECTED_SOURCE_ROWS:
        raise ValueError("Accepted analytic-table patient grain changed.")
    return fields, rows


def seed_defects(accepted: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    defective = deepcopy(accepted)
    used: set[str] = set()
    manifest: list[dict[str, str]] = []

    def take(count: int, predicate=lambda row: True) -> list[dict[str, str]]:
        selected = []
        for row in defective:
            if row["patient_id"] not in used and predicate(row):
                selected.append(row)
                used.add(row["patient_id"])
                if len(selected) == count:
                    return selected
        raise ValueError(f"Could not select {count} deterministic rows for a defect rule.")

    def change(issue: str, rows: list[dict[str, str]], field: str, value) -> None:
        for case_number, row in enumerate(rows, start=1):
            new_value = str(value(row) if callable(value) else value)
            case_id = f"{issue}-{case_number:03d}"
            manifest.append({
                "change_id": f"{case_id}-{sum(item['case_id'] == case_id for item in manifest) + 1:02d}",
                "case_id": case_id,
                "issue_id": issue,
                "patient_id": row["patient_id"],
                "field_name": field,
                "operation": "replace",
                "original_value": row[field],
                "defect_value": new_value,
            })
            row[field] = new_value

    duplicates = take(5)
    for number, row in enumerate(duplicates, start=1):
        case_id = f"D01-{number:03d}"
        manifest.append({
            "change_id": f"{case_id}-01", "case_id": case_id, "issue_id": "D01",
            "patient_id": row["patient_id"], "field_name": "*row*", "operation": "append_exact_duplicate",
            "original_value": "one accepted row", "defect_value": "two identical rows",
        })

    change("D02", take(3), "index_encounter_id", "")
    change("D03", take(3), "age_at_index", "17")
    change("D04", take(2), "age_at_index", "145")
    change("D05", take(3), "index_start", "not-a-timestamp")
    change("D06", take(3), "index_stop", lambda row: (datetime.fromisoformat(row["index_start"].replace("Z", "+00:00")) - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ"))
    change("D07", take(2), "index_class", "telehealth")
    change("D08", take(3, lambda row: row["index_class"] == "emergency"), "index_class", "Emergency")
    change("D09", take(3), "prior_365d_encounter_count", "-1")
    change("D10", take(3), "prior_365d_acute_count", lambda row: int(row["prior_365d_encounter_count"]) + 1)
    change("D11", take(4), "gender", "")
    change("D12", take(3), "gender", "U")

    no_next = take(3, lambda row: row["next_30d_state"] == "No encounter recorded")
    change("D13", no_next, "next_30d_encounter_id", lambda row: f"seeded-next-{row['patient_id'][:8]}")
    change("D13", no_next, "next_30d_start", lambda row: (datetime.fromisoformat(row["index_stop"].replace("Z", "+00:00")) + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ"))
    change("D13", no_next, "next_30d_days_after_index_stop", "1.0")

    has_next = take(3, lambda row: row["next_30d_state"] != "No encounter recorded")
    change("D14", has_next, "next_30d_encounter_id", "")
    change("D14", has_next, "next_30d_start", "")
    change("D14", has_next, "next_30d_days_after_index_stop", "")
    change("D15", take(2, lambda row: row["next_30d_state"] != "No encounter recorded"), "next_30d_days_after_index_stop", "-1")
    change("D16", take(2, lambda row: row["next_30d_state"] != "No encounter recorded"), "next_30d_days_after_index_stop", "31")
    change("D17", take(3), "acute_return_90d", "2")
    change("D18", take(2, lambda row: row["death_90d"] == "1"), "endpoint_90d", "Acute return")
    change("D19", take(2), "source_release", "synthea-csv-apr2021")
    change("D20", take(2), "cohort_definition_version", "0.0.9")

    defective.extend(deepcopy(duplicates))
    manifest.sort(key=lambda row: row["change_id"])
    return defective, manifest


def write_database(path: Path, fields: list[str], accepted: list[dict[str, str]], defective: list[dict[str, str]], manifest: list[dict[str, str]]) -> None:
    connection = sqlite3.connect(path)
    try:
        connection.execute("PRAGMA journal_mode = OFF")
        connection.execute("PRAGMA synchronous = OFF")
        columns = ", ".join(f'"{field}" TEXT' for field in fields)
        connection.execute(f"CREATE TABLE accepted_analytic_table ({columns})")
        connection.execute(f"CREATE TABLE defective_analytic_table ({columns})")
        connection.execute("CREATE TABLE defect_manifest (change_id TEXT PRIMARY KEY, case_id TEXT, issue_id TEXT, patient_id TEXT, field_name TEXT, operation TEXT, original_value TEXT, defect_value TEXT)")
        connection.execute("CREATE TABLE quality_rules (issue_id TEXT PRIMARY KEY, category TEXT, table_scope TEXT, field_name TEXT, rule TEXT, expected_count INTEGER, severity TEXT, blocking TEXT, likely_cause TEXT, analytic_consequence TEXT, expected_response TEXT, owner TEXT, teaching_purpose TEXT)")
        connection.execute("CREATE TABLE release_metadata (name TEXT PRIMARY KEY, value TEXT)")
        names = ", ".join(f'"{field}"' for field in fields)
        placeholders = ", ".join("?" for _ in fields)
        connection.executemany(f"INSERT INTO accepted_analytic_table ({names}) VALUES ({placeholders})", [[row[field] for field in fields] for row in accepted])
        connection.executemany(f"INSERT INTO defective_analytic_table ({names}) VALUES ({placeholders})", [[row[field] for field in fields] for row in defective])
        connection.executemany("INSERT INTO defect_manifest VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [[row[field] for field in manifest[0]] for row in manifest])
        rule_fields = list(RULES[0])
        connection.executemany(f"INSERT INTO quality_rules VALUES ({', '.join('?' for _ in rule_fields)})", [[row[field] for field in rule_fields] for row in RULES])
        connection.executemany("INSERT INTO release_metadata VALUES (?, ?)", [
            ("module_version", "0.1.0"), ("defect_release_version", "0.1.0"),
            ("accepted_source_sha256", EXPECTED_SOURCE_SHA256), ("synthetic", "true"),
        ])
        connection.execute("CREATE UNIQUE INDEX accepted_patient_id ON accepted_analytic_table(patient_id)")
        connection.execute("CREATE UNIQUE INDEX accepted_index_id ON accepted_analytic_table(index_encounter_id)")
        connection.execute("CREATE INDEX defective_patient_id ON defective_analytic_table(patient_id)")
        connection.execute("PRAGMA user_version = 1")
        connection.commit()
        connection.execute("VACUUM")
    finally:
        connection.close()


def build(source: Path, target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    fields, accepted = read_source(source)
    defective, manifest = seed_defects(accepted)
    if len({row["case_id"] for row in manifest}) != 56 or len(manifest) != 68:
        raise ValueError("Seeded defect case or manifest count changed.")
    target.mkdir(parents=True)
    accepted_path = target / "accepted-analytic-table.csv"
    shutil.copy2(source, accepted_path)
    defective_path = target / "defective-analytic-table.csv"
    manifest_path = target / "defect-manifest.csv"
    rules_path = target / "quality-rules.csv"
    database_path = target / "fnd1-quality-defects.sqlite"
    write_csv(defective_path, fields, defective)
    write_csv(manifest_path, list(manifest[0]), manifest)
    write_csv(rules_path, list(RULES[0]), list(RULES))
    write_database(database_path, fields, accepted, defective, manifest)
    report = {
        "status": "pass",
        "version": "0.1.0",
        "source": {"rows": len(accepted), "fields": len(fields), "bytes": accepted_path.stat().st_size, "sha256": sha256(accepted_path)},
        "defective": {"rows": len(defective), "fields": len(fields), "bytes": defective_path.stat().st_size, "sha256": sha256(defective_path), "distinct_patients": len({row["patient_id"] for row in defective})},
        "manifest": {"rows": len(manifest), "cases": len({row["case_id"] for row in manifest}), "bytes": manifest_path.stat().st_size, "sha256": sha256(manifest_path)},
        "rules": {"rows": len(RULES), "bytes": rules_path.stat().st_size, "sha256": sha256(rules_path)},
        "database": {"bytes": database_path.stat().st_size, "sha256": sha256(database_path), "sqlite": sqlite3.sqlite_version},
    }
    with (target / "build-report.json").open("w", encoding="utf-8", newline="") as handle:
        handle.write(json.dumps(report, indent=2) + "\n")
    return report


def self_check() -> None:
    assert len(RULES) == 28
    assert sum(int(row["expected_count"]) for row in RULES if str(row["issue_id"]).startswith("D")) == 56
    with tempfile.TemporaryDirectory(prefix="fnd1-module04-build-") as temp_dir:
        target = Path(temp_dir)
        try:
            build(Path("missing.csv"), target)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target.")
    print("FND-1 Module 04 defect builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.source or not args.target:
        parser.error("--source and --target are required")
    try:
        report = build(args.source.resolve(), args.target.resolve())
    except (OSError, ValueError, sqlite3.Error) as exc:
        parser.exit(1, f"Build failed: {exc}\n")
    print(
        "FND-1 Module 04 defect build passed: "
        f"{report['defective']['rows']} rows, {report['manifest']['cases']} cases, "
        f"and {report['manifest']['rows']} manifest changes."
    )


if __name__ == "__main__":
    main()
