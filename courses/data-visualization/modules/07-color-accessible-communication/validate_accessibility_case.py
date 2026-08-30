#!/usr/bin/env python3
"""Validate the DA-730 Module 07 accessibility teaching release."""

from __future__ import annotations

import csv
import hashlib
import re
from collections import Counter
from pathlib import Path

from build_accessibility_case import ENCODINGS, OUTPUT_FIELDS, SOURCE_SHA256, contrast_ratio


MODULE_ROOT = Path(__file__).resolve().parent
SOURCE = MODULE_ROOT.parent / "06-uncertainty-variation-small-numbers" / "data" / "ma_hf_readmission_uncertainty_2026.csv"
DATA = MODULE_ROOT / "data" / "accessibility_hf_readmission_2026.csv"
SOURCE_FIELDS = (
    "facility_id",
    "facility_name",
    "city",
    "county",
    "measure_id",
    "measure_name",
    "denominator",
    "score",
    "lower_estimate",
    "higher_estimate",
    "start_date",
    "end_date",
    "estimate_status",
    "source_comparison_group",
    "footnote_text",
    "source_release",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def main() -> int:
    checks: list[str] = []

    def check(condition: bool, label: str) -> None:
        if not condition:
            raise AssertionError(label)
        checks.append(label)

    check(SOURCE.is_file(), "Module 06 source exists")
    check(DATA.is_file(), "Module 07 release exists")
    check(sha256(SOURCE) == SOURCE_SHA256, "Module 06 source checksum matches")

    source_fields, source_rows = read_rows(SOURCE)
    fields, rows = read_rows(DATA)
    check(tuple(fields) == OUTPUT_FIELDS, "released columns match the contract")
    check(len(source_rows) == 65, "source has 65 rows")
    check(len(rows) == 65, "release has 65 rows")
    check(len({row["facility_id"] for row in rows}) == 65, "facility IDs are unique")
    check(all(field in source_fields for field in SOURCE_FIELDS), "source comparison fields exist")

    source_by_id = {row["facility_id"]: row for row in source_rows}
    check(set(source_by_id) == {row["facility_id"] for row in rows}, "release preserves every source facility")
    check(
        all(row[field] == source_by_id[row["facility_id"]][field] for row in rows for field in SOURCE_FIELDS),
        "release preserves every source value used by the module",
    )

    status_counts = Counter(row["estimate_status"] for row in rows)
    display_counts = Counter(row["display_status"] for row in rows)
    check(status_counts == {"reported": 53, "too_few": 2, "not_available": 10}, "source status counts reconcile")
    check(display_counts == {"no different": 52, "worse": 1, "too few": 2, "not available": 10}, "display status counts reconcile")
    check(all(row["measure_id"] == "READM_30_HF" for row in rows), "measure ID is fixed")
    check(all(row["start_date"] == "2023-07-01" and row["end_date"] == "2025-06-30" for row in rows), "reporting period is fixed")
    check(all(row["source_release"] == "2026-08-13" for row in rows), "source release is fixed")

    check([int(row["reading_order"]) for row in rows] == list(range(1, 66)), "reading order is complete and unique")
    reported = [row for row in rows if row["estimate_status"] == "reported"]
    check(len(reported) == 53, "53 reported rows lead the reading order")
    check(all(rows[index]["estimate_status"] == "reported" for index in range(53)), "reported rows appear before unavailable rows")
    check([float(row["score"]) for row in reported] == sorted((float(row["score"]) for row in reported), reverse=True), "reported rows use descending score order")

    check(all(not row["score"] and not row["lower_estimate"] and not row["higher_estimate"] for row in rows if row["estimate_status"] != "reported"), "unavailable estimates remain blank")
    check(all(row["score"] and row["lower_estimate"] and row["higher_estimate"] for row in reported), "reported estimates remain complete")
    check(all(float(row["lower_estimate"]) <= float(row["score"]) <= float(row["higher_estimate"]) for row in reported), "reported points stay inside source intervals")
    check(min(float(row["score"]) for row in reported) == 19.7 and max(float(row["score"]) for row in reported) == 25.2, "score range is unchanged")
    check(min(int(row["denominator"]) for row in reported) == 30 and max(int(row["denominator"]) for row in reported) == 2088, "denominator range is unchanged")

    for status, encoding in ENCODINGS.items():
        status_rows = [row for row in rows if row["display_status"] == status]
        if status_rows:
            for key, expected in encoding.items():
                check(all(row[key] == expected for row in status_rows), f"{status} {key} matches the encoding contract")
            expected_white = round(contrast_ratio(encoding["display_color_hex"], "#FFFFFF"), 2)
            expected_black = round(contrast_ratio(encoding["display_color_hex"], "#000000"), 2)
            check(all(float(row["contrast_on_white"]) == expected_white for row in status_rows), f"{status} white contrast is reproducible")
            check(all(float(row["contrast_on_black"]) == expected_black for row in status_rows), f"{status} black contrast is reproducible")
            check(expected_white >= 4.5, f"{status} color has at least 4.5 to 1 contrast on white")

    check(all(row["display_symbol"] and row["display_shape"] and row["display_label"] for row in rows), "every status has redundant text and shape cues")
    check(len({row["display_color_hex"] for row in rows}) == 4, "four present statuses use four colors")
    check(all(re.fullmatch(r"#[0-9A-F]{6}", row["display_color_hex"]) for row in rows), "colors use uppercase six-digit hex values")
    check(all(row["facility_name"] in row["short_alt_row"] for row in rows), "every short alternative names the facility")
    check(all("source interval" in row["short_alt_row"] and "denominator" in row["short_alt_row"] for row in reported), "reported alternatives preserve interval and denominator")
    check(all("no score or source interval" in row["short_alt_row"] for row in rows if row["estimate_status"] != "reported"), "unavailable alternatives explain missing values")

    print(f"Module 07 accessibility data passed {len(checks)} checks.")
    print(f"Rows: {len(rows)}")
    print(f"SHA-256: {sha256(DATA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
