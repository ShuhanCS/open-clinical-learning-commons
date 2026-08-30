"""Validate the FND-2 Module 06 reference, starter, or learner submission."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import tempfile
from pathlib import Path

import build_agent_test_evidence as builder


MODULE_ROOT = Path(__file__).resolve().parent
OUTPUT_CSVS = ("accepted-artifact-manifest.csv", "accepted-contract-tests.csv", "seeded-failure-results.csv", "independent-verification.csv", "claim-adjudication.csv", "data-class-rules.csv", "test-summary.csv")
OUTPUT_TEXT = ("failure-fixtures.json", "test-summary.md")
OUTPUT_FILES = tuple(f"outputs/{name}" for name in OUTPUT_CSVS + OUTPUT_TEXT) + ("outputs/build-report.json",)
RECORD_FILES = ("agent-task-plan.md", "prompt-trace-log.csv", "agent-critique.md", "claim-adjudication.csv", "independent-verification.md", "human-sign-off.md", "reproducibility-check.md", "accessibility-review.md", "ai-use.md", "progression-decision.md")
PORTABLE_FILES = ("requirements.txt", "data-spec.md", "source-record.yml", "test-contract.json", "prompt-constraints.md", "assessment.md")
LEARNER_FILES = (".gitattributes", ".gitignore", "README.md", "VERSION", *PORTABLE_FILES, *RECORD_FILES, "run_contract_tests.py", "build_agent_test_evidence.py", "validate_agent_test_evidence.py") + tuple(f"data/{name}" for name in builder.UPSTREAM) + OUTPUT_FILES
RELEASE_FILES = (".gitattributes", ".gitignore", "README.md", "VERSION", *PORTABLE_FILES, *RECORD_FILES, "instructor-notes.md", "run_contract_tests.py", "build_agent_test_evidence.py", "validate_agent_test_evidence.py", "release.json") + OUTPUT_FILES
TEXT_FILES = ("README.md", "data-spec.md", "source-record.yml", "prompt-constraints.md", "assessment.md", *RECORD_FILES)


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
        check(paths[name].stat().st_size == size, f"Upstream bytes changed: {name}")
        check(builder.sha256(paths[name]) == digest, f"Upstream SHA-256 changed: {name}")

    with tempfile.TemporaryDirectory(prefix="fnd2-module06-expected-") as temp_dir:
        expected_root = Path(temp_dir) / "outputs"
        expected_report = builder.build_outputs(paths, expected_root)
        for name in OUTPUT_CSVS:
            actual_fields, actual_rows = read_csv(root / "outputs" / name)
            expected_fields, expected_rows = read_csv(expected_root / name)
            check(actual_fields == expected_fields, f"Output fields changed: {name}")
            check(len(actual_rows) == len(expected_rows), f"Output rows changed: {name}")
            if len(actual_rows) == len(expected_rows):
                for row_number, (actual, expected) in enumerate(zip(actual_rows, expected_rows, strict=True), start=1):
                    for field in expected_fields:
                        check(actual.get(field) == expected.get(field), f"{name} row {row_number} changed: {field}")
        for name in OUTPUT_TEXT:
            check((root / "outputs" / name).read_bytes() == (expected_root / name).read_bytes(), f"Output bytes changed: {name}")
        actual_report = json.loads((root / "outputs" / "build-report.json").read_text(encoding="utf-8"))
        check(actual_report == expected_report, "Build report changed.")

    _, manifest = read_csv(root / "outputs" / "accepted-artifact-manifest.csv")
    _, accepted = read_csv(root / "outputs" / "accepted-contract-tests.csv")
    _, failures = read_csv(root / "outputs" / "seeded-failure-results.csv")
    _, verifications = read_csv(root / "outputs" / "independent-verification.csv")
    _, claims = read_csv(root / "outputs" / "claim-adjudication.csv")
    _, data_classes = read_csv(root / "outputs" / "data-class-rules.csv")
    _, summaries = read_csv(root / "outputs" / "test-summary.csv")
    check(len(manifest) == 13 and all(row["status"] == "accepted unchanged" for row in manifest), "Artifact manifest changed.")
    check(len(accepted) == 18 and all(row["status"] == "pass" for row in accepted), "Accepted tests must be 18 of 18 pass.")
    check(len(failures) == 10 and all(row["status"] == "pass" and row["rejected"] == "yes" and row["intended_reason"] == "yes" for row in failures), "All ten failures must reject for intended codes.")
    check([row["observed_code"] for row in failures] == ["LEAKAGE_FIELD", "TEST_ROW_IN_FIT", "LABEL_INVERTED", "SPLIT_CHANGED", "FUTURE_ROW_IN_FIT", "CONFUSION_DENOMINATOR", "CALIBRATION_BIN_OMITTED", "FINGERPRINT_CHANGED", "USE_BOUNDARY_MISSING", "AGENT_CLAIM_UNVERIFIED"], "Failure codes changed.")
    check(len(verifications) == 3 and all(row["status"] == "pass" for row in verifications), "Independent verifications changed.")
    check(len(claims) == 4 and {row["adjudication"] for row in claims} == {"accept", "modify", "reject"}, "Claim adjudications changed.")
    check(len(data_classes) == 7, "Data-class rules changed.")
    check(len(summaries) == 7 and all(row["status"] == "pass" for row in summaries), "Summary gates changed.")

    contract = json.loads((root / "test-contract.json").read_text(encoding="utf-8"))
    check(contract["module"] == "oclc-fnd2-06" and contract["module_version"] == "0.1.0", "Test contract identity changed.")
    check(contract["accepted_artifacts"] == 13 and contract["accepted_contract_tests"] == 18 and contract["seeded_failures"] == 10, "Test contract counts changed.")
    check(contract["human_owner_required"] is True, "Human-owner requirement changed.")

    for name in TEXT_FILES:
        text = (root / name).read_text(encoding="utf-8")
        check("C:\\Users\\" not in text, f"Local absolute path found in {name}.")
        check("\u2013" not in text and "\u2014" not in text, f"Unicode dash found in {name}.")
        if mode == "release":
            check("REPLACE" not in text, f"Unresolved reference prompt found in {name}.")
        elif mode == "submission":
            check("REPLACE" not in text, f"Unresolved prompt found in {name}.")

    if mode != "starter":
        signoff = (root / "human-sign-off.md").read_text(encoding="utf-8").lower()
        progression = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
        check("human" in signoff and "sign" in signoff and "pending" in signoff if mode == "release" else "pending" not in signoff, "Human sign-off status is incomplete.")
        check(any(value in progression for value in ("accept week 6 gate", "revise module 06", "return affected upstream module", "refer responsible-ai", "`stop`")), "Allowed progression disposition missing.")
        check("clinical" in progression and "deployment" in progression, "Use boundaries missing from progression.")

    if mode == "release":
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        check(release["module"]["id"] == "oclc-fnd2-06" and release["module"]["version"] == "0.1.0", "Release identity changed.")
        check(release["module"]["commons_release"] == "0.45.0" and release["module"]["hours"] == 16.0, "Release version or hours changed.")
        check(release["tests"] == {"accepted_artifacts": 13, "accepted_tests": 18, "seeded_failures": 10, "independent_verifications": 3, "agent_claims": 4, "summary_gates": 7}, "Release test counts changed.")
        for name in OUTPUT_CSVS + OUTPUT_TEXT:
            path = root / "outputs" / name
            metadata = release["outputs"][name]
            check(metadata["bytes"] == path.stat().st_size, f"Release bytes changed: {name}")
            check(metadata["sha256"] == builder.sha256(path), f"Release SHA-256 changed: {name}")
        check(release["decision"]["reference"] == "accept Week 6 gate and continue to Checkpoint 2 with conditions", "Release decision changed.")
    return checks, errors


def self_check() -> None:
    release_checks, release_errors = validate(MODULE_ROOT, "release")
    assert not release_errors, release_errors
    with tempfile.TemporaryDirectory(prefix="fnd2-module06-validator-") as temp_dir:
        fixture = Path(temp_dir) / "starter"
        builder.build_workspace(builder.upstream_paths(), fixture)
        starter_checks, starter_errors = validate(fixture, "starter")
        assert not starter_errors, starter_errors
        _, submission_errors = validate(fixture, "submission")
        assert submission_errors and any("Unresolved prompt" in error or "sign-off" in error for error in submission_errors)
        broken = Path(temp_dir) / "broken"
        shutil.copytree(fixture, broken)
        (broken / "outputs" / "seeded-failure-results.csv").unlink()
        _, broken_errors = validate(broken, "starter")
        assert broken_errors and any("Missing required file" in error for error in broken_errors)
    print(f"FND-2 Module 06 validator self-check passed: {release_checks} release checks and {starter_checks} starter checks; incomplete and broken submissions rejected.")


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
        raise SystemExit(f"FND-2 Module 06 validation failed: {len(errors)} error(s) across {checks} checks.")
    print(f"FND-2 Module 06 {args.mode} validation passed: {checks} checks.")


if __name__ == "__main__":
    main()
