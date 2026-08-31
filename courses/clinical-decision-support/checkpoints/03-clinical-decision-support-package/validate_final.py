"""Validate APP-4 final Clinical Decision Support packages."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
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
MODULE_ROOT = COURSE_ROOT / "modules/07-clinician-leadership-product-defense"
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
MODULE_MANIFEST_BYTES = 319268
MODULE_MANIFEST_SHA256 = "8fc03ea9a7ebce8e0e4bf350b2699c5f74ec4a9c5ae493f25f26c94be8c2cea9"
MODULE_RELEASE_SHA256 = "8e2eada4dadc30d92976963bc8bd01639ea851b88e115464801ee9900ed6e7cd"
CP1_RELEASE_SHA256 = "8f637bef551ebe5cb91e93b3b91fef51f25736d07168b904851405c703b62c03"
CP2_RELEASE_SHA256 = "05e65b59f0d4c4b33dc341256141e39c02cfffc32e22aca546dbb85384cb1221"
SCORE_MAXIMUMS = {
    "E01": Decimal("8.00"), "C01": Decimal("9.00"), "L01": Decimal("8.00"),
    "G01": Decimal("6.00"), "H01": Decimal("4.00"),
}
ALLOWED_DISPOSITIONS = {"accept", "accept with conditions", "revise", "refer"}
ALLOWED_RECOMMENDATIONS = {
    "recommend seeking local approval for bounded silent-mode evaluation",
    "revise before seeking local silent-mode approval", "refer", "stop",
}
REVIEWER_ROLES = (
    "APP-4 faculty owner", "Joe Joseph, MD, SFHM, clinician of record",
    "Local clinical decision owner", "Patient-safety reviewer",
    "Workflow and human-factors reviewer", "Patient or caregiver reviewer",
    "Equity language and disability-access reviewer",
    "Clinical informatics and interoperability reviewer",
    "Survey-methods and calibration reviewer", "Model-risk and biostatistics reviewer",
    "Accessibility reviewer", "Privacy data-governance and security reviewers",
    "Responsible-AI reviewer", "Independent reproducer",
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


def markdown_field(value: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\.?\s*$", value)
    return match.group(1).strip() if match else None


def run_validator(script: Path, target: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(script), "--candidate", str(target), "--complete"],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise ValidationError(result.stderr.strip() or result.stdout.strip())


def link_or_copy(source: Path, destination: Path) -> None:
    try:
        os.link(source, destination)
    except OSError:
        shutil.copy2(source, destination)


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
    require(len(final_manifest) == 1347, "Final candidate manifest has 1,347 rows")
    candidate_paths = [row["relative_path"] for row in final_manifest]
    require(candidate_paths == sorted(candidate_paths) and len(set(candidate_paths)) == 1347, "Final candidate paths are sorted and unique")
    for row in final_manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts and "\\" not in row["relative_path"], f"Portable candidate path: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        require(bool(row["role"]), f"Candidate role is present: {row['relative_path']}")
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == set(candidate_paths) | FINAL_FILES and len(actual) == 1362, "Final package has exactly 1,362 expected files")

    module_header, module_manifest = read_csv(root / "release-manifest.csv")
    require(module_header == MODULE_MANIFEST_FIELDS and len(module_manifest) == 1320, "Module 07 immutable manifest has 1,320 rows")
    require(
        (root / "release-manifest.csv").stat().st_size == MODULE_MANIFEST_BYTES
        and sha256(root / "release-manifest.csv") == MODULE_MANIFEST_SHA256,
        "Module 07 manifest fingerprint matches",
    )
    require(sha256(root / "final-review/checkpoint1-release.json") == CP1_RELEASE_SHA256, "Checkpoint 01 release identity matches")
    require(sha256(root / "final-review/checkpoint2-release.json") == CP2_RELEASE_SHA256, "Checkpoint 02 release identity matches")
    require(sha256(root / "final-review/module07-release.json") == MODULE_RELEASE_SHA256, "Module 07 release identity matches")
    require(sha256(root / "evidence/provenance/checkpoint1-release.json") == CP1_RELEASE_SHA256, "Nested Checkpoint 01 release identity matches")
    require(sha256(root / "evidence/provenance/checkpoint2-release.json") == CP2_RELEASE_SHA256, "Nested Checkpoint 02 release identity matches")

    if nested:
        with tempfile.TemporaryDirectory(prefix="app4-final-candidate-validate-") as temp_dir:
            candidate = Path(temp_dir) / "candidate"
            candidate.mkdir()
            for relative_text in candidate_paths:
                relative = Path(relative_text)
                destination = candidate / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                link_or_copy(root / relative, destination)
            run_validator(candidate / "validate_candidate.py", candidate)
        checks.append("Reconstructed Module 07 candidate validates")

    review_root = root / "final-review"
    for name in REVIEW_RECORDS:
        value = (review_root / name).read_text(encoding="utf-8")
        require("\u2013" not in value and "\u2014" not in value, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(value), f"No personal absolute path: {name}")
        if starter:
            require(bool(PLACEHOLDER.search(value)), f"Starter prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(value), f"Final review record is complete: {name}")

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
        report = {
            "status": "pass", "mode": "starter", "checks_passed": len(checks),
            "candidate_files": 1347, "assembled_files": 1362,
        }
        print(f"APP-4 final starter validation passed: {len(checks)} checks.")
        return report

    submission = (review_root / "submission-record.md").read_text(encoding="utf-8")
    manifest = review_root / "candidate-manifest.csv"
    require(markdown_field(submission, "Final candidate manifest rows") == "1347", "Submission final-manifest rows match")
    require(markdown_field(submission, "Final candidate manifest bytes") == str(manifest.stat().st_size), "Submission final-manifest bytes match")
    require(markdown_field(submission, "Final candidate manifest SHA-256") == sha256(manifest), "Submission final-manifest SHA-256 matches")
    require(markdown_field(submission, "Module 07 release SHA-256") == MODULE_RELEASE_SHA256, "Submission Module 07 release identity matches")
    require(markdown_field(submission, "Tag status") == "proposed - not created", "Submission tag remains uncreated")

    score = tables["final-score.csv"]
    require([row["criterion_id"] for row in score] == list(SCORE_MAXIMUMS), "Final score criteria are exact and ordered")
    require(all(Decimal(row["maximum"]) == SCORE_MAXIMUMS[row["criterion_id"]] for row in score), "Final score maximums match")
    require(all(Decimal(row["score"]) == SCORE_MAXIMUMS[row["criterion_id"]] and row["status"] == "pass" for row in score), "Reference final criterion scores pass")
    total = sum((Decimal(row["score"]) for row in score), Decimal("0.00"))
    require(total == Decimal("35.00"), "Final score totals 35.00")

    gates = tables["gate-results.csv"]
    require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 27)], "Final gate IDs are exact and ordered")
    require(all(row["result"] in {"pass", "pass with condition"} and row["evidence"] and row["reviewer"] for row in gates), "All final gates pass with evidence and reviewer")
    require(all(not row["condition_id"] or re.fullmatch(r"C(?:0[1-9]|1[0-6])", row["condition_id"]) for row in gates), "Gate condition links are valid")

    conditions = tables["conditions-register.csv"]
    require([row["condition_id"] for row in conditions] == [f"C{index:02d}" for index in range(1, 17)], "Final conditions are exact and ordered")
    require(all(row["status"] == "open" and all(row[field] for field in ("condition", "owner", "due_point", "evidence", "verifier", "escalation_trigger")) for row in conditions), "All final conditions remain open owned and complete")

    defense = (review_root / "final-defense.md").read_text(encoding="utf-8")
    require(re.findall(r"^## Q\d{2}\.", defense, re.MULTILINE) == [f"## Q{index:02d}." for index in range(1, 15)], "Final defense has 14 ordered questions")
    require(defense.count("- Exact answer:") == 14 and defense.count("- Evidence:") == 14, "Final defense answers and evidence are complete")
    require(defense.count("- Decision consequence:") == 14 and defense.count("- Limit:") == 14, "Final defense consequences and limits are complete")
    require(all(value in defense for value in ("adequate for curriculum construction", "pending before alpha", "Agent output is not evidence", "revise before seeking local silent-mode approval")), "Final defense preserves status agent and recommendation boundaries")

    reviewer = (review_root / "reviewer-record.md").read_text(encoding="utf-8")
    require(all(role in reviewer for role in REVIEWER_ROLES), "All 14 reviewer roles are present")
    require(all(value in reviewer for value in ("Completed named human reviews claimed: `none`", "Current clinical authorization: `none`", "does not claim that Joe Joseph participated")), "Reviewer completion and clinician boundaries match")

    reproduction = (review_root / "final-reproduction.md").read_text(encoding="utf-8")
    require(markdown_field(reproduction, "Final candidate manifest bytes") == str(manifest.stat().st_size), "Reproduction final-manifest bytes match")
    require(markdown_field(reproduction, "Final candidate manifest SHA-256") == sha256(manifest), "Reproduction final-manifest SHA-256 matches")
    require(all(value in reproduction for value in ("`1347`", "`1362`", "`1320`", "Module 07 validator: `pass`", "Two-build match: `pass`", "pending before alpha")), "Final reproduction package results match")

    audit = (review_root / "final-audit.md").read_text(encoding="utf-8")
    audit_values = (
        "1,347 rows", "1,320 rows", "all 3 copied release records match", "none found",
        "six candidates remain unaccepted", "all 17 failures", "malformed-card defect remains blocked",
        "22 hazards 20 measures 12 human escalation routes and zero automatic actions",
        "failed R03 R04 R08", "40 plus 25 plus 35 equals 100", "separate and consistent",
        "prohibited", "accept with conditions for curriculum construction",
    )
    require(all(value in audit for value in audit_values), "Final audit covers identity evidence failures score decisions and authority")

    decision = (review_root / "final-decision.md").read_text(encoding="utf-8")
    disposition = markdown_field(decision, "Package disposition")
    recommendation = markdown_field(decision, "CDS recommendation")
    require(disposition in ALLOWED_DISPOSITIONS and recommendation in ALLOWED_RECOMMENDATIONS, "Final package and CDS decisions are allowed")
    expected_decision = {
        "Final score": "35.00 of 35.00", "Score destination": "Checkpoint 03 exactly once",
        "Course score": "40 + 25 + 35 = 100",
        "Gates": "26 of 26 pass or pass with an allowed condition",
        "Defense": "adequate for curriculum construction", "Package disposition": "accept with conditions",
        "CDS recommendation": "revise before seeking local silent-mode approval",
        "Accepted clinical threshold": "none", "Selected design": "panel-t003 mechanics fixture only",
        "ML decision": "retain transparent model", "Open conditions": "C01 through C16",
        "Real-patient scoring": "prohibited", "Clinical threshold acceptance": "prohibited",
        "Clinical alerting": "prohibited", "Clinical action": "prohibited",
        "Silent-mode evaluation": "prohibited", "Implementation": "prohibited",
        "Production connection": "prohibited", "Deployment": "prohibited",
        "Course status": "complete for curriculum construction only",
        "Proposed tag": "app4-clinical-decision-support-candidate-v0.1.0",
        "Tag status": "proposed - not created",
        "Tag authorization": "pending named human approval and exact-commit verification",
    }
    require(all(markdown_field(decision, key) == value for key, value in expected_decision.items()), "Reference final decisions score and authority boundary match")

    module_progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(module_progression, "CDS recommendation") == recommendation, "Final recommendation matches Module 07")
    require(markdown_field(module_progression, "Curriculum package status") == disposition, "Final package disposition matches Module 07")
    require(markdown_field(module_progression, "Accepted clinical threshold") == "none", "Final threshold status matches Module 07")
    require(markdown_field(module_progression, "ML decision") == "retain transparent model; R03, R04, and R08 fail", "Final model decision matches Module 07")

    acceptance = (review_root / "release-acceptance.md").read_text(encoding="utf-8")
    acceptance_values = (
        "curriculum construction", "Real-patient scoring", "clinical threshold acceptance",
        "clinical alerting or action", "silent-mode evaluation", "implementation",
        "production connection", "deployment", "Any changed candidate byte requires a new Module 07 version",
        "proposed and not created",
    )
    require(all(value in acceptance for value in acceptance_values), "Release acceptance states allowed use change rule prohibitions and tag status")

    report = {
        "status": "pass", "mode": "complete", "checks_passed": len(checks),
        "candidate_files": 1347, "assembled_files": 1362, "manifest_rows": 1347,
        "score": str(total), "gates_passed": 26, "conditions": 16,
        "package_disposition": disposition, "cds_recommendation": recommendation,
    }
    print(f"APP-4 final complete validation passed: {len(checks)} checks.")
    return report


def replace(path: Path, old: str, new: str) -> None:
    value = path.read_text(encoding="utf-8")
    if old not in value:
        raise AssertionError(f"Mutation source is absent in {path.name}: {old}")
    path.write_text(value.replace(old, new, 1), encoding="utf-8", newline="\n")


def append(path: Path) -> None:
    path.write_text(path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8", newline="\n")


def command(args: list[str]) -> None:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode:
        raise AssertionError(result.stderr.strip() or result.stdout.strip())


def self_check() -> None:
    import assemble_final

    with tempfile.TemporaryDirectory(prefix="app4-final-validate-") as temp_dir:
        base = Path(temp_dir)
        candidate = base / "candidate"
        command([sys.executable, str(MODULE_ASSEMBLER), "--target", str(candidate), "--reference"])
        reference = base / "reference"
        assemble_final.assemble(candidate, reference, reference=True, hardlink=True)
        shutil.rmtree(candidate)
        complete = validate(reference)

        candidate = base / "candidate"
        candidate.mkdir()
        _, candidate_rows = read_csv(reference / "final-review/candidate-manifest.csv")
        for row in candidate_rows:
            relative = Path(row["relative_path"])
            destination = candidate / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            link_or_copy(reference / relative, destination)
        starter = base / "starter"
        assemble_final.assemble(candidate, starter, hardlink=True)
        starter_report = validate(starter, starter=True, nested=False)
        try:
            validate(starter, nested=False)
        except ValidationError as error:
            assert "Final review record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted learner prompts as complete")
        shutil.rmtree(candidate)
        shutil.rmtree(starter)

        mutation = base / "mutation"
        shutil.copytree(reference, mutation, copy_function=link_or_copy)
        routes: list[tuple[str, str, Callable[[Path], None]]] = [
            ("changed-candidate", "evidence-synthesis.md", append),
            ("changed-release", "final-review/module07-release.json", append),
            ("invalid-score", "final-review/final-score.csv", lambda path: replace(path, "8.00,8.00", "8.00,1.00")),
            ("failed-gate", "final-review/gate-results.csv", lambda path: replace(path, ",pass,final-review/submission-record.md", ",fail,final-review/submission-record.md")),
            ("early-tag", "final-review/final-decision.md", lambda path: replace(path, "proposed - not created", "created")),
            ("changed-recommendation", "final-review/final-decision.md", lambda path: replace(path, "revise before seeking local silent-mode approval", "recommend seeking local approval for bounded silent-mode evaluation")),
            ("false-silent-authorization", "final-review/final-decision.md", lambda path: replace(path, "Silent-mode evaluation: `prohibited`", "Silent-mode evaluation: `authorized`")),
            ("accepted-threshold", "final-review/final-decision.md", lambda path: replace(path, "Accepted clinical threshold: `none`", "Accepted clinical threshold: `0.03000000`")),
            ("changed-model", "final-review/final-decision.md", lambda path: replace(path, "retain transparent model", "accept challenger")),
            ("waived-accessibility", "final-review/final-audit.md", lambda path: replace(path, "malformed-card defect remains blocked", "malformed-card defect is waived")),
            ("hidden-failure", "final-review/final-audit.md", lambda path: replace(path, "all 17 failures", "no failures")),
            ("missing-reviewer", "final-review/reviewer-record.md", lambda path: replace(path, "Independent reproducer", "Package observer")),
            ("closed-condition", "final-review/conditions-register.csv", lambda path: replace(path, ",open,", ",closed,")),
            ("incomplete-defense", "final-review/final-defense.md", lambda path: replace(path, "## Q14.", "## Closing question.")),
            ("hidden-agent-use", "final-review/final-defense.md", lambda path: replace(path, "Agent output is not evidence", "Agent output is evidence")),
            ("duplicate-final-score", "final-review/final-decision.md", lambda path: replace(path, "40 + 25 + 35 = 100", "40 + 25 + 35 + 35 = 135")),
            ("accepted-design", "final-review/final-decision.md", lambda path: replace(path, "panel-t003 mechanics fixture only", "panel-t003 accepted clinical design")),
            ("false-clinical-action", "final-review/final-decision.md", lambda path: replace(path, "Clinical action: `prohibited`", "Clinical action: `authorized`")),
            ("false-clinician-participation", "final-review/reviewer-record.md", lambda path: replace(path, "does not claim that Joe Joseph participated", "claims that Joe Joseph participated")),
            ("changed-course-status", "final-review/final-decision.md", lambda path: replace(path, "complete for curriculum construction only", "approved for clinical use")),
        ]
        for name, relative, mutate in routes:
            path = mutation / relative
            path.unlink()
            shutil.copy2(reference / relative, path)
            mutate(path)
            try:
                validate(mutation, nested=False)
            except (ValidationError, OSError, ValueError, KeyError, json.JSONDecodeError):
                pass
            else:
                raise AssertionError(f"Validator accepted {name} mutation")
            finally:
                path.unlink()
                link_or_copy(reference / relative, path)

    print(
        f"APP-4 final validator self-check passed: {complete['checks_passed']} complete checks and "
        f"{starter_report['checks_passed']} starter checks; 20 failure routes and complete-mode template rejection verified."
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
