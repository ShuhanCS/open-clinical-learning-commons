"""Build the APP-4 Module 02 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MODULE01 = ROOT.parent / "01-cds-use-case-decision"
REFERENCE = ROOT / "reference"
TEMPLATE = ROOT / "template"
CONTROL_FILES = (
    ".gitattributes", "VERSION", "assessment.md", "data-spec.md", "decision-contract.json",
    "release.json", "source-record.yml", "synthea.properties", "generate_synthetic_release.py",
    "build_logic_fixtures.py", "evaluate_rules.py", "validate_workspace.py",
)
SYNTHETIC_CONTROLS = (
    "data/synthetic-release/source-manifest.csv",
    "data/synthetic-release/build-inputs.csv",
    "data/synthetic-release/synthetic-release.json",
    "data/synthetic-release/generation-log.txt",
)
COMMONS_FILES = (
    "data/commons/patient-linkage.csv",
    "data/commons/rule-test-cases.csv",
    "data/commons/logic-config.json",
)
MODULE01_FILES = (
    ".gitattributes", "VERSION", "requirements.txt", "assessment.md", "data-spec.md",
    "decision-contract.json", "profile_sources.py", "source-record.yml", "validate_workspace.py",
    "data/source-inventory.csv", "data/field-inventory.csv", "data/cycle-join-profile.csv",
    "data/standards-inventory.csv",
) + tuple(
    f"data/raw/{component}_{suffix}.xpt.gz"
    for suffix in ("H", "I", "J", "L")
    for component in ("DEMO", "BMX", "DIQ", "GHB")
)
RECORD_FILES = (
    "use-case-logic-release.md", "logic-specification.csv", "input-contract.csv",
    "trigger-suppression-matrix.csv", "rule-test-results.csv", "terminology-map.csv",
    "synthetic-release-interpretation.md", "logic-change-control.md",
    "patient-workflow-consequence-map.csv", "claim-boundary.csv", "ai-use.md",
    "progression-decision.md",
)
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def synthetic_files() -> tuple[str, ...]:
    manifest = ROOT / "data" / "synthetic-release" / "source-manifest.csv"
    with manifest.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 25:
        raise ValueError(f"Synthetic source contract changed: {len(rows)} files")
    return SYNTHETIC_CONTROLS + tuple(
        f"data/synthetic-release/{row['relative_path']}" for row in rows
    )


def copy(source: Path, target: Path, relative: str) -> None:
    destination = target / Path(relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = REFERENCE if reference else TEMPLATE
    own_files = CONTROL_FILES + synthetic_files() + COMMONS_FILES
    missing = [relative for relative in own_files if not (ROOT / relative).is_file()]
    missing += [relative for relative in MODULE01_FILES if not (MODULE01 / relative).is_file()]
    missing += [relative for relative in RECORD_FILES if not (record_root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for relative in MODULE01_FILES:
        destination_relative = f"inherited/module01/{relative}"
        copy(MODULE01 / relative, target, destination_relative)
        destination = target / destination_relative
        manifest.append({
            "relative_path": destination_relative,
            "bytes": destination.stat().st_size,
            "sha256": sha256(destination),
            "role": "immutable Module 01 inheritance",
        })
    for relative in own_files:
        copy(ROOT / relative, target, relative)
        destination = target / relative
        role = (
            "immutable full synthetic FHIR source"
            if relative.startswith("data/synthetic-release/fhir/")
            else "immutable synthetic release control"
            if relative.startswith("data/synthetic-release/")
            else "immutable Commons rule fixture"
            if relative.startswith("data/commons/")
            else "immutable Module 02 control"
        )
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
    if len(manifest) != 73 or files != 86:
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
    with tempfile.TemporaryDirectory(prefix="app4-module02-build-") as temporary:
        base = Path(temporary)
        first, second, starter = base / "reference-1", base / "reference-2", base / "starter"
        report = assemble(first, reference=True)
        second_report = assemble(second, reference=True)
        starter_report = assemble(starter)
        assert report["manifest_rows"] == 73 and report["assembled_files"] == 86
        assert report["manifest_sha256"] == second_report["manifest_sha256"]
        assert starter_report["mode"] == "learner" and starter_report["editable_records"] == 12
        assert "REPLACE" in (starter / "use-case-logic-release.md").read_text(encoding="utf-8")
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
    print("APP-4 Module 02 builder self-check passed: 73 immutable rows and 86 workspace files.")


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
