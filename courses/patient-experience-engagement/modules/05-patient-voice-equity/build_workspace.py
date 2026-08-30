"""Assemble an APP-2 Module 05 learner or reference workspace."""

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
    ".gitattributes", "README.md", "VERSION", "assessment.md", "build_patient_voice.py",
    "build_workspace.py", "data-spec.md", "instructor-notes.md", "source-record.yml",
    "validate_workspace.py", "voice-equity-contract.json",
)
UPSTREAM_FILES = (
    "data/upstream/module04-release.json", "data/upstream/module04-linked-persons.csv",
    "data/upstream/module04-linked-events.csv", "data/upstream/module04-source-inventory.csv",
    "data/upstream/module04-denominator-registry.csv",
)
GENERATED_FILES = (
    "data/synthetic/comment-opportunities.csv", "data/synthetic/synthetic-comments.csv",
    "data/synthetic/double-coding-sample.csv", "outputs/source-profile.csv",
    "outputs/comment-codebook.csv", "outputs/comment-flow.csv", "outputs/agreement-summary.csv",
    "outputs/assisted-classification-audit.csv", "outputs/theme-summary.csv",
    "outputs/comment-examples.csv", "outputs/group-support.csv", "outputs/group-estimates.csv",
    "outputs/group-contrasts.csv", "outputs/channel-exclusion-audit.csv",
    "outputs/invariant-checks.csv", "build-report.json",
)
RECORD_FILES = (
    "comment-provenance.md", "codebook-decisions.csv", "double-coding-review.csv",
    "agreement-interpretation.md", "assisted-classification-review.md", "group-analysis-plan.md",
    "group-support-decisions.csv", "group-difference-interpretation.md",
    "channel-exclusion-review.md", "equity-patient-voice-memo.md", "responsible-claims.md",
    "reproducibility-check.md", "gate-results.csv", "ai-use.md", "progression-decision.md",
)
IMMUTABLE_FILES = CONTROLS + ("data/upstream-inventory.csv",) + UPSTREAM_FILES + GENERATED_FILES


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
    record_root = MODULE_ROOT / ("reference" if reference else "template")
    missing = [relative for relative in IMMUTABLE_FILES if not (MODULE_ROOT / relative).is_file()]
    missing += [relative for relative in RECORD_FILES if not (record_root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Module package is missing: {', '.join(missing)}")
    target.mkdir(parents=True)
    manifest: list[dict[str, object]] = []
    for relative in IMMUTABLE_FILES:
        source = MODULE_ROOT / relative
        copy(source, target, relative)
        role = "immutable module control"
        if relative.startswith("data/upstream/"):
            role = "immutable accepted Module 04 handoff"
        elif relative.startswith("data/synthetic/"):
            role = "immutable synthetic patient-voice teaching data"
        elif relative.startswith("outputs/") or relative == "build-report.json":
            role = "immutable patient-voice group and validation evidence"
        manifest.append({"relative_path": relative, "bytes": source.stat().st_size, "sha256": sha256(source), "role": role})
    for relative in RECORD_FILES:
        copy(record_root / relative, target, relative)
    manifest.sort(key=lambda row: str(row["relative_path"]))
    manifest_path = target / "release-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("relative_path", "bytes", "sha256", "role"), lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    files = sum(path.is_file() for path in target.rglob("*") if "__pycache__" not in path.parts)
    if len(manifest) != 33 or files != 49:
        raise ValueError(f"Workspace contract changed: {len(manifest)} manifest rows and {files} files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "manifest_rows": len(manifest), "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path), "assembled_files": files,
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module05-workspace-") as temp_dir:
        base = Path(temp_dir)
        first, second, learner = base / "reference-1", base / "reference-2", base / "learner"
        one = assemble(first, reference=True)
        two = assemble(second, reference=True)
        starter = assemble(learner)
        assert one == two
        assert one["manifest_rows"] == 33 and one["assembled_files"] == 49
        assert starter["mode"] == "learner" and "REPLACE" in (learner / "comment-provenance.md").read_text(encoding="utf-8")
        assert not (learner / "instructor").exists()
        try:
            assemble(first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workspace builder overwrote an existing target")
    print(f"APP-2 Module 05 workspace builder self-check passed: 33 immutable rows, {one['manifest_bytes']} manifest bytes, and 49 files.")


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
