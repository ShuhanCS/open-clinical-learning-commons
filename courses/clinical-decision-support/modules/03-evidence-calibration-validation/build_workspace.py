"""Build the APP-4 Module 03 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MODULE02 = ROOT.parent / "02-logic-triggers-data"
REFERENCE = ROOT / "reference"
TEMPLATE = ROOT / "template"
CONTROL_FILES = (
    ".gitattributes", "VERSION", "requirements.txt", "environment.yml", "assessment.md",
    "data-spec.md", "decision-contract.json", "release.json", "source-record.yml",
    "build_evidence.py", "validate_workspace.py",
)
RECORD_FILES = (
    "evidence-release.md", "cohort-target-contract.csv", "survey-design-audit.csv",
    "model-specification.csv", "performance-interpretation.md", "calibration-audit.csv",
    "threshold-consequence-audit.csv", "decision-curve-interpretation.md",
    "transport-stress-audit.csv", "subgroup-support-audit.csv", "evidence-limitations.md",
    "week3-component-release.md", "claim-boundary.csv", "ai-use.md",
    "progression-decision.md",
)
MANIFEST_FIELDS = ("relative_path", "bytes", "sha256", "role")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_module02_builder():
    path = MODULE02 / "build_workspace.py"
    spec = importlib.util.spec_from_file_location("app4_module02_builder", path)
    if spec is None or spec.loader is None:
        raise ValueError("Cannot load the Module 02 workspace builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def copy(source: Path, target: Path, relative: str) -> None:
    destination = target / Path(relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def evidence_files() -> tuple[str, ...]:
    manifest = ROOT / "data" / "evidence" / "evidence-manifest.csv"
    rows = read_csv(manifest)
    if len(rows) != 17:
        raise ValueError(f"Evidence manifest changed: {len(rows)} files")
    return ("data/evidence/evidence-manifest.csv",) + tuple(
        f"data/evidence/{row['relative_path']}" for row in rows
    )


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = REFERENCE if reference else TEMPLATE
    own_files = CONTROL_FILES + evidence_files()
    missing = [relative for relative in own_files if not (ROOT / relative).is_file()]
    missing += [relative for relative in RECORD_FILES if not (record_root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    with tempfile.TemporaryDirectory(prefix="app4-module03-inherit-") as temporary:
        module02_workspace = Path(temporary) / "module02"
        module02_builder = load_module02_builder()
        module02_builder.assemble(module02_workspace, reference=True)
        inherited = read_csv(module02_workspace / "release-manifest.csv")
        if len(inherited) != 73:
            raise ValueError(f"Module 02 inheritance changed: {len(inherited)} files")
        target.mkdir(parents=True)
        manifest: list[dict[str, object]] = []
        for row in inherited:
            relative = row["relative_path"]
            destination_relative = f"inherited/module02/{relative}"
            copy(module02_workspace / relative, target, destination_relative)
            destination = target / destination_relative
            manifest.append({
                "relative_path": destination_relative,
                "bytes": destination.stat().st_size,
                "sha256": sha256(destination),
                "role": "immutable accepted Module 02 inheritance",
            })
    for relative in own_files:
        copy(ROOT / relative, target, relative)
        destination = target / relative
        manifest.append({
            "relative_path": relative,
            "bytes": destination.stat().st_size,
            "sha256": sha256(destination),
            "role": "immutable Module 03 historical evidence" if relative.startswith("data/evidence/") else "immutable Module 03 control",
        })
    for relative in RECORD_FILES:
        copy(record_root / relative, target, relative)
    manifest.sort(key=lambda row: str(row["relative_path"]))
    with (target / "release-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*"))
    if len(manifest) != 102 or files != 118:
        raise ValueError(f"Workspace contract changed: {len(manifest)} immutable rows and {files} files")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest),
        "manifest_sha256": sha256(target / "release-manifest.csv"),
        "editable_records": len(RECORD_FILES),
        "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module03-workspace-") as temporary:
        base = Path(temporary)
        first, second, starter = base / "reference-1", base / "reference-2", base / "starter"
        first_report = assemble(first, reference=True)
        second_report = assemble(second, reference=True)
        starter_report = assemble(starter)
        assert first_report["manifest_rows"] == 102 and first_report["assembled_files"] == 118
        assert first_report["manifest_sha256"] == second_report["manifest_sha256"]
        assert starter_report["editable_records"] == 15 and starter_report["mode"] == "learner"
        assert "REPLACE" in (starter / "evidence-release.md").read_text(encoding="utf-8")
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
    print("APP-4 Module 03 workspace builder self-check passed: 102 immutable rows and 118 files.")


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
            parser.error("provide --target or choose --self-check")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
