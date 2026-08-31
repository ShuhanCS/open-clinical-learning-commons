"""Generate and verify the APP-5 Module 03 synthetic equity release."""

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
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GENERATOR_VERSION = "0.1.0"
RELEASE = "fma-dp-01-equity-v1"
SEED = 73053
PERIOD = "2024"
EXPECTED_FILES: dict[str, dict[str, object]] = {
    "raw/synthetic-equity-margins.csv.gz": {"bytes": 1708745, "sha256": "aaacdd529cf3ab563db5ad4ebd4509496db544ebb63896b8c4dfaed44c89793d"},
    "raw/synthetic-field-completeness.csv.gz": {"bytes": 71316, "sha256": "9093020f885deaa71b9f1a1f47682343c17a401910c298b9f72fd661768c9edf"},
    "equity-group-contract.csv": {"bytes": 5366, "sha256": "56530a6063dd614eab498396ca9cfaca68fd37c70888be375a003d21fe468e70"},
    "data-dictionary.csv": {"bytes": 8148, "sha256": "1ae498e5a8f084bacb5e34a65d716b70747116c73d03fc3e25c7326712e0fdab"},
    "synthetic-source-manifest.csv": {"bytes": 1606, "sha256": "c3f7549f6fcc25e0bfd5f074a7f936e519a0bd7f9459452da903c653aee28384"},
}

GROUPS = (
    ("race_ethnicity", "Combined race and ethnicity", "american_indian_alaska_native", "American Indian or Alaska Native", 1, 0.012, 1.18, 0, 0),
    ("race_ethnicity", "Combined race and ethnicity", "asian", "Asian", 2, 0.075, 0.84, 0, 0),
    ("race_ethnicity", "Combined race and ethnicity", "black_african_american", "Black or African American", 3, 0.090, 1.22, 0, 0),
    ("race_ethnicity", "Combined race and ethnicity", "hispanic_latino", "Hispanic or Latino", 4, 0.130, 1.15, 0, 0),
    ("race_ethnicity", "Combined race and ethnicity", "middle_eastern_north_african", "Middle Eastern or North African", 5, 0.020, 0.92, 0, 0),
    ("race_ethnicity", "Combined race and ethnicity", "native_hawaiian_pacific_islander", "Native Hawaiian or Pacific Islander", 6, 0.004, 1.10, 0, 0),
    ("race_ethnicity", "Combined race and ethnicity", "white", "White", 7, 0.590, 0.88, 0, 1),
    ("race_ethnicity", "Combined race and ethnicity", "multiple_identities", "Multiple identities", 8, 0.045, 1.05, 0, 0),
    ("race_ethnicity", "Combined race and ethnicity", "missing", "Missing", 9, 0.034, 1.00, 1, 0),
    ("primary_language", "Primary language", "english", "English", 1, 0.740, 0.95, 0, 1),
    ("primary_language", "Primary language", "spanish", "Spanish", 2, 0.100, 1.16, 0, 0),
    ("primary_language", "Primary language", "portuguese", "Portuguese", 3, 0.050, 1.11, 0, 0),
    ("primary_language", "Primary language", "haitian_creole", "Haitian Creole", 4, 0.025, 1.20, 0, 0),
    ("primary_language", "Primary language", "chinese", "Chinese", 5, 0.025, 0.90, 0, 0),
    ("primary_language", "Primary language", "other_language", "Another language", 6, 0.040, 1.08, 0, 0),
    ("primary_language", "Primary language", "missing", "Missing", 7, 0.020, 1.00, 1, 0),
    ("disability_status", "Disability status", "reported_disability", "Reported disability", 1, 0.170, 1.35, 0, 0),
    ("disability_status", "Disability status", "no_reported_disability", "No reported disability", 2, 0.800, 0.90, 0, 1),
    ("disability_status", "Disability status", "missing", "Missing", 3, 0.030, 1.00, 1, 0),
)

