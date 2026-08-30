#!/usr/bin/env python3
"""Validate the DA-730 Module 08 NHSN time-series releases."""

from __future__ import annotations

import csv
import hashlib
import statistics
from collections import Counter
from datetime import date
from pathlib import Path

from build_nhsn_time_series import ALL_FIELDS, EXPECTED_RAW_SHA256, MA_FIELDS, MAX_DATE, MIN_DATE


MODULE_ROOT = Path(__file__).resolve().parent
ALL_DATA = MODULE_ROOT / "data" / "nhsn_hospital_capacity_jurisdiction_2024_2026.csv"
MA_DATA = MODULE_ROOT / "data" / "ma_hospital_capacity_time_2024_2026.csv"
ALL_SHA256 = "8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1"
MA_SHA256 = "394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616"
CORE_NUMERIC = (
    "inpatient_beds",
    "inpatient_beds_occupied",
    "inpatient_occupancy_pct",
    "icu_beds",
    "icu_beds_occupied",
    "icu_occupancy_pct",
    "covid_new_admissions",
    "flu_new_admissions",
    "rsv_new_admissions",
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
    check(ALL_DATA.is_file(), "all-jurisdiction release exists")
    check(MA_DATA.is_file(), "Massachusetts teaching release exists")
    check(sha256(ALL_DATA) == ALL_SHA256, "all-jurisdiction checksum matches")
    check(sha256(MA_DATA) == MA_SHA256, "Massachusetts checksum matches")

    all_fields, all_rows = read_rows(ALL_DATA)
    ma_fields, ma_rows = read_rows(MA_DATA)
    check(all_fields == ALL_FIELDS, "all-jurisdiction columns match")
    check(ma_fields == MA_FIELDS, "Massachusetts columns match")
    check(len(all_rows) == 6208, "all-jurisdiction release has 6,208 rows")
    check(len(ma_rows) == 94, "Massachusetts release has 94 rows")
    check(len({row["jurisdiction"] for row in all_rows}) == 67, "release has 67 jurisdictions")
    check(len({(row["week_end"], row["jurisdiction"]) for row in all_rows}) == 6208, "jurisdiction-week keys are unique")
    check(min(row["week_end"] for row in all_rows) == MIN_DATE, "minimum week is pinned")
    check(max(row["week_end"] for row in all_rows) == MAX_DATE, "maximum week is pinned")
    check(all(row["week_end"] <= MAX_DATE for row in all_rows), "future source rows are excluded")

    missing_core = [row for row in all_rows if not row["inpatient_occupancy_pct"]]
    complete_core = [row for row in all_rows if row["inpatient_occupancy_pct"]]
    check(len(missing_core) == 120, "120 jurisdiction-weeks preserve unavailable core metrics")
    check(len(complete_core) == 6088, "6,088 jurisdiction-weeks have complete occupancy metrics")
    check(all(all(not row[field] for field in CORE_NUMERIC) for row in missing_core), "unavailable core fields remain jointly blank")
    check(all(all(row[field] for field in CORE_NUMERIC) for row in complete_core), "available core fields remain jointly complete")
    check(
        all(
            abs(float(row["inpatient_occupancy_pct"]) - 100 * int(row["inpatient_beds_occupied"]) / int(row["inpatient_beds"])) <= 0.0051
            for row in complete_core
        ),
        "published inpatient occupancy reconciles with counts",
    )
    inpatient_over_capacity = [row for row in complete_core if int(row["inpatient_beds_occupied"]) > int(row["inpatient_beds"])]
    icu_over_capacity = [row for row in complete_core if int(row["icu_beds_occupied"]) > int(row["icu_beds"])]
    check(len(inpatient_over_capacity) == 3 and {row["jurisdiction"] for row in inpatient_over_capacity} == {"GU"}, "three published Guam inpatient rows exceed reported beds")
    check(len(icu_over_capacity) == 3 and {row["jurisdiction"] for row in icu_over_capacity} == {"GU", "MP"}, "three published Guam or Northern Mariana Islands ICU rows exceed reported beds")
    coverage_over_100 = [row for row in all_rows if float(row["hospitals_reporting_occupancy_pct"]) > 100]
    check(
        len(coverage_over_100) == 1
        and coverage_over_100[0]["jurisdiction"] == "WI"
        and coverage_over_100[0]["week_end"] == "2026-07-25"
        and coverage_over_100[0]["hospitals_reporting_occupancy_pct"] == "100.68",
        "one published Wisconsin coverage value exceeds 100 percent",
    )
    check(all(float(row["hospitals_reporting_occupancy_pct"]) >= 0 for row in all_rows), "reporting coverage is nonnegative")

    check(all(row["jurisdiction"] == "MA" for row in ma_rows), "teaching rows are Massachusetts")
    check([int(row["week_index"]) for row in ma_rows] == list(range(1, 95)), "week index is complete")
    check(ma_rows[0]["days_since_prior"] == "", "first week has no prior interval")
    check(all(row["days_since_prior"] == "7" for row in ma_rows[1:]), "Massachusetts sequence is weekly without gaps")
    check(all(all(row[field] for field in CORE_NUMERIC) for row in ma_rows), "Massachusetts core metrics are complete")
    check(all(int(row["inpatient_beds_occupied"]) <= int(row["inpatient_beds"]) for row in ma_rows), "Massachusetts inpatient counts do not exceed beds")
    check(all(int(row["icu_beds_occupied"]) <= int(row["icu_beds"]) for row in ma_rows), "Massachusetts ICU counts do not exceed beds")
    check(all(row["calendar_year"] == row["week_end"][:4] for row in ma_rows), "calendar year is reproducible")
    check(all(int(row["iso_week"]) == date.fromisoformat(row["week_end"]).isocalendar().week for row in ma_rows), "ISO week is reproducible")
    check(Counter(row["source_season_status"] for row in ma_rows) == {"source field unavailable": 61, "source reported": 33}, "source season-field availability is explicit")
    check(all((row["respiratory_season"] != "") == (row["source_season_status"] == "source reported") for row in ma_rows), "season status matches source values")
    check(
        all(
            int(row["total_respiratory_new_admissions"])
            == int(row["covid_new_admissions"]) + int(row["flu_new_admissions"]) + int(row["rsv_new_admissions"])
            for row in ma_rows
        ),
        "combined respiratory admissions equal the three source counts",
    )
    check(all(abs(float(row["reporting_gap_pct"]) + float(row["hospitals_reporting_occupancy_pct"]) - 100) < 0.001 for row in ma_rows), "reporting gap is reproducible")

    all_by_key = {(row["week_end"], row["jurisdiction"]): row for row in all_rows}
    check(
        all(all_by_key[(row["week_end"], "MA")][field] == row[field] for row in ma_rows for field in ALL_FIELDS),
        "Massachusetts source fields match the all-jurisdiction release",
    )

    occupancy = [float(row["inpatient_occupancy_pct"]) for row in ma_rows]
    admissions = [int(row["total_respiratory_new_admissions"]) for row in ma_rows]
    coverage = [float(row["hospitals_reporting_occupancy_pct"]) for row in ma_rows]
    deltas = [occupancy[index] - occupancy[index - 1] for index in range(1, len(occupancy))]
    check(min(occupancy) == 77.96 and ma_rows[occupancy.index(min(occupancy))]["week_end"] == "2024-12-28", "occupancy minimum matches")
    check(max(occupancy) == 87.30 and ma_rows[occupancy.index(max(occupancy))]["week_end"] == "2025-03-01", "occupancy maximum matches")
    check(round(statistics.mean(occupancy), 2) == 83.87, "occupancy mean matches")
    check(round(statistics.median(occupancy), 2) == 84.12, "occupancy median matches")
    check(max(admissions) == 1996 and ma_rows[admissions.index(max(admissions))]["week_end"] == "2025-02-08", "respiratory-admission maximum matches")
    check(min(admissions) == 13, "respiratory-admission minimum matches")
    check(min(coverage) == 67.05 and ma_rows[coverage.index(min(coverage))]["week_end"] == "2025-02-15", "reporting-coverage minimum matches")
    check(max(coverage) == 96.67, "reporting-coverage maximum matches")
    check(round(max(deltas), 2) == 6.35 and ma_rows[deltas.index(max(deltas)) + 1]["week_end"] == "2025-01-04", "largest occupancy rise matches")
    check(round(min(deltas), 2) == -7.79 and ma_rows[deltas.index(min(deltas)) + 1]["week_end"] == "2024-12-28", "largest occupancy fall matches")

    print(f"Module 08 NHSN time data passed {len(checks)} checks.")
    print(f"All-jurisdiction rows: {len(all_rows):,}; SHA-256: {sha256(ALL_DATA)}")
    print(f"Massachusetts rows: {len(ma_rows):,}; SHA-256: {sha256(MA_DATA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
