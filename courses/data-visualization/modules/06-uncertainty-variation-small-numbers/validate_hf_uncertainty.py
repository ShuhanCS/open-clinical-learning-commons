#!/usr/bin/env python3
"""Validate the released data contract for DA-730 Module 06."""

from __future__ import annotations

import csv
import hashlib
import itertools
import statistics
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
EXPECTED_HASHES = {
    "cms_footnote_crosswalk_2026.csv": "94d22120d0efcb0d6f98f3470bce8a7cffb3cf657eb95179556198c4ebae84e7",
    "cms_hf_readmission_hospitals_2026.csv": "e69fcee79711ef8496cb32205b492e6e3a788c4e63009bc1330a84216b0edeba",
    "cms_unplanned_national_2026.csv": "408c2d3f27a93c9294f9399e6a0deabfe70076685a5e06f285daf857e92161f9",
    "ma_hf_readmission_uncertainty_2026.csv": "33e6284a1064bb12600903526e4e65c009f875d9e6f6a3f25783d3a9a4b00727",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(name: str) -> tuple[list[str], list[dict[str, str]]]:
    with (DATA / name).open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        return list(reader.fieldnames or []), list(reader)


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def record(name: str, passed: bool, result: object) -> None:
        checks.append((name, bool(passed), str(result)))

    for name, expected in EXPECTED_HASHES.items():
        actual = sha256(DATA / name)
        record(f"hash {name}", actual == expected, actual)

    footnote_fields, footnotes = read_csv("cms_footnote_crosswalk_2026.csv")
    footnote_map = {row["footnote_code"]: row["footnote_text"] for row in footnotes}
    record("footnote fields", footnote_fields == ["footnote_code", "footnote_text"], footnote_fields)
    record("footnote rows", len(footnotes) == 32, len(footnotes))
    record("footnote identities", len(footnote_map) == 32, len(footnote_map))
    record("too-few definition", footnote_map.get("1") == "The number of cases/patients is too few to report.", footnote_map.get("1"))
    record("unavailable definition", footnote_map.get("5") == "Results are not available for this reporting period.", footnote_map.get("5"))

    national_fields, national = read_csv("cms_unplanned_national_2026.csv")
    record("national fields", len(national_fields) == 14, len(national_fields))
    record("national rows", len(national) == 14, len(national))
    record("national measures", len({row["measure_id"] for row in national}) == 14, len({row["measure_id"] for row in national}))
    hf_national = next(row for row in national if row["measure_id"] == "READM_30_HF")
    record("national benchmark", float(hf_national["national_rate"]) == 21.3, hf_national["national_rate"])
    record("national period", (hf_national["start_date"], hf_national["end_date"]) == ("2023-07-01", "2025-06-30"), f"{hf_national['start_date']} to {hf_national['end_date']}")
    national_counts = tuple(int(hf_national[field]) for field in (
        "number_of_hospitals_worse", "number_of_hospitals_same",
        "number_of_hospitals_better", "number_of_hospitals_too_few",
    ))
    record("national category counts", national_counts == (38, 3253, 21, 1121), national_counts)

    hospital_fields, hospitals = read_csv("cms_hf_readmission_hospitals_2026.csv")
    record("hospital fields", len(hospital_fields) == 20, len(hospital_fields))
    record("hospital rows", len(hospitals) == 4790, len(hospitals))
    record("hospital identities", len({row["facility_id"] for row in hospitals}) == 4790, len({row["facility_id"] for row in hospitals}))
    record("measure contract", {row["measure_id"] for row in hospitals} == {"READM_30_HF"}, {row["measure_id"] for row in hospitals})
    record("hospital period", {(row["start_date"], row["end_date"]) for row in hospitals} == {("2023-07-01", "2025-06-30")}, "one expected period")
    statuses = Counter(row["estimate_status"] for row in hospitals)
    record("national status counts", statuses == {"reported": 3253, "too_few": 1020, "not_available": 517}, statuses)
    comparisons = Counter(row["compared_to_national"] for row in hospitals)
    expected_comparisons = {
        "No Different Than the National Rate": 3194,
        "Number of Cases Too Small": 1020,
        "Not Available": 517,
        "Worse Than the National Rate": 38,
        "Better Than the National Rate": 21,
    }
    record("national comparison labels", comparisons == expected_comparisons, comparisons)
    reported = [row for row in hospitals if row["estimate_status"] == "reported"]
    record("reported values complete", all(row["denominator"] and row["score"] and row["lower_estimate"] and row["higher_estimate"] for row in reported), len(reported))
    record("reported intervals contain point", all(float(row["lower_estimate"]) <= float(row["score"]) <= float(row["higher_estimate"]) for row in reported), len(reported))
    unavailable = [row for row in hospitals if row["estimate_status"] != "reported"]
    record("unavailable values blank", all(not row["score"] and not row["lower_estimate"] and not row["higher_estimate"] for row in unavailable), len(unavailable))
    record("footnote joins", all(not row["footnote_code"] or row["footnote_text"] == footnote_map[row["footnote_code"]] for row in hospitals), "all used codes")

    ma_fields, ma = read_csv("ma_hf_readmission_uncertainty_2026.csv")
    required = {
        "reported_rank_worst_first", "interval_width", "contains_national_rate",
        "source_comparison_group", "denominator_display_group", "top_ten_point_rank",
    }
    record("Massachusetts derived fields", required.issubset(ma_fields), sorted(required))
    record("Massachusetts rows", len(ma) == 65, len(ma))
    record("Massachusetts only", {row["state"] for row in ma} == {"MA"}, {row["state"] for row in ma})
    ma_status = Counter(row["estimate_status"] for row in ma)
    record("Massachusetts status", ma_status == {"reported": 53, "not_available": 10, "too_few": 2}, ma_status)
    ma_reported = [row for row in ma if row["estimate_status"] == "reported"]
    ma_comparison = Counter(row["source_comparison_group"] for row in ma_reported)
    record("Massachusetts comparison", ma_comparison == {"no different": 52, "worse": 1}, ma_comparison)
    denominators = [int(row["denominator"]) for row in ma_reported]
    record("denominator range", (min(denominators), max(denominators)) == (30, 2088), (min(denominators), max(denominators)))
    record("denominator median", statistics.median(denominators) == 538, statistics.median(denominators))
    record("reported under 100", sum(value < 100 for value in denominators) == 4, sum(value < 100 for value in denominators))
    scores = [float(row["score"]) for row in ma_reported]
    widths = [float(row["interval_width"]) for row in ma_reported]
    record("score range", (min(scores), max(scores)) == (19.7, 25.2), (min(scores), max(scores)))
    record("interval-width range", (min(widths), max(widths)) == (6.9, 9.2), (min(widths), max(widths)))
    record("interval-width formula", all(abs(float(row["interval_width"]) - (float(row["higher_estimate"]) - float(row["lower_estimate"]))) < 1e-9 for row in ma_reported), len(ma_reported))
    ranks = sorted(int(row["reported_rank_worst_first"]) for row in ma_reported)
    record("rank sequence", ranks == list(range(1, 54)), f"{ranks[0]} to {ranks[-1]}")
    top_ten = [row for row in ma_reported if row["top_ten_point_rank"] == "1"]
    record("top-ten rows", len(top_ten) == 10, len(top_ten))
    record("top-ten source contrast", Counter(row["source_comparison_group"] for row in top_ten) == {"no different": 9, "worse": 1}, Counter(row["source_comparison_group"] for row in top_ten))
    top = next(row for row in ma_reported if row["reported_rank_worst_first"] == "1")
    bottom = next(row for row in ma_reported if row["reported_rank_worst_first"] == "53")
    record("rank endpoints", (top["facility_name"], top["score"], bottom["facility_name"], bottom["score"]) == ("SAINT ANNE'S HOSPITAL", "25.2", "MASSACHUSETTS GENERAL HOSPITAL", "19.7"), f"{top['facility_name']} to {bottom['facility_name']}")
    overlap_pairs = sum(
        not (float(a["higher_estimate"]) < float(b["lower_estimate"]) or float(b["higher_estimate"]) < float(a["lower_estimate"]))
        for a, b in itertools.combinations(ma_reported, 2)
    )
    record("descriptive interval overlap", overlap_pairs == 1378, overlap_pairs)

    print("DA-730 Module 06 validation report")
    for name, passed, result in checks:
        print(f"{'PASS' if passed else 'FAIL'}\t{name}\t{result}")
    failures = [name for name, passed, _ in checks if not passed]
    if failures:
        print(f"FAILED: {len(failures)} checks: {', '.join(failures)}", file=sys.stderr)
        return 1
    print(f"PASS: {len(checks)} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
