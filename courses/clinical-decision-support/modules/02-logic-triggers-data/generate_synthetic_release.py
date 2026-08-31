"""Generate or verify the APP-4 Module 02 synthetic FHIR R4 source release."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import shutil
import subprocess
import tempfile
import urllib.request
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "synthea.properties"
POPULATION = 1000
RANDOM_SEED = 7400202
CLINICIAN_SEED = 7400203
REFERENCE_DATE = "20260831"
AGE_RANGE = "18-89"
STATE = "Massachusetts"
SYNTHEA = {
    "name": "synthea-with-dependencies-4.0.0.jar",
    "version": "4.0.0",
    "url": "https://github.com/synthetichealth/synthea/releases/download/v4.0.0/synthea-with-dependencies.jar",
    "bytes": 201164144,
    "sha256": "ed43c20ad40ba5c3bc724503a5af032715fe3c491620b766148e7c2361e6ecc1",
}
JAVA = {
    "name": "OpenJDK17U-jre_x64_windows_hotspot_17.0.20.1_1.zip",
    "version": "Temurin 17.0.20.1+1",
    "url": "https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.20.1%2B1/OpenJDK17U-jre_x64_windows_hotspot_17.0.20.1_1.zip",
    "bytes": 43780109,
    "sha256": "bc21a93923103cdaac93ee337b0ae4365e739fde36df823dd456bc67c8a9d352",
}
MANIFEST_FIELDS = [
    "relative_path", "resource_type", "rows", "unique_ids", "duplicate_ids",
    "parse_failures", "uncompressed_bytes", "compressed_bytes", "sha256",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_input(path: Path, contract: dict[str, object]) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.stat().st_size != contract["bytes"] or sha256(path) != contract["sha256"]:
        raise ValueError(f"Build input identity mismatch: {path.name}")


def acquire(cache: Path) -> None:
    cache.mkdir(parents=True, exist_ok=True)
    for contract in (SYNTHEA, JAVA):
        target = cache / str(contract["name"])
        if not target.exists():
            request = urllib.request.Request(
                str(contract["url"]), headers={"User-Agent": "OpenClinicalLearningCommons/0.78.0"}
            )
            with urllib.request.urlopen(request) as response, target.open("wb") as handle:
                shutil.copyfileobj(response, handle)
        verify_input(target, contract)


def normalize_ndjson(source: Path, target: Path) -> dict[str, object]:
    target.parent.mkdir(parents=True, exist_ok=True)
    ids: list[str] = []
    types: Counter[str] = Counter()
    rows = failures = normalized_bytes = 0
    with source.open("r", encoding="cp1252") as incoming, target.open("wb") as outgoing:
        with gzip.GzipFile(filename="", mode="wb", fileobj=outgoing, mtime=0) as compressed:
            for line in incoming:
                rows += 1
                try:
                    resource = json.loads(line)
                    types[str(resource.get("resourceType", ""))] += 1
                    ids.append(str(resource.get("id", "")))
                    normalized = (
                        json.dumps(resource, ensure_ascii=False, separators=(",", ":")) + "\n"
                    ).encode("utf-8")
                    compressed.write(normalized)
                    normalized_bytes += len(normalized)
                except (json.JSONDecodeError, AttributeError):
                    failures += 1
    resource_type = next(iter(types)) if len(types) == 1 else "mixed"
    return {
        "resource_type": resource_type,
        "rows": rows,
        "unique_ids": len(set(ids)),
        "duplicate_ids": len(ids) - len(set(ids)),
        "parse_failures": failures,
        "uncompressed_bytes": normalized_bytes,
    }


def normalize_json(source: Path, target: Path) -> dict[str, object]:
    with source.open("r", encoding="cp1252") as handle:
        resource = json.load(handle)
    normalized = (json.dumps(resource, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as outgoing:
        with gzip.GzipFile(filename="", mode="wb", fileobj=outgoing, mtime=0) as compressed:
            compressed.write(normalized)
    return {
        "resource_type": str(resource.get("resourceType", "")),
        "rows": 1,
        "unique_ids": 0,
        "duplicate_ids": 0,
        "parse_failures": 0,
        "uncompressed_bytes": len(normalized),
    }


def inspect_ndjson(path: Path, compressed: bool = False) -> dict[str, object]:
    opener = gzip.open if compressed else Path.open
    ids: list[str] = []
    types: Counter[str] = Counter()
    rows = failures = 0
    if compressed:
        handle = opener(path, "rt", encoding="utf-8")
    else:
        handle = opener(path, "r", encoding="utf-8")
    with handle:
        for line in handle:
            rows += 1
            try:
                resource = json.loads(line)
                types[str(resource.get("resourceType", ""))] += 1
                ids.append(str(resource.get("id", "")))
            except (json.JSONDecodeError, AttributeError):
                failures += 1
    resource_type = next(iter(types)) if len(types) == 1 else "mixed"
    return {
        "resource_type": resource_type,
        "rows": rows,
        "unique_ids": len(set(ids)),
        "duplicate_ids": len(ids) - len(set(ids)),
        "parse_failures": failures,
    }


def inspect_json(path: Path, compressed: bool = False) -> dict[str, object]:
    opener = gzip.open if compressed else Path.open
    if compressed:
        handle = opener(path, "rt", encoding="utf-8")
    else:
        handle = opener(path, "r", encoding="utf-8")
    with handle:
        resource = json.load(handle)
    return {
        "resource_type": str(resource.get("resourceType", "")),
        "rows": 1,
        "unique_ids": 0,
        "duplicate_ids": 0,
        "parse_failures": 0,
    }


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_input_rows() -> list[dict[str, object]]:
    return [
        {
            "input": "Synthea runnable JAR", "version": SYNTHEA["version"],
            "url": SYNTHEA["url"], "bytes": SYNTHEA["bytes"], "sha256": SYNTHEA["sha256"],
            "license": "Apache-2.0", "committed": "no",
        },
        {
            "input": "Eclipse Temurin portable JRE", "version": JAVA["version"],
            "url": JAVA["url"], "bytes": JAVA["bytes"], "sha256": JAVA["sha256"],
            "license": "GPL-2.0-with-Classpath-exception", "committed": "no",
        },
    ]


def generate(cache: Path, target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target.resolve()}")
    acquire(cache)
    jar = cache / str(SYNTHEA["name"])
    runtime_zip = cache / str(JAVA["name"])
    with tempfile.TemporaryDirectory(prefix="app4-module02-synthea-") as temporary:
        temp = Path(temporary)
        runtime = temp / "runtime"
        with zipfile.ZipFile(runtime_zip) as archive:
            archive.extractall(runtime)
        java_candidates = sorted(runtime.rglob("java.exe"))
        if not java_candidates:
            raise FileNotFoundError("The pinned Java archive contains no java.exe")
        output = temp / "output"
        command = [
            str(java_candidates[0]), "-Xmx6g", "-jar", str(jar),
            "-s", str(RANDOM_SEED), "-cs", str(CLINICIAN_SEED),
            "-p", str(POPULATION), "-r", REFERENCE_DATE, "-e", REFERENCE_DATE,
            "-a", AGE_RANGE,
            "-c", str(CONFIG), f"--exporter.baseDirectory={output}", STATE,
        ]
        result = subprocess.run(command, capture_output=True, timeout=7200)
        if result.returncode:
            error = result.stderr[-2000:].decode("utf-8", errors="replace")
            raise RuntimeError(f"Synthea failed with exit code {result.returncode}: {error}")
        fhir = output / "fhir"
        sources = sorted(fhir.glob("*.ndjson"))
        parameters = fhir / "parameters.json"
        expected = set(sources) | {parameters}
        unexpected = sorted(path for path in fhir.rglob("*") if path.is_file() and path not in expected)
        if not sources or not parameters.is_file() or unexpected:
            names = ", ".join(path.name for path in unexpected) or "none"
            raise ValueError(
                f"Unexpected FHIR output: {len(sources)} NDJSON, parameters={parameters.is_file()}, other={names}"
            )
        (target / "fhir").mkdir(parents=True)
        manifest: list[dict[str, object]] = []
        for source in sources:
            destination = target / "fhir" / f"{source.name}.gz"
            inspection = normalize_ndjson(source, destination)
            if inspection["parse_failures"]:
                raise ValueError(f"Invalid FHIR resources: {source.name}")
            manifest.append({
                "relative_path": destination.relative_to(target).as_posix(),
                **inspection,
                "compressed_bytes": destination.stat().st_size,
                "sha256": sha256(destination),
            })
        parameters_destination = target / "fhir" / "parameters.json.gz"
        parameters_inspection = normalize_json(parameters, parameters_destination)
        manifest.append({
            "relative_path": parameters_destination.relative_to(target).as_posix(),
            **parameters_inspection,
            "compressed_bytes": parameters_destination.stat().st_size,
            "sha256": sha256(parameters_destination),
        })
        manifest.sort(key=lambda row: str(row["relative_path"]))
    write_csv(target / "source-manifest.csv", MANIFEST_FIELDS, manifest)
    write_csv(
        target / "build-inputs.csv",
        ["input", "version", "url", "bytes", "sha256", "license", "committed"],
        build_input_rows(),
    )
    total_rows = sum(int(row["rows"]) for row in manifest)
    total_uncompressed = sum(int(row["uncompressed_bytes"]) for row in manifest)
    total_compressed = sum(int(row["compressed_bytes"]) for row in manifest)
    duplicate_ids = sum(int(row["duplicate_ids"]) for row in manifest)
    release = {
        "schema_version": "1.0.0",
        "release_id": "CGH-GIM-01-SYNTHETIC-2026-08-31-v1",
        "status": "synthetic teaching data only",
        "generator": "Synthea 4.0.0",
        "fhir": "R4 with US Core 7.0.0 exporter setting",
        "population_requested": POPULATION,
        "state": STATE,
        "age_range": AGE_RANGE,
        "only_alive": True,
        "random_seed": RANDOM_SEED,
        "clinician_seed": CLINICIAN_SEED,
        "reference_date": REFERENCE_DATE,
        "end_date": REFERENCE_DATE,
        "history_years": 5,
        "upstream_windows_text_encoding": "windows-1252",
        "committed_text_encoding": "utf-8",
        "resource_files": len(manifest),
        "resource_rows": total_rows,
        "uncompressed_bytes": total_uncompressed,
        "compressed_bytes": total_compressed,
        "parse_failures": 0,
        "duplicate_resource_ids_within_file": duplicate_ids,
        "source_manifest_sha256": sha256(target / "source-manifest.csv"),
        "configuration_sha256": sha256(CONFIG),
        "claim_limit": "does not establish real prevalence, performance, workflow fit, clinical correctness, safety, or deployment readiness",
    }
    (target / "synthetic-release.json").write_text(
        json.dumps(release, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    lines = [
        "APP-4 Module 02 synthetic generation log",
        "status=pass",
        f"release_id={release['release_id']}",
        f"command=java -Xmx6g -jar {SYNTHEA['name']} -s {RANDOM_SEED} -cs {CLINICIAN_SEED} -p {POPULATION} -r {REFERENCE_DATE} -e {REFERENCE_DATE} -a {AGE_RANGE} -c synthea.properties --exporter.baseDirectory=TEMP_OUTPUT {STATE}",
        f"resource_files={len(manifest)}",
        f"resource_rows={total_rows}",
        f"uncompressed_bytes={total_uncompressed}",
        f"compressed_bytes={total_compressed}",
        "parse_failures=0",
        f"duplicate_resource_ids_within_file={duplicate_ids}",
        "upstream_windows_text_encoding=windows-1252",
        "committed_text_encoding=utf-8",
        "local_paths_recorded=0",
    ]
    (target / "generation-log.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return release


def verify(target: Path) -> dict[str, object]:
    required = [
        target / "source-manifest.csv", target / "build-inputs.csv",
        target / "synthetic-release.json", target / "generation-log.txt",
    ]
    if any(not path.is_file() for path in required):
        raise FileNotFoundError("Synthetic release control file is missing")
    with (target / "source-manifest.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Synthetic release manifest is empty")
    for row in rows:
        source = target / row["relative_path"]
        if not source.is_file() or source.stat().st_size != int(row["compressed_bytes"]):
            raise ValueError(f"Synthetic source bytes changed: {row['relative_path']}")
        if sha256(source) != row["sha256"]:
            raise ValueError(f"Synthetic source hash changed: {row['relative_path']}")
        inspection = (
            inspect_json(source, compressed=True)
            if row["relative_path"].endswith(".json.gz")
            else inspect_ndjson(source, compressed=True)
        )
        for field in ("resource_type", "rows", "unique_ids", "duplicate_ids", "parse_failures"):
            expected: object = row[field] if field == "resource_type" else int(row[field])
            if inspection[field] != expected:
                raise ValueError(f"Synthetic source profile changed: {row['relative_path']} {field}")
    with (target / "build-inputs.csv").open(encoding="utf-8", newline="") as handle:
        inputs = list(csv.DictReader(handle))
    if inputs != [{key: str(value) for key, value in row.items()} for row in build_input_rows()]:
        raise ValueError("Build input contract changed")
    release = json.loads((target / "synthetic-release.json").read_text(encoding="utf-8"))
    if release["source_manifest_sha256"] != sha256(target / "source-manifest.csv"):
        raise ValueError("Synthetic release manifest identity changed")
    if release["configuration_sha256"] != sha256(CONFIG) or release["parse_failures"] != 0:
        raise ValueError("Synthetic release configuration or parse status changed")
    return {
        "status": "pass", "resource_files": len(rows),
        "resource_rows": sum(int(row["rows"]) for row in rows),
        "compressed_bytes": sum(int(row["compressed_bytes"]) for row in rows),
    }


def self_check() -> None:
    assert len(SYNTHEA["sha256"]) == len(JAVA["sha256"]) == 64
    assert POPULATION == 1000 and RANDOM_SEED != CLINICIAN_SEED
    assert REFERENCE_DATE == "20260831" and AGE_RANGE == "18-89"
    assert CONFIG.is_file() and "generate.thread_pool_size = 1" in CONFIG.read_text(encoding="utf-8")
    print("APP-4 Module 02 synthetic generator self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path)
    parser.add_argument("--target", type=Path, default=ROOT / "data" / "synthetic-release")
    parser.add_argument("--acquire", action="store_true")
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.acquire:
            if not args.cache:
                parser.error("--cache is required with --acquire")
            acquire(args.cache)
            print("Pinned build inputs acquired and verified.")
        elif args.generate:
            if not args.cache:
                parser.error("--cache is required with --generate")
            print(json.dumps(generate(args.cache, args.target), indent=2))
        elif args.verify:
            print(json.dumps(verify(args.target), indent=2))
        else:
            parser.error("choose --acquire, --generate, --verify, or --self-check")
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        parser.exit(1, f"Synthetic release failed: {error}\n")


if __name__ == "__main__":
    main()
