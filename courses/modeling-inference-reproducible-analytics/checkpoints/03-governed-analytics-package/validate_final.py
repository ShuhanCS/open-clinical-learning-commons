"""Validate an assembled FND-2 final governed analytics package."""

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


PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
REVIEW_RECORDS = (
    "submission-record.md", "final-score.csv", "gate-results.csv", "final-defense.md",
    "reviewer-record.md", "final-reproduction.md", "conditions-register.csv",
    "final-audit.md", "final-decision.md", "release-acceptance.md",
)
FINAL_FILES = {
    "final-review/CHECKPOINT-VERSION", "final-review/checkpoint2-release.json",
    "final-review/module07-release.json",
    "final-review/candidate-manifest.csv",
    *(f"final-review/{name}" for name in REVIEW_RECORDS),
}
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]
CRITERIA = ("M01", "R01", "E01", "V01", "G01", "H01")
AVAILABLE = tuple(Decimal(value) for value in ("5.00", "6.00", "7.00", "5.00", "6.00", "6.00"))
GATES = tuple(f"G{index:02d}" for index in range(1, 28))
REVIEWER_ROLES = (
    "FND-2 faculty owner", "biostatistical methods", "clinical informatics",
    "model evaluation", "forecasting", "accessibility", "privacy and data governance",
    "responsible AI", "independent reproduction",
)
PACKAGE_DISPOSITIONS = {"accept", "accept with conditions", "revise", "refer"}
MODEL_USES = {"teaching use only", "silent prospective validation only", "revise before further validation", "stop model use"}
RELEASE_HASHES = {
    "evidence/checkpoint2/prior-checkpoint/release.json": "03c147d2e75cd446a43b9d56e49495df69af90d42d2b14ad4d860aea9d67239f",
    "final-review/checkpoint2-release.json": "b58316081496f42d473b823fac88ed8e6c981e47afb11d0c4856c9f39627d761",
    "final-review/module07-release.json": "a2fccdcd096a066337f1de856cb9610f6b389db15c90dff1627af1cbf30ac96e",
}
MODULE_MANIFEST_SHA256 = "ab2537e278ea549b8152434df0a21438394d28caa6031b03e9a570a27db07c1b"
SOURCE_COMMIT = "31c69e9152d797f49e5d8968eb1dd5ea53090568"
TAG = "fnd2-governed-candidate-v0.1.0"


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


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValidationError(f"Path is not portable: {value}")
    return path