MARGIN_FIELDS = [
    "equity_margin_id", "case_id", "tract_fips", "age_band_id", "age_band",
    "band_order", "period", "equity_dimension", "dimension_label", "group_id",
    "group_label", "group_order", "population_count", "synthetic_event_count",
    "base_share", "risk_multiplier", "generator_version", "seed", "synthetic_flag",
    "margin_only", "claim_limit",
]
COMPLETENESS_FIELDS = [
    "completeness_id", "case_id", "tract_fips", "age_band_id", "age_band",
    "band_order", "period", "synthetic_event_count", "race_missing_count",
    "ethnicity_missing_count", "primary_language_missing_count",
    "disability_status_missing_count", "tract_geography_missing_count",
    "generator_version", "seed", "synthetic_flag", "analytic_universe",
    "claim_limit",
]
GROUP_FIELDS = [
    "equity_dimension", "dimension_label", "group_id", "group_label", "group_order",
    "base_share", "risk_multiplier", "missing_group", "primary_reference",
    "analysis_role", "claim_limit",
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


def open_csv(path: Path):
    return gzip.open(path, "rt", encoding="utf-8", newline="") if path.suffix == ".gz" else path.open(encoding="utf-8", newline="")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with open_csv(path) as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def allocate(total: int, weights: list[float]) -> list[int]:
    require(total >= 0 and all(weight >= 0 for weight in weights) and sum(weights) > 0, "Invalid allocation inputs")
    normalized = [weight / sum(weights) for weight in weights]
    raw = [total * weight for weight in normalized]
    result = [math.floor(value) for value in raw]
    for index in sorted(range(len(raw)), key=lambda item: (-(raw[item] - result[item]), item))[: total - sum(result)]:
        result[index] += 1
    require(sum(result) == total, "Largest-remainder allocation failed")
    return result


def allocate_events(total: int, populations: list[int], multipliers: list[float], rng: random.Random) -> list[int]:
    remaining = populations.copy()
    result = [0] * len(populations)
    require(total <= sum(remaining), "Event total exceeds the generated population")
    for _ in range(total):
        weights = [population * multiplier for population, multiplier in zip(remaining, multipliers)]
        threshold = rng.random() * sum(weights)
        cumulative = 0.0
        selected = len(weights) - 1
        for index, weight in enumerate(weights):
            cumulative += weight
            if threshold < cumulative:
                selected = index
                break
        result[selected] += 1
        remaining[selected] -= 1
    require(sum(result) == total and all(count <= population for count, population in zip(result, populations)), "Constrained event allocation failed")
    return result


def group_contract_rows() -> list[dict[str, object]]:
    rows = []
    for dimension, label, group_id, group_label, order, share, multiplier, missing, reference in GROUPS:
        rows.append({
            "equity_dimension": dimension,
            "dimension_label": label,
            "group_id": group_id,
            "group_label": group_label,
            "group_order": order,
            "base_share": f"{share:.6f}",
            "risk_multiplier": f"{multiplier:.6f}",
            "missing_group": missing,
            "primary_reference": reference,
            "analysis_role": "missingness audit only" if missing else "reported synthetic comparison group",
            "claim_limit": "fictional marginal group; not a person record, Massachusetts demographic estimate, biological trait, eligibility category, or allocation signal",
        })
    return rows


def dictionary_rows() -> list[dict[str, object]]:
    definitions = {
        "synthetic-equity-margins": {
            "equity_margin_id": ("text", "no", "Stable generated tract-age-dimension-group row identifier"),
            "case_id": ("text", "no", "Fictional planning case identifier"),
            "tract_fips": ("text", "no", "Accepted eleven-character Census tract key"),
            "age_band_id": ("text", "no", "Accepted adult age-band identifier"),
            "age_band": ("text", "no", "Accepted adult age-band label"),
            "band_order": ("integer", "no", "Age-band calculation order"),
            "period": ("text", "no", "Fictional event period"),
            "equity_dimension": ("text", "no", "One separate marginal equity dimension"),
            "dimension_label": ("text", "no", "Human-readable dimension label"),
            "group_id": ("text", "no", "Stable generated group identifier"),
            "group_label": ("text", "no", "Human-readable generated group label"),
            "group_order": ("integer", "no", "Display order within dimension"),
            "population_count": ("integer", "no", "Generated marginal population count that reconciles to the accepted denominator"),
            "synthetic_event_count": ("integer", "no", "Generated marginal event count that reconciles to the accepted numerator"),
            "base_share": ("decimal", "no", "Fixed generator share before seeded tract variation"),
            "risk_multiplier": ("decimal", "no", "Fixed generator multiplier used only to allocate synthetic events"),
            "generator_version": ("text", "no", "Generator semantic version"),
            "seed": ("integer", "no", "Generator seed"),
            "synthetic_flag": ("integer", "no", "One for every row"),
            "margin_only": ("integer", "no", "One; dimensions cannot be joined into person-level combinations"),
            "claim_limit": ("text", "no", "Prohibition on real identity, disparity, eligibility, and allocation claims"),
        },
        "synthetic-field-completeness": {
            "completeness_id": ("text", "no", "Stable generated tract-age completeness row identifier"),
            "case_id": ("text", "no", "Fictional planning case identifier"),
            "tract_fips": ("text", "no", "Accepted Census tract key for the conditioned analytic universe"),
            "age_band_id": ("text", "no", "Accepted adult age-band identifier"),
            "age_band": ("text", "no", "Accepted adult age-band label"),
            "band_order": ("integer", "no", "Age-band calculation order"),
            "period": ("text", "no", "Fictional event period"),
            "synthetic_event_count": ("integer", "no", "Accepted generated event count"),
            "race_missing_count": ("integer", "no", "Generated event records missing race"),
            "ethnicity_missing_count": ("integer", "no", "Generated event records missing ethnicity"),
            "primary_language_missing_count": ("integer", "no", "Generated event records missing primary language"),
            "disability_status_missing_count": ("integer", "no", "Generated event records missing disability status"),
            "tract_geography_missing_count": ("integer", "no", "Zero by construction because the analytic universe is conditioned on tract linkage"),
            "generator_version": ("text", "no", "Generator semantic version"),
            "seed": ("integer", "no", "Generator seed"),
            "synthetic_flag": ("integer", "no", "One for every row"),
            "analytic_universe": ("text", "no", "Conditioned linked analytic universe"),
            "claim_limit": ("text", "no", "Missingness counts do not establish capture quality or real group identity"),
        },
    }
    rows = []
    for source_id, fields in definitions.items():
        for order, (field, (kind, nullable, definition)) in enumerate(fields.items(), start=1):
            rows.append({
                "source_id": source_id,
                "field_order": order,
                "field_name": field,
                "type": kind,
                "nullable": nullable,
                "definition": definition,
                "claim_limit": "Synthetic aggregate teaching data only; no person, community, clinical, eligibility, or allocation inference.",
            })
    return rows


def load_upstream(root: Path) -> list[dict[str, str]]:
    reference = root / "upstream/module02-reference/outputs"
    _, denominators = read_csv(reference / "age-band-denominators.csv.gz")
    _, events = read_csv(reference / "synthetic-event-linkage.csv.gz")
    event_map = {(row["tract_fips"], row["age_band_id"]): row for row in events}
    require(len(denominators) == len(events) == 7985, "Frozen Module 02 tract-age shape changed")
    rows = []
    for denominator in denominators:
        key = (denominator["tract_fips"], denominator["age_band_id"])
        event = event_map.get(key)
        require(event is not None and event["denominator_match"] == "1", f"Missing accepted event row: {key}")
        require(int(event["denominator_estimate"]) == int(denominator["denominator_estimate"]), f"Accepted denominator mismatch: {key}")
        rows.append({**denominator, "synthetic_event_count": event["synthetic_event_count"], "period": event["period"]})
    require(sum(int(row["denominator_estimate"]) for row in rows) == 5679768, "Frozen adult denominator changed")
    require(sum(int(row["synthetic_event_count"]) for row in rows) == 283614, "Frozen generated-event total changed")
    return rows


def build_rows(root: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    upstream = load_upstream(root)
    by_dimension: dict[str, list[tuple]] = defaultdict(list)
    for group in GROUPS:
        by_dimension[group[0]].append(group)
    margins = []
    completeness = []
    for row in upstream:
        tract = row["tract_fips"]
        age_id = row["age_band_id"]
        denominator = int(row["denominator_estimate"])
        events = int(row["synthetic_event_count"])
        for dimension, groups in by_dimension.items():
            weights = []
            for group in groups:
                rng = random.Random(stable_seed(SEED, tract, age_id, dimension, group[2], "share"))
                weights.append(group[5] * (1.0 + rng.uniform(-0.18, 0.18)))
            populations = allocate(denominator, weights)
            event_rng = random.Random(stable_seed(SEED, tract, age_id, dimension, "events"))
            event_counts = allocate_events(events, populations, [group[6] for group in groups], event_rng)
            require(all(count <= population for count, population in zip(event_counts, populations)), f"Generated events exceed group population: {tract} {age_id} {dimension}")
            for group, population, count in zip(groups, populations, event_counts):
                margins.append({
                    "equity_margin_id": f"EM-{tract}-{age_id}-{dimension}-{group[2]}",
                    "case_id": "FMA-DP-01",
                    "tract_fips": tract,
                    "age_band_id": age_id,
                    "age_band": row["age_band"],
                    "band_order": row["band_order"],
                    "period": row["period"],
                    "equity_dimension": dimension,
                    "dimension_label": group[1],
                    "group_id": group[2],
                    "group_label": group[3],
                    "group_order": group[4],
                    "population_count": population,
                    "synthetic_event_count": count,
                    "base_share": f"{group[5]:.6f}",
                    "risk_multiplier": f"{group[6]:.6f}",
                    "generator_version": GENERATOR_VERSION,
                    "seed": SEED,
                    "synthetic_flag": 1,
                    "margin_only": 1,
                    "claim_limit": "fictional marginal aggregate; not a person record, observed disparity, eligibility category, or allocation signal",
                })
        rates = {
            "race": 0.022,
            "ethnicity": 0.027,
            "primary_language": 0.020,
            "disability_status": 0.030,
        }
        missing = {}
        for field, base_rate in rates.items():
            rng = random.Random(stable_seed(SEED, tract, age_id, field, "missing"))
            missing[field] = min(events, round(events * max(0.0, base_rate + rng.uniform(-0.008, 0.008))))
        completeness.append({
            "completeness_id": f"FC-{tract}-{age_id}",
            "case_id": "FMA-DP-01",
            "tract_fips": tract,
            "age_band_id": age_id,
            "age_band": row["age_band"],
            "band_order": row["band_order"],
            "period": row["period"],
            "synthetic_event_count": events,
            "race_missing_count": missing["race"],
            "ethnicity_missing_count": missing["ethnicity"],
            "primary_language_missing_count": missing["primary_language"],
            "disability_status_missing_count": missing["disability_status"],
            "tract_geography_missing_count": 0,
            "generator_version": GENERATOR_VERSION,
            "seed": SEED,
            "synthetic_flag": 1,
            "analytic_universe": "accepted Module 02 tract-linked synthetic event aggregates",
            "claim_limit": "zero geography missingness is conditioned on linkage and does not prove complete real-world capture",
        })
    require(len(margins) == 151715 and len(completeness) == 7985, "Synthetic equity release row shape changed")
    return margins, completeness


def write_release(root: Path, target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    margins, completeness = build_rows(root.resolve())
    (target / "raw").mkdir(parents=True)
    payloads = []
    for source_id, relative, fields, rows, compressed in (
        ("synthetic-equity-margins", "raw/synthetic-equity-margins.csv.gz", MARGIN_FIELDS, margins, True),
        ("synthetic-field-completeness", "raw/synthetic-field-completeness.csv.gz", COMPLETENESS_FIELDS, completeness, True),
        ("equity-group-contract", "equity-group-contract.csv", GROUP_FIELDS, group_contract_rows(), False),
        ("equity-data-dictionary", "data-dictionary.csv", DICTIONARY_FIELDS, dictionary_rows(), False),
    ):
        raw = csv_bytes(fields, rows)
        value = deterministic_gzip(raw) if compressed else raw
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value)
        payloads.append((source_id, relative, len(rows), len(fields), raw, value))
    manifest = []
    for source_id, relative, row_count, column_count, raw, value in payloads:
        manifest.append({
            "source_id": source_id,
            "relative_path": f"data/{relative}",
            "format": "deterministic gzip CSV" if relative.endswith(".gz") else "CSV",
            "rows": row_count,
            "columns": column_count,
            "bytes": len(value),
            "sha256": sha256_bytes(value),
            "content_bytes": len(raw),
            "content_sha256": sha256_bytes(raw),
            "generator_version": GENERATOR_VERSION,
            "seed": SEED,
            "synthetic_flag": 1,
            "period": PERIOD,
            "claim_limit": "fictional marginal aggregate teaching source; no person, observed disparity, eligibility, targeting, or allocation claim",
        })
    manifest_raw = csv_bytes(MANIFEST_FIELDS, manifest)
    (target / "synthetic-source-manifest.csv").write_bytes(manifest_raw)
    return {
        "margin_rows": len(margins),
        "completeness_rows": len(completeness),
        "groups": len(GROUPS),
        "dimensions": len({group[0] for group in GROUPS}),
        "source_manifest_sha256": sha256_bytes(manifest_raw),
        "files": {relative: {"bytes": len(value), "sha256": sha256_bytes(value)} for _, relative, _, _, _, value in payloads} | {
            "synthetic-source-manifest.csv": {"bytes": len(manifest_raw), "sha256": sha256_bytes(manifest_raw)}
        },
    }


def verify(root: Path = ROOT) -> dict[str, object]:
    data = root.resolve() / "data"
    manifest_path = data / "synthetic-source-manifest.csv"
    header, manifest = read_csv(manifest_path)
    require(header == MANIFEST_FIELDS and len(manifest) == 4, "Synthetic source manifest changed")
    for row in manifest:
        path = root.resolve() / row["relative_path"]
        require(path.is_file() and path.stat().st_size == int(row["bytes"]), f"Synthetic source bytes changed: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Synthetic source SHA-256 changed: {row['relative_path']}")
        require(row["generator_version"] == GENERATOR_VERSION and int(row["seed"]) == SEED and row["synthetic_flag"] == "1", "Synthetic source identity changed")
    if EXPECTED_FILES:
        for relative, expected in EXPECTED_FILES.items():
            path = data / relative
            require(path.stat().st_size == expected["bytes"] and sha256(path) == expected["sha256"], f"Pinned synthetic file changed: {relative}")

    _, margins = read_csv(data / "raw/synthetic-equity-margins.csv.gz")
    _, completeness = read_csv(data / "raw/synthetic-field-completeness.csv.gz")
    _, groups = read_csv(data / "equity-group-contract.csv")
    require(len(margins) == 151715 and len(completeness) == 7985 and len(groups) == 19, "Synthetic equity source shape changed")
    totals: dict[tuple[str, str, str], list[int]] = defaultdict(lambda: [0, 0])
    for row in margins:
        require(row["synthetic_flag"] == "1" and row["margin_only"] == "1", "Synthetic margin flag changed")
        key = (row["tract_fips"], row["age_band_id"], row["equity_dimension"])
        totals[key][0] += int(row["population_count"])
        totals[key][1] += int(row["synthetic_event_count"])
    upstream = load_upstream(root.resolve())
    expected = {(row["tract_fips"], row["age_band_id"]): (int(row["denominator_estimate"]), int(row["synthetic_event_count"])) for row in upstream}
    require(len(totals) == 23955, "Synthetic margin key count changed")
    for (tract, age_id, _), values in totals.items():
        require(tuple(values) == expected[(tract, age_id)], f"Synthetic margin reconciliation failed: {tract} {age_id}")
    return {
        "margin_rows": len(margins),
        "completeness_rows": len(completeness),
        "groups": len(groups),
        "dimensions": 3,
        "adult_denominator_per_dimension": sum(int(row["population_count"]) for row in margins) // 3,
        "synthetic_events_per_dimension": sum(int(row["synthetic_event_count"]) for row in margins) // 3,
        "source_manifest_sha256": sha256(manifest_path),
        "files": {Path(row["relative_path"]).relative_to("data").as_posix(): {"bytes": int(row["bytes"]), "sha256": row["sha256"]} for row in manifest} | {
            "synthetic-source-manifest.csv": {"bytes": manifest_path.stat().st_size, "sha256": sha256(manifest_path)}
        },
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module03-equity-") as temp_dir:
        base = Path(temp_dir)
        first = write_release(ROOT, base / "first")
        second = write_release(ROOT, base / "second")
        require(first == second, "Two synthetic equity builds differ")
        for relative in first["files"]:
            require((base / "first" / relative).read_bytes() == (base / "second" / relative).read_bytes(), f"Synthetic build differs: {relative}")
            require((base / "first" / relative).read_bytes() == (ROOT / "data" / relative).read_bytes(), f"Committed synthetic file differs: {relative}")
        try:
            write_release(ROOT, base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Synthetic generator did not protect an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 03 synthetic-source self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.write:
            print(json.dumps(write_release(args.root, args.target or (args.root / "data")), indent=2, sort_keys=True))
        else:
            print(json.dumps(verify(args.root), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, SourceError) as error:
        parser.exit(1, f"Synthetic equity release failed: {error}\n")


if __name__ == "__main__":
    main()
