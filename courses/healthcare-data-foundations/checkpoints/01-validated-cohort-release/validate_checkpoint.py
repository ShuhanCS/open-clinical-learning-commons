"""Validate the FND-1 Week 3 cumulative checkpoint."""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import assemble_checkpoint


PACKAGE_ROOT = Path(__file__).resolve().parent
MODULE3_VALIDATOR = PACKAGE_ROOT.parents[1] / "modules" / "03-cohorts-analytic-tables" / "validate_cohort.py"
PLACEHOLDER = re.compile(r"\[REPLACE:[^\]\r\n]*\]|\b(?:TODO|TBD|REPLACE_ME)\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
FIRST_EXTRACTS = {
    "encounter-class-counts.csv": (6, 125, "26106dd682622ddbc6d75857a93607d48a353ba707ef56fc51d231be8f201d65"),
    "numeric-observation-sample.csv": (25, 3335, "f6854aeeeca3a7083147f53fa7e41fd7797e3ee94f459864c087190126c2d940"),
    "observation-linkage.csv": (3, 138, "901e06e7c9b71b5e11daf021772837af9223338c921641aeff60cc1ca214dd12"),
    "selected-patient-timeline.csv": (25, 3364, "411a05229819cd5e7cfe9d678fc8920053db8e2be8cc93135c6fcb88d1b28a0c"),
    "table-inventory.csv": (16, 337, "3f8fc12567ef57d1b74c21aa9fcfaedfac764c772e8d422ced002b7901358c07"),
}
M3_OUTPUTS = {
    "eligible-events.csv": (1048, 229592, "28163b5bb5db0ac78dc3a1e3ada606cb582dd5c6835678d2322550f4178878f3"),
    "index-cohort.csv": (374, 82045, "27bb741f914da2efcfcaa70a2a5a527b9dc32c06946afdcc5ac451216e314891"),
    "analytic-table.csv": (374, 121787, "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"),
    "cohort-flow.csv": (4, 259, "d9addbe256d4a94e878a84ae3a59b15f849e8110bec3a50d54f97cbac968d2c6"),
    "query-checks.csv": (16, 739, "e82b275e698634fda7072d816abd0a51cc0a0d11dcc581f842fec821b1eb3319"),
}
REQUIRED_FILES = (
    ".gitattributes", "README.md", "VERSION", "requirements.txt", "environment-note.md",
    "version-policy.md", "schema/schema-diagram.svg", "schema/data-model.mmd",
    "schema/schema-description.md", "schema/data-dictionary.csv",
    "schema/analytic-data-dictionary.csv", "schema/source-manifest.csv", "schema/schema.sql",
    "schema/source-system-comparison.md", "schema/fhir-json-reading.md",
    "sql/01-first-extracts.sql", "sql/02-index-cohort.sql", "sql/03-analytic-table.sql",
    "sql/04-validation.sql", "outputs/first-extracts.csv", "outputs/eligible-events.csv",
    "outputs/index-cohort.csv", "outputs/cohort-flow.csv", "outputs/analytic-table.csv",
    "outputs/query-checks.csv", "cohort-spec.md", "table-spec.md", "source-record.yml",
    "transformation-record.md", "reproducibility-check.md", "ai-use.md", "component-score.csv",
    "review-disposition.md", "evidence/module-01-ai-use.md",
    "evidence/module-01-reproducibility-check.md", "evidence/module-02-ai-use.md",
    "evidence/module-02-validation-notes.md", "evidence/module-03-ai-use.md",
    "evidence/module-03-reproducibility-check.md", "release-manifest.csv",
) + tuple(f"outputs/first-extracts/{name}" for name in FIRST_EXTRACTS)
COMPLETE_RECORDS = (
    "README.md", "environment-note.md", "version-policy.md", "schema/data-model.mmd",
    "schema/schema-description.md", "schema/source-system-comparison.md", "schema/fhir-json-reading.md",
    "cohort-spec.md", "table-spec.md", "source-record.yml", "transformation-record.md",
    "reproducibility-check.md", "ai-use.md", "component-score.csv", "review-disposition.md",
    "sql/01-first-extracts.sql", "sql/02-index-cohort.sql", "sql/03-analytic-table.sql",
    "sql/04-validation.sql",
)


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


def validate_module03_subset(root: Path, checks: list[str]) -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-checkpoint1-module03-") as temp_dir:
        subset = Path(temp_dir) / "submission"
        (subset / "sql").mkdir(parents=True)
        (subset / "outputs").mkdir()
        mapping = {
            "README.md": root / "README.md",
            "VERSION": root / "VERSION",
            "ai-use.md": root / "ai-use.md",
            "cohort-spec.md": root / "cohort-spec.md",
            "data-dictionary.csv": root / "schema" / "analytic-data-dictionary.csv",
            "reproducibility-check.md": root / "reproducibility-check.md",
            "source-record.yml": root / "source-record.yml",
            "table-spec.md": root / "table-spec.md",
            "transformation-record.md": root / "transformation-record.md",
        }
        for relative, source in mapping.items():
            shutil.copy2(source, subset / relative)
        for name in ("01-eligible-events.sql", "02-index-cohort.sql", "03-analytic-table.sql", "04-validation.sql"):
            source_name = name if name != "01-eligible-events.sql" else None
            if source_name:
                shutil.copy2(root / "sql" / source_name, subset / "sql" / name)
            else:
                # The checkpoint intentionally begins at the Module 02 extract query. Eligible-event SQL is not in its four-file folder contract.
                shutil.copy2(PACKAGE_ROOT.parents[1] / "modules" / "03-cohorts-analytic-tables" / "sql" / name, subset / "sql" / name)
        for name in M3_OUTPUTS:
            shutil.copy2(root / "outputs" / name, subset / "outputs" / name)
        result = subprocess.run(
            [sys.executable, str(MODULE3_VALIDATOR), str(subset), "--submission"],
            capture_output=True,
            text=True,
            check=False,
        )
        require(result.returncode == 0, f"Embedded Module 03 validation passes: {result.stderr.strip() or result.stdout.strip()}", checks)


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    checks: list[str] = []
    require(root.is_dir(), "Checkpoint directory exists", checks)
    for relative in REQUIRED_FILES:
        require((root / relative).is_file(), f"Required file exists: {relative}", checks)
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version is 0.1.0", checks)

    for relative in COMPLETE_RECORDS:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII punctuation: {relative}", checks)
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}", checks)
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}", checks)

    requirements = (root / "requirements.txt").read_text(encoding="utf-8").splitlines()
    require(requirements == ["jupyterlab==4.6.3", "nbclient==0.10.2", "pandas==3.0.5"], "Requirement pins match", checks)

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "source_unit", "source_version", "bytes", "sha256"], "Release manifest header matches", checks)
    require(len(manifest) == 35, "Release manifest has 35 immutable files", checks)
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths), "Release manifest paths are sorted", checks)
    require(len(paths) == len(set(paths)), "Release manifest paths are unique", checks)
    for row in manifest:
        relative = row["relative_path"]
        require(not Path(relative).is_absolute() and ".." not in Path(relative).parts, f"Manifest path is relative: {relative}", checks)
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {relative}", checks)
        require(path.stat().st_size == int(row["bytes"]), f"Manifest byte count matches: {relative}", checks)
        require(assemble_checkpoint.sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {relative}", checks)

    source_header, source_manifest = read_csv(root / "schema" / "source-manifest.csv")
    require(len(source_manifest) == 16, "Source manifest has 16 tables", checks)
    require(sum(int(row["source_rows"]) for row in source_manifest) == 471_836, "Source manifest has 471836 rows", checks)
    require(sum(int(row["source_columns"]) for row in source_manifest) == 168, "Source manifest has 168 source fields", checks)
    require("source_sha256" in source_header, "Source manifest includes member fingerprints", checks)

    dictionary_header, dictionary = read_csv(root / "schema" / "data-dictionary.csv")
    require(len(dictionary) == 177, "Database dictionary has 177 fields", checks)
    require(len({(row["table_name"], row["database_field"]) for row in dictionary}) == 177, "Database dictionary keys are unique", checks)
    require(sum(row["included_in_core_view"] == "yes" for row in dictionary) == 27, "Database dictionary marks 27 core-view fields", checks)
    require("identity_like" in dictionary_header and "cost_or_coverage" in dictionary_header, "Database dictionary includes minimization flags", checks)

    analytic_header, analytic_dictionary = read_csv(root / "schema" / "analytic-data-dictionary.csv")
    require(len(analytic_dictionary) == 29, "Analytic dictionary has 29 fields", checks)
    require([int(row["position"]) for row in analytic_dictionary] == list(range(1, 30)), "Analytic dictionary positions are complete", checks)
    require({row["timing"] for row in analytic_dictionary} == {"key", "source", "index", "pre-index", "post-index", "metadata"}, "Analytic timing labels are complete", checks)
    require("field_name" in analytic_header, "Analytic dictionary names fields", checks)

    schema_sql = (root / "schema" / "schema.sql").read_text(encoding="utf-8").lower()
    for table in ("patients", "encounters", "conditions", "medications", "observations", "supplies"):
        require(f"create table {table}" in schema_sql, f"Schema declares table: {table}", checks)
    require("create view v_patients_minimal" in schema_sql and "create view v_encounters_core" in schema_sql and "create view v_observations_core" in schema_sql, "Schema declares three minimized views", checks)

    svg = (root / "schema" / "schema-diagram.svg").read_text(encoding="utf-8")
    require("<svg" in svg and "<title" in svg and "<desc" in svg, "Schema SVG has title and description", checks)
    if not starter:
        model = (root / "schema" / "data-model.mmd").read_text(encoding="utf-8").upper()
        for table in ("PATIENTS", "ENCOUNTERS", "OBSERVATIONS", "CONDITIONS", "MEDICATIONS", "SUPPLIES", "PAYER_TRANSITIONS"):
            require(table in model, f"Relationship model includes: {table}", checks)
        comparison = (root / "schema" / "source-system-comparison.md").read_text(encoding="utf-8").lower()
        for source_type in ("ehr", "claims", "registry", "survey", "operational", "fhir", "public aggregate", "synthetic"):
            require(source_type in comparison, f"Source-system comparison includes: {source_type}", checks)
        fhir = (root / "schema" / "fhir-json-reading.md").read_text(encoding="utf-8")
        require(all(item in fhir for item in ("Patient", "Encounter", "Observation", "00185faa-2760-4218-9bf5-db301acf8274")), "FHIR reading links three resources", checks)

    if not starter:
        extract_sql = (root / "sql" / "01-first-extracts.sql").read_text(encoding="utf-8").lower()
        require(extract_sql.count("-- query:") == 5, "First-extract SQL has five named queries", checks)
        for name in ("02-index-cohort.sql", "03-analytic-table.sql", "04-validation.sql"):
            sql = (root / "sql" / name).read_text(encoding="utf-8").lower()
            require("with " in sql and not re.search(r"\b(insert|update|delete|drop|alter|attach)\b", sql), f"Read-only WITH SQL: {name}", checks)

    registry_header, registry = read_csv(root / "outputs" / "first-extracts.csv")
    require(registry_header == ["output_name", "row_count", "bytes", "sha256"], "First-extract registry header matches", checks)
    require([row["output_name"] for row in registry] == sorted(FIRST_EXTRACTS), "First-extract registry is complete and sorted", checks)
    for row in registry:
        name = row["output_name"]
        expected_rows, expected_bytes, expected_sha = FIRST_EXTRACTS[name]
        path = root / "outputs" / "first-extracts" / name
        require(int(row["row_count"]) == expected_rows, f"First-extract row count matches: {name}", checks)
        require(int(row["bytes"]) == path.stat().st_size == expected_bytes, f"First-extract bytes match: {name}", checks)
        require(row["sha256"] == assemble_checkpoint.sha256(path) == expected_sha, f"First-extract SHA-256 matches: {name}", checks)

    for name, (expected_rows, expected_bytes, expected_sha) in M3_OUTPUTS.items():
        path = root / "outputs" / name
        _, rows = read_csv(path)
        require(len(rows) == expected_rows, f"Module 03 row count matches: {name}", checks)
        require(path.stat().st_size == expected_bytes, f"Module 03 bytes match: {name}", checks)
        require(assemble_checkpoint.sha256(path) == expected_sha, f"Module 03 SHA-256 matches: {name}", checks)

    for relative in ("outputs/first-extracts.csv", "release-manifest.csv"):
        require(b"\r\n" not in (root / relative).read_bytes(), f"Generated CSV uses LF: {relative}", checks)

    for relative in REQUIRED_FILES:
        if relative.startswith("evidence/"):
            require((root / relative).stat().st_size >= 150, f"Preserved evidence is substantive: {relative}", checks)

    score_header, scores = read_csv(root / "component-score.csv")
    require(score_header == ["criterion", "component", "course_points_available", "points_earned", "status", "evidence"], "Component-score header matches", checks)
    require(len(scores) == 7, "Component score has seven criteria", checks)
    require(sum(int(row["course_points_available"]) for row in scores) == 40, "Component points total 40", checks)
    require(sum(int(row["course_points_available"]) for row in scores if row["component"] == "Module 01 setup") == 15, "Setup component totals 15", checks)
    require(sum(int(row["course_points_available"]) for row in scores if row["component"] == "Module 03 SQL cohort") == 25, "SQL cohort component totals 25", checks)

    if not starter:
        earned = [int(row["points_earned"]) for row in scores]
        require(all(0 <= value <= int(row["course_points_available"]) for value, row in zip(earned, scores, strict=True)), "Earned points are in range", checks)
        require(sum(earned) >= 32, "Passing reference score is at least 32", checks)
        require(all(row["status"] in {"pass", "pass with conditions"} for row in scores), "All scored criteria pass", checks)
        review = (root / "review-disposition.md").read_text(encoding="utf-8").lower()
        match = re.search(r"(?m)^disposition:\s*(accept with conditions|accept|revise|refer)\s*$", review)
        require(bool(match), "Review has an allowed disposition", checks)
        require(match.group(1) in {"accept", "accept with conditions"}, "Reference disposition permits Module 04", checks)
        require("senior clinical data analyst" in review and "course instructor" in review, "Both decision owners are recorded", checks)
        validate_module03_subset(root, checks)

    report = {
        "status": "pass",
        "mode": "starter" if starter else "complete",
        "checks_passed": len(checks),
        "checks": checks,
        "manifest_rows": len(manifest),
        "course_points": 40,
    }
    print(f"FND-1 Checkpoint 1 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-checkpoint1-validate-") as temp_dir:
        root = Path(temp_dir) / "checkpoint-1"
        assemble_checkpoint.assemble(root, reference=True)
        validate(root)
        (root / "outputs" / "query-checks.csv").unlink()
        try:
            validate(root)
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted a checkpoint with a missing required output.")
    print("FND-1 Checkpoint 1 validator self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.checkpoint:
            parser.error("provide a checkpoint folder or --self-check")
        validate(args.checkpoint.resolve(), args.starter)
    except (OSError, ValueError, KeyError, ValidationError) as exc:
        parser.exit(1, f"Validation failed: {exc}\n")


if __name__ == "__main__":
    main()
