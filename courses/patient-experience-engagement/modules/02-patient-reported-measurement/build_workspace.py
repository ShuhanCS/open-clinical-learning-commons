"""Build an APP-2 Module 02 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
CONTROLS = (
    ".gitattributes", "README.md", "VERSION", "assessment.md", "build_measurement.py",
    "build_workspace.py", "data-spec.md", "instructor-notes.md", "measurement-contract.json",
    "rights-record.md", "source-record.yml", "validate_workspace.py",
)
DATA_FILES = (
    "data/source-inventory.csv", "data/mode-language-inventory.csv", "data/version-crosswalk.csv",
    "data/item-map.csv", "data/scoring-rules.csv",
    "data/synthetic/patient-measurement-responses.csv", "outputs/synthetic-score-summary.csv",
    "outputs/reliability-diagnostics.csv", "outputs/published-concordance.csv",
    "outputs/published-concordance-summary.csv", "outputs/invariant-checks.csv", "build-report.json",
)
RECORD_FILES = (
    "instrument-comparison.csv", "construct-content-validity.md", "scoring-reproduction.csv",
    "reliability-interpretation.md", "meaningful-interpretation.md", "language-mode-access.csv",
    "proxy-burden-record.md", "rights-naming-decision.md", "measurement-decision.md",
    "measurement-score.csv", "gate-results.csv", "ai-use.md", "progression-decision.md",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def raw_files() -> tuple[str, ...]:
    with (MODULE_ROOT / "data/source-inventory.csv").open(encoding="utf-8", newline="") as handle:
        return tuple(row["relative_path"] for row in csv.DictReader(handle))


def immutable_files() -> tuple[str, ...]:
    files = CONTROLS + DATA_FILES + raw_files()
    if len(files) != 52 or len(set(files)) != 52:
        raise ValueError(f"Immutable package contract changed: {len(files)} rows")
    return files


def copy(source: Path, target: Path, relative: str) -> None:
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def assemble(target: Path, reference: bool = False) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    record_root = MODULE_ROOT / ("reference" if reference else "template")
    immutable = immutable_files()
    missing = [relative for relative in immutable if not (MODULE_ROOT / relative).is_file()]
    missing += [relative for relative in RECORD_FILES if not (record_root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for relative in immutable:
        source = MODULE_ROOT / relative
        copy(source, target, relative)
        role = "immutable module control"
        if relative.startswith("data/raw/"):
            role = "immutable full public source"
        elif relative.startswith("data/") or relative.startswith("outputs/") or relative == "build-report.json":
            role = "immutable measurement evidence"
        manifest.append({"relative_path": relative, "bytes": source.stat().st_size, "sha256": sha256(source), "role": role})
    for relative in RECORD_FILES:
        copy(record_root / relative, target, relative)
    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "release-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256", "role"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*"))
    if len(manifest) != 52 or files != 66:
        raise ValueError(f"Workspace contract changed: {len(manifest)} manifest rows and {files} files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "manifest_rows": 52, "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path), "assembled_files": 66,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module02-workspace-") as temp_dir:
        base = Path(temp_dir)
        first, second, starter = base / "reference-1", base / "reference-2", base / "starter"
        first_report = assemble(first, reference=True)
        second_report = assemble(second, reference=True)
        starter_report = assemble(starter)
        assert first_report["manifest_sha256"] == second_report["manifest_sha256"]
        assert first_report["assembled_files"] == 66 and starter_report["mode"] == "learner"
        assert "REPLACE" in (starter / "measurement-decision.md").read_text(encoding="utf-8")
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder did not protect an existing target")
    print("APP-2 Module 02 workspace builder self-check passed: 52 immutable rows and 66 files.")


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
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
