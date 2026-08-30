#!/usr/bin/env python3
"""Build the DA-730 Module 12 public ED reporting dashboard releases."""

from __future__ import annotations

import argparse
import csv
import hashlib
from datetime import date
from pathlib import Path
from statistics import median


MODULE_ROOT = Path(__file__).resolve().parent
DATA_ROOT = MODULE_ROOT / "data"
SOURCE_URL = "https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv"
LANDING_PAGE = "https://data.cms.gov/provider-data/dataset/yv7e-xc69"
EXPECTED_FULL_SHA256 = "1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516"
CMS_RELEASE_DATE = date(2026, 8, 13)
SELECTED_HOSPITAL = "220029"
MEASURE_ORDER = {"EDV": 0, "OP_18b": 1, "OP_22": 2}

SOURCE_OUTPUT = DATA_ROOT / "cms_ma_ed_dashboard_source_2026.csv"
TEACHING_OUTPUT = DATA_ROOT / "ma_ed_public_reporting_dashboard_2026.csv"
DICTIONARY_OUTPUT = DATA_ROOT / "ed_dashboard_measure_dictionary_2026.csv"

SOURCE_FIELDS = (
    "facility_id", "facility_name", "city", "state", "county", "condition",
    "measure_id", "measure_name", "score", "sample", "footnote",
    "period_start", "period_end", "cms_release_date", "source_url",
)
TEACHING_FIELDS = (
    "facility_id", "facility_name", "city", "state", "county", "measure_id",
    "display_label", "unit", "direction", "score_raw", "score_numeric",
    "value_status", "sample", "footnote", "period_start", "period_end",
    "cms_release_date", "ma_reported_n", "ma_median", "ma_min", "ma_max",
    "ma_rank_unfavorable", "selected_hospital", "scenario_threshold",
    "threshold_operator", "threshold_crossed", "threshold_origin",
    "source_lag_days_at_release", "monitoring_use", "action_if_crossed",
    "interpretation_boundary",
)
DICTIONARY_FIELDS = (
    "measure_id", "display_label", "source_measure_name", "unit", "direction",
    "grain", "numerator_or_summary", "denominator_or_population",
    "sample_field_meaning", "reporting_window", "cms_release_date",
    "scenario_trigger", "trigger_status_for_220029", "action_if_crossed",
    "refresh_cadence", "decision_owner", "interpretation_limit", "source_url",
)

