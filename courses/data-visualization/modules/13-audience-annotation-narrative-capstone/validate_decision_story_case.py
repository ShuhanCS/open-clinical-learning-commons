#!/usr/bin/env python3
"""Validate the released inputs and invariants for DA-730 Module 13."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = MODULE_ROOT.parents[3]
UPSTREAM = REPO_ROOT / "courses" / "data-visualization" / "modules" / "12-dashboards-multi-view-composition"
TEACHING = UPSTREAM / "data" / "ma_ed_public_reporting_dashboard_2026.csv"
DICTIONARY = UPSTREAM / "data" / "ed_dashboard_measure_dictionary_2026.csv"
SOURCE = UPSTREAM / "data" / "cms_ma_ed_dashboard_source_2026.csv"

EXPECTED_HASHES = {
    TEACHING: "fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd",
    DICTIONARY: "2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412",
    SOURCE: "f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    checks: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            raise AssertionError(message)
        checks.append(message)

    for path, expected in EXPECTED_HASHES.items():
        check(path.is_file(), f"missing {path.name}")
        check(sha256(path) == expected, f"checksum mismatch for {path.name}")

    teaching_fields, teaching = read_csv(TEACHING)
    dictionary_fields, dictionary = read_csv(DICTIONARY)
    source_fields, source = read_csv(SOURCE)

    check(len(teaching) == 186, "teaching row count")
    check(len(teaching_fields) == 31, "teaching column count")
    check(len(dictionary) == 3, "dictionary row count")
    check(len(dictionary_fields) == 18, "dictionary column count")
    check(len(source) == 186, "source row count")
    check(len(source_fields) == 15, "source column count")
    check(len({row["facility_id"] for row in teaching}) == 62, "teaching facility count")
    check({row["measure_id"] for row in teaching} == {"EDV", "OP_18b", "OP_22"}, "teaching measure set")
    check(all(sum(row["measure_id"] == measure for row in teaching) == 62 for measure in ("EDV", "OP_18b", "OP_22")), "one row per facility and measure")
    check({row["measure_id"] for row in dictionary} == {"EDV", "OP_18b", "OP_22"}, "dictionary measure set")

    selected = [row for row in teaching if row["selected_hospital"] == "yes"]
    check(len(selected) == 3, "selected row count")
    check({row["facility_id"] for row in selected} == {"220029"}, "selected facility ID")
    check({row["facility_name"] for row in selected} == {"ANNA JAQUES HOSPITAL"}, "selected facility name")
    check({row["city"] for row in selected} == {"NEWBURYPORT"}, "selected city")
    check({row["state"] for row in selected} == {"MA"}, "selected state")

    by_measure = {row["measure_id"]: row for row in selected}
    edv = by_measure["EDV"]
    op18 = by_measure["OP_18b"]
    op22 = by_measure["OP_22"]

    check(edv["score_raw"] == "low", "selected EDV value")
    check(edv["value_status"] == "reported_category", "selected EDV status")
    check(edv["period_start"] == "2024-01-01" and edv["period_end"] == "2024-12-31", "selected EDV period")
    check(edv["source_lag_days_at_release"] == "590", "selected EDV lag")
    check(edv["threshold_crossed"] == "not_applicable", "selected EDV trigger status")

    check(op18["score_numeric"] == "188", "selected OP_18b value")
    check(op18["unit"] == "minutes", "selected OP_18b unit")
    check(op18["sample"] == "422", "selected OP_18b sample")
    check(op18["ma_reported_n"] == "54", "selected OP_18b peer count")
    check(op18["ma_median"] == "211.5", "selected OP_18b median")
    check(op18["ma_rank_unfavorable"] == "45", "selected OP_18b rank")
    check(op18["scenario_threshold"] == "240", "selected OP_18b threshold")
    check(op18["threshold_crossed"] == "no", "selected OP_18b trigger result")
    check(op18["period_start"] == "2024-10-01" and op18["period_end"] == "2025-09-30", "selected OP_18b period")
    check(op18["source_lag_days_at_release"] == "317", "selected OP_18b lag")

    check(op22["score_numeric"] == "23", "selected OP_22 value")
    check(op22["unit"] == "percent", "selected OP_22 unit")
    check(op22["sample"] == "19211", "selected OP_22 sample")
    check(op22["ma_reported_n"] == "53", "selected OP_22 peer count")
    check(op22["ma_median"] == "3", "selected OP_22 median")
    check(op22["ma_rank_unfavorable"] == "1", "selected OP_22 rank")
    check(op22["scenario_threshold"] == "10", "selected OP_22 threshold")
    check(op22["threshold_crossed"] == "yes", "selected OP_22 trigger result")
    check(op22["period_start"] == "2024-01-01" and op22["period_end"] == "2024-12-31", "selected OP_22 period")
    check(op22["source_lag_days_at_release"] == "590", "selected OP_22 lag")

    check(all(row["cms_release_date"] == "2026-08-13" for row in selected), "selected CMS release date")
    check(all(row["monitoring_use"] == "historical_public_reporting_review_only" for row in selected), "selected monitoring-use label")
    check(all("current operations" in row["interpretation_boundary"] for row in selected), "selected current-operations boundary")
    check("not a CMS benchmark" in op18["threshold_origin"], "OP_18b trigger origin")
    check("not a CMS benchmark" in op22["threshold_origin"], "OP_22 trigger origin")
    check("current local" in op18["action_if_crossed"], "OP_18b action boundary")
    check("current local" in op22["action_if_crossed"], "OP_22 action boundary")

    dict_by_measure = {row["measure_id"]: row for row in dictionary}
    check(dict_by_measure["EDV"]["unit"] == "CMS volume category", "dictionary EDV unit")
    check(dict_by_measure["OP_18b"]["unit"] == "minutes", "dictionary OP_18b unit")
    check(dict_by_measure["OP_22"]["unit"] == "percent", "dictionary OP_22 unit")
    check(dict_by_measure["OP_18b"]["direction"] == "lower_is_better", "dictionary OP_18b direction")
    check(dict_by_measure["OP_22"]["direction"] == "lower_is_better", "dictionary OP_22 direction")
    check(all(row["decision_owner"] == "Emergency department quality director" for row in dictionary), "dictionary decision owner")
    check(all("current local data" in row["refresh_cadence"] for row in dictionary), "dictionary refresh boundary")
    check(all(row["source_url"] == "https://data.cms.gov/provider-data/dataset/yv7e-xc69" for row in dictionary), "dictionary source URL")
    check(all("cannot establish current operations" in row["interpretation_limit"].lower() for row in dictionary), "dictionary current-operations limit")

    reported_op22 = [float(row["score_numeric"]) for row in teaching if row["measure_id"] == "OP_22" and row["value_status"] == "reported"]
    reported_op18 = [float(row["score_numeric"]) for row in teaching if row["measure_id"] == "OP_18b" and row["value_status"] == "reported"]
    check(len(reported_op22) == 53, "reported OP_22 values")
    check(max(reported_op22) == 23, "maximum OP_22 value")
    check(len(reported_op18) == 54, "reported OP_18b values")
    check(min(reported_op18) == 113 and max(reported_op18) == 336, "OP_18b range")

    print(f"Module 13 decision story data passed {len(checks)} checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
