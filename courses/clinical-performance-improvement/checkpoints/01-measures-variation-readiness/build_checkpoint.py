"""Assemble the APP-3 cumulative Week 3 checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import shutil
import tempfile
from pathlib import Path


CHECKPOINT_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = CHECKPOINT_ROOT.parent.parent
MODULES = (
    ("oclc-app3-01", "0.1.0", "module-01", COURSE_ROOT / "modules/01-clinical-performance-decision", 25),
    ("oclc-app3-02", "0.1.0", "module-02", COURSE_ROOT / "modules/02-measures-operational-metrics", 58),
    ("oclc-app3-03", "0.1.0", "module-03", COURSE_ROOT / "modules/03-variation-safety-bottlenecks", 54),
)
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "checkpoint-contract.json", "assessment.md",
    "instructor-notes.md", "build_checkpoint.py", "validate_checkpoint.py",
)
WORK_FILES = (
    "README.md", "evidence-index.csv", "measures-variation-readiness-review.md",
    "checkpoint-gates.csv", "checkpoint-defense.md", "reproducibility-check.md",
    "ai-use.md", "progression-decision.md",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_builder(module_id: str, root: Path):
    spec = importlib.util.spec_from_file_location(
        f"{module_id.replace('-', '_')}_workspace", root / "build_workspace.py"
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load workspace builder for {module_id}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def copy(source: Path, target: Path, relative: str) -> None:
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = CHECKPOINT_ROOT / ("reference" if reference else "template")
    missing = [name for name in IMMUTABLE_FILES if not (CHECKPOINT_ROOT / name).is_file()]
    missing += [name for name in WORK_FILES if not (record_root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Checkpoint package is missing: {', '.join(missing)}")
    target.mkdir(parents=True)
    for name in IMMUTABLE_FILES:
        copy(CHECKPOINT_ROOT / name, target, name)
    for name in WORK_FILES:
        copy(record_root / name, target, name)

    manifest: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="app3-cp01-modules-") as temp_dir:
        temp = Path(temp_dir)
        for module_id, version, directory, module_root, expected_files in MODULES:
            workspace = temp / directory
            report = load_builder(module_id, module_root).assemble(workspace, reference=True)
            if report["assembled_files"] != expected_files:
                raise ValueError(f"{module_id} assembled file count changed")
            for path in sorted(workspace.rglob("*")):
                if not path.is_file() or "__pycache__" in path.parts:
                    continue
                within = path.relative_to(workspace).as_posix()
                relative = f"candidate/{directory}/{within}"
                copy(path, target, relative)
                destination = target / relative
                manifest.append({
                    "relative_path": relative,
                    "bytes": destination.stat().st_size,
                    "sha256": sha256(destination),
                    "source_module": module_id,
                    "source_version": version,
                    "role": "accepted reference workspace artifact",
                })
    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "candidate-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["relative_path", "bytes", "sha256", "source_module", "source_version", "role"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(manifest)
    file_count = sum(
        path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts
    )
    if len(manifest) != 137 or file_count != 153:
        raise ValueError(f"Checkpoint contract changed: {len(manifest)} candidate rows and {file_count} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "candidate_manifest_rows": len(manifest),
        "candidate_manifest_bytes": manifest_path.stat().st_size,
        "candidate_manifest_sha256": sha256(manifest_path),
        "assembled_files": file_count,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app3-cp01-") as temp_dir:
        base = Path(temp_dir)
        first, second, learner = base / "reference-1", base / "reference-2", base / "learner"
        one = assemble(first, reference=True)
        two = assemble(second, reference=True)
        starter = assemble(learner)
        assert one == two
        assert one["candidate_manifest_rows"] == 137
        assert one["assembled_files"] == starter["assembled_files"] == 153
        assert one["candidate_manifest_sha256"] == starter["candidate_manifest_sha256"]
        assert "REPLACE" not in (first / "measures-variation-readiness-review.md").read_text(encoding="utf-8")
        assert "REPLACE" in (learner / "measures-variation-readiness-review.md").read_text(encoding="utf-8")
        first_files = {
            path.relative_to(first): sha256(path)
            for path in first.rglob("candidate/**/*") if path.is_file()
        }
        second_files = {
            path.relative_to(second): sha256(path)
            for path in second.rglob("candidate/**/*") if path.is_file()
        }
        assert first_files == second_files
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Checkpoint builder overwrote an existing target")
    print("APP-3 Checkpoint 1 builder self-check passed: 137 accepted component files and 153 assembled files.")


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
            print(json.dumps(assemble(args.target, reference=args.reference), indent=2))
        else:
            parser.error("--target is required unless --self-check is used")
    except (OSError, ValueError, ImportError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
