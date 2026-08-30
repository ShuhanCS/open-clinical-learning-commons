#!/usr/bin/env python3
"""Build the public CMS releases for DA-730 Module 06."""

from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import tempfile
import urllib.request
from datetime import datetime
from pathlib import Path


HOSPITAL_URL = (
    "https://data.cms.gov/provider-data/sites/default/files/resources/"
    "30edc1d0417a34b58affcc2495a02b0a_1785189969/"
    "Unplanned_Hospital_Visits-Hospital.csv"
)
NATIONAL_URL = (
    "https://data.cms.gov/provider-data/sites/default/files/resources/"
    "d30b0557f1d06bee1d5646d2eaede709_1785189969/"
    "Unplanned_Hospital_Visits-National.csv"
)
FOOTNOTE_URL = (
    "https://data.cms.gov/provider-data/sites/default/files/resources/"
    "f29bb7c812e242f6edfef0a4b7d0eaca_1760630713/Footnote_Crosswalk.csv"
)
EXPECTED_RAW = {
    "hospital": (19048784, "a3e64029ea6daea1f7de163e5b5054b918d0c8be986fccfc47c7a8d5b29a6d1d"),
    "national": (2814, "44e39aedc296f00fa8477a3485a66012cbfcdefb173435199a0b03343c9402c3"),
    "footnote": (3456, "5214e1468fb04c5cdeac8920f2c446cccaa65e2f6f929424cd228042a52d963e"),
}
MEASURE_ID = "READM_30_HF"
NATIONAL_RATE = 21.3
SOURCE_RELEASE = "2026-08-13"

HOSPITAL_FIELDS = [
    "Facility ID", "Facility Name", "Address", "City/Town", "State", "ZIP Code",
    "County/Parish", "Telephone Number", "Measure ID", "Measure Name",
    "Compared to National", "Denominator", "Score", "Lower Estimate",
    "Higher Estimate", "Number of Patients", "Number of Patients Returned",
    "Footnote", "Start Date", "End Date",
]

SELECTED_FIELDS = [
    "facility_id", "facility_name", "city", "state", "county", "measure_id",
    "measure_name", "compared_to_national", "denominator", "score",
    "lower_estimate", "higher_estimate", "number_of_patients",
    "number_of_patients_returned", "footnote_code", "footnote_text",
    "start_date", "end_date", "estimate_status", "source_release",
]

NATIONAL_FIELDS = [
    "measure_id", "measure_name", "national_rate", "number_of_hospitals_worse",
    "number_of_hospitals_same", "number_of_hospitals_better",
    "number_of_hospitals_too_few", "footnote_code", "start_date", "end_date",
    "number_of_hospitals_fewer", "number_of_hospitals_average",
    "number_of_hospitals_more", "number_of_hospitals_too_small",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(url: str, path: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "OpenClinicalLearningCommons/0.17"})
    with urllib.request.urlopen(request, timeout=120) as response, path.open("wb") as target:
        shutil.copyfileobj(response, target)


def validate_raw(label: str, path: Path) -> None:
    expected = EXPECTED_RAW[label]
    actual = (path.stat().st_size, sha256(path))
    if actual != expected:
        raise ValueError(
            f"{label} source changed: expected {expected[0]} bytes and {expected[1]}, "
            f"received {actual[0]} bytes and {actual[1]}"
        )


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def iso_date(value: str) -> str:
    return datetime.strptime(value, "%m/%d/%Y").date().isoformat()


def numeric_or_blank(value: str, integer: bool = False) -> int | float | str:
    if value in {"Not Available", "Not Applicable", ""}:
        return ""
    return int(value) if integer else float(value)


def build_footnotes(raw_path: Path, output_path: Path) -> dict[str, str]:
    with raw_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != ["Footnote", "Footnote Text"]:
            raise ValueError(f"Footnote fields changed: {reader.fieldnames}")
        rows = [
            {"footnote_code": row["Footnote"], "footnote_text": row["Footnote Text"]}
            for row in reader
        ]
    if len(rows) != 32 or len({row["footnote_code"] for row in rows}) != 32:
        raise ValueError(f"Expected 32 unique footnotes, received {len(rows)}")
    write_csv(output_path, ["footnote_code", "footnote_text"], rows)
    return {str(row["footnote_code"]): str(row["footnote_text"]) for row in rows}


