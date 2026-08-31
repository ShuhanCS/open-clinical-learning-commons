"""Freeze and verify the accepted APP-5 Module 01 reference handoff."""

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
MODULE01 = ROOT.parent / "01-population-health-decision"
EXPECTED_HANDOFF_MANIFEST_SHA256 = "beda2254d019c0969c952773b31fb23db30e2be99798aa8af66d5cb1fbd87a2e"
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "role"]


class HandoffError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HandoffError(message)


def run_module01(script: str, *args: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(MODULE01 / script), *args],
        text=True,
        capture_output=True,
        env=environment,
        check=False,
    )
    if completed.returncode:
        raise HandoffError(completed.stderr.strip() or completed.stdout.strip())


def freeze(target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    require(MODULE01.is_dir(), f"Module 01 package is missing: {MODULE01}")
    with tempfile.TemporaryDirectory(prefix="app5-module02-freeze-") as temp_dir:
        reference = Path(temp_dir) / "module01-reference"
        run_module01("build_workspace.py", "--target", str(reference), "--reference")
        run_module01("validate_workspace.py", str(reference))
        require(sum(path.is_file() for path in reference.rglob("*")) == 27, "Module 01 reference file count changed")
        target.mkdir(parents=True)
        shutil.copytree(reference, target / "module01-reference")
    shutil.copy2(MODULE01 / "release.json", target / "module01-release.json")

    manifest = []
    for path in sorted((path for path in target.rglob("*") if path.is_file()), key=lambda value: value.as_posix()):
        relative = path.relative_to(target).as_posix()
        manifest.append({
            "relative_path": relative,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "role": "accepted Module 01 release record" if relative == "module01-release.json" else "accepted Module 01 reference workspace",
        })
    require(len(manifest) == 28, "Module 01 handoff payload must contain 28 files")
    with (target / "module01-handoff-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    return {
        "payload_files": len(manifest),
        "upstream_files": len(manifest) + 1,
        "manifest_bytes": (target / "module01-handoff-manifest.csv").stat().st_size,
        "manifest_sha256": sha256(target / "module01-handoff-manifest.csv"),
    }


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def verify(root: Path = ROOT) -> dict[str, object]:
    upstream = root.resolve() / "upstream"
    manifest_path = upstream / "module01-handoff-manifest.csv"
    require(manifest_path.is_file(), "Module 01 handoff manifest is missing")
    header, manifest = read_csv(manifest_path)
    require(header == MANIFEST_FIELDS, "Module 01 handoff manifest header changed")
    require(len(manifest) == 28, "Module 01 handoff manifest must contain 28 payload rows")
    require([row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Module 01 handoff manifest is not sorted")
    expected = {row["relative_path"] for row in manifest} | {"module01-handoff-manifest.csv"}
    actual = {path.relative_to(upstream).as_posix() for path in upstream.rglob("*") if path.is_file()}
    require(actual == expected, "Module 01 handoff file set changed")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Unsafe handoff path: {relative}")
        path = upstream / relative
        require(path.stat().st_size == int(row["bytes"]), f"Handoff byte count changed: {relative}")
        require(sha256(path) == row["sha256"], f"Handoff SHA-256 changed: {relative}")
    if EXPECTED_HANDOFF_MANIFEST_SHA256:
        require(sha256(manifest_path) == EXPECTED_HANDOFF_MANIFEST_SHA256, "Module 01 handoff manifest identity changed")

    release = json.loads((upstream / "module01-release.json").read_text(encoding="utf-8"))
    require(release["module_id"] == "oclc-app5-01" and release["module_version"] == "0.1.0", "Module 01 release identity changed")
    require(release["commons_release"] == "0.87.0" and release["status"] == "runnable release candidate", "Module 01 release status changed")
    require(release["public_source_release"]["three_source_intersection"] == 1597, "Module 01 tract intersection changed")
    require(release["reference_decision"]["module02_permission"] == "permitted for curriculum construction", "Module 02 permission changed")
    require(release["reference_decision"]["targeting_or_allocation"] == "prohibited", "Targeting authority changed")

    nested_header, nested_manifest = read_csv(upstream / "module01-reference/release-manifest.csv")
    require(nested_header == MANIFEST_FIELDS and len(nested_manifest) == 16, "Module 01 nested manifest changed")
    return {
        "payload_files": len(manifest),
        "upstream_files": len(actual),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "nested_manifest_rows": len(nested_manifest),
        "reference_files": sum(path.is_file() for path in (upstream / "module01-reference").rglob("*")),
        "three_source_intersection": release["public_source_release"]["three_source_intersection"],
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module02-handoff-") as temp_dir:
        base = Path(temp_dir)
        first = freeze(base / "first")
        second = freeze(base / "second")
        require(first == second, "Two Module 01 freezes differ")
        require((base / "first/module01-handoff-manifest.csv").read_bytes() == (base / "second/module01-handoff-manifest.csv").read_bytes(), "Two handoff manifests differ")
        try:
            freeze(base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Freeze script did not protect an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 02 handoff self-check passed: {json.dumps(committed, sort_keys=True)}")


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
            target = args.target or (ROOT / "upstream")
            print(json.dumps(freeze(target), indent=2, sort_keys=True))
        else:
            print(json.dumps(verify(ROOT), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, HandoffError) as error:
        parser.exit(1, f"Handoff failed: {error}\n")


if __name__ == "__main__":
    main()
