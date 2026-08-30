#!/usr/bin/env python3
"""Validate the released data contract for DA-730 Module 05."""

from __future__ import annotations

import csv
import hashlib
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
EXPECTED_HASHES = {
    "places_diabetes_county_2024.csv": "764b46c63508a5a6a2510ee2766866ab91abdeeaf7d633f50ae70a3aff561de6",
    "acs_adult_population_county_2024.csv": "1efa6d51591bf2941c22d09a6e8a86f70f6405f753bf59b60a0a6e99d45b24a2",
    "nc_county_boundaries_2024.csv": "6eb085f49b400d4ecf6f88646f51dd01fdd4154533262e66ade02b1d1d8f666f",
    "nc_diabetes_rates_2024.csv": "1528b204830966dff88e00f57fc4f77b8dcf5db135daa122e8aff3679fdf32c7",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(name: str) -> tuple[list[str], list[dict[str, str]]]:
    path = DATA / name
    with path.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        return list(reader.fieldnames or []), list(reader)


def rank(rows: list[dict[str, str]], field: str) -> dict[str, int]:
    ordered = sorted(rows, key=lambda row: (-float(row[field]), row["county_fips"]))
    return {row["county_fips"]: index for index, row in enumerate(ordered, start=1)}


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def record(name: str, passed: bool, result: object) -> None:
        checks.append((name, bool(passed), str(result)))

    for name, expected in EXPECTED_HASHES.items():
        actual = sha256(DATA / name)
        record(f"hash {name}", actual == expected, actual)

    places_fields, places = read_csv("places_diabetes_county_2024.csv")
    county_places = [row for row in places if len(row["locationid"]) == 5]
    national = [row for row in places if len(row["locationid"]) != 5]
    record("PLACES rows", len(places) == 6290, len(places))
    record("PLACES county rows", len(county_places) == 6288, len(county_places))
    record("PLACES county identities", len({row["locationid"] for row in county_places}) == 3144, len({row["locationid"] for row in county_places}))
    record("PLACES national summary", len(national) == 2 and {row["datavaluetypeid"] for row in national} == {"CrdPrv", "AgeAdjPrv"}, len(national))
    record("PLACES measure", {row["measureid"] for row in places} == {"DIABETES"}, {row["measureid"] for row in places})
    record("PLACES value types", {row["datavaluetypeid"] for row in places} == {"CrdPrv", "AgeAdjPrv"}, {row["datavaluetypeid"] for row in places})
    record("PLACES source fields", len(places_fields) == 16, ", ".join(places_fields))

    acs_fields, acs = read_csv("acs_adult_population_county_2024.csv")
    record("ACS rows", len(acs) == 3222, len(acs))
    record("ACS unique counties", len({row["county_fips"] for row in acs}) == 3222, len({row["county_fips"] for row in acs}))
    record("ACS FIPS format", all(len(row["county_fips"]) == 5 for row in acs), "five characters")
    record("ACS status field", "acs_moe_status" in acs_fields, "present" if "acs_moe_status" in acs_fields else "missing")

    teaching_fields, teaching = read_csv("nc_diabetes_rates_2024.csv")
    required = {
        "county_fips",
        "county_name",
        "places_adult_population",
        "crude_prevalence_pct",
        "crude_low_95_pct",
        "crude_high_95_pct",
        "age_adjusted_prevalence_pct",
        "age_adjusted_low_95_pct",
        "age_adjusted_high_95_pct",
        "modeled_adult_count",
        "acs_adult_population",
        "acs_adult_moe90",
        "acs_65plus_share_adult_pct",
        "teaching_low_denominator_flag",
        "count_status",
    }
    record("teaching fields", required.issubset(teaching_fields), ", ".join(teaching_fields))
    record("teaching rows", len(teaching) == 100, len(teaching))
    record("teaching county identities", len({row["county_fips"] for row in teaching}) == 100, len({row["county_fips"] for row in teaching}))
    record("North Carolina only", {row["state_abbr"] for row in teaching} == {"NC"}, {row["state_abbr"] for row in teaching})
    record("measure contract", {row["measure_id"] for row in teaching} == {"DIABETES"} and {row["measure_year"] for row in teaching} == {"2022"}, "DIABETES 2022")

    intervals_pass = all(
        float(row["crude_low_95_pct"]) <= float(row["crude_prevalence_pct"]) <= float(row["crude_high_95_pct"])
        and float(row["age_adjusted_low_95_pct"]) <= float(row["age_adjusted_prevalence_pct"]) <= float(row["age_adjusted_high_95_pct"])
        for row in teaching
    )
    record("source intervals contain estimates", intervals_pass, "100 counties")

    count_pass = all(
        int(row["modeled_adult_count"])
        == round(float(row["crude_prevalence_pct"]) / 100 * int(row["places_adult_population"]))
        for row in teaching
    )
    record("modeled count formula", count_pass, "round(crude / 100 * PLACES adults)")
    record("modeled count label", {row["count_status"] for row in teaching} == {"modeled estimate, not observed cases"}, "explicit")
    record("ACS margins available in teaching case", all(row["acs_moe_status"] == "reported" and row["acs_adult_moe90"] for row in teaching), "100 counties")

    low = [row for row in teaching if row["teaching_low_denominator_flag"] == "1"]
    record("training denominator rule", len(low) == 9 and all(int(row["places_adult_population"]) < 10000 for row in low), len(low))

    count_rank = rank(teaching, "modeled_adult_count")
    crude_rank = rank(teaching, "crude_prevalence_pct")
    adjusted_rank = rank(teaching, "age_adjusted_prevalence_pct")
    largest_count_shift = max(abs(count_rank[fips] - adjusted_rank[fips]) for fips in count_rank)
    largest_crude_shift = max(abs(crude_rank[fips] - adjusted_rank[fips]) for fips in crude_rank)
    top_count = {fips for fips, value in count_rank.items() if value <= 12}
    top_adjusted = {fips for fips, value in adjusted_rank.items() if value <= 12}
    record("count to adjusted rank shift", largest_count_shift >= 80, largest_count_shift)
    record("crude to adjusted rank shift", largest_crude_shift >= 40, largest_crude_shift)
    record("top-12 quantity contrast", len(top_count & top_adjusted) == 0, len(top_count & top_adjusted))

    boundary_fields, boundaries = read_csv("nc_county_boundaries_2024.csv")
    boundary_fips = {row["county_fips"] for row in boundaries}
    record("boundary fields", boundary_fields == ["county_fips", "county_name", "polygon_group", "point_order", "longitude", "latitude"], ", ".join(boundary_fields))
    record("boundary rows", len(boundaries) == 7121, len(boundaries))
    record("boundary county coverage", boundary_fips == {row["county_fips"] for row in teaching}, len(boundary_fips))
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in boundaries:
        groups[row["polygon_group"]].append(row)
    closed = all(
        group[0]["longitude"] == group[-1]["longitude"]
        and group[0]["latitude"] == group[-1]["latitude"]
        and [int(row["point_order"]) for row in group] == list(range(1, len(group) + 1))
        for group in groups.values()
    )
    record("closed ordered boundary parts", closed, len(groups))

    print("DA-730 Module 05 validation report")
    for name, passed, result in checks:
        print(f"{'PASS' if passed else 'FAIL'}\t{name}\t{result}")
    failures = [name for name, passed, _ in checks if not passed]
    if failures:
        print(f"FAILED: {len(failures)} checks: {', '.join(failures)}", file=sys.stderr)
        return 1

    top = sorted(teaching, key=lambda row: (-float(row["age_adjusted_prevalence_pct"]), row["county_fips"]))[:12]
    print("Recommended comparison shortlist: " + ", ".join(row["county_name"] for row in top))
    print(f"PASS: {len(checks)} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
