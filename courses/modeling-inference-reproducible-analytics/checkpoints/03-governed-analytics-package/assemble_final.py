"""Freeze an accepted FND-2 Module 07 candidate for final review."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


CHECKPOINT_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = CHECKPOINT_ROOT.parent.parent
MODULE_ROOT = COURSE_ROOT / "modules" / "07-model-cards-governance-defense"
MODULE_ASSEMBLER = MODULE_ROOT / "assemble_candidate.py"
MODULE_VALIDATOR = MODULE_ROOT / "validate_candidate.py"
MODULE_RELEASE = MODULE_ROOT / "release.json"
CHECKPOINT2_RELEASE = COURSE_ROOT / "checkpoints" / "02-validity-forecast-testing-release" / "release.json"
TEMPLATE_ROOT = CHECKPOINT_ROOT / "template"
REFERENCE_ROOT = CHECKPOINT_ROOT / "reference"
REVIEW_RECORDS = (
    "submission-record.md", "final-score.csv", "gate-results.csv", "final-defense.md",
    "reviewer-record.md", "final-reproduction.md", "conditions-register.csv",
    "final-audit.md", "final-decision.md", "release-acceptance.md",
)
FINAL_FILES = {
    "final-review/CHECKPOINT-VERSION",
    "final-review/checkpoint2-release.json",
    "final-review/module07-release.json",
    "final-review/candidate-manifest.csv",
    *(f"final-review/{name}" for name in REVIEW_RECORDS),
}
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]
MODULE_MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]
MODULE_MANIFEST_SHA256 = "ab2537e278ea549b8152434df0a21438394d28caa6031b03e9a570a27db07c1b"
RELEASE_HASHES = {
    "evidence/checkpoint2/prior-checkpoint/release.json": "03c147d2e75cd446a43b9d56e49495df69af90d42d2b14ad4d860aea9d67239f",
}
CHECKPOINT2_RELEASE_SHA256 = "b58316081496f42d473b823fac88ed8e6c981e47afb11d0c4856c9f39627d761"
MODULE_RELEASE_SHA256 = "a2fccdcd096a066337f1de856cb9610f6b389db15c90dff1627af1cbf30ac96e"


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
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Path is not portable: {value}")
    return path


def run_module_validation(candidate: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(MODULE_VALIDATOR), str(candidate)],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise ValueError(f"Module 07 complete validation failed: {result.stderr.strip() or result.stdout.strip()}")


def candidate_inventory(candidate: Path) -> list[dict[str, object]]:
    run_module_validation(candidate)
    fields, immutable = read_csv(candidate / "release-manifest.csv")
    if fields != MODULE_MANIFEST_FIELDS or len(immutable) != 143:
        raise ValueError("Module 07 immutable manifest changed")
    if (candidate / "release-manifest.csv").stat().st_size != 27316 or sha256(candidate / "release-manifest.csv") != MODULE_MANIFEST_SHA256:
        raise ValueError("Module 07 manifest fingerprint changed")
    for relative, digest in RELEASE_HASHES.items():
        if sha256(candidate / relative) != digest:
            raise ValueError(f"Accepted release identity changed: {relative}")
    roles = {row["relative_path"]: row["role"] for row in immutable}
    paths = sorted(path.relative_to(candidate).as_posix() for path in candidate.rglob("*") if path.is_file())
    if len(paths) != 168 or len(set(paths)) != 168:
        raise ValueError("Module 07 candidate must contain exactly 168 unique files")
    return [
        {
            "relative_path": relative,
            "bytes": (candidate / safe_relative(relative)).stat().st_size,
            "sha256": sha256(candidate / safe_relative(relative)),
            "role": roles.get(relative, "Module 07 candidate release record"),
        }
        for relative in paths
    ]


def write_manifest(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def render(text: str, values: dict[str, object]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    if "{{" in text or "}}" in text:
        raise ValueError("An unresolved assembly token remains")
    return text


def assemble(candidate: Path, target: Path, reference: bool = False) -> dict[str, object]:
    candidate, target = candidate.resolve(), target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if target == candidate or candidate in target.parents:
        raise ValueError("Target cannot be the candidate or a folder inside it")
    if not MODULE_RELEASE.is_file() or sha256(MODULE_RELEASE) != MODULE_RELEASE_SHA256:
        raise ValueError("Accepted Module 07 release identity changed")
    if not CHECKPOINT2_RELEASE.is_file() or sha256(CHECKPOINT2_RELEASE) != CHECKPOINT2_RELEASE_SHA256:
        raise ValueError("Accepted Checkpoint 2 release identity changed")
    rows = candidate_inventory(candidate)
    record_root = REFERENCE_ROOT if reference else TEMPLATE_ROOT
    missing = [name for name in REVIEW_RECORDS if not (record_root / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Review records are missing: {', '.join(missing)}")

    target.mkdir(parents=True)
    for row in rows:
        relative = safe_relative(str(row["relative_path"]))
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(candidate / relative, destination)

    review = target / "final-review"
    review.mkdir()
    shutil.copy2(CHECKPOINT_ROOT / "VERSION", review / "CHECKPOINT-VERSION")
    shutil.copy2(CHECKPOINT2_RELEASE, review / "checkpoint2-release.json")
    shutil.copy2(MODULE_RELEASE, review / "module07-release.json")
    manifest = review / "candidate-manifest.csv"
    write_manifest(manifest, rows)
    values = {
        "CANDIDATE_MANIFEST_BYTES": manifest.stat().st_size,
        "CANDIDATE_MANIFEST_SHA256": sha256(manifest),
    }
    for name in REVIEW_RECORDS:
        text = render((record_root / name).read_text(encoding="utf-8"), values)
        (review / name).write_text(text, encoding="utf-8", newline="\n")

    actual = {path.relative_to(target).as_posix() for path in target.rglob("*") if path.is_file()}
    expected = {str(row["relative_path"]) for row in rows} | FINAL_FILES
    if actual != expected or len(actual) != 182:
        raise ValueError("Final checkpoint tree must contain exactly 182 expected files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "candidate_files": len(rows), "assembled_files": len(actual),
        "manifest_bytes": values["CANDIDATE_MANIFEST_BYTES"],
        "manifest_sha256": values["CANDIDATE_MANIFEST_SHA256"],
    }


def assemble_reference_candidate(target: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(MODULE_ASSEMBLER), str(target), "--reference"],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise ValueError(f"Module 07 reference assembly failed: {result.stderr.strip() or result.stdout.strip()}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd2-final-assemble-") as temp_dir:
        base = Path(temp_dir)
        candidate = base / "candidate"
        assemble_reference_candidate(candidate)
        first, second, starter = base / "reference-1", base / "reference-2", base / "starter"
        report = assemble(candidate, first, reference=True)
        second_report = assemble(candidate, second, reference=True)
        starter_report = assemble(candidate, starter)
        assert report["candidate_files"] == 168 and report["assembled_files"] == 182
        assert report["manifest_sha256"] == second_report["manifest_sha256"]
        assert starter_report["mode"] == "learner"
        assert "REPLACE" in (starter / "final-review/submission-record.md").read_text(encoding="utf-8")
        assert "{{" not in (starter / "final-review/submission-record.md").read_text(encoding="utf-8")
        try:
            assemble(candidate, first, reference=True)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Assembler did not protect an existing target")
    print("FND-2 final assembler self-check passed: 168 frozen candidate files and 182 total files.")


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
            with tempfile.TemporaryDirectory(prefix="fnd2-final-reference-") as temp_dir:
                candidate = Path(temp_dir) / "candidate"
                assemble_reference_candidate(candidate)
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
