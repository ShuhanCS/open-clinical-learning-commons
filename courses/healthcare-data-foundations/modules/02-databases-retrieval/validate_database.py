"""Validate the FND-1 Module 02 relational database workspace."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import tempfile
from pathlib import Path

import build_database
import run_queries


MODULE_ROOT = Path(__file__).resolve().parent
MANIFEST = MODULE_ROOT / "source-manifest.csv"
REFERENCE_SQL = MODULE_ROOT / "reference-first-extracts.sql"
SURROGATE_TABLES = {
    "allergies", "conditions", "devices", "immunizations", "medications",
    "observations", "payer_transitions", "procedures", "supplies",
}
EXPECTED_ENCOUNTER_CLASSES = {
    "ambulatory": 18_936,
    "emergency": 2_090,
    "inpatient": 1_838,
    "outpatient": 9_003,
    "urgentcare": 2_373,
    "wellness": 19_106,
}
EXPECTED_QUERY_ROWS = {
    "table-inventory": 16,
    "encounter-class-counts": 6,
    "observation-linkage": 3,
    "selected-patient-timeline": 25,
    "numeric-observation-sample": 25,
}


class ValidationError(RuntimeError):
    pass


def require(condition: bool, label: str, checks: list[str]) -> None:
    if not condition:
        raise ValidationError(label)
    checks.append(label)


def manifest_rows(path: Path = MANIFEST) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_fhir(root: Path, checks: list[str]) -> None:
    resources = {}
    for filename, resource_type in (
        ("patient.json", "Patient"),
        ("encounter.json", "Encounter"),
        ("observation.json", "Observation"),
    ):
        path = root / "fhir" / filename
        require(path.is_file(), f"FHIR file exists: {filename}", checks)
        resource = json.loads(path.read_text(encoding="utf-8"))
        require(resource.get("resourceType") == resource_type, f"FHIR resource type: {resource_type}", checks)
        require(bool(resource.get("id")), f"FHIR resource ID: {resource_type}", checks)
        resources[resource_type] = resource
    patient_ref = f"Patient/{resources['Patient']['id']}"
    encounter_ref = f"Encounter/{resources['Encounter']['id']}"
    require(resources["Encounter"].get("subject", {}).get("reference") == patient_ref, "Encounter subject resolves to Patient", checks)
    require(resources["Observation"].get("subject", {}).get("reference") == patient_ref, "Observation subject resolves to Patient", checks)
    require(resources["Observation"].get("encounter", {}).get("reference") == encounter_ref, "Observation encounter resolves to Encounter", checks)
    quantity = resources["Observation"].get("valueQuantity", {})
    require(isinstance(quantity.get("value"), (int, float)) and bool(quantity.get("unit")), "Observation has numeric value and unit", checks)


def validate(target: Path, source_zip: Path | None = None, submission: bool = False) -> dict[str, object]:
    checks: list[str] = []
    required_files = (
        ".gitattributes", ".gitignore", "README.md", "VERSION", "ai-use.md",
        "build-report.json", "data-dictionary.csv", "data-model.mmd",
        "fhir-json-reading.md", "run_queries.py", "schema-description.md", "schema.sql",
        "source-manifest.csv", "source-record.yml", "validation-notes.md",
        "sql/01-first-extracts.sql", "data/fnd1_synthea_apr2020.sqlite",
    )
    for name in required_files:
        require((target / name).is_file(), f"Required file exists: {name}", checks)
    require((target / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Workspace version is 0.1.0", checks)

    registered = manifest_rows()
    submitted = manifest_rows(target / "source-manifest.csv")
    require(submitted == registered, "Source manifest matches release", checks)
    if source_zip:
        build_database.validate_archive(source_zip, registered)
        checks.append("Source archive bytes, fingerprint, members, and member fingerprints match")

    report = json.loads((target / "build-report.json").read_text(encoding="utf-8"))
    require(report.get("status") == "pass", "Build report status is pass", checks)
    require(report.get("source", {}).get("sha256") == build_database.EXPECTED_ARCHIVE_SHA256, "Build report source fingerprint matches", checks)
    require(report.get("source", {}).get("bytes") == build_database.EXPECTED_ARCHIVE_BYTES, "Build report source bytes match", checks)
    require(report.get("total_source_rows") == 471_836, "Build report total is 471836 rows", checks)
    require(report.get("foreign_key_failures") == 0, "Build report has zero foreign-key failures", checks)
    require(report.get("integrity_check") == "ok", "Build report integrity is ok", checks)
    require(report.get("data_dictionary_rows") == 177, "Build report has 177 dictionary rows", checks)

    database = target / "data" / "fnd1_synthea_apr2020.sqlite"
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    require(connection.execute("PRAGMA integrity_check").fetchone()[0] == "ok", "SQLite integrity check is ok", checks)
    require(len(connection.execute("PRAGMA foreign_key_check").fetchall()) == 0, "SQLite has zero foreign-key failures", checks)
    require(connection.execute("PRAGMA user_version").fetchone()[0] == 1, "SQLite user_version is 1", checks)

    for row in registered:
        table = row["table_name"]
        observed = connection.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
        require(observed == int(row["source_rows"]), f"Row count matches: {table}", checks)
        columns = connection.execute(f'PRAGMA table_info("{table}")').fetchall()
        expected_columns = int(row["source_columns"]) + (1 if table in SURROGATE_TABLES else 0)
        require(len(columns) == expected_columns, f"Column count matches: {table}", checks)

    manifest_count = connection.execute("SELECT COUNT(*) FROM source_table_manifest").fetchone()[0]
    require(manifest_count == 16, "Database manifest has 16 rows", checks)
    total = sum(connection.execute(f'SELECT COUNT(*) FROM "{row["table_name"]}"').fetchone()[0] for row in registered)
    require(total == 471_836, "Database has 471836 total source rows", checks)
    require(connection.execute("SELECT COUNT(*) FROM v_patients_minimal").fetchone()[0] == 1_171, "Minimal patient view has 1171 rows", checks)
    require(connection.execute("SELECT COUNT(*) FROM v_encounters_core").fetchone()[0] == 53_346, "Core encounter view has 53346 rows", checks)
    require(connection.execute("SELECT COUNT(*) FROM v_observations_core").fetchone()[0] == 299_697, "Core observation view has 299697 rows", checks)

    encounter_classes = dict(connection.execute("SELECT encounterclass, COUNT(*) FROM encounters GROUP BY encounterclass"))
    for name, count in EXPECTED_ENCOUNTER_CLASSES.items():
        require(encounter_classes.get(name) == count, f"Encounter class count matches: {name}", checks)
    require(connection.execute("SELECT COUNT(*) FROM observations WHERE type='numeric'").fetchone()[0] == 278_488, "Numeric observation count is 278488", checks)
    require(connection.execute("SELECT COUNT(*) FROM observations WHERE type='text'").fetchone()[0] == 21_209, "Text observation count is 21209", checks)
    require(connection.execute("SELECT COUNT(*) FROM observations WHERE encounter IS NULL").fetchone()[0] == 30_363, "Observations without encounter reference total 30363", checks)
    require(connection.execute("SELECT COUNT(*) FROM supplies").fetchone()[0] == 0, "Empty supplies table is preserved", checks)
    connection.close()

    with (target / "data-dictionary.csv").open(encoding="utf-8", newline="") as handle:
        dictionary = list(csv.DictReader(handle))
    require(len(dictionary) == 177, "Data dictionary has 177 rows", checks)
    require(len({(row["table_name"], row["database_field"]) for row in dictionary}) == 177, "Data dictionary table-field keys are unique", checks)
    require(sum(row["identity_like"] == "yes" for row in dictionary) > 0, "Data dictionary flags identity-like fields", checks)
    require(sum(row["cost_or_coverage"] == "yes" for row in dictionary) > 0, "Data dictionary flags cost and coverage fields", checks)
    require(sum(row["included_in_core_view"] == "yes" for row in dictionary) == 27, "Data dictionary marks 27 core-view fields", checks)

    validate_fhir(target, checks)

    with tempfile.TemporaryDirectory(prefix="fnd1-module02-reference-") as temp_dir:
        query_counts = run_queries.run(database, REFERENCE_SQL, Path(temp_dir) / "outputs")
    require(query_counts == EXPECTED_QUERY_ROWS, "Five reference extracts have expected row counts", checks)

    if submission:
        learner_files = (
            "source-record.yml", "data-model.mmd", "schema-description.md",
            "fhir-json-reading.md", "validation-notes.md", "ai-use.md",
            "sql/01-first-extracts.sql",
        )
        for name in learner_files:
            content = (target / name).read_text(encoding="utf-8")
            require("[REPLACE:" not in content, f"Learner record is complete: {name}", checks)
            require(not re.search(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)", content), f"Learner record has no personal absolute path: {name}", checks)
        with tempfile.TemporaryDirectory(prefix="fnd1-module02-submission-") as temp_dir:
            temp_root = Path(temp_dir)
            observed_dir = temp_root / "observed"
            expected_dir = temp_root / "expected"
            observed_counts = run_queries.run(database, target / "sql" / "01-first-extracts.sql", observed_dir)
            expected_counts = run_queries.run(database, REFERENCE_SQL, expected_dir)
            require(observed_counts == expected_counts == EXPECTED_QUERY_ROWS, "Learner extract row counts match reference", checks)
            for name in EXPECTED_QUERY_ROWS:
                submitted_output = target / "outputs" / f"{name}.csv"
                require(submitted_output.is_file(), f"Learner extract exists: {name}", checks)
                require(submitted_output.read_bytes() == (observed_dir / f"{name}.csv").read_bytes(), f"Learner extract matches submitted SQL: {name}", checks)
                require(submitted_output.read_bytes() == (expected_dir / f"{name}.csv").read_bytes(), f"Learner extract matches reference result: {name}", checks)

    validation_report = {
        "status": "pass",
        "checks_passed": len(checks),
        "checks": checks,
        "database_bytes": database.stat().st_size,
        "database_sha256": build_database.sha256(database),
        "source_archive_revalidated": bool(source_zip),
        "reference_query_rows": query_counts,
    }
    (target / "validation-report.json").write_text(json.dumps(validation_report, indent=2) + "\n", encoding="utf-8")
    print(f"FND-1 Module 02 database validation passed: {len(checks)} checks.")
    return validation_report


def self_check() -> None:
    rows = manifest_rows()
    assert len(rows) == 16
    assert sum(int(row["source_rows"]) for row in rows) == 471_836
    run_queries.self_check()
    with tempfile.TemporaryDirectory(prefix="fnd1-module02-fhir-") as temp_dir:
        root = Path(temp_dir)
        (root / "fhir").mkdir()
        patient = {"resourceType": "Patient", "id": "p1"}
        encounter = {"resourceType": "Encounter", "id": "e1", "subject": {"reference": "Patient/p1"}}
        observation = {
            "resourceType": "Observation", "id": "o1",
            "subject": {"reference": "Patient/p1"},
            "encounter": {"reference": "Encounter/e1"},
            "valueQuantity": {"value": 1.0, "unit": "unit"},
        }
        for name, resource in (("patient.json", patient), ("encounter.json", encounter), ("observation.json", observation)):
            (root / "fhir" / name).write_text(json.dumps(resource), encoding="utf-8")
        checks: list[str] = []
        validate_fhir(root, checks)
        assert len(checks) == 13
        observation["encounter"]["reference"] = "Encounter/wrong"
        (root / "fhir" / "observation.json").write_text(json.dumps(observation), encoding="utf-8")
        try:
            validate_fhir(root, [])
        except ValidationError:
            pass
        else:
            raise AssertionError("FHIR validator accepted a broken encounter reference.")
    print("FND-1 Module 02 validator self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--source-zip", type=Path)
    parser.add_argument("--submission", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.workspace:
            parser.error("workspace is required unless --self-check is used")
        if args.submission and not args.source_zip:
            parser.error("--submission requires --source-zip")
        validate(args.workspace.resolve(), args.source_zip.resolve() if args.source_zip else None, args.submission)
    except (OSError, ValueError, sqlite3.Error, ValidationError) as exc:
        parser.exit(1, f"Validation failed: {exc}\n")


if __name__ == "__main__":
    main()
