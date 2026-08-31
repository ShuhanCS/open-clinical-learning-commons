"""Validate the APP-4 cumulative Week 6 checkpoint."""

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


CHECKPOINT_ROOT = Path(__file__).resolve().parent
WORK_FILES = (
    "README.md", "evidence-index.csv", "checkpoint-score.csv", "checkpoint-gates.csv",
    "responsible-claims-check.md", "reproducibility-check.md", "ai-use.md",
    "checkpoint-defense.md", "module07-handoff.md",
)
CONTROL_FILES = (
    ".gitattributes", "VERSION", "checkpoint-contract.json", "assessment.md",
    "instructor-notes.md", "build_checkpoint.py", "validate_checkpoint.py",
)
MODULES = {
    "module-04": {
        "id": "oclc-app4-04", "version": "0.1.0", "commons": "0.81.0", "files": 302,
        "manifest_rows": 285, "manifest_bytes": 60302,
        "manifest_sha256": "41692b01fa2c339068fcdbf5fbc6f3e301a79ba4535d9ecb94d602cb2e4b3bf9",
        "points": "25", "gates": 20,
    },
    "module-05": {
        "id": "oclc-app4-05", "version": "0.1.0", "commons": "0.82.0", "files": 341,
        "manifest_rows": 324, "manifest_bytes": 75019,
        "manifest_sha256": "6bc3e7c0040b8ae93d273d1464459ae8d500913e0e8a423ca1e5b120256c8baf",
        "points": "0", "gates": 20,
    },
    "module-06": {
        "id": "oclc-app4-06", "version": "0.1.0", "commons": "0.83.0", "files": 387,
        "manifest_rows": 369, "manifest_bytes": 88971,
        "manifest_sha256": "e6553079256fdd2a37ab042a87c2ec69812cad7074abefa7d7907e6ee7b56f7d",
        "points": "0", "gates": 22,
    },
}
EXPECTED_CANDIDATE_MANIFEST_BYTES = 236732
EXPECTED_CANDIDATE_MANIFEST_SHA256 = "14ac12dd890045dce21cdc44a9b614770b8b2428bd71a1d4f5eb9cc9de63d642"
PLACEHOLDER = re.compile(r"\b(?:REPLACE|TODO|TBD|INCOMPLETE)\b|(?:^|,)incomplete(?:,|$)", re.MULTILINE)


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


