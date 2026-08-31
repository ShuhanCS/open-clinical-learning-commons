"""Validate APP-3 Module 07 clinical leadership candidates."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from decimal import Decimal
from pathlib import Path
from typing import Callable


MODULE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
CONTROL_FILES = (
    ".gitattributes", "VERSION", "leadership-contract.json", "clinician-profile.md",
    "clinician-session-plan.md", "assessment.md", "assemble_candidate.py", "validate_candidate.py",
)
RECORD_FILES = (
    "README.md", "evidence-synthesis.md", "frontline-brief.md", "leadership-summary.md",
    "recommendation-and-alternatives.md", "people-equity-safety-workforce.md", "stakeholder-roles.csv",
    "workflow-resource-feasibility.md", "revision-learning-plan.md", "stewardship-plan.md",
    "monitoring-measures.csv", "escalation-fallback-rules.csv", "disagreement-record.md",
    "leadership-reflection.md", "technical-appendix.md", "evidence-index.csv", "accessibility-review.md",
    "reproducibility-check.md", "responsible-claims-audit.md", "ai-use.md", "component-score.csv",
    "gate-results.csv", "conditions-register.csv", "technical-defense.md", "reviewer-record.md",
    "progression-decision.md",
)
MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]
ALLOWED_RECOMMENDATIONS = {
    "run bounded prospective improvement test", "revise before testing", "refer", "stop",
}
CHECKPOINTS = (
    {
        "directory": "checkpoint1", "id": "oclc-app3-cp01", "files": 153,
        "manifest_sha256": "9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656",
        "release_sha256": "270b4e49d1c21d8faf7243cd11cef1dddea836d32be551dfe72edac771b31f27",
    },
    {
        "directory": "checkpoint2", "id": "oclc-app3-cp02", "files": 226,
        "manifest_sha256": "4f2a303bc5626ea58139aa935da157f524db1d25b5a158a927ef5daec197958a",
        "release_sha256": "b8af80b7e07c2eac2aeb0e9206533bfae134f55d69a5df9038a7a9a915c4dd05",
    },
)
SCORE_MAXIMUMS = {"E01": Decimal("8.00"), "C01": Decimal("9.00"), "L01": Decimal("8.00"), "M01": Decimal("6.00"), "H01": Decimal("4.00")}


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
    require(len(manifest) == 389, "Release manifest has 389 immutable rows")
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths) and len(set(paths)) == 389, "Release manifest paths are sorted and unique")
    require(set(CONTROL_FILES).issubset(paths), "All eight controls are immutable")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts and "\\" not in row["relative_path"], f"Portable manifest path: {row['relative_path']}")
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
    require(actual_tree == expected_tree and len(actual_tree) == 416, "Candidate has exactly 416 expected files")
    sources = Counter(row["source_unit"] for row in manifest)
    require(sources == {"APP-3 Module 07": 8, "oclc-app3-cp01": 154, "oclc-app3-cp02": 227}, "Immutable provenance counts match")

    for contract in CHECKPOINTS:
        directory = str(contract["directory"])
        checkpoint = root / f"evidence/{directory}"
        checkpoint_files = sum(path.is_file() for path in checkpoint.rglob("*") if "__pycache__" not in path.parts)
        require(checkpoint_files == contract["files"], f"{contract['id']} nested file count matches")
        require(sha256(checkpoint / "candidate-manifest.csv") == contract["manifest_sha256"], f"{contract['id']} candidate manifest matches")
        run_validator(checkpoint / "validate_checkpoint.py", checkpoint)
        checks.append(f"{contract['id']} nested validator passes")
        release = root / f"evidence/provenance/{directory}-release.json"
        require(sha256(release) == contract["release_sha256"], f"{contract['id']} release identity matches")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    contract = json.loads((root / "leadership-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {
        "id": "oclc-app3-07", "version": "0.1.0", "commons_release": "0.74.0",
        "course": "APP-3: Data for Clinical Performance and Improvement", "hours": 16.0, "course_points": 35,
    }, "Leadership module identity matches")
    require(set(contract["allowed_recommendations"]) == ALLOWED_RECOMMENDATIONS, "Allowed recommendation set matches")
    require(contract["reference"] == {
        "package_status": "accept with conditions", "recommendation": "revise before testing",
        "selected_scenario": "none", "accepted_forecast": "seasonal exponential smoothing",
        "ml_decision": "retain transparent forecast", "final_checkpoint_permission": "permitted for curriculum construction",
    }, "Reference decisions match")
    require(
        {key: Decimal(str(value)) for key, value in contract["score"]["criteria"].items()} == SCORE_MAXIMUMS
        and Decimal(str(contract["score"]["minimum_to_pass"])) == Decimal("28.0")
        and Decimal(str(contract["score"]["maximum"])) == Decimal("35.0"),
        "Score contract matches",
    )
    require(contract["required_gates"] == 26 and contract["defense_questions"] == 14, "Gate and defense counts match")
    require(all(value == "prohibited" for value in contract["boundaries"].values()), "All authority boundaries remain prohibited")

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
    require("35.00 of 35.00" in assessment and "all 26 gates" in assessment and "14-question defense" in assessment, "Assessment preserves points gates and defense")

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
        "monitoring-measures.csv": ["measure_id", "domain", "measure", "evidence_state", "accepted_value", "unit", "source_path", "owner", "review_cadence", "decision_use", "leadership_response", "definition_changed"],
        "escalation-fallback-rules.csv": ["rule_id", "measure_id", "response_level", "confirmation_owner", "decision_owner", "fallback_state", "restart_condition", "automatic_action", "source_path"],
        "evidence-index.csv": ["claim_id", "material_claim", "evidence_path", "owner", "decision_use", "limit"],
        "component-score.csv": ["criterion_id", "criterion", "points_available", "points_awarded", "evidence"],
        "gate-results.csv": ["gate_id", "gate", "status", "evidence", "owner"],
        "conditions-register.csv": ["condition_id", "condition", "owner", "due_point", "verification", "effect_if_open", "status"],
    }
    for name, expected_header in csv_headers.items():
        actual_header, _ = read_csv(root / name)
        require(actual_header == expected_header, f"CSV header matches: {name}")
    if starter:
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "assembled_files": 416}
        print(f"APP-3 Module 07 starter validation passed: {len(checks)} checks.")
        return report

    synthesis = (root / "evidence-synthesis.md").read_text(encoding="utf-8")
    synthesis_terms = (
        "CGH-ED-01", "43,628", "39,975", "3,653", "Weeks 1 through 24", "nine signal records",
        "894", "673", "358", "379", "75.2796", "40.0447", "99.0302", "49 minutes at baseline", "66 in the target window",
        "401 and 242", "Root cause and staffing adequacy are not established", "28 rolling origins", "588 common target rows",
        "5.937283", "7.307180", "0.008215", "15.141268", "876.924084", "805.136639 to 970.733035",
        "Little's Law equilibrium is not established", "4,000 paired runs", "Six comparisons are null or failed", "no option qualified",
        "21.244986", "1.958703", "5.803341", "41.617987", "86.671644", "0.316383", "14.547388",
        "Safety and return within 72 hours were not simulated", "28 feasibility rows", "five supported, 18 requires-local-evidence, and five not-supported",
        "S00 is retained", "S01 and S03 require revision", "S02 is stopped", "12 measures", "three prospectively unavailable values",
        "ten human-owned escalation rules", "zero automatic actions", "no live connection", "same 28 folds and 588 target rows",
        "5.205494", "860.277096", "0.750000", "0.731788", "Seven of eight rules pass", "revise before testing",
    )
    require(all(term in synthesis for term in synthesis_terms), "Evidence synthesis contains exact accepted facts")
    require(not re.search(r"(?i)signal proves cause|option selected|safety outcome was simulated|staffing recommendation is authorized|ML challenger is accepted|test is authorized", synthesis), "Evidence synthesis contains no prohibited conclusion")

    frontline = (root / "frontline-brief.md").read_text(encoding="utf-8")
    require(
        all(term in frontline for term in ("fictional", "synthetic", "signal can open review", "revise before testing", "No workflow, staffing, schedule, routing, or clinical change is approved", "without blame", "Silence is not agreement")),
        "Frontline brief is plain blame-free and bounded",
    )
    summary = (root / "leadership-summary.md").read_text(encoding="utf-8")
    require(
        markdown_field(summary, "Package status") == "accept with conditions"
        and markdown_field(summary, "Recommendation") == "revise before testing"
        and markdown_field(summary, "Selected scenario") == "none"
        and markdown_field(summary, "Accepted forecast") == "seasonal exponential smoothing"
        and markdown_field(summary, "ML decision") == "retain transparent forecast",
        "Leadership summary carries exact decisions",
    )

    recommendation = (root / "recommendation-and-alternatives.md").read_text(encoding="utf-8")
    rec = markdown_field(recommendation, "Clinical performance recommendation")
    require(rec in ALLOWED_RECOMMENDATIONS and rec == "revise before testing", "Reference recommendation is allowed and exact")
    require(
        markdown_field(recommendation, "Package status") == "accept with conditions"
        and markdown_field(recommendation, "Selected scenario") == "none"
        and markdown_field(recommendation, "Current test authorization") == "not authorized"
        and markdown_field(recommendation, "Final checkpoint permission") == "permitted for curriculum construction",
        "Recommendation separates package test and checkpoint decisions",
    )
    require(all(term in recommendation for term in ("S00", "S01", "S02", "S03", "40.000000", "25.220413", "R01", "no-change monitoring")), "Recommendation considers every accepted alternative")

    people = (root / "people-equity-safety-workforce.md").read_text(encoding="utf-8")
    require(
        all(term in people for term in ("High-acuity", "language or mobility support", "Safety outcome and 72-hour return were not simulated", "Workforce interruption", "401 and 242", "blame-free", "No unavailable value may be converted to zero")),
        "People review preserves safety access workforce and unavailable limits",
    )
    workflow = (root / "workflow-resource-feasibility.md").read_text(encoding="utf-8")
    require(all(term in workflow for term in ("S00", "40.000000", "25.220413", "not staffing recommendations", "Feasibility is incomplete", "may not authorize a test")), "Workflow feasibility preserves resource and action limits")
    revision = (root / "revision-learning-plan.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^## Stage [1-5]", revision)) == 5 and "does not authorize that protocol now" in revision, "Revision plan has five governed stages and no test authority")
    stewardship = (root / "stewardship-plan.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\| [^|]+ \|", stewardship)) >= 11 and "A changed upstream fact cannot be patched only in leadership prose" in stewardship, "Stewardship covers all evidence owners and change routes")

    _, roles = read_csv(root / "stakeholder-roles.csv")
    require(len(roles) == 12 and [row["stakeholder_id"] for row in roles] == [f"S{number:02d}" for number in range(1, 13)], "Stakeholder register has 12 ordered roles")
    require(sum(row["raci_role"] == "accountable" for row in roles) == 1 and sum(row["raci_role"] == "responsible" for row in roles) >= 7, "Stakeholder register has accountable and responsible ownership")
    require(all(row["stakeholder"] and row["decision_responsibility"] and row["required_action"] and row["evidence"] and row["owner_status"] for row in roles), "Every stakeholder role is complete")

    _, monitoring = read_csv(root / "monitoring-measures.csv")
    require(len(monitoring) == 12 and [row["measure_id"] for row in monitoring] == [f"M{number:02d}" for number in range(1, 13)], "Leadership monitoring retains 12 ordered measures")
    require(sum(row["accepted_value"] == "unavailable" for row in monitoring) == 3 and all(row["definition_changed"] == "0" for row in monitoring), "Monitoring retains three unavailable values and changes no definition")
    source_header, source_measures = read_csv(root / "evidence/checkpoint2/candidate/module-06/outputs/monitoring-measures.csv")
    require(source_header[0:3] == ["measure_id", "domain", "measure"] and len(source_measures) == 12, "Accepted source monitoring table is complete")
    source_by_id = {row["measure_id"]: row for row in source_measures}
    for row in monitoring:
        source = source_by_id[row["measure_id"]]
        require(
            row["domain"] == source["domain"] and row["measure"] == source["measure"]
            and row["evidence_state"] == source["evidence_state"] and row["accepted_value"] == source["value"]
            and row["unit"] == source["unit"] and row["owner"] == source["owner"] and row["review_cadence"] == source["review_cadence"],
            f"Leadership monitoring matches accepted measure: {row['measure_id']}",
        )

    _, escalation = read_csv(root / "escalation-fallback-rules.csv")
    require(len(escalation) == 10 and [row["rule_id"] for row in escalation] == [f"E{number:02d}" for number in range(1, 11)], "Leadership escalation retains ten ordered rules")
    require(all(row["fallback_state"] == "continue no-change monitoring" and row["automatic_action"] == "0" for row in escalation), "Escalation retains no-change fallback and zero automatic actions")
    _, source_escalation = read_csv(root / "evidence/checkpoint2/candidate/module-06/outputs/escalation-fallback.csv")
    source_escalation_by_id = {row["rule_id"]: row for row in source_escalation}
    for row in escalation:
        source = source_escalation_by_id[row["rule_id"]]
        require(
            row["measure_id"] == source["measure_id"] and row["response_level"] == source["response_level"]
            and row["confirmation_owner"] == source["confirmation_owner"] and row["decision_owner"] == source["decision_owner"]
            and row["fallback_state"] == source["fallback_state"] and row["restart_condition"] == source["restart_condition"]
            and row["automatic_action"] == source["automatic_action"],
            f"Leadership escalation matches accepted rule: {row['rule_id']}",
        )

    disagreement = (root / "disagreement-record.md").read_text(encoding="utf-8")
    disagreement_fields = ("Disagreement ID", "Issue", "Position A", "Position B", "Accepted evidence", "Decision effect", "Owner", "Response", "Status", "Escalation route", "Protection")
    require(all(markdown_field(disagreement, field) for field in disagreement_fields) and "Silence is not agreement" in disagreement, "Disagreement record is complete and protected")

    appendix = (root / "technical-appendix.md").read_text(encoding="utf-8")
    appendix_terms = (
        "43,628", "39,975", "3,653", "894", "673", "358", "379", "75.2796", "40.0447", "99.0302",
        "49, 66, 44, and 49", "401", "242", "28", "588", "5.937283", "7.307180", "0.008215", "15.141268",
        "876.924084", "805.136639 to 970.733035", "4,000", "6", "none", "86.671644", "28", "5 supported, 18 requires local evidence, 5 not supported",
        "12", "3", "10", "0", "5.205494", "6.554934", "860.277096", "0.750000", "0.731788", "7 of 8", "retain transparent forecast",
    )
    require(all(term in appendix for term in appendix_terms), "Technical appendix carries all material accepted facts")

    _, index = read_csv(root / "evidence-index.csv")
    require(len(index) == 20 and [row["claim_id"] for row in index] == [f"E{number:02d}" for number in range(1, 21)], "Evidence index has 20 ordered material claims")
    for row in index:
        require((root / row["evidence_path"]).is_file(), f"Evidence index path exists: {row['claim_id']}")
        require(all(row[field] for field in ("material_claim", "owner", "decision_use", "limit")), f"Evidence index row is complete: {row['claim_id']}")

    accessibility = (root / "accessibility-review.md").read_text(encoding="utf-8")
    require(accessibility.count("`pass`") >= 11 and "pending before alpha" in accessibility and "same exact facts" in accessibility, "Accessibility review preserves equivalent routes and human review")
    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    reproduction_terms = (
        "153", "226", "389", "416", "byte-identical", "both pass", "overwrite refused", "copied validator",
        "changed evidence", "changed release identity", "invalid score", "failed gate", "forced scenario selection",
        "hidden failed evidence", "unavailable-as-zero", "changed forecast", "accepted-challenger", "moved threshold",
        "unauthorized test", "missing owner", "missing disagreement", "incomplete defense", "hidden agent use",
        "inaccessible communication", "invalid progression", "pending before alpha",
    )
    require(all(term in reproduction for term in reproduction_terms), "Reproducibility record covers package and failure routes")
    claims = (root / "responsible-claims-audit.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\| [^|]+ \| pass \|", claims)) == 17 and "all prohibited" in claims, "Responsible claims audit covers 17 claim risks")

    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = (
        "Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected",
        "Output used modified or rejected", "Material claim", "Independent verification", "Correction or retained action",
        "Human owner", "Accountability statement",
    )
    require(all(markdown_field(ai, field) for field in ai_fields), "Responsible agent-use record has every accountable field")

    _, score = read_csv(root / "component-score.csv")
    criteria = [row for row in score if row["criterion_id"] != "TOTAL"]
    total = next(row for row in score if row["criterion_id"] == "TOTAL")
    require(len(criteria) == 5 and {row["criterion_id"]: Decimal(row["points_available"]) for row in criteria} == SCORE_MAXIMUMS, "Component score criteria and maximums match")
    require(sum(Decimal(row["points_awarded"]) for row in criteria) == Decimal("35.00") and total["points_awarded"] == "35.00", "Reference component score totals 35 once")
    require(all(Decimal(row["points_awarded"]) <= Decimal(row["points_available"]) for row in criteria), "No score exceeds its maximum")

    _, gates = read_csv(root / "gate-results.csv")
    require(len(gates) == 26 and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 27)] and all(row["status"] == "pass" for row in gates), "All 26 noncompensable gates pass")
    _, conditions = read_csv(root / "conditions-register.csv")
    require(len(conditions) == 12 and [row["condition_id"] for row in conditions] == [f"C{number:02d}" for number in range(1, 13)], "Conditions register has 12 ordered conditions")
    require(all(row["owner"] and row["due_point"] and row["verification"] and row["effect_if_open"] and row["status"] == "open" for row in conditions), "Every condition has ownership verification effect and open status")

    defense = (root / "technical-defense.md").read_text(encoding="utf-8")
    require(re.findall(r"(?m)^## Q(\d{2})\.", defense) == [f"{number:02d}" for number in range(1, 15)], "Technical defense has 14 ordered questions")
    require(
        len(re.findall(r"(?m)^Answer:", defense)) == 14
        and len(re.findall(r"(?m)^Evidence:", defense)) == 14
        and len(re.findall(r"(?m)^Practical consequence:", defense)) == 14
        and len(re.findall(r"(?m)^Limit:", defense)) == 14,
        "Every defense answer has evidence consequence and limit",
    )
    reviewer = (root / "reviewer-record.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\| (?!---|Review role)[^|]+ \|", reviewer)) >= 8 and "does not claim that the pending human reviews occurred" in reviewer, "Reviewer record separates construction from pending human review")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    progression_exact = {
        "Draft component score": "35.00 of 35.00", "Score destination": "Checkpoint 03 exactly once",
        "Required gates": "26 of 26 pass", "Failed gates": "none", "Defense": "adequate for curriculum construction",
        "Package status": "accept with conditions", "Clinical performance recommendation": "revise before testing",
        "Selected scenario": "none", "Scenario dispositions": "S00 retain, S01 revise, S02 stop, S03 revise",
        "Accepted forecast": "seasonal exponential smoothing", "ML decision": "retain transparent forecast",
        "Final checkpoint permission": "permitted for curriculum construction", "Open conditions": "C01 through C12",
    }
    require(all(markdown_field(progression, field) == value for field, value in progression_exact.items()), "Progression carries exact score decisions conditions and permission")
    prohibited_fields = ("Clinical action", "Staffing change", "Schedule change", "Automated action", "Test start", "Implementation", "Production scoring", "Model deployment")
    require(all(markdown_field(progression, field) == "prohibited" for field in prohibited_fields), "Progression preserves every action boundary")

    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 416}
    print(f"APP-3 Module 07 reference validation passed: {len(checks)} checks.")
    return report


def load_assembler():
    spec = importlib.util.spec_from_file_location("app3_module07_assembler", MODULE_ROOT / "assemble_candidate.py")
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load Module 07 assembler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def self_check() -> None:
    assembler = load_assembler()

    def replace(path: Path, old: str, new: str) -> None:
        text = path.read_text(encoding="utf-8")
        if old not in text:
            raise AssertionError(f"Mutation source not found in {path.name}: {old}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")

    def append(path: Path) -> None:
        with path.open("ab") as handle:
            handle.write(b"\nmutation")

    with tempfile.TemporaryDirectory(prefix="app3-module07-validator-") as temp_dir:
        base = Path(temp_dir)
        checkpoint1, checkpoint2 = base / "checkpoint1", base / "checkpoint2"
        assembler.build_reference_checkpoint(checkpoint1, assembler.CHECKPOINTS[0])
        assembler.build_reference_checkpoint(checkpoint2, assembler.CHECKPOINTS[1])
        reference, second, learner = base / "reference", base / "reference-2", base / "learner"
        one = assembler.assemble(checkpoint1, checkpoint2, reference, reference=True)
        two = assembler.assemble(checkpoint1, checkpoint2, second, reference=True)
        assembler.assemble(checkpoint1, checkpoint2, learner)
        assert one == two
        complete = validate(reference)
        starter_result = validate(learner, starter=True)
        copied = subprocess.run([sys.executable, "validate_candidate.py", "."], cwd=reference, capture_output=True, text=True, check=False)
        assert copied.returncode == 0, copied.stdout + copied.stderr

        routes: list[tuple[str, Callable[[Path], None]]] = [
            ("changed-evidence", lambda root: append(root / "evidence/checkpoint1/candidate/module-03/outputs/signal-audit.csv")),
            ("changed-release", lambda root: append(root / "evidence/provenance/checkpoint2-release.json")),
            ("invalid-score", lambda root: replace(root / "component-score.csv", "35.00,35.00", "35.00,34.00")),
            ("failed-gate", lambda root: replace(root / "gate-results.csv", ",pass,progression-decision.md,module owner", ",fail,progression-decision.md,module owner")),
            ("forced-selection", lambda root: replace(root / "recommendation-and-alternatives.md", "Selected scenario: `none`", "Selected scenario: `S01`")),
            ("hidden-failure", lambda root: replace(root / "evidence-synthesis.md", "Six comparisons are null or failed", "All comparisons pass")),
            ("unavailable-as-zero", lambda root: replace(root / "monitoring-measures.csv", ",unavailable,events per 1000", ",0.000000,events per 1000")),
            ("changed-forecast", lambda root: replace(root / "progression-decision.md", "seasonal exponential smoothing", "gradient boosted")),
            ("accepted-challenger", lambda root: replace(root / "progression-decision.md", "retain transparent forecast", "accept challenger")),
            ("moved-threshold", lambda root: replace(root / "technical-appendix.md", "0.750000", "0.700000")),
            ("unauthorized-test", lambda root: replace(root / "progression-decision.md", "- Test start: `prohibited`", "- Test start: `authorized`")),
            ("missing-owner", lambda root: replace(root / "stakeholder-roles.csv", "S01,accountable", "S01,consulted")),
            ("missing-disagreement", lambda root: replace(root / "disagreement-record.md", "- Owner:", "- Steward:")),
            ("incomplete-defense", lambda root: replace(root / "technical-defense.md", "Practical consequence: The package may proceed", "Consequence: The package may proceed")),
            ("hidden-agent-use", lambda root: replace(root / "ai-use.md", "- Human owner:", "- Owner:")),
            ("inaccessible-communication", lambda root: replace(root / "accessibility-review.md", "Frontline brief uses plain language: `pass`", "Frontline brief uses plain language: `fail`")),
            ("invalid-progression", lambda root: replace(root / "progression-decision.md", "permitted for curriculum construction", "not permitted")),
            ("false-package-status", lambda root: replace(root / "progression-decision.md", "accept with conditions", "authorized for implementation")),
            ("clinician-current-title", lambda root: append(root / "clinician-profile.md")),
            ("placeholder-reference", lambda root: replace(root / "reviewer-record.md", "named sign-off pending", "REPLACE")),
        ]
        for name, mutate in routes:
            target = base / f"mutation-{name}"
            shutil.copytree(reference, target)
            mutate(target)
            try:
                validate(target)
            except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError):
                pass
            else:
                raise AssertionError(f"Validator accepted {name} mutation")
        try:
            validate(learner)
        except ValidationError as error:
            assert "Leadership record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted learner prompts as complete")

    print(
        f"APP-3 Module 07 validator self-check passed: {complete['checks_passed']} reference checks and "
        f"{starter_result['checks_passed']} starter checks; copied validation and {len(routes)} failure routes verified."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.candidate:
            validate(args.candidate, starter=args.starter)
        else:
            parser.error("candidate is required unless --self-check is used")
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ImportError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
