"""Acquire, profile, and verify the APP-4 Module 01 public source release."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import shutil
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RAW = DATA / "raw"
RETRIEVED = "2026-08-30"
USER_AGENT = "OpenClinicalLearningCommons/0.77.0 source acquisition"
COMPONENTS = {
    "DEMO": "demographics and survey design",
    "BMX": "body measures",
    "DIQ": "diabetes questionnaire",
    "GHB": "glycohemoglobin laboratory",
}
CYCLES = (
    ("2013-2014", "2013", "H", "development evidence"),
    ("2015-2016", "2015", "I", "development evidence"),
    ("2017-2018", "2017", "J", "temporal holdout"),
    ("2021-2023", "2021", "L", "later-cycle transport stress test"),
)
SOURCE_SPECS = tuple(
    {
        "source_id": f"NHANES-{cycle}-{component}-{suffix}",
        "cycle": cycle,
        "year_path": year,
        "suffix": suffix,
        "component": component,
        "cycle_role": role,
        "component_role": component_role,
        "filename": f"{component}_{suffix}.xpt",
        "url": f"https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/{year}/DataFiles/{component}_{suffix}.xpt",
        "codebook_url": f"https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/{year}/DataFiles/{component}_{suffix}.htm",
    }
    for cycle, year, suffix, role in CYCLES
    for component, component_role in COMPONENTS.items()
)

PINNED_IDENTITIES: dict[str, dict[str, object]] = {
    "DEMO_H.xpt": {"raw_bytes": 3833200, "raw_sha256": "f8f0cbb3085a323d4cde22349b164878fea1e64dbc404e65b5815c7816b547d7", "gzip_bytes": 472473, "gzip_sha256": "c42448a52080c75a9d9dc1e49e47ee05c2f502e9532eaaa9318458573706a88c", "rows": 10175, "columns": 47, "seqn_unique": 10175, "seqn_duplicates": 0},
    "BMX_H.xpt": {"raw_bytes": 2045520, "raw_sha256": "fd5e9fc6e6aab0a4aee6e699f51497bbc9b62101f7f43aee924c473e38fd9442", "gzip_bytes": 272963, "gzip_sha256": "d95927caf9d6b35c99691e1f7a1ff995c5d7fab0ceb27f7f784cac7676cc8bba", "rows": 9813, "columns": 26, "seqn_unique": 9813, "seqn_duplicates": 0},
    "DIQ_H.xpt": {"raw_bytes": 4228960, "raw_sha256": "c74c7ccef65e6997dfac1db1e73bc3f63dec67c70b2e322ffc14f14ce27429a9", "gzip_bytes": 85855, "gzip_sha256": "42851286c6669e312c3f730b00b4225271eae52ed61aacb3f01a1941bde83cdc", "rows": 9770, "columns": 54, "seqn_unique": 9770, "seqn_duplicates": 0},
    "GHB_H.xpt": {"raw_bytes": 112720, "raw_sha256": "0695894ad55ac96f315a8415401977b0856c402d16762115b534bcd5dfeae89e", "gzip_bytes": 24297, "gzip_sha256": "a9039cee1a61514689c50689a642d171f519c5ec54791d47e6ff7e4fffcad806", "rows": 6979, "columns": 2, "seqn_unique": 6979, "seqn_duplicates": 0},
    "DEMO_I.xpt": {"raw_bytes": 3756480, "raw_sha256": "c9297c6c37ae8f78f29be9568fa2a03cf3b112616a39afee04030fc775a66a0d", "gzip_bytes": 465463, "gzip_sha256": "065fcb3f3d87ac7c4f0efe2ea0e69b26312b378d0438a8acb7030cab34c5bba2", "rows": 9971, "columns": 47, "seqn_unique": 9971, "seqn_duplicates": 0},
    "BMX_I.xpt": {"raw_bytes": 1989600, "raw_sha256": "d31da84e14212b4e58e8340598a5b8e2144fac83333563e966eb1b332e4141d6", "gzip_bytes": 264583, "gzip_sha256": "29d3c394c67c63182feb8503bb4f1f7f73059b19e0897a880872fd37d693b448", "rows": 9544, "columns": 26, "seqn_unique": 9544, "seqn_duplicates": 0},
    "DIQ_I.xpt": {"raw_bytes": 4144720, "raw_sha256": "e87587479b29f175b63eee5dd40d582837e3e3fe2665503012085eefdb978e0d", "gzip_bytes": 91013, "gzip_sha256": "39f348d86113f7b92caa6f3cad5d9ed826f50a6b98c6f3f403f0da3cedd67e0a", "rows": 9575, "columns": 54, "seqn_unique": 9575, "seqn_duplicates": 0},
    "GHB_I.xpt": {"raw_bytes": 108960, "raw_sha256": "e4bc626cd12f6057c7806aef4f85874c9bf1407a7480d6621a4af142260addd2", "gzip_bytes": 23457, "gzip_sha256": "299853de579178d113b220f4a1dbc23fae4002dcee4a715fde45962e676cfdcb", "rows": 6744, "columns": 2, "seqn_unique": 6744, "seqn_duplicates": 0},
    "DEMO_J.xpt": {"raw_bytes": 3412720, "raw_sha256": "c0b46e0345ea19404928656277c8b0d10b0cca348a9b2fe4fc3c67e8b7ee73ec", "gzip_bytes": 406039, "gzip_sha256": "87cdf1223c97b7e9ff2feb193d257ac62b6ebbc18ecb94825b83913df800fee7", "rows": 9254, "columns": 46, "seqn_unique": 9254, "seqn_duplicates": 0},
    "BMX_J.xpt": {"raw_bytes": 1466000, "raw_sha256": "8d675e42d8826ac98714b2c3dd4c5138a5e353fb4424f7eff5e6db4a01ce838a", "gzip_bytes": 204171, "gzip_sha256": "31bc823243b88d72b441f9bcdaf8b859d78295c3c321506d5a9de613fa0af88c", "rows": 8704, "columns": 21, "seqn_unique": 8704, "seqn_duplicates": 0},
    "DIQ_J.xpt": {"raw_bytes": 3851840, "raw_sha256": "1ecbf5360dfc331d1efbf32198553dc30e9a1f4cff0a907ed30ca72bac797f89", "gzip_bytes": 89679, "gzip_sha256": "9947db89bba73c8a07c519a8467343691d19cc05689df6dd05704a94690c89cb", "rows": 8897, "columns": 54, "seqn_unique": 8897, "seqn_duplicates": 0},
    "GHB_J.xpt": {"raw_bytes": 103520, "raw_sha256": "35f07094573a0061a03ed609a5a363b34eb1b1c7065d1623b43d72e132a8a654", "gzip_bytes": 22437, "gzip_sha256": "4ba9fdde459560d1e88264570d119532421c1c4c7206bd14f5e3ae4a367dd8ed", "rows": 6401, "columns": 2, "seqn_unique": 6401, "seqn_duplicates": 0},
    "DEMO_L.xpt": {"raw_bytes": 2582160, "raw_sha256": "ca4374a158b493b8b0163e1388da21d57a18d1b9cecff2aa4e2fa2bec494fe23", "gzip_bytes": 384431, "gzip_sha256": "565da2e91a5a9fd354dddd144d3945a861c33ab28be183958690bbd2afe5200d", "rows": 11933, "columns": 27, "seqn_unique": 11933, "seqn_duplicates": 0},
    "BMX_L.xpt": {"raw_bytes": 1563200, "raw_sha256": "44440c416d9ad709e8b1708a5975378ab4d5b18edc39eb5015c2ae7186500170", "gzip_bytes": 210644, "gzip_sha256": "072951c3ae09534e18b89ea20fd368890649dbb422fbc323d966009dc0b1fbae", "rows": 8860, "columns": 22, "seqn_unique": 8860, "seqn_duplicates": 0},
    "DIQ_L.xpt": {"raw_bytes": 847600, "raw_sha256": "9535a023673ae869afae19d842d8679e06f6a464606ac15900686b41ef05090f", "gzip_bytes": 48146, "gzip_sha256": "ca78f289a7b99142443bde43dfaa0018238dbf412178c90cc32e427a0f424068", "rows": 11744, "columns": 9, "seqn_unique": 11744, "seqn_duplicates": 0},
    "GHB_L.xpt": {"raw_bytes": 174000, "raw_sha256": "67aee0353160e2392dc0a33bece99b90764a630c76d82415ac4639105ad9dd03", "gzip_bytes": 83392, "gzip_sha256": "3056f3ca93ea7d4f1b6426ecefe3e632af7e30347eaa0187e882d96e51312f9c", "rows": 7199, "columns": 3, "seqn_unique": 7199, "seqn_duplicates": 0},
}

SOURCE_FIELDS = [
    "source_id", "cycle", "component", "suffix", "cycle_role", "component_role",
    "url", "codebook_url", "retrieved", "raw_filename", "raw_bytes", "raw_sha256",
    "gzip_filename", "gzip_bytes", "gzip_sha256", "rows", "columns", "seqn_unique",
    "seqn_duplicates", "teaching_role", "claim_limit",
]
FIELD_FIELDS = [
    "source_id", "cycle", "component", "field_order", "field_name", "pandas_dtype",
    "rows", "nonmissing", "missing", "distinct_nonmissing", "source_role",
]
JOIN_FIELDS = [
    "cycle", "demo_rows", "bmx_rows", "diq_rows", "ghb_rows", "demo_bmx_joined",
    "demo_diq_joined", "demo_ghb_joined", "all_four_joined", "ridageyr_present",
    "bmxbmi_present", "diq010_present", "lbxgh_present", "survey_design_present",
    "interpretation",
]
STANDARD_FIELDS = ["source_id", "title", "version", "url", "teaching_role", "claim_limit"]


class SourceError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def raw_identity(path: Path, compressed: bool = False) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0
    opener = gzip.open if compressed else Path.open
    with opener(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            size += len(block)
            digest.update(block)
    return size, digest.hexdigest()


def deterministic_gzip(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as input_handle, target.open("wb") as output_handle:
        with gzip.GzipFile(filename="", mode="wb", fileobj=output_handle, mtime=0) as zipped:
            shutil.copyfileobj(input_handle, zipped, 1024 * 1024)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def download(url: str, target: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response, target.open("wb") as handle:
        if response.status != 200:
            raise SourceError(f"Download failed with HTTP {response.status}: {url}")
        shutil.copyfileobj(response, handle, 1024 * 1024)
    if target.stat().st_size == 0:
        raise SourceError(f"Download returned an empty file: {url}")


def read_xpt(path: Path, compressed: bool = False) -> pd.DataFrame:
    if not compressed:
        return pd.read_sas(path, format="xport")
    with tempfile.NamedTemporaryFile(suffix=".xpt", delete=False) as temporary:
        temp_path = Path(temporary.name)
        with gzip.open(path, "rb") as source:
            shutil.copyfileobj(source, temporary, 1024 * 1024)
    try:
        return pd.read_sas(temp_path, format="xport")
    finally:
        temp_path.unlink(missing_ok=True)


def profile_frame(spec: dict[str, str], frame: pd.DataFrame) -> tuple[dict[str, object], list[dict[str, object]]]:
    if "SEQN" not in frame.columns:
        raise SourceError(f"{spec['filename']} does not contain SEQN")
    duplicates = int(frame["SEQN"].duplicated().sum())
    if duplicates:
        raise SourceError(f"{spec['filename']} contains {duplicates} duplicate SEQN values")
    fields = []
    for order, name in enumerate(frame.columns, start=1):
        nonmissing = int(frame[name].notna().sum())
        fields.append({
            "source_id": spec["source_id"],
            "cycle": spec["cycle"],
            "component": spec["component"],
            "field_order": order,
            "field_name": name,
            "pandas_dtype": str(frame[name].dtype),
            "rows": len(frame),
            "nonmissing": nonmissing,
            "missing": len(frame) - nonmissing,
            "distinct_nonmissing": int(frame[name].nunique(dropna=True)),
            "source_role": spec["component_role"],
        })
    return {
        "rows": len(frame),
        "columns": len(frame.columns),
        "seqn_unique": int(frame["SEQN"].nunique(dropna=True)),
        "seqn_duplicates": duplicates,
    }, fields


def standard_rows() -> list[dict[str, str]]:
    return [
        {"source_id": "CDS-HOOKS-2.0.1", "title": "CDS Hooks", "version": "2.0.1", "url": "https://cds-hooks.hl7.org/", "teaching_role": "nonproduction hook, context, request, and response shapes", "claim_limit": "does not certify conformance or EHR compatibility"},
        {"source_id": "FHIR-R4-OBSERVATION", "title": "FHIR R4 Observation", "version": "4.0.1", "url": "https://hl7.org/fhir/R4/observation.html", "teaching_role": "synthetic observation shape and timing", "claim_limit": "does not certify terminology or implementation readiness"},
        {"source_id": "FHIR-R4-CONDITION", "title": "FHIR R4 Condition", "version": "4.0.1", "url": "https://hl7.org/fhir/R4/condition.html", "teaching_role": "synthetic condition shape and status", "claim_limit": "does not define a clinical diagnosis or local problem list"},
        {"source_id": "SYNTHEA-4.0.0", "title": "Synthea synthetic patient generator", "version": "4.0.0", "url": "https://github.com/synthetichealth/synthea/releases/tag/v4.0.0", "teaching_role": "candidate upstream synthetic FHIR generator for Module 02", "claim_limit": "synthetic output is not clinical or deployment evidence"},
        {"source_id": "ONC-SAFER-CPOE-CDS", "title": "SAFER Guide 3: Computerized Provider Order Entry with Decision Support", "version": "2025 PDF", "url": "https://www.healthit.gov/wp-content/uploads/2025/06/SAFER-Guide-3.-CPOE-Final.pdf", "teaching_role": "safety, governance, and unintended-consequence prompts", "claim_limit": "does not replace local review, policy, testing, or approval"},
    ]


def cycle_join_rows(frames: dict[str, pd.DataFrame]) -> list[dict[str, object]]:
    rows = []
    for cycle, _, suffix, _ in CYCLES:
        by_component = {component: frames[f"{component}_{suffix}.xpt"] for component in COMPONENTS}
        ids = {component: set(frame["SEQN"].astype(int)) for component, frame in by_component.items()}
        demo = by_component["DEMO"]
        rows.append({
            "cycle": cycle,
            "demo_rows": len(by_component["DEMO"]),
            "bmx_rows": len(by_component["BMX"]),
            "diq_rows": len(by_component["DIQ"]),
            "ghb_rows": len(by_component["GHB"]),
            "demo_bmx_joined": len(ids["DEMO"] & ids["BMX"]),
            "demo_diq_joined": len(ids["DEMO"] & ids["DIQ"]),
            "demo_ghb_joined": len(ids["DEMO"] & ids["GHB"]),
            "all_four_joined": len(set.intersection(*ids.values())),
            "ridageyr_present": str("RIDAGEYR" in demo.columns).lower(),
            "bmxbmi_present": str("BMXBMI" in by_component["BMX"].columns).lower(),
            "diq010_present": str("DIQ010" in by_component["DIQ"].columns).lower(),
            "lbxgh_present": str("LBXGH" in by_component["GHB"].columns).lower(),
            "survey_design_present": str(all(field in demo.columns for field in ("SDMVPSU", "SDMVSTRA", "WTMEC2YR"))).lower(),
            "interpretation": "source feasibility only; no final cohort, target, model, threshold, or local validity claim",
        })
    return rows


def build(acquire: bool) -> dict[str, object]:
    inventory: list[dict[str, object]] = []
    fields: list[dict[str, object]] = []
    frames: dict[str, pd.DataFrame] = {}
    with tempfile.TemporaryDirectory(prefix="app4-module01-sources-") as temp_dir:
        temp = Path(temp_dir)
        for spec in SOURCE_SPECS:
            raw = temp / spec["filename"]
            committed = RAW / f"{spec['filename']}.gz"
            if acquire:
                download(spec["url"], raw)
                deterministic_gzip(raw, committed)
                frame = read_xpt(raw)
            else:
                if not committed.is_file():
                    raise SourceError(f"Missing committed source: {committed.name}")
                frame = read_xpt(committed, compressed=True)
            raw_bytes, raw_hash = raw_identity(raw if acquire else committed, compressed=not acquire)
            profile, field_rows = profile_frame(spec, frame)
            pinned = PINNED_IDENTITIES.get(spec["filename"])
            if not acquire:
                if not pinned:
                    raise SourceError(f"No pinned identity for {spec['filename']}")
                actual = {
                    "raw_bytes": raw_bytes,
                    "raw_sha256": raw_hash,
                    "gzip_bytes": committed.stat().st_size,
                    "gzip_sha256": sha256(committed),
                    **profile,
                }
                if any(actual[key] != pinned[key] for key in actual):
                    raise SourceError(f"Pinned identity mismatch for {spec['filename']}: {actual}")
            inventory.append({
                **{key: spec[key] for key in ("source_id", "cycle", "component", "suffix", "cycle_role", "component_role", "url", "codebook_url")},
                "retrieved": RETRIEVED,
                "raw_filename": spec["filename"],
                "raw_bytes": raw_bytes,
                "raw_sha256": raw_hash,
                "gzip_filename": f"data/raw/{spec['filename']}.gz",
                "gzip_bytes": committed.stat().st_size,
                "gzip_sha256": sha256(committed),
                **profile,
                "teaching_role": "full public historical evidence for source feasibility and later model evaluation",
                "claim_limit": "not local workflow, prospective utility, clinical guidance, or deployment validation",
            })
            fields.extend(field_rows)
            frames[spec["filename"]] = frame
    joins = cycle_join_rows(frames)
    write_csv(DATA / "source-inventory.csv", SOURCE_FIELDS, inventory)
    write_csv(DATA / "field-inventory.csv", FIELD_FIELDS, fields)
    write_csv(DATA / "cycle-join-profile.csv", JOIN_FIELDS, joins)
    write_csv(DATA / "standards-inventory.csv", STANDARD_FIELDS, standard_rows())
    return {
        "sources": len(inventory),
        "raw_bytes": sum(int(row["raw_bytes"]) for row in inventory),
        "gzip_bytes": sum(int(row["gzip_bytes"]) for row in inventory),
        "source_rows": sum(int(row["rows"]) for row in inventory),
        "field_rows": len(fields),
        "cycles": len(joins),
    }


def verify_profiles() -> dict[str, object]:
    summary = build(acquire=False)
    inventory = read_csv(DATA / "source-inventory.csv")
    if len(inventory) != 16 or len(read_csv(DATA / "cycle-join-profile.csv")) != 4 or len(read_csv(DATA / "standards-inventory.csv")) != 5:
        raise SourceError("Committed profile row counts do not match the module contract")
    return summary


def self_check() -> None:
    summary = verify_profiles()
    first = SOURCE_SPECS[0]
    source = RAW / f"{first['filename']}.gz"
    with tempfile.TemporaryDirectory(prefix="app4-module01-mutation-") as temp_dir:
        changed = Path(temp_dir) / source.name
        raw = gzip.decompress(source.read_bytes())
        raw = bytes([raw[0] ^ 1]) + raw[1:]
        with changed.open("wb") as output:
            with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
                zipped.write(raw)
        size, digest = raw_identity(changed, compressed=True)
        pinned = PINNED_IDENTITIES[first["filename"]]
        if size == pinned["raw_bytes"] and digest == pinned["raw_sha256"]:
            raise AssertionError("Source mutation did not change the pinned identity")
    print(f"APP-4 Module 01 source self-check passed: {json.dumps(summary, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--acquire", action="store_true", help="Download and write all complete source files and profiles.")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        else:
            print(json.dumps(build(acquire=args.acquire) if args.acquire else verify_profiles(), indent=2))
    except (OSError, ValueError, KeyError, urllib.error.URLError, SourceError) as error:
        parser.exit(1, f"Source profiling failed: {error}\n")


if __name__ == "__main__":
    main()
