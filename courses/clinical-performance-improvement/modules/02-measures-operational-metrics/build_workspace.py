"""Build an APP-3 Module 02 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONTROL_FILES = (
    ".gitattributes", "VERSION", "assessment.md", "data-spec.md",
    "operational-contract.json", "release.json", "source-record.yml",
    "generate_operational_release.py", "freeze_upstream.py", "build_measures.py",
    "build_workspace.py", "validate_workspace.py",
)
DATA_FILES = (
    "data/operational-source-manifest.csv", "data/data-dictionary.csv",
    "data/raw/encounters.csv.gz", "data/raw/process-events.csv.gz",
    "data/raw/staffing.csv.gz", "data/raw/queue-snapshots.csv.gz",
    "data/raw/safety-events.csv.gz", "data/raw/calendar-demand.csv.gz",
    "data/raw/scenarios.csv.gz", "data/raw/known-truth.csv.gz",
    "data/raw/defect-register.csv.gz",
)
UPSTREAM_FILES = (
    "upstream/module01-handoff-manifest.csv", "upstream/module01-decision-contract.json",
    "upstream/clinical-performance-charter.md", "upstream/synthetic-service-declaration.md",
    "upstream/unit-of-flow.csv", "upstream/process-boundary.csv",
    "upstream/measure-family.csv", "upstream/module01-source-inventory.csv",
    "upstream/source-feasibility-interpretation.md", "upstream/claim-boundary.csv",
    "upstream/progression-decision.md",
)
SQL_FILES = tuple(f"sql/{name}" for name in (
    "01-clean-operational-sources.sql", "02-encounter-measures.sql",
    "03-operational-measures.sql", "04-validation-and-defects.sql",
))
RECORD_FILES = (
    "measure-specifications.csv", "defect-repair-log.csv", "event-validation.md",
    "operational-interpretation.md", "subgroup-support-interpretation.md",
    "measure-score.csv", "gate-results.csv", "ai-use.md",
    "progression-decision.md", "reproducibility-check.md",
)
OUTPUT_FILES = (
    "outputs/source-reconciliation.csv", "outputs/encounter-measures.csv.gz",
    "outputs/shift-metrics.csv", "outputs/weekly-metrics.csv",
    "outputs/safety-diagnostics.csv", "outputs/subgroup-support.csv",
    "outputs/defect-impact.csv", "outputs/query-checks.csv",
    "outputs/build-report.json",
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
    source_records = ROOT / ("reference" if reference else "template")
    immutable = CONTROL_FILES + DATA_FILES + UPSTREAM_FILES + (OUTPUT_FILES if reference else ())
    required = list(immutable)
    required += [f"{source_records.name}/{relative}" for relative in RECORD_FILES]
    required += [f"{source_records.name}/{relative}" for relative in SQL_FILES]
    missing = [relative for relative in required if not (ROOT / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")

    target.mkdir(parents=True)
    manifest = []
    for relative in immutable:
        copy(ROOT / relative, target, relative)
        destination = target / relative
        role = "reference output" if relative.startswith("outputs/") else (
            "immutable source evidence" if relative.startswith(("data/", "upstream/")) else "immutable module control"
        )
        manifest.append({
            "relative_path": relative, "bytes": destination.stat().st_size,
            "sha256": sha256(destination), "role": role,
        })
    for relative in SQL_FILES + RECORD_FILES:
        copy(source_records / relative, target, relative)

    manifest.sort(key=lambda row: str(row["relative_path"]))
    with (target / "release-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256", "role"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*"))
    expected_files = 58 if reference else 49
    expected_manifest = 43 if reference else 34
    if files != expected_files or len(manifest) != expected_manifest:
        raise ValueError(f"Workspace contract changed: {files} files and {len(manifest)} manifest rows")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "assembled_files": files, "manifest_rows": len(manifest),
        "manifest_sha256": sha256(target / "release-manifest.csv"),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app3-module02-workspace-") as temp_dir:
        base = Path(temp_dir)
        first = assemble(base / "reference-1", reference=True)
        second = assemble(base / "reference-2", reference=True)
        starter = assemble(base / "starter")
        assert first["assembled_files"] == 58 and first["manifest_rows"] == 43
        assert first["manifest_sha256"] == second["manifest_sha256"]
        assert starter["assembled_files"] == 49 and starter["manifest_rows"] == 34
        assert "REPLACE" in (base / "starter/measure-specifications.csv").read_text(encoding="utf-8")
        try:
            assemble(base / "reference-1", reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
    print("APP-3 Module 02 workspace-builder self-check passed: 49 learner files and 58 reference files.")


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
            parser.error("--target is required")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Workspace build failed: {error}\n")


if __name__ == "__main__":
    main()
