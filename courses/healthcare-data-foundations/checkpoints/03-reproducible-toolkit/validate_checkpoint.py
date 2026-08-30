"""Validate an FND-1 final reproducible-toolkit checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal, InvalidOperation
from pathlib import Path


SCRIPT_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = SCRIPT_ROOT.parent.parent
MODULE_VALIDATOR = COURSE_ROOT / "modules" / "07-reproducible-handoff-ai-audit" / "validate_toolkit.py"
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]
SCORE_FIELDS = ["criterion_id", "criterion", "points_available", "points_earned", "evidence", "status"]
GATE_FIELDS = ["gate_id", "gate", "result", "evidence", "reviewer", "condition_id"]
REVIEW_RECORDS = (
    "submission-record.md",
    "final-score.csv",
    "gate-results.csv",
    "defense-score.csv",
    "reviewer-record.md",
    "final-disposition.md",
    "handoff-acceptance.md",
    "final-reproduction.md",
)
FINAL_REVIEW_FILES = {
    "final-review/CHECKPOINT-VERSION",
    "final-review/candidate-manifest.csv",
    *(f"final-review/{name}" for name in REVIEW_RECORDS),
}
SCORE_MAP = (
    ("R01", "Repository identity, semantic version, change log, release notes, and tag evidence", "4.00"),
    ("R02", "Complete package, ownership map, immutable manifest, and fingerprint integrity", "5.00"),
    ("R03", "Environment, clean reproduction, output comparison, and hidden-dependency removal", "6.00"),
    ("D01", "Data brief, source, rights, grain, cohort, and denominator clarity", "4.00"),
    ("D02", "Quality conditions, descriptive limits, permitted use, and stop rules", "3.00"),
    ("A01", "Accessible schema and figure routes, exact tables, alternatives, and handoff communication", "3.00"),
    ("AI01", "Complete AI-use inventory, prompt log, material audit, verification, and human ownership", "4.00"),
    ("H01", "Release checklist, eight-minute handoff, defense, conditions, and disposition", "6.00"),
)
DEFENSE_MAP = (
    ("H01-A", "Source, rights, grain, and cohort explanation", "1.00"),
    ("H01-B", "Quality, denominator, and interpretation explanation", "1.00"),
    ("H01-C", "Reproduction, version, and manifest explanation", "1.00"),
    ("H01-D", "Accessibility and AI-accountability explanation", "1.00"),
    ("H01-E", "Response accuracy, limits, conditions, and final recommendation", "2.00"),
)
GATES = (
    "Exact accepted Module 07 version and candidate",
    "Exact 90-row candidate manifest",
    "Exact 100-file final tree",
    "Repository, commit, semantic version, and tag identity",
    "Exact source archive and rights",
    "Exact analytic grain and fingerprint",
    "Deterministic cohort and conserved counts",
    "D01 through D20 resolution preserved",
    "N01 through N08 conditions preserved",
    "Exact descriptive denominators and interval meaning",
    "Exact F01 through F03 evidence and equivalent access",
    "Complete pipeline source and declared environment",
    "Clean reproduction and exact output comparison",
    "No hidden dependency or manual output edit",
    "No prohibited data, archive, database, secret, or credential",
    "Complete data brief, limitations, change log, release notes, and checklist",
    "Complete material AI disclosure and independent audit",
    "Adequate accessible technical defense",
    "Complete reviewer, condition, and final-disposition records",
    "No unsupported real-world or causal claim",
)
REVIEWER_ROLES = (
    "FND-1 faculty owner",
    "Health-system analytics engineering lead",
    "SQL and data engineering",
    "Clinical informatics",
    "Accessibility",
    "Privacy and data governance",
    "Responsible AI",
    "Independent reproducer",
)
PLACEHOLDER = re.compile(r"\[REPLACE:[^\]\r\n]*\]|\b(?:TODO|TBD|REPLACE(?:_ME)?)\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
COMMIT = re.compile(r"(?i)\b[0-9a-f]{40}\b")
PIPELINE_SHA256 = "d61f208046663b80f8a591be66cc4f22fecbf0c5be7803786f75fd74cdd1d783"
MODULE_MANIFEST_SHA256 = "804d454dcdf43d0f625c90130b9bd5c698b51451ddcc1fd0910ca52e1bbd9111"
ANALYTIC_SHA256 = "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"
SOURCE_SHA256 = "4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a"
CALENDAR_URL = "https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf"


class ValidationError(RuntimeError):
    pass


def require(condition: bool, label: str, checks: list[str]) -> None:
    if not condition:
        raise ValidationError(label)
    checks.append(label)


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
        raise ValidationError(f"Candidate path is not portable: {value}")
    return path


def decimal(value: str, label: str) -> Decimal:
    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise ValidationError(f"{label} is not a decimal: {value}") from exc


def module_validation(root: Path, rows: list[dict[str, str]], checks: list[str]) -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-final-candidate-") as temp_dir:
        candidate = Path(temp_dir) / "candidate"
        candidate.mkdir()
        for row in rows:
            relative = safe_relative(row["relative_path"])
            destination = candidate / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / relative, destination)
        result = subprocess.run(
            [sys.executable, str(MODULE_VALIDATOR), str(candidate)],
            capture_output=True,
            text=True,
            check=False,
        )
    require(result.returncode == 0, f"Module 07 complete validation passes: {result.stderr.strip() or result.stdout.strip()}", checks)


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    checks: list[str] = []
    require(root.is_dir(), "Final checkpoint directory exists", checks)
    version = root / "final-review/CHECKPOINT-VERSION"
    require(version.read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version is 0.1.0", checks)

    manifest_path = root / "final-review/candidate-manifest.csv"
    fields, manifest = read_csv(manifest_path)
    require(fields == MANIFEST_FIELDS, "Candidate manifest header matches", checks)
    require(len(manifest) == 90, "Candidate manifest has 90 rows", checks)
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths), "Candidate manifest paths are sorted", checks)
    require(len(set(paths)) == 90, "Candidate manifest paths are unique", checks)
    require(not any(path.startswith("final-review/") for path in paths), "Candidate manifest excludes final-review records", checks)
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    expected = set(paths) | FINAL_REVIEW_FILES
    require(actual == expected and len(actual) == 100, "Final package has the exact 100-file tree", checks)
    require(not any(path.is_symlink() for path in root.rglob("*")), "Final package contains no symbolic link", checks)

    for row in manifest:
        relative = row["relative_path"]
        path = safe_relative(relative)
        file_path = root / path
        require(file_path.is_file(), f"Candidate file exists: {relative}", checks)
        require(file_path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {relative}", checks)
        require(sha256(file_path) == row["sha256"], f"Candidate SHA-256 matches: {relative}", checks)
        require(bool(row["role"].strip()), f"Candidate role is present: {relative}", checks)

    require(sha256(root / "pipeline-contract.csv") == PIPELINE_SHA256, "Pipeline contract fingerprint matches", checks)
    require(sha256(root / "release-manifest.csv") == MODULE_MANIFEST_SHA256, "Module 07 manifest fingerprint matches", checks)
    require(sha256(root / "data/analytic-table.csv") == ANALYTIC_SHA256, "Analytic-table fingerprint matches", checks)
    module_validation(root, manifest, checks)

    blocked_suffixes = {".sqlite", ".db", ".zip", ".pyc", ".pem", ".key"}
    require(not any(path.suffix.lower() in blocked_suffixes for path in root.rglob("*") if path.is_file()), "No prohibited archive, database, cache, key, or certificate file", checks)
    require(not any(part in {".venv", "__pycache__", "source-cache"} for path in root.rglob("*") for part in path.parts), "No environment, cache, or source-cache directory", checks)

    review_paths = [root / "final-review" / name for name in REVIEW_RECORDS]
    for path in review_paths:
        text = path.read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII punctuation: {path.name}", checks)
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {path.name}", checks)
        if not starter:
            require(not PLACEHOLDER.search(text), f"Final-review record is complete: {path.name}", checks)

    score_fields, scores = read_csv(root / "final-review/final-score.csv")
    require(score_fields == SCORE_FIELDS and len(scores) == 8, "Final score has the exact eight-row schema", checks)
    require(
        [(row["criterion_id"], row["criterion"], row["points_available"]) for row in scores] == list(SCORE_MAP),
        "Final score preserves criterion IDs, names, and weights",
        checks,
    )
    require(sum(decimal(row["points_available"], "Available score") for row in scores) == Decimal("35.00"), "Available course points total 35.00", checks)

    gate_fields, gates = read_csv(root / "final-review/gate-results.csv")
    require(gate_fields == GATE_FIELDS and len(gates) == 20, "Gate record has the exact 20-row schema", checks)
    require([row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 21)], "Gate IDs are G01 through G20", checks)
    require([row["gate"] for row in gates] == list(GATES), "Gate names preserve the final contract", checks)

    defense_fields, defense = read_csv(root / "final-review/defense-score.csv")
    require(defense_fields == SCORE_FIELDS and len(defense) == 5, "Defense score has the exact five-row schema", checks)
    require(
        [(row["criterion_id"], row["criterion"], row["points_available"]) for row in defense] == list(DEFENSE_MAP),
        "Defense preserves criterion IDs, names, and H01 weights",
        checks,
    )
    require(sum(decimal(row["points_available"], "Available defense score") for row in defense) == Decimal("6.00"), "Available defense points total 6.00", checks)

    manifest_hash = sha256(manifest_path)
    manifest_bytes = manifest_path.stat().st_size
    if not starter:
        allowed_score_status = {"pass", "pass with conditions"}
        earned = [decimal(row["points_earned"], "Earned score") for row in scores]
        available = [decimal(row["points_available"], "Available score") for row in scores]
        require(all(Decimal("0") <= value <= limit for value, limit in zip(earned, available, strict=True)), "Earned criterion scores are in range", checks)
        final_total = sum(earned)
        require(final_total >= Decimal("28.00"), "Final score is at least 28.00 of 35.00", checks)
        require(all(row["status"] in allowed_score_status and row["evidence"].strip() for row in scores), "All final score rows pass with evidence", checks)

        allowed_gate_status = {"pass", "pass with condition"}
        require(all(row["result"] in allowed_gate_status and row["evidence"].strip() and row["reviewer"].strip() for row in gates), "All gates pass with evidence and reviewer", checks)
        conditional_ids = {row["condition_id"] for row in gates if row["result"] == "pass with condition"}
        pass_count = sum(row["result"] == "pass" for row in gates)
        conditional_count = sum(row["result"] == "pass with condition" for row in gates)
        require(all(value and value.lower() != "none" for value in conditional_ids), "Conditional gates name condition IDs", checks)
        require(all(row["condition_id"].lower() == "none" for row in gates if row["result"] == "pass"), "Unconditional gates use condition ID none", checks)

        defense_earned = [decimal(row["points_earned"], "Earned defense score") for row in defense]
        defense_available = [decimal(row["points_available"], "Available defense score") for row in defense]
        require(all(Decimal("0") <= value <= limit for value, limit in zip(defense_earned, defense_available, strict=True)), "Earned defense scores are in range", checks)
        defense_total = sum(defense_earned)
        require(defense_total >= Decimal("4.80"), "Defense score is at least 4.80 of 6.00", checks)
        h01 = next(value for row, value in zip(scores, earned, strict=True) if row["criterion_id"] == "H01")
        require(defense_total == h01, "Defense total equals the H01 final score", checks)
        require(all(row["status"] in allowed_score_status and row["evidence"].strip() for row in defense), "All defense rows pass with evidence", checks)

        submission = (root / "final-review/submission-record.md").read_text(encoding="utf-8")
        submission_lower = submission.lower()
        for phrase in (
            "https://github.com/shuhancs/open-clinical-learning-commons",
            "oclc-fnd1-07",
            "module 07 candidate version: 0.1.0",
            "final checkpoint version: 0.1.0",
            "fnd1-toolkit-v0.1.0",
            CALENDAR_URL,
            "published half-term last day controls",
            "7.5 weeks is the planning model",
            "candidate manifest rows: 90",
            f"candidate manifest bytes: {manifest_bytes}",
            manifest_hash,
            "module 07 complete validation: pass",
            "final checkpoint complete validation: pass",
        ):
            require(phrase.lower() in submission_lower, f"Submission record includes: {phrase}", checks)
        require(bool(COMMIT.search(submission)), "Submission record has a full 40-character commit", checks)
        require("candidate status: accepted" in submission_lower, "Submission record has an accepted candidate status", checks)

        reviewer = (root / "final-review/reviewer-record.md").read_text(encoding="utf-8")
        reviewer_lower = reviewer.lower()
        for role in REVIEWER_ROLES:
            require(role.lower() in reviewer_lower, f"Reviewer record includes role: {role}", checks)
        require("learner is not the final decision owner or independent reproducer" in reviewer_lower, "Reviewer independence rule is explicit", checks)
        for phrase in ("condition id", "owner", "due point", "evidence required", "verifier", "closure status", "escalation trigger"):
            require(phrase in reviewer_lower, f"Reviewer condition record includes: {phrase}", checks)

        disposition = (root / "final-review/final-disposition.md").read_text(encoding="utf-8")
        disposition_lower = disposition.lower()
        disposition_match = re.search(r"(?mi)^disposition:\s*(accept with conditions|accept|revise|refer)\s*$", disposition)
        require(bool(disposition_match) and disposition_match.group(1).lower() in {"accept", "accept with conditions"}, "Final disposition permits FND-2 handoff", checks)
        require(bool(re.search(r"(?mi)^tag authorization:\s*authorized(?: with conditions)?\s*$", disposition)), "Annotated final tag is authorized", checks)
        require(bool(re.search(r"(?mi)^fnd-2 progression:\s*allowed(?: with conditions)?\s*$", disposition)), "FND-2 progression is explicit", checks)
        require("defense result: adequate" in disposition_lower, "Final disposition records an adequate defense", checks)
        require(
            f"gate result: {pass_count} pass and {conditional_count} pass with condition; none failed" in disposition_lower,
            "Disposition gate summary matches the gate record",
            checks,
        )
        require(f"total score: {final_total:.2f} of 35.00" in disposition_lower, "Disposition total matches final score", checks)
        require(f"defense score: {defense_total:.2f} of 6.00" in disposition_lower, "Disposition defense total matches defense score", checks)
        for condition_id in conditional_ids:
            require(condition_id.lower() in reviewer_lower and condition_id.lower() in disposition_lower, f"Conditional gate is owned in reviewer and disposition records: {condition_id}", checks)

        handoff = (root / "final-review/handoff-acceptance.md").read_text(encoding="utf-8").lower()
        for phrase in (
            "fnd-2",
            "fnd1-toolkit-v0.1.0",
            "permitted use",
            "public technical education",
            "downstream method development",
            "prohibited claims and uses",
            "production deployment",
            "real-patient use",
            "causal claims",
            "support owner",
            "change notification",
            "stop or referral triggers",
        ):
            require(phrase in handoff, f"Handoff acceptance includes: {phrase}", checks)

        reproduction = (root / "final-review/final-reproduction.md").read_text(encoding="utf-8")
        reproduction_lower = reproduction.lower()
        for phrase in (
            "operating system:",
            "python:",
            "sqlite:",
            "packages:",
            "source archive bytes: 8,982,431",
            SOURCE_SHA256,
            "candidate manifest rows: 90",
            manifest_hash,
            "ordered commands:",
            "exact output comparison: pass",
            "module 07 complete validation: pass",
            "final checkpoint complete validation: pass",
            "hidden dependency or manual output edit: none",
            "independent reproducer:",
            "independence:",
        ):
            require(phrase in reproduction_lower, f"Final reproduction includes: {phrase}", checks)
        require(bool(COMMIT.search(reproduction)), "Final reproduction has a full clean-checkout commit", checks)

        ai_audit = (root / "documentation/ai-audit.md").read_text(encoding="utf-8").lower()
        require("independent method and evidence" in ai_audit and "263" in ai_audit and "human owner" in ai_audit and "not source" in ai_audit, "Material AI audit remains independently evidenced and human-owned", checks)
        access = (root / "documentation/checkpoint2/accessibility-synthesis.md").read_text(encoding="utf-8").lower()
        require(all(phrase in access for phrase in ("f01", "f02", "f03", "png", "svg", "csv")), "Accessibility synthesis retains F01-F03 equivalent routes", checks)

    for relative in ("final-review/candidate-manifest.csv", "final-review/final-score.csv", "final-review/gate-results.csv", "final-review/defense-score.csv"):
        require(b"\r\n" not in (root / relative).read_bytes(), f"Final contract uses LF: {relative}", checks)

    report = {
        "status": "pass",
        "mode": "starter" if starter else "complete",
        "checks_passed": len(checks),
        "candidate_files": len(manifest),
        "final_files": len(actual),
        "manifest_bytes": manifest_bytes,
        "manifest_sha256": manifest_hash,
        "course_points": 35,
    }
    print(f"FND-1 final checkpoint {report['mode']} validation passed: {len(checks)} checks.")
    return report


def load_assembler():
    path = SCRIPT_ROOT / "assemble_checkpoint.py"
    if not path.is_file():
        raise ValidationError("Self-check requires assemble_checkpoint.py beside the validator.")
    spec = importlib.util.spec_from_file_location("fnd1_final_assembler", path)
    if spec is None or spec.loader is None:
        raise ValidationError("Could not load the final-checkpoint assembler.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def self_check() -> None:
    assembler = load_assembler()
    with tempfile.TemporaryDirectory(prefix="fnd1-final-validate-") as temp_dir:
        temp = Path(temp_dir)
        toolkit = temp / "toolkit"
        reference = temp / "reference"
        learner = temp / "learner"
        assembler.assemble_reference_toolkit(toolkit)
        assembler.assemble(toolkit, reference, reference=True)
        assembler.assemble(toolkit, learner)
        validate(reference)
        validate(learner, starter=True)
        try:
            validate(learner)
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted unfinished final-review records.")
        (reference / "data/analytic-table.csv").unlink()
        try:
            validate(reference)
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted a missing candidate file.")
    print("FND-1 final-checkpoint validator self-check passed.")


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
        validate(args.checkpoint.resolve(), starter=args.starter)
    except (OSError, ValueError, KeyError, ValidationError) as exc:
        parser.exit(1, f"Validation failed: {exc}\n")


if __name__ == "__main__":
    main()
