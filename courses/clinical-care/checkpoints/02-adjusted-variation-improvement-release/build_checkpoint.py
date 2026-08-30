"""Assemble the APP-1 cumulative Week 6 checkpoint."""

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
TEMPLATE_ROOT = CHECKPOINT_ROOT / "template"
MODULES = (
    ("oclc-app1-04", "0.1.0", "module-04", COURSE_ROOT / "modules/04-risk-adjustment-fair-comparison", 32),
    ("oclc-app1-05", "0.1.0", "module-05", COURSE_ROOT / "modules/05-clinical-variation-patterns-of-care", 30),
    ("oclc-app1-06", "0.1.0", "module-06", COURSE_ROOT / "modules/06-equity-improvement-embedded-ml", 38),
)
IMMUTABLE_FILES = (".gitattributes", "VERSION", "checkpoint-contract.json", "assessment.md", "build_checkpoint.py", "validate_checkpoint.py")
WORK_FILES = ("README.md", "evidence-index.csv", "adjusted-variation-improvement-review.md", "reproducibility-check.md", "ai-use.md", "progression-decision.md")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_builder(module_id: str, root: Path):
    spec = importlib.util.spec_from_file_location(f"{module_id.replace('-', '_')}_workspace", root / "build_workspace.py")
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
    record_root = CHECKPOINT_ROOT if reference else TEMPLATE_ROOT
    missing = [name for name in IMMUTABLE_FILES if not (CHECKPOINT_ROOT / name).is_file()]
    missing += [name for name in WORK_FILES if not (record_root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Checkpoint package is missing: {', '.join(missing)}")
    target.mkdir(parents=True)
    for name in IMMUTABLE_FILES:
        copy(CHECKPOINT_ROOT / name, target, name)
    for name in WORK_FILES:
        copy(record_root / name, target, name)

    manifest = []
    with tempfile.TemporaryDirectory(prefix="app1-cp02-modules-") as temp_dir:
        temp = Path(temp_dir)
        for module_id, version, directory, module_root, expected_files in MODULES:
            workspace = temp / directory
            report = load_builder(module_id, module_root).assemble(workspace, reference=True)
            if report["assembled_files"] != expected_files:
                raise ValueError(f"{module_id} assembled file count changed")
            for path in sorted(workspace.rglob("*")):
                if not path.is_file():
                    continue
                within = path.relative_to(workspace).as_posix()
                relative = f"candidate/{directory}/{within}"
                copy(path, target, relative)
                destination = target / relative
                manifest.append({
                    "relative_path": relative, "bytes": destination.stat().st_size, "sha256": sha256(destination),
                    "source_module": module_id, "source_version": version, "role": "accepted reference workspace artifact",
                })
    manifest.sort(key=lambda row: row["relative_path"])
    manifest_path = target / "candidate-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256", "source_module", "source_version", "role"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    file_count = sum(path.is_file() for path in target.rglob("*"))
    if len(manifest) != 100 or file_count != 113:
        raise ValueError(f"Checkpoint contract changed: {len(manifest)} candidate rows and {file_count} files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "candidate_manifest_rows": len(manifest), "candidate_manifest_bytes": manifest_path.stat().st_size,
        "candidate_manifest_sha256": sha256(manifest_path), "assembled_files": file_count,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app1-cp02-") as temp_dir:
        base = Path(temp_dir)
        first, second, learner = base / "first", base / "second", base / "learner"
        one = assemble(first, reference=True)
        two = assemble(second, reference=True)
        starter = assemble(learner)
        assert one == two
        assert one["assembled_files"] == starter["assembled_files"] == 113
        assert one["candidate_manifest_sha256"] == starter["candidate_manifest_sha256"]
        assert "REPLACE" not in (first / "adjusted-variation-improvement-review.md").read_text(encoding="utf-8")
        assert "REPLACE" in (learner / "adjusted-variation-improvement-review.md").read_text(encoding="utf-8")
        assert {path.relative_to(first): sha256(path) for path in first.rglob("candidate/**/*") if path.is_file()} == {path.relative_to(second): sha256(path) for path in second.rglob("candidate/**/*") if path.is_file()}
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Checkpoint builder overwrote an existing target")
    print("APP-1 Checkpoint 2 builder self-check passed: 100 accepted component files and 113 assembled files.")


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
    except (OSError, ValueError, ImportError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
