#!/usr/bin/env python3
"""Build the DA-730 Module 09 CDC PLACES comparison releases."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import urllib.parse
import urllib.request
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
DATASET_ID = "fu4u-a9bh"
LANDING_PAGE = "https://data.cdc.gov/d/fu4u-a9bh"
API_BASE = f"https://data.cdc.gov/resource/{DATASET_ID}.csv"
MEASURES = ("CSMOKING", "DIABETES", "GHLTH", "LPA", "OBESITY")
MEASURE_LABELS = {
    "CSMOKING": "Current smoking",
    "DIABETES": "Diagnosed diabetes",
    "GHLTH": "Fair or poor health",
    "LPA": "No leisure activity",
    "OBESITY": "Obesity",
}
EXPECTED_RAW_SHA256 = "897064d10703b870afe6d55f4cf0bc7e08d1c91f5d3490584952894df3f6de4b"
DEFAULT_ALL_OUTPUT = MODULE_ROOT / "data" / "places_county_comparison_2024.csv"
DEFAULT_NC_OUTPUT = MODULE_ROOT / "data" / "nc_county_health_profiles_2024.csv"

SOURCE_FIELDS = (
    "year",
    "stateabbr",
    "statedesc",
    "locationname",
    "locationid",
    "measureid",
    "measure",
    "data_value_type",
    "datavaluetypeid",
    "data_value",
    "low_confidence_limit",
    "high_confidence_limit",
    "totalpopulation",
    "totalpop18plus",
    "data_value_footnote_symbol",
    "data_value_footnote",
)

TEACHING_FIELDS = (
    "county_fips",
    "county_name",
    "state_abbr",
    "state_name",
    "measure_id",
    "measure_name",
    "measure_label",
    "measure_year",
    "adult_population",
    "crude_prevalence_pct",
    "crude_low_ci_pct",
    "crude_high_ci_pct",
    "age_adjusted_prevalence_pct",
    "age_adjusted_low_ci_pct",
    "age_adjusted_high_ci_pct",
    "national_age_adjusted_pct",
    "national_age_adjusted_low_ci_pct",
    "national_age_adjusted_high_ci_pct",
    "difference_from_national_pct_points",
    "rank_descending_point_estimate",
    "counties_compared",
    "point_estimate_above_national",
    "measures_above_national",
    "largest_gap_measure_id",
    "largest_gap_pct_points",
    "profile_order",
    "source_footnote",
)


def query_url() -> str:
    quoted = ",".join(f"'{measure}'" for measure in MEASURES)
    params = {
        "$select": ",".join(SOURCE_FIELDS),
        "$where": f"measureid in({quoted})",
        "$order": "measureid,locationid,datavaluetypeid",
        "$limit": "50000",
    }
    return f"{API_BASE}?{urllib.parse.urlencode(params)}"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "OpenClinicalLearningCommons/0.20"})
    with urllib.request.urlopen(request, timeout=180) as response:
        return response.read()


def decimal_text(value: str) -> str:
    if not value:
        return ""
    return f"{Decimal(value).quantize(Decimal('0.1')):.1f}"


def integer_text(value: str) -> str:
    if not value:
        return ""
    return str(int(Decimal(value)))


def normalize(row: dict[str, str]) -> dict[str, str]:
    result = {field: row.get(field, "").strip() for field in SOURCE_FIELDS}
    for field in ("data_value", "low_confidence_limit", "high_confidence_limit"):
        result[field] = decimal_text(result[field])
    for field in ("totalpopulation", "totalpop18plus"):
        result[field] = integer_text(result[field])
    return result


def write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def competition_ranks(rows: list[dict[str, str]]) -> dict[str, int]:
    values = [Decimal(row["age_adjusted_prevalence_pct"]) for row in rows]
    ranks = {value: 1 + sum(other > value for other in values) for value in set(values)}
    return {row["county_fips"]: ranks[Decimal(row["age_adjusted_prevalence_pct"])] for row in rows}


def make_nc(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    national = {
        row["measureid"]: row
        for row in rows
        if row["locationid"] == "59" and row["datavaluetypeid"] == "AgeAdjPrv"
    }
    if set(national) != set(MEASURES):
        raise SystemExit("Expected one national age-adjusted reference for every measure.")

    pairs: dict[tuple[str, str], dict[str, dict[str, str]]] = defaultdict(dict)
    for row in rows:
        if row["stateabbr"] == "NC":
            pairs[(row["locationid"], row["measureid"])][row["datavaluetypeid"]] = row
    if len(pairs) != 500 or any(set(pair) != {"CrdPrv", "AgeAdjPrv"} for pair in pairs.values()):
        raise SystemExit("Expected crude and age-adjusted rows for 100 counties and five measures.")

    teaching: list[dict[str, str]] = []
    for (county_fips, measure_id), pair in sorted(pairs.items()):
        crude = pair["CrdPrv"]
        adjusted = pair["AgeAdjPrv"]
        reference = national[measure_id]
        if crude["locationname"] != adjusted["locationname"]:
            raise SystemExit("County names do not match within a crude and adjusted pair.")
        if crude["totalpop18plus"] != adjusted["totalpop18plus"]:
            raise SystemExit("Adult populations do not match within a crude and adjusted pair.")
        gap = Decimal(adjusted["data_value"]) - Decimal(reference["data_value"])
        footnotes = " | ".join(
            dict.fromkeys(value for value in (crude["data_value_footnote"], adjusted["data_value_footnote"]) if value)
        )
        teaching.append(
            {
                "county_fips": county_fips,
                "county_name": adjusted["locationname"],
                "state_abbr": adjusted["stateabbr"],
                "state_name": adjusted["statedesc"],
                "measure_id": measure_id,
                "measure_name": adjusted["measure"],
                "measure_label": MEASURE_LABELS[measure_id],
                "measure_year": adjusted["year"],
                "adult_population": adjusted["totalpop18plus"],
                "crude_prevalence_pct": crude["data_value"],
                "crude_low_ci_pct": crude["low_confidence_limit"],
                "crude_high_ci_pct": crude["high_confidence_limit"],
                "age_adjusted_prevalence_pct": adjusted["data_value"],
                "age_adjusted_low_ci_pct": adjusted["low_confidence_limit"],
                "age_adjusted_high_ci_pct": adjusted["high_confidence_limit"],
                "national_age_adjusted_pct": reference["data_value"],
                "national_age_adjusted_low_ci_pct": reference["low_confidence_limit"],
                "national_age_adjusted_high_ci_pct": reference["high_confidence_limit"],
                "difference_from_national_pct_points": f"{gap:.1f}",
                "rank_descending_point_estimate": "",
                "counties_compared": "100",
                "point_estimate_above_national": "yes" if gap > 0 else "no",
                "measures_above_national": "",
                "largest_gap_measure_id": "",
                "largest_gap_pct_points": "",
                "profile_order": "",
                "source_footnote": footnotes,
            }
        )

    by_measure: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_county: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in teaching:
        by_measure[row["measure_id"]].append(row)
        by_county[row["county_fips"]].append(row)
    for measure_rows in by_measure.values():
        ranks = competition_ranks(measure_rows)
        for row in measure_rows:
            row["rank_descending_point_estimate"] = str(ranks[row["county_fips"]])

    profiles: dict[str, tuple[int, Decimal, str]] = {}
    for county_fips, county_rows in by_county.items():
        above = sum(row["point_estimate_above_national"] == "yes" for row in county_rows)
        largest = max(county_rows, key=lambda row: (Decimal(row["difference_from_national_pct_points"]), row["measure_id"]))
        largest_gap = Decimal(largest["difference_from_national_pct_points"])
        profiles[county_fips] = (above, largest_gap, largest["measure_id"])
        for row in county_rows:
            row["measures_above_national"] = str(above)
            row["largest_gap_measure_id"] = largest["measure_id"]
            row["largest_gap_pct_points"] = f"{largest_gap:.1f}"

    county_names = {row["county_fips"]: row["county_name"] for row in teaching}
    ordered_counties = sorted(
        profiles,
        key=lambda county_fips: (
            -profiles[county_fips][0],
            -profiles[county_fips][1],
            county_names[county_fips],
        ),
    )
    profile_order = {county_fips: index for index, county_fips in enumerate(ordered_counties, start=1)}
    for row in teaching:
        row["profile_order"] = str(profile_order[row["county_fips"]])

    teaching.sort(key=lambda row: (int(row["profile_order"]), MEASURES.index(row["measure_id"])))
    return teaching


def build(raw_input: Path | None, all_output: Path, nc_output: Path) -> None:
    url = query_url()
    raw = raw_input.read_bytes() if raw_input else download(url)
    raw_sha = sha256_bytes(raw)
    if EXPECTED_RAW_SHA256 and raw_sha != EXPECTED_RAW_SHA256:
        raise SystemExit(f"Pinned CDC PLACES query checksum changed: {raw_sha}")

    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    if tuple(reader.fieldnames or ()) != SOURCE_FIELDS:
        raise SystemExit("CDC PLACES query columns changed.")
    rows = [normalize(row) for row in reader]
    if len(rows) != 31450:
        raise SystemExit(f"Expected 31,450 selected rows; received {len(rows):,}.")
    if {row["measureid"] for row in rows} != set(MEASURES):
        raise SystemExit("CDC PLACES selected measure set changed.")
    if {row["datavaluetypeid"] for row in rows} != {"CrdPrv", "AgeAdjPrv"}:
        raise SystemExit("Expected crude and age-adjusted value types.")
    if {row["year"] for row in rows} != {"2022"}:
        raise SystemExit("Expected one common 2022 measure year.")
    if any(not row["data_value"] for row in rows):
        raise SystemExit("Selected PLACES estimates unexpectedly contain unavailable values.")

    teaching = make_nc(rows)
    if len(teaching) != 500:
        raise SystemExit(f"Expected 500 North Carolina county-measure rows; received {len(teaching)}.")

    write_csv(all_output, SOURCE_FIELDS, rows)
    write_csv(nc_output, TEACHING_FIELDS, teaching)

    print(f"Pinned query: {url}")
    print(f"Raw bytes: {len(raw):,}")
    print(f"Raw SHA-256: {raw_sha}")
    print(f"Selected rows: {len(rows):,}; SHA-256: {sha256_file(all_output)}")
    print(f"North Carolina rows: {len(teaching):,}; SHA-256: {sha256_file(nc_output)}")
    if not EXPECTED_RAW_SHA256:
        print("Bootstrap build only: record and pin the raw checksum before release.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-input", type=Path)
    parser.add_argument("--all-output", type=Path, default=DEFAULT_ALL_OUTPUT)
    parser.add_argument("--nc-output", type=Path, default=DEFAULT_NC_OUTPUT)
    args = parser.parse_args()
    build(
        args.raw_input.resolve() if args.raw_input else None,
        args.all_output.resolve(),
        args.nc_output.resolve(),
    )


if __name__ == "__main__":
    main()
