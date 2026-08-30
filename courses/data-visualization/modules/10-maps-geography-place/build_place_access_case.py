#!/usr/bin/env python3
"""Build the DA-730 Module 10 North Carolina place and access releases."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import shutil
import urllib.request
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
MODULES_ROOT = MODULE_ROOT.parent
PLACES_INPUT = MODULES_ROOT / "09-comparison-small-multiples" / "data" / "nc_county_health_profiles_2024.csv"
BOUNDARY_INPUT = MODULES_ROOT / "05-rates-denominators-adjustment" / "data" / "nc_county_boundaries_2024.csv"
HPSA_URL = "https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv"
HPSA_METADATA_URL = "https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX"
EXPECTED_PLACES_SHA256 = "33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9"
EXPECTED_BOUNDARY_SHA256 = "6eb085f49b400d4ecf6f88646f51dd01fdd4154533262e66ade02b1d1d8f666f"
EXPECTED_HPSA_FULL_SHA256 = "4552ebf09bc5a40d79d71df8ea84aea165de2205953615e03571ad84f1d6b132"
EXPECTED_HPSA_SELECTED_SHA256 = "061fe5e18bc9cd58bd89256c686ddefbce6d77972c1139b1b339497f2eab5445"

DEFAULT_HPSA_OUTPUT = MODULE_ROOT / "data" / "hpsa_primary_care_nc_2026_08_29.csv"
DEFAULT_TEACHING_OUTPUT = MODULE_ROOT / "data" / "nc_place_access_2026.csv"
DEFAULT_BOUNDARY_OUTPUT = MODULE_ROOT / "data" / "nc_county_boundaries_2024.csv"

HPSA_SOURCE_FIELDS = (
    "HPSA Name",
    "HPSA ID",
    "Designation Type",
    "HPSA Discipline Class",
    "HPSA Score",
    "Primary State Abbreviation",
    "HPSA Status",
    "HPSA Designation Date",
    "HPSA Designation Last Update Date",
    "HPSA Degree of Shortage",
    "Withdrawn Date",
    "HPSA FTE",
    "HPSA Designation Population",
    "% of Population Below 100% Poverty",
    "HPSA Formal Ratio",
    "HPSA Population Type",
    "Rural Status",
    "Common County Name",
    "Common State Abbreviation",
    "State and County Federal Information Processing Standard Code",
    "HPSA Component Name",
    "HPSA Component Source Identification Number",
    "HPSA Component Type Description",
    "HPSA Estimated Served Population",
    "HPSA Estimated Underserved Population",
    "HPSA Provider Ratio Goal",
    "HPSA Shortage",
    "Data Warehouse Record Create Date",
)

TEACHING_FIELDS = (
    "county_fips",
    "county_name",
    "state_abbr",
    "health_measure_id",
    "health_measure_label",
    "health_measure_year",
    "adult_population",
    "age_adjusted_fair_poor_health_pct",
    "age_adjusted_low_ci_pct",
    "age_adjusted_high_ci_pct",
    "national_age_adjusted_pct",
    "difference_from_national_pct_points",
    "health_rank_descending",
    "health_point_above_national",
    "active_hpsa_component_rows",
    "active_hpsa_designations",
    "max_active_hpsa_score",
    "max_score_hpsa_ids",
    "max_score_hpsa_names",
    "active_designation_types",
    "active_rural_statuses",
    "whole_county_geographic_hpsa",
    "higher_hpsa_score_screen",
    "bivariate_screen_class",
    "reference_review_eligible",
    "reference_review_order",
    "reference_shortlist",
    "time_alignment_status",
    "interpretation_boundary",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path, encoding: str = "utf-8") -> tuple[tuple[str, ...], list[dict[str, str]]]:
    with path.open(encoding=encoding, newline="") as handle:
        reader = csv.DictReader(handle)
        return tuple(reader.fieldnames or ()), list(reader)


def read_hpsa_input(path: Path | None) -> tuple[tuple[str, ...], list[dict[str, str]], str, int]:
    if path:
        raw = path.read_bytes()
    elif DEFAULT_HPSA_OUTPUT.exists():
        raw = DEFAULT_HPSA_OUTPUT.read_bytes()
    else:
        request = urllib.request.Request(HPSA_URL, headers={"User-Agent": "OpenClinicalLearningCommons/0.21"})
        with urllib.request.urlopen(request, timeout=180) as response:
            raw = response.read()
    digest = hashlib.sha256(raw).hexdigest()
    text = raw.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text, newline=""))
    return tuple(reader.fieldnames or ()), list(reader), digest, len(raw)


def select_hpsa_rows(fields: tuple[str, ...], rows: list[dict[str, str]], digest: str) -> list[dict[str, str]]:
    if set(HPSA_SOURCE_FIELDS).issubset(fields) and len(fields) > len(HPSA_SOURCE_FIELDS):
        if digest != EXPECTED_HPSA_FULL_SHA256:
            raise ValueError(f"Unexpected full HPSA SHA-256: {digest}")
        selected = [
            {field: row.get(field, "") for field in HPSA_SOURCE_FIELDS}
            for row in rows
            if len(row.get("State and County Federal Information Processing Standard Code", "")) == 5
            and row["State and County Federal Information Processing Standard Code"].startswith("37")
        ]
    elif fields == HPSA_SOURCE_FIELDS:
        if EXPECTED_HPSA_SELECTED_SHA256 and digest != EXPECTED_HPSA_SELECTED_SHA256:
            raise ValueError(f"Unexpected selected HPSA SHA-256: {digest}")
        selected = rows
    else:
        missing = sorted(set(HPSA_SOURCE_FIELDS) - set(fields))
        raise ValueError(f"HPSA input is missing required fields: {', '.join(missing)}")
    selected.sort(
        key=lambda row: (
            row["State and County Federal Information Processing Standard Code"],
            row["HPSA ID"],
            row["HPSA Component Source Identification Number"],
            row["HPSA Status"],
            row["HPSA Designation Date"],
        )
    )
    if len(selected) != 1546:
        raise ValueError(f"Expected 1,546 mappable North Carolina HPSA rows, received {len(selected):,}")
    return selected


def write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def source_score(row: dict[str, str]) -> int:
    value = row["HPSA Score"].strip()
    if not value.isdigit():
        raise ValueError(f"Designated HPSA row has a nonnumeric score: {value!r}")
    return int(value)


def build_teaching_rows(places: list[dict[str, str]], hpsa: list[dict[str, str]]) -> list[dict[str, object]]:
    health = [row for row in places if row["measure_id"] == "GHLTH"]
    if len(health) != 100 or len({row["county_fips"] for row in health}) != 100:
        raise ValueError("Expected one GHLTH row for each of 100 North Carolina counties")

    active_by_county: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in hpsa:
        if row["HPSA Status"] == "Designated":
            active_by_county[row["State and County Federal Information Processing Standard Code"]].append(row)

    ranked = sorted(
        health,
        key=lambda row: (-Decimal(row["age_adjusted_prevalence_pct"]), row["county_fips"]),
    )
    health_rank = {row["county_fips"]: rank for rank, row in enumerate(ranked, start=1)}
    output: list[dict[str, object]] = []
    for row in sorted(health, key=lambda item: item["county_fips"]):
        fips = row["county_fips"]
        active = active_by_county.get(fips, [])
        scores = [source_score(item) for item in active]
        max_score = max(scores) if scores else None
        max_rows = [item for item in active if source_score(item) == max_score] if max_score is not None else []
        high_health = Decimal(row["difference_from_national_pct_points"]) > 0
        high_hpsa = max_score is not None and max_score >= 20
        if high_health and high_hpsa:
            screen_class = "Higher health estimate + higher HPSA score"
        elif high_health:
            screen_class = "Higher health estimate only"
        elif high_hpsa:
            screen_class = "Higher HPSA score only"
        else:
            screen_class = "Neither screen condition"
        whole_county = any(
            item["Designation Type"] in {"Geographic HPSA", "High Needs Geographic HPSA"}
            and item["HPSA Component Type Description"] == "Single County"
            for item in active
        )
        output.append(
            {
                "county_fips": fips,
                "county_name": row["county_name"],
                "state_abbr": row["state_abbr"],
                "health_measure_id": row["measure_id"],
                "health_measure_label": row["measure_label"],
                "health_measure_year": row["measure_year"],
                "adult_population": row["adult_population"],
                "age_adjusted_fair_poor_health_pct": row["age_adjusted_prevalence_pct"],
                "age_adjusted_low_ci_pct": row["age_adjusted_low_ci_pct"],
                "age_adjusted_high_ci_pct": row["age_adjusted_high_ci_pct"],
                "national_age_adjusted_pct": row["national_age_adjusted_pct"],
                "difference_from_national_pct_points": row["difference_from_national_pct_points"],
                "health_rank_descending": health_rank[fips],
                "health_point_above_national": "yes" if high_health else "no",
                "active_hpsa_component_rows": len(active),
                "active_hpsa_designations": len({item["HPSA ID"] for item in active}),
                "max_active_hpsa_score": "" if max_score is None else max_score,
                "max_score_hpsa_ids": " | ".join(sorted({item["HPSA ID"] for item in max_rows})),
                "max_score_hpsa_names": " | ".join(sorted({item["HPSA Name"] for item in max_rows})),
                "active_designation_types": " | ".join(sorted({item["Designation Type"] for item in active})),
                "active_rural_statuses": " | ".join(sorted({item["Rural Status"] or "Not stated" for item in active})),
                "whole_county_geographic_hpsa": "yes" if whole_county else "no",
                "higher_hpsa_score_screen": "yes" if high_hpsa else "no",
                "bivariate_screen_class": screen_class,
                "reference_review_eligible": "yes" if high_health and high_hpsa else "no",
                "reference_review_order": "",
                "reference_shortlist": "no",
                "time_alignment_status": "PLACES measure year 2022; HPSA source snapshot 2026-08-29",
                "interpretation_boundary": "HPSA score is the highest active component score touching the county, not a county workforce rate",
            }
        )

    eligible = sorted(
        (row for row in output if row["reference_review_eligible"] == "yes"),
        key=lambda row: (
            -Decimal(str(row["age_adjusted_fair_poor_health_pct"])),
            -int(row["max_active_hpsa_score"]),
            str(row["county_name"]),
            str(row["county_fips"]),
        ),
    )
    for rank, row in enumerate(eligible, start=1):
        row["reference_review_order"] = rank
        row["reference_shortlist"] = "yes" if rank <= 12 else "no"
    return output


def build(
    hpsa_input: Path | None,
    hpsa_output: Path,
    teaching_output: Path,
    boundary_output: Path,
) -> None:
    if sha256(PLACES_INPUT) != EXPECTED_PLACES_SHA256:
        raise ValueError("Module 09 PLACES input does not match its pinned release")
    if sha256(BOUNDARY_INPUT) != EXPECTED_BOUNDARY_SHA256:
        raise ValueError("Module 05 boundary input does not match its pinned release")

    places_fields, places = read_csv(PLACES_INPUT)
    if "measure_id" not in places_fields:
        raise ValueError("Module 09 PLACES input is missing measure_id")
    hpsa_fields, hpsa_rows, input_digest, input_bytes = read_hpsa_input(hpsa_input)
    selected = select_hpsa_rows(hpsa_fields, hpsa_rows, input_digest)
    teaching = build_teaching_rows(places, selected)

    write_csv(hpsa_output, HPSA_SOURCE_FIELDS, selected)
    write_csv(teaching_output, TEACHING_FIELDS, teaching)
    boundary_output.parent.mkdir(parents=True, exist_ok=True)
    if BOUNDARY_INPUT.resolve() != boundary_output.resolve():
        shutil.copyfile(BOUNDARY_INPUT, boundary_output)

    print(f"HPSA input bytes: {input_bytes:,}; SHA-256: {input_digest}")
    print(f"Selected HPSA rows: {len(selected):,}; SHA-256: {sha256(hpsa_output)}")
    print(f"Teaching rows: {len(teaching):,}; SHA-256: {sha256(teaching_output)}")
    print(f"Boundary rows: 7,121; SHA-256: {sha256(boundary_output)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hpsa-input", type=Path)
    parser.add_argument("--hpsa-output", type=Path, default=DEFAULT_HPSA_OUTPUT)
    parser.add_argument("--teaching-output", type=Path, default=DEFAULT_TEACHING_OUTPUT)
    parser.add_argument("--boundary-output", type=Path, default=DEFAULT_BOUNDARY_OUTPUT)
    args = parser.parse_args()
    build(
        args.hpsa_input.resolve() if args.hpsa_input else None,
        args.hpsa_output.resolve(),
        args.teaching_output.resolve(),
        args.boundary_output.resolve(),
    )


if __name__ == "__main__":
    main()
