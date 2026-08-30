"""Validate APP-2 final patient-experience and engagement packages."""

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
from pathlib import Path


CHECKPOINT_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = CHECKPOINT_ROOT.parent.parent
MODULE_ROOT = COURSE_ROOT / "modules/07-clinician-patient-leadership-defense"
MODULE_ASSEMBLER = MODULE_ROOT / "assemble_candidate.py"
MODULE_VALIDATOR = MODULE_ROOT / "validate_candidate.py"
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
MODULE_MANIFEST_BYTES = 64149
MODULE_MANIFEST_SHA256 = "53bd306692145df85d1b2a709615000f80829099a916659c6a8cfd3bd994697f"
MODULE_RELEASE_SHA256 = "2a30f59869be0041b813ce6005c226a9bcd3cd28632222464a5defc1586ca317"
CP1_RELEASE_SHA256 = "44f189a6225a1ed72fee70fa7366cc6dfd2ab5952c1ddcd8304fff5ea89a0137"
CP2_RELEASE_SHA256 = "7684d17f2441883cdcd87521e5376b133bf7d85dc0513f655770c18f19edb60c"
SCORE_MAXIMUMS = {"M01": 7.0, "P01": 8.0, "L01": 8.0, "A01": 7.0, "H01": 5.0}
ALLOWED_DISPOSITIONS = {"accept", "accept with conditions", "revise", "refer"}
ALLOWED_RECOMMENDATIONS = {
    "run bounded prospective measurement and improvement test", "revise before testing", "refer", "stop",
}


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


