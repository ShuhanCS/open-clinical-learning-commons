"""Validate the APP-4 Module 07 clinician leadership candidate."""

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
from pathlib import Path, PurePosixPath


MODULE_ROOT = Path(__file__).resolve().parent
CONTROL_FILES = (
    ".gitattributes", "VERSION", "leadership-contract.json", "clinician-profile.md",
    "clinician-session-plan.md", "assessment.md", "assemble_candidate.py", "validate_candidate.py",
)
RECORD_FILES = (
    "README.md", "product-brief.md", "evidence-synthesis.md", "logic-input-threshold.md",
    "workflow-patient-consequences.md", "prototype-disclosure.md", "safety-case.md",
    "monitoring-silent-failure-plan.md", "evaluation-proposal.md",
    "stewardship-governance-retirement.md", "stakeholder-roles.csv",
    "recommendation-and-alternatives.md", "disagreement-record.md", "leadership-reflection.md",
    "accessible-communication.md", "technical-appendix.md", "evidence-index.csv",
    "reproducibility-check.md", "responsible-claims-audit.md", "ai-use.md",
    "component-score.csv", "gate-results.csv", "conditions-register.csv", "technical-defense.md",
    "reviewer-record.md", "progression-decision.md",
)
CHECKPOINTS = {
    "checkpoint1": {
        "id": "oclc-app4-cp01", "version": "0.1.0", "files": 263,
        "manifest_sha256": "4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151",
        "release_sha256": "8f637bef551ebe5cb91e93b3b91fef51f25736d07168b904851405c703b62c03",
    },
    "checkpoint2": {
        "id": "oclc-app4-cp02", "version": "0.1.0", "files": 1047,
        "manifest_sha256": "14ac12dd890045dce21cdc44a9b614770b8b2428bd71a1d4f5eb9cc9de63d642",
        "release_sha256": "05e65b59f0d4c4b33dc341256141e39c02cfffc32e22aca546dbb85384cb1221",
    },
}
PLACEHOLDER = re.compile(r"\b(?:REPLACE|TODO|TBD|INCOMPLETE|PENDING_RELEASE_IDENTITY)\b|(?:^|,)incomplete(?:,|$)", re.MULTILINE)


