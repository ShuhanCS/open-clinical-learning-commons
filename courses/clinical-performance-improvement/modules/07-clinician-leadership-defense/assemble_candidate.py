"""Assemble the APP-3 Module 07 clinical leadership candidate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = MODULE_ROOT.parent.parent
CP1_ROOT = COURSE_ROOT / "checkpoints/01-measures-variation-readiness"
CP2_ROOT = COURSE_ROOT / "checkpoints/02-forecast-scenario-monitoring-release"
REFERENCE_ROOT = MODULE_ROOT / "reference"
TEMPLATE_ROOT = MODULE_ROOT / "template"
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
CHECKPOINTS = (
    {
        "id": "oclc-app3-cp01", "version": "0.1.0", "directory": "checkpoint1", "root": CP1_ROOT,
        "files": 153, "manifest": "candidate-manifest.csv",
        "manifest_sha256": "9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656",
        "release_sha256": "270b4e49d1c21d8faf7243cd11cef1dddea836d32be551dfe72edac771b31f27",
    },
    {
        "id": "oclc-app3-cp02", "version": "0.1.0", "directory": "checkpoint2", "root": CP2_ROOT,
        "files": 226, "manifest": "candidate-manifest.csv",
        "manifest_sha256": "4f2a303bc5626ea58139aa935da157f524db1d25b5a158a927ef5daec197958a",
        "release_sha256": "b8af80b7e07c2eac2aeb0e9206533bfae134f55d69a5df9038a7a9a915c4dd05",
    },
)
MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_files(root: Path, names: tuple[str, ...], label: str) -> None:
    missing = [name for name in names if not (root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"{label} is missing: {', '.join(missing)}")


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Path is not portable: {value}")
    return path


def run(command: list[str], label: str) -> None:
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError(f"{label} failed: {result.stderr.strip() or result.stdout.strip()}")


def validate_checkpoint(checkpoint: Path, contract: dict[str, object]) -> None:
    root = Path(contract["root"])
    run([sys.executable, str(root / "validate_checkpoint.py"), str(checkpoint)], str(contract["id"]))
    if sum(path.is_file() for path in checkpoint.rglob("*") if "__pycache__" not in path.parts) != contract["files"]:
        raise ValueError(f"{contract['id']} file count changed")
    if sha256(checkpoint / str(contract["manifest"])) != contract["manifest_sha256"]:
        raise ValueError(f"{contract['id']} candidate manifest changed")
    identity = json.loads((checkpoint / "checkpoint-contract.json").read_text(encoding="utf-8"))
    version = (checkpoint / "VERSION").read_text(encoding="utf-8").strip()
    if identity["checkpoint_id"] != contract["id"] or version != contract["version"]:
        raise ValueError(f"{contract['id']} identity changed")


def build_reference_checkpoint(target: Path, contract: dict[str, object]) -> None:
    builder = Path(contract["root"]) / "build_checkpoint.py"
    run([sys.executable, str(builder), "--target", str(target), "--reference"], f"Build {contract['id']}")


def copy_registered(source: Path, target: Path, relative: str, source_unit: str, version: str, role: str, manifest: list[dict[str, object]]) -> None:
    destination = target / safe_relative(relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    manifest.append({
        "relative_path": relative.replace("\\", "/"),
        "source_unit": source_unit,
        "source_version": version,
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "role": role,
    })


def assemble(checkpoint1: Path, checkpoint2: Path, target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    checkpoints = (checkpoint1.resolve(), checkpoint2.resolve())
    require_files(MODULE_ROOT, CONTROL_FILES, "Module controls")
    record_root = REFERENCE_ROOT if reference else TEMPLATE_ROOT
    require_files(record_root, RECORD_FILES, "Leadership records")
    for checkpoint, contract in zip(checkpoints, CHECKPOINTS, strict=True):
        validate_checkpoint(checkpoint, contract)
        release = Path(contract["root"]) / "release.json"
        if not release.is_file() or sha256(release) != contract["release_sha256"]:
            raise ValueError(f"{contract['id']} release identity changed")

    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for name in CONTROL_FILES:
        copy_registered(MODULE_ROOT / name, target, name, "APP-3 Module 07", "0.1.0", "immutable leadership control", manifest)
    for name in RECORD_FILES:
        destination = target / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(record_root / name, destination)
    for checkpoint, contract in zip(checkpoints, CHECKPOINTS, strict=True):
        directory = str(contract["directory"])
        for source in sorted(path for path in checkpoint.rglob("*") if path.is_file() and "__pycache__" not in path.parts):
            within = source.relative_to(checkpoint).as_posix()
            copy_registered(source, target, f"evidence/{directory}/{within}", str(contract["id"]), str(contract["version"]), f"accepted {directory} package artifact", manifest)
        release = Path(contract["root"]) / "release.json"
        copy_registered(release, target, f"evidence/provenance/{directory}-release.json", str(contract["id"]), str(contract["version"]), "accepted checkpoint release record", manifest)

    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "release-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts)
    if len(manifest) != 389 or files != 416:
        raise ValueError(f"Candidate contract changed: {len(manifest)} manifest rows and {files} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app3-module07-assemble-") as temp_dir:
        base = Path(temp_dir)
        checkpoint1, checkpoint2 = base / "checkpoint1", base / "checkpoint2"
        build_reference_checkpoint(checkpoint1, CHECKPOINTS[0])
        build_reference_checkpoint(checkpoint2, CHECKPOINTS[1])
        first, second, learner = base / "reference-1", base / "reference-2", base / "learner"
        one = assemble(checkpoint1, checkpoint2, first, reference=True)
        two = assemble(checkpoint1, checkpoint2, second, reference=True)
        starter = assemble(checkpoint1, checkpoint2, learner)
        assert one == two
        assert one["manifest_rows"] == 389 and one["assembled_files"] == 416
        assert starter["manifest_sha256"] == one["manifest_sha256"]
        assert "REPLACE" not in (first / "recommendation-and-alternatives.md").read_text(encoding="utf-8")
        assert "REPLACE" in (learner / "recommendation-and-alternatives.md").read_text(encoding="utf-8")
        try:
            assemble(checkpoint1, checkpoint2, first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler overwrote an existing target")
    print("APP-3 Module 07 assembler self-check passed: 389 immutable rows and 416 candidate files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--checkpoint1", type=Path)
    parser.add_argument("--checkpoint2", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.target:
        parser.error("--target is required")
    try:
        if args.reference:
            if args.checkpoint1 or args.checkpoint2:
                parser.error("--reference cannot be combined with checkpoint paths")
            with tempfile.TemporaryDirectory(prefix="app3-module07-reference-") as temp_dir:
                base = Path(temp_dir)
                checkpoint1, checkpoint2 = base / "checkpoint1", base / "checkpoint2"
                build_reference_checkpoint(checkpoint1, CHECKPOINTS[0])
                build_reference_checkpoint(checkpoint2, CHECKPOINTS[1])
                report = assemble(checkpoint1, checkpoint2, args.target, reference=True)
        else:
            if not args.checkpoint1 or not args.checkpoint2:
                parser.error("--checkpoint1 and --checkpoint2 are required outside reference mode")
            report = assemble(args.checkpoint1, args.checkpoint2, args.target)
    except (OSError, ValueError, ImportError) as error:
        parser.exit(1, f"Assembly failed: {error}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
