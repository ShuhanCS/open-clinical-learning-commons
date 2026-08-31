"""Build an APP-5 Module 02 learner or reference workspace."""

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
    ".gitattributes", "VERSION", "requirements.txt", "assessment.md", "data-spec.md",
    "measure-contract.json", "release.json", "source-record.yml",
    "generate_synthetic_events.py", "freeze_upstream.py", "build_measures.py",
    "build_workspace.py", "validate_workspace.py",
)
DATA_FILES = (
    "data/raw/synthetic-events.csv.gz", "data/age-band-crosswalk.csv",
    "data/data-dictionary.csv", "data/synthetic-source-manifest.csv",
)
OUTPUT_FILES = tuple(f"outputs/{name}" for name in (
    "tract-linkage-audit.csv", "age-band-denominators.csv.gz",
    "synthetic-event-linkage.csv.gz", "age-specific-rates.csv.gz",
    "standard-population.csv", "tract-rate-summary.csv",
    "indirect-standardization.csv", "public-modeled-prevalence.csv",
    "source-reconciliation.csv", "query-checks.csv", "build-report.json",
))
SQL_FILES = tuple(f"sql/{name}" for name in (
    "01-link-sources-and-build-denominators.sql",
    "02-link-events-and-separate-public-measure.sql",
    "03-calculate-rates-and-direct-standardization.sql",
    "04-indirect-standardization-and-validation.sql",
))
RECORD_FILES = (
    "population-measure-specifications.csv", "age-band-and-moe-method.md",
    "linkage-and-denominator-audit.md", "standardization-interpretation.md",
    "public-synthetic-separation.md", "measure-score.csv", "gate-results.csv",
    "progression-decision.md", "reproducibility-check.md", "ai-use.md",
)


def upstream_files(root: Path = ROOT) -> tuple[str, ...]:
    manifest_path = root / "upstream/module01-handoff-manifest.csv"
    if not manifest_path.is_file():
        return ("upstream/module01-handoff-manifest.csv",)
    with manifest_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return ("upstream/module01-handoff-manifest.csv",) + tuple(f"upstream/{row['relative_path']}" for row in rows)


UPSTREAM_FILES = upstream_files()
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]


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
    manifest = []
    for relative in immutable:
        copy(ROOT / relative, target, relative)
        destination = target / relative
        role = "reference output" if relative.startswith("outputs/") else (
            "immutable source evidence" if relative.startswith(("data/", "upstream/")) else "immutable module control"
        )
        manifest.append({
            "relative_path": relative,
            "bytes": destination.stat().st_size,
            "sha256": sha256(destination),
            "role": role,
        })
    for relative in SQL_FILES + RECORD_FILES:
        copy(source_records / relative, target, relative)

    manifest.sort(key=lambda row: str(row["relative_path"]))
    with (target / "release-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*"))
    expected_files = 72 if reference else 61
    expected_manifest = 57 if reference else 46
    if files != expected_files or len(manifest) != expected_manifest:
        raise ValueError(f"Workspace contract changed: {files} files and {len(manifest)} manifest rows")
    return {
        "status": "pass",
        "mode": "reference" if reference else "learner",
        "assembled_files": files,
        "manifest_rows": len(manifest),
        "manifest_sha256": sha256(target / "release-manifest.csv"),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module02-workspace-") as temp_dir:
        base = Path(temp_dir)
        first = assemble(base / "reference-1", reference=True)
        second = assemble(base / "reference-2", reference=True)
        starter = assemble(base / "starter")
        assert first["assembled_files"] == 72 and first["manifest_rows"] == 57
        assert first["manifest_sha256"] == second["manifest_sha256"]
        assert starter["assembled_files"] == 61 and starter["manifest_rows"] == 46
        assert "REPLACE" in (base / "starter/population-measure-specifications.csv").read_text(encoding="utf-8")
        try:
            assemble(base / "reference-1", reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder did not protect an existing target")
    print("APP-5 Module 02 workspace-builder self-check passed: 61 learner files and 72 reference files.")


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
