"""Freeze an accepted FND-1 Module 07 toolkit for final review."""

from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


CHECKPOINT_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = CHECKPOINT_ROOT.parent.parent
MODULE_ROOT = COURSE_ROOT / "modules" / "07-reproducible-handoff-ai-audit"
MODULE_ASSEMBLER = MODULE_ROOT / "assemble_toolkit.py"
MODULE_VALIDATOR = MODULE_ROOT / "validate_toolkit.py"
TEMPLATE_ROOT = CHECKPOINT_ROOT / "template"
REFERENCE_ROOT = CHECKPOINT_ROOT / "reference"
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]
MODULE_MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]
REVIEW_RECORDS = (
    "submission-record.md",
    "final-score.csv",
    "gate-results.csv",
    "defense-score.csv",
    "reviewer-record.md",
    "final-disposition.md",
    "handoff-acceptance.md",
    "final-reproduction.md",
)
FINAL_REVIEW_FILES = {
    "final-review/CHECKPOINT-VERSION",
    "final-review/candidate-manifest.csv",
    *(f"final-review/{name}" for name in REVIEW_RECORDS),
}


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


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Path is not portable: {value}")
    return path


def run_module_validation(toolkit: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(MODULE_VALIDATOR), str(toolkit)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        raise ValueError(f"Module 07 complete validation failed: {result.stderr.strip() or result.stdout.strip()}")


def candidate_inventory(toolkit: Path) -> list[dict[str, object]]:
    run_module_validation(toolkit)
    fields, immutable = read_csv(toolkit / "release-manifest.csv")
    if fields != MODULE_MANIFEST_FIELDS or len(immutable) != 74:
        raise ValueError("Module 07 release manifest changed.")
    roles = {row["relative_path"]: row["role"] for row in immutable}
    paths = sorted(path.relative_to(toolkit).as_posix() for path in toolkit.rglob("*") if path.is_file())
    if len(paths) != 90 or len(set(paths)) != 90:
        raise ValueError("Module 07 candidate must contain exactly 90 unique files.")
    rows = []
    for relative in paths:
        path = toolkit / safe_relative(relative)
        role = roles.get(relative)
        if relative == "release-manifest.csv":
            role = "Module 07 immutable manifest"
        elif role is None:
            role = "Module 07 release record"
        rows.append({
            "relative_path": relative,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "role": role,
        })
    return rows


def write_manifest(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def render_reference(text: str, values: dict[str, object]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    if "{{" in text or "}}" in text:
        raise ValueError("An unresolved reference token remains.")
    return text


def assemble(toolkit: Path, target: Path, reference: bool = False) -> dict[str, object]:
    toolkit = toolkit.resolve()
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if toolkit == target or toolkit in target.parents:
        raise ValueError("Target cannot be the candidate or a folder inside it.")
    rows = candidate_inventory(toolkit)

    target.mkdir(parents=True)
    for row in rows:
        relative = safe_relative(str(row["relative_path"]))
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(toolkit / relative, destination)

    review_root = target / "final-review"
    review_root.mkdir()
    shutil.copy2(CHECKPOINT_ROOT / "VERSION", review_root / "CHECKPOINT-VERSION")
    manifest_path = review_root / "candidate-manifest.csv"
    write_manifest(manifest_path, rows)
    values = {
        "CANDIDATE_MANIFEST_ROWS": len(rows),
        "CANDIDATE_MANIFEST_BYTES": manifest_path.stat().st_size,
        "CANDIDATE_MANIFEST_SHA256": sha256(manifest_path),
    }
    records_root = REFERENCE_ROOT if reference else TEMPLATE_ROOT
    for name in REVIEW_RECORDS:
        source = records_root / name
        destination = review_root / name
        if reference:
            destination.write_text(render_reference(source.read_text(encoding="utf-8"), values), encoding="utf-8", newline="\n")
        else:
            shutil.copy2(source, destination)

    actual = {path.relative_to(target).as_posix() for path in target.rglob("*") if path.is_file()}
    expected = {str(row["relative_path"]) for row in rows} | FINAL_REVIEW_FILES
    if actual != expected or len(actual) != 100:
        raise ValueError("Final checkpoint tree must contain exactly 100 expected files.")
    return {
        "files": len(actual),
        "candidate_files": len(rows),
        "manifest_bytes": values["CANDIDATE_MANIFEST_BYTES"],
        "manifest_sha256": values["CANDIDATE_MANIFEST_SHA256"],
        "reference": reference,
    }


def assemble_reference_toolkit(target: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(MODULE_ASSEMBLER), "--reference", "--target", str(target)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        raise ValueError(f"Module 07 reference assembly failed: {result.stderr.strip() or result.stdout.strip()}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-final-assemble-") as temp_dir:
        temp = Path(temp_dir)
        toolkit = temp / "toolkit"
        reference = temp / "reference"
        learner = temp / "learner"
        assemble_reference_toolkit(toolkit)
        reference_report = assemble(toolkit, reference, reference=True)
        learner_report = assemble(toolkit, learner)
        assert reference_report["files"] == learner_report["files"] == 100
        assert reference_report["candidate_files"] == learner_report["candidate_files"] == 90
        assert reference_report["manifest_sha256"] == learner_report["manifest_sha256"]
        assert "REPLACE" in (learner / "final-review/submission-record.md").read_text(encoding="utf-8")
        assert "{{" not in (reference / "final-review/submission-record.md").read_text(encoding="utf-8")
        try:
            assemble(toolkit, reference, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler did not protect an existing target.")
    print("FND-1 final-checkpoint assembler self-check passed: 100 files and 90 frozen candidate files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toolkit", type=Path)
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
            if args.toolkit:
                parser.error("--reference cannot be combined with --toolkit")
            with tempfile.TemporaryDirectory(prefix="fnd1-final-reference-") as temp_dir:
                toolkit = Path(temp_dir) / "toolkit"
                assemble_reference_toolkit(toolkit)
                report = assemble(toolkit, args.target, reference=True)
        else:
            if not args.toolkit:
                parser.error("--toolkit is required outside reference mode")
            report = assemble(args.toolkit, args.target)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Assembly failed: {exc}\n")
    print(
        "FND-1 final-checkpoint assembly passed: "
        f"{report['files']} files, {report['candidate_files']} frozen candidate files, "
        f"manifest SHA-256 {report['manifest_sha256']}."
    )


if __name__ == "__main__":
    main()
