#!/usr/bin/env python3
"""Build the DA-730 Module 08 NHSN weekly time-series releases."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import urllib.parse
import urllib.request
from datetime import date
from decimal import Decimal
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
DATASET_ID = "rhwp-grxi"
LANDING_PAGE = "https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi"
API_BASE = f"https://data.cdc.gov/resource/{DATASET_ID}.csv"
MIN_DATE = "2024-11-09"
MAX_DATE = "2026-08-22"
EXPECTED_RAW_SHA256 = "d261cbc441069a41ef1b14347af90dfd6c59e402d7854a5e86288a4f0e9d4dc6"
DEFAULT_ALL_OUTPUT = MODULE_ROOT / "data" / "nhsn_hospital_capacity_jurisdiction_2024_2026.csv"
DEFAULT_MA_OUTPUT = MODULE_ROOT / "data" / "ma_hospital_capacity_time_2024_2026.csv"

SOURCE_FIELDS = (
    "weekendingdate",
    "jurisdiction",
    "respseason",
    "numinptbeds",
    "numinptbedsocc",
    "pctinptbedsocc",
    "numicubeds",
    "numicubedsocc",
    "pcticubedsocc",
    "totalconfc19newadm",
    "totalconfflunewadm",
    "totalconfrsvnewadm",
    "pctinptbedsocchosprep",
    "pctinptbedsoccperchosprep",
)

ALL_FIELDS = (
    "week_end",
    "jurisdiction",
    "respiratory_season",
    "inpatient_beds",
    "inpatient_beds_occupied",
    "inpatient_occupancy_pct",
    "icu_beds",
    "icu_beds_occupied",
    "icu_occupancy_pct",
    "covid_new_admissions",
    "flu_new_admissions",
    "rsv_new_admissions",
    "hospitals_reporting_occupancy",
    "hospitals_reporting_occupancy_pct",
)

MA_FIELDS = ALL_FIELDS + (
    "week_index",
    "calendar_year",
    "iso_week",
    "source_season_status",
    "days_since_prior",
    "total_respiratory_new_admissions",
    "reporting_gap_pct",
)


def query_url() -> str:
    params = {
        "$select": ",".join(SOURCE_FIELDS),
        "$where": f"weekendingdate between '{MIN_DATE}T00:00:00.000' and '{MAX_DATE}T00:00:00.000'",
        "$order": "weekendingdate,jurisdiction",
        "$limit": "10000",
    }
    return f"{API_BASE}?{urllib.parse.urlencode(params)}"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "OpenClinicalLearningCommons/0.19"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def date_only(value: str) -> str:
    return value[:10]


def integer_text(value: str) -> str:
    if not value:
        return ""
    return str(int(Decimal(value)))


def decimal_text(value: str) -> str:
    if not value:
        return ""
    return f"{Decimal(value).quantize(Decimal('0.01')):.2f}"


def normalize(row: dict[str, str]) -> dict[str, str]:
    return {
        "week_end": date_only(row["weekendingdate"]),
        "jurisdiction": row["jurisdiction"],
        "respiratory_season": row.get("respseason", ""),
        "inpatient_beds": integer_text(row.get("numinptbeds", "")),
        "inpatient_beds_occupied": integer_text(row.get("numinptbedsocc", "")),
        "inpatient_occupancy_pct": decimal_text(row.get("pctinptbedsocc", "")),
        "icu_beds": integer_text(row.get("numicubeds", "")),
        "icu_beds_occupied": integer_text(row.get("numicubedsocc", "")),
        "icu_occupancy_pct": decimal_text(row.get("pcticubedsocc", "")),
        "covid_new_admissions": integer_text(row.get("totalconfc19newadm", "")),
        "flu_new_admissions": integer_text(row.get("totalconfflunewadm", "")),
        "rsv_new_admissions": integer_text(row.get("totalconfrsvnewadm", "")),
        "hospitals_reporting_occupancy": integer_text(row.get("pctinptbedsocchosprep", "")),
        "hospitals_reporting_occupancy_pct": decimal_text(row.get("pctinptbedsoccperchosprep", "")),
    }


def write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def make_ma(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    ma = [row.copy() for row in rows if row["jurisdiction"] == "MA"]
    ma.sort(key=lambda row: row["week_end"])
    previous: date | None = None
    for index, row in enumerate(ma, start=1):
        current = date.fromisoformat(row["week_end"])
        row["week_index"] = str(index)
        row["calendar_year"] = str(current.year)
        row["iso_week"] = str(current.isocalendar().week)
        row["source_season_status"] = "source reported" if row["respiratory_season"] else "source field unavailable"
        row["days_since_prior"] = "" if previous is None else str((current - previous).days)
        admissions = [row["covid_new_admissions"], row["flu_new_admissions"], row["rsv_new_admissions"]]
        row["total_respiratory_new_admissions"] = "" if any(value == "" for value in admissions) else str(sum(map(int, admissions)))
        reporting = row["hospitals_reporting_occupancy_pct"]
        row["reporting_gap_pct"] = "" if not reporting else f"{Decimal('100') - Decimal(reporting):.2f}"
        previous = current
    return ma


def build(raw_input: Path | None, all_output: Path, ma_output: Path) -> None:
    url = query_url()
    raw = raw_input.read_bytes() if raw_input else download(url)
    raw_sha = sha256_bytes(raw)
    if EXPECTED_RAW_SHA256 and raw_sha != EXPECTED_RAW_SHA256:
        raise SystemExit(f"Pinned NHSN query checksum changed: {raw_sha}")

    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    if tuple(reader.fieldnames or ()) != SOURCE_FIELDS:
        raise SystemExit("NHSN query columns changed.")
    rows = [normalize(row) for row in reader]
    if len(rows) != 6208:
        raise SystemExit(f"Expected 6,208 selected NHSN rows; received {len(rows):,}.")
    if len({row["jurisdiction"] for row in rows}) != 67:
        raise SystemExit("Expected 67 source jurisdictions.")
    if min(row["week_end"] for row in rows) != MIN_DATE or max(row["week_end"] for row in rows) != MAX_DATE:
        raise SystemExit("NHSN query does not match the pinned date range.")

    ma = make_ma(rows)
    if len(ma) != 94:
        raise SystemExit(f"Expected 94 Massachusetts weeks; received {len(ma)}.")
    if any(row["days_since_prior"] not in ("", "7") for row in ma):
        raise SystemExit("Massachusetts does not have a complete weekly sequence.")

    write_csv(all_output, ALL_FIELDS, rows)
    write_csv(ma_output, MA_FIELDS, ma)

    print(f"Pinned query: {url}")
    print(f"Raw bytes: {len(raw):,}")
    print(f"Raw SHA-256: {raw_sha}")
    print(f"All-jurisdiction rows: {len(rows):,}; SHA-256: {sha256_file(all_output)}")
    print(f"Massachusetts rows: {len(ma):,}; SHA-256: {sha256_file(ma_output)}")
    if not EXPECTED_RAW_SHA256:
        print("Bootstrap build only: record the raw checksum before release.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-input", type=Path)
    parser.add_argument("--all-output", type=Path, default=DEFAULT_ALL_OUTPUT)
    parser.add_argument("--ma-output", type=Path, default=DEFAULT_MA_OUTPUT)
    args = parser.parse_args()
    build(
        args.raw_input.resolve() if args.raw_input else None,
        args.all_output.resolve(),
        args.ma_output.resolve(),
    )


if __name__ == "__main__":
    main()
