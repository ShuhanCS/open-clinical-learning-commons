"""Validate the APP-5 Module 07 clinician leadership candidate."""

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
    "README.md", "population-intervention-brief.md", "evidence-synthesis.md",
    "population-place-claim-boundary.md", "equity-benefit-harm-consequences.md",
    "intervention-readiness.md", "community-accountability-and-access.md",
    "implementation-monitoring-governance.md", "evaluation-proposal.md",
    "stewardship-retirement.md", "stakeholder-roles.csv",
    "recommendation-and-alternatives.md", "disagreement-record.md", "leadership-reflection.md",
    "community-facing-summary.md", "technical-appendix.md", "evidence-index.csv",
    "reproducibility-check.md", "responsible-claims-audit.md", "ai-use.md",
    "component-score.csv", "gate-results.csv", "conditions-register.csv", "technical-defense.md",
    "reviewer-record.md", "progression-decision.md",
)
CHECKPOINTS = {
    "checkpoint1": {
        "id": "oclc-app5-cp01", "version": "0.1.0", "files": 240,
        "manifest_sha256": "b8331c4fbdddf1403560f0e494c057d2d29944d2b9f15f6273d8b2cabe7b9192",
        "release_sha256": "2748c0bf5f6c0fe90bca29899202e8a3e2b0fa303b4fa37248bbd8daca5d5289",
    },
    "checkpoint2": {
        "id": "oclc-app5-cp02", "version": "0.1.0", "files": 1051,
        "manifest_sha256": "6d403bfb0e4bb6f177400ae97a3b1d89cf968c35b24482f64cea6b927f397f83",
        "release_sha256": "b67fa825fa35e86063799091c34c65ccb95c3784f03e3c4c6cfa692f0c584f55",
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
    checks.require(len(files) == 1328, "Expected exactly 1,328 candidate files")
    checks.require(text(candidate / "VERSION").strip() == "0.1.0", "Module version changed")

    contract = json.loads(text(candidate / "leadership-contract.json"))
    checks.require(contract["module"]["id"] == "oclc-app5-07", "Module ID changed")
    checks.require(contract["module"]["commons_release"] == "0.95.0", "Commons release changed")
    checks.require(contract["module"]["hours"] == 16.0 and contract["module"]["course_points"] == 35, "Module hours or points changed")
    checks.require(contract["reference"]["package_status"] == "accept with conditions", "Package status changed")
    checks.require(contract["reference"]["recommendation"] == "recommend seeking approval for bounded structured community review", "Planning recommendation changed")
    checks.require(contract["reference"]["intervention_ready_for_real_use"] is False, "Contract accepted intervention readiness")
    checks.require(contract["reference"]["outcomes_available"] is False, "Contract invented outcomes")
    checks.require(contract["reference"]["ml_decision"] == "reject challenger; preserve transparent community-review comparison", "ML decision changed")
    checks.require(all(value == "prohibited" for value in contract["boundaries"].values()), "Contract expanded authority")

    manifest_path = candidate / "release-manifest.csv"
    manifest = rows(manifest_path)
    checks.require(len(manifest) == 1301, "Expected 1,301 immutable manifest rows")
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
            checks.require(row["source_unit"] == "APP-5 Module 07" and row["source_version"] == "0.1.0", f"Control provenance changed: {relative}")
        elif relative.startswith("evidence/checkpoint1/"):
            counts["checkpoint1"] += 1
            checks.require(row["source_unit"] == "oclc-app5-cp01", f"Checkpoint 01 provenance changed: {relative}")
        elif relative.startswith("evidence/checkpoint2/"):
            counts["checkpoint2"] += 1
            checks.require(row["source_unit"] == "oclc-app5-cp02", f"Checkpoint 02 provenance changed: {relative}")
        elif relative.startswith("evidence/provenance/"):
            counts["provenance"] += 1
        else:
            checks.require(False, f"Unexpected immutable route: {relative}")
    checks.require(counts == {"controls": 8, "checkpoint1": 240, "checkpoint2": 1051, "provenance": 2}, "Immutable source counts changed")

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
        checks.require([row["input_id"] for row in index] == ["oclc-app5-cp01", "oclc-app5-cp02"], "Evidence index order changed")
        checks.require([row["assembled_files"] for row in index] == ["240", "1051"], "Evidence index file counts changed")
        checks.require([row["points"] for row in index] == ["40", "25"], "Earlier point history changed")

        score = rows(candidate / "component-score.csv")
        checks.require([row["criterion_id"] for row in score] == ["E01", "P01", "L01", "G01", "H01", "TOTAL"], "Score criteria changed")
        checks.require(sum(Decimal(row["points_awarded"]) for row in score[:-1]) == Decimal("35.00"), "Module 07 score does not total 35.00")
        checks.require(score[-1]["points_possible"] == "35.00" and score[-1]["points_awarded"] == "35.00", "Score total changed")
        checks.require(all(row["status"] == "complete" for row in score), "Score record is incomplete")

        gates = rows(candidate / "gate-results.csv")
        checks.require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 27)], "Gate IDs changed")
        checks.require(all(row["status"] == "pass" for row in gates), "A noncompensable gate failed")
        conditions = rows(candidate / "conditions-register.csv")
        checks.require([row["condition_id"] for row in conditions] == [f"CP1-C{index:02d}" for index in range(1, 13)] + [f"CP2-C{index:02d}" for index in range(1, 15)], "Conditions are incomplete")
        checks.require(all(row["status"] == "open" and row["owner"] and row["evidence_needed"] for row in conditions), "A condition is falsely closed or unowned")
        stakeholders = rows(candidate / "stakeholder-roles.csv")
        checks.require([row["role_id"] for row in stakeholders] == [f"R{index:02d}" for index in range(1, 19)], "Stakeholder roles are incomplete")
        checks.require(all(row["accountability"] and row["decision_right"] and row["status"] for row in stakeholders), "Stakeholder ownership is incomplete")
        agent = next(row for row in stakeholders if row["role_id"] == "R18")
        checks.require(agent["decision_right"] == "no decision or sign-off right" and agent["consulted"] == "false", "Agent received decision authority")

        required_phrases = {
            "README.md": ("35.00 of 35.00", "accept with conditions", "recommend seeking approval for bounded structured community review", "Intervention ready for real use: `no`"),
            "population-intervention-brief.md": ("fictional voluntary diabetes-prevention access and navigation program", "28 carried tracts", "No person is classified or contacted", "bounded structured community review"),
            "evidence-synthesis.md": ("5,679,768", "1,597 linked modeled estimates", "Outcomes remain unavailable", "clustering challenger remains rejected"),
            "population-place-claim-boundary.md": ("23 geometry-only tracts remain unavailable", "area-level modeled value", "Individual need or eligibility", "prohibited"),
            "equity-benefit-harm-consequences.md": ("four fictional rules", "least unacceptable", "12 high-travel", "one high-burden"),
            "intervention-readiness.md": ("Five staff-not-ready", "Outcomes: `unavailable`", "not ready for real implementation"),
            "community-accountability-and-access.md": ("does not represent observed community statements", "Silence is not agreement", "language and disability access", "No community contact is authorized"),
            "implementation-monitoring-governance.md": ("20 implementation and monitoring measures", "six triggers", "23 incidents", "Automatic actions total zero"),
            "evaluation-proposal.md": ("No intervention effect can be estimated", "APP-6 owns causal identification", "does not submit or approve an evaluation protocol"),
            "stewardship-retirement.md": ("No learner, model, analyst, clinician, or agent", "Retire the proposal", "Silence is not agreement"),
            "recommendation-and-alternatives.md": ("`accept with conditions`", "`recommend seeking approval for bounded structured community review`", "No outreach, allocation, service, or implementation"),
            "disagreement-record.md": ("does not represent observed statements", "D01", "D06", "Silence is not agreement"),
            "community-facing-summary.md": ("No person is being classified or contacted", "outcomes are unavailable", "clustering method was rejected", "not ready for implementation"),
            "technical-appendix.md": ("0.11995481449421869", "0.893633", "Selected tracts span 2 clusters", "Automatic actions | 0"),
            "responsible-claims-audit.md": ("The proposal is ready for real implementation. | rejected", "Joe Joseph reviewed or endorsed this candidate. | rejected"),
            "ai-use.md": ("Material use: `yes`", "no protected or identifiable data", "no evidence ownership", "direct review and participation are not claimed"),
            "progression-decision.md": ("35.00 of 35.00", "26 of 26 pass", "Intervention ready for real use: `no`", "Final checkpoint: `permitted for curriculum construction`", "Deployment: `prohibited`"),
        }
        for relative, phrases in required_phrases.items():
            for phrase in phrases:
                checks.require(phrase in record_text[relative], f"{relative} lost required fact: {phrase}")

        reproduction = record_text["reproducibility-check.md"]
        for phrase in (
            "1,301", "1,328", str(manifest_path.stat().st_size), sha256(manifest_path),
            "Independent human clean reproduction",
        ):
            checks.require(str(phrase) in reproduction, f"Reproduction record lost: {phrase}")

        defense = record_text["technical-defense.md"]
        checks.require(re.findall(r"^## Q\d{2}\.", defense, re.MULTILINE) == [f"## Q{index:02d}." for index in range(1, 17)], "Defense must contain 16 ordered questions")
        checks.require(defense.count("- Exact answer:") == 16 and defense.count("- Evidence:") == 16, "Defense answers or evidence are incomplete")
        checks.require(defense.count("- Decision consequence:") == 16 and defense.count("- Limit:") == 16, "Defense consequences or limits are incomplete")
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
        "recommendation": "recommend seeking approval for bounded structured community review" if complete else "not assessed",
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

    with tempfile.TemporaryDirectory(prefix="app5-module07-validation-") as temp_dir:
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
            ("evidence/checkpoint2/candidate/module-06/cluster-stability-support-review.md", "challenger is rejected as not useful", "challenger is accepted as useful"),
            ("release-manifest.csv", "accepted checkpoint1 package artifact", "changed artifact"),
            ("leadership-contract.json", '"course_points": 35', '"course_points": 70'),
            ("leadership-contract.json", '"intervention_ready_for_real_use": false', '"intervention_ready_for_real_use": true'),
            ("leadership-contract.json", '"deployment": "prohibited"', '"deployment": "permitted"'),
            ("clinician-profile.md", "no claim about Dr. Joseph's current employer or title", "claims a current title"),
            ("population-intervention-brief.md", "No person is classified or contacted", "People are classified and contacted"),
            ("evidence-synthesis.md", "Outcomes remain unavailable", "Outcomes demonstrate benefit"),
            ("population-place-claim-boundary.md", "Individual need or eligibility is prohibited", "Individual need or eligibility is permitted"),
            ("equity-benefit-harm-consequences.md", "12 high-travel", "0 high-travel"),
            ("intervention-readiness.md", "Five staff-not-ready", "Zero staff-not-ready"),
            ("community-accountability-and-access.md", "Silence is not agreement", "Silence is agreement"),
            ("implementation-monitoring-governance.md", "Automatic actions total zero", "Automatic actions are permitted"),
            ("evaluation-proposal.md", "No intervention effect can be estimated", "An intervention effect is established"),
            ("stewardship-retirement.md", "No learner, model, analyst, clinician, or agent", "An agent"),
            ("recommendation-and-alternatives.md", "`recommend seeking approval for bounded structured community review`", "`begin real implementation`"),
            ("disagreement-record.md", "Silence is not agreement", "Silence is agreement"),
            ("community-facing-summary.md", "not ready for implementation", "ready for implementation"),
            ("technical-appendix.md", "0.11995481449421869", "0.91995481449421869"),
            ("evidence-index.csv", ",40,continue", ",80,continue"),
            ("component-score.csv", "35.00,35.00,complete", "70.00,70.00,complete"),
            ("gate-results.csv", "G01,accepted Checkpoint 01 identity,pass", "G01,accepted Checkpoint 01 identity,fail"),
            ("conditions-register.csv", "CP1-C01,", "CP1-X01,"),
            ("technical-defense.md", "## Q16.", "## Q17."),
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
        "APP-5 Module 07 validator self-check passed: "
        f"{reference_report['checks']} reference checks, {learner_report['checks']} learner checks, "
        "copied validation, and 29 rejected failure routes."
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
