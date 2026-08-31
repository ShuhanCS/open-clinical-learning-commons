"""Acquire and verify the accepted APP-5 Module 04 TIGER/Line archive."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent
SOURCE_URL = "https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_25_tract.zip"
EXPECTED_BYTES = 4_506_627
EXPECTED_SHA256 = "74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4"
EXPECTED_MEMBERS = (
    "tl_2024_25_tract.cpg",
    "tl_2024_25_tract.dbf",
    "tl_2024_25_tract.prj",
    "tl_2024_25_tract.shp",
    "tl_2024_25_tract.shp.ea.iso.xml",
    "tl_2024_25_tract.shp.iso.xml",
    "tl_2024_25_tract.shx",
)
MANIFEST_FIELDS = ["relative_path", "bytes", "sha256", "source_url", "role"]


class SourceError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SourceError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def bytes_sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def inspect_archive(path: Path) -> list[dict[str, object]]:
    require(path.stat().st_size == EXPECTED_BYTES, "TIGER archive byte count changed")
    require(sha256(path) == EXPECTED_SHA256, "TIGER archive SHA-256 changed")
    with zipfile.ZipFile(path) as archive:
        members = sorted(archive.namelist())
        require(tuple(members) == EXPECTED_MEMBERS, "TIGER archive member inventory changed")
        rows: list[dict[str, object]] = []
        for name in members:
            relative = PurePosixPath(name)
            require(
                not relative.is_absolute() and ".." not in relative.parts,
                f"Unsafe TIGER archive member: {name}",
            )
            payload = archive.read(name)
            rows.append(
                {
                    "relative_path": f"archive/{name}",
                    "bytes": len(payload),
                    "sha256": bytes_sha256(payload),
                    "source_url": SOURCE_URL,
                    "role": "decompressed official TIGER/Line archive member",
                }
            )
    return rows


def write_manifest(path: Path, archive_path: Path) -> dict[str, object]:
    member_rows = inspect_archive(archive_path)
    rows = [
        {
            "relative_path": f"raw/{archive_path.name}",
            "bytes": archive_path.stat().st_size,
            "sha256": sha256(archive_path),
            "source_url": SOURCE_URL,
            "role": "complete official 2024 TIGER/Line Massachusetts tract archive",
        },
        *member_rows,
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return {
        "archive_bytes": archive_path.stat().st_size,
        "archive_sha256": sha256(archive_path),
        "archive_members": len(member_rows),
        "manifest_rows": len(rows),
        "manifest_bytes": path.stat().st_size,
        "manifest_sha256": sha256(path),
    }


def acquire(target: Path, manifest: Path, source: Path | None = None) -> dict[str, object]:
    target = target.resolve()
    manifest = manifest.resolve()
    if target.exists() or manifest.exists():
        raise FileExistsError("Refusing to overwrite an existing source or manifest")
    target.parent.mkdir(parents=True, exist_ok=True)
    manifest.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".partial")
    if temporary.exists():
        raise FileExistsError(f"Refusing to overwrite partial source: {temporary}")
    try:
        if source is not None:
            source = source.resolve()
            require(source.is_file(), f"Local source is missing: {source}")
            shutil.copyfile(source, temporary)
        else:
            request = urllib.request.Request(
                SOURCE_URL,
                headers={"User-Agent": "Open-Clinical-Learning-Commons/0.91.0"},
            )
            with urllib.request.urlopen(request, timeout=120) as response, temporary.open("wb") as handle:
                require(response.status == 200, f"TIGER download returned HTTP {response.status}")
                shutil.copyfileobj(response, handle)
        inspect_archive(temporary)
        temporary.replace(target)
        report = write_manifest(manifest, target)
    except Exception:
        temporary.unlink(missing_ok=True)
        target.unlink(missing_ok=True)
        manifest.unlink(missing_ok=True)
        raise
    return report


def verify(root: Path = ROOT) -> dict[str, object]:
    archive = root / "data/raw/tl_2024_25_tract.zip"
    manifest = root / "data/source-manifest.csv"
    require(archive.is_file(), "Committed TIGER archive is missing")
    require(manifest.is_file(), "Committed source manifest is missing")
    with tempfile.TemporaryDirectory(prefix="app5-module04-source-verify-") as temporary:
        generated = Path(temporary) / "source-manifest.csv"
        report = write_manifest(generated, archive)
        require(generated.read_bytes() == manifest.read_bytes(), "Committed source manifest changed")
    return report


def self_check() -> None:
    committed = ROOT / "data/raw/tl_2024_25_tract.zip"
    require(committed.is_file(), "Run source acquisition before the self-check")
    with tempfile.TemporaryDirectory(prefix="app5-module04-source-") as temporary:
        base = Path(temporary)
        one = acquire(base / "one/tl_2024_25_tract.zip", base / "one/source-manifest.csv", committed)
        two = acquire(base / "two/tl_2024_25_tract.zip", base / "two/source-manifest.csv", committed)
        require(one == two, "Two source acquisitions differ")
        require(
            (base / "one/source-manifest.csv").read_bytes()
            == (base / "two/source-manifest.csv").read_bytes(),
            "Two source manifests differ",
        )
        try:
            acquire(base / "one/tl_2024_25_tract.zip", base / "one/again.csv", committed)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Source acquisition overwrote an existing target")
        changed = base / "changed.zip"
        shutil.copyfile(committed, changed)
        payload = bytearray(changed.read_bytes())
        payload[-1] ^= 1
        changed.write_bytes(payload)
        try:
            acquire(base / "bad/tl_2024_25_tract.zip", base / "bad/source-manifest.csv", changed)
        except SourceError:
            pass
        else:
            raise AssertionError("Source acquisition accepted changed archive bytes")
    verified = verify(ROOT)
    print(f"APP-5 Module 04 source self-check passed: {json.dumps(verified, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.verify:
            print(json.dumps(verify(ROOT), indent=2, sort_keys=True))
        elif args.target and args.manifest:
            print(json.dumps(acquire(args.target, args.manifest, args.source), indent=2, sort_keys=True))
        else:
            parser.error("use --self-check, --verify, or provide --target and --manifest")
    except (OSError, ValueError, zipfile.BadZipFile, SourceError) as error:
        parser.exit(1, f"Source acquisition failed: {error}\n")


if __name__ == "__main__":
    main()
