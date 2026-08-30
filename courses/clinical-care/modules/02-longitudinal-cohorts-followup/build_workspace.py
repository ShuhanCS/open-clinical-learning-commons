"""Assemble an APP-1 Module 02 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
TEMPLATE_ROOT = MODULE_ROOT / "template"
OUTPUT_ROOT = MODULE_ROOT / "outputs"
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "source-record.yml", "extension-contract.json",
    "data-dictionary.csv", "assessment.md", "build_longitudinal.py", "validate_longitudinal.py",
)
WORK_FILES = (
    "README.md", "phenotype-spec.md", "transformation-record.md", "validation-notes.md",
    "reproducibility-check.md", "ai-use.md", "progression-decision.md",
    "sql/01-index-cohort.sql", "sql/02-event-audit.sql",
    "sql/03-longitudinal-cohort.sql", "sql/04-validation.sql",
)
OUTPUT_FILES = (
    "analysis-cohort.csv", "build-report.json", "censoring-summary.csv", "cohort-flow.csv",
    "event-audit.csv", "index-cohort.csv", "longitudinal-cohort.csv", "query-checks.csv",
    "site-assignment.csv", "site-support.csv",
)


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


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = MODULE_ROOT if reference else TEMPLATE_ROOT
    missing = [relative for relative in IMMUTABLE_FILES if not (MODULE_ROOT / relative).is_file()]
    missing += [relative for relative in WORK_FILES if not (record_root / relative).is_file()]
    if reference:
        missing += [f"outputs/{relative}" for relative in OUTPUT_FILES if not (OUTPUT_ROOT / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")

    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for relative in IMMUTABLE_FILES:
        source = MODULE_ROOT / relative
        copy(source, target, relative)
        destination = target / relative
        manifest.append({
            "relative_path": relative,
            "bytes": destination.stat().st_size,
            "sha256": sha256(destination),
            "role": "immutable source extension assessment or executable control",
        })
    for relative in WORK_FILES:
        copy(record_root / relative, target, relative)
    if reference:
        for relative in OUTPUT_FILES:
            copy(OUTPUT_ROOT / relative, target, f"outputs/{relative}")

    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "workspace-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256", "role"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    file_count = sum(path.is_file() for path in target.rglob("*"))
    expected_files = 30 if reference else 20
    if len(manifest) != 8 or file_count != expected_files:
        raise ValueError(f"Workspace contract changed: {len(manifest)} immutable rows and {file_count} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "assembled_files": file_count,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app1-module02-workspace-") as temp_dir:
        base = Path(temp_dir)
        reference_one, reference_two, learner = base / "reference-one", base / "reference-two", base / "learner"
        first = assemble(reference_one, reference=True)
        second = assemble(reference_two, reference=True)
        starter = assemble(learner)
        assert first["manifest_sha256"] == second["manifest_sha256"]
        assert first["assembled_files"] == 30 and starter["assembled_files"] == 20
        assert "REPLACE" in (learner / "phenotype-spec.md").read_text(encoding="utf-8")
        assert "REPLACE" not in (reference_one / "phenotype-spec.md").read_text(encoding="utf-8")
        try:
            assemble(reference_one, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder overwrote an existing target")
    print("APP-1 Module 02 workspace builder self-check passed: 8 immutable rows and 20/30 starter/reference files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
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
        report = assemble(args.target, reference=args.reference)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
