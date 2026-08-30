"""Assemble the FND-1 Module 07 reproducible toolkit candidate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = MODULE_ROOT.parent.parent
CHECKPOINT_ROOT = COURSE_ROOT / "checkpoints" / "02-quality-descriptive-accessible-release"
CHECKPOINT_ASSEMBLER = CHECKPOINT_ROOT / "assemble_checkpoint.py"
CHECKPOINT_VALIDATOR = CHECKPOINT_ROOT / "validate_checkpoint.py"
PIPELINE_CONTRACT = MODULE_ROOT / "pipeline-contract.csv"
TEMPLATE_ROOT = MODULE_ROOT / "template"
REFERENCE_ROOT = MODULE_ROOT / "reference"
RECORD_FILES = (
    ".gitattributes", "README.md", "CHANGELOG.md", "release-notes.md",
    "component-score.csv", "release-checklist.md", "reproducibility-check.md",
    "review-disposition.md", "documentation/data-brief.md", "documentation/limitations.md",
    "documentation/ai-audit.md", "audit/prompt-log.csv", "defense/handoff-brief.md",
    "defense/questions-and-responses.md",
)
CHECKPOINT_RECORDS = (
    "README.md", "component-score.csv", "quality-decision.md", "interpretation-memo.md",
    "accessibility-synthesis.md", "source-record.yml", "transformation-record.md",
    "reproducibility-check.md", "ai-use.md", "review-disposition.md",
)
CHECKPOINT_PROVENANCE = {
    "VERSION": "provenance/checkpoint2-VERSION",
    "artifact-contract.csv": "provenance/checkpoint2-artifact-contract.csv",
    "release-manifest.csv": "provenance/checkpoint2-release-manifest.csv",
    "checkpoint-summary.csv": "provenance/checkpoint2-summary.csv",
}
PIPELINE_FIELDS = ["artifact_id", "source_unit", "source_module_dir", "source_path", "target_path", "byte_count", "sha256", "role"]
CHECKPOINT_MANIFEST_FIELDS = [
    "artifact_id", "source_module", "source_path", "target_path", "row_count",
    "byte_count", "sha256", "role", "assembled_byte_count", "assembled_sha256", "status",
]
RELEASE_MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]


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


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=RELEASE_MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Path is not portable: {value}")
    return path


def read_pipeline_contract(course_root: Path) -> list[dict[str, str]]:
    fields, rows = read_csv(PIPELINE_CONTRACT)
    if fields != PIPELINE_FIELDS or len(rows) != 23:
        raise ValueError("Pipeline contract schema or row count changed.")
    if len({row["artifact_id"] for row in rows}) != 23 or len({row["target_path"] for row in rows}) != 23:
        raise ValueError("Pipeline artifact IDs and target paths must be unique.")
    if Counter(row["source_unit"] for row in rows) != Counter({"M01": 1, "M02": 13, "M03": 5, "M04": 2, "M05": 1, "M06": 1}):
        raise ValueError("Pipeline source allocation changed.")
    for row in rows:
        source = course_root / "modules" / safe_relative(row["source_module_dir"]) / safe_relative(row["source_path"])
        safe_relative(row["target_path"])
        if not source.is_file():
            raise ValueError(f"Missing pipeline source: {source}")
        if source.stat().st_size != int(row["byte_count"]) or sha256(source) != row["sha256"]:
            raise ValueError(f"Pipeline source fingerprint changed: {row['artifact_id']}")
    return rows


def validate_checkpoint(checkpoint: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKPOINT_VALIDATOR), str(checkpoint)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        raise ValueError(f"Checkpoint 2 validation failed: {result.stderr.strip() or result.stdout.strip()}")


def checkpoint_manifest(checkpoint: Path) -> list[dict[str, str]]:
    fields, rows = read_csv(checkpoint / "release-manifest.csv")
    if fields != CHECKPOINT_MANIFEST_FIELDS or len(rows) != 35:
        raise ValueError("Checkpoint 2 manifest schema or row count changed.")
    if any(row["status"] != "verified" for row in rows):
        raise ValueError("Checkpoint 2 manifest contains an unverified artifact.")
    return rows


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


def assemble(checkpoint: Path, course_root: Path, target: Path, reference: bool = False) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    checkpoint = checkpoint.resolve()
    course_root = course_root.resolve()
    validate_checkpoint(checkpoint)
    checkpoint_rows = checkpoint_manifest(checkpoint)
    pipeline_rows = read_pipeline_contract(course_root)

    immutable_paths = {row["target_path"] for row in checkpoint_rows}
    additions = {
        *(f"documentation/checkpoint2/{name}" for name in CHECKPOINT_RECORDS),
        *CHECKPOINT_PROVENANCE.values(),
        *(row["target_path"] for row in pipeline_rows),
        "pipeline-contract.csv", "validation/validate_toolkit.py",
    }
    if immutable_paths & additions or len(immutable_paths | additions) != 74:
        raise ValueError("Toolkit immutable paths overlap or changed.")

    target.mkdir(parents=True)
    records_root = REFERENCE_ROOT if reference else TEMPLATE_ROOT
    for relative in RECORD_FILES:
        destination = target / safe_relative(relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(records_root / safe_relative(relative), destination)
    shutil.copy2(MODULE_ROOT / "VERSION", target / "VERSION")

    manifest: list[dict[str, object]] = []
    for row in checkpoint_rows:
        source = checkpoint / safe_relative(row["target_path"])
        if source.stat().st_size != int(row["byte_count"]) or sha256(source) != row["sha256"]:
            raise ValueError(f"Checkpoint artifact changed after validation: {row['artifact_id']}")
        copy_registered(source, target, row["target_path"], f"CP2-{row['source_module']}", "0.1.0", row["role"], manifest)

    for name in CHECKPOINT_RECORDS:
        copy_registered(checkpoint / name, target, f"documentation/checkpoint2/{name}", "CP2", "0.1.0", "accepted cumulative checkpoint record", manifest)
    for source_name, target_name in CHECKPOINT_PROVENANCE.items():
        copy_registered(checkpoint / source_name, target, target_name, "CP2", "0.1.0", "checkpoint provenance contract", manifest)

    for row in pipeline_rows:
        source = course_root / "modules" / safe_relative(row["source_module_dir"]) / safe_relative(row["source_path"])
        copy_registered(source, target, row["target_path"], row["source_unit"], "0.1.0", row["role"], manifest)

    copy_registered(PIPELINE_CONTRACT, target, "pipeline-contract.csv", "M07", "0.1.0", "pipeline source contract", manifest)
    copy_registered(MODULE_ROOT / "validate_toolkit.py", target, "validation/validate_toolkit.py", "M07", "0.1.0", "portable toolkit validator", manifest)
    manifest.sort(key=lambda row: str(row["relative_path"]))
    write_csv(target / "release-manifest.csv", manifest)

    report = {
        "files": sum(1 for path in target.rglob("*") if path.is_file()),
        "immutable": len(manifest),
        "pipeline": len(pipeline_rows),
        "reference": reference,
    }
    if report["files"] != 90 or report["immutable"] != 74:
        raise ValueError(f"Assembled toolkit counts changed: {report}")
    return report


def assemble_reference_checkpoint(target: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKPOINT_ASSEMBLER), "--reference", "--target", str(target)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        raise ValueError(f"Reference Checkpoint 2 assembly failed: {result.stderr.strip() or result.stdout.strip()}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-module07-assemble-") as temp_dir:
        temp = Path(temp_dir)
        checkpoint = temp / "checkpoint2"
        reference = temp / "reference"
        learner = temp / "learner"
        assemble_reference_checkpoint(checkpoint)
        report = assemble(checkpoint, COURSE_ROOT, reference, reference=True)
        assert report == {"files": 90, "immutable": 74, "pipeline": 23, "reference": True}
        learner_report = assemble(checkpoint, COURSE_ROOT, learner)
        assert learner_report == {"files": 90, "immutable": 74, "pipeline": 23, "reference": False}
        assert (reference / "release-manifest.csv").read_bytes() == (learner / "release-manifest.csv").read_bytes()
        assert "REPLACE" in (learner / "README.md").read_text(encoding="utf-8")
        try:
            assemble(checkpoint, COURSE_ROOT, reference, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler did not protect an existing target.")
    print("FND-1 Module 07 assembler self-check passed: 90 files and 74 immutable artifacts.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint2", type=Path)
    parser.add_argument("--course-root", type=Path, default=COURSE_ROOT)
    parser.add_argument("--target", type=Path)
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
            if args.checkpoint2:
                parser.error("--reference cannot be combined with --checkpoint2")
            with tempfile.TemporaryDirectory(prefix="fnd1-module07-reference-") as temp_dir:
                checkpoint = Path(temp_dir) / "checkpoint2"
                assemble_reference_checkpoint(checkpoint)
                report = assemble(checkpoint, args.course_root, args.target.resolve(), reference=True)
        else:
            if not args.checkpoint2:
                parser.error("--checkpoint2 is required outside reference mode")
            report = assemble(args.checkpoint2, args.course_root, args.target.resolve())
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Assembly failed: {exc}\n")
    print(f"FND-1 Module 07 assembly passed: {report['files']} files and {report['immutable']} immutable artifacts.")


if __name__ == "__main__":
    main()