def validate(workspace: Path, complete: bool = False) -> dict[str, object]:
    workspace = workspace.resolve()
    checks = Checks()
    required = CONTROL_FILES + WORK_FILES + ("candidate-manifest.csv",)
    for relative in required:
        checks.require((workspace / relative).is_file(), f"Missing checkpoint file: {relative}")

    files = [path for path in workspace.rglob("*") if path.is_file() and "__pycache__" not in path.parts]
    checks.require(len(files) == 1047, "Expected exactly 1,047 assembled files")
    checks.require(text(workspace / "VERSION").strip() == "0.1.0", "Checkpoint version changed")
    contract = json.loads(text(workspace / "checkpoint-contract.json"))
    checks.require(contract["checkpoint_id"] == "oclc-app4-cp02", "Checkpoint ID changed")
    checks.require(contract["commons_release"] == "0.84.0", "Commons release changed")
    checks.require(contract["course_points"] == 25 and contract["accepted_component_files"] == 1030, "Checkpoint point or file contract changed")
    checks.require(contract["accepted_decisions"]["accepted_threshold"] is None, "Contract accepted a threshold")
    checks.require(contract["accepted_decisions"]["ml"] == "retain transparent model", "Contract changed the ML decision")
    checks.require(all(value == "prohibited" for value in contract["authority"].values()), "Contract expanded authority")

    manifest_path = workspace / "candidate-manifest.csv"
    manifest = rows(manifest_path)
    checks.require(len(manifest) == 1030, "Expected 1,030 candidate manifest rows")
    checks.require(manifest == sorted(manifest, key=lambda row: row["relative_path"]), "Candidate manifest is not sorted")
    if EXPECTED_CANDIDATE_MANIFEST_BYTES:
        checks.require(manifest_path.stat().st_size == EXPECTED_CANDIDATE_MANIFEST_BYTES, "Candidate manifest bytes changed")
        checks.require(sha256(manifest_path) == EXPECTED_CANDIDATE_MANIFEST_SHA256, "Candidate manifest hash changed")

    seen: set[str] = set()
    module_counts = {directory: 0 for directory in MODULES}
    for row in manifest:
        relative = row["relative_path"]
        pure = PurePosixPath(relative)
        checks.require(not pure.is_absolute() and ".." not in pure.parts and "\\" not in relative, f"Unsafe candidate path: {relative}")
        checks.require(relative not in seen, f"Duplicate candidate path: {relative}")
        seen.add(relative)
        checks.require(len(pure.parts) >= 3 and pure.parts[0] == "candidate" and pure.parts[1] in MODULES, f"Unexpected candidate route: {relative}")
        directory = pure.parts[1]
        expected = MODULES[directory]
        path = workspace / Path(*pure.parts)
        checks.require(path.is_file(), f"Missing candidate file: {relative}")
        checks.require(row["bytes"] == str(path.stat().st_size), f"Candidate bytes changed: {relative}")
        checks.require(row["sha256"] == sha256(path), f"Candidate hash changed: {relative}")
        checks.require(row["source_module"] == expected["id"] and row["source_version"] == expected["version"], f"Candidate source identity changed: {relative}")
        checks.require(row["role"] == "accepted reference workspace artifact", f"Candidate role changed: {relative}")
        module_counts[directory] += 1

    for directory, expected in MODULES.items():
        root = workspace / "candidate" / directory
        checks.require(module_counts[directory] == expected["files"], f"{directory} file count changed")
        release_manifest = root / "release-manifest.csv"
        checks.require(len(rows(release_manifest)) == expected["manifest_rows"], f"{directory} nested manifest rows changed")
        checks.require(release_manifest.stat().st_size == expected["manifest_bytes"], f"{directory} nested manifest bytes changed")
        checks.require(sha256(release_manifest) == expected["manifest_sha256"], f"{directory} nested manifest hash changed")
        release = json.loads(text(root / "release.json"))
        checks.require(release["module"]["id"] == expected["id"] and release["module"]["version"] == expected["version"], f"{directory} release identity changed")
        checks.require(release["module"]["commons_release"] == expected["commons"], f"{directory} Commons release changed")
        gate_rows = rows(root / "gate-results.csv")
        checks.require(len(gate_rows) == expected["gates"] and all(row["status"] == "pass" for row in gate_rows), f"{directory} inherited gates changed")

    record_text = {relative: text(workspace / relative) for relative in WORK_FILES}
    for relative, value in record_text.items():
        checks.require(value.isascii(), f"Checkpoint record must use portable ASCII: {relative}")
        if complete:
            checks.require(not PLACEHOLDER.search(value), f"Reference record is incomplete: {relative}")
        else:
            checks.require(bool(PLACEHOLDER.search(value)), f"Learner record lacks a visible placeholder: {relative}")

    if complete:
        evidence = rows(workspace / "evidence-index.csv")
        checks.require([row["module_id"] for row in evidence] == ["oclc-app4-04", "oclc-app4-05", "oclc-app4-06"], "Evidence index module order changed")
        checks.require([row["checkpoint_points"] for row in evidence] == ["25", "0", "0"], "Evidence index point map changed")
        checks.require([row["gates"] for row in evidence] == ["20", "20", "22"], "Evidence index gate map changed")
        checks.require([row["assembled_files"] for row in evidence] == ["302", "341", "387"], "Evidence index file map changed")

        score = rows(workspace / "checkpoint-score.csv")
        criteria = [row for row in score if row["record_type"] == "criterion"]
        checks.require([row["source_id"] for row in criteria] == [f"M04-S{index:02d}" for index in range(1, 11)], "Module 04 score criteria changed")
        checks.require(sum(Decimal(row["earned_points"]) for row in criteria) == Decimal("25.00"), "Module 04 score does not total 25.00 once")
        summaries = [row for row in score if row["record_type"] == "summary"]
        checks.require(len(summaries) == 1, "Checkpoint must have one score summary")
        checks.require(summaries[0]["possible_points"] == "25.00" and summaries[0]["earned_points"] == "25.00", "Checkpoint score summary changed")
        checks.require(all(row["status"] == "pass" for row in score), "Checkpoint score contains a failed row")
        checks.require(all(row["earned_points"] == "0.00" for row in score if row["record_type"] == "gate"), "A zero-point module received points")

        gates = rows(workspace / "checkpoint-gates.csv")
        checks.require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 21)], "Checkpoint gates are incomplete or unordered")
        checks.require(all(row["status"] == "pass" and row["owner"] for row in gates), "Checkpoint gate failed or lacks an owner")

        claims = record_text["responsible-claims-check.md"]
        for phrase in (
            "panel-t003", "0.03000000", "accepted threshold is none", "Seventeen inherited sandbox failure modes",
            "silent failure", "malformed-card accessibility fixture remains blocked", "-0.00743486", "-0.01928938",
            "0.10385240", "R03, R04, and R08", "not permission to score patients", "No agent owns a clinical decision",
        ):
            checks.require(phrase in claims, f"Responsible claims record lost: {phrase}")

        reproduction = record_text["reproducibility-check.md"]
        for phrase in ("1,030", MODULES["module-04"]["manifest_sha256"], MODULES["module-05"]["manifest_sha256"], MODULES["module-06"]["manifest_sha256"], "does not rerun, tune, or improve"):
            checks.require(str(phrase) in reproduction, f"Reproduction record lost: {phrase}")

        ai_use = record_text["ai-use.md"]
        for phrase in ("Material use: `yes`", "no protected health information", "Human owner", "no clinical decision"):
            checks.require(phrase in ai_use, f"AI-use record lost: {phrase}")

        defense = record_text["checkpoint-defense.md"]
        checks.require(re.findall(r"^## Q\d{2}\.", defense, re.MULTILINE) == [f"## Q{index:02d}." for index in range(1, 15)], "Defense must contain 14 ordered questions")
        checks.require(defense.count("- Exact answer:") == 14 and defense.count("- Evidence:") == 14, "Defense answers or evidence paths are incomplete")
        checks.require(defense.count("- Decision consequence:") == 14 and defense.count("- Limit:") == 14, "Defense consequences or limits are incomplete")

        handoff = record_text["module07-handoff.md"]
        for phrase in (
            "- Progression: `continue with conditions`.", "25.00 of 25.00, counted once", "62 of 62 inherited gates", "R03, R04, and R08 fail",
            "Joe Joseph, MD", "may not change an upstream byte", "silent-mode evaluation", "production", "deploy",
        ):
            checks.require(phrase in handoff, f"Module 07 handoff lost: {phrase}")

    return {
        "status": "pass",
        "mode": "reference" if complete else "learner",
        "checks": checks.count,
        "candidate_manifest_rows": len(manifest),
        "candidate_manifest_bytes": manifest_path.stat().st_size,
        "candidate_manifest_sha256": sha256(manifest_path),
        "assembled_files": len(files),
        "week6_points": 25 if complete else 0,
        "inherited_gates": 62 if complete else 0,
        "checkpoint_gates": 20 if complete else 0,
    }