def field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    require(root.is_dir(), "Final package directory exists")
    review = root / "final-review"
    for relative in FINAL_FILES:
        require((root / relative).is_file(), f"Required final file exists: {relative}")
    require((review / "CHECKPOINT-VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Final checkpoint version is 0.1.0")

    header, manifest = read_csv(review / "candidate-manifest.csv")
    require(header == MANIFEST_FIELDS, "Candidate manifest header matches")
    require(len(manifest) == 168, "Candidate manifest has 168 rows")
    candidate_paths = [row["relative_path"] for row in manifest]
    require(candidate_paths == sorted(candidate_paths) and len(set(candidate_paths)) == 168, "Candidate manifest paths are sorted and unique")
    for row in manifest:
        relative = safe_relative(row["relative_path"])
        require(not row["relative_path"].startswith("final-review/"), f"Candidate path excludes final review: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        require(bool(row["role"].strip()), f"Candidate role is present: {row['relative_path']}")
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    require(actual == set(candidate_paths) | FINAL_FILES and len(actual) == 182, "Final package has exactly 182 expected files")

    require(sha256(root / "release-manifest.csv") == MODULE_MANIFEST_SHA256, "Module 07 immutable manifest matches")
    module_manifest_header, module_manifest = read_csv(root / "release-manifest.csv")
    require(module_manifest_header == ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"] and len(module_manifest) == 143, "Module 07 manifest has 143 registered rows")
    for relative, digest in RELEASE_HASHES.items():
        require(sha256(root / relative) == digest, f"Accepted release fingerprint matches: {relative}")

    with tempfile.TemporaryDirectory(prefix="fnd2-final-validate-") as temp_dir:
        candidate = Path(temp_dir) / "candidate"
        candidate.mkdir()
        for row in manifest:
            relative = safe_relative(row["relative_path"])
            destination = candidate / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / relative, destination)
        result = subprocess.run(
            [sys.executable, str(candidate / "validate_candidate.py"), str(candidate)],
            capture_output=True, text=True, check=False,
        )
        require(result.returncode == 0, "Reconstructed Module 07 candidate passes complete validation")

    for name in REVIEW_RECORDS:
        text = (review / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {name}")

    score_header, scores = read_csv(review / "final-score.csv")
    require(score_header == ["criterion_id", "criterion", "course_points_available", "points_earned", "status", "evidence"], "Final score header matches")
    require(tuple(row["criterion_id"] for row in scores) == CRITERIA, "Final score criteria match")
    require(tuple(Decimal(row["course_points_available"]) for row in scores) == AVAILABLE and sum(AVAILABLE) == Decimal("35.00"), "Available points total 35.00")
    earned_total: Decimal | None = None
    if not starter:
        earned = tuple(Decimal(row["points_earned"]) for row in scores)
        require(all(Decimal("0") <= value <= available for value, available in zip(earned, AVAILABLE, strict=True)), "Earned points are in range")
        earned_total = sum(earned)
        require(earned_total >= Decimal("28.00"), "Earned points meet 28.00 minimum")
        require(all(row["status"] in {"pass", "pass with conditions"} and row["evidence"].strip() for row in scores), "All final score rows pass and cite evidence")

    gate_header, gates = read_csv(review / "gate-results.csv")
    require(gate_header == ["gate_id", "gate", "status", "evidence", "reviewer", "condition_id"] and tuple(row["gate_id"] for row in gates) == GATES, "Final gate contract has 27 ordered gates")
    condition_header, conditions = read_csv(review / "conditions-register.csv")
    require(condition_header == ["condition_id", "source", "status", "condition", "owner", "due_point", "evidence_required", "verifier", "escalation_trigger"] and len(conditions) >= 1, "Condition register contract matches")
    if not starter:
        require(all(all(row[column].strip() for column in condition_header) for row in conditions), "Every condition is complete")
        condition_ids = {row["condition_id"] for row in conditions}
        require(all(row["status"] in {"pass", "pass with condition"} and row["evidence"].strip() and row["reviewer"].strip() for row in gates), "All final gates pass with evidence and reviewers")
        require(all(row["condition_id"] == "NONE" or row["condition_id"] in condition_ids for row in gates), "Every gate condition is registered")
        require(all((row["status"] == "pass with condition") == (row["condition_id"] != "NONE") for row in gates), "Gate statuses and condition links agree")

    defense = (review / "final-defense.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\d+\.", defense)) == 15, "Final defense has 15 numbered answers")
    if not starter:
        require(field(defense, "Status") == "adequate", "Final defense is adequate")

    reviewer = (review / "reviewer-record.md").read_text(encoding="utf-8")
    for role in REVIEWER_ROLES:
        require(role.lower() in reviewer.lower(), f"Reviewer role is present: {role}")
    if not starter:
        require(field(reviewer, "Final decision owner") is not None and field(reviewer, "Human sign-off scope") is not None, "Reviewer ownership and sign-off scope are present")

    submission = (review / "submission-record.md").read_text(encoding="utf-8")
    if not starter:
        require(field(submission, "Full candidate source commit") == SOURCE_COMMIT, "Submission records exact candidate source commit")
        require(field(submission, "Candidate files") == "168" and field(submission, "Candidate manifest rows") == "168", "Submission candidate counts match")
        require(field(submission, "Candidate manifest bytes") == str((review / "candidate-manifest.csv").stat().st_size), "Submission candidate manifest bytes match")
        require(field(submission, "Candidate manifest SHA-256") == sha256(review / "candidate-manifest.csv"), "Submission candidate manifest SHA-256 matches")
        require(field(submission, "Proposed annotated tag") == TAG and field(submission, "Tag status") == "proposed - not created", "Submission records uncreated proposed tag")

    reproduction = (review / "final-reproduction.md").read_text(encoding="utf-8").lower()
    audit = (review / "final-audit.md").read_text(encoding="utf-8").lower()
    if not starter:
        for phrase in ("module 07 complete validation", "candidate manifest comparison", "checkpoint 1 release comparison", "checkpoint 2 release comparison", "module 07 release comparison", "hidden dependency scan", "independent reproducer"):
            require(phrase in reproduction, f"Reproduction includes: {phrase}")
        for phrase in ("source and rights", "accessibility", "agent and human accountability", "evidence coverage", "structured alternatives", "prohibited-data"):
            require(phrase in audit, f"Final audit includes: {phrase}")

    decision = (review / "final-decision.md").read_text(encoding="utf-8")
    acceptance = (review / "release-acceptance.md").read_text(encoding="utf-8")
    if not starter:
        package = field(decision, "Package disposition")
        model_use = field(decision, "Model-use recommendation")
        require(package in PACKAGE_DISPOSITIONS and model_use in MODEL_USES, "Final package and model-use values are allowed")
        require(package != model_use, "Package disposition and model-use recommendation are separate")
        require(field(decision, "Gate result") is not None and field(decision, "Defense result") is not None, "Final gate and defense results are recorded")
        require(field(decision, "Proposed annotated tag") == TAG and field(decision, "Proposed tag target") == SOURCE_COMMIT, "Final decision records exact proposed tag target")
        require(field(decision, "Tag status") == "proposed - not created" and field(decision, "Tag authorization") is not None, "Final tag remains uncreated and authorization is explicit")
        require(earned_total is not None and field(decision, "Final score") == f"{earned_total:.2f} of 35.00", "Final decision score matches score table")
        require(field(acceptance, "Package disposition") == package and field(acceptance, "Model-use recommendation") == model_use, "Release acceptance agrees with final decision")
        candidate_use = field((root / "model-use-recommendation.md").read_text(encoding="utf-8"), "Model-use recommendation")
        require(candidate_use == model_use, "Final decision agrees with governed candidate model-use recommendation")
        require((package in {"accept", "accept with conditions"}) and "not deployment permission" in decision.lower(), "Accepting package remains separate from deployment")

    report = {
        "status": "pass", "mode": "starter" if starter else "complete",
        "checks_passed": len(checks), "candidate_files": 168,
        "assembled_files": 182, "course_points": "35.00",
    }
    print(f"FND-2 final {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import assemble_final

    with tempfile.TemporaryDirectory(prefix="fnd2-final-selfcheck-") as temp_dir:
        base = Path(temp_dir)
        candidate = base / "candidate"
        assemble_final.assemble_reference_candidate(candidate)
        reference, starter = base / "reference", base / "starter"
        assemble_final.assemble(candidate, reference, reference=True)
        complete_report = validate(reference)
        assemble_final.assemble(candidate, starter, reference=False)
        starter_report = validate(starter, starter=True)
        try:
            validate(starter)
        except ValidationError as error:
            assert "Record is complete" in str(error), str(error)
        else:
            raise AssertionError("Validator accepted an incomplete starter")

        cases: list[tuple[Path, str]] = []
        broken = base / "broken-evidence"
        shutil.copytree(reference, broken)
        path = broken / "model-card.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8", newline="\n")
        cases.append((broken, "Candidate bytes match"))
        bad_score = base / "bad-score"
        shutil.copytree(reference, bad_score)
        path = bad_score / "final-review/final-score.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("5.00,5.00,pass", "5.00,6.00,pass", 1), encoding="utf-8", newline="\n")
        cases.append((bad_score, "Earned points are in range"))
        bad_gate = base / "bad-gate"
        shutil.copytree(reference, bad_gate)
        path = bad_gate / "final-review/gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8", newline="\n")
        cases.append((bad_gate, "All final gates pass"))
        bad_tag = base / "bad-tag"
        shutil.copytree(reference, bad_tag)
        path = bad_tag / "final-review/final-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("proposed - not created", "created early", 1), encoding="utf-8", newline="\n")
        cases.append((bad_tag, "Final tag remains uncreated"))
        bad_decision = base / "bad-decision"
        shutil.copytree(reference, bad_decision)
        path = bad_decision / "final-review/final-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Model-use recommendation: `teaching use only`", "Model-use recommendation: `stop model use`", 1), encoding="utf-8", newline="\n")
        cases.append((bad_decision, "Release acceptance agrees"))
        for package, expected in cases:
            try:
                validate(package)
            except ValidationError as error:
                assert expected in str(error), str(error)
            else:
                raise AssertionError(f"Validator accepted invalid package: {package.name}")
    print(f"FND-2 final validator self-check passed: {complete_report['checks_passed']} complete checks and {starter_report['checks_passed']} starter checks; incomplete and broken packages rejected.")


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
        if not args.package:
            parser.error("package is required unless --self-check is used")
        validate(args.package.resolve(), starter=args.starter)
    except (OSError, ValueError, KeyError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
