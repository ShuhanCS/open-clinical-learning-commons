"""Freeze an accepted APP-5 Module 07 candidate for final review."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


sys.dont_write_bytecode = True


CHECKPOINT_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = CHECKPOINT_ROOT.parent.parent
MODULE_ROOT = COURSE_ROOT / "modules/07-clinician-leadership-equity-recommendation"
MODULE_ASSEMBLER = MODULE_ROOT / "assemble_candidate.py"
MODULE_VALIDATOR = MODULE_ROOT / "validate_candidate.py"
MODULE_RELEASE = MODULE_ROOT / "release.json"
CP1_RELEASE = COURSE_ROOT / "checkpoints/01-measures-disparities-readiness/release.json"
CP2_RELEASE = COURSE_ROOT / "checkpoints/02-place-targeting-intervention-release/release.json"
REFERENCE_ROOT = CHECKPOINT_ROOT / "reference"
TEMPLATE_ROOT = CHECKPOINT_ROOT / "template"
REVIEW_RECORDS = (
    "submission-record.md", "final-score.csv", "gate-results.csv", "final-defense.md",
    "reviewer-record.md", "final-reproduction.md", "conditions-register.csv",
    "final-audit.md", "final-decision.md", "release-acceptance.md",
)
FINAL_FILES = {
    "final-review/CHECKPOINT-VERSION", "final-review/checkpoint1-release.json",
    "final-review/checkpoint2-release.json", "final-review/module07-release.json",
    "final-review/candidate-manifest.csv", *(f"final-review/{name}" for name in REVIEW_RECORDS),
}
MODULE_MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]
FINAL_MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]
MODULE_MANIFEST_BYTES = 328429
MODULE_MANIFEST_SHA256 = "ebae232c051fe8b1204b4266aec416f48fe152b4dc5cda06a3ae00171807097b"
MODULE_RELEASE_SHA256 = "6e5a2c796257b7a9f72ccc1e7f725a2f9e818753791afd90e24fdef817477ce7"
CP1_RELEASE_SHA256 = "2748c0bf5f6c0fe90bca29899202e8a3e2b0fa303b4fa37248bbd8daca5d5289"
CP2_RELEASE_SHA256 = "b67fa825fa35e86063799091c34c65ccb95c3784f03e3c4c6cfa692f0c584f55"


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


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError(f"Path is not portable: {value}")
    return path


def link_or_copy(source: Path, destination: Path) -> None:
    try:
        os.link(source, destination)
    except OSError:
        shutil.copy2(source, destination)


def run(command: list[str], label: str) -> None:
    result = subprocess.run(
        command, capture_output=True, text=True, check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if result.returncode:
        raise ValueError(f"{label} failed: {result.stderr.strip() or result.stdout.strip()}")


def candidate_inventory(candidate: Path) -> list[dict[str, object]]:
    run(
        [sys.executable, str(MODULE_VALIDATOR), "--candidate", str(candidate), "--complete"],
        "Module 07 validation",
    )
    fields, immutable = read_csv(candidate / "release-manifest.csv")
    if fields != MODULE_MANIFEST_FIELDS or len(immutable) != 1301:
        raise ValueError("Module 07 immutable manifest changed")
    manifest = candidate / "release-manifest.csv"
    if manifest.stat().st_size != MODULE_MANIFEST_BYTES or sha256(manifest) != MODULE_MANIFEST_SHA256:
        raise ValueError("Module 07 manifest fingerprint changed")
    roles = {row["relative_path"]: row["role"] for row in immutable}
    paths = sorted(
        path.relative_to(candidate).as_posix()
        for path in candidate.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    )
    if len(paths) != 1328 or len(set(paths)) != 1328:
        raise ValueError("Module 07 candidate must contain exactly 1,328 unique files")
    return [{
        "relative_path": relative,
        "bytes": (candidate / safe_relative(relative)).stat().st_size,
        "sha256": sha256(candidate / safe_relative(relative)),
        "role": roles.get(relative, "Module 07 leadership record or generated manifest"),
    } for relative in paths]


def write_manifest(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FINAL_MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def render(value: str, tokens: dict[str, object]) -> str:
    for key, replacement in tokens.items():
        value = value.replace("{{" + key + "}}", str(replacement))
    if "{{" in value or "}}" in value:
        raise ValueError("An unresolved assembly token remains")
    return value


def assemble(candidate: Path, target: Path, reference: bool = False, hardlink: bool = False) -> dict[str, object]:
    candidate, target = candidate.resolve(), target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if target == candidate or candidate in target.parents:
        raise ValueError("Target cannot be the candidate or a folder inside it")
    for path, digest, label in (
        (MODULE_RELEASE, MODULE_RELEASE_SHA256, "Module 07"),
        (CP1_RELEASE, CP1_RELEASE_SHA256, "Checkpoint 01"),
        (CP2_RELEASE, CP2_RELEASE_SHA256, "Checkpoint 02"),
    ):
        if not path.is_file() or sha256(path) != digest:
            raise ValueError(f"Accepted {label} release identity changed")
    rows = candidate_inventory(candidate)
    record_root = REFERENCE_ROOT if reference else TEMPLATE_ROOT
    missing = [name for name in REVIEW_RECORDS if not (record_root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Final review records are missing: {', '.join(missing)}")

    target.mkdir(parents=True)
    for row in rows:
        relative = safe_relative(str(row["relative_path"]))
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if hardlink:
            link_or_copy(candidate / relative, destination)
        else:
            shutil.copy2(candidate / relative, destination)

    review = target / "final-review"
    review.mkdir()
    shutil.copy2(CHECKPOINT_ROOT / "VERSION", review / "CHECKPOINT-VERSION")
    shutil.copy2(CP1_RELEASE, review / "checkpoint1-release.json")
    shutil.copy2(CP2_RELEASE, review / "checkpoint2-release.json")
    shutil.copy2(MODULE_RELEASE, review / "module07-release.json")
    manifest = review / "candidate-manifest.csv"
    write_manifest(manifest, rows)
    tokens = {
        "CANDIDATE_MANIFEST_BYTES": manifest.stat().st_size,
        "CANDIDATE_MANIFEST_SHA256": sha256(manifest),
    }
    for name in REVIEW_RECORDS:
        (review / name).write_text(
            render((record_root / name).read_text(encoding="utf-8"), tokens),
            encoding="utf-8", newline="\n",
        )

    actual = {
        path.relative_to(target).as_posix()
        for path in target.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    expected = {str(row["relative_path"]) for row in rows} | FINAL_FILES
    if actual != expected or len(actual) != 1343:
        raise ValueError("Final checkpoint tree must contain exactly 1,343 expected files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "candidate_files": len(rows), "assembled_files": len(actual),
        "manifest_bytes": tokens["CANDIDATE_MANIFEST_BYTES"],
        "manifest_sha256": tokens["CANDIDATE_MANIFEST_SHA256"],
    }


def build_reference_candidate(target: Path) -> None:
    run(
        [sys.executable, str(MODULE_ASSEMBLER), "--target", str(target), "--reference"],
        "Module 07 reference assembly",
    )


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-final-assemble-") as temp_dir:
        base = Path(temp_dir)
        candidate = base / "candidate"
        build_reference_candidate(candidate)
        first, second, starter = base / "reference-1", base / "reference-2", base / "starter"
        one = assemble(candidate, first, reference=True, hardlink=True)
        assert "REPLACE" not in (first / "final-review/final-decision.md").read_text(encoding="utf-8")
        shutil.rmtree(first)
        two = assemble(candidate, second, reference=True, hardlink=True)
        shutil.rmtree(second)
        learner = assemble(candidate, starter, hardlink=True)
        assert one == two
        assert one["candidate_files"] == 1328 and one["assembled_files"] == 1343
        assert learner["manifest_sha256"] == one["manifest_sha256"]
        assert "REPLACE" in (starter / "final-review/final-decision.md").read_text(encoding="utf-8")
        try:
            assemble(candidate, starter)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Final assembler overwrote an existing target")
        try:
            assemble(candidate, candidate / "inside")
        except ValueError:
            pass
        else:
            raise AssertionError("Final assembler allowed a target inside the candidate")
    print("APP-5 final assembler self-check passed: 1,328 frozen candidate files and 1,343 total files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path)
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
        if args.reference:
            if args.candidate:
                parser.error("--reference cannot be combined with --candidate")
            with tempfile.TemporaryDirectory(prefix="app5-final-reference-") as temp_dir:
                candidate = Path(temp_dir) / "candidate"
                build_reference_candidate(candidate)
                report = assemble(candidate, args.target, reference=True)
        else:
            if not args.candidate:
                parser.error("--candidate is required outside reference mode")
            report = assemble(args.candidate, args.target)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Assembly failed: {error}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