def build_national(raw_path: Path, output_path: Path) -> list[dict[str, object]]:
    with raw_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if len(reader.fieldnames or []) != 14:
            raise ValueError(f"National fields changed: {reader.fieldnames}")
        rows = []
        for row in reader:
            rows.append(
                {
                    "measure_id": row["Measure ID"],
                    "measure_name": row["Measure Name"],
                    "national_rate": row["National Rate"],
                    "number_of_hospitals_worse": row["Number of Hospitals Worse"],
                    "number_of_hospitals_same": row["Number of Hospitals Same"],
                    "number_of_hospitals_better": row["Number of Hospitals Better"],
                    "number_of_hospitals_too_few": row["Number of Hospitals Too Few"],
                    "footnote_code": row["Footnote"],
                    "start_date": iso_date(row["Start Date"]),
                    "end_date": iso_date(row["End Date"]),
                    "number_of_hospitals_fewer": row["Number of Hospitals Fewer"],
                    "number_of_hospitals_average": row["Number of Hospitals Average"],
                    "number_of_hospitals_more": row["Number of Hospitals More"],
                    "number_of_hospitals_too_small": row["Number of Hospitals Too Small"],
                }
            )
    if len(rows) != 14 or len({row["measure_id"] for row in rows}) != 14:
        raise ValueError(f"Expected 14 unique national measures, received {len(rows)}")
    selected = next((row for row in rows if row["measure_id"] == MEASURE_ID), None)
    if selected is None or float(selected["national_rate"]) != NATIONAL_RATE:
        raise ValueError("National heart failure benchmark changed")
    write_csv(output_path, NATIONAL_FIELDS, rows)
    return rows


def estimate_status(row: dict[str, str]) -> str:
    if row["Score"] != "Not Available":
        return "reported"
    if row["Compared to National"] == "Number of Cases Too Small" or row["Footnote"] == "1":
        return "too_few"
    return "not_available"


def build_hospitals(raw_path: Path, footnotes: dict[str, str], output_path: Path) -> list[dict[str, object]]:
    with raw_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != HOSPITAL_FIELDS:
            raise ValueError(f"Hospital fields changed: {reader.fieldnames}")
        raw_rows = list(reader)
    if len(raw_rows) != 67060:
        raise ValueError(f"Expected 67,060 hospital rows, received {len(raw_rows):,}")

    rows: list[dict[str, object]] = []
    for row in raw_rows:
        if row["Measure ID"] != MEASURE_ID:
            continue
        code = row["Footnote"]
        if code and code not in footnotes:
            raise ValueError(f"Missing footnote definition for code {code}")
        rows.append(
            {
                "facility_id": row["Facility ID"],
                "facility_name": row["Facility Name"],
                "city": row["City/Town"],
                "state": row["State"],
                "county": row["County/Parish"],
                "measure_id": row["Measure ID"],
                "measure_name": row["Measure Name"],
                "compared_to_national": row["Compared to National"],
                "denominator": numeric_or_blank(row["Denominator"], integer=True),
                "score": numeric_or_blank(row["Score"]),
                "lower_estimate": numeric_or_blank(row["Lower Estimate"]),
                "higher_estimate": numeric_or_blank(row["Higher Estimate"]),
                "number_of_patients": numeric_or_blank(row["Number of Patients"], integer=True),
                "number_of_patients_returned": numeric_or_blank(row["Number of Patients Returned"], integer=True),
                "footnote_code": code,
                "footnote_text": footnotes.get(code, ""),
                "start_date": iso_date(row["Start Date"]),
                "end_date": iso_date(row["End Date"]),
                "estimate_status": estimate_status(row),
                "source_release": SOURCE_RELEASE,
            }
        )
    rows.sort(key=lambda row: str(row["facility_id"]))
    if len(rows) != 4790 or len({row["facility_id"] for row in rows}) != 4790:
        raise ValueError(f"Expected 4,790 unique selected hospital rows, received {len(rows):,}")
    write_csv(output_path, SELECTED_FIELDS, rows)
    return rows


