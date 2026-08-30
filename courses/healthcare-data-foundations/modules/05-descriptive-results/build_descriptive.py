"""Build the FND-1 Module 05 exact descriptive evidence release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
import tempfile
from collections import Counter
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = MODULE_ROOT.parent / "04-cleaning-profiling" / "outputs" / "resolved-analytic-table.csv"
DEFAULT_QUALITY = MODULE_ROOT.parent / "04-cleaning-profiling" / "outputs" / "quality-rule-results.csv"
SOURCE_BYTES = 121_787
SOURCE_SHA256 = "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"
QUALITY_BYTES = 3_607
QUALITY_SHA256 = "c301cd46d6058329d72cc2b71649f5bb1ccf9fbff43f6c97e8b2fc008f791c06"
NUMERIC_FIELDS = {
    "age_at_index", "prior_365d_encounter_count", "prior_365d_acute_count",
    "prior_365d_condition_count", "prior_365d_medication_count",
    "next_30d_days_after_index_stop",
}
PROFILE_SPECS = (
    ("VP01", "death_date", "date availability", "N01", "Available dates describe recorded synthetic deaths only."),
    ("VP02", "age_at_index", "continuous", "N04", "Five accepted ages are at least 100 and remain included."),
    ("VP03", "gender", "categorical", "", "Values preserve the pinned source vocabulary and do not define identity universally."),
    ("VP04", "race", "categorical", "N07", "Rare categories remain exact internally and require cautious display."),
    ("VP05", "ethnicity", "categorical", "", "Values preserve the pinned source vocabulary."),
    ("VP06", "index_class", "categorical", "", "Class describes the selected synthetic index encounter."),
    ("VP07", "index_reason_code", "text availability", "N02", "Available values use a smaller denominator; blank is not no reason clinically."),
    ("VP08", "index_reason_description", "text availability", "N02", "Availability is paired with the source reason code."),
    ("VP09", "prior_365d_encounter_count", "count", "N05", "Two supported counts above 100 remain included; rows are not unique services."),
    ("VP10", "prior_365d_acute_count", "count", "", "Counts describe source rows in the declared lookback."),
    ("VP11", "prior_365d_condition_count", "count", "", "Counts describe source condition rows, not unique clinical burden."),
    ("VP12", "prior_365d_medication_count", "count", "N06", "One supported count above 100 remains included; rows are not unique therapies."),
    ("VP13", "next_30d_state", "categorical", "N03|N08", "No encounter recorded is source-specific; small states require cautious display."),
    ("VP14", "next_30d_days_after_index_stop", "continuous available-case", "N03", "Timing describes 111 recorded next encounters, not all 374 people."),
    ("VP15", "acute_return_90d", "binary categorical", "", "Flag describes a recorded synthetic event in the declared window."),
    ("VP16", "death_90d", "binary categorical", "N08", "The small synthetic-death cell requires cautious interpretation."),
    ("VP17", "endpoint_90d", "categorical", "N08", "Endpoint uses death precedence and small-cell caution."),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def fixed(value: float) -> str:
    return f"{value:.6f}"


def numeric_summary(values: list[str]) -> dict[str, str]:
    numbers = [float(value) for value in values]
    q1, _, q3 = statistics.quantiles(numbers, n=4, method="inclusive")
    return {
        "mean": fixed(statistics.fmean(numbers)),
        "sample_sd": fixed(statistics.stdev(numbers)),
        "median": fixed(statistics.median(numbers)),
        "q1": fixed(q1),
        "q3": fixed(q3),
        "minimum": fixed(min(numbers)),
        "maximum": fixed(max(numbers)),
    }


def wilson(numerator: int, denominator: int, z: float = 1.959963984540054) -> tuple[float, float]:
    proportion = numerator / denominator
    z2 = z * z
    scale = 1 + z2 / denominator
    center = (proportion + z2 / (2 * denominator)) / scale
    half_width = z * math.sqrt((proportion * (1 - proportion) / denominator) + z2 / (4 * denominator * denominator)) / scale
    return 100 * (center - half_width), 100 * (center + half_width)


def profile_rows(source: list[dict[str, str]]) -> list[dict[str, object]]:
    result = []
    for result_id, field, role, conditions, limit in PROFILE_SPECS:
        values = [row[field] for row in source]
        available = [value for value in values if value != ""]
        summary = {key: "" for key in ("mean", "sample_sd", "median", "q1", "q3", "minimum", "maximum")}
        category_counts = ""
        if field in NUMERIC_FIELDS:
            summary.update(numeric_summary(available))
        elif role == "date availability" and available:
            summary["minimum"], summary["maximum"] = min(available), max(available)
        elif "categorical" in role:
            counts = Counter(available)
            category_counts = "|".join(f"{value}={counts[value]}" for value in sorted(counts))
        result.append({
            "result_id": result_id, "field_name": field, "summary_role": role,
            "total_rows": len(source), "available_n": len(available), "missing_n": len(source) - len(available),
            "missing_percent": fixed(100 * (len(source) - len(available)) / len(source)),
            "distinct_available": len(set(available)), **summary, "category_counts": category_counts,
            "retained_conditions": conditions, "interpretation_limit": limit,
        })
    return result


def cross_tab_rows(source: list[dict[str, str]]) -> list[dict[str, object]]:
    specs = (
        ("CT01", "gender", ("F", "M")),
        ("CT02", "index_class", ("emergency", "inpatient")),
    )
    endpoints = ("Acute return", "Death", "No acute return recorded")
    result = []
    for result_id, row_field, row_categories in specs:
        cell_number = 0
        for row_category in row_categories:
            row_denominator = sum(row[row_field] == row_category for row in source)
            for endpoint in endpoints:
                cell_number += 1
                count = sum(row[row_field] == row_category and row["endpoint_90d"] == endpoint for row in source)
                result.append({
                    "result_id": result_id, "cell_id": f"{result_id}-C{cell_number:02d}",
                    "row_variable": row_field, "row_category": row_category,
                    "column_variable": "endpoint_90d", "column_category": endpoint,
                    "n": count, "row_denominator": row_denominator,
                    "row_percent": fixed(100 * count / row_denominator),
                    "cohort_denominator": len(source), "missing_n": 0,
                    "retained_conditions": "N08",
                    "interpretation_limit": "Complete unadjusted synthetic-cohort cross-tab; no group effect or real-population inference.",
                })
    return result


def rate_rows(source: list[dict[str, str]]) -> list[dict[str, object]]:
    specs = (
        ("RT01", "Any recorded next encounter within 30 days", lambda row: row["next_30d_state"] != "No encounter recorded", "next_30d_state is not No encounter recorded", "N03", "Recorded in this source does not mean all other people received no care."),
        ("RT02", "Scheduled care within 30 days", lambda row: row["next_30d_state"] == "Scheduled care", "next_30d_state equals Scheduled care", "N03", "Describes the first recorded next-encounter group in this source."),
        ("RT03", "Urgent care within 30 days", lambda row: row["next_30d_state"] == "Urgent care", "next_30d_state equals Urgent care", "N03|N08", "Small synthetic cell; no quality or access conclusion."),
        ("RT04", "Acute return within 30 days", lambda row: row["next_30d_state"] == "Acute return", "next_30d_state equals Acute return", "N03", "Describes the first next recorded encounter group, not every event."),
        ("RT05", "Any acute return within 90 days", lambda row: row["acute_return_90d"] == "1", "acute_return_90d equals 1", "", "Synthetic-cohort description; no real event-rate inference."),
        ("RT06", "Synthetic death within 90 days", lambda row: row["death_90d"] == "1", "death_90d equals 1", "N08", "Small synthetic cell; no real mortality or performance inference."),
    )
    result = []
    for result_id, measure, predicate, numerator_definition, conditions, limit in specs:
        numerator = sum(predicate(row) for row in source)
        lower, upper = wilson(numerator, len(source))
        result.append({
            "result_id": result_id, "measure": measure, "numerator_definition": numerator_definition,
            "denominator_definition": "all accepted Module 04 synthetic patient rows", "numerator": numerator,
            "denominator": len(source), "percent": fixed(100 * numerator / len(source)),
            "wilson_95_lower_percent": fixed(lower), "wilson_95_upper_percent": fixed(upper),
            "time_window": "after index stop through 30 days" if result_id <= "RT04" else "after index stop through 90 days",
            "unit": "percent of synthetic patients", "retained_conditions": conditions,
            "interpretation_limit": limit,
        })
    return result


def stratum_rows(source: list[dict[str, str]]) -> list[dict[str, object]]:
    result = []
    for result_id, category in (("ST01", "emergency"), ("ST02", "inpatient")):
        rows = [row for row in source if row["index_class"] == category]
        ages = numeric_summary([row["age_at_index"] for row in rows])
        prior = numeric_summary([row["prior_365d_encounter_count"] for row in rows])
        acute = sum(row["acute_return_90d"] == "1" for row in rows)
        death = sum(row["death_90d"] == "1" for row in rows)
        result.append({
            "result_id": result_id, "index_class": category, "n": len(rows),
            "percent_of_cohort": fixed(100 * len(rows) / len(source)),
            "age_mean": ages["mean"], "age_sample_sd": ages["sample_sd"],
            "age_median": ages["median"], "age_q1": ages["q1"], "age_q3": ages["q3"],
            "prior_encounter_median": prior["median"], "prior_encounter_q1": prior["q1"],
            "prior_encounter_q3": prior["q3"], "acute_return_90d_n": acute,
            "acute_return_90d_percent": fixed(100 * acute / len(rows)), "death_90d_n": death,
            "death_90d_percent": fixed(100 * death / len(rows)),
            "retained_conditions": "N04|N05|N06|N08",
            "interpretation_limit": "Unadjusted synthetic-cohort stratum; no class effect, fair comparison, or real-population inference.",
        })
    return result


def registry_rows(profiles: list[dict[str, object]], cross_tabs: list[dict[str, object]], rates: list[dict[str, object]], strata: list[dict[str, object]]) -> list[dict[str, object]]:
    result = []
    for row in profiles:
        available = int(row["available_n"])
        result.append({
            "result_id": row["result_id"], "output_file": "variable-profile.csv",
            "measure_name": f"One-variable profile: {row['field_name']}",
            "numerator_definition": "not applicable; summary over registered field values",
            "denominator_definition": "available nonblank field values" if available < 374 else "all accepted Module 04 synthetic patient rows",
            "denominator_n": available, "exclusions": "none",
            "missing_handling": f"retain {row['missing_n']} blanks; do not convert to zero or a clinical state",
            "time_window": "field-specific as declared in the Module 03 data dictionary",
            "unit": row["summary_role"], "interpretation_limit": row["interpretation_limit"],
            "retained_conditions": row["retained_conditions"],
        })
    for result_id in ("CT01", "CT02"):
        rows = [row for row in cross_tabs if row["result_id"] == result_id]
        result.append({
            "result_id": result_id, "output_file": "cross-tabs.csv",
            "measure_name": f"{rows[0]['row_variable']} by endpoint_90d",
            "numerator_definition": "people in the row-category and endpoint cell",
            "denominator_definition": "people in each complete row category for row percentages",
            "denominator_n": 374, "exclusions": "none", "missing_handling": "no missing row or endpoint values",
            "time_window": "index encounter plus mutually exclusive 90-day endpoint",
            "unit": "count and row percent", "interpretation_limit": rows[0]["interpretation_limit"],
            "retained_conditions": "N08",
        })
    for row in rates:
        result.append({
            "result_id": row["result_id"], "output_file": "rates.csv", "measure_name": row["measure"],
            "numerator_definition": row["numerator_definition"], "denominator_definition": row["denominator_definition"],
            "denominator_n": row["denominator"], "exclusions": "none",
            "missing_handling": "explicit state retained; no blank treated as zero",
            "time_window": row["time_window"], "unit": row["unit"],
            "interpretation_limit": row["interpretation_limit"], "retained_conditions": row["retained_conditions"],
        })
    for row in strata:
        result.append({
            "result_id": row["result_id"], "output_file": "stratified-table.csv",
            "measure_name": f"Index-class stratum: {row['index_class']}",
            "numerator_definition": f"accepted people with index_class equal to {row['index_class']}",
            "denominator_definition": "all accepted Module 04 synthetic patient rows for stratum share; stratum rows for within-stratum summaries",
            "denominator_n": row["n"], "exclusions": "none", "missing_handling": "registered fields are complete",
            "time_window": "index age, 365-day lookback, and 90-day follow-up",
            "unit": "mixed descriptive units stated in column headers",
            "interpretation_limit": row["interpretation_limit"], "retained_conditions": row["retained_conditions"],
        })
    return result


def check_rows(source: list[dict[str, str]], quality: list[dict[str, str]], profiles: list[dict[str, object]], cross_tabs: list[dict[str, object]], rates: list[dict[str, object]], strata: list[dict[str, object]], registry: list[dict[str, object]]) -> list[dict[str, object]]:
    rate_by_id = {row["result_id"]: row for row in rates}
    conditions = {value for row in registry for value in str(row["retained_conditions"]).split("|") if value}
    checks = (
        ("CHK01", "source rows", len(source), 374),
        ("CHK02", "source fields", len(source[0]), 29),
        ("CHK03", "unique patients", len({row["patient_id"] for row in source}), 374),
        ("CHK04", "unique index encounters", len({row["index_encounter_id"] for row in source}), 374),
        ("CHK05", "passing upstream rules", sum(row["detection_status"] == "pass" for row in quality), 28),
        ("CHK06", "retained natural rules", len({row["issue_id"] for row in quality if row["issue_id"].startswith("N")}), 8),
        ("CHK07", "variable profile rows", len(profiles), 17),
        ("CHK08", "profile count reconciliation", sum(int(row["available_n"]) + int(row["missing_n"]) == 374 for row in profiles), 17),
        ("CHK09", "cross-tab cells", len(cross_tabs), 12),
        ("CHK10", "cross-tab table totals", sum(sum(int(row["n"]) for row in cross_tabs if row["result_id"] == result_id) == 374 for result_id in ("CT01", "CT02")), 2),
        ("CHK11", "rate rows", len(rates), 6),
        ("CHK12", "30-day state conservation", int(rate_by_id["RT02"]["numerator"]) + int(rate_by_id["RT03"]["numerator"]) + int(rate_by_id["RT04"]["numerator"]), 111),
        ("CHK13", "stratum rows", len(strata), 2),
        ("CHK14", "stratum population conservation", sum(int(row["n"]) for row in strata), 374),
        ("CHK15", "denominator registry rows", len(registry), 27),
        ("CHK16", "unique registry result IDs", len({row["result_id"] for row in registry}), 27),
        ("CHK17", "retained condition coverage", len(conditions), 8),
        ("CHK18", "source version rows", sum(row["source_release"] == "synthea-csv-apr2020" and row["cohort_definition_version"] == "0.1.0" for row in source), 374),
    )
    return [{"check_id": check_id, "check": text, "observed": observed, "expected": expected, "status": "pass" if observed == expected else "fail"} for check_id, text, observed, expected in checks]


def build(source_path: Path, quality_path: Path, target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if source_path.stat().st_size != SOURCE_BYTES or sha256(source_path) != SOURCE_SHA256:
        raise ValueError("Resolved analytic-table fingerprint changed.")
    if quality_path.stat().st_size != QUALITY_BYTES or sha256(quality_path) != QUALITY_SHA256:
        raise ValueError("Quality-rule-results fingerprint changed.")
    fields, source = read_csv(source_path)
    _, quality = read_csv(quality_path)
    if len(source) != 374 or len(fields) != 29 or len({row["patient_id"] for row in source}) != 374:
        raise ValueError("Resolved analytic-table shape or grain changed.")
    if len(quality) != 28 or any(row["detection_status"] != "pass" for row in quality):
        raise ValueError("Upstream quality-rule status changed.")

    profiles = profile_rows(source)
    cross_tabs = cross_tab_rows(source)
    rates = rate_rows(source)
    strata = stratum_rows(source)
    registry = registry_rows(profiles, cross_tabs, rates, strata)
    checks = check_rows(source, quality, profiles, cross_tabs, rates, strata, registry)
    if any(row["status"] != "pass" for row in checks):
        raise ValueError("One or more descriptive release checks failed.")

    target.mkdir(parents=True)
    outputs = {
        "variable-profile.csv": profiles, "cross-tabs.csv": cross_tabs, "rates.csv": rates,
        "stratified-table.csv": strata, "denominator-registry.csv": registry,
        "descriptive-checks.csv": checks,
    }
    report: dict[str, object] = {
        "status": "pass", "version": "0.1.0",
        "source": {"rows": len(source), "fields": len(fields), "bytes": source_path.stat().st_size, "sha256": sha256(source_path)},
        "quality_results": {"rows": len(quality), "bytes": quality_path.stat().st_size, "sha256": sha256(quality_path)},
        "outputs": {},
    }
    for name, rows in outputs.items():
        path = target / name
        write_csv(path, rows)
        report["outputs"][name] = {"rows": len(rows), "fields": len(rows[0]), "bytes": path.stat().st_size, "sha256": sha256(path)}
    report["decision"] = {"disposition": "accept with conditions", "module_06_source": "exact released CSV tables"}
    with (target / "build-report.json").open("w", encoding="utf-8", newline="") as handle:
        handle.write(json.dumps(report, indent=2) + "\n")
    return report


def self_check() -> None:
    lower, upper = wilson(8, 374)
    assert round(lower, 6) == 1.087782 and round(upper, 6) == 4.163484
    with tempfile.TemporaryDirectory(prefix="fnd1-module05-build-") as temp_dir:
        target = Path(temp_dir) / "outputs"
        report = build(DEFAULT_SOURCE, DEFAULT_QUALITY, target)
        assert report["outputs"]["denominator-registry.csv"]["rows"] == 27
        try:
            build(DEFAULT_SOURCE, DEFAULT_QUALITY, target)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target.")
    print("FND-1 Module 05 descriptive builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--quality-results", type=Path, default=DEFAULT_QUALITY)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.target:
        parser.error("--target is required")
    try:
        report = build(args.source.resolve(), args.quality_results.resolve(), args.target.resolve())
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Build failed: {exc}\n")
    print(
        "FND-1 Module 05 descriptive build passed: "
        f"{report['outputs']['variable-profile.csv']['rows']} profiles, "
        f"{report['outputs']['denominator-registry.csv']['rows']} denominator records."
    )


if __name__ == "__main__":
    main()
