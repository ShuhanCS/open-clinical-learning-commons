"""Freeze and verify the accepted APP-5 Module 04 reference handoff."""

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
MODULE04 = ROOT.parent / "04-place-evidence-geographic-reasoning"
EXPECTED_HANDOFF_MANIFEST_SHA256 = "0670760f650e0d13cfd4c5dc85ab26fdce5779cc86d35b3d3c27d6a3cc7738dd"
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


def run_module04(script: str, *args: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(MODULE04 / script), *args],
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
    require(MODULE04.is_dir(), f"Module 04 package is missing: {MODULE04}")
    with tempfile.TemporaryDirectory(prefix="app5-module05-freeze-") as temporary:
        reference = Path(temporary) / "module04-reference"
        run_module04("build_workspace.py", "--target", str(reference), "--reference")
        run_module04("validate_workspace.py", str(reference))
        files = sum(path.is_file() for path in reference.rglob("*") if "__pycache__" not in path.parts)
        require(files == 287, "Module 04 reference file count changed")
        target.mkdir(parents=True)
        shutil.copytree(reference, target / "module04-reference")

    manifest: list[dict[str, object]] = []
    reference_root = target / "module04-reference"
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
                    "accepted Module 04 upstream handoff"
                    if "/upstream/" in f"/{relative}"
                    else "accepted Module 04 source, output, control, or review record"
                ),
            }
        )
    require(len(manifest) == 287, "Module 04 handoff payload must contain 287 files")
    manifest_path = target / "module04-handoff-manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    return {
        "payload_files": len(manifest),
        "upstream_files": len(manifest) + 1,
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "reference_files": 287,
        "reference_manifest_rows": 271,
    }


def verify(root: Path = ROOT) -> dict[str, object]:
    upstream = root.resolve() / "upstream"
    manifest_path = upstream / "module04-handoff-manifest.csv"
    require(manifest_path.is_file(), "Module 04 handoff manifest is missing")
    header, manifest = read_csv(manifest_path)
    require(header == MANIFEST_FIELDS, "Module 04 handoff manifest header changed")
    require(len(manifest) == 287, "Module 04 handoff manifest must contain 287 payload rows")
    require(
        [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest),
        "Module 04 handoff manifest is not sorted",
    )
    expected = {row["relative_path"] for row in manifest} | {"module04-handoff-manifest.csv"}
    actual = {
        path.relative_to(upstream).as_posix()
        for path in upstream.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == expected, "Module 04 handoff file set changed")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Unsafe handoff path: {relative}")
        path = upstream / relative
        require(path.stat().st_size == int(row["bytes"]), f"Handoff byte count changed: {relative}")
        require(sha256(path) == row["sha256"], f"Handoff SHA-256 changed: {relative}")
    if EXPECTED_HANDOFF_MANIFEST_SHA256:
        require(sha256(manifest_path) == EXPECTED_HANDOFF_MANIFEST_SHA256, "Module 04 handoff identity changed")

    reference = upstream / "module04-reference"
    release = json.loads((reference / "release.json").read_text(encoding="utf-8"))
    contract = json.loads((reference / "geography-contract.json").read_text(encoding="utf-8"))
    require(
        release["module_id"] == "oclc-app5-04"
        and release["module_version"] == "0.1.0"
        and release["commons_release"] == "0.91.0",
        "Module 04 release identity changed",
    )
    require(
        contract["workspace"]["reference_files"] == 287
        and contract["workspace"]["reference_manifest_rows"] == 271,
        "Module 04 workspace identity changed",
    )
    require(
        release["reference_decision"]["score"] == 10
        and release["reference_decision"]["gates_passed"] == 22
        and release["reference_decision"]["module05_permission"] == "permitted for curriculum construction",
        "Module 04 progression authority changed",
    )
    require(
        release["reference_decision"]["week6_checkpoint_permission"].startswith("not yet")
        and release["reference_decision"]["deployment"] == "prohibited",
        "Module 04 downstream boundary changed",
    )
    return {
        "payload_files": len(manifest),
        "upstream_files": len(actual),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "reference_files": sum(path.is_file() for path in reference.rglob("*")),
        "reference_manifest_rows": sum(1 for _ in csv.DictReader((reference / "release-manifest.csv").open(encoding="utf-8", newline=""))),
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module05-handoff-") as temporary:
        base = Path(temporary)
        first = freeze(base / "first")
        second = freeze(base / "second")
        require(first == second, "Two Module 04 freezes differ")
        require(
            (base / "first/module04-handoff-manifest.csv").read_bytes()
            == (base / "second/module04-handoff-manifest.csv").read_bytes(),
            "Two Module 04 handoff manifests differ",
        )
        try:
            freeze(base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Freeze script did not protect an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 05 handoff self-check passed: {json.dumps(committed, sort_keys=True)}")


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
