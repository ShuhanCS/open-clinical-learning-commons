"""Assemble APP-1 Module 06 learner or reference workspaces."""

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
    ".gitattributes", "VERSION", "source-record.yml", "equity-contract.csv", "model-contract.json",
    "feature-contract.csv", "environment.yml", "assessment.md", "build_equity_improvement.py",
    "build_workspace.py", "validate_equity_improvement.py",
)
WORK_FILES = (
    "README.md", "equity-review.md", "pathway-display.md", "improvement-brief.md", "driver-diagram.csv",
    "improvement-measures.csv", "ml-comparison.md", "failure-case-review.md", "reproducibility-check.md",
    "ai-use.md", "progression-decision.md",
)
OUTPUT_FILES = (
    "analysis-checks.csv", "bootstrap-comparison.csv", "build-report.json", "calibration-bins.csv",
    "equity-summary.csv", "failure-cases.csv", "feature-importance.csv", "model-performance.csv",
    "model-predictions.csv", "pathway-edges.csv", "pathway-figure.svg", "pathway-nodes.csv",
    "split-registry.csv", "subgroup-model-audit.csv", "threshold-errors.csv",
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
    missing = [name for name in IMMUTABLE_FILES if not (MODULE_ROOT / name).is_file()]
    missing += [name for name in WORK_FILES if not (record_root / name).is_file()]
    if reference:
        missing += [f"outputs/{name}" for name in OUTPUT_FILES if not (OUTPUT_ROOT / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    target.mkdir(parents=True)
    manifest = []
    for relative in IMMUTABLE_FILES:
        copy(MODULE_ROOT / relative, target, relative)
        destination = target / relative
        manifest.append({
            "relative_path": relative, "bytes": destination.stat().st_size, "sha256": sha256(destination),
            "role": "immutable source equity model environment assessment or executable control",
        })
    for relative in WORK_FILES:
        copy(record_root / relative, target, relative)
    if reference:
        for relative in OUTPUT_FILES:
            copy(OUTPUT_ROOT / relative, target, f"outputs/{relative}")
    manifest.sort(key=lambda row: row["relative_path"])
    manifest_path = target / "workspace-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256", "role"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    expected_files = 38 if reference else 23
    actual_files = sum(path.is_file() for path in target.rglob("*"))
    if len(manifest) != 11 or actual_files != expected_files:
        raise ValueError(f"Workspace contract changed: {len(manifest)} manifest rows and {actual_files} files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner", "manifest_rows": len(manifest),
        "manifest_bytes": manifest_path.stat().st_size, "manifest_sha256": sha256(manifest_path), "assembled_files": actual_files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app1-module06-workspace-") as temp_dir:
        root = Path(temp_dir)
        first, second, learner = root / "first", root / "second", root / "learner"
        one, two = assemble(first, reference=True), assemble(second, reference=True)
        starter = assemble(learner)
        assert one == two
        assert one["assembled_files"] == 38 and starter["assembled_files"] == 23
        assert "REPLACE" not in (first / "equity-review.md").read_text(encoding="utf-8")
        assert "REPLACE" in (learner / "equity-review.md").read_text(encoding="utf-8")
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder overwrote an existing target")
    print("APP-1 Module 06 workspace builder self-check passed: 11 immutable rows and 23/38 learner/reference files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.target:
            parser.error("--target is required")
        print(json.dumps(assemble(args.target, reference=args.reference), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Assembly failed: {error}\n")


if __name__ == "__main__":
    main()
