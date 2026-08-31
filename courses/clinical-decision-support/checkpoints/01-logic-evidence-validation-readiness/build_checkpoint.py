"""Assemble the APP-4 cumulative Week 3 checkpoint."""

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
    {
        "id": "oclc-app4-01", "version": "0.1.0", "directory": "module-01",
        "root": COURSE_ROOT / "modules/01-cds-use-case-decision", "files": 41,
        "manifest_rows": 29,
        "manifest_sha256": "40ff7384d227a38b0f93832731d984098e6e6f3324a958dafc2319d23f282b45",
    },
    {
        "id": "oclc-app4-02", "version": "0.1.0", "directory": "module-02",
        "root": COURSE_ROOT / "modules/02-logic-triggers-data", "files": 86,
        "manifest_rows": 73,
        "manifest_sha256": "bf3a30d66944a799a1dcbb3bc971bbcc81a6a3986e3e08cacf26fac41ecb9ded",
    },
    {
        "id": "oclc-app4-03", "version": "0.1.0", "directory": "module-03",
        "root": COURSE_ROOT / "modules/03-evidence-calibration-validation", "files": 118,
        "manifest_rows": 102,
        "manifest_sha256": "e67f20599704f83ec1e695f23f571fb57c558109bde3bcc676a64afc3dcf8e22",
    },
)
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "assessment.md", "checkpoint-contract.json",
    "instructor-notes.md", "release.json", "build_checkpoint.py", "validate_checkpoint.py",
)
WORK_FILES = (
    "README.md", "evidence-index.csv", "logic-evidence-readiness-review.md",
    "checkpoint-score.csv", "checkpoint-gates.csv", "checkpoint-defense.md",
    "reproducibility-check.md", "ai-use.md", "progression-decision.md",
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
    with tempfile.TemporaryDirectory(prefix="app4-cp01-modules-") as temporary:
        temp = Path(temporary)
        for details in MODULES:
            workspace = temp / str(details["directory"])
            report = load_builder(str(details["id"]), Path(details["root"])).assemble(
                workspace, reference=True
            )
            if (
                report["assembled_files"] != details["files"]
                or report["manifest_rows"] != details["manifest_rows"]
                or report["manifest_sha256"] != details["manifest_sha256"]
            ):
                raise ValueError(f"{details['id']} accepted workspace identity changed")
            for path in sorted(workspace.rglob("*")):
                if not path.is_file() or "__pycache__" in path.parts:
                    continue
                within = path.relative_to(workspace).as_posix()
                relative = f"candidate/{details['directory']}/{within}"
                copy(path, target, relative)
                destination = target / relative
                manifest.append({
                    "relative_path": relative,
                    "bytes": destination.stat().st_size,
                    "sha256": sha256(destination),
                    "source_module": details["id"],
                    "source_version": details["version"],
                    "role": "accepted reference workspace artifact",
                })
    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "candidate-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "relative_path", "bytes", "sha256", "source_module", "source_version", "role"
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(manifest)
    file_count = sum(
        path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts
    )
    if len(manifest) != 245 or file_count != 263:
        raise ValueError(
            f"Checkpoint contract changed: {len(manifest)} candidate rows and {file_count} files"
        )
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "candidate_manifest_rows": len(manifest),
        "candidate_manifest_bytes": manifest_path.stat().st_size,
        "candidate_manifest_sha256": sha256(manifest_path),
        "checkpoint_editable_records": len(WORK_FILES),
        "assembled_files": file_count,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-cp01-build-") as temporary:
        base = Path(temporary)
        first, second, learner = base / "reference-1", base / "reference-2", base / "learner"
        one = assemble(first, reference=True)
        two = assemble(second, reference=True)
        starter = assemble(learner)
        assert one == two
        assert one["candidate_manifest_rows"] == 245
        assert one["assembled_files"] == starter["assembled_files"] == 263
        assert one["candidate_manifest_sha256"] == starter["candidate_manifest_sha256"]
        assert "REPLACE" not in (
            first / "logic-evidence-readiness-review.md"
        ).read_text(encoding="utf-8")
        assert "REPLACE" in (
            learner / "logic-evidence-readiness-review.md"
        ).read_text(encoding="utf-8")
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
    print("APP-4 Checkpoint 01 builder self-check passed: 245 accepted component files and 263 assembled files.")


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
