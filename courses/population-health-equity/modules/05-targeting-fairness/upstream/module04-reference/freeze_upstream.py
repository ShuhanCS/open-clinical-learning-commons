"""Freeze and verify the accepted APP-5 Week 3 checkpoint handoff."""

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


ROOT = Path(__file__).resolve().parent
CHECKPOINT = ROOT.parent.parent / "checkpoints/01-measures-disparities-readiness"
EXPECTED_HANDOFF_MANIFEST_SHA256 = "db70b4e20a17fbddd2b49f7647dd9ce5bcd064e01af5e7a7e23df9122889914e"
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]


class HandoffError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HandoffError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_checkpoint(script: str, *args: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(CHECKPOINT / script), *args],
        text=True,
        capture_output=True,
        env=environment,
        check=False,
    )
    if completed.returncode:
        raise HandoffError(completed.stderr.strip() or completed.stdout.strip())


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def freeze(target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    require(CHECKPOINT.is_dir(), f"Checkpoint package is missing: {CHECKPOINT}")
    with tempfile.TemporaryDirectory(prefix="app5-module04-freeze-") as temporary:
        reference = Path(temporary) / "checkpoint-reference"
        run_checkpoint("build_checkpoint.py", "--target", str(reference), "--reference")
        run_checkpoint("validate_checkpoint.py", str(reference))
        require(
            sum(path.is_file() for path in reference.rglob("*") if "__pycache__" not in path.parts) == 240,
            "Checkpoint reference file count changed",
        )
        target.mkdir(parents=True)
        shutil.copytree(reference, target / "checkpoint-reference")

    manifest: list[dict[str, object]] = []
    reference_root = target / "checkpoint-reference"
    for path in sorted(
        (path for path in reference_root.rglob("*") if path.is_file() and "__pycache__" not in path.parts),
        key=lambda value: value.as_posix(),
    ):
        relative = path.relative_to(target).as_posix()
        manifest.append(
            {
                "relative_path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "role": (
                    "accepted checkpoint candidate artifact"
                    if "/candidate/" in f"/{relative}"
                    else "accepted checkpoint control or review record"
                ),
            }
        )
    require(len(manifest) == 240, "Checkpoint handoff payload must contain 240 files")
    manifest_path = target / "checkpoint-handoff-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    return {
        "payload_files": len(manifest),
        "upstream_files": len(manifest) + 1,
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "candidate_files": 219,
        "reference_files": 240,
    }


def verify(root: Path = ROOT) -> dict[str, object]:
    upstream = root.resolve() / "upstream"
    manifest_path = upstream / "checkpoint-handoff-manifest.csv"
    require(manifest_path.is_file(), "Checkpoint handoff manifest is missing")
    header, manifest = read_csv(manifest_path)
    require(header == MANIFEST_FIELDS, "Checkpoint handoff manifest header changed")
    require(len(manifest) == 240, "Checkpoint handoff manifest must contain 240 payload rows")
    require(
        [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest),
        "Checkpoint handoff manifest is not sorted",
    )
    expected = {row["relative_path"] for row in manifest} | {"checkpoint-handoff-manifest.csv"}
    actual = {
        path.relative_to(upstream).as_posix()
        for path in upstream.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == expected, "Checkpoint handoff file set changed")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Unsafe handoff path: {relative}")
        path = upstream / relative
        require(path.stat().st_size == int(row["bytes"]), f"Handoff byte count changed: {relative}")
        require(sha256(path) == row["sha256"], f"Handoff SHA-256 changed: {relative}")
    if EXPECTED_HANDOFF_MANIFEST_SHA256:
        require(
            sha256(manifest_path) == EXPECTED_HANDOFF_MANIFEST_SHA256,
            "Checkpoint handoff manifest identity changed",
        )

    reference = upstream / "checkpoint-reference"
    release = json.loads((reference / "release.json").read_text(encoding="utf-8"))
    contract = json.loads((reference / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(
        release["checkpoint"]["id"] == "oclc-app5-cp01"
        and release["checkpoint"]["version"] == "0.1.0"
        and release["checkpoint"]["commons_release"] == "0.90.0",
        "Checkpoint release identity changed",
    )
    require(
        contract["accepted_component_files"] == 219
        and contract["accepted_immutable_rows"] == 177,
        "Checkpoint candidate identity changed",
    )
    require(
        release["accepted_evidence"]["checkpoint_score"] == "40 of 40"
        and release["progression"]["module04_permission"] == "permitted for curriculum construction",
        "Checkpoint progression authority changed",
    )
    require(
        release["progression"]["module05_permission"] == "prohibited until Module 04 passes"
        and release["progression"]["deployment"] == "prohibited",
        "Checkpoint downstream boundary changed",
    )
    candidate_header, candidate = read_csv(reference / "candidate-manifest.csv")
    require(
        candidate_header
        == ["relative_path", "bytes", "sha256", "source_module", "source_version", "role"]
        and len(candidate) == 219,
        "Checkpoint candidate manifest changed",
    )
    return {
        "payload_files": len(manifest),
        "upstream_files": len(actual),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "candidate_files": len(candidate),
        "reference_files": sum(path.is_file() for path in reference.rglob("*")),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module04-handoff-") as temporary:
        base = Path(temporary)
        first = freeze(base / "first")
        second = freeze(base / "second")
        require(first == second, "Two checkpoint freezes differ")
        require(
            (base / "first/checkpoint-handoff-manifest.csv").read_bytes()
            == (base / "second/checkpoint-handoff-manifest.csv").read_bytes(),
            "Two checkpoint handoff manifests differ",
        )
        try:
            freeze(base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Freeze script did not protect an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 04 handoff self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.write:
            print(json.dumps(freeze(args.target or (ROOT / "upstream")), indent=2, sort_keys=True))
        else:
            print(json.dumps(verify(ROOT), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, HandoffError) as error:
        parser.exit(1, f"Handoff failed: {error}\n")


if __name__ == "__main__":
    main()
