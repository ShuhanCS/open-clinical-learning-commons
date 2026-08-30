#!/usr/bin/env python3
"""Validate the DA-730 Module 12 ED dashboard teaching releases."""

from __future__ import annotations

import csv
import hashlib
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from statistics import median


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FILES = {
    "source": DATA / "cms_ma_ed_dashboard_source_2026.csv",
    "teaching": DATA / "ma_ed_public_reporting_dashboard_2026.csv",
    "dictionary": DATA / "ed_dashboard_measure_dictionary_2026.csv",
}
EXPECTED = {
    "source": (186, 15, "f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b"),
    "teaching": (186, 31, "fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd"),
    "dictionary": (3, 18, "2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def number(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def main() -> None:
    passed = 0

    def check(condition: bool, message: str) -> None:
        nonlocal passed
        if not condition:
            raise AssertionError(message)
        passed += 1

    loaded: dict[str, tuple[list[str], list[dict[str, str]]]] = {}
    for name, path in FILES.items():
        check(path.exists(), f"Missing {name} release")
        fields, rows = read_csv(path)
        loaded[name] = fields, rows
        expected_rows, expected_columns, expected_hash = EXPECTED[name]
        check(len(rows) == expected_rows, f"Unexpected {name} row count")
        check(len(fields) == expected_columns, f"Unexpected {name} column count")
        check(sha256(path) == expected_hash, f"Unexpected {name} SHA-256")

    source_fields, source = loaded["source"]
    teaching_fields, teaching = loaded["teaching"]
    dictionary_fields, dictionary = loaded["dictionary"]
    source_keys = {(row["facility_id"], row["measure_id"]): row for row in source}
    teaching_keys = {(row["facility_id"], row["measure_id"]): row for row in teaching}

    check(len(source_keys) == len(source), "Source facility-measure keys must be unique")
    check(len(teaching_keys) == len(teaching), "Teaching facility-measure keys must be unique")
    check(set(source_keys) == set(teaching_keys), "Teaching keys differ from source keys")
    check(len({row["facility_id"] for row in source}) == 62, "Expected 62 Massachusetts facilities")
    check(set(row["measure_id"] for row in source) == {"EDV", "OP_18b", "OP_22"}, "Measure set changed")
    check(Counter(row["measure_id"] for row in source) == {"EDV": 62, "OP_18b": 62, "OP_22": 62}, "Measure row counts changed")
    check(all(row["state"] == "MA" for row in source), "Non-Massachusetts row found")
    check(all(row["condition"] == "Emergency Department" for row in source), "Unexpected condition")
    check(all(row["cms_release_date"] == "2026-08-13" for row in source), "CMS release date changed")
    check(all(row["source_url"] == "https://data.cms.gov/provider-data/dataset/yv7e-xc69" for row in source), "Source URL changed")
    check(not ({"address", "telephone_number", "zip_code"} & set(source_fields)), "Unused location or phone fields were retained")

    status_counts = Counter((row["measure_id"], row["value_status"]) for row in teaching)
    check(status_counts[("EDV", "reported_category")] == 53, "EDV reported count changed")
    check(status_counts[("EDV", "not_available")] == 9, "EDV unavailable count changed")
    check(status_counts[("OP_18b", "reported")] == 54, "OP_18b reported count changed")
    check(status_counts[("OP_18b", "not_available")] == 8, "OP_18b unavailable count changed")
    check(status_counts[("OP_22", "reported")] == 53, "OP_22 reported count changed")
    check(status_counts[("OP_22", "not_available")] == 9, "OP_22 unavailable count changed")
    check(all(row["score_raw"] == source_keys[(row["facility_id"], row["measure_id"])]["score"] for row in teaching), "Source scores changed")
    check(all(row["sample"] == source_keys[(row["facility_id"], row["measure_id"])]["sample"] for row in teaching), "Source samples changed")
    check(all(row["footnote"] == source_keys[(row["facility_id"], row["measure_id"])]["footnote"] for row in teaching), "Source footnotes changed")
    check(all(row["period_start"] == source_keys[(row["facility_id"], row["measure_id"])]["period_start"] for row in teaching), "Period starts changed")
    check(all(row["period_end"] == source_keys[(row["facility_id"], row["measure_id"])]["period_end"] for row in teaching), "Period ends changed")
    check(all(row["interpretation_boundary"].startswith("Public aggregate reporting") for row in teaching), "Interpretation boundary changed")
    check(all(row["monitoring_use"] == "historical_public_reporting_review_only" for row in teaching), "Historical-use label changed")

    reported: dict[str, list[float]] = defaultdict(list)
    for row in teaching:
        value = number(row["score_numeric"])
        if value is not None:
            reported[row["measure_id"]].append(value)
            check(row["value_status"] == "reported", "Numeric score not marked reported")
    check(sorted(reported["OP_18b"]) == sorted(number(row["score"]) for row in source if row["measure_id"] == "OP_18b" and number(row["score"]) is not None), "OP_18b numeric selection changed")
    check(sorted(reported["OP_22"]) == sorted(number(row["score"]) for row in source if row["measure_id"] == "OP_22" and number(row["score"]) is not None), "OP_22 numeric selection changed")
    check(median(reported["OP_18b"]) == 211.5, "OP_18b median changed")
    check(median(reported["OP_22"]) == 3, "OP_22 median changed")
    check(min(reported["OP_18b"]) == 113 and max(reported["OP_18b"]) == 336, "OP_18b range changed")
    check(min(reported["OP_22"]) == 0 and max(reported["OP_22"]) == 23, "OP_22 range changed")
    check(all(row["ma_reported_n"] == "54" for row in teaching if row["measure_id"] == "OP_18b"), "OP_18b peer count changed")
    check(all(row["ma_reported_n"] == "53" for row in teaching if row["measure_id"] == "OP_22"), "OP_22 peer count changed")
    check(all(row["ma_median"] == "211.5" for row in teaching if row["measure_id"] == "OP_18b"), "OP_18b repeated median changed")
    check(all(row["ma_median"] == "3" for row in teaching if row["measure_id"] == "OP_22"), "OP_22 repeated median changed")

    selected = {row["measure_id"]: row for row in teaching if row["selected_hospital"] == "yes"}
    check(set(selected) == {"EDV", "OP_18b", "OP_22"}, "Selected hospital measure set changed")
    check(all(row["facility_id"] == "220029" for row in selected.values()), "Selected facility changed")
    check(all(row["facility_name"] == "ANNA JAQUES HOSPITAL" for row in selected.values()), "Selected facility name changed")
    check(selected["EDV"]["score_raw"] == "low", "Selected ED volume changed")
    check(selected["OP_18b"]["score_numeric"] == "188", "Selected OP_18b score changed")
    check(selected["OP_18b"]["sample"] == "422", "Selected OP_18b sample changed")
    check(selected["OP_18b"]["ma_rank_unfavorable"] == "45", "Selected OP_18b rank changed")
    check(selected["OP_18b"]["threshold_crossed"] == "no", "Selected OP_18b trigger changed")
    check(selected["OP_22"]["score_numeric"] == "23", "Selected OP_22 score changed")
    check(selected["OP_22"]["sample"] == "19211", "Selected OP_22 denominator changed")
    check(selected["OP_22"]["ma_rank_unfavorable"] == "1", "Selected OP_22 rank changed")
    check(selected["OP_22"]["threshold_crossed"] == "yes", "Selected OP_22 trigger changed")
    check(selected["OP_18b"]["source_lag_days_at_release"] == "317", "OP_18b source lag changed")
    check(selected["OP_22"]["source_lag_days_at_release"] == "590", "OP_22 source lag changed")
    check((date.fromisoformat(selected["OP_22"]["cms_release_date"]) - date.fromisoformat(selected["OP_22"]["period_end"])).days == 590, "OP_22 source lag formula changed")
    check(sum(row["selected_hospital"] == "yes" for row in teaching) == 3, "Selected-hospital row count changed")
    check(sum(row["threshold_crossed"] == "yes" for row in teaching if row["facility_id"] == "220029") == 1, "Selected trigger count changed")
    check(all("not a CMS benchmark" in row["threshold_origin"] for row in teaching if row["scenario_threshold"]), "Threshold origin changed")

    check(set(row["measure_id"] for row in dictionary) == {"EDV", "OP_18b", "OP_22"}, "Dictionary measure set changed")
    check(len({row["measure_id"] for row in dictionary}) == len(dictionary), "Dictionary keys must be unique")
    check(all(row["source_url"] == "https://data.cms.gov/provider-data/dataset/yv7e-xc69" for row in dictionary), "Dictionary URL changed")
    check(all(row["decision_owner"] == "Emergency department quality director" for row in dictionary), "Decision owner changed")
    check(all("current local data" in row["refresh_cadence"] for row in dictionary), "Refresh boundary changed")
    check({row["measure_id"]: row["trigger_status_for_220029"] for row in dictionary} == {"EDV": "not_applicable", "OP_18b": "no", "OP_22": "yes"}, "Dictionary trigger states changed")
    check(all(field in teaching_fields for field in ("period_end", "source_lag_days_at_release", "action_if_crossed")), "Teaching action fields are missing")
    check(all(field in dictionary_fields for field in ("numerator_or_summary", "denominator_or_population", "interpretation_limit")), "Dictionary definition fields are missing")

    print(f"Module 12 ED dashboard data passed {passed} checks.")


if __name__ == "__main__":
    main()
