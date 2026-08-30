#!/usr/bin/env python3
"""Validate the DA-730 Module 10 place and access releases."""

from __future__ import annotations

import csv
import hashlib
import sys
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

sys.dont_write_bytecode = True

from build_place_access_case import HPSA_SOURCE_FIELDS, TEACHING_FIELDS


MODULE_ROOT = Path(__file__).resolve().parent
HPSA_DATA = MODULE_ROOT / "data" / "hpsa_primary_care_nc_2026_08_29.csv"
TEACHING_DATA = MODULE_ROOT / "data" / "nc_place_access_2026.csv"
BOUNDARY_DATA = MODULE_ROOT / "data" / "nc_county_boundaries_2024.csv"
HPSA_SHA256 = "061fe5e18bc9cd58bd89256c686ddefbce6d77972c1139b1b339497f2eab5445"
TEACHING_SHA256 = "90a575f03bc94cc0eb336d263e3f9d8afe09cf68ddb95476bf1836c0574f9a07"
BOUNDARY_SHA256 = "6eb085f49b400d4ecf6f88646f51dd01fdd4154533262e66ade02b1d1d8f666f"
EXPECTED_SHORTLIST = (
    "Robeson",
    "Scotland",
    "Hertford",
    "Halifax",
    "Warren",
    "Greene",
    "Washington",
    "Wilson",
    "Anson",
    "Lenoir",
    "Edgecombe",
    "Swain",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path: Path) -> tuple[tuple[str, ...], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return tuple(reader.fieldnames or ()), list(reader)


def main() -> None:
    checks: list[tuple[str, bool, object]] = []

    def record(label: str, condition: bool, detail: object) -> None:
        checks.append((label, bool(condition), detail))

    hpsa_fields, hpsa = read_rows(HPSA_DATA)
    teaching_fields, teaching = read_rows(TEACHING_DATA)
    boundary_fields, boundaries = read_rows(BOUNDARY_DATA)

    record("HPSA checksum", sha256(HPSA_DATA) == HPSA_SHA256, sha256(HPSA_DATA))
    record("teaching checksum", sha256(TEACHING_DATA) == TEACHING_SHA256, sha256(TEACHING_DATA))
    record("boundary checksum", sha256(BOUNDARY_DATA) == BOUNDARY_SHA256, sha256(BOUNDARY_DATA))
    record("HPSA fields", hpsa_fields == HPSA_SOURCE_FIELDS, len(hpsa_fields))
    record("teaching fields", teaching_fields == TEACHING_FIELDS, len(teaching_fields))
    record(
        "boundary fields",
        boundary_fields == ("county_fips", "county_name", "polygon_group", "point_order", "longitude", "latitude"),
        boundary_fields,
    )

    record("HPSA rows", len(hpsa) == 1546, len(hpsa))
    record("HPSA county coverage", len({row["State and County Federal Information Processing Standard Code"] for row in hpsa}) == 100, "100")
    record("HPSA county FIPS", all(len(row["State and County Federal Information Processing Standard Code"]) == 5 and row["State and County Federal Information Processing Standard Code"].startswith("37") for row in hpsa), "NC five-character FIPS")
    record("HPSA discipline", {row["HPSA Discipline Class"] for row in hpsa} == {"Primary Care"}, "Primary Care")
    record("HPSA source date", {row["Data Warehouse Record Create Date"] for row in hpsa} == {"08/29/2026"}, "08/29/2026")
    statuses = Counter(row["HPSA Status"] for row in hpsa)
    record("designated HPSA rows", statuses["Designated"] == 740, statuses["Designated"])
    record("withdrawn HPSA rows", statuses["Withdrawn"] == 702, statuses["Withdrawn"])
    record("proposed withdrawal HPSA rows", statuses["Proposed For Withdrawal"] == 104, statuses["Proposed For Withdrawal"])
    record("HPSA status total", sum(statuses.values()) == len(hpsa), statuses)
    active = [row for row in hpsa if row["HPSA Status"] == "Designated"]
    record("active HPSA identifiers", len({row["HPSA ID"] for row in active}) == 210, len({row["HPSA ID"] for row in active}))
    record("active county coverage", len({row["State and County Federal Information Processing Standard Code"] for row in active}) == 98, "98")
    record("active scores numeric", all(row["HPSA Score"].isdigit() for row in active), "numeric")
    record("active score range", (min(int(row["HPSA Score"]) for row in active), max(int(row["HPSA Score"]) for row in active)) == (3, 24), "3 to 24")
    record("designation types retained", len({row["Designation Type"] for row in hpsa}) == 9, len({row["Designation Type"] for row in hpsa}))

    record("teaching rows", len(teaching) == 100, len(teaching))
    record("teaching county identities", len({row["county_fips"] for row in teaching}) == 100, "100")
    record("teaching FIPS", all(len(row["county_fips"]) == 5 and row["county_fips"].startswith("37") for row in teaching), "NC five-character FIPS")
    record("health measure", {row["health_measure_id"] for row in teaching} == {"GHLTH"}, "GHLTH")
    record("health year", {row["health_measure_year"] for row in teaching} == {"2022"}, "2022")
    record("national reference", {row["national_age_adjusted_pct"] for row in teaching} == {"17.0"}, "17.0")
    health_values = [Decimal(row["age_adjusted_fair_poor_health_pct"]) for row in teaching]
    record("health range", (min(health_values), max(health_values)) == (Decimal("12.1"), Decimal("27.2")), f"{min(health_values)} to {max(health_values)}")
    record("interval ordering", all(Decimal(row["age_adjusted_low_ci_pct"]) <= Decimal(row["age_adjusted_fair_poor_health_pct"]) <= Decimal(row["age_adjusted_high_ci_pct"]) for row in teaching), "low <= point <= high")
    record("difference formula", all(Decimal(row["difference_from_national_pct_points"]) == Decimal(row["age_adjusted_fair_poor_health_pct"]) - Decimal(row["national_age_adjusted_pct"]) for row in teaching), "point minus national")
    record("health above national", sum(row["health_point_above_national"] == "yes" for row in teaching) == 73, sum(row["health_point_above_national"] == "yes" for row in teaching))
    record("health rank set", {int(row["health_rank_descending"]) for row in teaching} == set(range(1, 101)), "1 through 100")
    record("health rank monotonic", [row["county_fips"] for row in sorted(teaching, key=lambda row: int(row["health_rank_descending"]))] == [row["county_fips"] for row in sorted(teaching, key=lambda row: (-Decimal(row["age_adjusted_fair_poor_health_pct"]), row["county_fips"]))], "descending point estimate")
    populations = [int(row["adult_population"]) for row in teaching]
    record("adult population range", (min(populations), max(populations)) == (2644, 908531), f"{min(populations):,} to {max(populations):,}")

    active_by_county: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in active:
        active_by_county[row["State and County Federal Information Processing Standard Code"]].append(row)
    record("component row reconciliation", all(int(row["active_hpsa_component_rows"]) == len(active_by_county[row["county_fips"]]) for row in teaching), "matches source")
    record("designation count reconciliation", all(int(row["active_hpsa_designations"]) == len({item["HPSA ID"] for item in active_by_county[row["county_fips"]]}) for row in teaching), "matches source")
    record("component row total", sum(int(row["active_hpsa_component_rows"]) for row in teaching) == 740, sum(int(row["active_hpsa_component_rows"]) for row in teaching))
    record("counties without active HPSA", sum(row["active_hpsa_designations"] == "0" for row in teaching) == 2, sum(row["active_hpsa_designations"] == "0" for row in teaching))
    record("county maximum score range", (min(int(row["max_active_hpsa_score"]) for row in teaching if row["max_active_hpsa_score"]), max(int(row["max_active_hpsa_score"]) for row in teaching if row["max_active_hpsa_score"])) == (11, 24), "11 to 24")
    record("missing maximum scores", sum(not row["max_active_hpsa_score"] for row in teaching) == 2, sum(not row["max_active_hpsa_score"] for row in teaching))
    record("higher HPSA screen", sum(row["higher_hpsa_score_screen"] == "yes" for row in teaching) == 23, sum(row["higher_hpsa_score_screen"] == "yes" for row in teaching))
    record("whole-county geographic designations", sum(row["whole_county_geographic_hpsa"] == "yes" for row in teaching) == 7, sum(row["whole_county_geographic_hpsa"] == "yes" for row in teaching))
    classes = Counter(row["bivariate_screen_class"] for row in teaching)
    record("combined class", classes["Higher health estimate + higher HPSA score"] == 19, classes)
    record("health-only class", classes["Higher health estimate only"] == 54, classes)
    record("HPSA-only class", classes["Higher HPSA score only"] == 4, classes)
    record("neither class", classes["Neither screen condition"] == 23, classes)
    record("bivariate class total", sum(classes.values()) == 100, classes)
    record("review eligible", sum(row["reference_review_eligible"] == "yes" for row in teaching) == 19, sum(row["reference_review_eligible"] == "yes" for row in teaching))
    record("shortlist count", sum(row["reference_shortlist"] == "yes" for row in teaching) == 12, sum(row["reference_shortlist"] == "yes" for row in teaching))
    shortlist = sorted((row for row in teaching if row["reference_shortlist"] == "yes"), key=lambda row: int(row["reference_review_order"]))
    record("shortlist order", tuple(row["county_name"] for row in shortlist) == EXPECTED_SHORTLIST, tuple(row["county_name"] for row in shortlist))
    record("review order range", {int(row["reference_review_order"]) for row in teaching if row["reference_review_order"]} == set(range(1, 20)), "1 through 19")
    record("shortlist is first twelve", all(int(row["reference_review_order"]) <= 12 for row in shortlist), "first twelve")
    record("time boundary", {row["time_alignment_status"] for row in teaching} == {"PLACES measure year 2022; HPSA source snapshot 2026-08-29"}, "declared")
    record("score boundary", {row["interpretation_boundary"] for row in teaching} == {"HPSA score is the highest active component score touching the county, not a county workforce rate"}, "declared")

    record("boundary rows", len(boundaries) == 7121, len(boundaries))
    boundary_fips = {row["county_fips"] for row in boundaries}
    record("boundary county coverage", boundary_fips == {row["county_fips"] for row in teaching}, len(boundary_fips))
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in boundaries:
        groups[row["polygon_group"]].append(row)
    record("boundary polygon parts", len(groups) == 104, len(groups))
    record("boundary point order", all([int(row["point_order"]) for row in rows] == list(range(1, len(rows) + 1)) for rows in groups.values()), "sequential")
    record("closed boundary parts", all((rows[0]["longitude"], rows[0]["latitude"]) == (rows[-1]["longitude"], rows[-1]["latitude"]) for rows in groups.values()), "closed")
    record("longitude range", all(-85 < Decimal(row["longitude"]) < -75 for row in boundaries), "North Carolina")
    record("latitude range", all(33 < Decimal(row["latitude"]) < 37 for row in boundaries), "North Carolina")

    failures = [(label, detail) for label, passed, detail in checks if not passed]
    if failures:
        for label, detail in failures:
            print(f"FAIL: {label}: {detail}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Module 10 place and access data passed {len(checks)} checks.")
    print(f"HPSA selected rows: {len(hpsa):,}; SHA-256: {sha256(HPSA_DATA)}")
    print(f"Teaching counties: {len(teaching):,}; SHA-256: {sha256(TEACHING_DATA)}")
    print(f"Boundary points: {len(boundaries):,}; SHA-256: {sha256(BOUNDARY_DATA)}")


if __name__ == "__main__":
    main()