def mutate_and_reject(root: Path, relative: str, old: str, new: str) -> None:
    path = root / relative
    original = path.read_text(encoding="utf-8")
    if old not in original:
        raise AssertionError(f"Mutation fixture missing in {relative}: {old}")
    path.write_text(original.replace(old, new, 1), encoding="utf-8", newline="")
    try:
        validate(root, complete=True)
    except (ValueError, OSError, json.JSONDecodeError):
        pass
    else:
        raise AssertionError(f"Validator accepted deliberate failure: {relative} {old}")
    finally:
        path.write_text(original, encoding="utf-8", newline="")


def self_check() -> None:
    import build_checkpoint

    with tempfile.TemporaryDirectory(prefix="app4-cp02-validation-") as temp_dir:
        base = Path(temp_dir)
        reference, learner, copied = base / "reference", base / "learner", base / "copied"
        build_checkpoint.assemble(reference, reference=True)
        reference_report = validate(reference, complete=True)

        shutil.copytree(reference, copied)
        completed = subprocess.run(
            [sys.executable, str(copied / "validate_checkpoint.py"), "--workspace", str(copied), "--complete"],
            capture_output=True, text=True, check=False,
        )
        if completed.returncode != 0:
            raise AssertionError(f"Copied validation failed: {completed.stderr}")
        shutil.rmtree(copied)

        failures = (
            ("candidate/module-06/model-comparison.md", "retain transparent model", "accept challenger"),
            ("candidate-manifest.csv", "accepted reference workspace artifact", "changed artifact"),
            ("checkpoint-contract.json", '"course_points": 25', '"course_points": 50'),
            ("checkpoint-contract.json", '"accepted_threshold": null', '"accepted_threshold": 0.03'),
            ("checkpoint-contract.json", '"deployment": "prohibited"', '"deployment": "permitted"'),
            ("evidence-index.csv", ",25,20,continue", ",50,20,continue"),
            ("evidence-index.csv", ",0,20,continue", ",5,20,continue"),
            ("checkpoint-score.csv", "25.00,25.00,summary only", "50.00,50.00,summary only"),
            ("checkpoint-score.csv", "0.00,0.00,required zero-point gate", "5.00,5.00,required zero-point gate"),
            ("checkpoint-gates.csv", "G01,All three", "G01,INCOMPLETE all three"),
            ("checkpoint-gates.csv", ",pass,candidate-manifest.csv", ",fail,candidate-manifest.csv"),
            ("responsible-claims-check.md", "accepted threshold is none", "accepted threshold is 0.03000000"),
            ("responsible-claims-check.md", "Seventeen inherited sandbox failure modes", "No inherited sandbox failure modes"),
            ("responsible-claims-check.md", "malformed-card accessibility fixture remains blocked", "malformed-card accessibility fixture is waived"),
            ("responsible-claims-check.md", "R03, R04, and R08", "all rules"),
            ("responsible-claims-check.md", "not permission to score patients", "permission to score patients"),
            ("reproducibility-check.md", "does not rerun, tune, or improve", "reruns and improves"),
            ("ai-use.md", "no protected health information", "protected health information"),
            ("checkpoint-defense.md", "## Q14.", "## Q15."),
            ("module07-handoff.md", "- Progression: `continue with conditions`.", "- Progression: `deploy`."),
            ("module07-handoff.md", "may not change an upstream byte", "may change upstream evidence"),
            ("README.md", "The package freezes", "REPLACE The package freezes"),
        )
        for relative, old, new in failures:
            mutate_and_reject(reference, relative, old, new)

        missing = reference / "candidate/module-05/accessibility-review.csv"
        original = missing.read_bytes()
        missing.unlink()
        try:
            validate(reference, complete=True)
        except (ValueError, OSError):
            pass
        else:
            raise AssertionError("Validator accepted a missing candidate file")
        finally:
            missing.write_bytes(original)

        shutil.rmtree(reference)
        build_checkpoint.assemble(learner)
        learner_report = validate(learner)
        try:
            validate(learner, complete=True)
        except ValueError:
            pass
        else:
            raise AssertionError("Validator accepted the learner starter as complete")

    print(
        "APP-4 Checkpoint 2 validator self-check passed: "
        f"{reference_report['checks']} reference checks, {learner_report['checks']} learner checks, "
        "copied validation, and 24 rejected failure routes."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--complete", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            print(json.dumps(validate(args.workspace, complete=args.complete), indent=2, sort_keys=True))
        else:
            parser.error("--workspace is required unless --self-check is used")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
