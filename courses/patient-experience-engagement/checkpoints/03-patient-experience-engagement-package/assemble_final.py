"""Freeze an accepted APP-2 Module 07 candidate for final review."""

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
MODULE_ROOT = COURSE_ROOT / "modules/07-clinician-patient-leadership-defense"
MODULE_ASSEMBLER = MODULE_ROOT / "assemble_candidate.py"
MODULE_VALIDATOR = MODULE_ROOT / "validate_candidate.py"
MODULE_RELEASE = MODULE_ROOT / "release.json"
CP1_RELEASE = COURSE_ROOT / "checkpoints/01-measurement-representation-readiness/release.json"
CP2_RELEASE = COURSE_ROOT / "checkpoints/02-linked-evidence-patient-voice-release/release.json"
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
MODULE_MANIFEST_BYTES = 64149
MODULE_MANIFEST_SHA256 = "53bd306692145df85d1b2a709615000f80829099a916659c6a8cfd3bd994697f"
MODULE_RELEASE_SHA256 = "2a30f59869be0041b813ce6005c226a9bcd3cd28632222464a5defc1586ca317"
CP1_RELEASE_SHA256 = "44f189a6225a1ed72fee70fa7366cc6dfd2ab5952c1ddcd8304fff5ea89a0137"
CP2_RELEASE_SHA256 = "7684d17f2441883cdcd87521e5376b133bf7d85dc0513f655770c18f19edb60c"


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
    result = subprocess.run([sys.executable, str(MODULE_VALIDATOR), str(candidate)], capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError(f"Module 07 validation failed: {result.stderr.strip() or result.stdout.strip()}")


def candidate_inventory(candidate: Path) -> list[dict[str, object]]:
    run_module_validation(candidate)
    fields, immutable = read_csv(candidate / "release-manifest.csv")
    if fields != MODULE_MANIFEST_FIELDS or len(immutable) != 334:
        raise ValueError("Module 07 immutable manifest changed")
    manifest = candidate / "release-manifest.csv"
    if manifest.stat().st_size != MODULE_MANIFEST_BYTES or sha256(manifest) != MODULE_MANIFEST_SHA256:
        raise ValueError("Module 07 manifest fingerprint changed")
    roles = {row["relative_path"]: row["role"] for row in immutable}
    paths = sorted(path.relative_to(candidate).as_posix() for path in candidate.rglob("*") if path.is_file() and "__pycache__" not in path.parts)
    if len(paths) != 358 or len(set(paths)) != 358:
        raise ValueError("Module 07 candidate must contain exactly 358 unique files")
    return [{
        "relative_path": relative,
        "bytes": (candidate / safe_relative(relative)).stat().st_size,
        "sha256": sha256(candidate / safe_relative(relative)),
        "role": roles.get(relative, "Module 07 clinician and patient leadership record"),
    } for relative in paths]


def write_manifest(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FINAL_MANIFEST_FIELDS, lineterminator="\n")
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
    release_checks = (
        (MODULE_RELEASE, MODULE_RELEASE_SHA256, "Module 07"),
        (CP1_RELEASE, CP1_RELEASE_SHA256, "Checkpoint 01"),
        (CP2_RELEASE, CP2_RELEASE_SHA256, "Checkpoint 02"),
    )
    for path, digest, label in release_checks:
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
        shutil.copy2(candidate / relative, destination)

    review = target / "final-review"
    review.mkdir()
    shutil.copy2(CHECKPOINT_ROOT / "VERSION", review / "CHECKPOINT-VERSION")
    shutil.copy2(CP1_RELEASE, review / "checkpoint1-release.json")
    shutil.copy2(CP2_RELEASE, review / "checkpoint2-release.json")
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

    actual = {path.relative_to(target).as_posix() for path in target.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    expected = {str(row["relative_path"]) for row in rows} | FINAL_FILES
    if actual != expected or len(actual) != 373:
        raise ValueError("Final checkpoint tree must contain exactly 373 expected files")
    return {
        "status": "pass", "mode": "reference" if reference else "learner",
        "candidate_files": len(rows), "assembled_files": len(actual),
        "manifest_bytes": values["CANDIDATE_MANIFEST_BYTES"],
        "manifest_sha256": values["CANDIDATE_MANIFEST_SHA256"],
    }


def build_reference_candidate(target: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(MODULE_ASSEMBLER), "--target", str(target), "--reference"],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise ValueError(f"Module 07 reference assembly failed: {result.stderr.strip() or result.stdout.strip()}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-final-assemble-") as temp_dir:
        base = Path(temp_dir)
        candidate = base / "candidate"
        build_reference_candidate(candidate)
        first, second, starter = base / "reference-1", base / "reference-2", base / "starter"
        one = assemble(candidate, first, reference=True)
        two = assemble(candidate, second, reference=True)
        learner = assemble(candidate, starter)
        assert one == two
        assert one["candidate_files"] == 358 and one["assembled_files"] == 373
        assert learner["manifest_sha256"] == one["manifest_sha256"]
        assert "REPLACE" not in (first / "final-review/final-decision.md").read_text(encoding="utf-8")
        assert "REPLACE" in (starter / "final-review/final-decision.md").read_text(encoding="utf-8")
        try:
            assemble(candidate, first, reference=True)
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
    print("APP-2 final assembler self-check passed: 358 frozen candidate files and 373 total files.")


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
            with tempfile.TemporaryDirectory(prefix="app2-final-reference-") as temp_dir:
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
