"""Validate the FND-2 Module 01 reference, starter, or learner submission."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
from pathlib import Path

import build_modeling_workspace as builder


MODULE_ROOT = Path(__file__).resolve().parent
OUTPUT_FILES = (
    "outputs/modeling-cohort.csv",
    "outputs/split-registry.csv",
    "outputs/baseline-metrics.csv",
    "outputs/modeling-checks.csv",
    "outputs/build-report.json",
)
LEARNER_RECORDS = (
    "README.md",
    "VERSION",
    "requirements.txt",
    "data-spec.md",
    "source-record.yml",
    "aim-classification-exercises.csv",
    "aim-and-method-plan.md",
    "estimand-target-registry.csv",
    "feature-role-contract.csv",
    "environment-note.md",
    "reproducibility-check.md",
    "ai-use.md",
    "progression-decision.md",
    "assessment.md",
    "build_modeling_workspace.py",
    "validate_modeling_workspace.py",
    "data/resolved-analytic-table.csv",
) + OUTPUT_FILES
RELEASE_RECORDS = (
    "README.md",
    "VERSION",
    "requirements.txt",
    "data-spec.md",
    "source-record.yml",
    "aim-classification-exercises.csv",
    "aim-and-method-plan.md",
    "estimand-target-registry.csv",
    "feature-role-contract.csv",
    "environment-note.md",
    "reproducibility-check.md",
    "ai-use.md",
    "progression-decision.md",
    "assessment.md",
    "instructor-notes.md",
    "release.json",
    "build_modeling_workspace.py",
    "validate_modeling_workspace.py",
) + OUTPUT_FILES
TEXT_RECORDS = (
    "README.md", "data-spec.md", "source-record.yml", "aim-and-method-plan.md",
    "environment-note.md", "reproducibility-check.md", "ai-use.md",
    "progression-decision.md", "assessment.md",
)
EXPECTED_AIMS = ["descriptive", "associational", "predictive", "causal", "longitudinal", "forecasting"]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def source_for(root: Path) -> Path:
    local = root / "data" / "resolved-analytic-table.csv"
    return local if local.is_file() else builder.default_source()


def validate(root: Path, mode: str) -> tuple[int, list[str]]:
    checks = 0
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            errors.append(message)

    required = RELEASE_RECORDS if mode == "release" else LEARNER_RECORDS
    for name in required:
        check((root / name).is_file(), f"Missing required file: {name}")
    if errors:
        return checks, errors

    check((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "VERSION must be 0.1.0.")
    source_path = source_for(root)
    try:
        source_rows = builder.verify_source(source_path)
    except (FileNotFoundError, ValueError) as error:
        check(False, str(error))
        return checks, errors
    check(source_path.stat().st_size == builder.SOURCE_BYTES, "Source byte count changed.")
    check(builder.sha256(source_path) == builder.SOURCE_SHA256, "Source SHA-256 changed.")

    expected_cohort, expected_registry = builder.derive_rows(source_rows)
    expected_baseline = builder.baseline_rows(expected_registry)
    expected_checks = builder.check_rows(expected_cohort, expected_registry, expected_baseline)
    expected_by_name = {
        "modeling-cohort.csv": expected_cohort,
        "split-registry.csv": expected_registry,
        "baseline-metrics.csv": expected_baseline,
        "modeling-checks.csv": expected_checks,
    }
    expected_fields = {
        "modeling-cohort.csv": list(builder.SOURCE_FIELDS + builder.DERIVED_FIELDS),
        "split-registry.csv": list(expected_registry[0]),
        "baseline-metrics.csv": list(expected_baseline[0]),
        "modeling-checks.csv": list(expected_checks[0]),
    }
    actual_by_name: dict[str, list[dict[str, str]]] = {}
    for name, expected_rows in expected_by_name.items():
        fields, actual_rows = read_csv(root / "outputs" / name)
        actual_by_name[name] = actual_rows
        check(fields == expected_fields[name], f"{name} fields or field order changed.")
        check(len(actual_rows) == len(expected_rows), f"{name} row count changed.")
        if len(actual_rows) != len(expected_rows):
            continue
        for row_number, (actual, expected) in enumerate(zip(actual_rows, expected_rows, strict=True), start=1):
            for field, value in expected.items():
                check(actual.get(field) == str(value), f"{name} row {row_number} changed: {field}")

    report = json.loads((root / "outputs" / "build-report.json").read_text(encoding="utf-8"))
    check(report["status"] == "pass", "Build report status changed.")
    check(report["version"] == "0.1.0", "Build report version changed.")
    check(report["source"]["sha256"] == builder.SOURCE_SHA256, "Build report source fingerprint changed.")
    check(report["split"]["train"]["rows"] == 224, "Build report train rows changed.")
    check(report["split"]["validation"]["rows"] == 75, "Build report validation rows changed.")
    check(report["split"]["test"]["rows"] == 75, "Build report test rows changed.")
    check(report["split"]["train"]["positives"] == 25, "Build report train positives changed.")
    check(report["split"]["validation"]["positives"] == 7, "Build report validation positives changed.")
    check(report["split"]["test"]["positives"] == 4, "Build report test positives changed.")
    check(report["baseline"]["constant_probability"] == "0.111607142857", "Build report baseline changed.")

    feature_fields, feature_rows = read_csv(root / "feature-role-contract.csv")
    check(feature_fields == ["field_name", "origin", "role", "available_at_prediction_time", "default_predictor", "use_condition", "leakage_action", "reason"], "Feature-role columns changed.")
    check(len(feature_rows) == 34, "Feature-role contract must contain 34 rows.")
    check(len({row["field_name"] for row in feature_rows}) == 34, "Feature-role field names must be unique.")
    check({row["field_name"] for row in feature_rows} == set(builder.SOURCE_FIELDS + builder.DERIVED_FIELDS), "Feature-role fields do not match the modeling cohort.")
    if mode != "starter":
        default_predictors = {row["field_name"] for row in feature_rows if row["default_predictor"] == "yes"}
        blocked = {row["field_name"] for row in feature_rows if row["leakage_action"] == "block"}
        check(default_predictors == builder.ALLOWED_PREDICTORS, "Default predictor set changed.")
        check(builder.PROHIBITED_PREDICTORS <= blocked, "One or more prohibited predictors are not blocked.")

    registry_fields, target_rows = read_csv(root / "estimand-target-registry.csv")
    check(len(registry_fields) == 12, "Estimand-target registry must contain 12 fields.")
    check(len(target_rows) == 6, "Estimand-target registry must contain six rows.")
    if mode != "starter":
        check([row["aim"] for row in target_rows] == EXPECTED_AIMS, "Estimand-target aim sequence changed.")

    exercise_fields, exercise_rows = read_csv(root / "aim-classification-exercises.csv")
    check(len(exercise_fields) == 6, "Aim exercise table must contain six fields.")
    check(len(exercise_rows) == 12, "Aim exercise table must contain twelve rows.")

    for name in TEXT_RECORDS:
        text = (root / name).read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {name}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {name}.")
        if mode == "release":
            check("REPLACE:" not in text, f"Unresolved prompt found in {name}.")
        elif mode == "submission":
            check("REPLACE" not in text, f"Unresolved prompt found in {name}.")
    for name in ("feature-role-contract.csv", "estimand-target-registry.csv"):
        text = (root / name).read_text(encoding="utf-8")
        if mode in {"release", "submission"}:
            check("REPLACE" not in text, f"Unresolved prompt found in {name}.")
    if mode == "submission":
        check("REPLACE" not in (root / "aim-classification-exercises.csv").read_text(encoding="utf-8"), "Aim exercises are incomplete.")

    decision = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
    if mode != "starter":
        check(any(value in decision for value in ("`accept`", "`accept with conditions`", "`revise`", "`refer`")), "Allowed progression disposition missing.")

    if mode == "release":
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["id"] == "oclc-fnd2-01", "Release module ID changed.")
        check(release["module"]["version"] == "0.1.0", "Release module version changed.")
        check(release["module"]["commons_release"] == "0.39.0", "Commons release changed.")
        check(release["module"]["hours"] == 15.5, "Module hours changed.")
        check(release["source"]["sha256"] == builder.SOURCE_SHA256, "Release source fingerprint changed.")
        for name in expected_by_name:
            metadata = release["outputs"][name]
            path = root / "outputs" / name
            check(metadata["bytes"] == path.stat().st_size, f"Release byte count changed for {name}.")
            check(metadata["sha256"] == builder.sha256(path), f"Release fingerprint changed for {name}.")
        check(release["decision"]["reference"] == "accept with conditions", "Reference disposition changed.")
    return checks, errors


def self_check() -> None:
    release_checks, release_errors = validate(MODULE_ROOT, "release")
    assert not release_errors, release_errors
    with tempfile.TemporaryDirectory(prefix="fnd2-module01-validator-") as temp_dir:
        fixture = Path(temp_dir) / "starter"
        builder.build_workspace(builder.default_source(), fixture)
        starter_checks, starter_errors = validate(fixture, "starter")
        assert not starter_errors, starter_errors
        submission_checks, submission_errors = validate(fixture, "submission")
        assert submission_errors and any("Unresolved prompt" in error or "incomplete" in error for error in submission_errors)
        broken = Path(temp_dir) / "broken"
        shutil.copytree(fixture, broken)
        (broken / "outputs" / "baseline-metrics.csv").unlink()
        broken_checks, broken_errors = validate(broken, "starter")
        assert broken_errors and any("Missing required file" in error for error in broken_errors)
    print(f"FND-2 Module 01 validator self-check passed: {release_checks} release checks and {starter_checks} starter checks; incomplete and broken submissions rejected.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=MODULE_ROOT)
    parser.add_argument("--mode", choices=("release", "starter", "submission"), default="release")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    checks, errors = validate(args.root.resolve(), args.mode)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(f"FND-2 Module 01 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-2 Module 01 {args.mode} validation passed: {checks} checks.")


if __name__ == "__main__":
    main()