def comparison_group(value: str) -> str:
    return {
        "Better Than the National Rate": "better",
        "No Different Than the National Rate": "no different",
        "Worse Than the National Rate": "worse",
        "Number of Cases Too Small": "too few",
        "Not Available": "not available",
    }[value]


def build_massachusetts(rows: list[dict[str, object]], output_path: Path) -> list[dict[str, object]]:
    ma = [dict(row) for row in rows if row["state"] == "MA"]
    reported = [row for row in ma if row["estimate_status"] == "reported"]
    ranked = sorted(reported, key=lambda row: (-float(row["score"]), str(row["facility_name"])))
    ranks = {str(row["facility_id"]): rank for rank, row in enumerate(ranked, start=1)}

    for row in ma:
        if row["estimate_status"] == "reported":
            denominator = int(row["denominator"])
            row.update(
                {
                    "reported_rank_worst_first": ranks[str(row["facility_id"])],
                    "interval_width": f"{float(row['higher_estimate']) - float(row['lower_estimate']):.1f}",
                    "contains_national_rate": int(
                        float(row["lower_estimate"]) <= NATIONAL_RATE <= float(row["higher_estimate"])
                    ),
                    "denominator_display_group": (
                        "under 100" if denominator < 100 else "100 to 499" if denominator < 500 else "500 or more"
                    ),
                    "top_ten_point_rank": int(ranks[str(row["facility_id"])] <= 10),
                }
            )
        else:
            row.update(
                {
                    "reported_rank_worst_first": "",
                    "interval_width": "",
                    "contains_national_rate": "",
                    "denominator_display_group": "unavailable",
                    "top_ten_point_rank": 0,
                }
            )
        row["source_comparison_group"] = comparison_group(str(row["compared_to_national"]))

    ma.sort(key=lambda row: str(row["facility_id"]))
    if len(ma) != 65 or len(reported) != 53:
        raise ValueError(f"Expected 65 Massachusetts rows and 53 reported, received {len(ma)} and {len(reported)}")
    fields = SELECTED_FIELDS + [
        "reported_rank_worst_first", "interval_width", "contains_national_rate",
        "source_comparison_group", "denominator_display_group", "top_ten_point_rank",
    ]
    write_csv(output_path, fields, ma)
    return ma


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hospital-input", type=Path)
    parser.add_argument("--national-input", type=Path)
    parser.add_argument("--footnote-input", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "data")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="oclc-module06-") as temporary:
        temp = Path(temporary)
        sources = {
            "hospital": args.hospital_input or temp / "hospital.csv",
            "national": args.national_input or temp / "national.csv",
            "footnote": args.footnote_input or temp / "footnote.csv",
        }
        for label, url in (("hospital", HOSPITAL_URL), ("national", NATIONAL_URL), ("footnote", FOOTNOTE_URL)):
            if not sources[label].exists():
                print(f"Downloading {label}: {url}")
                download(url, sources[label])
            validate_raw(label, sources[label])

        output = args.output_dir
        output.mkdir(parents=True, exist_ok=True)
        footnotes = build_footnotes(sources["footnote"], output / "cms_footnote_crosswalk_2026.csv")
        build_national(sources["national"], output / "cms_unplanned_national_2026.csv")
        hospitals = build_hospitals(
            sources["hospital"], footnotes, output / "cms_hf_readmission_hospitals_2026.csv"
        )
        ma = build_massachusetts(hospitals, output / "ma_hf_readmission_uncertainty_2026.csv")

    print(f"Built {len(hospitals):,} national and {len(ma):,} Massachusetts rows")
    for path in sorted(args.output_dir.glob("*.csv")):
        print(f"{path.name}: {sum(1 for _ in path.open(encoding='utf-8')) - 1:,} rows; sha256={sha256(path)}")


if __name__ == "__main__":
    main()
