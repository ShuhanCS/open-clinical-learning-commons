#!/usr/bin/env python3
"""Validate the DA-730 Module 09 CDC PLACES comparison releases."""

from __future__ import annotations

import csv
import hashlib
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

from build_places_comparison import EXPECTED_RAW_SHA256, MEASURES, SOURCE_FIELDS, TEACHING_FIELDS


MODULE_ROOT = Path(__file__).resolve().parent
ALL_DATA = MODULE_ROOT / "data" / "places_county_comparison_2024.csv"
NC_DATA = MODULE_ROOT / "data" / "nc_county_health_profiles_2024.csv"
ALL_SHA256 = "2af5ce99fc7d66a18e95451084afc397e0f7392e9f1a2b5476377fd8811658d2"
NC_SHA256 = "33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9"
EXPECTED_NATIONAL = {
    "CSMOKING": Decimal("13.2"),
    "DIABETES": Decimal("10.4"),
    "GHLTH": Decimal("17.0"),
    "LPA": Decimal("23.0"),
    "OBESITY": Decimal("33.4"),
}
EXPECTED_RANGES = {
    "CSMOKING": (Decimal("9.7"), Decimal("25.0")),
    "DIABETES": (Decimal("8.0"), Decimal("15.6")),
    "GHLTH": (Decimal("12.1"), Decimal("27.2")),
    "LPA": (Decimal("15.8"), Decimal("33.1")),
    "OBESITY": (Decimal("25.6"), Decimal("43.5")),
}
EXPECTED_ABOVE = {
    "CSMOKING": 89,
    "DIABETES": 62,
    "GHLTH": 73,
    "LPA": 68,
    "OBESITY": 70,
}
EXPECTED_PROFILE_COUNTS = {0: 9, 1: 9, 2: 10, 3: 9, 4: 9, 5: 54}
EXPECTED_SHORTLIST = (
    "Robeson",
    "Bertie",
    "Hertford",
    "Anson",
    "Hyde",
    "Nash",
    "Warren",
    "Columbus",
    "Scotland",
    "Halifax",
    "Swain",
    "Sampson",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path: Path) -> tuple[tuple[str, ...], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return tuple(reader.fieldnames or ()), list(reader)


def main() -> int:
    checks: list[str] = []

    def check(condition: bool, label: str) -> None:
        if not condition:
            raise AssertionError(label)
        checks.append(label)

    check(len(EXPECTED_RAW_SHA256) == 64, "raw query checksum is pinned")
    check(ALL_DATA.is_file(), "selected national release exists")
    check(NC_DATA.is_file(), "North Carolina teaching release exists")
    check(sha256(ALL_DATA) == ALL_SHA256, "selected national checksum matches")
    check(sha256(NC_DATA) == NC_SHA256, "North Carolina checksum matches")

    all_fields, all_rows = read_rows(ALL_DATA)
    nc_fields, nc_rows = read_rows(NC_DATA)
    check(all_fields == SOURCE_FIELDS, "selected national columns match")
    check(nc_fields == TEACHING_FIELDS, "North Carolina columns match")
    check(len(all_rows) == 31450, "selected national release has 31,450 rows")
    check(len(nc_rows) == 500, "North Carolina release has 500 rows")
    check({row["measureid"] for row in all_rows} == set(MEASURES), "selected measures match")
    check(Counter(row["measureid"] for row in all_rows) == {measure: 6290 for measure in MEASURES}, "each measure has 6,290 rows")
    check(Counter(row["datavaluetypeid"] for row in all_rows) == {"AgeAdjPrv": 15725, "CrdPrv": 15725}, "value-type counts match")
    check({row["year"] for row in all_rows} == {"2022"}, "all selected estimates use measure year 2022")
    check(len({(row["measureid"], row["locationid"], row["datavaluetypeid"]) for row in all_rows}) == 31450, "source keys are unique")
    check(all(row["data_value"] and row["low_confidence_limit"] and row["high_confidence_limit"] for row in all_rows), "selected estimates and intervals are complete")
    check(all(Decimal(row["low_confidence_limit"]) <= Decimal(row["data_value"]) <= Decimal(row["high_confidence_limit"]) for row in all_rows), "source intervals contain point estimates")
    check(sum(row["locationid"] == "59" for row in all_rows) == 10, "ten national summary rows are preserved")
    check(len({row["locationid"] for row in all_rows if row["locationid"] != "59"}) == 3144, "3,144 county geographies are preserved")
    check(sum(row["stateabbr"] == "NC" for row in all_rows) == 1000, "one thousand North Carolina source rows are preserved")

    check({row["measure_id"] for row in nc_rows} == set(MEASURES), "teaching measures match")
    check(Counter(row["measure_id"] for row in nc_rows) == {measure: 100 for measure in MEASURES}, "each teaching measure has 100 counties")
    check(len({row["county_fips"] for row in nc_rows}) == 100, "teaching release has 100 counties")
    check(len({(row["county_fips"], row["measure_id"]) for row in nc_rows}) == 500, "county-measure keys are unique")
    check(all(row["state_abbr"] == "NC" and row["state_name"] == "North Carolina" for row in nc_rows), "teaching geography is North Carolina")
    check(all(row["measure_year"] == "2022" for row in nc_rows), "teaching year is 2022")
    check(all(row["counties_compared"] == "100" for row in nc_rows), "comparison denominator is explicit")
    check(all(row["source_footnote"] == "" for row in nc_rows), "selected North Carolina estimates have no source footnote")
    check(all(Decimal(row["crude_low_ci_pct"]) <= Decimal(row["crude_prevalence_pct"]) <= Decimal(row["crude_high_ci_pct"]) for row in nc_rows), "crude intervals contain point estimates")
    check(all(Decimal(row["age_adjusted_low_ci_pct"]) <= Decimal(row["age_adjusted_prevalence_pct"]) <= Decimal(row["age_adjusted_high_ci_pct"]) for row in nc_rows), "adjusted intervals contain point estimates")
    check(all(Decimal(row["difference_from_national_pct_points"]) == Decimal(row["age_adjusted_prevalence_pct"]) - Decimal(row["national_age_adjusted_pct"]) for row in nc_rows), "national differences are reproducible")
    check(all((row["point_estimate_above_national"] == "yes") == (Decimal(row["difference_from_national_pct_points"]) > 0) for row in nc_rows), "point-estimate direction is reproducible")

    all_by_key = {(row["locationid"], row["measureid"], row["datavaluetypeid"]): row for row in all_rows}
    check(
        all(
            row["crude_prevalence_pct"] == all_by_key[(row["county_fips"], row["measure_id"], "CrdPrv")]["data_value"]
            and row["age_adjusted_prevalence_pct"] == all_by_key[(row["county_fips"], row["measure_id"], "AgeAdjPrv")]["data_value"]
            for row in nc_rows
        ),
        "teaching point estimates match source rows",
    )
    check(
        all(
            row["national_age_adjusted_pct"] == all_by_key[("59", row["measure_id"], "AgeAdjPrv")]["data_value"]
            for row in nc_rows
        ),
        "teaching national references match source rows",
    )

    populations: dict[str, set[str]] = defaultdict(set)
    for row in nc_rows:
        populations[row["county_fips"]].add(row["adult_population"])
    check(all(len(values) == 1 for values in populations.values()), "adult population is stable across measures within county")
    population_values = [int(next(iter(values))) for values in populations.values()]
    check(min(population_values) == 2644 and max(population_values) == 908531, "adult population range matches")

    by_measure: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_county: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in nc_rows:
        by_measure[row["measure_id"]].append(row)
        by_county[row["county_fips"]].append(row)

    check(all({int(row["rank_descending_point_estimate"]) for row in rows} <= set(range(1, 101)) for rows in by_measure.values()), "within-measure ranks are valid")
    check(
        all(
            int(row["rank_descending_point_estimate"])
            == 1 + sum(Decimal(other["age_adjusted_prevalence_pct"]) > Decimal(row["age_adjusted_prevalence_pct"]) for other in by_measure[row["measure_id"]])
            for row in nc_rows
        ),
        "competition ranks are reproducible",
    )
    check(
        all(int(row["measures_above_national"]) == sum(item["point_estimate_above_national"] == "yes" for item in by_county[row["county_fips"]]) for row in nc_rows),
        "county profile counts are reproducible",
    )
    check(
        all(
            Decimal(row["largest_gap_pct_points"])
            == max(Decimal(item["difference_from_national_pct_points"]) for item in by_county[row["county_fips"]])
            for row in nc_rows
        ),
        "largest county gaps are reproducible",
    )
    check(Counter(int(rows[0]["measures_above_national"]) for rows in by_county.values()) == EXPECTED_PROFILE_COUNTS, "profile-count distribution matches")
    check(sorted({int(row["profile_order"]) for row in nc_rows}) == list(range(1, 101)), "profile order covers 1 through 100")
    check(all(len({row["profile_order"] for row in rows}) == 1 for rows in by_county.values()), "profile order is stable across panels")

    for measure in MEASURES:
        values = [Decimal(row["age_adjusted_prevalence_pct"]) for row in by_measure[measure]]
        check({Decimal(row["national_age_adjusted_pct"]) for row in by_measure[measure]} == {EXPECTED_NATIONAL[measure]}, f"{measure} national reference matches")
        check((min(values), max(values)) == EXPECTED_RANGES[measure], f"{measure} range matches")
        check(sum(row["point_estimate_above_national"] == "yes" for row in by_measure[measure]) == EXPECTED_ABOVE[measure], f"{measure} above-national count matches")

    shortlist = tuple(
        rows[0]["county_name"]
        for _, rows in sorted(by_county.items(), key=lambda item: int(item[1][0]["profile_order"]))[:12]
    )
    check(shortlist == EXPECTED_SHORTLIST, "twelve-county profile shortlist matches")

    print(f"Module 09 CDC PLACES comparison data passed {len(checks)} checks.")
    print(f"Selected rows: {len(all_rows):,}; SHA-256: {sha256(ALL_DATA)}")
    print(f"North Carolina rows: {len(nc_rows):,}; SHA-256: {sha256(NC_DATA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
