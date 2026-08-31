"""Generate and verify the APP-5 Module 02 synthetic event release."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import random
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GENERATOR_VERSION = "0.1.0"
RELEASE = "fma-dp-01-measures-v1"
SEED = 73052
PERIOD = "2024"
EXPECTED_FILES: dict[str, dict[str, object]] = {
    "raw/synthetic-events.csv.gz": {"bytes": 113029, "sha256": "56f04f4e660e40292351cc0ed630b8cbb2f2c0d9cf9c39fbc8420b2113d813cb"},
    "age-band-crosswalk.csv": {"bytes": 2456, "sha256": "16cf59b15747375088bdd7f77e380a0b17b5d6f8f4dbb5ee1fe3e2d234646e20"},
    "data-dictionary.csv": {"bytes": 5053, "sha256": "66a42e357d190f85e69b3774d7b50cecb6131573398ea6615bed15f33cd93e59"},
    "synthetic-source-manifest.csv": {"bytes": 778, "sha256": "9915aeb15f62d88a52cfa6304d211a4fd092d33c11e73cd5d63a14d64946823d"},
}

AGE_BANDS = (
    ("A01", "18-34", 1, 0.018, ((7, "Male 18 and 19 years"), (8, "Male 20 years"), (9, "Male 21 years"), (10, "Male 22 to 24 years"), (11, "Male 25 to 29 years"), (12, "Male 30 to 34 years"), (31, "Female 18 and 19 years"), (32, "Female 20 years"), (33, "Female 21 years"), (34, "Female 22 to 24 years"), (35, "Female 25 to 29 years"), (36, "Female 30 to 34 years"))),
    ("A02", "35-49", 2, 0.035, ((13, "Male 35 to 39 years"), (14, "Male 40 to 44 years"), (15, "Male 45 to 49 years"), (37, "Female 35 to 39 years"), (38, "Female 40 to 44 years"), (39, "Female 45 to 49 years"))),
    ("A03", "50-64", 3, 0.065, ((16, "Male 50 to 54 years"), (17, "Male 55 to 59 years"), (18, "Male 60 and 61 years"), (19, "Male 62 to 64 years"), (40, "Female 50 to 54 years"), (41, "Female 55 to 59 years"), (42, "Female 60 and 61 years"), (43, "Female 62 to 64 years"))),
    ("A04", "65-74", 4, 0.085, ((20, "Male 65 and 66 years"), (21, "Male 67 to 69 years"), (22, "Male 70 to 74 years"), (44, "Female 65 and 66 years"), (45, "Female 67 to 69 years"), (46, "Female 70 to 74 years"))),
    ("A05", "75+", 5, 0.100, ((23, "Male 75 to 79 years"), (24, "Male 80 to 84 years"), (25, "Male 85 years and over"), (47, "Female 75 to 79 years"), (48, "Female 80 to 84 years"), (49, "Female 85 years and over"))),
)

EVENT_FIELDS = [
    "synthetic_event_id", "case_id", "tract_fips", "age_band_id", "age_band",
    "period", "acs_denominator_estimate", "synthetic_event_count",
    "generated_probability", "fictional_tract_effect", "generator_version", "seed",
    "synthetic_flag", "numerator_definition", "claim_limit",
]
CROSSWALK_FIELDS = [
    "age_band_id", "age_band", "band_order", "sex", "source_age_label",
    "acs_estimate_field", "acs_moe_field",
]
MANIFEST_FIELDS = [
    "source_id", "relative_path", "format", "rows", "columns", "bytes", "sha256",
    "content_bytes", "content_sha256", "generator_version", "seed", "synthetic_flag",
    "period", "claim_limit",
]
DICTIONARY_FIELDS = [
    "source_id", "field_order", "field_name", "type", "nullable", "definition", "claim_limit",
]


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


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def csv_bytes(fields: list[str], rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def deterministic_gzip(raw: bytes) -> bytes:
    output = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
        zipped.write(raw)
    return output.getvalue()


def stable_seed(*parts: object) -> int:
    text = "|".join(str(part) for part in parts)
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:16], 16)


def crosswalk_rows() -> list[dict[str, object]]:
    rows = []
    for age_id, age_band, order, _, cells in AGE_BANDS:
        for cell, label in cells:
            rows.append({
                "age_band_id": age_id,
                "age_band": age_band,
                "band_order": order,
                "sex": "female" if cell >= 26 else "male",
                "source_age_label": label,
                "acs_estimate_field": f"B01001_E{cell:03d}",
                "acs_moe_field": f"B01001_M{cell:03d}",
            })
    return rows


def dictionary_rows() -> list[dict[str, object]]:
    event_definitions = {
        "synthetic_event_id": ("text", "no", "Stable generated tract-age-period row identifier"),
        "case_id": ("text", "no", "Fictional planning case identifier FMA-DP-01"),
        "tract_fips": ("text", "no", "Eleven-character Census tract key from the accepted public intersection"),
        "age_band_id": ("text", "no", "Stable adult age-band identifier"),
        "age_band": ("text", "no", "Adult age-band label"),
        "period": ("text", "no", "Fictional synthetic event period"),
        "acs_denominator_estimate": ("integer", "no", "ACS-derived age-band estimate copied only for generator reconciliation"),
        "synthetic_event_count": ("integer", "no", "Generated planning-need event count"),
        "generated_probability": ("decimal", "no", "Fixed age probability plus seeded fictional tract effect"),
        "fictional_tract_effect": ("decimal", "no", "Seeded effect unrelated to PLACES or SVI values"),
        "generator_version": ("text", "no", "Synthetic generator semantic version"),
        "seed": ("integer", "no", "Synthetic generator seed"),
        "synthetic_flag": ("integer", "no", "One for every generated row"),
        "numerator_definition": ("text", "no", "Exact teaching numerator definition"),
        "claim_limit": ("text", "no", "Prohibition on real case, eligibility, outcome, or allocation claims"),
    }
    crosswalk_definitions = {
        "age_band_id": ("text", "no", "Stable adult age-band identifier"),
        "age_band": ("text", "no", "Adult age-band label"),
        "band_order": ("integer", "no", "Display and calculation order"),
        "sex": ("text", "no", "B01001 source sex branch"),
        "source_age_label": ("text", "no", "Human-readable B01001 source cell label"),
        "acs_estimate_field": ("text", "no", "B01001 estimate field included in the age-band sum"),
        "acs_moe_field": ("text", "no", "Paired B01001 90 percent margin-of-error field"),
    }
    rows = []
    for source_id, definitions in (("synthetic-events", event_definitions), ("age-band-crosswalk", crosswalk_definitions)):
        for order, (field, (data_type, nullable, definition)) in enumerate(definitions.items(), start=1):
            rows.append({
                "source_id": source_id,
                "field_order": order,
                "field_name": field,
                "type": data_type,
                "nullable": nullable,
                "definition": definition,
                "claim_limit": "Synthetic aggregates and ACS field routing support teaching only; they do not establish real cases, individual traits, or action authority.",
            })
    return rows


def load_accepted_tracts(root: Path) -> tuple[dict[str, dict[str, str]], set[str]]:
    source = root / "upstream/module01-reference/data"
    _, acs_rows = read_csv(source / "acs-b01001-ma-tract-2024.csv")
    _, places_rows = read_csv(source / "places-diabetes-ma-tract-2025.csv")
    _, svi_rows = read_csv(source / "svi2022-ma-tract.csv")
    acs = {row["tract_fips"]: row for row in acs_rows}
    places = {row["locationid"] for row in places_rows}
    svi = {row["FIPS"] for row in svi_rows}
    intersection = set(acs) & places & svi
    require(len(acs) == 1620 and len(places) == 1597 and len(svi) == 1613, "Frozen public source shape changed")
    require(len(intersection) == 1597, "Frozen three-source tract intersection changed")
    return acs, intersection


def age_denominator(row: dict[str, str], cells: tuple[tuple[int, str], ...]) -> int:
    values = [int(row[f"B01001_E{cell:03d}"]) for cell, _ in cells]
    require(all(value >= 0 for value in values), "ACS age-band source contains a negative estimate")
    return sum(values)


def binomial_count(population: int, probability: float, rng: random.Random) -> int:
    return sum(rng.random() < probability for _ in range(population))


def build_rows(root: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    acs, intersection = load_accepted_tracts(root)
    events = []
    for tract in sorted(intersection):
        area_rng = random.Random(stable_seed(SEED, tract, "area-effect"))
        effect = area_rng.uniform(-0.0125, 0.0125)
        for age_id, age_band, _, base_probability, cells in AGE_BANDS:
            denominator = age_denominator(acs[tract], cells)
            probability = min(0.20, max(0.005, base_probability + effect))
            event_rng = random.Random(stable_seed(SEED, tract, age_id, PERIOD))
            count = binomial_count(denominator, probability, event_rng)
            events.append({
                "synthetic_event_id": f"SE-{tract}-{age_id}-{PERIOD}",
                "case_id": "FMA-DP-01",
                "tract_fips": tract,
                "age_band_id": age_id,
                "age_band": age_band,
                "period": PERIOD,
                "acs_denominator_estimate": denominator,
                "synthetic_event_count": count,
                "generated_probability": f"{probability:.8f}",
                "fictional_tract_effect": f"{effect:.8f}",
                "generator_version": GENERATOR_VERSION,
                "seed": SEED,
                "synthetic_flag": 1,
                "numerator_definition": "generated adult planning-need event for rate construction",
                "claim_limit": "not a diagnosis, PLACES case, individual eligibility result, local observation, intervention outcome, or allocation signal",
            })
    crosswalk = crosswalk_rows()
    require(len(events) == 7985 and len(crosswalk) == 38, "Synthetic release row contract changed")
    return events, crosswalk


def write_release(root: Path, target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    events, crosswalk = build_rows(root.resolve())
    (target / "raw").mkdir(parents=True)

    event_raw = csv_bytes(EVENT_FIELDS, events)
    event_gzip = deterministic_gzip(event_raw)
    event_path = target / "raw/synthetic-events.csv.gz"
    event_path.write_bytes(event_gzip)
    crosswalk_raw = csv_bytes(CROSSWALK_FIELDS, crosswalk)
    crosswalk_path = target / "age-band-crosswalk.csv"
    crosswalk_path.write_bytes(crosswalk_raw)
    dictionary_raw = csv_bytes(DICTIONARY_FIELDS, dictionary_rows())
    dictionary_path = target / "data-dictionary.csv"
    dictionary_path.write_bytes(dictionary_raw)

    manifest = [
        {
            "source_id": "synthetic-events",
            "relative_path": "data/raw/synthetic-events.csv.gz",
            "format": "deterministic gzip CSV",
            "rows": len(events),
            "columns": len(EVENT_FIELDS),
            "bytes": len(event_gzip),
            "sha256": sha256_bytes(event_gzip),
            "content_bytes": len(event_raw),
            "content_sha256": sha256_bytes(event_raw),
            "generator_version": GENERATOR_VERSION,
            "seed": SEED,
            "synthetic_flag": 1,
            "period": PERIOD,
            "claim_limit": "generated teaching numerator only; no real cases, eligibility, outcomes, targeting, or allocation",
        },
        {
            "source_id": "age-band-crosswalk",
            "relative_path": "data/age-band-crosswalk.csv",
            "format": "CSV",
            "rows": len(crosswalk),
            "columns": len(CROSSWALK_FIELDS),
            "bytes": len(crosswalk_raw),
            "sha256": sha256_bytes(crosswalk_raw),
            "content_bytes": len(crosswalk_raw),
            "content_sha256": sha256_bytes(crosswalk_raw),
            "generator_version": GENERATOR_VERSION,
            "seed": "",
            "synthetic_flag": 0,
            "period": "ACS 2020-2024",
            "claim_limit": "field routing only; ACS estimates remain survey-derived area estimates",
        },
    ]
    manifest_path = target / "synthetic-source-manifest.csv"
    manifest_path.write_bytes(csv_bytes(MANIFEST_FIELDS, manifest))
    return verify_data(target)


def open_gzip_csv(path: Path) -> tuple[list[str], list[dict[str, str]], bytes]:
    with gzip.open(path, "rb") as handle:
        raw = handle.read()
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8")))
    return list(reader.fieldnames or []), list(reader), raw


def verify_data(data: Path) -> dict[str, object]:
    data = data.resolve()
    event_path = data / "raw/synthetic-events.csv.gz"
    crosswalk_path = data / "age-band-crosswalk.csv"
    dictionary_path = data / "data-dictionary.csv"
    manifest_path = data / "synthetic-source-manifest.csv"
    for path in (event_path, crosswalk_path, dictionary_path, manifest_path):
        require(path.is_file(), f"Synthetic source file is missing: {path.name}")
    event_header, events, event_raw = open_gzip_csv(event_path)
    crosswalk_header, crosswalk = read_csv(crosswalk_path)
    dictionary_header, dictionary = read_csv(dictionary_path)
    manifest_header, manifest = read_csv(manifest_path)
    require(event_header == EVENT_FIELDS and len(events) == 7985, "Synthetic event shape changed")
    require(crosswalk_header == CROSSWALK_FIELDS and len(crosswalk) == 38, "Age-band crosswalk shape changed")
    require(dictionary_header == DICTIONARY_FIELDS and len(dictionary) == 22, "Data dictionary shape changed")
    require(manifest_header == MANIFEST_FIELDS and len(manifest) == 2, "Synthetic source manifest shape changed")
    require(len({row["synthetic_event_id"] for row in events}) == 7985, "Synthetic event identifier is not unique")
    require(len({row["tract_fips"] for row in events}) == 1597, "Synthetic event tract count changed")
    require(all(row["case_id"] == "FMA-DP-01" and row["period"] == PERIOD and row["synthetic_flag"] == "1" for row in events), "Synthetic identity field changed")
    require(all(0 <= int(row["synthetic_event_count"]) <= int(row["acs_denominator_estimate"]) for row in events), "Synthetic event count is invalid")
    require(sum(int(row["acs_denominator_estimate"]) for row in events) == 5679768, "Accepted adult denominator total changed")
    require({row["age_band_id"] for row in events} == {"A01", "A02", "A03", "A04", "A05"}, "Synthetic age bands changed")
    require(all(math.isfinite(float(row["generated_probability"])) for row in events), "Synthetic probability is invalid")

    by_id = {row["source_id"]: row for row in manifest}
    require(set(by_id) == {"synthetic-events", "age-band-crosswalk"}, "Synthetic source manifest identities changed")
    require(int(by_id["synthetic-events"]["content_bytes"]) == len(event_raw) and by_id["synthetic-events"]["content_sha256"] == sha256_bytes(event_raw), "Synthetic event content identity changed")
    for source_id, path in (("synthetic-events", event_path), ("age-band-crosswalk", crosswalk_path)):
        row = by_id[source_id]
        require(path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"Manifest identity changed: {source_id}")
    if EXPECTED_FILES:
        for relative, expected in EXPECTED_FILES.items():
            path = data / relative
            require(path.stat().st_size == expected["bytes"] and sha256(path) == expected["sha256"], f"Pinned synthetic file changed: {relative}")
    return {
        "tracts": 1597,
        "age_bands": 5,
        "event_rows": len(events),
        "synthetic_events": sum(int(row["synthetic_event_count"]) for row in events),
        "adult_denominator": sum(int(row["acs_denominator_estimate"]) for row in events),
        "zero_denominators": sum(int(row["acs_denominator_estimate"]) == 0 for row in events),
        "source_manifest_sha256": sha256(manifest_path),
        "files": {
            relative: {"bytes": (data / relative).stat().st_size, "sha256": sha256(data / relative)}
            for relative in ("raw/synthetic-events.csv.gz", "age-band-crosswalk.csv", "data-dictionary.csv", "synthetic-source-manifest.csv")
        },
    }


def verify(root: Path = ROOT) -> dict[str, object]:
    return verify_data(root.resolve() / "data")


def self_check() -> None:
    committed = verify(ROOT)
    with tempfile.TemporaryDirectory(prefix="app5-module02-source-") as temp_dir:
        base = Path(temp_dir)
        first = write_release(ROOT, base / "first")
        second = write_release(ROOT, base / "second")
        require(first == second, "Two synthetic source builds differ")
        for relative in first["files"]:
            require((base / "first" / relative).read_bytes() == (base / "second" / relative).read_bytes(), f"Two source builds differ: {relative}")
            require((base / "first" / relative).read_bytes() == (ROOT / "data" / relative).read_bytes(), f"Committed source differs: {relative}")
        try:
            write_release(ROOT, base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Generator did not protect an existing target")
    print(f"APP-5 Module 02 synthetic-source self-check passed: {json.dumps(committed, sort_keys=True)}")


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
            print(json.dumps(write_release(ROOT, args.target or (ROOT / "data")), indent=2, sort_keys=True))
        else:
            print(json.dumps(verify(ROOT), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, SourceError) as error:
        parser.exit(1, f"Synthetic source failed: {error}\n")


if __name__ == "__main__":
    main()
