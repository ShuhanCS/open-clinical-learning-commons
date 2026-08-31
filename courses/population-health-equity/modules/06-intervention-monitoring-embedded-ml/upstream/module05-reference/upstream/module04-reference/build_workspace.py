"""Build an APP-5 Module 04 learner or reference workspace."""

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
    ".gitattributes",
    "VERSION",
    "requirements.txt",
    "README.md",
    "assessment.md",
    "instructor-notes.md",
    "data-spec.md",
    "geography-contract.json",
    "release.json",
    "source-record.yml",
    "acquire_geometry.py",
    "freeze_upstream.py",
    "build_place_evidence.py",
    "build_workspace.py",
    "validate_workspace.py",
)
DATA_FILES = (
    "data/raw/tl_2024_25_tract.zip",
    "data/source-manifest.csv",
    "data/data-dictionary.csv",
)
OUTPUT_FILES = tuple(
    f"outputs/{name}"
    for name in (
        "source-profile.csv",
        "geometry-audit.csv",
        "geometry-join-audit.csv",
        "tract-map-table.csv",
        "small-area-stability.csv",
        "county-aggregation.csv",
        "aggregation-comparison.csv",
        "map-class-summary.csv",
        "query-checks.csv",
        "responsible-diabetes-prevalence-map.svg",
        "map-text-facts.json",
        "build-report.json",
    )
)
SQL_FILES = tuple(
    f"sql/{name}"
    for name in (
        "01-link-geometry-and-measures.sql",
        "02-compare-tract-and-county-aggregation.sql",
        "03-audit-map-release.sql",
    )
)
RECORD_FILES = (
    "geometry-source-review.md",
    "geography-join-and-crs-audit.md",
    "aggregation-and-stability-review.md",
    "ecological-contextual-claims-audit.csv",
    "responsible-map-specification.md",
    "responsible-map-text-alternative.md",
    "responsible-map-context-memo.md",
    "week6-component-score.csv",
    "gate-results.csv",
    "progression-decision.md",
    "reproducibility-check.md",
    "ai-use.md",
)
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]
EXPECTED_LEARNER_FILES = 275
EXPECTED_LEARNER_MANIFEST_ROWS = 259
EXPECTED_REFERENCE_FILES = 287
EXPECTED_REFERENCE_MANIFEST_ROWS = 271


def upstream_files(root: Path = ROOT) -> tuple[str, ...]:
    manifest_path = root / "upstream/checkpoint-handoff-manifest.csv"
    if not manifest_path.is_file():
        return ("upstream/checkpoint-handoff-manifest.csv",)
    with manifest_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return ("upstream/checkpoint-handoff-manifest.csv",) + tuple(
        f"upstream/{row['relative_path']}" for row in rows
    )


UPSTREAM_FILES = upstream_files()


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
    required += [f"{source_records.name}/{relative}" for relative in SQL_FILES + RECORD_FILES]
    missing = [relative for relative in required if not (ROOT / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")

    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for relative in immutable:
        copy(ROOT / relative, target, relative)
        destination = target / relative
        role = (
            "reference output"
            if relative.startswith("outputs/")
            else "immutable public source evidence"
            if relative.startswith("data/")
            else "accepted checkpoint handoff"
            if relative.startswith("upstream/")
            else "immutable module control"
        )
        manifest.append(
            {
                "relative_path": relative,
                "bytes": destination.stat().st_size,
                "sha256": sha256(destination),
                "role": role,
            }
        )
    for relative in SQL_FILES + RECORD_FILES:
        copy(source_records / relative, target, relative)

    manifest.sort(key=lambda row: str(row["relative_path"]))
    with (target / "release-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts)
    expected_files = EXPECTED_REFERENCE_FILES if reference else EXPECTED_LEARNER_FILES
    expected_manifest = EXPECTED_REFERENCE_MANIFEST_ROWS if reference else EXPECTED_LEARNER_MANIFEST_ROWS
    if files != expected_files or len(manifest) != expected_manifest:
        raise ValueError(f"Workspace contract changed: {files} files and {len(manifest)} manifest rows")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "assembled_files": files,
        "manifest_rows": len(manifest),
        "manifest_bytes": (target / "release-manifest.csv").stat().st_size,
        "manifest_sha256": sha256(target / "release-manifest.csv"),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module04-workspace-") as temporary:
        base = Path(temporary)
        first = assemble(base / "reference-1", reference=True)
        second = assemble(base / "reference-2", reference=True)
        learner = assemble(base / "learner")
        assert first["assembled_files"] == EXPECTED_REFERENCE_FILES
        assert first["manifest_rows"] == EXPECTED_REFERENCE_MANIFEST_ROWS
        assert first["manifest_sha256"] == second["manifest_sha256"]
        assert learner["assembled_files"] == EXPECTED_LEARNER_FILES
        assert learner["manifest_rows"] == EXPECTED_LEARNER_MANIFEST_ROWS
        assert "REPLACE" in (base / "learner/responsible-map-context-memo.md").read_text(encoding="utf-8")
        assert "REPLACE" not in (base / "reference-1/responsible-map-context-memo.md").read_text(encoding="utf-8")
        try:
            assemble(base / "reference-1", reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder did not protect an existing target")
    print(
        "APP-5 Module 04 workspace-builder self-check passed: "
        f"{EXPECTED_LEARNER_FILES} learner files and {EXPECTED_REFERENCE_FILES} reference files."
    )


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
            print(json.dumps(assemble(args.target, reference=args.reference), indent=2, sort_keys=True))
        else:
            parser.error("--target is required unless --self-check is used")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Workspace build failed: {error}\n")


if __name__ == "__main__":
    main()
