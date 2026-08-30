"""Validate APP-1 Module 07 clinical leadership candidates."""

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
    "clinician-session-plan.md", "assessment.md", "assemble_candidate.py", "validate_candidate.py",
)
RECORD_FILES = (
    "README.md", "evidence-synthesis.md", "improvement-recommendation.md", "people-equity-safety.md",
    "stakeholder-roles.csv", "workflow-feasibility.md", "bounded-test-plan.md", "measures-monitoring.csv",
    "stop-escalation-rules.csv", "leadership-reflection.md", "technical-appendix.md", "evidence-index.csv",
    "accessibility-review.md", "reproducibility-check.md", "ai-use.md", "component-score.csv",
    "gate-results.csv", "conditions-register.csv", "technical-defense.md", "reviewer-record.md",
    "progression-decision.md",
)
MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]
ALLOWED_RECOMMENDATIONS = {
    "run bounded prospective improvement test", "revise before testing", "refer", "stop",
}
CHECKPOINTS = (
    {
        "directory": "checkpoint1", "id": "oclc-app1-cp01", "files": 91,
        "manifest_sha256": "ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860",
        "release_sha256": "ef2ee1dd1fcac47dda2efd680b9605862a0006962867d59a836dec4c276b090c",
    },
    {
        "directory": "checkpoint2", "id": "oclc-app1-cp02", "files": 113,
        "manifest_sha256": "f5f892c2b5f6c193f5389c10f7e60df81b1400ca5a163734a103efa745c54ed1",
        "release_sha256": "58cc270fad6649feec5e958b0850ea3dff3a8119599c30f2e900d68ad5f591da",
    },
)
SCORE_MAXIMUMS = {"C01": 8.0, "R01": 5.0, "L01": 10.0, "A01": 8.0, "H01": 4.0}
MEASURE_MINIMUMS = {"process": 2, "outcome": 1, "balancing": 2, "access": 2, "implementation": 1, "data-quality": 2}


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
    require(len(manifest) == 214, "Release manifest has 214 immutable rows")
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths) and len(set(paths)) == 214, "Release manifest paths are sorted and unique")
    require(set(CONTROL_FILES).issubset(paths), "All eight controls are immutable")
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
    require(actual_tree == expected_tree and len(actual_tree) == 236, "Candidate has exactly 236 expected files")
    sources = Counter(row["source_unit"] for row in manifest)
    require(sources == {"APP-1 Module 07": 8, "oclc-app1-cp01": 92, "oclc-app1-cp02": 114}, "Immutable provenance counts match")

    for contract in CHECKPOINTS:
        directory = str(contract["directory"])
        checkpoint = root / f"evidence/{directory}"
        checkpoint_files = sum(path.is_file() for path in checkpoint.rglob("*"))
        require(checkpoint_files == contract["files"], f"{contract['id']} nested file count matches")
        require(sha256(checkpoint / "candidate-manifest.csv") == contract["manifest_sha256"], f"{contract['id']} candidate manifest matches")
        run_validator(checkpoint / "validate_checkpoint.py", checkpoint)
        checks.append(f"{contract['id']} nested validator passes")
        release = root / f"evidence/provenance/{directory}-release.json"
        require(sha256(release) == contract["release_sha256"], f"{contract['id']} release identity matches")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    contract = json.loads((root / "leadership-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {
        "id": "oclc-app1-07", "version": "0.1.0", "commons_release": "0.55.0",
        "course": "APP-1: Data for Clinical Care", "hours": 16.0, "course_points": 35,
    }, "Leadership module identity matches")
    require(set(contract["allowed_recommendations"]) == ALLOWED_RECOMMENDATIONS, "Allowed recommendation set matches")
    require(contract["reference_recommendation"] == "revise before testing", "Reference recommendation matches")
    require(contract["score"]["criteria"] == SCORE_MAXIMUMS and contract["score"]["minimum_to_pass"] == 28.0, "Score contract matches")
    require(contract["required_gates"] == 24 and contract["defense_questions"] == 12, "Gate and defense counts match")
    require(contract["measure_minimums"] == MEASURE_MINIMUMS, "Measure minimums match")

    profile = (root / "clinician-profile.md").read_text(encoding="utf-8")
    profile_values = (
        "Joe Joseph, MD, SFHM", "Fellow in Hospital Medicine in 2015", "Senior Fellow in Hospital Medicine in 2017",
        "Regional Chief Medical Officer in a 2019 release", "makes no claim about Dr. Joseph's current employer or title",
        "https://www.soundphysicians.com/press-release/sound-physicians-actively-participating-hospital-medicine-2015/",
        "https://www.soundphysicians.com/press-release/sound-physicians-thought-leaders-presenting-at-hospital-medicine-2017-annual-conference/",
        "https://www.soundphysicians.com/press-release/sound-physicians-acquires-indigo-health-partners/",
    )
    require(all(value in profile for value in profile_values), "Clinician identity sources and current-title boundary match")
    session = (root / "clinician-session-plan.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^## Session [1-4]", session)) == 4 and session.count("4 hours") == 4, "Four clinician-led segments total 16 hours")
    assessment = (root / "assessment.md").read_text(encoding="utf-8")
    require("35.00 of 35.00" in assessment and len(re.findall(r"(?m)^\d+\. ", assessment)) == 24, "Assessment preserves 35 points and 24 gates")

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
        "stakeholder-roles.csv": ["stakeholder_id", "raci_role", "stakeholder", "decision_responsibility", "required_action", "evidence", "owner_status"],
        "measures-monitoring.csv": ["measure_id", "family", "name", "definition", "numerator", "denominator", "unit", "direction", "source", "timing", "cadence", "owner", "trigger", "action", "subgroup_rule", "missingness_rule"],
        "stop-escalation-rules.csv": ["rule_id", "trigger", "immediate_action", "owner", "notification", "restart_evidence", "final_authority"],
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
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "assembled_files": 236}
        print(f"APP-1 Module 07 starter validation passed: {len(checks)} checks.")
        return report

    stakeholders = tables["stakeholder-roles.csv"]
    require(len(stakeholders) == 8 and [row["stakeholder_id"] for row in stakeholders] == [f"S{i:02d}" for i in range(1, 9)], "Eight stakeholder rows are ordered")
    require({row["raci_role"] for row in stakeholders} == {"accountable", "responsible", "consulted", "informed"}, "All four stakeholder role classes are present")
    require(sum(row["raci_role"] == "accountable" for row in stakeholders) == 1 and sum(row["raci_role"] == "responsible" for row in stakeholders) >= 2, "Accountable and responsible ownership is explicit")

    measures = tables["measures-monitoring.csv"]
    require(len(measures) == 11 and len({row["measure_id"] for row in measures}) == 11, "Eleven unique measures are present")
    families = Counter(row["family"] for row in measures)
    require(all(families[family] >= minimum for family, minimum in MEASURE_MINIMUMS.items()), "Every required measure family meets its minimum")
    require(all(row["numerator"] and row["denominator"] and row["owner"] and row["trigger"] and row["action"] for row in measures), "Every measure has denominator owner trigger and action")
    require(all(row["subgroup_rule"] and row["missingness_rule"] for row in measures), "Every measure has subgroup and missingness rules")

    stop_rules = tables["stop-escalation-rules.csv"]
    require(len(stop_rules) == 8 and [row["rule_id"] for row in stop_rules] == [f"STOP{i:02d}" for i in range(1, 9)], "Eight ordered stop and escalation rules are present")
    require(all(row["immediate_action"] and row["owner"] and row["notification"] and row["restart_evidence"] and row["final_authority"] for row in stop_rules), "Every stop rule has action ownership notice restart evidence and authority")

    evidence = tables["evidence-index.csv"]
    require(len(evidence) == 16 and [row["claim_id"] for row in evidence] == [f"E{i:02d}" for i in range(1, 17)], "Sixteen ordered evidence claims are present")
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
    require(len(conditions) == 6 and condition_ids == {f"COND-{i:02d}" for i in range(1, 7)}, "Six reference conditions are registered")
    require(all(row["owner"] and row["due_point"] and row["evidence"] and row["verifier"] and row["status"] == "open" and row["escalation_trigger"] for row in conditions), "Every condition has complete open ownership")

    gates = tables["gate-results.csv"]
    require(len(gates) == 24 and [row["gate_id"] for row in gates] == [f"G{i:02d}" for i in range(1, 25)], "Twenty-four gates are ordered")
    require(all(row["result"] in {"pass", "pass with condition"} for row in gates), "Every gate passes or passes with an allowed condition")
    require(all((not row["condition_id"] and row["result"] == "pass") or (row["condition_id"] in condition_ids and row["result"] == "pass with condition") for row in gates), "Gate conditions are consistent and registered")
    require(all((root / Path(row["evidence"])).is_file() for row in gates), "Every gate cites an existing evidence file")

    recommendation_text = (root / "improvement-recommendation.md").read_text(encoding="utf-8")
    recommendation = markdown_field(recommendation_text, "Recommendation")
    require(recommendation in ALLOWED_RECOMMENDATIONS, "Clinical recommendation is allowed")
    require(markdown_field(recommendation_text, "Clinical implementation") == "prohibited" and markdown_field(recommendation_text, "Model deployment") == "prohibited", "Recommendation preserves implementation and deployment prohibitions")
    if recommendation == "revise before testing":
        require("local workflow" in recommendation_text and "patient or caregiver partner" in recommendation_text and "universal offer" in recommendation_text, "Reference revision conditions and universal offer are explicit")

    synthesis = (root / "evidence-synthesis.md").read_text(encoding="utf-8")
    facts = ("476 people", "87 acute-return events", "129 people", "347", "0.00636020", "0.09609243", "0.10745654", "does not change the improvement decision")
    require(all(value in synthesis for value in facts), "Evidence synthesis preserves exact case and model facts")
    appendix = (root / "technical-appendix.md").read_text(encoding="utf-8")
    require(all(value in appendix for value in ("518 people", "476 people", "87", "389", "0.00636020", "0.66363212", "0.62371615", "60", "67")), "Technical appendix preserves exact accepted facts")

    defense = (root / "technical-defense.md").read_text(encoding="utf-8")
    require(markdown_field(defense, "Defense status") == "adequate for curriculum construction", "Reference defense status is adequate")
    require(len(re.findall(r"(?m)^## Q(?:0[1-9]|1[0-2])\.", defense)) == 12, "All 12 defense answers are present")
    require(all(len(section.strip()) >= 100 for section in re.split(r"(?m)^## Q(?:0[1-9]|1[0-2])\..*$", defense)[1:]), "Every defense answer is substantive")

    reviewer = (root / "reviewer-record.md").read_text(encoding="utf-8")
    reviewer_roles = (
        "APP-1 faculty owner", "Hospital medicine clinical decision owner", "Improvement science reviewer",
        "Biostatistical methods reviewer", "Clinical informatics reviewer", "Equity reviewer",
        "Accessibility reviewer", "Privacy and data-governance reviewer", "Responsible-AI reviewer", "Independent reproducer",
    )
    require(all(role in reviewer for role in reviewer_roles), "All ten reviewer roles are present")
    require(all(value in (root / "reproducibility-check.md").read_text(encoding="utf-8") for value in ("`214`", "`236`", "Two-build immutable comparison: `pass`")), "Reproduction record matches package contract")
    require("Patient or restricted data shared: `none`" in (root / "ai-use.md").read_text(encoding="utf-8"), "Agent record excludes patient and restricted data")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    expected_progression = {
        "Candidate score": "35.00 of 35.00",
        "Gates": "24 of 24 pass or pass with an allowed condition",
        "Defense": "adequate for curriculum construction",
        "Candidate status": "accept with conditions",
        "Clinical recommendation": recommendation,
        "Final checkpoint": "permitted for curriculum construction",
        "Clinical implementation": "prohibited",
        "Model deployment": "prohibited",
        "Patient targeting": "prohibited",
        "Human sign-off scope": "curriculum construction only",
        "Course points": "drafted here and recorded once at Checkpoint 3",
    }
    require(all(markdown_field(progression, key) == value for key, value in expected_progression.items()), "Progression fields are separate and consistent")

    report = {
        "status": "pass", "mode": "complete", "checks_passed": len(checks),
        "assembled_files": 236, "manifest_rows": 214, "score": total,
        "gates_passed": 24, "recommendation": recommendation,
    }
    print(f"APP-1 Module 07 complete validation passed: {len(checks)} checks.")
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
    with tempfile.TemporaryDirectory(prefix="app1-module07-validate-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        command([sys.executable, str(assembler), "--target", str(reference), "--reference"])
        report = validate(reference)
        assert report["assembled_files"] == 236 and report["manifest_rows"] == 214

        copied = subprocess.run([sys.executable, str(reference / "validate_candidate.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0, copied.stderr or copied.stdout

        checkpoint1, checkpoint2 = base / "checkpoint1", base / "checkpoint2"
        command([sys.executable, str(course_root / "checkpoints/01-longitudinal-survival-readiness/build_checkpoint.py"), "--target", str(checkpoint1), "--reference"])
        command([sys.executable, str(course_root / "checkpoints/02-adjusted-variation-improvement-release/build_checkpoint.py"), "--target", str(checkpoint2), "--reference"])
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
        score.write_text(score.read_text(encoding="utf-8").replace("8.00,8.00", "8.00,1.00", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "failed-gate"
        shutil.copytree(reference, changed)
        gates = changed / "gate-results.csv"
        gates.write_text(gates.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "bad-recommendation"
        shutil.copytree(reference, changed)
        decision = changed / "improvement-recommendation.md"
        decision.write_text(decision.read_text(encoding="utf-8").replace("revise before testing", "deploy model", 1), encoding="utf-8")
        expect_failure(changed)

        changed = base / "bad-progression"
        shutil.copytree(reference, changed)
        progression = changed / "progression-decision.md"
        progression.write_text(progression.read_text(encoding="utf-8").replace("Clinical implementation: `prohibited`", "Clinical implementation: `authorized`"), encoding="utf-8")
        expect_failure(changed)
    print("APP-1 Module 07 validator self-check passed: complete, starter, copied-validator, evidence, score, gate, recommendation, and progression routes.")


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