MEASURES = {
    "EDV": {
        "label": "Emergency department volume category",
        "unit": "CMS volume category",
        "direction": "context_only",
        "threshold": None,
        "action": "Use as public volume context; do not treat the category as a performance result.",
    },
    "OP_18b": {
        "label": "Median ED time before departure",
        "unit": "minutes",
        "direction": "lower_is_better",
        "threshold": 240.0,
        "action": "Validate the current local throughput definition and review recent encounter-level time data before choosing an intervention.",
    },
    "OP_22": {
        "label": "Patients leaving before being seen",
        "unit": "percent",
        "direction": "lower_is_better",
        "threshold": 10.0,
        "action": "Validate the numerator, denominator, and current local abandonment data, then open a multidisciplinary review if the current local measure confirms the signal.",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def iso_date(value: str) -> str:
    month, day, year = value.split("/")
    return f"{year}-{month}-{day}"


def select_source(path: Path) -> list[dict[str, object]]:
    if sha256(path) != EXPECTED_FULL_SHA256:
        raise ValueError(f"Unexpected CMS full-source SHA-256: {sha256(path)}")
    fields, rows = read_csv(path)
    required = {
        "Facility ID", "Facility Name", "City/Town", "State", "County/Parish",
        "Condition", "Measure ID", "Measure Name", "Score", "Sample", "Footnote",
        "Start Date", "End Date",
    }
    if not required.issubset(fields):
        raise ValueError(f"CMS source is missing fields: {', '.join(sorted(required - set(fields)))}")
    selected = []
    for row in rows:
        if row["State"] != "MA" or row["Measure ID"] not in MEASURE_ORDER:
            continue
        selected.append({
            "facility_id": row["Facility ID"],
            "facility_name": row["Facility Name"],
            "city": row["City/Town"],
            "state": row["State"],
            "county": row["County/Parish"],
            "condition": row["Condition"],
            "measure_id": row["Measure ID"],
            "measure_name": row["Measure Name"],
            "score": row["Score"],
            "sample": row["Sample"],
            "footnote": row["Footnote"],
            "period_start": iso_date(row["Start Date"]),
            "period_end": iso_date(row["End Date"]),
            "cms_release_date": CMS_RELEASE_DATE.isoformat(),
            "source_url": LANDING_PAGE,
        })
    selected.sort(key=lambda row: (str(row["facility_id"]), MEASURE_ORDER[str(row["measure_id"])]))
    if len(selected) != 186 or len({row["facility_id"] for row in selected}) != 62:
        raise ValueError(f"Expected 186 rows across 62 Massachusetts hospitals, received {len(selected)} rows")
    return selected


def numeric(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def display_number(value: float | None) -> str:
    if value is None:
        return ""
    return str(int(value)) if value.is_integer() else f"{value:.1f}"


def build_teaching(source: list[dict[str, str]]) -> list[dict[str, object]]:
    peer: dict[str, list[float]] = {}
    for measure_id in ("OP_18b", "OP_22"):
        peer[measure_id] = sorted(
            value for row in source
            if row["measure_id"] == measure_id
            if (value := numeric(row["score"])) is not None
        )
    output = []
    for row in source:
        measure_id = row["measure_id"]
        config = MEASURES[measure_id]
        value = numeric(row["score"])
        values = peer.get(measure_id, [])
        threshold = config["threshold"]
        period_end = date.fromisoformat(row["period_end"])
        lag = (CMS_RELEASE_DATE - period_end).days
        if value is not None:
            rank = 1 + sum(other > value for other in values)
            status = "reported"
        elif measure_id == "EDV" and row["score"].lower() in {"low", "medium", "high", "very high"}:
            rank = None
            status = "reported_category"
        else:
            rank = None
            status = "not_available"
        crossed = "not_applicable" if threshold is None or value is None else ("yes" if value >= threshold else "no")
        output.append({
            "facility_id": row["facility_id"],
            "facility_name": row["facility_name"],
            "city": row["city"],
            "state": row["state"],
            "county": row["county"],
            "measure_id": measure_id,
            "display_label": config["label"],
            "unit": config["unit"],
            "direction": config["direction"],
            "score_raw": row["score"],
            "score_numeric": display_number(value),
            "value_status": status,
            "sample": row["sample"],
            "footnote": row["footnote"],
            "period_start": row["period_start"],
            "period_end": row["period_end"],
            "cms_release_date": row["cms_release_date"],
            "ma_reported_n": len(values) if values else "",
            "ma_median": display_number(float(median(values))) if values else "",
            "ma_min": display_number(min(values)) if values else "",
            "ma_max": display_number(max(values)) if values else "",
            "ma_rank_unfavorable": rank or "",
            "selected_hospital": "yes" if row["facility_id"] == SELECTED_HOSPITAL else "no",
            "scenario_threshold": display_number(float(threshold)) if threshold is not None else "",
            "threshold_operator": ">=" if threshold is not None else "",
            "threshold_crossed": crossed,
            "threshold_origin": "Mock QI charter for teaching; not a CMS benchmark" if threshold is not None else "Not applicable",
            "source_lag_days_at_release": lag,
            "monitoring_use": "historical_public_reporting_review_only" if lag > 180 else "recent_public_reporting_review",
            "action_if_crossed": config["action"],
            "interpretation_boundary": "Public aggregate reporting can trigger local definition and data review; it cannot establish current operations, cause, or intervention effect.",
        })
    return output


def build_dictionary(source: list[dict[str, str]], teaching: list[dict[str, object]]) -> list[dict[str, object]]:
    source_by_measure = {row["measure_id"]: row for row in source if row["facility_id"] == SELECTED_HOSPITAL}
    selected = {row["measure_id"]: row for row in teaching if row["facility_id"] == SELECTED_HOSPITAL}
    definitions = {
        "EDV": (
            "CMS category derived from submitted ED volume",
            "Volume used for OP-22 public reporting",
            "Sample is blank because the score itself is a volume category",
            "No scenario performance trigger",
        ),
        "OP_18b": (
            "Hospital median of included ED duration values",
            "Included ED visits, excluding transfers and psychiatric or mental-health patients as stated in the source measure name",
            "Number of cases shown by CMS for the hospital score",
            "At or above 240 minutes in the mock QI charter",
        ),
        "OP_22": (
            "Included ED visits where the patient left before being seen",
            "Included ED visits for OP-22",
            "CMS-reported denominator associated with the score",
            "At or above 10 percent in the mock QI charter",
        ),
    }
    rows = []
    for measure_id in ("EDV", "OP_18b", "OP_22"):
        src = source_by_measure[measure_id]
        result = selected[measure_id]
        numerator, denominator, sample_meaning, trigger = definitions[measure_id]
        rows.append({
            "measure_id": measure_id,
            "display_label": MEASURES[measure_id]["label"],
            "source_measure_name": src["measure_name"],
            "unit": MEASURES[measure_id]["unit"],
            "direction": MEASURES[measure_id]["direction"],
            "grain": "One CMS public aggregate score for one hospital and reporting period",
            "numerator_or_summary": numerator,
            "denominator_or_population": denominator,
            "sample_field_meaning": sample_meaning,
            "reporting_window": f"{src['period_start']} through {src['period_end']}",
            "cms_release_date": CMS_RELEASE_DATE.isoformat(),
            "scenario_trigger": trigger,
            "trigger_status_for_220029": result["threshold_crossed"],
            "action_if_crossed": MEASURES[measure_id]["action"],
            "refresh_cadence": "Check each CMS release; use current local data for operational monitoring",
            "decision_owner": "Emergency department quality director",
            "interpretation_limit": result["interpretation_boundary"],
            "source_url": LANDING_PAGE,
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-csv", type=Path, help="Pinned complete CMS Timely and Effective Care hospital CSV")
    args = parser.parse_args()
    if args.source_csv:
        source = select_source(args.source_csv)
        write_csv(SOURCE_OUTPUT, SOURCE_FIELDS, source)
    else:
        if not SOURCE_OUTPUT.exists():
            raise FileNotFoundError("Committed source selection is missing; pass --source-csv to create it")
        fields, source = read_csv(SOURCE_OUTPUT)
        if tuple(fields) != SOURCE_FIELDS:
            raise ValueError("Committed source selection fields changed")
    teaching = build_teaching(source)
    dictionary = build_dictionary(source, teaching)
    write_csv(TEACHING_OUTPUT, TEACHING_FIELDS, teaching)
    write_csv(DICTIONARY_OUTPUT, DICTIONARY_FIELDS, dictionary)
    print(f"Wrote {len(source):,} source rows, {len(teaching):,} teaching rows, and {len(dictionary)} dictionary rows.")
    for path in (SOURCE_OUTPUT, TEACHING_OUTPUT, DICTIONARY_OUTPUT):
        print(f"{path.name}: {sha256(path)}")


if __name__ == "__main__":
    main()
