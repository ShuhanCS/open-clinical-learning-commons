"""Validate the FND-2 Module 03 reference, starter, or learner submission."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
from pathlib import Path

import build_prediction_evidence as builder


MODULE_ROOT = Path(__file__).resolve().parent
OUTPUT_CSVS = (
    "resampling-results.csv", "validation-predictions.csv", "validation-comparison.csv",
    "model-selection-record.csv", "threshold-table.csv", "threshold-decision.csv",
    "test-predictions.csv", "test-metrics.csv", "confusion-table.csv",
    "calibration-table.csv", "subgroup-metrics.csv", "transformed-feature-names.csv",
    "leaked-model-failure.csv", "prediction-checks.csv",
)
OUTPUT_BINARY = ("calibration.svg", "threshold.svg")
OUTPUT_FILES = tuple(f"outputs/{name}" for name in OUTPUT_CSVS + OUTPUT_BINARY) + ("outputs/build-report.json",)
LEARNER_FILES = (
    "README.md", "VERSION", "requirements.txt", "data-spec.md", "source-record.yml",
    "model-contract.json", "assessment.md", "prediction-evaluation-report.md",
    "figure-accessibility.md", "environment-note.md", "reproducibility-check.md",
    "ai-use.md", "progression-decision.md", "build_prediction_evidence.py",
    "validate_prediction_evidence.py", "data/modeling-cohort.csv", "data/split-registry.csv",
    "data/baseline-metrics.csv", "data/feature-role-contract.csv", "data/formula-registry.csv",
    "data/model-matrix-fields.csv", "data/assumption-register.csv",
) + OUTPUT_FILES
RELEASE_FILES = (
    "README.md", "VERSION", "requirements.txt", "data-spec.md", "source-record.yml",
    "model-contract.json", "assessment.md", "instructor-notes.md",
    "prediction-evaluation-report.md", "figure-accessibility.md", "environment-note.md",
    "reproducibility-check.md", "ai-use.md", "progression-decision.md",
    "build_prediction_evidence.py", "validate_prediction_evidence.py", "release.json",
) + OUTPUT_FILES
TEXT_FILES = (
    "README.md", "data-spec.md", "source-record.yml", "assessment.md",
    "prediction-evaluation-report.md", "figure-accessibility.md", "environment-note.md",
    "reproducibility-check.md", "ai-use.md", "progression-decision.md",
)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def paths_for(root: Path) -> dict[str, Path]:
    data = root / "data"
    return builder.upstream_paths(data) if data.is_dir() else builder.upstream_paths()


def validate(root: Path, mode: str) -> tuple[int, list[str]]:
    checks = 0
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            errors.append(message)

    required = RELEASE_FILES if mode == "release" else LEARNER_FILES
    for name in required:
        check((root / name).is_file(), f"Missing required file: {name}")
    if errors:
        return checks, errors

    check((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "VERSION must be 0.1.0.")
    paths = paths_for(root)
    try:
        builder.verify_upstream(paths)
    except (FileNotFoundError, ValueError) as error:
        check(False, str(error))
        return checks, errors
    for name, (size, digest) in builder.UPSTREAM.items():
        check(paths[name].stat().st_size == size, f"Upstream byte count changed: {name}")
        check(builder.sha256(paths[name]) == digest, f"Upstream SHA-256 changed: {name}")

    with tempfile.TemporaryDirectory(prefix="fnd2-module03-expected-") as temp_dir:
        expected_root = Path(temp_dir) / "outputs"
        expected_report = builder.build_outputs(paths, expected_root)
        for name in OUTPUT_CSVS:
            actual_fields, actual_rows = read_csv(root / "outputs" / name)
            expected_fields, expected_rows = read_csv(expected_root / name)
            check(actual_fields == expected_fields, f"Output fields changed: {name}")
            check(len(actual_rows) == len(expected_rows), f"Output row count changed: {name}")
            if len(actual_rows) != len(expected_rows):
                continue
            for row_number, (actual, expected) in enumerate(zip(actual_rows, expected_rows, strict=True), start=1):
                for field in expected_fields:
                    check(actual.get(field) == expected.get(field), f"{name} row {row_number} changed: {field}")
        for name in OUTPUT_BINARY:
            check((root / "outputs" / name).read_bytes() == (expected_root / name).read_bytes(), f"Output bytes changed: {name}")
        actual_report = json.loads((root / "outputs" / "build-report.json").read_text(encoding="utf-8"))
        check(actual_report == expected_report, "Build report content changed.")

    contract = json.loads((root / "model-contract.json").read_text(encoding="utf-8"))
    check(contract["module"] == "oclc-fnd2-03", "Model contract module changed.")
    check(contract["module_version"] == "0.1.0", "Model contract version changed.")
    check(contract["seed"] == builder.SEED, "Model contract seed changed.")
    check(contract["models"]["LEAK01"]["eligible"] is False, "Leaked model must remain ineligible.")
    check(contract["selection_rule"]["selected_model"] == "ML01", "Selected model contract changed.")
    check(contract["threshold_rule"]["locked_threshold"] == "0.08513264", "Locked threshold contract changed.")
    check(contract["threshold_rule"]["locked_before_test"] is True, "Threshold must remain locked before test.")
    check(contract["bootstrap"]["replicates"] == 2000, "Bootstrap replicate contract changed.")

    for name in TEXT_FILES:
        text = (root / name).read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {name}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {name}.")
        if mode == "release":
            check("REPLACE:" not in text, f"Unresolved reference prompt found in {name}.")
        elif mode == "submission":
            check("REPLACE" not in text, f"Unresolved prompt found in {name}.")

    report = (root / "prediction-evaluation-report.md").read_text(encoding="utf-8").lower()
    decision = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
    if mode != "starter":
        check("four" in report and "outcome" in report, "Report must keep the four-outcome test limit visible.")
        check("leak" in report, "Report must explain leakage failure.")
        check("23" in report and "false positive" in report, "Report must interpret exact false-positive evidence.")
        check("deployment" in report, "Report must state the deployment boundary.")
        check(any(value in decision for value in ("continue to validity review", "`revise`", "`stop`")), "Allowed Checkpoint 1 recommendation missing.")

    if mode == "release":
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["id"] == "oclc-fnd2-03", "Release module ID changed.")
        check(release["module"]["version"] == "0.1.0", "Release module version changed.")
        check(release["module"]["commons_release"] == "0.41.0", "Commons release changed.")
        check(release["module"]["hours"] == 16.5, "Module hours changed.")
        check(release["upstream"]["modeling_cohort_sha256"] == builder.UPSTREAM["modeling-cohort.csv"][1], "Release upstream fingerprint changed.")
        check(release["partitions"] == {"train": 224, "validation": 75, "test": 75, "training_outcomes": 25, "validation_outcomes": 7, "test_outcomes": 4}, "Release partitions changed.")
        check(release["selection"]["model_id"] == "ML01", "Release selected model changed.")
        check(release["selection"]["locked_threshold"] == "0.08513264", "Release threshold changed.")
        check(release["test_confusion"] == {"true_negative": 48, "false_positive": 23, "false_negative": 2, "true_positive": 2}, "Release test confusion changed.")
        for name in OUTPUT_CSVS + OUTPUT_BINARY:
            path = root / "outputs" / name
            metadata = release["outputs"][name]
            check(metadata["bytes"] == path.stat().st_size, f"Release byte count changed: {name}")
            check(metadata["sha256"] == builder.sha256(path), f"Release SHA-256 changed: {name}")
        check(release["decision"]["reference"] == "continue to validity review with conditions", "Reference recommendation changed.")
    return checks, errors


def self_check() -> None:
    release_checks, release_errors = validate(MODULE_ROOT, "release")
    assert not release_errors, release_errors
    with tempfile.TemporaryDirectory(prefix="fnd2-module03-validator-") as temp_dir:
        fixture = Path(temp_dir) / "starter"
        builder.build_workspace(builder.upstream_paths(), fixture)
        starter_checks, starter_errors = validate(fixture, "starter")
        assert not starter_errors, starter_errors
        _, submission_errors = validate(fixture, "submission")
        assert submission_errors and any("Unresolved prompt" in error for error in submission_errors)
        broken = Path(temp_dir) / "broken"
        shutil.copytree(fixture, broken)
        (broken / "outputs" / "test-predictions.csv").unlink()
        _, broken_errors = validate(broken, "starter")
        assert broken_errors and any("Missing required file" in error for error in broken_errors)
    print(f"FND-2 Module 03 validator self-check passed: {release_checks} release checks and {starter_checks} starter checks; incomplete and broken submissions rejected.")


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
        raise SystemExit(f"FND-2 Module 03 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-2 Module 03 {args.mode} validation passed: {checks} checks.")


if __name__ == "__main__":
    main()