class Checks:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, message: str) -> None:
        self.count += 1
        if not condition:
            raise ValueError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate(candidate: Path, complete: bool = False) -> dict[str, object]:
    candidate = candidate.resolve()
    checks = Checks()
    for relative in CONTROL_FILES + RECORD_FILES + ("release-manifest.csv",):
        checks.require((candidate / relative).is_file(), f"Missing candidate file: {relative}")
    files = [path for path in candidate.rglob("*") if path.is_file() and "__pycache__" not in path.parts]
    checks.require(len(files) == 1347, "Expected exactly 1,347 candidate files")
    checks.require(text(candidate / "VERSION").strip() == "0.1.0", "Module version changed")

    contract = json.loads(text(candidate / "leadership-contract.json"))
    checks.require(contract["module"]["id"] == "oclc-app4-07", "Module ID changed")
    checks.require(contract["module"]["commons_release"] == "0.85.0", "Commons release changed")
    checks.require(contract["module"]["hours"] == 16.0 and contract["module"]["course_points"] == 35, "Module hours or points changed")
    checks.require(contract["reference"]["package_status"] == "accept with conditions", "Package status changed")
    checks.require(contract["reference"]["recommendation"] == "revise before seeking local silent-mode approval", "CDS recommendation changed")
    checks.require(contract["reference"]["accepted_threshold"] is None, "Contract accepted a threshold")
    checks.require(contract["reference"]["ml_decision"] == "retain transparent model", "ML decision changed")
    checks.require(all(value == "prohibited" for value in contract["boundaries"].values()), "Contract expanded authority")

    manifest_path = candidate / "release-manifest.csv"
    manifest = rows(manifest_path)
    checks.require(len(manifest) == 1320, "Expected 1,320 immutable manifest rows")
    checks.require(manifest == sorted(manifest, key=lambda row: row["relative_path"]), "Release manifest is not sorted")
    counts = {"controls": 0, "checkpoint1": 0, "checkpoint2": 0, "provenance": 0}
    seen: set[str] = set()
    for row in manifest:
        relative = row["relative_path"]
        pure = PurePosixPath(relative)
        checks.require(not pure.is_absolute() and ".." not in pure.parts and "\\" not in relative, f"Unsafe manifest path: {relative}")
        checks.require(relative not in seen, f"Duplicate manifest path: {relative}")
        seen.add(relative)
        path = candidate / Path(*pure.parts)
        checks.require(path.is_file(), f"Missing immutable file: {relative}")
        checks.require(row["bytes"] == str(path.stat().st_size), f"Immutable bytes changed: {relative}")
        checks.require(row["sha256"] == sha256(path), f"Immutable hash changed: {relative}")
        checks.require(bool(row["source_unit"] and row["source_version"] and row["role"]), f"Manifest provenance incomplete: {relative}")
        if relative in CONTROL_FILES:
            counts["controls"] += 1
            checks.require(row["source_unit"] == "APP-4 Module 07" and row["source_version"] == "0.1.0", f"Control provenance changed: {relative}")
        elif relative.startswith("evidence/checkpoint1/"):
            counts["checkpoint1"] += 1
            checks.require(row["source_unit"] == "oclc-app4-cp01", f"Checkpoint 01 provenance changed: {relative}")
        elif relative.startswith("evidence/checkpoint2/"):
            counts["checkpoint2"] += 1
            checks.require(row["source_unit"] == "oclc-app4-cp02", f"Checkpoint 02 provenance changed: {relative}")
        elif relative.startswith("evidence/provenance/"):
            counts["provenance"] += 1
        else:
            checks.require(False, f"Unexpected immutable route: {relative}")
    checks.require(counts == {"controls": 8, "checkpoint1": 263, "checkpoint2": 1047, "provenance": 2}, "Immutable source counts changed")

    for directory, expected in CHECKPOINTS.items():
        root = candidate / "evidence" / directory
        checks.require(sha256(root / "candidate-manifest.csv") == expected["manifest_sha256"], f"{directory} candidate manifest changed")
        identity = json.loads(text(root / "checkpoint-contract.json"))
        checks.require(identity["checkpoint_id"] == expected["id"] and text(root / "VERSION").strip() == expected["version"], f"{directory} identity changed")
        release = candidate / "evidence" / "provenance" / f"{directory}-release.json"
        checks.require(sha256(release) == expected["release_sha256"], f"{directory} release record changed")

    profile = text(candidate / "clinician-profile.md")
    for phrase in (
        "Joe Joseph, MD, SFHM", "Fellow in Hospital Medicine in 2015", "Senior Fellow in Hospital Medicine in 2017",
        "Regional Chief Medical Officer in a 2019 release", "no claim about Dr. Joseph's current employer or title",
        "does not claim that he reviewed, endorsed, or delivered",
    ):
        checks.require(phrase in profile, f"Clinician boundary lost: {phrase}")
    checks.require(text(candidate / "clinician-session-plan.md").count("## Session ") == 4, "Clinician session plan must contain four sessions")

    record_text = {relative: text(candidate / relative) for relative in RECORD_FILES}
    for relative, value in record_text.items():
        checks.require(value.isascii(), f"Leadership record must use portable ASCII: {relative}")
        if complete:
            checks.require(not PLACEHOLDER.search(value), f"Reference record is incomplete: {relative}")
        else:
            checks.require(bool(PLACEHOLDER.search(value)), f"Learner record lacks a visible placeholder: {relative}")

    if complete:
        index = rows(candidate / "evidence-index.csv")
        checks.require([row["input_id"] for row in index] == ["oclc-app4-cp01", "oclc-app4-cp02"], "Evidence index order changed")
        checks.require([row["assembled_files"] for row in index] == ["263", "1047"], "Evidence index file counts changed")
        checks.require([row["points"] for row in index] == ["40", "25"], "Earlier point history changed")

        score = rows(candidate / "component-score.csv")
        checks.require([row["criterion_id"] for row in score] == ["E01", "C01", "L01", "G01", "H01", "TOTAL"], "Score criteria changed")
        checks.require(sum(Decimal(row["points_awarded"]) for row in score[:-1]) == Decimal("35.00"), "Module 07 score does not total 35.00")
        checks.require(score[-1]["points_possible"] == "35.00" and score[-1]["points_awarded"] == "35.00", "Score total changed")
        checks.require(all(row["status"] == "complete" for row in score), "Score record is incomplete")

        gates = rows(candidate / "gate-results.csv")
        checks.require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 27)], "Gate IDs changed")
        checks.require(all(row["status"] == "pass" for row in gates), "A noncompensable gate failed")
        conditions = rows(candidate / "conditions-register.csv")
        checks.require([row["condition_id"] for row in conditions] == [f"C{index:02d}" for index in range(1, 17)], "Conditions are incomplete")
        checks.require(all(row["status"] == "open" and row["owner"] and row["evidence_needed"] for row in conditions), "A condition is falsely closed or unowned")
        stakeholders = rows(candidate / "stakeholder-roles.csv")
        checks.require([row["role_id"] for row in stakeholders] == [f"R{index:02d}" for index in range(1, 18)], "Stakeholder roles are incomplete")
        checks.require(all(row["accountability"] and row["decision_right"] and row["status"] for row in stakeholders), "Stakeholder ownership is incomplete")
        agent = next(row for row in stakeholders if row["role_id"] == "R17")
        checks.require(agent["decision_right"] == "no decision or sign-off right" and agent["consulted"] == "false", "Agent received decision authority")

        required_phrases = {
            "README.md": ("35.00 of 35.00", "accept with conditions", "revise before seeking local silent-mode approval", "Accepted clinical threshold: `none`"),
            "product-brief.md": ("CGH-GIM-01", "panel-t003", "0.03000000", "No clinical threshold is accepted", "blocked malformed-card accessibility defect"),
            "evidence-synthesis.md": ("7,544 rows", "Seventeen failures remain visible", "R03", "R04", "R08", "transparent model remains retained"),
            "logic-input-threshold.md": ("0.020, 0.030, 0.040, 0.050, 0.075, and 0.100", "Accepted clinical threshold: `none`", "Agent threshold selection: prohibited"),
            "workflow-patient-consequences.md": ("hidden follow-up work", "Silence from staff is not agreement", "does not support silent-mode approval"),
            "prototype-disclosure.md": ("Cases: `31`", "Inherited failure modes: `17`", "Silent failures detected: `1`", "Accessibility defects blocked: `1`"),
            "safety-case.md": ("Hazards: `22 of 22 retained`", "Escalation routes: `12 of 12 human owned`", "Automatic clinical actions: `0`"),
            "monitoring-silent-failure-plan.md": ("all 20 accepted measures", "request, response, terminal trace, and human notice", "Automatic actions total zero"),
            "evaluation-proposal.md": ("Do not seek local approval", "accepted threshold is none", "does not submit or approve that protocol"),
            "stewardship-governance-retirement.md": ("No learner, model, analyst, or agent", "Silence is not agreement", "Retire the concept"),
            "recommendation-and-alternatives.md": ("`accept with conditions`", "`revise before seeking local silent-mode approval`", "No clinical use, no real-patient scoring"),
            "disagreement-record.md": ("does not represent observed statements", "D01", "D05", "Silence is not agreement"),
            "accessible-communication.md": ("No patient is being scored", "malformed-card fixture remains blocked", "does not claim that the frozen prototype is accessible"),
            "technical-appendix.md": ("-0.00743486", "-0.01928938", "0.10385240", "Automatic actions | 0"),
            "responsible-claims-audit.md": ("The CDS concept is ready for local silent-mode approval. | rejected", "Joe Joseph reviewed or endorsed this candidate. | rejected"),
            "ai-use.md": ("Material use: `yes`", "no protected health information", "no evidence ownership", "direct review and participation are not claimed"),
            "progression-decision.md": ("35.00 of 35.00", "26 of 26 pass", "Accepted clinical threshold: `none`", "Final checkpoint: `permitted for curriculum construction`", "Deployment: `prohibited`"),
        }
        for relative, phrases in required_phrases.items():
            for phrase in phrases:
                checks.require(phrase in record_text[relative], f"{relative} lost required fact: {phrase}")

        reproduction = record_text["reproducibility-check.md"]
        for phrase in (
            "1,320", "1,347", str(manifest_path.stat().st_size), sha256(manifest_path),
            "Independent human clean reproduction",
        ):
            checks.require(str(phrase) in reproduction, f"Reproduction record lost: {phrase}")

        defense = record_text["technical-defense.md"]
        checks.require(re.findall(r"^## Q\d{2}\.", defense, re.MULTILINE) == [f"## Q{index:02d}." for index in range(1, 15)], "Defense must contain 14 ordered questions")
        checks.require(defense.count("- Exact answer:") == 14 and defense.count("- Evidence:") == 14, "Defense answers or evidence are incomplete")
        checks.require(defense.count("- Decision consequence:") == 14 and defense.count("- Limit:") == 14, "Defense consequences or limits are incomplete")
        reviewer = record_text["reviewer-record.md"]
        checks.require("No named reviewer sign-off is implied" in reviewer and "pending direct confirmation" in reviewer and "may not convert pending review into approval" in reviewer, "Reviewer boundary changed")

    return {
        "status": "pass",
        "mode": "reference" if complete else "learner",
        "checks": checks.count,
        "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "assembled_files": len(files),
        "module07_points": 35 if complete else 0,
        "gates_passed": 26 if complete else 0,
        "recommendation": "revise before seeking local silent-mode approval" if complete else "not assessed",
    }


