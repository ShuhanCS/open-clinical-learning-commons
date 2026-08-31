"""Build an APP-5 Module 03 learner or reference workspace."""

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
    "disparity-contract.json", "release.json", "source-record.yml",
    "generate_equity_layer.py", "freeze_upstream.py", "build_disparities.py",
    "build_workspace.py", "validate_workspace.py",
)
DATA_FILES = (
    "data/raw/synthetic-equity-margins.csv.gz",
    "data/raw/synthetic-field-completeness.csv.gz",
    "data/equity-group-contract.csv",
    "data/data-dictionary.csv",
    "data/synthetic-source-manifest.csv",
)
OUTPUT_FILES = tuple(f"outputs/{name}" for name in (
    "equity-margin-reconciliation.csv", "group-age-rates.csv",
    "standardized-group-rates.csv", "disparity-comparisons.csv",
    "summary-disparities.csv", "missingness-audit.csv",
    "representation-audit.csv", "published-tract-group-rates.csv.gz",
    "complementary-suppression-audit.csv", "bias-register.csv",
    "query-checks.csv", "build-report.json",
))
SQL_FILES = tuple(f"sql/{name}" for name in (
    "01-link-equity-margins-and-reconcile.sql",
    "02-build-group-age-rates.sql",
    "03-standardize-and-compare-references.sql",
    "04-audit-missingness-bias-and-suppression.sql",
))
RECORD_FILES = (
    "disparity-measure-specifications.csv", "reference-group-sensitivity.csv",
    "missingness-and-representation-audit.md", "selection-linkage-measurement-bias.md",
    "suppression-policy.md", "responsible-disparity-claim.md",
    "week3-component-score.csv", "gate-results.csv", "progression-decision.md",
    "reproducibility-check.md", "ai-use.md",
)


def upstream_files(root: Path = ROOT) -> tuple[str, ...]:
    manifest_path = root / "upstream/module02-handoff-manifest.csv"
    if not manifest_path.is_file():
        return ("upstream/module02-handoff-manifest.csv",)
    with manifest_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return ("upstream/module02-handoff-manifest.csv",) + tuple(f"upstream/{row['relative_path']}" for row in rows)


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
    expected_files = 120 if reference else 108
    expected_manifest = 104 if reference else 92
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
    with tempfile.TemporaryDirectory(prefix="app5-module03-workspace-") as temp_dir:
        base = Path(temp_dir)
        first = assemble(base / "reference-1", reference=True)
        second = assemble(base / "reference-2", reference=True)
        starter = assemble(base / "starter")
        assert first["assembled_files"] == 120 and first["manifest_rows"] == 104
        assert first["manifest_sha256"] == second["manifest_sha256"]
        assert starter["assembled_files"] == 108 and starter["manifest_rows"] == 92
        assert "REPLACE" in (base / "starter/disparity-measure-specifications.csv").read_text(encoding="utf-8")
        try:
            assemble(base / "reference-1", reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder did not protect an existing target")
    print("APP-5 Module 03 workspace-builder self-check passed: 108 learner files and 120 reference files.")


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
