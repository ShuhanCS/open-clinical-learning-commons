"""Assemble the APP-5 Module 07 clinician leadership candidate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = MODULE_ROOT.parent.parent
REFERENCE_ROOT = MODULE_ROOT / "reference"
TEMPLATE_ROOT = MODULE_ROOT / "template"
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
CHECKPOINTS = (
    {
        "id": "oclc-app5-cp01", "version": "0.1.0", "directory": "checkpoint1",
        "root": COURSE_ROOT / "checkpoints/01-measures-disparities-readiness", "files": 240,
        "manifest_sha256": "b8331c4fbdddf1403560f0e494c057d2d29944d2b9f15f6273d8b2cabe7b9192",
        "release_sha256": "2748c0bf5f6c0fe90bca29899202e8a3e2b0fa303b4fa37248bbd8daca5d5289",
        "validator_args": ("{validator}", "{checkpoint}"),
    },
    {
        "id": "oclc-app5-cp02", "version": "0.1.0", "directory": "checkpoint2",
        "root": COURSE_ROOT / "checkpoints/02-place-targeting-intervention-release", "files": 1051,
        "manifest_sha256": "6d403bfb0e4bb6f177400ae97a3b1d89cf968c35b24482f64cea6b927f397f83",
        "release_sha256": "b67fa825fa35e86063799091c34c65ccb95c3784f03e3c4c6cfa692f0c584f55",
        "validator_args": ("{validator}", "{checkpoint}", "--mode", "complete"),
    },
)
MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run(command: list[str], label: str) -> None:
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError(f"{label} failed: {result.stderr.strip() or result.stdout.strip()}")


def validate_checkpoint(checkpoint: Path, contract: dict[str, object]) -> None:
    validator = Path(contract["root"]) / "validate_checkpoint.py"
    command = [sys.executable] + [
        value.format(validator=str(validator), checkpoint=str(checkpoint))
        for value in contract["validator_args"]
    ]
    run(command, str(contract["id"]))
    files = sum(path.is_file() for path in checkpoint.rglob("*") if "__pycache__" not in path.parts)
    if files != contract["files"]:
        raise ValueError(f"{contract['id']} file count changed")
    manifest = checkpoint / "candidate-manifest.csv"
    if sha256(manifest) != contract["manifest_sha256"]:
        raise ValueError(f"{contract['id']} candidate manifest changed")
    identity = json.loads((checkpoint / "checkpoint-contract.json").read_text(encoding="utf-8"))
    if identity["checkpoint_id"] != contract["id"] or (checkpoint / "VERSION").read_text(encoding="utf-8").strip() != contract["version"]:
        raise ValueError(f"{contract['id']} identity changed")


def build_reference_checkpoint(target: Path, contract: dict[str, object]) -> None:
    builder = Path(contract["root"]) / "build_checkpoint.py"
    run([sys.executable, str(builder), "--target", str(target), "--reference"], f"Build {contract['id']}")


def copy_registered(source: Path, target: Path, relative: str, unit: str, version: str, role: str, manifest: list[dict[str, object]]) -> None:
    portable = Path(relative)
    if portable.is_absolute() or ".." in portable.parts:
        raise ValueError(f"Path is not portable: {relative}")
    destination = target / portable
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    manifest.append({
        "relative_path": relative.replace("\\", "/"),
        "source_unit": unit,
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
    record_root = REFERENCE_ROOT if reference else TEMPLATE_ROOT
    missing = [name for name in CONTROL_FILES if not (MODULE_ROOT / name).is_file()]
    missing += [name for name in RECORD_FILES if not (record_root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    for checkpoint, contract in zip(checkpoints, CHECKPOINTS, strict=True):
        validate_checkpoint(checkpoint, contract)
        release = Path(contract["root"]) / "release.json"
        if not release.is_file() or sha256(release) != contract["release_sha256"]:
            raise ValueError(f"{contract['id']} release identity changed")

    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for name in CONTROL_FILES:
        copy_registered(MODULE_ROOT / name, target, name, "APP-5 Module 07", "0.1.0", "immutable leadership control", manifest)
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
    if len(manifest) != 1301 or files != 1328:
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
    with tempfile.TemporaryDirectory(prefix="app5-module07-assemble-") as temp_dir:
        base = Path(temp_dir)
        checkpoint1, checkpoint2 = base / "checkpoint1", base / "checkpoint2"
        build_reference_checkpoint(checkpoint1, CHECKPOINTS[0])
        build_reference_checkpoint(checkpoint2, CHECKPOINTS[1])
        first, second, learner = base / "reference-1", base / "reference-2", base / "learner"
        one = assemble(checkpoint1, checkpoint2, first, reference=True)
        assert "REPLACE" not in (first / "recommendation-and-alternatives.md").read_text(encoding="utf-8")
        shutil.rmtree(first)
        two = assemble(checkpoint1, checkpoint2, second, reference=True)
        shutil.rmtree(second)
        starter = assemble(checkpoint1, checkpoint2, learner)
        assert one == two
        assert one["manifest_rows"] == 1301 and one["assembled_files"] == 1328
        assert starter["manifest_sha256"] == one["manifest_sha256"]
        assert "REPLACE" in (learner / "recommendation-and-alternatives.md").read_text(encoding="utf-8")
        try:
            assemble(checkpoint1, checkpoint2, learner)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler overwrote an existing target")
    print("APP-5 Module 07 assembler self-check passed: 1,301 immutable rows and 1,328 candidate files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--checkpoint1", type=Path)
    parser.add_argument("--checkpoint2", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.target and args.reference:
            if args.checkpoint1 or args.checkpoint2:
                parser.error("--reference cannot be combined with checkpoint paths")
            with tempfile.TemporaryDirectory(prefix="app5-module07-reference-") as temp_dir:
                base = Path(temp_dir)
                checkpoint1, checkpoint2 = base / "checkpoint1", base / "checkpoint2"
                build_reference_checkpoint(checkpoint1, CHECKPOINTS[0])
                build_reference_checkpoint(checkpoint2, CHECKPOINTS[1])
                print(json.dumps(assemble(checkpoint1, checkpoint2, args.target, reference=True), indent=2))
        elif args.target and args.checkpoint1 and args.checkpoint2:
            print(json.dumps(assemble(args.checkpoint1, args.checkpoint2, args.target), indent=2))
        else:
            parser.error("use --target with --reference or with --checkpoint1 and --checkpoint2")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Assembly failed: {error}\n")


if __name__ == "__main__":
    main()