def validate(root: Path, starter: bool = False) -> dict[str, object]:
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
    require(len(final_manifest) == 358, "Final candidate manifest has 358 rows")
    candidate_paths = [row["relative_path"] for row in final_manifest]
    require(candidate_paths == sorted(candidate_paths) and len(set(candidate_paths)) == 358, "Final candidate paths are sorted and unique")
    for row in final_manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Portable candidate path: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        require(bool(row["role"]), f"Candidate role is present: {row['relative_path']}")
    actual = {
        path.relative_to(root).as_posix() for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == set(candidate_paths) | FINAL_FILES and len(actual) == 373, "Final package has exactly 373 expected files")

    module_header, module_manifest = read_csv(root / "release-manifest.csv")
    require(module_header == MODULE_MANIFEST_FIELDS and len(module_manifest) == 334, "Module 07 immutable manifest has 334 rows")
    require((root / "release-manifest.csv").stat().st_size == MODULE_MANIFEST_BYTES and sha256(root / "release-manifest.csv") == MODULE_MANIFEST_SHA256, "Module 07 manifest fingerprint matches")
    require(sha256(root / "final-review/checkpoint1-release.json") == CP1_RELEASE_SHA256, "Checkpoint 01 release identity matches")
    require(sha256(root / "final-review/checkpoint2-release.json") == CP2_RELEASE_SHA256, "Checkpoint 02 release identity matches")
    require(sha256(root / "final-review/module07-release.json") == MODULE_RELEASE_SHA256, "Module 07 release identity matches")
    require(sha256(root / "evidence/provenance/checkpoint1-release.json") == CP1_RELEASE_SHA256, "Nested Checkpoint 01 release identity matches")
    require(sha256(root / "evidence/provenance/checkpoint2-release.json") == CP2_RELEASE_SHA256, "Nested Checkpoint 02 release identity matches")

    with tempfile.TemporaryDirectory(prefix="app2-final-candidate-validate-") as temp_dir:
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
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "candidate_files": 358, "assembled_files": 373}
        print(f"APP-2 final starter validation passed: {len(checks)} checks.")
        return report

    submission = (review_root / "submission-record.md").read_text(encoding="utf-8")
    manifest = review_root / "candidate-manifest.csv"
    require(markdown_field(submission, "Final candidate manifest bytes") == str(manifest.stat().st_size), "Submission final-manifest bytes match")
    require(markdown_field(submission, "Final candidate manifest SHA-256") == sha256(manifest), "Submission final-manifest SHA-256 matches")
    submission_values = (
        "https://github.com/ShuhanCS/open-clinical-learning-commons", "`358`", "`334`", "`64149`",
        MODULE_MANIFEST_SHA256, CP1_RELEASE_SHA256, CP2_RELEASE_SHA256, MODULE_RELEASE_SHA256,
        "official last day of the assigned MGH Institute half-term",
        "app2-patient-experience-engagement-candidate-v0.1.0", "proposed - not created",
        "https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf",
    )
    require(all(value in submission for value in submission_values), "Submission identities calendar and tag status match")

    scores = tables["final-score.csv"]
    require([row["criterion_id"] for row in scores] == list(SCORE_MAXIMUMS), "Final score criteria are in fixed order")
    require(all(float(row["maximum"]) == SCORE_MAXIMUMS[row["criterion_id"]] for row in scores), "Final score maximums match")
    total = sum(float(row["score"]) for row in scores)
    require(all(0 <= float(row["score"]) <= float(row["maximum"]) for row in scores) and total >= 28.0, "Final scores are bounded and meet the minimum")
    require(abs(total - 35.0) < 1e-9 and all(row["status"] == "pass" for row in scores), "Reference final score is 35.00 of 35.00")
    for row in scores:
        for evidence in row["evidence"].split(" and "):
            require((root / Path(evidence)).is_file(), f"Final score evidence exists: {row['criterion_id']}")

    conditions = tables["conditions-register.csv"]
    condition_ids = {row["condition_id"] for row in conditions}
    require(len(conditions) == 8 and condition_ids == {f"COND-{i:02d}" for i in range(1, 9)}, "Eight final conditions are registered")
    require(all(row["owner"] and row["due_point"] and row["evidence"] and row["verifier"] and row["status"] == "open" and row["escalation_trigger"] for row in conditions), "Every final condition has complete open ownership")
    for row in conditions:
        for evidence in row["evidence"].split(" and "):
            require((root / Path(evidence)).is_file(), f"Condition evidence exists: {row['condition_id']}")

    gates = tables["gate-results.csv"]
    require(len(gates) == 26 and [row["gate_id"] for row in gates] == [f"G{i:02d}" for i in range(1, 27)], "Twenty-six final gates are ordered")
    require(all(row["result"] in {"pass", "pass with condition"} for row in gates), "Every final gate passes or passes with an allowed condition")
    require(all((not row["condition_id"] and row["result"] == "pass") or (row["condition_id"] in condition_ids and row["result"] == "pass with condition") for row in gates), "Final gate conditions are consistent and registered")
    require(all((root / Path(row["evidence"])).is_file() for row in gates), "Every final gate cites existing evidence")

    defense = (review_root / "final-defense.md").read_text(encoding="utf-8")
    require(markdown_field(defense, "Defense status") == "adequate for curriculum construction", "Final defense status is adequate")
    require(len(re.findall(r"(?m)^## Q(?:0[1-9]|1[0-4])\.", defense)) == 14, "All 14 final defense answers are present")
    require(all(len(section.strip()) >= 90 for section in re.split(r"(?m)^## Q(?:0[1-9]|1[0-4])\..*$", defense)[1:]), "Every final defense answer is substantive")

    reviewer = (review_root / "reviewer-record.md").read_text(encoding="utf-8")
    reviewer_roles = (
        "APP-2 faculty owner", "Joe Joseph, MD, SFHM, clinician of record", "Local clinical decision owner",
        "Patient or caregiver co-lead", "Patient-experience measurement reviewer", "Survey-methods reviewer",
        "Health-services data reviewer", "Qualitative-methods reviewer", "Equity reviewer",
        "Access and language reviewer", "Privacy and data-governance reviewer",
        "Responsible-AI and model reviewer", "Improvement and operations reviewer", "Independent reproducer",
    )
    require(all(role in reviewer for role in reviewer_roles), "All 14 final reviewer roles are present")

    reproduction = (review_root / "final-reproduction.md").read_text(encoding="utf-8")
    require(markdown_field(reproduction, "Final candidate manifest bytes") == str(manifest.stat().st_size), "Reproduction final-manifest bytes match")
    require(markdown_field(reproduction, "Final candidate manifest SHA-256") == sha256(manifest), "Reproduction final-manifest SHA-256 matches")
    require(all(value in reproduction for value in ("`358`", "`373`", "`334`", "Module 07 validator: `pass`", "Two-build match: `pass`")), "Final reproduction package results match")

    audit = (review_root / "final-audit.md").read_text(encoding="utf-8")
    audit_values = ("358 rows", "334 rows", "18 of 18", "statements in reference: `0`", "none found", "separate and consistent", "prohibited", "pass with conditions for curriculum construction")
    require(all(value in audit for value in audit_values), "Final audit covers identity integrity partnership access accountability and decisions")

    decision = (review_root / "final-decision.md").read_text(encoding="utf-8")
    disposition = markdown_field(decision, "Package disposition")
    recommendation = markdown_field(decision, "Organizational recommendation")
    require(disposition in ALLOWED_DISPOSITIONS and recommendation in ALLOWED_RECOMMENDATIONS, "Final package and organizational decisions are allowed")
    expected_decision = {
        "Final score": "35.00 of 35.00",
        "Gates": "26 of 26 pass or pass with an allowed condition",
        "Defense": "adequate for curriculum construction",
        "Package disposition": "accept with conditions",
        "Organizational recommendation": "revise before testing",
        "Actual patient or caregiver statements in reference": "0",
        "Patient/caregiver co-lead": "pending before alpha",
        "Patient contact and fielding": "prohibited",
        "Official HCAHPS reporting": "prohibited",
        "Patient or group targeting": "prohibited",
        "Clinical implementation": "prohibited",
        "Model deployment": "prohibited",
        "Course status": "complete for curriculum construction only",
        "Proposed tag": "app2-patient-experience-engagement-candidate-v0.1.0",
        "Tag status": "proposed - not created",
        "Tag authorization": "pending named human approval, direct patient review, and exact-commit verification",
    }
    require(all(markdown_field(decision, key) == value for key, value in expected_decision.items()), "Reference final decisions and authorization boundary match")

    module_progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(module_progression, "Organizational recommendation") == recommendation, "Final recommendation matches Module 07")
    require(markdown_field(module_progression, "Candidate status") == disposition, "Final package disposition matches Module 07 candidate status")

    acceptance = (review_root / "release-acceptance.md").read_text(encoding="utf-8")
    acceptance_values = (
        "Curriculum construction", "Patient contact", "official HCAHPS reporting", "model deployment",
        "Any changed candidate byte requires a new Module 07 version", "proposed and not created",
    )
    require(all(value in acceptance for value in acceptance_values), "Release acceptance states allowed use change rule prohibitions and tag status")

    report = {
        "status": "pass", "mode": "complete", "checks_passed": len(checks),
        "candidate_files": 358, "assembled_files": 373, "manifest_rows": 358,
        "score": total, "gates_passed": 26, "package_disposition": disposition,
        "organizational_recommendation": recommendation,
    }
    print(f"APP-2 final complete validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path) -> None:
    try:
        validate(root)
    except (ValidationError, OSError, ValueError, json.JSONDecodeError):
        return
    raise AssertionError(f"Expected final validation failure for {root}")


def command(args: list[str]) -> None:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode:
        raise AssertionError(result.stderr.strip() or result.stdout.strip())


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-final-validate-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        command([sys.executable, str(ASSEMBLER), "--target", str(reference), "--reference"])
        report = validate(reference)
        assert report["candidate_files"] == 358 and report["assembled_files"] == 373

        candidate = base / "candidate"
        command([sys.executable, str(MODULE_ASSEMBLER), "--target", str(candidate), "--reference"])
        starter = base / "starter"
        command([sys.executable, str(ASSEMBLER), "--candidate", str(candidate), "--target", str(starter)])
        validate(starter, starter=True)

        changed = base / "changed-candidate"
        shutil.copytree(reference, changed)
        evidence = changed / "leadership-recommendation.md"
        evidence.write_text(evidence.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        expect_failure(changed)

        changed = base / "changed-score"
        shutil.copytree(reference, changed)
        score = changed / "final-review/final-score.csv"
        score.write_text(score.read_text(encoding="utf-8").replace("7.00,7.00", "7.00,1.00", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "failed-gate"
        shutil.copytree(reference, changed)
        gates = changed / "final-review/gate-results.csv"
        gates.write_text(gates.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "early-tag"
        shutil.copytree(reference, changed)
        decision = changed / "final-review/final-decision.md"
        decision.write_text(decision.read_text(encoding="utf-8").replace("proposed - not created", "created", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "false-partnership"
        shutil.copytree(reference, changed)
        decision = changed / "final-review/final-decision.md"
        decision.write_text(decision.read_text(encoding="utf-8").replace("statements in reference: `0`", "statements in reference: `1`"), encoding="utf-8")
        expect_failure(changed)

        changed = base / "bad-decision"
        shutil.copytree(reference, changed)
        decision = changed / "final-review/final-decision.md"
        decision.write_text(decision.read_text(encoding="utf-8").replace("Clinical implementation: `prohibited`", "Clinical implementation: `authorized`"), encoding="utf-8")
        expect_failure(changed)
    print("APP-2 final validator self-check passed: complete, starter, candidate, score, gate, tag, partnership, and decision routes.")


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
    except (ValidationError, OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
