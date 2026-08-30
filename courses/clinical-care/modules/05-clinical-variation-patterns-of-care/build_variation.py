"""Build deterministic APP-1 Module 05 clinical-variation evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sqlite3
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy.stats import chi2_contingency, fisher_exact


MODULE_ROOT = Path(__file__).resolve().parent
DEFAULT_COHORT = MODULE_ROOT.parent / "02-longitudinal-cohorts-followup" / "outputs" / "analysis-cohort.csv"
DEFAULT_EXPECTED = MODULE_ROOT.parent / "04-risk-adjustment-fair-comparison" / "outputs" / "expected-outcomes.csv"
MEASURE_CONTRACT = MODULE_ROOT / "measure-contract.csv"
ANALYSIS_CONTRACT = MODULE_ROOT / "variation-contract.json"
EXPECTED_COHORT = {"rows": 476, "fields": 49, "bytes": 200699, "sha256": "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5"}
EXPECTED_OUTCOMES = {"rows": 476, "fields": 12, "bytes": 54320, "sha256": "e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e"}
EXPECTED_DATABASE_SHA256 = "1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a"
SITE_ORDER = ("SITE-A", "SITE-B", "SITE-C", "SITE-D", "SITE-E", "SITE-F")
SCHEDULED_CLASSES = ("ambulatory", "outpatient", "wellness")
ACUTE_CLASSES = ("emergency", "inpatient")
WINDOWS = (("days_31_90", 30, 90, 60), ("days_91_180", 90, 180, 90), ("days_181_365", 180, 365, 185))
OUTPUT_FILES = (
    "analysis-checks.csv", "build-report.json", "care-patterns.csv", "clinical-subgroup-variation.csv",
    "exposure-variation.csv", "measure-summary.csv", "record-mix.csv", "site-summary.csv",
    "site-variation.csv", "time-variation.csv", "variation-figure.svg",
)
BINARY_MEASURES = (
    ("M02", "scheduled_continuity_31_90_flag"),
    ("M03", "scheduled_any_31_365_flag"),
    ("M04", "medication_record_31_365_flag"),
    ("M05", "medication_reconciliation_31_365_flag"),
    ("M06", "procedure_record_31_365_flag"),
    ("M10", "event_indicator"),
)
SITE_MEASURES = (
    ("M01", "landmark_exposure"), ("M02", "scheduled_continuity_31_90_flag"),
    ("M04", "medication_record_31_365_flag"), ("M05", "medication_reconciliation_31_365_flag"),
    ("M06", "procedure_record_31_365_flag"), ("M10", "event_indicator"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fixed(value: float) -> str:
    return f"{value:.8f}"


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def verify_csv(path: Path, expected: dict[str, object], label: str) -> pd.DataFrame:
    path = path.resolve()
    if path.stat().st_size != expected["bytes"] or sha256(path) != expected["sha256"]:
        raise ValueError(f"{label} fingerprint changed")
    frame = pd.read_csv(path)
    if len(frame) != expected["rows"] or len(frame.columns) != expected["fields"]:
        raise ValueError(f"{label} shape changed")
    return frame


def source_records(connection: sqlite3.Connection, cohort: pd.DataFrame, table: str, date_field: str, fields: str) -> pd.DataFrame:
    ids = cohort["patient_id"].tolist()
    placeholders = ",".join("?" for _ in ids)
    rows = pd.read_sql_query(f"SELECT patient, {date_field}, {fields} FROM {table} WHERE patient IN ({placeholders})", connection, params=ids)
    rows = rows.merge(cohort[["patient_id", "index_stop"]], left_on="patient", right_on="patient_id", validate="many_to_one")
    rows[date_field] = pd.to_datetime(rows[date_field], utc=True)
    rows["index_stop"] = pd.to_datetime(rows["index_stop"], utc=True)
    rows["days_from_discharge"] = (rows[date_field] - rows["index_stop"]).dt.total_seconds() / 86400
    return rows.drop(columns=["index_stop"])


def counts_by_person(records: pd.DataFrame, ids: pd.Index) -> pd.Series:
    return records.groupby("patient").size().reindex(ids, fill_value=0).astype(int)


def difference_rows(frame: pd.DataFrame, group_field: str, group_one: object, group_zero: object, measures: dict[str, dict[str, str]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    one = frame[frame[group_field] == group_one]
    zero = frame[frame[group_field] == group_zero]
    for measure_id, field in BINARY_MEASURES:
        x1, n1 = int(one[field].sum()), len(one)
        x0, n0 = int(zero[field].sum()), len(zero)
        p1, p0 = x1 / n1, x0 / n0
        difference = p1 - p0
        standard_error = math.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)
        lower, upper = difference - 1.96 * standard_error, difference + 1.96 * standard_error
        p_value = float(fisher_exact([[x1, n1 - x1], [x0, n0 - x0]], alternative="two-sided").pvalue)
        threshold = float(measures[measure_id]["operational_threshold"])
        rows.append({
            "measure_id": measure_id,
            "measure": measures[measure_id]["label"],
            "group_one": str(group_one), "group_one_people": n1, "group_one_numerator": x1, "group_one_proportion": fixed(p1),
            "group_zero": str(group_zero), "group_zero_people": n0, "group_zero_numerator": x0, "group_zero_proportion": fixed(p0),
            "absolute_difference": fixed(difference), "lower95": fixed(lower), "upper95": fixed(upper),
            "fisher_two_sided_p": fixed(p_value), "operational_threshold": fixed(threshold),
            "threshold_met": "yes" if abs(difference) >= threshold else "no",
            "interval_excludes_zero": "yes" if lower > 0 or upper < 0 else "no",
            "claim_limit": measures[measure_id]["claim_limit"],
        })
    return rows


def wilson_interval(numerator: int, denominator: int) -> tuple[float, float]:
    z = 1.96
    proportion = numerator / denominator
    scale = 1 + z * z / denominator
    center = (proportion + z * z / (2 * denominator)) / scale
    half = z * math.sqrt(proportion * (1 - proportion) / denominator + z * z / (4 * denominator * denominator)) / scale
    return center - half, center + half


def render_figure(path: Path, site_rows: list[dict[str, object]], site_summary: dict[str, dict[str, object]]) -> None:
    matplotlib.rcParams["svg.hashsalt"] = "oclc-app1-05"
    rows = [row for row in site_rows if row["measure_id"] == "M01"]
    values = np.array([float(row["proportion"]) for row in rows])
    lower = values - np.array([float(row["lower95"]) for row in rows])
    upper = np.array([float(row["upper95"]) for row in rows]) - values
    figure, axis = plt.subplots(figsize=(8, 5))
    positions = np.arange(len(rows))
    axis.errorbar(positions, values, yerr=np.vstack([lower, upper]), fmt="o", color="#1f49b6", ecolor="#64748b", capsize=4, linewidth=1.5)
    axis.axhline(129 / 476, color="#c2410c", linestyle="--", linewidth=1.5, label="cohort recorded-follow-up proportion")
    axis.set_xticks(positions, SITE_ORDER)
    axis.set(xlabel="Synthetic teaching site in fixed order", ylabel="Recorded scheduled follow-up proportion", ylim=(0, 0.55))
    axis.set_title("Recorded follow-up variation across synthetic teaching sites, not rankings")
    axis.grid(axis="y", color="#d1d5db", linewidth=0.6)
    axis.legend(frameon=False)
    summary = site_summary["M01"]
    figure.text(0.5, 0.01, f"Range {summary['absolute_range']}; global chi-square p = {summary['global_p_value']}. Exact evidence is in site-variation.csv.", ha="center", fontsize=8)
    figure.tight_layout(rect=(0, 0.04, 1, 1))
    figure.savefig(path, format="svg", metadata={"Date": None})
    plt.close(figure)


def build(database: Path, cohort_path: Path, expected_path: Path, target: Path) -> dict[str, object]:
    database, target = database.resolve(), target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if sha256(database) != EXPECTED_DATABASE_SHA256:
        raise ValueError("Synthea SQLite fingerprint changed")
    cohort = verify_csv(cohort_path, EXPECTED_COHORT, "Module 02 analysis cohort")
    expected = verify_csv(expected_path, EXPECTED_OUTCOMES, "Module 04 expected outcomes")
    if set(cohort["patient_id"]) != set(expected["patient_id"]):
        raise ValueError("Cohort and expected-outcome people changed")
    if not (cohort["event_indicator"].to_numpy() == expected["event_indicator"].to_numpy()).all():
        expected_map = expected.set_index("patient_id")["event_indicator"]
        if not (cohort.set_index("patient_id")["event_indicator"] == expected_map).all():
            raise ValueError("Accepted outcomes changed")
    contract = json.loads(ANALYSIS_CONTRACT.read_text(encoding="utf-8"))
    measures_frame = pd.read_csv(MEASURE_CONTRACT, dtype=str, keep_default_na=False)
    measures = measures_frame.set_index("measure_id").to_dict("index")
    if contract["analysis_id"] != "app1-clinical-variation-v1" or tuple(contract["site_order"]) != SITE_ORDER or set(measures) != {f"M{i:02d}" for i in range(1, 12)}:
        raise ValueError("Variation or measure contract changed")

    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    connection.execute("PRAGMA query_only = ON")
    try:
        encounters = source_records(connection, cohort, "encounters", "start", "encounterclass, description")
        medications = source_records(connection, cohort, "medications", "start", "description")
        procedures = source_records(connection, cohort, "procedures", "date", "description")
        careplans = source_records(connection, cohort, "careplans", "start", "description")
    finally:
        connection.close()

    early_encounters = encounters[(encounters["days_from_discharge"] > 0) & (encounters["days_from_discharge"] <= 30)]
    post_encounters = encounters[(encounters["days_from_discharge"] > 30) & (encounters["days_from_discharge"] <= 365)].copy()
    early_procedures = procedures[(procedures["days_from_discharge"] > 0) & (procedures["days_from_discharge"] <= 30)]
    post_procedures = procedures[(procedures["days_from_discharge"] > 30) & (procedures["days_from_discharge"] <= 365)].copy()
    post_medications = medications[(medications["days_from_discharge"] > 30) & (medications["days_from_discharge"] <= 365)].copy()
    post_careplans = careplans[(careplans["days_from_discharge"] > 30) & (careplans["days_from_discharge"] <= 365)].copy()
    ids = pd.Index(sorted(cohort["patient_id"]), name="patient_id")

    base = cohort.set_index("patient_id").loc[ids, ["index_encounter_class", "age_at_index", "landmark_exposure", "teaching_site_id", "baseline_risk_tier", "event_indicator"]].copy()
    base["expected_probability"] = expected.set_index("patient_id").loc[ids, "expected_probability"].astype(float)
    scheduled_post = post_encounters[post_encounters["encounterclass"].isin(SCHEDULED_CLASSES)]
    acute_post = post_encounters[post_encounters["encounterclass"].isin(ACUTE_CLASSES)]
    medrec_early = early_procedures[early_procedures["description"] == "Medication Reconciliation (procedure)"]
    medrec_post = post_procedures[post_procedures["description"] == "Medication Reconciliation (procedure)"]
    base["medication_reconciliation_0_30_flag"] = (counts_by_person(medrec_early, ids) > 0).astype(int)
    base["scheduled_continuity_31_90_flag"] = (counts_by_person(scheduled_post[scheduled_post["days_from_discharge"] <= 90], ids) > 0).astype(int)
    base["scheduled_any_31_365_flag"] = (counts_by_person(scheduled_post, ids) > 0).astype(int)
    base["medication_record_31_365_flag"] = (counts_by_person(post_medications, ids) > 0).astype(int)
    base["medication_reconciliation_31_365_flag"] = (counts_by_person(medrec_post, ids) > 0).astype(int)
    base["procedure_record_31_365_flag"] = (counts_by_person(post_procedures, ids) > 0).astype(int)
    base["total_encounter_count_31_365"] = counts_by_person(post_encounters, ids)
    base["scheduled_encounter_count_31_365"] = counts_by_person(scheduled_post, ids)
    base["acute_encounter_count_31_365"] = counts_by_person(acute_post, ids)
    base["medication_record_count_31_365"] = counts_by_person(post_medications, ids)
    base["medication_reconciliation_count_31_365"] = counts_by_person(medrec_post, ids)
    base["procedure_record_count_31_365"] = counts_by_person(post_procedures, ids)
    base["careplan_record_count_31_365"] = counts_by_person(post_careplans, ids)
    for window_id, start, end, _ in WINDOWS:
        records = scheduled_post[(scheduled_post["days_from_discharge"] > start) & (scheduled_post["days_from_discharge"] <= end)]
        base[f"scheduled_count_{window_id}"] = counts_by_person(records, ids)
    base["post_landmark_person_days"] = 335
    base = base.reset_index()

    checks = {
        "people": len(base), "unique_people": base["patient_id"].nunique(), "recorded_followup": int(base["landmark_exposure"].sum()),
        "later_acute_returns": int(base["event_indicator"].sum()), "teaching_sites": base["teaching_site_id"].nunique(),
        "sum_expected_events": fixed(float(base["expected_probability"].sum())), "post_landmark_encounters": len(post_encounters),
        "post_landmark_scheduled_encounters": len(scheduled_post), "post_landmark_acute_encounters": len(acute_post),
        "post_landmark_medication_rows": len(post_medications), "post_landmark_procedure_rows": len(post_procedures),
        "post_landmark_careplan_rows": len(post_careplans), "medication_reconciliation_rows_day_0_30": len(medrec_early),
        "people_with_medication_reconciliation_day_0_30": int(base["medication_reconciliation_0_30_flag"].sum()),
        "common_person_days": int(base["post_landmark_person_days"].min()), "database_query_only": 1,
    }
    expected_checks = {
        "people": 476, "unique_people": 476, "recorded_followup": 129, "later_acute_returns": 87, "teaching_sites": 6,
        "sum_expected_events": "86.99999984", "post_landmark_encounters": 1694, "post_landmark_scheduled_encounters": 1457,
        "post_landmark_acute_encounters": 166, "post_landmark_medication_rows": 742, "post_landmark_procedure_rows": 1832,
        "post_landmark_careplan_rows": 92, "medication_reconciliation_rows_day_0_30": 19,
        "people_with_medication_reconciliation_day_0_30": 17, "common_person_days": 335, "database_query_only": 1,
    }
    if checks != expected_checks:
        raise ValueError(f"Variation invariants changed: {checks}")

    target.mkdir(parents=True)
    write_csv(target / "analysis-checks.csv", ["check_name", "observed_value", "expected_value", "status"], [
        {"check_name": name, "observed_value": value, "expected_value": expected_checks[name], "status": "pass"} for name, value in checks.items()
    ])

    person_fields = [
        "patient_id", "index_encounter_class", "age_at_index", "landmark_exposure", "teaching_site_id", "baseline_risk_tier", "event_indicator", "expected_probability",
        "medication_reconciliation_0_30_flag", "scheduled_continuity_31_90_flag", "scheduled_any_31_365_flag", "medication_record_31_365_flag",
        "medication_reconciliation_31_365_flag", "procedure_record_31_365_flag", "total_encounter_count_31_365", "scheduled_encounter_count_31_365",
        "acute_encounter_count_31_365", "medication_record_count_31_365", "medication_reconciliation_count_31_365", "procedure_record_count_31_365",
        "careplan_record_count_31_365", "scheduled_count_days_31_90", "scheduled_count_days_91_180", "scheduled_count_days_181_365", "post_landmark_person_days", "claim_boundary",
    ]
    person_rows = []
    for row in base.to_dict("records"):
        output = {field: row[field] for field in person_fields if field != "claim_boundary"}
        output["expected_probability"] = fixed(float(row["expected_probability"]))
        output["claim_boundary"] = "synthetic recorded-care pattern; not adherence causation quality fairness or real utilization"
        person_rows.append(output)
    write_csv(target / "care-patterns.csv", person_fields, person_rows)

    measure_summary = []
    summary_specs = (
        ("M01", int(base["landmark_exposure"].sum()), 476),
        ("M02", int(base["scheduled_continuity_31_90_flag"].sum()), 476),
        ("M03", int(base["scheduled_any_31_365_flag"].sum()), 476),
        ("M04", int(base["medication_record_31_365_flag"].sum()), 476),
        ("M05", int(base["medication_reconciliation_31_365_flag"].sum()), 476),
        ("M06", int(base["procedure_record_31_365_flag"].sum()), 476),
        ("M10", int(base["event_indicator"].sum()), 476),
        ("M11", int(base.loc[base["landmark_exposure"] == 1, "medication_reconciliation_0_30_flag"].sum()), 129),
    )
    for measure_id, numerator, denominator in summary_specs:
        measure_summary.append({
            "measure_id": measure_id, "measure": measures[measure_id]["label"], "numerator": numerator, "denominator": denominator,
            "proportion": fixed(numerator / denominator), "denominator_definition": measures[measure_id]["denominator"], "claim_limit": measures[measure_id]["claim_limit"],
        })
    write_csv(target / "measure-summary.csv", list(measure_summary[0]), measure_summary)

    exposure_rows = difference_rows(base, "landmark_exposure", 1, 0, measures)
    for row in exposure_rows:
        row["group_one"] = "scheduled_followup"
        row["group_zero"] = "no_recorded_followup"
    write_csv(target / "exposure-variation.csv", list(exposure_rows[0]), exposure_rows)
    subgroup_rows = difference_rows(base, "index_encounter_class", "inpatient", "emergency", measures)
    write_csv(target / "clinical-subgroup-variation.csv", list(subgroup_rows[0]), subgroup_rows)

    site_rows: list[dict[str, object]] = []
    for measure_id, field in SITE_MEASURES:
        for site in SITE_ORDER:
            group = base[base["teaching_site_id"] == site]
            numerator, denominator = int(group[field].sum()), len(group)
            lower, upper = wilson_interval(numerator, denominator)
            supported = denominator >= 50 and numerator >= 10 and denominator - numerator >= 10
            site_rows.append({
                "measure_id": measure_id, "measure": measures[measure_id]["label"], "teaching_site_id": site,
                "people": denominator, "numerator": numerator, "proportion": fixed(numerator / denominator),
                "lower95": fixed(lower), "upper95": fixed(upper), "support_status": "report with caution" if supported else "suppress",
                "known_direct_site_effect": 0, "site_field_class": "synthetic_extension",
                "claim_limit": "fixed-order synthetic description; not facility rank quality cause or real performance",
            })
    write_csv(target / "site-variation.csv", list(site_rows[0]), site_rows)

    site_summary_rows: list[dict[str, object]] = []
    site_summary_map: dict[str, dict[str, object]] = {}
    for measure_id, _ in SITE_MEASURES:
        rows = [row for row in site_rows if row["measure_id"] == measure_id]
        proportions = [float(row["proportion"]) for row in rows]
        table = [[int(row["numerator"]), int(row["people"]) - int(row["numerator"])] for row in rows]
        chi = chi2_contingency(table, correction=False)
        minimum, maximum = min(proportions), max(proportions)
        min_site = rows[proportions.index(minimum)]["teaching_site_id"]
        max_site = rows[proportions.index(maximum)]["teaching_site_id"]
        threshold = float(measures[measure_id]["operational_threshold"])
        summary = {
            "measure_id": measure_id, "measure": measures[measure_id]["label"], "minimum_site": min_site,
            "minimum_proportion": fixed(minimum), "maximum_site": max_site, "maximum_proportion": fixed(maximum),
            "absolute_range": fixed(maximum - minimum), "operational_threshold": fixed(threshold),
            "threshold_met": "yes" if maximum - minimum >= threshold else "no", "global_chi_square": fixed(float(chi.statistic)),
            "global_degrees_freedom": int(chi.dof), "global_p_value": fixed(float(chi.pvalue)),
            "sites_report_with_caution": sum(row["support_status"] == "report with caution" for row in rows),
            "sites_suppressed": sum(row["support_status"] == "suppress" for row in rows),
            "interpretation": "operational range and global statistical evidence are separate; synthetic sites are not rankings",
        }
        site_summary_rows.append(summary)
        site_summary_map[measure_id] = summary
    write_csv(target / "site-summary.csv", list(site_summary_rows[0]), site_summary_rows)

    time_rows: list[dict[str, object]] = []
    for exposure, exposure_label in ((1, "scheduled_followup"), (0, "no_recorded_followup")):
        group_ids = set(base.loc[base["landmark_exposure"] == exposure, "patient_id"])
        for window_id, start, end, days in WINDOWS:
            records = post_encounters[(post_encounters["patient"].isin(group_ids)) & (post_encounters["days_from_discharge"] > start) & (post_encounters["days_from_discharge"] <= end)]
            scheduled = records[records["encounterclass"].isin(SCHEDULED_CLASSES)]
            acute = records[records["encounterclass"].isin(ACUTE_CLASSES)]
            people, person_days = len(group_ids), len(group_ids) * days
            time_rows.append({
                "exposure_group": exposure_label, "window": window_id, "window_days": days, "people": people, "person_days": person_days,
                "people_with_scheduled_record": scheduled["patient"].nunique(), "scheduled_records": len(scheduled),
                "scheduled_records_per_1000_person_days": fixed(1000 * len(scheduled) / person_days), "all_encounter_records": len(records),
                "all_records_per_1000_person_days": fixed(1000 * len(records) / person_days), "acute_records": len(acute),
                "acute_records_per_1000_person_days": fixed(1000 * len(acute) / person_days),
                "claim_limit": "synthetic source-record rate; not real utilization need access quality overuse or underuse",
            })
    write_csv(target / "time-variation.csv", list(time_rows[0]), time_rows)

    record_mix: list[dict[str, object]] = []
    for record_type, records in (("medication", post_medications), ("procedure", post_procedures)):
        for group_name, group_ids in (("all", set(ids)), ("scheduled_followup", set(base.loc[base["landmark_exposure"] == 1, "patient_id"])), ("no_recorded_followup", set(base.loc[base["landmark_exposure"] == 0, "patient_id"]))):
            counts = records[records["patient"].isin(group_ids)].groupby("description").size().reset_index(name="record_count")
            counts = counts.sort_values(["record_count", "description"], ascending=[False, True], kind="mergesort").head(5)
            for rank, row in enumerate(counts.to_dict("records"), start=1):
                record_mix.append({
                    "record_type": record_type, "exposure_group": group_name, "rank": rank, "description": row["description"],
                    "record_count": int(row["record_count"]), "people": records[(records["patient"].isin(group_ids)) & (records["description"] == row["description"])]["patient"].nunique(),
                    "claim_limit": "record composition can reflect clinical need and simulation pathways; not quality or effect",
                })
    write_csv(target / "record-mix.csv", list(record_mix[0]), record_mix)
    render_figure(target / "variation-figure.svg", site_rows, site_summary_map)

    report = {
        "module": "oclc-app1-05", "module_version": "0.1.0", "commons_release": "0.53.0", "analysis_id": contract["analysis_id"],
        "sources": {
            "database_sha256": EXPECTED_DATABASE_SHA256, "database_access": "read-only", "analysis_cohort_sha256": EXPECTED_COHORT["sha256"],
            "expected_outcomes_sha256": EXPECTED_OUTCOMES["sha256"], "source_rows_post_landmark": {
                "encounters": len(post_encounters), "medications": len(post_medications), "procedures": len(post_procedures), "careplans": len(post_careplans),
            },
        },
        "cohort": {"people": 476, "recorded_followup": 129, "later_acute_returns": 87, "sites": 6, "post_landmark_person_days_each": 335},
        "reference_findings": {
            "medication_reconciliation_people_day_0_30_among_recorded_followup": 17,
            "medication_reconciliation_denominator_recorded_followup": 129,
            "site_recorded_followup_range": site_summary_map["M01"]["absolute_range"],
            "site_recorded_followup_global_p": site_summary_map["M01"]["global_p_value"],
            "site_recorded_followup_threshold_met": site_summary_map["M01"]["threshold_met"],
            "known_direct_site_effect": 0,
        },
        "methods": {"randomness": "none", "difference_interval": contract["statistics"]["difference_interval"], "site_global_test": contract["statistics"]["site_global_test"]},
        "software": {"python": "3.12", "pandas": pd.__version__, "numpy": np.__version__, "scipy": scipy.__version__, "matplotlib": matplotlib.__version__, "sqlite": sqlite3.sqlite_version},
        "outputs": list(OUTPUT_FILES),
        "claim_boundary": "synthetic recorded-care variation only; not adherence causation quality fairness ranking or deployment",
    }
    (target / "build-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    return report


def self_check(database: Path, cohort: Path, expected: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="app1-module05-build-") as temp_dir:
        root = Path(temp_dir)
        first, second = root / "first", root / "second"
        build(database, cohort, expected, first)
        build(database, cohort, expected, second)
        assert {path.name: sha256(path) for path in first.iterdir()} == {path.name: sha256(path) for path in second.iterdir()}
        assert len(list(first.iterdir())) == len(OUTPUT_FILES)
        try:
            build(database, cohort, expected, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder overwrote an existing target")
    print("APP-1 Module 05 builder self-check passed: two deterministic eleven-output builds match.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", required=True, type=Path)
    parser.add_argument("--cohort", type=Path, default=DEFAULT_COHORT)
    parser.add_argument("--expected", type=Path, default=DEFAULT_EXPECTED)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check(args.database, args.cohort, args.expected)
        elif args.target:
            print(json.dumps(build(args.database, args.cohort, args.expected, args.target), indent=2))
        else:
            parser.error("--target is required unless --self-check is used")
    except (OSError, ValueError, sqlite3.Error) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
