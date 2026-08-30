"""Validate the FND-2 Module 04 reference, starter, or learner submission."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
from pathlib import Path

import build_validity_evidence as builder


MODULE_ROOT = Path(__file__).resolve().parent
OUTPUT_CSVS = (
    "treatment-fixture.csv", "repeated-measures-fixture.csv", "survival-fixture.csv",
    "analytic-aim-validity-map.csv", "dag-nodes.csv", "dag-edges.csv",
    "propensity-predictions.csv", "overlap-table.csv", "balance-table.csv",
    "adjustment-estimates.csv", "selection-profile.csv", "missingness-profile.csv",
    "missingness-mechanisms.csv", "longitudinal-models.csv", "mixed-variance.csv",
    "kaplan-meier-table.csv", "cox-reading.csv", "validity-threat-register.csv",
    "validity-checks.csv",
)
OUTPUT_BINARY = ("dag.svg",)
OUTPUT_FILES = tuple(f"outputs/{name}" for name in OUTPUT_CSVS + OUTPUT_BINARY) + ("outputs/build-report.json",)
DECISION_FILES = (
    "causal-claim-screen.md", "dag-narrative.md", "validity-adjustment-longitudinal-memo.md",
    "mixed-model-reading.md", "survival-censoring-reading.md", "specialist-referrals.md",
    "reproducibility-check.md", "accessibility-review.md", "ai-use.md", "progression-decision.md",
)
PORTABLE_FILES = ("requirements.txt", "data-spec.md", "source-record.yml", "assessment.md", "dag.mmd", "paired-longitudinal-survival.R")
LEARNER_FILES = (
    ".gitattributes", ".gitignore", "README.md", "VERSION", *PORTABLE_FILES, *DECISION_FILES,
    "build_validity_evidence.py", "validate_validity_evidence.py",
) + tuple(f"data/{name}" for name in builder.UPSTREAM) + OUTPUT_FILES
RELEASE_FILES = (
    ".gitattributes", ".gitignore", "README.md", "VERSION", *PORTABLE_FILES, *DECISION_FILES,
    "instructor-notes.md", "build_validity_evidence.py", "validate_validity_evidence.py", "release.json",
) + OUTPUT_FILES
TEXT_FILES = ("README.md", "data-spec.md", "source-record.yml", "assessment.md", "dag.mmd", *DECISION_FILES)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def paths_for(root: Path) -> dict[str, Path]:
    data = root / "data"
    return builder.upstream_paths(data) if data.is_dir() else builder.upstream_paths()


def rows_by(path: Path, field: str) -> dict[str, dict[str, str]]:
    _, rows = read_csv(path)
    return {row[field]: row for row in rows}


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

    with tempfile.TemporaryDirectory(prefix="fnd2-module04-expected-") as temp_dir:
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

    report = json.loads((root / "outputs" / "build-report.json").read_text(encoding="utf-8"))
    check(report["selection_case"] == {"cohort_rows": 374, "timing_rows": 111, "structural_blanks": 263}, "Selection case changed.")
    check(report["treatment_case"] == {"rows": 600, "treated": 255, "missing_severity": 91, "known_ate": "-6.00000000"}, "Treatment case changed.")
    check(report["repeated_case"] == {"rows": 2400, "people": 600, "visits_per_person": 4}, "Repeated case changed.")
    check(report["survival_case"] == {"rows": 600, "events": 449, "censored": 151}, "Survival case changed.")
    check(report["decision"]["reference"] == "continue with conditions", "Reference decision changed.")

    aims = rows_by(root / "outputs" / "analytic-aim-validity-map.csv", "aim_id")
    estimates = rows_by(root / "outputs" / "adjustment-estimates.csv", "method")
    variance = rows_by(root / "outputs" / "mixed-variance.csv", "component")
    cox = rows_by(root / "outputs" / "cox-reading.csv", "term")
    checks_table = rows_by(root / "outputs" / "validity-checks.csv", "check_id")
    check(set(aims) == {"V01", "V02", "V03", "V04", "V05"}, "Aim map changed.")
    check(estimates["known synthetic truth"]["estimate_treated_minus_untreated"] == "-6.00000000", "Known effect changed.")
    check(estimates["unadjusted"]["estimate_treated_minus_untreated"] == "-1.27214587", "Unadjusted estimate changed.")
    check(estimates["complete-case IPTW"]["rows"] == "509", "Complete-case population changed.")
    check(variance["intraclass_correlation"]["variance"] == "0.83598751", "ICC changed.")
    check(cox["treatment"]["hazard_ratio"] == "0.67945425", "Treatment hazard ratio changed.")
    check(len(checks_table) == 16 and all(row["status"] == "pass" for row in checks_table.values()), "Invariant checks must be 16 of 16 pass.")

    dag = (root / "dag.mmd").read_text(encoding="utf-8")
    check(dag.count("-->") == 18, "Editable DAG must contain 18 directed edges.")
    for token in ("Age", "Baseline severity", "Comorbidity count", "Site", "Clinical preference", "Treatment", "Early response", "30-day symptom score", "Complete severity record"):
        check(token in dag, f"Editable DAG missing node: {token}")
    r_script = (root / "paired-longitudinal-survival.R").read_text(encoding="utf-8")
    for token in ("nlme::lme", "survival::Surv", "survival::survfit", "survival::coxph"):
        check(token in r_script, f"Paired R reading missing: {token}")

    for name in TEXT_FILES:
        text = (root / name).read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {name}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {name}.")
        if mode == "release":
            check("REPLACE:" not in text, f"Unresolved reference prompt found in {name}.")
        elif mode == "submission":
            check("REPLACE" not in text, f"Unresolved prompt found in {name}.")

    if mode != "starter":
        memo = (root / "validity-adjustment-longitudinal-memo.md").read_text(encoding="utf-8").lower()
        mixed = (root / "mixed-model-reading.md").read_text(encoding="utf-8").lower()
        survival = (root / "survival-censoring-reading.md").read_text(encoding="utf-8").lower()
        progression = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
        check("-6.00000000" in memo and "-1.27214587" in memo, "Memo must compare known and unadjusted effects.")
        check("91" in memo and "263" in memo, "Memo must preserve missingness and structural-blank counts.")
        check("600" in mixed and "2,400" in mixed and "0.83598751" in mixed, "Mixed reading must preserve unit and ICC evidence.")
        check("449" in survival and "151" in survival and "0.67945425" in survival, "Survival reading must preserve event, censoring, and hazard-ratio evidence.")
        check("risk ratio" in survival and "probability" in survival and "causal" in survival, "Survival quantity boundaries are incomplete.")
        check(any(value in progression for value in ("continue with conditions", "`revise`", "`stop`")), "Allowed Module 05 disposition missing.")

    if mode == "release":
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["id"] == "oclc-fnd2-04", "Release module ID changed.")
        check(release["module"]["version"] == "0.1.0", "Release module version changed.")
        check(release["module"]["commons_release"] == "0.43.0", "Commons release changed.")
        check(release["module"]["hours"] == 16.5, "Module hours changed.")
        check(release["cases"] == {"selection_rows": 374, "selected_timing_rows": 111, "structural_blanks": 263, "treatment_rows": 600, "missing_severity": 91, "repeated_rows": 2400, "repeated_people": 600, "survival_rows": 600, "events": 449, "censored": 151}, "Release case counts changed.")
        check(release["reference_results"]["known_ate"] == "-6.00000000", "Release known ATE changed.")
        check(release["reference_results"]["icc"] == "0.83598751", "Release ICC changed.")
        check(release["reference_results"]["treatment_hazard_ratio"] == "0.67945425", "Release hazard ratio changed.")
        for name in OUTPUT_CSVS + OUTPUT_BINARY:
            path = root / "outputs" / name
            metadata = release["outputs"][name]
            check(metadata["bytes"] == path.stat().st_size, f"Release byte count changed: {name}")
            check(metadata["sha256"] == builder.sha256(path), f"Release SHA-256 changed: {name}")
        check(release["decision"]["reference"] == "continue with conditions", "Release decision changed.")
    return checks, errors


def self_check() -> None:
    release_checks, release_errors = validate(MODULE_ROOT, "release")
    assert not release_errors, release_errors
    with tempfile.TemporaryDirectory(prefix="fnd2-module04-validator-") as temp_dir:
        fixture = Path(temp_dir) / "starter"
        builder.build_workspace(builder.upstream_paths(), fixture)
        starter_checks, starter_errors = validate(fixture, "starter")
        assert not starter_errors, starter_errors
        _, submission_errors = validate(fixture, "submission")
        assert submission_errors and any("Unresolved prompt" in error for error in submission_errors)
        broken = Path(temp_dir) / "broken"
        shutil.copytree(fixture, broken)
        (broken / "outputs" / "balance-table.csv").unlink()
        _, broken_errors = validate(broken, "starter")
        assert broken_errors and any("Missing required file" in error for error in broken_errors)
    print(f"FND-2 Module 04 validator self-check passed: {release_checks} release checks and {starter_checks} starter checks; incomplete and broken submissions rejected.")


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
        raise SystemExit(f"FND-2 Module 04 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-2 Module 04 {args.mode} validation passed: {checks} checks.")


if __name__ == "__main__":
    main()
