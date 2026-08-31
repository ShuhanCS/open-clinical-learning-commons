"""Build an APP-4 Module 05 learner or reference workspace."""

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

from build_sandbox import OUTPUT_FILES, verify as verify_sandbox


MODULE_ROOT = Path(__file__).resolve().parent
MODULE04_ROOT = MODULE_ROOT.parent / "04-alert-burden-human-factors-equity"
CONTROLS = (
    ".gitattributes",
    "VERSION",
    "README.md",
    "assessment.md",
    "build_sandbox.py",
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
    "prototype-architecture.md",
    "request-prefetch-contract.csv",
    "response-card-contract.csv",
    "test-matrix-review.csv",
    "traceability-audit.csv",
    "visible-failure-review.csv",
    "silent-failure-review.md",
    "latency-version-review.csv",
    "accessibility-review.csv",
    "failure-mode-register.csv",
    "prototype-release.md",
    "checkpoint-score-carryforward.csv",
    "gate-results.csv",
    "reproducibility-check.md",
    "ai-use.md",
    "progression-module06-handoff.md",
)
MODULE04_EXPECTED = {
    "status": "pass",
    "mode": "reference",
    "manifest_rows": 285,
    "manifest_bytes": 60302,
    "manifest_sha256": "41692b01fa2c339068fcdbf5fbc6f3e301a79ba4535d9ecb94d602cb2e4b3bf9",
    "checkpoint_files": 263,
    "nested_immutable_rows": 204,
    "editable_records": 16,
    "assembled_files": 302,
}
NESTED_MANIFESTS = {
    "upstream/checkpoint01/candidate/module-01/release-manifest.csv": (
        29,
        "40ff7384d227a38b0f93832731d984098e6e6f3324a958dafc2319d23f282b45",
    ),
    "upstream/checkpoint01/candidate/module-02/release-manifest.csv": (
        73,
        "bf3a30d66944a799a1dcbb3bc971bbcc81a6a3986e3e08cacf26fac41ecb9ded",
    ),
    "upstream/checkpoint01/candidate/module-03/release-manifest.csv": (
        102,
        "e67f20599704f83ec1e695f23f571fb57c558109bde3bcc676a64afc3dcf8e22",
    ),
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


def load_module04_builder():
    module_name = "app4_module04_workspace_builder"
    spec = importlib.util.spec_from_file_location(module_name, MODULE04_ROOT / "build_workspace.py")
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load APP-4 Module 04 workspace builder")
    sys.path.insert(0, str(MODULE04_ROOT))
    try:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


def verify_module04(workspace: Path, report: dict[str, object]) -> None:
    if report != MODULE04_EXPECTED:
        raise ValueError("Module 04 reference workspace identity changed")
    manifest_path = workspace / "release-manifest.csv"
    if (
        len(read_manifest(manifest_path)) != 285
        or manifest_path.stat().st_size != 60302
        or sha256(manifest_path) != MODULE04_EXPECTED["manifest_sha256"]
    ):
        raise ValueError("Module 04 release manifest changed")
    nested_rows = 0
    for relative, (expected_rows, expected_hash) in NESTED_MANIFESTS.items():
        path = workspace / relative
        if len(read_manifest(path)) != expected_rows or sha256(path) != expected_hash:
            raise ValueError(f"Accepted nested manifest changed: {relative}")
        nested_rows += expected_rows
    if nested_rows != 204:
        raise ValueError("Expected 204 nested Week 3 immutable rows")
    release = json.loads((workspace / "release.json").read_text(encoding="utf-8"))
    handoff = (workspace / "progression-module05-handoff.md").read_text(encoding="utf-8")
    if (
        release["module"]["id"] != "oclc-app4-04"
        or release["module"]["version"] != "0.1.0"
        or release["module"]["commons_release"] != "0.81.0"
        or release["reference_decision"]["sandbox_design"] != "panel-t003"
        or release["reference_decision"]["accepted_threshold"] is not None
        or "permitted for nonproduction sandbox construction" not in handoff
    ):
        raise ValueError("Module 04 progression or authority changed")


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = MODULE_ROOT / ("reference" if reference else "template")
    missing = [relative for relative in CONTROLS + GENERATED_FILES if not (MODULE_ROOT / relative).is_file()]
    missing += [relative for relative in RECORD_FILES if not (record_root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    verify_sandbox(MODULE_ROOT)
    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []

    for relative in CONTROLS:
        source = MODULE_ROOT / relative
        copy_file(source, target, relative)
        manifest.append({
            "relative_path": relative,
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "role": "immutable module control",
            "source_release": "oclc-app4-05@0.1.0",
        })
    for relative in GENERATED_FILES:
        source = MODULE_ROOT / relative
        copy_file(source, target, relative)
        manifest.append({
            "relative_path": relative,
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "role": "immutable local synthetic sandbox evidence",
            "source_release": "APP4-M05-LOCAL-SANDBOX-2026-08-31-v1",
        })
    for relative in RECORD_FILES:
        copy_file(record_root / relative, target, relative)

    with tempfile.TemporaryDirectory(prefix="app4-module05-upstream-") as temporary:
        module04_workspace = Path(temporary) / "module04"
        module04_report = load_module04_builder().assemble(module04_workspace, reference=True)
        verify_module04(module04_workspace, module04_report)
        for path in sorted(module04_workspace.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            within = path.relative_to(module04_workspace).as_posix()
            relative = f"upstream/module04/{within}"
            copy_file(path, target, relative)
            destination = target / relative
            manifest.append({
                "relative_path": relative,
                "bytes": destination.stat().st_size,
                "sha256": sha256(destination),
                "role": "immutable accepted Module 04 reference artifact",
                "source_release": "oclc-app4-04-reference@0.1.0",
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
    if len(manifest) != 324 or files != 341:
        raise ValueError(f"Workspace contract changed: {len(manifest)} manifest rows and {files} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "module04_files": MODULE04_EXPECTED["assembled_files"],
        "module04_manifest_rows": MODULE04_EXPECTED["manifest_rows"],
        "nested_immutable_rows": 204,
        "editable_records": len(RECORD_FILES),
        "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module05-workspace-") as temporary:
        base = Path(temporary)
        learner, reference = base / "learner", base / "reference"
        learner_report = assemble(learner)
        reference_report = assemble(reference, reference=True)
        if learner_report["manifest_sha256"] != reference_report["manifest_sha256"]:
            raise AssertionError("Learner and reference immutable manifests differ")
        if (learner / "prototype-release.md").read_bytes() == (reference / "prototype-release.md").read_bytes():
            raise AssertionError("Learner starter unexpectedly matches the reference")
        try:
            assemble(learner)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder overwrote an existing target")
    print(
        "APP-4 Module 05 workspace builder self-check passed: "
        f"{reference_report['manifest_rows']} immutable rows, "
        f"{reference_report['module04_files']} Module 04 files, "
        f"and {reference_report['assembled_files']} assembled files."
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
            parser.error("choose --target or --self-check")
    except (OSError, ValueError, KeyError, AssertionError, ImportError, json.JSONDecodeError) as error:
        parser.exit(1, f"Workspace build failed: {error}\n")


if __name__ == "__main__":
    main()