def mutate_and_reject(root: Path, relative: str, old: str, new: str) -> None:
    path = root / relative
    original = path.read_text(encoding="utf-8")
    if old not in original:
        raise AssertionError(f"Mutation fixture missing in {relative}: {old}")
    path.write_text(original.replace(old, new), encoding="utf-8", newline="")
    try:
        validate(root, complete=True)
    except (ValueError, OSError, json.JSONDecodeError):
        pass
    else:
        raise AssertionError(f"Validator accepted deliberate failure: {relative} {old}")
    finally:
        path.write_text(original, encoding="utf-8", newline="")


def self_check() -> None:
    import assemble_candidate

    with tempfile.TemporaryDirectory(prefix="app4-module07-validation-") as temp_dir:
        base = Path(temp_dir)
        cp1, cp2, reference = base / "checkpoint1", base / "checkpoint2", base / "reference"
        assemble_candidate.build_reference_checkpoint(cp1, assemble_candidate.CHECKPOINTS[0])
        assemble_candidate.build_reference_checkpoint(cp2, assemble_candidate.CHECKPOINTS[1])
        assemble_candidate.assemble(cp1, cp2, reference, reference=True)
        shutil.rmtree(cp1)
        shutil.rmtree(cp2)
        reference_report = validate(reference, complete=True)

        copied = base / "copied"
        shutil.copytree(reference, copied)
        result = subprocess.run(
            [sys.executable, str(copied / "validate_candidate.py"), "--candidate", str(copied), "--complete"],
            capture_output=True, text=True, check=False,
        )
        if result.returncode:
            raise AssertionError(f"Copied validation failed: {result.stderr}")
        shutil.rmtree(copied)

        failures = (
            ("evidence/checkpoint2/candidate/module-06/model-comparison.md", "retain transparent model", "accept challenger"),
            ("release-manifest.csv", "accepted checkpoint1 package artifact", "changed artifact"),
            ("leadership-contract.json", '"course_points": 35', '"course_points": 70'),
            ("leadership-contract.json", '"accepted_threshold": null', '"accepted_threshold": 0.03'),
            ("leadership-contract.json", '"deployment": "prohibited"', '"deployment": "permitted"'),
            ("clinician-profile.md", "no claim about Dr. Joseph's current employer or title", "claims a current title"),
            ("product-brief.md", "No clinical threshold is accepted", "A clinical threshold is accepted"),
            ("evidence-synthesis.md", "Seventeen failures remain visible", "No failures remain visible"),
            ("logic-input-threshold.md", "Accepted clinical threshold: `none`", "Accepted clinical threshold: `0.03000000`"),
            ("workflow-patient-consequences.md", "Silence from staff is not agreement", "Silence from staff is agreement"),
            ("prototype-disclosure.md", "Accessibility defects blocked: `1`", "Accessibility defects blocked: `0`"),
            ("safety-case.md", "Hazards: `22 of 22 retained`", "Hazards: `21 of 22 retained`"),
            ("monitoring-silent-failure-plan.md", "Automatic actions total zero", "Automatic actions permitted"),
            ("evaluation-proposal.md", "Do not seek local approval", "Seek local approval now"),
            ("stewardship-governance-retirement.md", "No learner, model, analyst, or agent", "An agent"),
            ("recommendation-and-alternatives.md", "`revise before seeking local silent-mode approval`", "`recommend seeking local approval for bounded silent-mode evaluation`"),
            ("disagreement-record.md", "Silence is not agreement", "Silence is agreement"),
            ("accessible-communication.md", "malformed-card fixture remains blocked", "malformed-card fixture is waived"),
            ("technical-appendix.md", "-0.00743486", "0.00743486"),
            ("evidence-index.csv", ",40,continue", ",80,continue"),
            ("component-score.csv", "35.00,35.00,complete", "70.00,70.00,complete"),
            ("gate-results.csv", "G01,accepted Checkpoint 01 identity,pass", "G01,accepted Checkpoint 01 identity,fail"),
            ("conditions-register.csv", ",open,direct documented confirmation", ",closed,direct documented confirmation"),
            ("technical-defense.md", "## Q14.", "## Q15."),
            ("reviewer-record.md", "pending direct confirmation", "confirmed and approved"),
            ("progression-decision.md", "Deployment: `prohibited`", "Deployment: `permitted`"),
            ("ai-use.md", "Material use: `yes`", "Material use: `no`"),
            ("README.md", "The candidate preserves", "REPLACE The candidate preserves"),
        )
        for relative, old, new in failures:
            mutate_and_reject(reference, relative, old, new)

        missing = reference / "evidence/checkpoint1/candidate-manifest.csv"
        original = missing.read_bytes()
        missing.unlink()
        try:
            validate(reference, complete=True)
        except (ValueError, OSError):
            pass
        else:
            raise AssertionError("Validator accepted missing immutable evidence")
        finally:
            missing.write_bytes(original)

        learner = base / "learner"
        shutil.copytree(reference, learner)
        for relative in RECORD_FILES:
            shutil.copy2(MODULE_ROOT / "template" / relative, learner / relative)
        learner_report = validate(learner)
        try:
            validate(learner, complete=True)
        except ValueError:
            pass
        else:
            raise AssertionError("Validator accepted the learner starter as complete")

    print(
        "APP-4 Module 07 validator self-check passed: "
        f"{reference_report['checks']} reference checks, {learner_report['checks']} learner checks, "
        "copied validation, and 30 rejected failure routes."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--complete", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.candidate:
            print(json.dumps(validate(args.candidate, complete=args.complete), indent=2, sort_keys=True))
        else:
            parser.error("--candidate is required unless --self-check is used")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
