"""Validate APP-2 Module 07 clinician and patient leadership candidates."""

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
from collections import Counter
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
CONTROL_FILES = (
    ".gitattributes", "VERSION", "leadership-contract.json", "clinician-profile.md",
    "patient-partner-role.md", "leadership-session-plan.md", "assessment.md",
    "assemble_candidate.py", "validate_candidate.py",
)
RECORD_FILES = (
    "README.md", "evidence-synthesis.md", "patient-facing-summary.md", "leadership-recommendation.md",
    "patient-partner-decision-record.md", "stakeholder-roles.csv", "workflow-feasibility.md",
    "bounded-test-plan.md", "measures-monitoring.csv", "feedback-accountability.md",
    "stop-escalation-rules.csv", "leadership-reflection.md", "technical-appendix.md",
    "evidence-index.csv", "accessibility-language-review.md", "reproducibility-check.md", "ai-use.md",
    "component-score.csv", "gate-results.csv", "conditions-register.csv", "leadership-defense.md",
    "reviewer-record.md", "progression-decision.md",
)
MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]
CHECKPOINTS = (
    {
        "directory": "checkpoint1", "id": "oclc-app2-cp01", "files": 149,
        "manifest_sha256": "5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903",
        "release_sha256": "44f189a6225a1ed72fee70fa7366cc6dfd2ab5952c1ddcd8304fff5ea89a0137",
    },
    {
        "directory": "checkpoint2", "id": "oclc-app2-cp02", "files": 174,
        "manifest_sha256": "67248e989888cdabeb050c970e85d091ece68018047ef6f0bec7ba26441cfed1",
        "release_sha256": "7684d17f2441883cdcd87521e5376b133bf7d85dc0513f655770c18f19edb60c",
    },
)
ALLOWED_RECOMMENDATIONS = {
    "run bounded prospective measurement and improvement test", "revise before testing", "refer", "stop",
}
SCORE_MAXIMUMS = {"M01": 7.0, "P01": 8.0, "L01": 8.0, "A01": 7.0, "H01": 5.0}
MEASURE_FAMILIES = {"implementation", "process", "response", "outcome", "access", "balancing", "accountability", "safety"}


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

    require(root.is_dir(), "Candidate directory exists")
    required = set(CONTROL_FILES) | set(RECORD_FILES) | {"release-manifest.csv"}
    require(all((root / name).is_file() for name in required), "All controls records and manifest are present")

    header, manifest = read_csv(root / "release-manifest.csv")
    require(header == MANIFEST_FIELDS, "Release manifest header matches")
    require(len(manifest) == 334, "Release manifest has 334 immutable rows")
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths) and len(set(paths)) == 334, "Release manifest paths are sorted and unique")
    require(set(CONTROL_FILES).issubset(paths), "All nine controls are immutable")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Portable manifest path: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")
        require(bool(row["source_unit"] and row["source_version"] and row["role"]), f"Manifest provenance complete: {row['relative_path']}")
    expected_tree = set(paths) | set(RECORD_FILES) | {"release-manifest.csv"}
    actual_tree = {
        path.relative_to(root).as_posix() for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual_tree == expected_tree and len(actual_tree) == 358, "Candidate has exactly 358 expected files")
    require(Counter(row["source_unit"] for row in manifest) == {
        "APP-2 Module 07": 9, "oclc-app2-cp01": 150, "oclc-app2-cp02": 175,
    }, "Immutable provenance counts match")

    for contract in CHECKPOINTS:
        checkpoint = root / f"evidence/{contract['directory']}"
        files = sum(path.is_file() for path in checkpoint.rglob("*") if "__pycache__" not in path.parts)
        require(files == contract["files"], f"{contract['id']} nested file count matches")
        require(sha256(checkpoint / "candidate-manifest.csv") == contract["manifest_sha256"], f"{contract['id']} candidate manifest matches")
        run_validator(checkpoint / "validate_checkpoint.py", checkpoint)
        checks.append(f"{contract['id']} nested validator passes")
        release = root / f"evidence/provenance/{contract['directory']}-release.json"
        require(sha256(release) == contract["release_sha256"], f"{contract['id']} release identity matches")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    contract = json.loads((root / "leadership-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {
        "id": "oclc-app2-07", "version": "0.1.0", "commons_release": "0.63.0",
        "course": "APP-2: Data for Patient Experience and Engagement", "hours": 16.0, "course_points": 35,
    }, "Leadership module identity matches")
    require(set(contract["allowed_recommendations"]) == ALLOWED_RECOMMENDATIONS, "Allowed recommendation set matches")
    require(contract["reference_recommendation"] == "revise before testing" and contract["reference_package_status"] == "accept with conditions", "Reference decisions match")
    require(contract["score"]["criteria"] == SCORE_MAXIMUMS and contract["score"]["minimum_to_pass"] == 28.0, "Score contract matches")
    require(contract["required_gates"] == 26 and contract["defense_questions"] == 14 and contract["required_measures"] == 14, "Gate defense and measure counts match")
    require(set(contract["measure_families"]) == MEASURE_FAMILIES, "Measure family contract matches")

    profile = (root / "clinician-profile.md").read_text(encoding="utf-8")
    profile_values = (
        "Joe Joseph, MD, SFHM", "Fellow in Hospital Medicine in 2015", "Senior Fellow in Hospital Medicine in 2017",
        "Regional Chief Medical Officer in a 2019 release", "makes no claim about Dr. Joseph's current employer or title",
        "https://www.soundphysicians.com/press-release/sound-physicians-actively-participating-hospital-medicine-2015/",
        "https://www.soundphysicians.com/press-release/sound-physicians-thought-leaders-presenting-at-hospital-medicine-2017-annual-conference/",
        "https://www.soundphysicians.com/press-release/sound-physicians-acquires-indigo-health-partners/",
    )
    require(all(value in profile for value in profile_values), "Clinician identity sources and current-title boundary match")
    partner_role = (root / "patient-partner-role.md").read_text(encoding="utf-8")
    require(all(value in partner_role for value in ("pending before alpha", "compensation", "shares authority", "withdraw")), "Patient co-lead role and pending status match")
    session = (root / "leadership-session-plan.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^## Segment [1-4]", session)) == 4 and session.count("4 hours") == 4, "Four leadership segments total 16 hours")
    assessment = (root / "assessment.md").read_text(encoding="utf-8")
    require("35.00 of 35.00" in assessment and len(re.findall(r"(?m)^\d+\. ", assessment)) == 26, "Assessment preserves 35 points and 26 gates")

    for name in CONTROL_FILES + RECORD_FILES:
        path = root / name
        if path.suffix.lower() not in {".md", ".csv", ".json", ".py"} and path.name != "VERSION":
            continue
        text = path.read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        if path.suffix.lower() != ".py":
            require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if name in RECORD_FILES:
            if starter:
                require(bool(PLACEHOLDER.search(text)), f"Starter prompt is present: {name}")
            else:
                require(not PLACEHOLDER.search(text), f"Leadership record is complete: {name}")

    csv_headers = {
        "stakeholder-roles.csv": ["role_id", "role", "accountable_for", "responsible_for", "consulted_on", "informed_about", "decision_right", "status"],
        "measures-monitoring.csv": ["measure_id", "family", "name", "numerator", "denominator", "exclusions", "timing", "owner", "missingness_rule", "interpretation", "trigger", "response"],
        "stop-escalation-rules.csv": ["rule_id", "trigger", "immediate_action", "escalation_owner", "restart_evidence", "restart_authority"],
        "evidence-index.csv": ["claim_id", "claim", "evidence_path", "evidence_type", "owner", "status"],
        "component-score.csv": ["criterion_id", "criterion", "maximum", "score", "evidence", "status"],
        "gate-results.csv": ["gate_id", "gate", "result", "evidence", "reviewer", "condition_id"],
        "conditions-register.csv": ["condition_id", "condition", "owner", "due_point", "evidence", "verifier", "status", "escalation_trigger"],
    }
    tables: dict[str, list[dict[str, str]]] = {}
    for name, expected_header in csv_headers.items():
        table_header, rows = read_csv(root / name)
        require(table_header == expected_header, f"CSV header matches: {name}")
        require(bool(rows), f"CSV has at least one row: {name}")
        tables[name] = rows

    if starter:
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "assembled_files": 358}
        print(f"APP-2 Module 07 starter validation passed: {len(checks)} checks.")
        return report

    stakeholders = tables["stakeholder-roles.csv"]
    require(len(stakeholders) == 12 and [row["role_id"] for row in stakeholders] == [f"S{i:02d}" for i in range(1, 13)], "Twelve stakeholder roles are ordered")
    required_roles = ("Clinical decision owner", "Patient or caregiver co-lead", "Access and language lead", "Privacy and governance lead", "Model reviewer", "Independent reproducer")
    require(all(role in {row["role"] for row in stakeholders} for role in required_roles), "Clinical patient access governance model and independent roles are present")
    require(all(row["accountable_for"] and row["responsible_for"] and row["decision_right"] and row["status"] for row in stakeholders), "Every stakeholder has ownership authority and status")

    measures = tables["measures-monitoring.csv"]
    require(len(measures) == 14 and [row["measure_id"] for row in measures] == [f"M{i:02d}" for i in range(1, 15)], "Fourteen ordered measures are present")
    require(set(row["family"] for row in measures) == MEASURE_FAMILIES, "All eight measure families are present")
    require(all(row["numerator"] and row["denominator"] and row["owner"] and row["missingness_rule"] and row["trigger"] and row["response"] for row in measures), "Every measure has a complete monitoring and response contract")

    stop_rules = tables["stop-escalation-rules.csv"]
    require(len(stop_rules) == 14 and [row["rule_id"] for row in stop_rules] == [f"R{i:02d}" for i in range(1, 15)], "Fourteen ordered stop and escalation rules are present")
    require(all(row["immediate_action"] and row["escalation_owner"] and row["restart_evidence"] and row["restart_authority"] for row in stop_rules), "Every stop rule has action ownership restart evidence and authority")

    evidence = tables["evidence-index.csv"]
    require(len(evidence) == 18 and [row["claim_id"] for row in evidence] == [f"E{i:02d}" for i in range(1, 19)], "Eighteen ordered evidence claims are present")
    for row in evidence:
        path = Path(row["evidence_path"])
        require(not path.is_absolute() and ".." not in path.parts and (root / path).is_file(), f"Evidence path exists: {row['claim_id']}")

    scores = tables["component-score.csv"]
    require([row["criterion_id"] for row in scores] == list(SCORE_MAXIMUMS), "Five score criteria are in fixed order")
    require(all(float(row["maximum"]) == SCORE_MAXIMUMS[row["criterion_id"]] for row in scores), "Score maximums match")
    total = sum(float(row["score"]) for row in scores)
    require(all(0 <= float(row["score"]) <= float(row["maximum"]) for row in scores) and total >= 28.0, "Scores are bounded and meet the 28-point minimum")
    require(abs(total - 35.0) < 1e-9 and all(row["status"] == "pass" for row in scores), "Reference score is 35.00 of 35.00")

    conditions = tables["conditions-register.csv"]
    condition_ids = {row["condition_id"] for row in conditions}
    require(len(conditions) == 8 and condition_ids == {f"COND-{i:02d}" for i in range(1, 9)}, "Eight reference conditions are registered")
    require(all(row["owner"] and row["due_point"] and row["evidence"] and row["verifier"] and row["status"] == "open" and row["escalation_trigger"] for row in conditions), "Every condition has complete open ownership")

    gates = tables["gate-results.csv"]
    require(len(gates) == 26 and [row["gate_id"] for row in gates] == [f"G{i:02d}" for i in range(1, 27)], "Twenty-six gates are ordered")
    require(all(row["result"] in {"pass", "pass with condition"} for row in gates), "Every gate passes or passes with an allowed condition")
    require(all((not row["condition_id"] and row["result"] == "pass") or (row["condition_id"] in condition_ids and row["result"] == "pass with condition") for row in gates), "Gate conditions are consistent and registered")
    require(all((root / Path(row["evidence"])).is_file() for row in gates), "Every gate cites an existing evidence file")

    recommendation_text = (root / "leadership-recommendation.md").read_text(encoding="utf-8")
    recommendation = markdown_field(recommendation_text, "Recommendation")
    require(recommendation in ALLOWED_RECOMMENDATIONS, "Organizational recommendation is allowed")
    require(markdown_field(recommendation_text, "Patient contact and fielding") == "prohibited" and markdown_field(recommendation_text, "Clinical implementation") == "prohibited" and markdown_field(recommendation_text, "Model deployment") == "prohibited", "Recommendation preserves contact implementation and deployment prohibitions")
    require("universal offer" in recommendation_text and "no model or group targeting" in recommendation_text, "Recommendation preserves universal offer and no targeting")

    synthesis = (root / "evidence-synthesis.md").read_text(encoding="utf-8")
    facts = ("1,255", "782", "473", "28,455", "420 comments", "eight themes", "120-record", "80.00000000", "0.77142857", "0.78333333", "35 of 52", "19 of 36", "0.08367520", "0.50 threshold")
    require(all(value in synthesis for value in facts), "Evidence synthesis preserves exact accepted facts")
    patient_summary = (root / "patient-facing-summary.md").read_text(encoding="utf-8")
    require(all(value in patient_summary for value in ("generated responses and comments", "not things real patients said", "does not tell us what local patients want", "No model would select", "does not authorize contact or a change in care")), "Patient-facing summary preserves evidence and authorization boundaries")
    partner = (root / "patient-partner-decision-record.md").read_text(encoding="utf-8")
    require(markdown_field(partner, "Record status") == "simulated construction example; not actual patient or caregiver participation", "Patient-partner record remains simulated")
    require(markdown_field(partner, "Actual patient or caregiver statements") == "0" and markdown_field(partner, "Named patient/caregiver co-lead") == "pending before alpha", "Patient-partner statement count and pending co-lead match")
    appendix = (root / "technical-appendix.md").read_text(encoding="utf-8")
    appendix_facts = ("149 files", "174 files", "1,255", "28,455", "420", "0.77142857", "35 of 52", "19 of 36", "2.48289986", "2.39922466", "0.08367520", "0.50")
    require(all(value in appendix for value in appendix_facts), "Technical appendix preserves accepted package and analysis facts")

    defense = (root / "leadership-defense.md").read_text(encoding="utf-8")
    require(markdown_field(defense, "Defense status") == "adequate for curriculum construction", "Reference defense status is adequate")
    require(len(re.findall(r"(?m)^## Q(?:0[1-9]|1[0-4])\.", defense)) == 14, "All 14 defense answers are present")
    require(all(len(section.strip()) >= 100 for section in re.split(r"(?m)^## Q(?:0[1-9]|1[0-4])\..*$", defense)[1:]), "Every defense answer is substantive")

    reviewer = (root / "reviewer-record.md").read_text(encoding="utf-8")
    reviewer_roles = ("APP-2 faculty owner", "Joe Joseph, MD, SFHM", "Patient or caregiver co-lead", "Patient-experience measurement lead", "Survey-methods lead", "Health-services data lead", "Qualitative-methods lead", "Equity reviewer", "Access and language reviewer", "Privacy and data-governance reviewer", "Responsible-AI and model reviewer", "Independent reproducer")
    require(all(role in reviewer for role in reviewer_roles), "Required clinical patient technical governance and independent reviewers are present")
    reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8")
    require(all(value in reproducibility for value in ("`334`", "`358`", "Two-build immutable comparison: `pass`", "Independent human reproducer: `pending before alpha`")), "Reproduction record matches package contract")
    accessibility = (root / "accessibility-language-review.md").read_text(encoding="utf-8")
    require(all(value in accessibility for value in ("Phone route", "Caption and transcript route", "Interpreter support", "Proxy support", "Accessible formats", "Defense alternative")), "Accessibility and language routes are complete")
    require("Patient or restricted data shared: `none`" in (root / "ai-use.md").read_text(encoding="utf-8"), "Agent record excludes patient and restricted data")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    expected_progression = {
        "Candidate score": "35.00 of 35.00",
        "Gates": "26 of 26 pass or pass with an allowed condition",
        "Defense": "adequate for curriculum construction",
        "Candidate status": "accept with conditions",
        "Organizational recommendation": recommendation,
        "Final checkpoint": "permitted for curriculum construction",
        "Patient/caregiver co-lead": "pending before alpha",
        "Patient contact and fielding": "prohibited",
        "Official HCAHPS reporting": "prohibited",
        "Clinical implementation": "prohibited",
        "Patient or group targeting": "prohibited",
        "Model deployment": "prohibited",
        "Human sign-off scope": "curriculum construction only",
        "Course points": "drafted here and recorded once at Checkpoint 03",
    }
    require(all(markdown_field(progression, key) == value for key, value in expected_progression.items()), "Progression fields are separate and consistent")

    report = {
        "status": "pass", "mode": "complete", "checks_passed": len(checks),
        "assembled_files": 358, "manifest_rows": 334, "score": total,
        "gates_passed": 26, "recommendation": recommendation,
    }
    print(f"APP-2 Module 07 complete validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path, starter: bool = False) -> None:
    try:
        validate(root, starter=starter)
    except (ValidationError, OSError, ValueError, json.JSONDecodeError):
        return
    raise AssertionError(f"Expected validation failure for {root}")


def command(args: list[str]) -> None:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode:
        raise AssertionError(result.stderr.strip() or result.stdout.strip())


def self_check() -> None:
    assembler = MODULE_ROOT / "assemble_candidate.py"
    course_root = MODULE_ROOT.parent.parent
    with tempfile.TemporaryDirectory(prefix="app2-module07-validate-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        command([sys.executable, str(assembler), "--target", str(reference), "--reference"])
        report = validate(reference)
        assert report["assembled_files"] == 358 and report["manifest_rows"] == 334

        copied = subprocess.run([sys.executable, str(reference / "validate_candidate.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0, copied.stderr or copied.stdout

        checkpoint1, checkpoint2 = base / "checkpoint1", base / "checkpoint2"
        command([sys.executable, str(course_root / "checkpoints/01-measurement-representation-readiness/build_checkpoint.py"), "--target", str(checkpoint1), "--reference"])
        command([sys.executable, str(course_root / "checkpoints/02-linked-evidence-patient-voice-release/build_checkpoint.py"), "--target", str(checkpoint2), "--reference"])
        starter = base / "starter"
        command([sys.executable, str(assembler), "--checkpoint1", str(checkpoint1), "--checkpoint2", str(checkpoint2), "--target", str(starter)])
        validate(starter, starter=True)

        changed = base / "changed-evidence"
        shutil.copytree(reference, changed)
        release = changed / "evidence/provenance/checkpoint1-release.json"
        release.write_text(release.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        expect_failure(changed)

        changed = base / "changed-score"
        shutil.copytree(reference, changed)
        score = changed / "component-score.csv"
        score.write_text(score.read_text(encoding="utf-8").replace("7.00,7.00", "7.00,1.00", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "failed-gate"
        shutil.copytree(reference, changed)
        gates = changed / "gate-results.csv"
        gates.write_text(gates.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "bad-recommendation"
        shutil.copytree(reference, changed)
        decision = changed / "leadership-recommendation.md"
        decision.write_text(decision.read_text(encoding="utf-8").replace("revise before testing", "deploy model", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "false-partner-claim"
        shutil.copytree(reference, changed)
        partner = changed / "patient-partner-decision-record.md"
        partner.write_text(partner.read_text(encoding="utf-8").replace("simulated construction example; not actual patient or caregiver participation", "actual patient partnership"), encoding="utf-8")
        expect_failure(changed)

        changed = base / "bad-progression"
        shutil.copytree(reference, changed)
        progression = changed / "progression-decision.md"
        progression.write_text(progression.read_text(encoding="utf-8").replace("Clinical implementation: `prohibited`", "Clinical implementation: `authorized`"), encoding="utf-8")
        expect_failure(changed)
    print("APP-2 Module 07 validator self-check passed: complete, starter, copied-validator, evidence, score, gate, recommendation, partnership, and progression routes.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if args.candidate is None:
            parser.error("candidate is required unless --self-check is used")
        print(json.dumps(validate(args.candidate, starter=args.starter), indent=2))
    except (ValidationError, OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
