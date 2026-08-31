"""Build an APP-4 Module 04 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import shutil
import tempfile
from pathlib import Path

from build_workflow import OUTPUT_FILES, verify as verify_workflow


MODULE_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = MODULE_ROOT.parent.parent
CHECKPOINT_ROOT = COURSE_ROOT / "checkpoints/01-logic-evidence-validation-readiness"
CONTROLS = (
    ".gitattributes",
    "VERSION",
    "README.md",
    "assessment.md",
    "build_workflow.py",
    "build_workspace.py",
    "data-spec.md",
    "decision-contract.json",
    "instructor-notes.md",
    "release.json",
    "source-record.yml",
    "validate_workspace.py",
)
GENERATED_FILES = OUTPUT_FILES
RECORD_FILES = (
    "workflow-task-analysis.md",
    "role-handoff-map.csv",
    "timing-interruption-review.csv",
    "burden-assumption-register.csv",
    "candidate-design-review.md",
    "usability-review.csv",
    "automation-bias-controls.csv",
    "access-equity-privacy-review.csv",
    "patient-communication-hidden-work.md",
    "override-stop-conditions.md",
    "workflow-evidence-release.md",
    "module-score.csv",
    "gate-results.csv",
    "reproducibility-check.md",
    "ai-use.md",
    "progression-module05-handoff.md",
)
CHECKPOINT_EXPECTED = {
    "candidate_manifest_rows": 245,
    "candidate_manifest_bytes": 45897,
    "candidate_manifest_sha256": "4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151",
    "checkpoint_editable_records": 9,
    "assembled_files": 263,
}
NESTED_MANIFESTS = {
    "candidate/module-01/release-manifest.csv": (29, "40ff7384d227a38b0f93832731d984098e6e6f3324a958dafc2319d23f282b45"),
    "candidate/module-02/release-manifest.csv": (73, "bf3a30d66944a799a1dcbb3bc971bbcc81a6a3986e3e08cacf26fac41ecb9ded"),
    "candidate/module-03/release-manifest.csv": (102, "e67f20599704f83ec1e695f23f571fb57c558109bde3bcc676a64afc3dcf8e22"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def copy(source: Path, target: Path, relative: str) -> None:
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def load_checkpoint_builder():
    spec = importlib.util.spec_from_file_location("app4_checkpoint01_builder", CHECKPOINT_ROOT / "build_checkpoint.py")
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load APP-4 Checkpoint 01 builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_manifest_rows(path: Path) -> int:
    with path.open(encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def verify_checkpoint(workspace: Path, report: dict[str, object]) -> None:
    if report != {"status": "pass", "mode": "reference", **CHECKPOINT_EXPECTED}:
        raise ValueError("Checkpoint 01 reference workspace identity changed")
    if sha256(workspace / "candidate-manifest.csv") != CHECKPOINT_EXPECTED["candidate_manifest_sha256"]:
        raise ValueError("Checkpoint 01 candidate manifest changed")
    nested_rows = 0
    for relative, (expected_rows, expected_hash) in NESTED_MANIFESTS.items():
        path = workspace / relative
        if read_manifest_rows(path) != expected_rows or sha256(path) != expected_hash:
            raise ValueError(f"Accepted nested manifest changed: {relative}")
        nested_rows += expected_rows
    if nested_rows != 204:
        raise ValueError("Expected 204 accepted nested immutable rows")
    contract = json.loads((workspace / "checkpoint-contract.json").read_text(encoding="utf-8"))
    if (
        contract["checkpoint_id"] != "oclc-app4-cp01"
        or contract["version"] != "0.1.0"
        or contract["commons_release"] != "0.80.0"
        or contract["thresholds"]["accepted"] is not None
        or contract["progression"]["module04_permission"] != "permitted for curriculum construction"
        or contract["progression"]["module05_permission"] != "prohibited until Module 04 passes"
    ):
        raise ValueError("Checkpoint 01 progression or authority contract changed")


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = MODULE_ROOT / ("reference" if reference else "template")
    missing = [relative for relative in CONTROLS + GENERATED_FILES if not (MODULE_ROOT / relative).is_file()]
    missing += [relative for relative in RECORD_FILES if not (record_root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    verify_workflow(MODULE_ROOT)
    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []

    for relative in CONTROLS:
        copy(MODULE_ROOT / relative, target, relative)
        source = MODULE_ROOT / relative
        manifest.append({
            "relative_path": relative,
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "role": "immutable module control",
            "source_release": "oclc-app4-04@0.1.0",
        })
    for relative in GENERATED_FILES:
        copy(MODULE_ROOT / relative, target, relative)
        source = MODULE_ROOT / relative
        manifest.append({
            "relative_path": relative,
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "role": "immutable synthetic workflow evidence",
            "source_release": "APP4-M04-SYNTHETIC-WORKFLOW-2026-08-31-v1",
        })
    for relative in RECORD_FILES:
        copy(record_root / relative, target, relative)

    with tempfile.TemporaryDirectory(prefix="app4-module04-checkpoint-") as temporary:
        checkpoint_workspace = Path(temporary) / "checkpoint01"
        checkpoint_report = load_checkpoint_builder().assemble(checkpoint_workspace, reference=True)
        verify_checkpoint(checkpoint_workspace, checkpoint_report)
        for path in sorted(checkpoint_workspace.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            within = path.relative_to(checkpoint_workspace).as_posix()
            relative = f"upstream/checkpoint01/{within}"
            copy(path, target, relative)
            destination = target / relative
            manifest.append({
                "relative_path": relative,
                "bytes": destination.stat().st_size,
                "sha256": sha256(destination),
                "role": "immutable accepted Week 3 checkpoint artifact",
                "source_release": "oclc-app4-cp01@0.1.0",
            })

    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "release-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["relative_path", "bytes", "sha256", "role", "source_release"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts)
    if len(manifest) != 285 or files != 302:
        raise ValueError(f"Workspace contract changed: {len(manifest)} manifest rows and {files} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "checkpoint_files": CHECKPOINT_EXPECTED["assembled_files"],
        "nested_immutable_rows": 204,
        "editable_records": len(RECORD_FILES),
        "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module04-workspace-") as temporary:
        base = Path(temporary)
        first, second, learner = base / "reference-1", base / "reference-2", base / "learner"
        one = assemble(first, reference=True)
        two = assemble(second, reference=True)
        starter = assemble(learner)
        if one != two:
            raise AssertionError("Reference workspace builds are not deterministic")
        if one["manifest_sha256"] != starter["manifest_sha256"] or one["assembled_files"] != starter["assembled_files"]:
            raise AssertionError("Learner and reference immutable identities differ")
        if "REPLACE" in (first / "workflow-task-analysis.md").read_text(encoding="utf-8"):
            raise AssertionError("Reference task analysis contains a placeholder")
        if "REPLACE" not in (learner / "workflow-task-analysis.md").read_text(encoding="utf-8"):
            raise AssertionError("Learner task analysis is not a starter record")
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder overwrote an existing target")
    print(
        "APP-4 Module 04 workspace builder self-check passed: "
        f"{one['manifest_rows']} immutable rows, {one['nested_immutable_rows']} nested rows, "
        f"and {one['assembled_files']} assembled files."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.target:
            print(json.dumps(assemble(args.target, reference=args.reference), indent=2, sort_keys=True))
        else:
            parser.error("--target is required unless --self-check is used")
    except (OSError, ValueError, ImportError, KeyError, json.JSONDecodeError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
