"""Assemble the FND-2 Module 07 governed analytics candidate."""

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
REPO_ROOT = MODULE_ROOT.parents[3]
CP2_ROOT = COURSE_ROOT / "checkpoints" / "02-validity-forecast-testing-release"
CP2_ASSEMBLER = CP2_ROOT / "assemble_checkpoint.py"
CP2_VALIDATOR = CP2_ROOT / "validate_checkpoint.py"
REFERENCE = MODULE_ROOT / "reference"
TEMPLATE = MODULE_ROOT / "template"
CONTROL_FILES = (
    ".gitattributes", ".gitignore", "VERSION", "governance-contract.json",
    "assessment.md", "validate_candidate.py",
)
RECORD_FILES = (
    "README.md", "CHANGELOG.md", "release-notes.md", "environment-and-commands.md",
    "evidence-index.csv", "model-card.md", "performance-appendix.csv",
    "subgroup-equity-review.md", "monitoring-plan.csv", "drift-retraining-versioning.md",
    "rollback-stop-retirement.md", "model-use-recommendation.md", "reproducibility-audit.md",
    "accessibility-review.md", "ai-use.md", "human-sign-off.md", "handoff-brief.md",
    "technical-defense.md", "component-score.csv", "gate-results.csv",
    "release-checklist.csv", "conditions-register.csv", "reviewer-record.md",
    "progression-decision.md",
)
SUPPLEMENTARY = (
    (REPO_ROOT / "courses/healthcare-data-foundations/checkpoints/03-reproducible-toolkit/release.json", "evidence/provenance/fnd1-final-release.json", "FND-1 final checkpoint", "7afffdaeb0470d2ffc918570a0a2400a255ebe3f1a47cb467ab9e862dff32dd8"),
    (REPO_ROOT / "courses/healthcare-data-foundations/checkpoints/03-reproducible-toolkit/reference/handoff-acceptance.md", "evidence/provenance/fnd1-handoff-acceptance.md", "FND-1 final checkpoint", "50b1a279cbcdf4ca642bbd4189e543a158cb3a1f7f26457216041ce216752a28"),
    (COURSE_ROOT / "modules/01-aims-reproducible-workspace/source-record.yml", "evidence/provenance/fnd2-module01-source-record.yml", "FND-2 Module 01", "f3ef7bb8ecbd892b70810a44f37ac146d7fde9b587e557ac145c732cf41cfc2b"),
    (COURSE_ROOT / "modules/01-aims-reproducible-workspace/data-spec.md", "evidence/provenance/fnd2-module01-data-spec.md", "FND-2 Module 01", "083f34ea5e58c2b5143bfa1efc3266150aee8f3a15515dcb677acf5d10642f19"),
    (COURSE_ROOT / "modules/03-prediction-evaluation/outputs/test-metrics.csv", "evidence/provenance/fnd2-module03-test-metrics.csv", "FND-2 Module 03", "9d43a8085e835cbf368962acc37b0bed00bdfacf68e73ce87d0b359dee490bc9"),
    (COURSE_ROOT / "modules/03-prediction-evaluation/outputs/subgroup-metrics.csv", "evidence/provenance/fnd2-module03-subgroup-metrics.csv", "FND-2 Module 03", "7f95ec1f99a1f9f9bae6af566798a4f3aab9107681fe7e79c1ce27a821e07d24"),
    (COURSE_ROOT / "modules/03-prediction-evaluation/prediction-evaluation-report.md", "evidence/provenance/fnd2-module03-prediction-report.md", "FND-2 Module 03", "8559a9b97a1cf540cf122577afeb16dfb7363aae5ddd9165ac7d26c34c8d8de7"),
)
CP2_MANIFEST_SHA256 = "16733c55e8a9930f4903006c81e5fb1acb9e75386507f1aa46867daac89f6ccc"
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


