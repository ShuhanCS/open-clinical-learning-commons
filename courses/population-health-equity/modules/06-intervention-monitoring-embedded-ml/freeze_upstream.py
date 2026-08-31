"""Freeze and verify the accepted APP-5 Module 05 reference handoff."""

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
MODULE05 = ROOT.parent / "05-targeting-fairness"
EXPECTED_HANDOFF_MANIFEST_SHA256 = "0ab8cc15d252ef91436aa1b281f316e4eb21115aefc668a0930d04c90397a828"
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


def run_module05(script: str, *args: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(MODULE05 / script), *args],
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
    require(MODULE05.is_dir(), f"Module 05 package is missing: {MODULE05}")
    with tempfile.TemporaryDirectory(prefix="app5-module06-freeze-") as temporary:
        reference = Path(temporary) / "module05-reference"
        run_module05("build_workspace.py", "--target", str(reference), "--reference")
        run_module05("validate_workspace.py", str(reference))
        files = sum(path.is_file() for path in reference.rglob("*") if "__pycache__" not in path.parts)
        require(files == 340, "Module 05 reference file count changed")
        target.mkdir(parents=True)
        shutil.copytree(reference, target / "module05-reference")

    manifest: list[dict[str, object]] = []
    reference_root = target / "module05-reference"
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
                    "accepted Module 05 upstream handoff"
                    if "/upstream/" in f"/{relative}"
                    else "accepted Module 05 source, output, control, or review record"
                ),
            }
        )
    require(len(manifest) == 340, "Module 05 handoff payload must contain 340 files")
    manifest_path = target / "module05-handoff-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    return {
        "payload_files": len(manifest),
        "upstream_files": len(manifest) + 1,
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "reference_files": 340,
        "reference_manifest_rows": 318,
    }


def verify(root: Path = ROOT) -> dict[str, object]:
    upstream = root.resolve() / "upstream"
    manifest_path = upstream / "module05-handoff-manifest.csv"
    require(manifest_path.is_file(), "Module 05 handoff manifest is missing")
    header, manifest = read_csv(manifest_path)
    require(header == MANIFEST_FIELDS, "Module 05 handoff manifest header changed")
    require(len(manifest) == 340, "Module 05 handoff manifest must contain 340 payload rows")
    require(
        [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest),
        "Module 05 handoff manifest is not sorted",
    )
    expected = {row["relative_path"] for row in manifest} | {"module05-handoff-manifest.csv"}
    actual = {
        path.relative_to(upstream).as_posix()
        for path in upstream.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == expected, "Module 05 handoff file set changed")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Unsafe handoff path: {relative}")
        path = upstream / relative
        require(path.stat().st_size == int(row["bytes"]), f"Handoff byte count changed: {relative}")
        require(sha256(path) == row["sha256"], f"Handoff SHA-256 changed: {relative}")
    if EXPECTED_HANDOFF_MANIFEST_SHA256:
        require(sha256(manifest_path) == EXPECTED_HANDOFF_MANIFEST_SHA256, "Module 05 handoff identity changed")

    reference = upstream / "module05-reference"
    release = json.loads((reference / "release.json").read_text(encoding="utf-8"))
    contract = json.loads((reference / "targeting-contract.json").read_text(encoding="utf-8"))
    require(
        release["module_id"] == "oclc-app5-05"
        and release["module_version"] == "0.1.0"
        and release["commons_release"] == "0.92.0",
        "Module 05 release identity changed",
    )
    require(
        contract["workspace"]["reference_files"] == 340
        and contract["workspace"]["reference_manifest_rows"] == 318,
        "Module 05 workspace identity changed",
    )
    require(
        release["reference_decision"]["score"] == 15
        and release["reference_decision"]["gates_passed"] == 26
        and release["reference_decision"]["module06_permission"] == "permitted for curriculum construction",
        "Module 05 progression authority changed",
    )
    require(
        release["reference_decision"]["planning_candidate"].startswith("community-review rule")
        and release["reference_decision"]["week6_checkpoint_permission"].startswith("not yet")
        and release["reference_decision"]["deployment"] == "prohibited",
        "Module 05 downstream boundary changed",
    )
    return {
        "payload_files": len(manifest),
        "upstream_files": len(actual),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "reference_files": sum(path.is_file() for path in reference.rglob("*")),
        "reference_manifest_rows": sum(
            1 for _ in csv.DictReader((reference / "release-manifest.csv").open(encoding="utf-8", newline=""))
        ),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module06-handoff-") as temporary:
        base = Path(temporary)
        first = freeze(base / "first")
        second = freeze(base / "second")
        require(first == second, "Two Module 05 freezes differ")
        require(
            (base / "first/module05-handoff-manifest.csv").read_bytes()
            == (base / "second/module05-handoff-manifest.csv").read_bytes(),
            "Two Module 05 handoff manifests differ",
        )
        try:
            freeze(base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Freeze script did not protect an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 06 handoff self-check passed: {json.dumps(committed, sort_keys=True)}")


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
