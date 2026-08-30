"""Assemble the FND-1 cumulative Week 6 checkpoint from accepted modules."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from collections import Counter
from pathlib import Path


CHECKPOINT_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = CHECKPOINT_ROOT.parent.parent
CONTRACT_PATH = CHECKPOINT_ROOT / "artifact-contract.csv"
TEMPLATE_ROOT = CHECKPOINT_ROOT / "template"
REFERENCE_ROOT = CHECKPOINT_ROOT / "reference"
CANONICAL_ROOTS = {
    "M04": COURSE_ROOT / "modules" / "04-cleaning-profiling",
    "M05": COURSE_ROOT / "modules" / "05-descriptive-results",
    "M06": COURSE_ROOT / "modules" / "06-accessible-charts-time-data",
}
MODULES = {
    "M04": {"id": "oclc-fnd1-04", "version": "0.1.0", "role": "quality, risk, resolution, and final data decision", "decision": "proceed with conditions", "condition": "D01-D20 resolved; N01-N08 retained"},
    "M05": {"id": "oclc-fnd1-05", "version": "0.1.0", "role": "descriptive evidence, denominators, and interpretation", "decision": "accept with conditions", "condition": "exact denominators and descriptive limits preserved"},
    "M06": {"id": "oclc-fnd1-06", "version": "0.1.0", "role": "accessible figures, alternatives, and time limits", "decision": "accept with conditions", "condition": "equivalent access and selected-cohort limits preserved"},
}
RECORD_FILES = (
    ".gitattributes", "README.md", "component-score.csv", "quality-decision.md",
    "interpretation-memo.md", "accessibility-synthesis.md", "source-record.yml",
    "transformation-record.md", "reproducibility-check.md", "ai-use.md",
    "review-disposition.md",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Artifact contract path is not portable: {value}")
    return path


def read_contract() -> list[dict[str, str]]:
    fields, rows = read_csv(CONTRACT_PATH)
    expected_fields = ["artifact_id", "source_module", "source_path", "target_path", "row_count", "byte_count", "sha256", "role"]
    if fields != expected_fields or len(rows) != 35:
        raise ValueError("Artifact contract schema or row count changed.")
    if len({row["artifact_id"] for row in rows}) != 35 or len({row["target_path"] for row in rows}) != 35:
        raise ValueError("Artifact IDs and target paths must be unique.")
    if Counter(row["source_module"] for row in rows) != Counter({"M04": 11, "M05": 9, "M06": 15}):
        raise ValueError("Artifact module allocation changed.")
    for row in rows:
        safe_relative(row["source_path"])
        safe_relative(row["target_path"])
        if row["source_module"] not in MODULES:
            raise ValueError(f"Unknown source module: {row['source_module']}")
    return rows


def validate_module_root(key: str, root: Path) -> None:
    release_path = root / "release.json"
    if not release_path.is_file():
        raise ValueError(f"{key} release.json is missing: {root}")
    release = json.loads(release_path.read_text(encoding="utf-8"))
    expected = MODULES[key]
    if release.get("module", {}).get("id") != expected["id"] or release.get("module", {}).get("version") != expected["version"]:
        raise ValueError(f"{key} module ID or version changed.")
    decision = release["decision"].get("reference_final") or release["decision"].get("reference")
    if decision != expected["decision"]:
        raise ValueError(f"{key} accepted decision changed.")


def verify_source(path: Path, row: dict[str, str]) -> None:
    if not path.is_file():
        raise ValueError(f"Missing source artifact: {row['source_module']} {row['source_path']}")
    if path.stat().st_size != int(row["byte_count"]) or sha256(path) != row["sha256"]:
        raise ValueError(f"Source artifact fingerprint changed: {row['artifact_id']}")
    if row["row_count"]:
        _, records = read_csv(path)
        if len(records) != int(row["row_count"]):
            raise ValueError(f"Source artifact row count changed: {row['artifact_id']}")


def assemble(module_roots: dict[str, Path], target: Path, reference: bool = False) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    roots = {key: root.resolve() for key, root in module_roots.items()}
    if set(roots) != set(MODULES):
        raise ValueError("Exactly M04, M05, and M06 roots are required.")
    contract = read_contract()
    for key, root in roots.items():
        validate_module_root(key, root)
    for row in contract:
        verify_source(roots[row["source_module"]] / safe_relative(row["source_path"]), row)

    target.mkdir(parents=True)
    records_root = REFERENCE_ROOT if reference else TEMPLATE_ROOT
    for name in RECORD_FILES:
        shutil.copy2(records_root / name, target / name)
    shutil.copy2(CHECKPOINT_ROOT / "VERSION", target / "VERSION")
    shutil.copy2(CONTRACT_PATH, target / "artifact-contract.csv")

    manifest = []
    for row in contract:
        source = roots[row["source_module"]] / safe_relative(row["source_path"])
        destination = target / safe_relative(row["target_path"])
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        manifest.append({
            **row,
            "assembled_byte_count": destination.stat().st_size,
            "assembled_sha256": sha256(destination),
            "status": "verified",
        })
    write_csv(target / "release-manifest.csv", manifest)

    counts = Counter(row["source_module"] for row in contract)
    summary = []
    for key in ("M04", "M05", "M06"):
        module = MODULES[key]
        summary.append({
            "source_module": key, "module_id": module["id"], "version": module["version"],
            "role": module["role"], "accepted_decision": module["decision"],
            "artifact_count": counts[key], "progression_condition": module["condition"],
        })
    write_csv(target / "checkpoint-summary.csv", summary)
    return {"files": sum(1 for path in target.rglob("*") if path.is_file()), "artifacts": len(manifest), "reference": reference}


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-checkpoint2-assemble-") as temp_dir:
        temp = Path(temp_dir)
        reference = temp / "reference"
        learner = temp / "learner"
        report = assemble(CANONICAL_ROOTS, reference, reference=True)
        assert report == {"files": 50, "artifacts": 35, "reference": True}
        learner_report = assemble(CANONICAL_ROOTS, learner)
        assert learner_report == {"files": 50, "artifacts": 35, "reference": False}
        assert "REPLACE" in (learner / "README.md").read_text(encoding="utf-8")
        try:
            assemble(CANONICAL_ROOTS, reference, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler did not protect an existing target.")
    print("FND-1 Checkpoint 2 assembler self-check passed: 50 files and 35 immutable artifacts.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module04", type=Path)
    parser.add_argument("--module05", type=Path)
    parser.add_argument("--module06", type=Path)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.target:
        parser.error("--target is required")
    if args.reference:
        if any((args.module04, args.module05, args.module06)):
            parser.error("--reference cannot be combined with module roots")
        roots = CANONICAL_ROOTS
    else:
        if not all((args.module04, args.module05, args.module06)):
            parser.error("--module04, --module05, and --module06 are required")
        roots = {"M04": args.module04, "M05": args.module05, "M06": args.module06}
    try:
        report = assemble(roots, args.target.resolve(), reference=args.reference)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Assembly failed: {exc}\n")
    print(f"FND-1 Checkpoint 2 assembly passed: {report['files']} files and {report['artifacts']} immutable artifacts.")


if __name__ == "__main__":
    main()
