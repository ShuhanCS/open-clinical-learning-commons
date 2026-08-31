"""Build an APP-4 Module 06 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

from build_evidence import OUTPUT_FILES, verify as verify_evidence


ROOT = Path(__file__).resolve().parent
MODULE05_ROOT = ROOT.parent / "05-sandbox-prototype-failure-modes"
CONTROL_FILES = (
    ".gitattributes",
    "VERSION",
    "README.md",
    "assessment.md",
    "build_evidence.py",
    "build_workspace.py",
    "data-spec.md",
    "decision-contract.json",
    "environment.yml",
    "instructor-notes.md",
    "ml-contract.json",
    "release.json",
    "requirements.txt",
    "source-record.yml",
    "validate_workspace.py",
)
RECORD_FILES = (
    "safety-case.md",
    "hazard-review.csv",
    "monitoring-plan.csv",
    "silent-failure-monitoring.md",
    "incident-escalation-review.csv",
    "fallback-stop-restart-retirement.csv",
    "governance-accountability.csv",
    "ml-contract-review.md",
    "model-comparison.md",
    "threshold-burden-review.csv",
    "subgroup-drift-review.csv",
    "leakage-interpretability-review.md",
    "checkpoint-score-carryforward.csv",
    "gate-results.csv",
    "reproducibility-check.md",
    "ai-use.md",
    "progression-checkpoint02-handoff.md",
)
MODULE05_EXPECTED = {
    "status": "pass",
    "mode": "reference",
    "manifest_rows": 324,
    "manifest_bytes": 75019,
    "manifest_sha256": "6bc3e7c0040b8ae93d273d1464459ae8d500913e0e8a423ca1e5b120256c8baf",
    "module04_files": 302,
    "module04_manifest_rows": 285,
    "nested_immutable_rows": 204,
    "editable_records": 16,
    "assembled_files": 341,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def copy_file(source: Path, target: Path, relative: str) -> None:
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_module05_builder():
    spec = importlib.util.spec_from_file_location("app4_module05_workspace_builder", MODULE05_ROOT / "build_workspace.py")
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load APP-4 Module 05 workspace builder")
    sys.path.insert(0, str(MODULE05_ROOT))
    try:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


def verify_module05(workspace: Path, report: dict[str, object]) -> None:
    if report != MODULE05_EXPECTED:
        raise ValueError("Module 05 reference workspace identity changed")
    manifest = workspace / "release-manifest.csv"
    if len(read_manifest(manifest)) != 324 or manifest.stat().st_size != 75019 or sha256(manifest) != MODULE05_EXPECTED["manifest_sha256"]:
        raise ValueError("Module 05 release manifest changed")
    release = json.loads((workspace / "release.json").read_text(encoding="utf-8"))
    handoff = (workspace / "progression-module06-handoff.md").read_text(encoding="utf-8")
    gates = read_manifest(workspace / "gate-results.csv")
    if (
        release["module"]["id"] != "oclc-app4-05"
        or release["module"]["commons_release"] != "0.82.0"
        or release["sandbox"]["cases"] != 31
        or release["sandbox"]["silent_failures_detected"] != 1
        or release["design"]["id"] != "panel-t003"
        or release["design"]["accepted_threshold"] is not None
        or len(gates) != 20
        or any(row["status"] != "pass" for row in gates)
        or "continue with conditions" not in handoff
    ):
        raise ValueError("Module 05 decision, failures, gates, or authority changed")


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = ROOT / ("reference" if reference else "template")
    missing = [relative for relative in CONTROL_FILES + OUTPUT_FILES if not (ROOT / relative).is_file()]
    missing += [relative for relative in RECORD_FILES if not (record_root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    verify_evidence(ROOT / "outputs")
    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []

    for relative in CONTROL_FILES:
        copy_file(ROOT / relative, target, relative)
        source = target / relative
        manifest.append({
            "relative_path": relative,
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "role": "immutable Module 06 control",
            "source_release": "oclc-app4-06@0.1.0",
        })
    for relative in OUTPUT_FILES:
        copy_file(ROOT / relative, target, relative)
        source = target / relative
        manifest.append({
            "relative_path": relative,
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "role": "immutable safety, monitoring, and fixed-challenger evidence",
            "source_release": "APP4-M06-SAFETY-ML-2026-08-31-v1",
        })
    for relative in RECORD_FILES:
        copy_file(record_root / relative, target, relative)

    with tempfile.TemporaryDirectory(prefix="app4-module06-upstream-") as temporary:
        module05_workspace = Path(temporary) / "module05"
        report = load_module05_builder().assemble(module05_workspace, reference=True)
        verify_module05(module05_workspace, report)
        for path in sorted(module05_workspace.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            relative = f"upstream/module05/{path.relative_to(module05_workspace).as_posix()}"
            copy_file(path, target, relative)
            destination = target / relative
            manifest.append({
                "relative_path": relative,
                "bytes": destination.stat().st_size,
                "sha256": sha256(destination),
                "role": "immutable accepted Module 05 reference artifact",
                "source_release": "oclc-app4-05-reference@0.1.0",
            })

    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "release-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256", "role", "source_release"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts)
    if len(manifest) != 369 or files != 387:
        raise ValueError(f"Workspace contract changed: {len(manifest)} manifest rows and {files} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "module05_files": MODULE05_EXPECTED["assembled_files"],
        "module05_manifest_rows": MODULE05_EXPECTED["manifest_rows"],
        "nested_immutable_rows": 324,
        "editable_records": len(RECORD_FILES),
        "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module06-workspace-") as temporary:
        base = Path(temporary)
        learner, reference = base / "learner", base / "reference"
        learner_report = assemble(learner)
        reference_report = assemble(reference, reference=True)
        if learner_report["manifest_sha256"] != reference_report["manifest_sha256"]:
            raise AssertionError("Learner and reference immutable manifests differ")
        if (learner / "model-comparison.md").read_bytes() == (reference / "model-comparison.md").read_bytes():
            raise AssertionError("Learner starter unexpectedly matches the reference")
        try:
            assemble(learner)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder overwrote an existing target")
    print(f"APP-4 Module 06 workspace self-check passed: 369 immutable rows and {reference_report['assembled_files']} files.")


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
            parser.error("choose --target or --self-check")
    except (OSError, ValueError, KeyError, AssertionError, ImportError, json.JSONDecodeError) as error:
        parser.exit(1, f"Workspace build failed: {error}\n")


if __name__ == "__main__":
    main()
