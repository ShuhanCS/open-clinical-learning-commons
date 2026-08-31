"""Freeze and verify the accepted APP-5 Module 02 reference handoff."""

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
MODULE02 = ROOT.parent / "02-population-measures-linked-data"
EXPECTED_HANDOFF_MANIFEST_SHA256 = "f5e84b251143edeb65b68d816a57492755083d8bc57c73e6bdaede381b933ef1"
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


def run_module02(script: str, *args: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(MODULE02 / script), *args],
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
    require(MODULE02.is_dir(), f"Module 02 package is missing: {MODULE02}")
    with tempfile.TemporaryDirectory(prefix="app5-module03-freeze-") as temp_dir:
        reference = Path(temp_dir) / "module02-reference"
        run_module02("build_workspace.py", "--target", str(reference), "--reference")
        run_module02("validate_workspace.py", str(reference))
        require(sum(path.is_file() for path in reference.rglob("*")) == 72, "Module 02 reference file count changed")
        target.mkdir(parents=True)
        shutil.copytree(reference, target / "module02-reference")
    shutil.copy2(MODULE02 / "release.json", target / "module02-release.json")

    manifest = []
    for path in sorted((path for path in target.rglob("*") if path.is_file()), key=lambda value: value.as_posix()):
        relative = path.relative_to(target).as_posix()
        manifest.append({
            "relative_path": relative,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "role": "accepted Module 02 release record" if relative == "module02-release.json" else "accepted Module 02 reference workspace",
        })
    require(len(manifest) == 73, "Module 02 handoff payload must contain 73 files")
    manifest_path = target / "module02-handoff-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    return {
        "payload_files": len(manifest),
        "upstream_files": len(manifest) + 1,
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
    }


def verify(root: Path = ROOT) -> dict[str, object]:
    upstream = root.resolve() / "upstream"
    manifest_path = upstream / "module02-handoff-manifest.csv"
    require(manifest_path.is_file(), "Module 02 handoff manifest is missing")
    header, manifest = read_csv(manifest_path)
    require(header == MANIFEST_FIELDS, "Module 02 handoff manifest header changed")
    require(len(manifest) == 73, "Module 02 handoff manifest must contain 73 payload rows")
    require([row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Module 02 handoff manifest is not sorted")
    expected = {row["relative_path"] for row in manifest} | {"module02-handoff-manifest.csv"}
    actual = {path.relative_to(upstream).as_posix() for path in upstream.rglob("*") if path.is_file()}
    require(actual == expected, "Module 02 handoff file set changed")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Unsafe handoff path: {relative}")
        path = upstream / relative
        require(path.stat().st_size == int(row["bytes"]), f"Handoff byte count changed: {relative}")
        require(sha256(path) == row["sha256"], f"Handoff SHA-256 changed: {relative}")
    if EXPECTED_HANDOFF_MANIFEST_SHA256:
        require(sha256(manifest_path) == EXPECTED_HANDOFF_MANIFEST_SHA256, "Module 02 handoff manifest identity changed")

    release = json.loads((upstream / "module02-release.json").read_text(encoding="utf-8"))
    require(release["module_id"] == "oclc-app5-02" and release["module_version"] == "0.1.0", "Module 02 release identity changed")
    require(release["commons_release"] == "0.88.0" and release["status"] == "runnable release candidate", "Module 02 release status changed")
    require(release["source_release"]["adult_denominator"] == 5679768 and release["source_release"]["synthetic_events"] == 283614, "Module 02 accepted totals changed")
    require(release["reference_decision"]["module03_permission"] == "permitted for curriculum construction", "Module 03 permission changed")
    require(release["reference_decision"]["tract_ranking"] == "prohibited" and release["reference_decision"]["deployment"] == "prohibited", "Module 02 authority changed")

    nested_header, nested_manifest = read_csv(upstream / "module02-reference/release-manifest.csv")
    require(nested_header == MANIFEST_FIELDS and len(nested_manifest) == 57, "Module 02 nested manifest changed")
    return {
        "payload_files": len(manifest),
        "upstream_files": len(actual),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "nested_manifest_rows": len(nested_manifest),
        "reference_files": sum(path.is_file() for path in (upstream / "module02-reference").rglob("*")),
        "adult_denominator": release["source_release"]["adult_denominator"],
        "synthetic_events": release["source_release"]["synthetic_events"],
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module03-handoff-") as temp_dir:
        base = Path(temp_dir)
        first = freeze(base / "first")
        second = freeze(base / "second")
        require(first == second, "Two Module 02 freezes differ")
        require((base / "first/module02-handoff-manifest.csv").read_bytes() == (base / "second/module02-handoff-manifest.csv").read_bytes(), "Two handoff manifests differ")
        try:
            freeze(base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Freeze script did not protect an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 03 handoff self-check passed: {json.dumps(committed, sort_keys=True)}")


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
