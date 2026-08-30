"""Build an APP-2 Module 01 decision-framing workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
REFERENCE = MODULE_ROOT / "reference"
TEMPLATE = MODULE_ROOT / "template"
IMMUTABLE_FILES = (
    ".gitattributes", "README.md", "VERSION", "assessment.md", "build_workspace.py",
    "data-spec.md", "decision-contract.json", "instructor-notes.md", "profile_source.py",
    "source-record.yml", "validate_workspace.py", "data/raw/HCAHPS-Hospital.csv.gz",
    "data/source-profile.csv", "data/measure-inventory.csv", "data/discharge-measure-profile.csv",
)
RECORD_FILES = (
    "patient-experience-decision-charter.md", "construct-map.csv", "patient-journey-map.csv",
    "evidence-needs.csv", "stakeholder-partnership-map.csv", "claim-boundary.csv",
    "source-feasibility-interpretation.md", "ai-use.md", "progression-decision.md",
)
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def copy(source: Path, target: Path, relative: str) -> None:
    destination = target / Path(relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = REFERENCE if reference else TEMPLATE
    missing = [relative for relative in IMMUTABLE_FILES if not (MODULE_ROOT / relative).is_file()]
    missing += [relative for relative in RECORD_FILES if not (record_root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")

    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for relative in IMMUTABLE_FILES:
        source = MODULE_ROOT / relative
        copy(source, target, relative)
        destination = target / relative
        role = "immutable full public source" if relative.endswith(".csv.gz") else "immutable module control"
        if relative.startswith("data/") and not relative.endswith(".csv.gz"):
            role = "immutable derived source evidence"
        manifest.append({
            "relative_path": relative,
            "bytes": destination.stat().st_size,
            "sha256": sha256(destination),
            "role": role,
        })
    for relative in RECORD_FILES:
        copy(record_root / relative, target, relative)

    manifest.sort(key=lambda row: str(row["relative_path"]))
    with (target / "release-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*"))
    if len(manifest) != 15 or files != 25:
        raise ValueError(f"Workspace contract changed: {len(manifest)} immutable rows and {files} files")
    manifest_path = target / "release-manifest.csv"
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest), "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path), "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module01-build-") as temp_dir:
        base = Path(temp_dir)
        first, second, starter = base / "reference-1", base / "reference-2", base / "starter"
        first_report = assemble(first, reference=True)
        second_report = assemble(second, reference=True)
        starter_report = assemble(starter)
        assert first_report["manifest_rows"] == 15 and first_report["assembled_files"] == 25
        assert first_report["manifest_sha256"] == second_report["manifest_sha256"]
        assert starter_report["mode"] == "learner"
        assert "REPLACE" in (starter / "patient-experience-decision-charter.md").read_text(encoding="utf-8")
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
    print("APP-2 Module 01 builder self-check passed: 15 immutable rows and 25 workspace files.")


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
        print(json.dumps(assemble(args.target, reference=args.reference), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
