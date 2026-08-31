"""Validate APP-3 final clinical performance improvement packages."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal
from pathlib import Path
from typing import Callable


CHECKPOINT_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = CHECKPOINT_ROOT.parent.parent
MODULE_ROOT = COURSE_ROOT / "modules/07-clinician-leadership-defense"
MODULE_ASSEMBLER = MODULE_ROOT / "assemble_candidate.py"
ASSEMBLER = CHECKPOINT_ROOT / "assemble_final.py"
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
REVIEW_RECORDS = (
    "submission-record.md", "final-score.csv", "gate-results.csv", "final-defense.md",
    "reviewer-record.md", "final-reproduction.md", "conditions-register.csv",
    "final-audit.md", "final-decision.md", "release-acceptance.md",
)
FINAL_FILES = {
    "final-review/CHECKPOINT-VERSION", "final-review/checkpoint1-release.json",
    "final-review/checkpoint2-release.json", "final-review/module07-release.json",
    "final-review/candidate-manifest.csv", *(f"final-review/{name}" for name in REVIEW_RECORDS),
}
FINAL_MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]
MODULE_MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]
MODULE_MANIFEST_BYTES = 75470
MODULE_MANIFEST_SHA256 = "cd88ad1910ca35d231da734f919f58420e2f3f25deda9135ee6ca8c20105d2fc"
MODULE_RELEASE_SHA256 = "5dcec682080346570e89915473a9b2939c15cf57a28a15250137694d056486e2"
CP1_RELEASE_SHA256 = "270b4e49d1c21d8faf7243cd11cef1dddea836d32be551dfe72edac771b31f27"
CP2_RELEASE_SHA256 = "b8af80b7e07c2eac2aeb0e9206533bfae134f55d69a5df9038a7a9a915c4dd05"
SCORE_MAXIMUMS = {
    "E01": Decimal("8.00"), "C01": Decimal("9.00"), "L01": Decimal("8.00"),
    "M01": Decimal("6.00"), "H01": Decimal("4.00"),
}
ALLOWED_DISPOSITIONS = {"accept", "accept with conditions", "revise", "refer"}
ALLOWED_RECOMMENDATIONS = {"run bounded prospective improvement test", "revise before testing", "refer", "stop"}
REVIEWER_ROLES = (
    "APP-3 faculty owner", "Joe Joseph, MD, SFHM, clinician of record", "Local clinical decision owner",
    "Safety reviewer", "Improvement and simulation reviewer", "Operations and capacity reviewer",
    "Workforce reviewer", "Access and equity reviewer", "Measurement and statistical-process reviewer",
    "Forecasting reviewer", "Responsible-AI and ML reviewer", "Accessibility and communication reviewer",
    "Independent reproducer",
)


class ValidationError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def markdown_field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\.?\s*$", text)
    return match.group(1).strip() if match else None


def run_validator(script: Path, target: Path) -> None:
    result = subprocess.run([sys.executable, str(script), str(target)], capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValidationError(result.stderr.strip() or result.stdout.strip())


def validate(root: Path, starter: bool = False, nested: bool = True) -> dict[str, object]:
    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    require(root.is_dir(), "Final package directory exists")
    require(all((root / path).is_file() for path in FINAL_FILES), "All 15 final-review files are present")
    require((root / "final-review/CHECKPOINT-VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Final checkpoint version matches")

    final_header, final_manifest = read_csv(root / "final-review/candidate-manifest.csv")
    require(final_header == FINAL_MANIFEST_FIELDS, "Final candidate manifest header matches")
    require(len(final_manifest) == 416, "Final candidate manifest has 416 rows")
    candidate_paths = [row["relative_path"] for row in final_manifest]
    require(candidate_paths == sorted(candidate_paths) and len(set(candidate_paths)) == 416, "Final candidate paths are sorted and unique")
    for row in final_manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts and "\\" not in row["relative_path"], f"Portable candidate path: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        require(bool(row["role"]), f"Candidate role is present: {row['relative_path']}")
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    require(actual == set(candidate_paths) | FINAL_FILES and len(actual) == 431, "Final package has exactly 431 expected files")

    module_header, module_manifest = read_csv(root / "release-manifest.csv")
    require(module_header == MODULE_MANIFEST_FIELDS and len(module_manifest) == 389, "Module 07 immutable manifest has 389 rows")
    require((root / "release-manifest.csv").stat().st_size == MODULE_MANIFEST_BYTES and sha256(root / "release-manifest.csv") == MODULE_MANIFEST_SHA256, "Module 07 manifest fingerprint matches")
    require(sha256(root / "final-review/checkpoint1-release.json") == CP1_RELEASE_SHA256, "Checkpoint 01 release identity matches")
    require(sha256(root / "final-review/checkpoint2-release.json") == CP2_RELEASE_SHA256, "Checkpoint 02 release identity matches")
    require(sha256(root / "final-review/module07-release.json") == MODULE_RELEASE_SHA256, "Module 07 release identity matches")
    require(sha256(root / "evidence/provenance/checkpoint1-release.json") == CP1_RELEASE_SHA256, "Nested Checkpoint 01 release identity matches")
    require(sha256(root / "evidence/provenance/checkpoint2-release.json") == CP2_RELEASE_SHA256, "Nested Checkpoint 02 release identity matches")

    if nested:
        with tempfile.TemporaryDirectory(prefix="app3-final-candidate-validate-") as temp_dir:
            candidate = Path(temp_dir) / "candidate"
            candidate.mkdir()
            for relative_text in candidate_paths:
                relative = Path(relative_text)
                destination = candidate / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(root / relative, destination)
            run_validator(candidate / "validate_candidate.py", candidate)
        checks.append("Reconstructed Module 07 candidate validates")

    review_root = root / "final-review"
    for name in REVIEW_RECORDS:
        text = (review_root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if starter:
            require(bool(PLACEHOLDER.search(text)), f"Starter prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Final review record is complete: {name}")

    csv_headers = {
        "final-score.csv": ["criterion_id", "criterion", "maximum", "score", "evidence", "status"],
        "gate-results.csv": ["gate_id", "gate", "result", "evidence", "reviewer", "condition_id"],
        "conditions-register.csv": ["condition_id", "condition", "owner", "due_point", "evidence", "verifier", "status", "escalation_trigger"],
    }
    tables: dict[str, list[dict[str, str]]] = {}
    for name, expected_header in csv_headers.items():
        header, rows = read_csv(review_root / name)
        require(header == expected_header, f"CSV header matches: {name}")
        require(bool(rows), f"CSV has at least one row: {name}")
        tables[name] = rows

    if starter:
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "candidate_files": 416, "assembled_files": 431}
        print(f"APP-3 final starter validation passed: {len(checks)} checks.")
        return report

    submission = (review_root / "submission-record.md").read_text(encoding="utf-8")
    manifest = review_root / "candidate-manifest.csv"
    require(markdown_field(submission, "Final candidate manifest bytes") == str(manifest.stat().st_size), "Submission final-manifest bytes match")
    require(markdown_field(submission, "Final candidate manifest SHA-256") == sha256(manifest), "Submission final-manifest SHA-256 matches")
    submission_values = (
        "https://github.com/ShuhanCS/open-clinical-learning-commons", "`416`", "`389`", "`75470`",
        MODULE_MANIFEST_SHA256, CP1_RELEASE_SHA256, CP2_RELEASE_SHA256, MODULE_RELEASE_SHA256,
        "official last day of the assigned MGH Institute half-term",
        "app3-clinical-performance-improvement-candidate-v0.1.0", "proposed - not created",
        "https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf",
    )
    require(all(value in submission for value in submission_values), "Submission identities calendar and tag status match")

    scores = tables["final-score.csv"]
    require([row["criterion_id"] for row in scores] == list(SCORE_MAXIMUMS), "Final score criteria are in fixed order")
    require(all(Decimal(row["maximum"]) == SCORE_MAXIMUMS[row["criterion_id"]] for row in scores), "Final score maximums match")
    total = sum(Decimal(row["score"]) for row in scores)
    require(all(Decimal("0") <= Decimal(row["score"]) <= Decimal(row["maximum"]) for row in scores) and total >= Decimal("28.00"), "Final scores are bounded and meet the minimum")
    require(total == Decimal("35.00") and all(row["status"] == "pass" for row in scores), "Reference final score is 35.00 of 35.00")
    for row in scores:
        require((root / Path(row["evidence"])).is_file(), f"Final score evidence exists: {row['criterion_id']}")

    conditions = tables["conditions-register.csv"]
    condition_ids = {row["condition_id"] for row in conditions}
    require(len(conditions) == 12 and [row["condition_id"] for row in conditions] == [f"C{i:02d}" for i in range(1, 13)], "Twelve final conditions are ordered")
    require(all(row["owner"] and row["due_point"] and row["evidence"] and row["verifier"] and row["status"] == "open" and row["escalation_trigger"] for row in conditions), "Every final condition has complete open ownership")
    for row in conditions:
        require((root / Path(row["evidence"])).is_file(), f"Condition evidence exists: {row['condition_id']}")

    gates = tables["gate-results.csv"]
    require(len(gates) == 26 and [row["gate_id"] for row in gates] == [f"G{i:02d}" for i in range(1, 27)], "Twenty-six final gates are ordered")
    require(all(row["result"] in {"pass", "pass with condition"} for row in gates), "Every final gate passes or passes with an allowed condition")
    require(all((not row["condition_id"] and row["result"] == "pass") or (row["condition_id"] in condition_ids and row["result"] == "pass with condition") for row in gates), "Final gate conditions are consistent and registered")
    require(all((root / Path(row["evidence"])).is_file() for row in gates), "Every final gate cites existing evidence")

    defense = (review_root / "final-defense.md").read_text(encoding="utf-8")
    require(markdown_field(defense, "Defense status") == "adequate for curriculum construction", "Final defense status is adequate")
    require(re.findall(r"(?m)^## Q(\d{2})\.", defense) == [f"{i:02d}" for i in range(1, 15)], "All 14 final defense answers are ordered")
    require(all(len(section.strip()) >= 160 for section in re.split(r"(?m)^## Q\d{2}\..*$", defense)[1:]), "Every final defense answer is substantive")
    defense_terms = (
        "root cause", "876.924084", "805.136639 to 970.733035", "86.671644", "S00", "S01", "S02", "S03",
        "No unavailable or unsupported value", "zero automatic actions", "0.731788", "0.750000", "Silence is not agreement",
        "Agent output is not evidence", "clinical test is not yet supported",
    )
    require(all(term in defense for term in defense_terms), "Final defense preserves every material decision boundary")

    reviewer = (review_root / "reviewer-record.md").read_text(encoding="utf-8")
    require(all(role in reviewer for role in REVIEWER_ROLES), "All 13 final reviewer roles are present")
    require("Completed named human reviews claimed: `none`" in reviewer and "does not claim" in reviewer, "Reviewer record preserves pending human status")

    reproduction = (review_root / "final-reproduction.md").read_text(encoding="utf-8")
    require(markdown_field(reproduction, "Final candidate manifest bytes") == str(manifest.stat().st_size), "Reproduction final-manifest bytes match")
    require(markdown_field(reproduction, "Final candidate manifest SHA-256") == sha256(manifest), "Reproduction final-manifest SHA-256 matches")
    require(all(value in reproduction for value in ("`416`", "`431`", "`389`", "Module 07 validator: `pass`", "Two-build match: `pass`", "pending before alpha")), "Final reproduction package results match")

    audit = (review_root / "final-audit.md").read_text(encoding="utf-8")
    audit_values = (
        "416 rows", "389 rows", "all 3 copied release records match", "none found", "20 of 20", "17 of 17",
        "40 plus 25 plus 35 equals 100", "selected scenario remains none", "seasonal exponential smoothing",
        "failed R01", "separate and consistent", "prohibited", "pass with conditions for curriculum construction",
    )
    require(all(value in audit for value in audit_values), "Final audit covers identity evidence accountability score and decisions")

    decision = (review_root / "final-decision.md").read_text(encoding="utf-8")
    disposition = markdown_field(decision, "Package disposition")
    recommendation = markdown_field(decision, "Clinical performance recommendation")
    require(disposition in ALLOWED_DISPOSITIONS and recommendation in ALLOWED_RECOMMENDATIONS, "Final package and clinical decisions are allowed")
    expected_decision = {
        "Final score": "35.00 of 35.00", "Score destination": "Checkpoint 03 exactly once",
        "Course score": "40 + 25 + 35 = 100", "Gates": "26 of 26 pass or pass with an allowed condition",
        "Defense": "adequate for curriculum construction", "Package disposition": "accept with conditions",
        "Clinical performance recommendation": "revise before testing", "Selected scenario": "none",
        "Accepted forecast": "seasonal exponential smoothing", "ML decision": "retain transparent forecast",
        "Open conditions": "C01 through C12", "Clinical action": "prohibited", "Staffing change": "prohibited",
        "Schedule change": "prohibited", "Automated action": "prohibited", "Test start": "prohibited",
        "Implementation": "prohibited", "Production scoring": "prohibited", "Model deployment": "prohibited",
        "Course status": "complete for curriculum construction only",
        "Proposed tag": "app3-clinical-performance-improvement-candidate-v0.1.0",
        "Tag status": "proposed - not created",
        "Tag authorization": "pending named human approval and exact-commit verification",
    }
    require(all(markdown_field(decision, key) == value for key, value in expected_decision.items()), "Reference final decisions score and authority boundary match")

    module_progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(module_progression, "Clinical performance recommendation") == recommendation, "Final recommendation matches Module 07")
    require(markdown_field(module_progression, "Package status") == disposition, "Final package disposition matches Module 07")
    require(markdown_field(module_progression, "Accepted forecast") == "seasonal exponential smoothing" and markdown_field(module_progression, "Selected scenario") == "none", "Final forecast and scenario decisions match Module 07")

    acceptance = (review_root / "release-acceptance.md").read_text(encoding="utf-8")
    acceptance_values = (
        "curriculum construction", "Clinical action", "staffing or schedule change", "automated action", "test start",
        "implementation", "production scoring", "model deployment", "Any changed candidate byte requires a new Module 07 version",
        "proposed and not created",
    )
    require(all(value in acceptance for value in acceptance_values), "Release acceptance states allowed use change rule prohibitions and tag status")

    report = {
        "status": "pass", "mode": "complete", "checks_passed": len(checks),
        "candidate_files": 416, "assembled_files": 431, "manifest_rows": 416,
        "score": str(total), "gates_passed": 26, "conditions": 12,
        "package_disposition": disposition, "clinical_performance_recommendation": recommendation,
    }
    print(f"APP-3 final complete validation passed: {len(checks)} checks.")
    return report


def replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"Mutation source is absent in {path.name}: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def append(path: Path) -> None:
    path.write_text(path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8", newline="\n")


def command(args: list[str]) -> None:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode:
        raise AssertionError(result.stderr.strip() or result.stdout.strip())


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app3-final-validate-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        command([sys.executable, str(ASSEMBLER), "--target", str(reference), "--reference"])
        complete = validate(reference)

        candidate = base / "candidate"
        command([sys.executable, str(MODULE_ASSEMBLER), "--target", str(candidate), "--reference"])
        starter = base / "starter"
        command([sys.executable, str(ASSEMBLER), "--candidate", str(candidate), "--target", str(starter)])
        starter_report = validate(starter, starter=True)

        routes: list[tuple[str, Callable[[Path], None]]] = [
            ("changed-candidate", lambda root: append(root / "evidence-synthesis.md")),
            ("changed-release", lambda root: append(root / "final-review/module07-release.json")),
            ("invalid-score", lambda root: replace(root / "final-review/final-score.csv", "8.00,8.00", "8.00,1.00")),
            ("failed-gate", lambda root: replace(root / "final-review/gate-results.csv", ",pass,final-review/submission-record.md", ",fail,final-review/submission-record.md")),
            ("early-tag", lambda root: replace(root / "final-review/final-decision.md", "proposed - not created", "created")),
            ("changed-recommendation", lambda root: replace(root / "final-review/final-decision.md", "revise before testing", "run bounded prospective improvement test")),
            ("false-test-authorization", lambda root: replace(root / "final-review/final-decision.md", "Test start: `prohibited`", "Test start: `authorized`")),
            ("changed-forecast", lambda root: replace(root / "final-review/final-decision.md", "seasonal exponential smoothing", "gradient boosted")),
            ("selected-scenario", lambda root: replace(root / "final-review/final-decision.md", "Selected scenario: `none`", "Selected scenario: `S01`")),
            ("hidden-unavailable", lambda root: replace(root / "final-review/final-defense.md", "No unavailable or unsupported value", "Every missing value")),
            ("missing-reviewer", lambda root: replace(root / "final-review/reviewer-record.md", "Independent reproducer", "Package observer")),
            ("closed-condition", lambda root: replace(root / "final-review/conditions-register.csv", ",open,", ",closed,")),
            ("incomplete-defense", lambda root: replace(root / "final-review/final-defense.md", "## Q14.", "## Closing question.")),
            ("hidden-agent-use", lambda root: replace(root / "final-review/final-defense.md", "Agent output is not evidence", "Agent output is evidence")),
            ("duplicate-final-score", lambda root: replace(root / "final-review/final-decision.md", "40 + 25 + 35 = 100", "40 + 25 + 35 + 35 = 135")),
        ]
        for name, mutate in routes:
            target = base / f"mutation-{name}"
            shutil.copytree(reference, target)
            mutate(target)
            try:
                validate(target, nested=False)
            except (ValidationError, OSError, ValueError, KeyError, json.JSONDecodeError):
                pass
            else:
                raise AssertionError(f"Validator accepted {name} mutation")

        try:
            validate(starter, nested=False)
        except ValidationError as error:
            assert "Final review record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted learner prompts as complete")

    print(
        f"APP-3 final validator self-check passed: {complete['checks_passed']} complete checks and "
        f"{starter_report['checks_passed']} starter checks; 15 failure routes and complete-mode template rejection verified."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if args.package is None:
            parser.error("package is required unless --self-check is used")
        print(json.dumps(validate(args.package, starter=args.starter), indent=2))
    except (ValidationError, OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