def validate_checkpoint2(checkpoint: Path) -> None:
    result = subprocess.run([sys.executable, str(CP2_VALIDATOR), str(checkpoint)], capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError(f"Checkpoint 2 validation failed: {result.stderr.strip() or result.stdout.strip()}")
    if sum(path.is_file() for path in checkpoint.rglob("*")) != 130:
        raise ValueError("Checkpoint 2 file count changed")
    if sha256(checkpoint / "release-manifest.csv") != CP2_MANIFEST_SHA256:
        raise ValueError("Checkpoint 2 manifest fingerprint changed")
    contract = json.loads((checkpoint / "checkpoint-contract.json").read_text(encoding="utf-8"))
    if contract["checkpoint"]["id"] != "oclc-fnd2-cp2" or contract["checkpoint"]["version"] != "0.1.0":
        raise ValueError("Checkpoint 2 identity changed")


def assemble_reference_checkpoint(target: Path) -> None:
    result = subprocess.run([sys.executable, str(CP2_ASSEMBLER), str(target), "--reference"], capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError(f"Reference Checkpoint 2 assembly failed: {result.stderr.strip() or result.stdout.strip()}")


def copy_registered(source: Path, target: Path, relative: str, source_unit: str, version: str, role: str, manifest: list[dict[str, object]]) -> None:
    destination = target / safe_relative(relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    manifest.append({
        "relative_path": relative.replace("\\", "/"), "source_unit": source_unit,
        "source_version": version, "bytes": destination.stat().st_size,
        "sha256": sha256(destination), "role": role,
    })


def assemble(checkpoint: Path, target: Path, reference: bool = False) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    validate_checkpoint2(checkpoint)
    require_files(MODULE_ROOT, CONTROL_FILES, "Module controls")
    record_root = REFERENCE if reference else TEMPLATE
    require_files(record_root, RECORD_FILES, "Candidate records")
    for source, _, _, digest in SUPPLEMENTARY:
        if not source.is_file() or sha256(source) != digest:
            raise ValueError(f"Supplementary provenance changed: {source.name}")

    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for name in CONTROL_FILES:
        copy_registered(MODULE_ROOT / name, target, name, "Module 07", "0.1.0", "candidate control", manifest)
    for name in RECORD_FILES:
        destination = target / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(record_root / name, destination)
    for source in sorted(path for path in checkpoint.rglob("*") if path.is_file()):
        relative = source.relative_to(checkpoint).as_posix()
        copy_registered(source, target, f"evidence/checkpoint2/{relative}", "Checkpoint 2", "0.1.0", "accepted Week 6 evidence", manifest)
    for source, relative, unit, _ in SUPPLEMENTARY:
        copy_registered(source, target, relative, unit, "0.1.0", "source and evaluation provenance", manifest)

    manifest.sort(key=lambda row: str(row["relative_path"]))
    with (target / "release-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*"))
    if len(manifest) != 143 or files != 168:
        raise ValueError(f"Candidate file contract changed: {len(manifest)} manifest rows and {files} files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest), "manifest_bytes": (target / "release-manifest.csv").stat().st_size,
        "manifest_sha256": sha256(target / "release-manifest.csv"), "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd2-module07-assemble-") as temp_dir:
        base = Path(temp_dir)
        checkpoint = base / "checkpoint2"
        assemble_reference_checkpoint(checkpoint)
        first, second, starter = base / "reference-1", base / "reference-2", base / "starter"
        report = assemble(checkpoint, first, reference=True)
        second_report = assemble(checkpoint, second, reference=True)
        starter_report = assemble(checkpoint, starter, reference=False)
        assert report["manifest_rows"] == 143 and report["assembled_files"] == 168
        assert report["manifest_sha256"] == second_report["manifest_sha256"]
        assert starter_report["mode"] == "learner" and "REPLACE" in (starter / "README.md").read_text(encoding="utf-8")
        try:
            assemble(checkpoint, first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler did not refuse an existing target")
    print("FND-2 Module 07 assembler self-check passed: 143 immutable rows and 168 candidate files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path)
    parser.add_argument("--checkpoint2", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if args.target is None:
        parser.error("target is required unless --self-check is used")
    try:
        if args.reference:
            if args.checkpoint2:
                parser.error("--reference cannot be combined with --checkpoint2")
            with tempfile.TemporaryDirectory(prefix="fnd2-module07-reference-") as temp_dir:
                checkpoint = Path(temp_dir) / "checkpoint2"
                assemble_reference_checkpoint(checkpoint)
                report = assemble(checkpoint, args.target.resolve(), reference=True)
        else:
            if not args.checkpoint2:
                parser.error("--checkpoint2 is required outside reference mode")
            report = assemble(args.checkpoint2.resolve(), args.target.resolve())
    except (OSError, ValueError) as error:
        parser.exit(1, f"Assembly failed: {error}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
