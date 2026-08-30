"""Validate the FND-2 Module 02 reference, starter, or learner submission."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
from pathlib import Path

import build_regression_evidence as builder


MODULE_ROOT = Path(__file__).resolve().parent
OUTPUT_CSVS = (
    "linear-subset-registry.csv", "linear-coefficients.csv", "linear-diagnostics.csv",
    "linear-prediction-examples.csv", "logistic-coefficients.csv", "logistic-diagnostics.csv",
    "logistic-prediction-examples.csv", "model-matrix-fields.csv", "model-comparison.csv",
    "sparse-cell-checks.csv", "assumption-register.csv", "r-reading-fixture.csv",
    "regression-checks.csv",
)
OUTPUT_FILES = tuple(f"outputs/{name}" for name in OUTPUT_CSVS) + ("outputs/build-report.json",)
LEARNER_FILES = (
    "README.md", "VERSION", "requirements.txt", "data-spec.md", "source-record.yml",
    "formula-registry.csv", "reference-levels.csv", "interpretation-quantity-guide.csv",
    "regression-interpretation.md", "environment-note.md", "reproducibility-check.md",
    "r-run-record.md", "ai-use.md", "progression-decision.md", "assessment.md",
    "paired-models.R", "build_regression_evidence.py", "validate_regression_evidence.py",
    "data/modeling-cohort.csv", "data/split-registry.csv", "data/baseline-metrics.csv",
    "data/feature-role-contract.csv",
) + OUTPUT_FILES
RELEASE_FILES = (
    "README.md", "VERSION", "requirements.txt", "data-spec.md", "source-record.yml",
    "formula-registry.csv", "reference-levels.csv", "interpretation-quantity-guide.csv",
    "regression-interpretation.md", "environment-note.md", "reproducibility-check.md",
    "r-run-record.md", "ai-use.md", "progression-decision.md", "assessment.md",
    "instructor-notes.md", "paired-models.R", "build_regression_evidence.py",
    "validate_regression_evidence.py", "release.json",
) + OUTPUT_FILES
TEXT_FILES = (
    "README.md", "data-spec.md", "source-record.yml", "regression-interpretation.md",
    "environment-note.md", "reproducibility-check.md", "r-run-record.md", "ai-use.md",
    "progression-decision.md", "assessment.md",
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

    with tempfile.TemporaryDirectory(prefix="fnd2-module02-expected-") as temp_dir:
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
        actual_report = json.loads((root / "outputs" / "build-report.json").read_text(encoding="utf-8"))
        check(actual_report == expected_report, "Build report content changed.")

    formula_fields, formula_rows = read_csv(root / "formula-registry.csv")
    check(len(formula_fields) == 7, "Formula registry must contain seven fields.")
    check(len(formula_rows) == 4, "Formula registry must contain four models.")
    if mode != "starter":
        check([row["model_id"] for row in formula_rows] == ["LIN01", "LOG01", "LOG02", "LOG03"], "Formula model IDs changed.")
        check(all(row["fit_partition"].startswith("train") for row in formula_rows), "Every formula must use training data only.")

    reference_fields, reference_rows = read_csv(root / "reference-levels.csv")
    check(len(reference_fields) == 6, "Reference registry must contain six fields.")
    check(len(reference_rows) == 5, "Reference registry must contain five rows.")

    guide_fields, guide_rows = read_csv(root / "interpretation-quantity-guide.csv")
    check(len(guide_fields) == 4, "Interpretation guide must contain four fields.")
    check(len(guide_rows) == 9, "Interpretation guide must contain nine quantity rows.")

    r_script = (root / "paired-models.R").read_text(encoding="utf-8")
    for phrase in ("lm(", "glm(", "binomial(link = \"logit\")", "confint.default", "write.csv"):
        check(phrase in r_script, f"Paired R script is missing: {phrase}")
    check("C:\\Users\\" not in r_script, "Paired R script contains a local absolute path.")

    for name in TEXT_FILES:
        text = (root / name).read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {name}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {name}.")
        if mode == "release":
            check("REPLACE:" not in text, f"Unresolved reference prompt found in {name}.")
        elif mode == "submission":
            check("REPLACE" not in text, f"Unresolved prompt found in {name}.")
    for name in ("formula-registry.csv", "reference-levels.csv", "interpretation-quantity-guide.csv"):
        if mode in {"release", "submission"}:
            check("REPLACE" not in (root / name).read_text(encoding="utf-8"), f"Unresolved prompt found in {name}.")

    interpretation = (root / "regression-interpretation.md").read_text(encoding="utf-8").lower()
    if mode != "starter":
        check("structural blanks" in interpretation and "causal" in interpretation, "Interpretation must preserve missingness and causal boundaries.")
        check("log odds" in interpretation or "log-odds" in interpretation, "Interpretation must name the logistic coefficient scale.")
    decision = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
    if mode != "starter":
        check(any(value in decision for value in ("`accept`", "`accept with conditions`", "`revise`", "`refer`")), "Allowed Module 03 disposition missing.")
    if mode == "submission":
        check("0.000001" in (root / "r-run-record.md").read_text(encoding="utf-8"), "R reconciliation tolerance missing.")

    if mode == "release":
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["id"] == "oclc-fnd2-02", "Release module ID changed.")
        check(release["module"]["version"] == "0.1.0", "Release module version changed.")
        check(release["module"]["commons_release"] == "0.40.0", "Commons release changed.")
        check(release["module"]["hours"] == 16.0, "Module hours changed.")
        check(release["upstream"]["modeling_cohort_sha256"] == builder.UPSTREAM["modeling-cohort.csv"][1], "Release upstream fingerprint changed.")
        check(release["linear_case"]["all_available_rows"] == 111, "Release linear subset changed.")
        check(release["linear_case"]["training_fit_rows"] == 69, "Release linear fit rows changed.")
        check(release["linear_case"]["structural_blanks"] == 263, "Release structural blank count changed.")
        check(release["logistic_case"]["training_rows"] == 224, "Release logistic rows changed.")
        check(release["logistic_case"]["positive_outcomes"] == 25, "Release logistic outcomes changed.")
        for name in OUTPUT_CSVS:
            path = root / "outputs" / name
            metadata = release["outputs"][name]
            check(metadata["bytes"] == path.stat().st_size, f"Release byte count changed: {name}")
            check(metadata["sha256"] == builder.sha256(path), f"Release SHA-256 changed: {name}")
        check(release["decision"]["reference"] == "accept with conditions", "Reference disposition changed.")
    return checks, errors


def self_check() -> None:
    release_checks, release_errors = validate(MODULE_ROOT, "release")
    assert not release_errors, release_errors
    with tempfile.TemporaryDirectory(prefix="fnd2-module02-validator-") as temp_dir:
        fixture = Path(temp_dir) / "starter"
        builder.build_workspace(builder.upstream_paths(), fixture)
        starter_checks, starter_errors = validate(fixture, "starter")
        assert not starter_errors, starter_errors
        _, submission_errors = validate(fixture, "submission")
        assert submission_errors and any("Unresolved prompt" in error for error in submission_errors)
        broken = Path(temp_dir) / "broken"
        shutil.copytree(fixture, broken)
        (broken / "outputs" / "linear-coefficients.csv").unlink()
        _, broken_errors = validate(broken, "starter")
        assert broken_errors and any("Missing required file" in error for error in broken_errors)
    print(f"FND-2 Module 02 validator self-check passed: {release_checks} release checks and {starter_checks} starter checks; incomplete and broken submissions rejected.")


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
        raise SystemExit(f"FND-2 Module 02 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-2 Module 02 {args.mode} validation passed: {checks} checks.")


if __name__ == "__main__":
    main()
