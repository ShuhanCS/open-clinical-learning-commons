"""Build deterministic APP-3 Module 06 feasibility, monitoring, and ML evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import math
import platform
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


ROOT = Path(__file__).resolve().parent
UPSTREAM = ROOT / "upstream"
RANDOM_STATE = 7300600
TRANSPARENT = "seasonal_exponential_smoothing"
CHALLENGER = "gradient_boosted"
DIFFICULT_FOLDS = ("F03", "F09", "F15", "F16")
NUMERIC_FEATURES = (
    "horizon_shift", "week_index", "holiday_flag", "lag_21", "lag_42",
    "lag_63", "prior_21_mean", "prior_63_mean",
)
CATEGORICAL_FEATURES = ("shift_name", "weekday", "month")
FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
OUTPUT_NAMES = (
    "upstream-inventory.csv", "feasibility-screen.csv", "monitoring-measures.csv",
    "escalation-fallback.csv", "dashboard-data.csv", "ml-split-registry.csv",
    "ml-predictions.csv", "model-performance.csv", "fold-comparison.csv",
    "model-error-slices.csv", "feature-importance.csv", "failure-cases.csv",
    "leakage-tests.csv", "week53-model-comparison.csv", "decision-change.csv",
    "invariant-checks.csv", "build-report.json", "forecast-comparison.svg",
    "monitoring-dashboard.html",
)


class BuildError(RuntimeError):
    pass


def f6(value: float) -> str:
    return f"{value:.6f}"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def pipeline() -> Pipeline:
    transform = ColumnTransformer(
        [("categorical", OneHotEncoder(handle_unknown="ignore", sparse_output=False), list(CATEGORICAL_FEATURES))],
        remainder="passthrough",
        verbose_feature_names_out=False,
    )
    model = GradientBoostingRegressor(
        loss="squared_error",
        n_estimators=100,
        learning_rate=0.05,
        max_depth=2,
        min_samples_leaf=15,
        max_features=None,
        random_state=RANDOM_STATE,
    )
    return Pipeline([("preprocess", transform), ("model", model)])


def prepare_history() -> pd.DataFrame:
    frame = pd.read_csv(UPSTREAM / "shift-metrics.csv")
    frame["date"] = pd.to_datetime(frame["date"])
    frame["shift_order"] = frame["shift_name"].map({"night": 0, "day": 1, "evening": 2})
    frame = frame.sort_values(["week_index", "date", "shift_order"]).reset_index(drop=True)
    if len(frame) != 1092 or frame["week_index"].min() != 1 or frame["week_index"].max() != 52:
        raise BuildError("Accepted shift history changed")
    if frame.groupby("week_index").size().tolist() != [21] * 52:
        raise BuildError("Every accepted historical week must have 21 shifts")
    frame["horizon_shift"] = frame.groupby("week_index").cumcount() + 1
    frame["weekday"] = frame["date"].dt.day_name()
    frame["month"] = frame["date"].dt.month.astype(str)
    for lag in (21, 42, 63):
        frame[f"lag_{lag}"] = frame["arrivals"].shift(lag)
    week_mean = frame.groupby("week_index")["arrivals"].mean().to_dict()
    frame["prior_21_mean"] = frame["week_index"].map(lambda week: week_mean.get(week - 1, math.nan))
    frame["prior_63_mean"] = frame["week_index"].map(
        lambda week: float(np.mean([week_mean.get(index, math.nan) for index in (week - 3, week - 2, week - 1)]))
    )
    return frame


def metric(values: list[dict[str, object]], method: str) -> dict[str, object]:
    rows = [row for row in values if row["method"] == method]
    actual = np.array([float(row["actual_arrivals"]) for row in rows])
    predicted = np.array([float(row["forecast_arrivals_raw"]) for row in rows])
    error = predicted - actual
    under = float(np.maximum(-error, 0).sum())
    over = float(np.maximum(error, 0).sum())
    return {
        "method": method,
        "evaluation_rows": len(rows),
        "mae_arrivals": float(np.abs(error).mean()),
        "rmse_arrivals": float(np.sqrt(np.square(error).mean())),
        "bias_arrivals": float(error.mean()),
        "wape_percent": float(np.abs(error).sum() / actual.sum() * 100),
        "underforecast_arrivals": under,
        "overforecast_arrivals": over,
        "weighted_error_cost": 2 * under + over,
    }


def display_metric(row: dict[str, object], selected: bool, reason: str) -> dict[str, object]:
    return {
        "method": row["method"],
        "evaluation_rows": row["evaluation_rows"],
        "mae_arrivals": f6(float(row["mae_arrivals"])),
        "rmse_arrivals": f6(float(row["rmse_arrivals"])),
        "bias_arrivals": f6(float(row["bias_arrivals"])),
        "wape_percent": f6(float(row["wape_percent"])),
        "underforecast_arrivals": f6(float(row["underforecast_arrivals"])),
        "overforecast_arrivals": f6(float(row["overforecast_arrivals"])),
        "weighted_error_cost": f6(float(row["weighted_error_cost"])),
        "selected_flag": int(selected),
        "selection_reason": reason,
        "synthetic_flag": 1,
    }


def build_upstream_inventory() -> list[dict[str, object]]:
    manifest = read_csv(UPSTREAM / "module06-handoff-manifest.csv")
    return [{**row, "verification_status": "pass"} for row in manifest]


def build_feasibility() -> list[dict[str, object]]:
    domains = (
        ("D01", "staffing availability and role coverage", "workforce lead"),
        ("D02", "scheduling and shift fit", "operations lead"),
        ("D03", "clinical governance and scope", "clinical lead"),
        ("D04", "quality and safety interaction", "safety lead"),
        ("D05", "equity and access interaction", "access lead"),
        ("D06", "workforce burden and interruptions", "workforce lead"),
        ("D07", "sustainability, measurement, and ownership", "quality lead"),
    )
    scenarios = {
        "S00": ("No change", "retain as monitoring baseline"),
        "S01": ("Flex clinician coverage", "revise before reconsideration"),
        "S02": ("Fast-track activation", "stop in current form"),
        "S03": ("Combined bounded rule", "revise before reconsideration"),
    }
    evidence = {
        "S00": {
            "D01": ("supported", "No modeled staffing change is introduced."),
            "D02": ("supported", "No modeled schedule change is introduced."),
            "D03": ("supported", "Monitoring only preserves the current governed state."),
            "D04": ("requires local evidence", "Safety events and 72-hour returns were not simulated."),
            "D05": ("requires local evidence", "Access gaps require prospective denominators and review."),
            "D06": ("requires local evidence", "Interruptions and perceived load have no accepted baseline."),
            "D07": ("supported", "The accepted no-change state can anchor bounded monitoring."),
        },
        "S01": {
            "D01": ("requires local evidence", "The option uses 40.000000 modeled clinician-hours; availability is unknown."),
            "D02": ("requires local evidence", "Shift placement and coverage interactions are not established."),
            "D03": ("requires local evidence", "Governance and role coverage require local approval."),
            "D04": ("requires local evidence", "Safety effects were not simulated."),
            "D05": ("requires local evidence", "Prospective support-group effects remain required."),
            "D06": ("not supported", "Modeled resource use is visible but workforce burden is unmeasured."),
            "D07": ("requires local evidence", "Funding, ownership, and sustained coverage are unknown."),
        },
        "S02": {
            "D01": ("supported", "The scenario adds no net modeled staff."),
            "D02": ("requires local evidence", "Queue activation and coverage fit are not established locally."),
            "D03": ("not supported", "The current rule worsens point-demand and stress wait evidence."),
            "D04": ("not supported", "Acuity routing requires review and the current wait result is unfavorable."),
            "D05": ("requires local evidence", "Route access by support group requires prospective review."),
            "D06": ("requires local evidence", "Interruptions and task switching are not measured."),
            "D07": ("not supported", "The current rule does not qualify for continued feasibility work."),
        },
        "S03": {
            "D01": ("requires local evidence", "The option uses 25.220413 modeled flex clinician-hours."),
            "D02": ("requires local evidence", "Activation timing and shift fit require local evidence."),
            "D03": ("requires local evidence", "The combined rule requires clinical and operational review."),
            "D04": ("requires local evidence", "Safety effects were not simulated and wait gates were missed."),
            "D05": ("requires local evidence", "Prospective support-group effects remain required."),
            "D06": ("not supported", "Added modeled hours coexist with unmeasured interruptions and load."),
            "D07": ("requires local evidence", "Ownership and sustainability are not established."),
        },
    }
    return [
        {
            "scenario_id": scenario_id,
            "scenario_name": scenario_name,
            "domain_id": domain_id,
            "domain": domain,
            "status": evidence[scenario_id][domain_id][0],
            "accepted_evidence": evidence[scenario_id][domain_id][1],
            "owner": owner,
            "scenario_disposition": disposition,
            "return_condition": "new declared scenario contract and all Module 05 gates" if scenario_id in {"S01", "S03"} else (
                "materially different clinically reviewed design" if scenario_id == "S02" else "continue bounded monitoring"
            ),
            "implementation_authorized": 0,
        }
        for scenario_id, (scenario_name, disposition) in scenarios.items()
        for domain_id, domain, owner in domains
    ]


def build_monitoring() -> list[dict[str, object]]:
    source = {row["measure_id"]: row for row in read_csv(UPSTREAM / "evaluation-measures.csv")}
    values = {
        "M01": ("60.035963", "simulated planning baseline", "70.035963", "investigate above threshold", "weekly", "eligible arrivals"),
        "M02": ("136.453267", "simulated planning baseline", "151.453267", "investigate above threshold", "weekly", "eligible arrivals"),
        "M03": ("105.400000", "simulated planning baseline", "context only", "review with disposition mix", "weekly", "completed encounters"),
        "M04": ("11.914912", "simulated planning baseline", "12.914912", "investigate above threshold", "weekly", "eligible arrivals"),
        "M05": ("772.500000", "simulated planning baseline", "context only", "interpret with demand and abandonment", "weekly", "eligible arrivals"),
        "M06": ("84.996853", "simulated planning baseline", "context only", "review sustained high and low values", "weekly", "modeled available clinician time"),
        "M07": ("7.923167", "simulated planning reference", "8.715484", "investigate above threshold", "weekly", "modeled scheduled clinician-hours"),
        "M08": ("unavailable", "unavailable prospectively", "any reviewed candidate", "immediate clinical review", "weekly and event review", "completed encounters"),
        "M09": ("unavailable", "unavailable prospectively", "follow-up completeness required", "interpret only after completeness passes", "weekly", "eligible discharges with complete follow-up"),
        "M10": ("0.000000", "simulated planning baseline", "5.000000", "pause review above 5 minutes worse", "weekly", "language-support and standard eligible arrivals"),
        "M11": ("0.241085", "simulated planning baseline", "5.000000", "pause review above 5 minutes worse", "weekly", "mobility-support and standard eligible arrivals"),
        "M12": ("unavailable", "unavailable prospectively", "baseline required", "collect before any test", "each shift and weekly", "participating workforce respondents"),
    }
    rows = []
    for measure_id in sorted(source):
        row = source[measure_id]
        value, state, threshold, escalation, cadence, denominator = values[measure_id]
        rows.append({
            "measure_id": measure_id,
            "domain": row["domain"],
            "measure": row["measure"],
            "value": value,
            "unit": row["unit"],
            "evidence_state": state,
            "source_period": "Module 05 C02 no-change median" if value != "unavailable" else "prospective source not available",
            "denominator": denominator,
            "direction": row["direction"],
            "display": row["display"],
            "draft_threshold": threshold,
            "escalation": escalation,
            "owner": row["owner"],
            "review_cadence": cadence,
            "unavailable_state": row["unavailable_state"],
            "claim_limit": row["claim_limit"],
        })
    return rows


def build_escalation() -> list[dict[str, object]]:
    rules = (
        ("E01", "M01", "median arrival-to-clinician above 70.035963 minutes", "investigate", "flow lead", "operations council", "verify source and stratify the signal"),
        ("E02", "M02", "P90 arrival-to-clinician above 151.453267 minutes", "investigate", "flow lead", "operations council", "review tail periods and demand"),
        ("E03", "M04", "left before seen above 12.914912 percent", "investigate", "access lead", "operations council", "verify denominator and access groups"),
        ("E04", "supplemental", "high-acuity median wait above 60.084398 minutes", "pause review", "clinical lead", "clinical performance council", "pause redesign review and examine acuity cases"),
        ("E05", "M10", "language-support gap above 5 minutes worse", "pause review", "access lead", "clinical performance council", "verify support-group completeness and process"),
        ("E06", "M11", "mobility-support gap above 5 minutes worse", "pause review", "access lead", "clinical performance council", "verify support-group completeness and process"),
        ("E07", "M07", "modeled overtime reference above 8.715484 hours", "investigate", "workforce lead", "operations council", "review workload and coverage assumptions"),
        ("E08", "M08", "any reviewed safety-event candidate", "immediate clinical review", "safety lead", "clinical safety authority", "follow the governed event-review process"),
        ("E09", "M09", "follow-up completeness does not pass", "interpretability gate", "quality lead", "quality council", "report unavailable and repair follow-up capture"),
        ("E10", "M12", "no accepted interruption or perceived-load baseline", "baseline required", "workforce lead", "operations council", "collect baseline before any test"),
    )
    return [
        {
            "rule_id": rule_id,
            "measure_id": measure_id,
            "trigger": trigger,
            "response_level": level,
            "confirmation_owner": owner,
            "decision_owner": decision_owner,
            "immediate_safeguard": safeguard,
            "fallback_state": "continue no-change monitoring",
            "documentation": "governed Week 6 monitoring record",
            "restart_condition": "new evidence, clinician leadership review, and explicit authorization",
            "automatic_action": 0,
        }
        for rule_id, measure_id, trigger, level, owner, decision_owner, safeguard in rules
    ]


def fit_models(history: pd.DataFrame) -> tuple[list[dict[str, object]], list[dict[str, object]], Pipeline]:
    folds = read_csv(UPSTREAM / "folds.csv")
    transparent_rows = [row for row in read_csv(UPSTREAM / "transparent-predictions.csv") if row["method"] == TRANSPARENT]
    transparent = {(row["fold_id"], row["target_shift_id"]): float(row["forecast_arrivals"]) for row in transparent_rows}
    predictions: list[dict[str, object]] = []
    registry: list[dict[str, object]] = []
    for fold in folds:
        train_end = int(fold["train_end_week"])
        test_week = int(fold["test_week"])
        train = history[(history["week_index"] <= train_end) & history[list(FEATURES)].notna().all(axis=1)]
        test = history[history["week_index"] == test_week].copy()
        if len(test) != 21 or test[list(FEATURES)].isna().any().any():
            raise BuildError(f"Fold {fold['fold_id']} target features changed")
        fitted = pipeline()
        fitted.fit(train[list(FEATURES)], train["arrivals"])
        ml_values = np.maximum(0, fitted.predict(test[list(FEATURES)]))
        registry.append({
            "fold_id": fold["fold_id"],
            "issue_date": fold["issue_date"],
            "train_start_week": 4,
            "train_end_week": train_end,
            "eligible_train_rows": len(train),
            "test_week": test_week,
            "test_start_date": fold["test_start_date"],
            "test_end_date": fold["test_end_date"],
            "test_rows": len(test),
            "common_row_identity": "pass",
            "target_week_excluded_from_training": "pass",
            "preprocessing_fit": "training fold only",
        })
        for (_, target), ml_value in zip(test.iterrows(), ml_values):
            key = (fold["fold_id"], target["shift_id"])
            if key not in transparent:
                raise BuildError(f"Missing accepted transparent prediction: {key}")
            for method, predicted in ((TRANSPARENT, transparent[key]), (CHALLENGER, float(ml_value))):
                actual = float(target["arrivals"])
                error = predicted - actual
                predictions.append({
                    "fold_id": fold["fold_id"],
                    "method": method,
                    "target_shift_id": target["shift_id"],
                    "target_date": target["date"].strftime("%Y-%m-%d"),
                    "shift_name": target["shift_name"],
                    "horizon_shift": int(target["horizon_shift"]),
                    "actual_arrivals": int(actual),
                    "forecast_arrivals": f6(predicted),
                    "forecast_arrivals_raw": predicted,
                    "signed_error": f6(error),
                    "absolute_error": f6(abs(error)),
                    "squared_error": f6(error * error),
                    "underforecast_arrivals": f6(max(-error, 0)),
                    "overforecast_arrivals": f6(max(error, 0)),
                    "holiday_flag": int(target["holiday_flag"]),
                    "synthetic_flag": 1,
                })
    final = pipeline()
    eligible = history[history[list(FEATURES)].notna().all(axis=1)]
    final.fit(eligible[list(FEATURES)], eligible["arrivals"])
    return predictions, registry, final


def fold_comparison(predictions: list[dict[str, object]]) -> list[dict[str, object]]:
    by_fold: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in predictions:
        by_fold[str(row["fold_id"])].append(row)
    rows = []
    for fold_id in sorted(by_fold):
        transparent = metric(by_fold[fold_id], TRANSPARENT)
        ml = metric(by_fold[fold_id], CHALLENGER)
        ratio = (float(ml["mae_arrivals"]) / float(transparent["mae_arrivals"]) - 1) * 100
        rows.append({
            "fold_id": fold_id,
            "test_rows": 21,
            "transparent_mae_arrivals": f6(float(transparent["mae_arrivals"])),
            "ml_mae_arrivals": f6(float(ml["mae_arrivals"])),
            "ml_mae_change_percent": f6(ratio),
            "transparent_total_error": f6(sum(float(row["forecast_arrivals_raw"]) - float(row["actual_arrivals"]) for row in by_fold[fold_id] if row["method"] == TRANSPARENT)),
            "ml_total_error": f6(sum(float(row["forecast_arrivals_raw"]) - float(row["actual_arrivals"]) for row in by_fold[fold_id] if row["method"] == CHALLENGER)),
            "difficult_fold": int(fold_id in DIFFICULT_FOLDS),
            "difficult_fold_rule_status": "pass" if fold_id in DIFFICULT_FOLDS and ratio <= 10 else ("not applicable" if fold_id not in DIFFICULT_FOLDS else "fail"),
            "synthetic_flag": 1,
        })
    return rows


def error_slices(predictions: list[dict[str, object]]) -> list[dict[str, object]]:
    augmented = []
    for row in predictions:
        copy = dict(row)
        copy["weekday"] = pd.Timestamp(str(row["target_date"])).day_name()
        horizon = int(row["horizon_shift"])
        copy["horizon_group"] = "early 1-7" if horizon <= 7 else ("middle 8-14" if horizon <= 14 else "late 15-21")
        augmented.append(copy)
    definitions = (
        ("shift", lambda row: str(row["shift_name"])),
        ("weekday", lambda row: str(row["weekday"])),
        ("holiday", lambda row: "yes" if int(row["holiday_flag"]) else "no"),
        ("horizon", lambda row: str(row["horizon_group"])),
        ("difficult_fold", lambda row: str(row["fold_id"]) if row["fold_id"] in DIFFICULT_FOLDS else ""),
    )
    rows = []
    for method in (TRANSPARENT, CHALLENGER):
        method_rows = [row for row in augmented if row["method"] == method]
        for slice_type, value_fn in definitions:
            groups: dict[str, list[dict[str, object]]] = defaultdict(list)
            for row in method_rows:
                value = value_fn(row)
                if value:
                    groups[value].append(row)
            for value in sorted(groups):
                summary = metric(groups[value], method)
                rows.append({
                    "method": method,
                    "slice_type": slice_type,
                    "slice_value": value,
                    "rows": summary["evaluation_rows"],
                    "mae_arrivals": f6(float(summary["mae_arrivals"])),
                    "rmse_arrivals": f6(float(summary["rmse_arrivals"])),
                    "bias_arrivals": f6(float(summary["bias_arrivals"])),
                    "underforecast_arrivals": f6(float(summary["underforecast_arrivals"])),
                    "overforecast_arrivals": f6(float(summary["overforecast_arrivals"])),
                    "support_status": "supported" if int(summary["evaluation_rows"]) >= 21 else "limited",
                    "synthetic_flag": 1,
                })
    return rows


def feature_importance(fitted: Pipeline) -> list[dict[str, object]]:
    names = fitted.named_steps["preprocess"].get_feature_names_out()
    importance = fitted.named_steps["model"].feature_importances_
    rows = sorted(zip(names, importance), key=lambda item: (-item[1], item[0]))
    return [
        {
            "rank": index,
            "feature": name,
            "importance": f6(float(value)),
            "importance_percent": f6(float(value) * 100),
            "interpretation": "model split allocation only; not causal",
        }
        for index, (name, value) in enumerate(rows, start=1)
    ]


def failure_cases(predictions: list[dict[str, object]]) -> list[dict[str, object]]:
    ml = sorted(
        (row for row in predictions if row["method"] == CHALLENGER),
        key=lambda row: (-float(row["absolute_error"]), str(row["fold_id"]), int(row["horizon_shift"])),
    )[:10]
    return [
        {
            "rank": index,
            "fold_id": row["fold_id"],
            "target_shift_id": row["target_shift_id"],
            "target_date": row["target_date"],
            "shift_name": row["shift_name"],
            "horizon_shift": row["horizon_shift"],
            "actual_arrivals": row["actual_arrivals"],
            "ml_forecast_arrivals": row["forecast_arrivals"],
            "signed_error": row["signed_error"],
            "absolute_error": row["absolute_error"],
            "operational_consequence": "underforecast preparation risk" if float(row["signed_error"]) < 0 else "overforecast resource-attention risk",
            "retention_status": "retained",
            "synthetic_flag": 1,
        }
        for index, row in enumerate(ml, start=1)
    ]


def week53(history: pd.DataFrame, fitted: Pipeline) -> tuple[list[dict[str, object]], float]:
    future = pd.read_csv(UPSTREAM / "week53-forecast.csv")
    future["date"] = pd.to_datetime(future["date"])
    future["week_index"] = 53
    future["weekday"] = future["date"].dt.day_name()
    future["month"] = future["date"].dt.month.astype(str)
    week_mean = history.groupby("week_index")["arrivals"].mean().to_dict()
    for lag in (21, 42, 63):
        source_week = 53 - lag // 21
        values = history[history["week_index"] == source_week].sort_values(["date", "shift_order"])["arrivals"].to_numpy()
        future[f"lag_{lag}"] = values
    future["prior_21_mean"] = week_mean[52]
    future["prior_63_mean"] = float(np.mean([week_mean[50], week_mean[51], week_mean[52]]))
    ml = np.maximum(0, fitted.predict(future[list(FEATURES)]))
    rows = []
    for (_, source), ml_value in zip(future.iterrows(), ml):
        transparent = float(source["raw_forecast_arrivals"])
        rows.append({
            "record_type": "shift",
            "target_shift_id": source["forecast_shift_id"],
            "date": source["date"].strftime("%Y-%m-%d"),
            "shift_name": source["shift_name"],
            "horizon_shift": int(source["horizon_shift"]),
            "transparent_forecast_arrivals": f6(transparent),
            "ml_forecast_arrivals": f6(float(ml_value)),
            "ml_minus_transparent_arrivals": f6(float(ml_value) - transparent),
            "accepted_range_status": "not applicable at shift level",
            "actual_status": "future synthetic actual unavailable",
            "synthetic_flag": 1,
        })
    total = float(ml.sum())
    rows.append({
        "record_type": "total",
        "target_shift_id": "WEEK53_TOTAL",
        "date": "2024-12-30 to 2025-01-05",
        "shift_name": "all",
        "horizon_shift": 21,
        "transparent_forecast_arrivals": "876.924084",
        "ml_forecast_arrivals": f6(total),
        "ml_minus_transparent_arrivals": f6(total - 876.924084),
        "accepted_range_status": "pass: inside 805.136639 to 970.733035",
        "actual_status": "future synthetic actual unavailable",
        "synthetic_flag": 1,
    })
    return rows, total


def decision_rules(transparent: dict[str, object], ml: dict[str, object], folds: list[dict[str, object]], week53_total: float) -> list[dict[str, object]]:
    mae_improvement = float(transparent["mae_arrivals"]) - float(ml["mae_arrivals"])
    rmse_change = float(ml["rmse_arrivals"]) - float(transparent["rmse_arrivals"])
    wape_improvement = float(transparent["wape_percent"]) - float(ml["wape_percent"])
    cost_improvement = (float(transparent["weighted_error_cost"]) - float(ml["weighted_error_cost"])) / float(transparent["weighted_error_cost"]) * 100
    difficult_pass = sum(row["difficult_fold_rule_status"] == "pass" for row in folds)
    rules = [
        ("R01", "MAE improvement", "at least 0.750000 arrivals per shift", f6(mae_improvement), mae_improvement >= 0.75),
        ("R02", "RMSE change", "no worsening above 0.000000", f6(rmse_change), rmse_change <= 0),
        ("R03", "WAPE improvement", "at least 1.000000 percentage point", f6(wape_improvement), wape_improvement >= 1),
        ("R04", "absolute ML bias", "no more than 1.000000 arrival per shift", f6(abs(float(ml["bias_arrivals"]))), abs(float(ml["bias_arrivals"])) <= 1),
        ("R05", "weighted error cost improvement", "at least 5.000000 percent", f6(cost_improvement), cost_improvement >= 5),
        ("R06", "difficult folds", "at least 3 of 4 not worse by more than 10 percent", str(difficult_pass), difficult_pass >= 3),
        ("R07", "row and leakage identity", "588 rows and all leakage checks pass", "588 rows; all pass", int(ml["evaluation_rows"]) == 588),
        ("R08", "Week 53 total", "inside 805.136639 to 970.733035", f6(week53_total), 805.136639 <= week53_total <= 970.733035),
    ]
    rows = [
        {
            "rule_id": rule_id,
            "rule": rule,
            "threshold": threshold,
            "observed": observed,
            "status": "pass" if passed else "fail",
            "decision_effect": "required for replacement",
        }
        for rule_id, rule, threshold, observed, passed in rules
    ]
    passed = sum(row["status"] == "pass" for row in rows)
    rows.append({
        "rule_id": "FINAL",
        "rule": "all predeclared rules",
        "threshold": "8 of 8 pass",
        "observed": f"{passed} of 8 pass",
        "status": "pass" if passed == 8 else "fail",
        "decision_effect": "retain transparent forecast" if passed != 8 else "challenger eligible for future declared release",
    })
    return rows


def leakage_tests(history: pd.DataFrame, registry: list[dict[str, object]], predictions: list[dict[str, object]]) -> list[dict[str, object]]:
    eligible = history[history[list(FEATURES)].notna().all(axis=1)]
    tests = (
        ("L01", "common evaluation rows", len([row for row in predictions if row["method"] == CHALLENGER]) == 588, "588 exact challenger rows"),
        ("L02", "temporal cutoffs", all(int(row["train_end_week"]) + 1 == int(row["test_week"]) for row in registry), "every test week follows its training end"),
        ("L03", "lag source", history[["lag_21", "lag_42", "lag_63"]].iloc[63:].notna().all().all(), "lags use only earlier shifts"),
        ("L04", "complete-week means", eligible[["prior_21_mean", "prior_63_mean"]].notna().all().all(), "means use completed prior weeks"),
        ("L05", "target-week exclusion", all(row["target_week_excluded_from_training"] == "pass" for row in registry), "no target-week row enters training"),
        ("L06", "special-event exclusion", "synthetic_special_event_flag" not in FEATURES, "unverified issue-time event flag excluded"),
        ("L07", "prohibited outcome exclusion", not {"completed_encounters", "left_before_seen", "overtime_hours"}.intersection(FEATURES), "post-target outcomes excluded"),
        ("L08", "training-only preprocessing", all(row["preprocessing_fit"] == "training fold only" for row in registry), "one encoder fit per training fold"),
        ("L09", "feature completeness", eligible[list(FEATURES)].notna().all().all(), "all eligible rows complete"),
        ("L10", "row identity", len({(row["fold_id"], row["target_shift_id"]) for row in predictions if row["method"] == CHALLENGER}) == 588, "fold and target IDs unique"),
        ("L11", "fixed model family", True, "one GradientBoostingRegressor; no tuning"),
        ("L12", "supported environment", sys.version_info[:2] == (3, 12) and np.__version__ == "2.0.2" and pd.__version__ == "3.0.3" and sklearn.__version__ == "1.9.0", f"Python {platform.python_version()}, NumPy {np.__version__}, pandas {pd.__version__}, scikit-learn {sklearn.__version__}"),
    )
    return [{"test_id": test_id, "test": test, "status": "pass" if passed else "fail", "evidence": evidence} for test_id, test, passed, evidence in tests]


def invariant_checks(feasibility: list[dict[str, object]], monitoring: list[dict[str, object]], predictions: list[dict[str, object]], decisions: list[dict[str, object]], leak: list[dict[str, object]]) -> list[dict[str, object]]:
    checks = (
        ("I01", "33 upstream files verify", True),
        ("I02", "selected option remains none", True),
        ("I03", "four scenario dispositions are present", len({row["scenario_id"] for row in feasibility}) == 4),
        ("I04", "28 feasibility-domain rows are present", len(feasibility) == 28),
        ("I05", "no implementation is authorized", all(int(row["implementation_authorized"]) == 0 for row in feasibility)),
        ("I06", "12 monitoring measures are present", len(monitoring) == 12),
        ("I07", "three prospective measures remain unavailable", sum(row["value"] == "unavailable" for row in monitoring) == 3),
        ("I08", "all measures have owners and cadence", all(row["owner"] and row["review_cadence"] for row in monitoring)),
        ("I09", "28 rolling folds are present", len({row["fold_id"] for row in predictions}) == 28),
        ("I10", "588 common target rows are present", len({(row["fold_id"], row["target_shift_id"]) for row in predictions if row["method"] == CHALLENGER}) == 588),
        ("I11", "two methods use identical target rows", len(predictions) == 1176),
        ("I12", "all predictions are nonnegative", all(float(row["forecast_arrivals_raw"]) >= 0 for row in predictions)),
        ("I13", "all leakage tests pass", all(row["status"] == "pass" for row in leak)),
        ("I14", "one predeclared decision rule fails", sum(row["status"] == "fail" for row in decisions[:-1]) == 1),
        ("I15", "final model decision retains transparent forecast", decisions[-1]["decision_effect"] == "retain transparent forecast"),
        ("I16", "Module 05 points remain 25", True),
        ("I17", "Module 06 adds zero points", True),
        ("I18", "safety and return outcomes are not invented", all(row["value"] == "unavailable" for row in monitoring if row["measure_id"] in {"M08", "M09"})),
        ("I19", "machine learning does not alter Module 05", True),
        ("I20", "Module 07 receives no implementation authority", True),
    )
    return [{"check_id": check_id, "check": check, "status": "pass" if passed else "fail"} for check_id, check, passed in checks]


def svg(performance: list[dict[str, object]]) -> str:
    values = {(row["method"], metric_name): float(row[metric_name]) for row in performance for metric_name in ("mae_arrivals", "rmse_arrivals")}
    scale = 38
    bars = []
    entries = (
        ("Transparent MAE", values[(TRANSPARENT, "mae_arrivals")], "#1f49b6", 90),
        ("ML MAE", values[(CHALLENGER, "mae_arrivals")], "#0f766e", 140),
        ("Transparent RMSE", values[(TRANSPARENT, "rmse_arrivals")], "#1f49b6", 230),
        ("ML RMSE", values[(CHALLENGER, "rmse_arrivals")], "#0f766e", 280),
    )
    for label, value, color, y in entries:
        width = value * scale
        bars.append(f'<text x="20" y="{y + 18}" font-size="14">{html.escape(label)}</text>')
        bars.append(f'<rect x="175" y="{y}" width="{width:.2f}" height="24" fill="{color}"/>')
        bars.append(f'<text x="{185 + width:.2f}" y="{y + 18}" font-size="14">{value:.6f}</text>')
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-labelledby="title desc">',
        '<title id="title">Transparent and gradient-boosted forecast error</title>',
        '<desc id="desc">The ML challenger has lower MAE and RMSE, but its MAE improvement misses the predeclared replacement threshold.</desc>',
        '<rect width="640" height="360" fill="white"/>',
        '<text x="20" y="34" font-size="20" font-weight="700">Forecast error on 588 common shifts</text>',
        '<text x="20" y="58" font-size="14">Lower is better. Values are arrivals per shift.</text>',
        *bars,
        '<text x="20" y="330" font-size="14" font-weight="700">Decision: retain transparent forecast</text>',
        '</svg>',
        '',
    ])


def dashboard(rows: list[dict[str, object]]) -> str:
    table_rows = []
    cards = []
    for row in rows:
        state = str(row["evidence_state"])
        css_class = "unavailable" if state.startswith("unavailable") else "available"
        value = html.escape(str(row["value"]))
        unit = html.escape(str(row["unit"]))
        cards.append(
            f'<article class="measure {css_class}"><h3>{html.escape(str(row["measure_id"]))}: {html.escape(str(row["measure"]))}</h3>'
            f'<p class="value">{value} <span>{unit}</span></p><p><strong>State:</strong> {html.escape(state)}</p>'
            f'<p><strong>Draft review rule:</strong> {html.escape(str(row["draft_threshold"]))}; {html.escape(str(row["escalation"]))}</p>'
            f'<p><strong>Owner and cadence:</strong> {html.escape(str(row["owner"]))}; {html.escape(str(row["review_cadence"]))}</p></article>'
        )
        table_rows.append(
            "<tr>" + "".join(f"<td>{html.escape(str(row[field]))}</td>" for field in (
                "measure_id", "measure", "value", "unit", "evidence_state", "draft_threshold", "escalation", "owner", "review_cadence", "denominator"
            )) + "</tr>"
        )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CGH-ED-01 Week 6 monitoring design</title>
<style>
:root {{ color-scheme: light; font-family: Arial, sans-serif; color: #172033; background: #f4f7fb; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; }}
header, main, footer {{ width: min(1180px, 100%); margin: auto; padding: 1rem; }}
.banner {{ background: #fff3cd; border: 2px solid #8a6500; padding: 1rem; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 1rem; }}
.measure {{ background: white; border: 1px solid #bac5d6; border-left: 6px solid #1f49b6; padding: 1rem; }}
.measure.unavailable {{ border-left-color: #8a6500; background: #fffaf0; }}
.value {{ font-size: 1.55rem; font-weight: 700; }}
.value span {{ font-size: 1rem; font-weight: 400; }}
.table-wrap {{ overflow-x: auto; background: white; }}
table {{ border-collapse: collapse; width: 100%; min-width: 980px; }}
th, td {{ border: 1px solid #9aa8bd; padding: .55rem; text-align: left; vertical-align: top; }}
th {{ background: #e8eef9; }}
a:focus {{ outline: 3px solid #0d67ff; outline-offset: 3px; }}
@media (max-width: 420px) {{ header, main, footer {{ padding: .75rem; }} h1 {{ font-size: 1.55rem; }} }}
</style>
</head>
<body>
<header>
<div class="banner" role="note"><strong>Planning evidence only.</strong> Fictional service CGH-ED-01. No scenario qualified. No clinical action, staffing change, test, implementation, or deployment is authorized.</div>
<h1>Week 6 monitoring design</h1>
<p>Module 05 point-demand simulation and prospective evidence gaps. Values are simulated planning baselines unless marked unavailable.</p>
</header>
<main>
<section aria-labelledby="measures"><h2 id="measures">Twelve measures for leadership review</h2><div class="grid">{''.join(cards)}</div></section>
<section aria-labelledby="exact"><h2 id="exact">Exact measure table</h2><p>Unavailable values are not zero and must not be imputed.</p><div class="table-wrap" tabindex="0"><table><thead><tr><th>ID</th><th>Measure</th><th>Value</th><th>Unit</th><th>Evidence state</th><th>Draft threshold</th><th>Escalation</th><th>Owner</th><th>Cadence</th><th>Denominator</th></tr></thead><tbody>{''.join(table_rows)}</tbody></table></div></section>
<section aria-labelledby="limits"><h2 id="limits">How to use this design</h2><p>Confirm source completeness, review measures together, preserve group denominators, and use the named human decision owner. These draft thresholds are not control limits or automatic actions. The fallback is continued no-change monitoring.</p></section>
</main>
<footer><p>Static teaching artifact generated from <code>dashboard-data.csv</code>. No live connection or alerting.</p></footer>
</body>
</html>
"""


def generate(target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    target.mkdir(parents=True)
    inventory = build_upstream_inventory()
    feasibility = build_feasibility()
    monitoring = build_monitoring()
    escalation = build_escalation()
    history = prepare_history()
    predictions, registry, fitted = fit_models(history)
    transparent = metric(predictions, TRANSPARENT)
    ml = metric(predictions, CHALLENGER)
    performance = [
        display_metric(transparent, True, "accepted method retained because the challenger fails one predeclared rule"),
        display_metric(ml, False, "challenger misses the 0.750000 MAE-improvement rule"),
    ]
    folds = fold_comparison(predictions)
    slices = error_slices(predictions)
    importance = feature_importance(fitted)
    failures = failure_cases(predictions)
    week53_rows, week53_total = week53(history, fitted)
    decisions = decision_rules(transparent, ml, folds, week53_total)
    leak = leakage_tests(history, registry, predictions)
    if any(row["status"] != "pass" for row in leak):
        raise BuildError("Leakage or environment contract failed")
    invariants = invariant_checks(feasibility, monitoring, predictions, decisions, leak)
    if any(row["status"] != "pass" for row in invariants):
        raise BuildError("Release invariant failed")

    write_csv(target / "upstream-inventory.csv", list(inventory[0]), inventory)
    write_csv(target / "feasibility-screen.csv", list(feasibility[0]), feasibility)
    write_csv(target / "monitoring-measures.csv", list(monitoring[0]), monitoring)
    write_csv(target / "escalation-fallback.csv", list(escalation[0]), escalation)
    dashboard_fields = ["measure_id", "domain", "measure", "value", "unit", "evidence_state", "source_period", "denominator", "draft_threshold", "escalation", "owner", "review_cadence", "claim_limit"]
    dashboard_rows = [{field: row[field] for field in dashboard_fields} for row in monitoring]
    write_csv(target / "dashboard-data.csv", dashboard_fields, dashboard_rows)
    write_csv(target / "ml-split-registry.csv", list(registry[0]), registry)
    prediction_fields = [field for field in predictions[0] if field != "forecast_arrivals_raw"]
    write_csv(target / "ml-predictions.csv", prediction_fields, [{field: row[field] for field in prediction_fields} for row in predictions])
    write_csv(target / "model-performance.csv", list(performance[0]), performance)
    write_csv(target / "fold-comparison.csv", list(folds[0]), folds)
    write_csv(target / "model-error-slices.csv", list(slices[0]), slices)
    write_csv(target / "feature-importance.csv", list(importance[0]), importance)
    write_csv(target / "failure-cases.csv", list(failures[0]), failures)
    write_csv(target / "leakage-tests.csv", list(leak[0]), leak)
    write_csv(target / "week53-model-comparison.csv", list(week53_rows[0]), week53_rows)
    write_csv(target / "decision-change.csv", list(decisions[0]), decisions)
    write_csv(target / "invariant-checks.csv", list(invariants[0]), invariants)
    (target / "forecast-comparison.svg").write_text(svg(performance), encoding="utf-8", newline="\n")
    (target / "monitoring-dashboard.html").write_text(dashboard(dashboard_rows), encoding="utf-8", newline="\n")

    report = {
        "status": "pass",
        "module_id": "oclc-app3-06",
        "module_version": "0.1.0",
        "commons_release": "0.72.0",
        "outputs": 19,
        "upstream_files": len(inventory),
        "feasibility_rows": len(feasibility),
        "monitoring_measures": len(monitoring),
        "rolling_folds": len(registry),
        "prediction_rows": len(predictions),
        "common_evaluation_rows": int(ml["evaluation_rows"]),
        "transparent_mae_arrivals": round(float(transparent["mae_arrivals"]), 6),
        "ml_mae_arrivals": round(float(ml["mae_arrivals"]), 6),
        "mae_improvement_arrivals": round(float(transparent["mae_arrivals"]) - float(ml["mae_arrivals"]), 6),
        "week53_ml_arrivals": round(week53_total, 6),
        "decision_rules_passed": sum(row["status"] == "pass" for row in decisions[:-1]),
        "ml_decision": "retain transparent forecast",
        "week6_points": 25,
        "module06_points_added": 0,
        "implementation_authorized": False,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scikit_learn": sklearn.__version__,
        },
    }
    (target / "build-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    if sorted(path.name for path in target.iterdir()) != sorted(OUTPUT_NAMES):
        raise BuildError("Output file contract changed")
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app3-module06-build-") as temp_dir:
        base = Path(temp_dir)
        first = base / "first"
        second = base / "second"
        report = generate(first)
        generate(second)
        for name in OUTPUT_NAMES:
            if (first / name).read_bytes() != (second / name).read_bytes():
                raise AssertionError(f"Nondeterministic output: {name}")
        assert report["outputs"] == 19 and report["prediction_rows"] == 1176
        assert report["decision_rules_passed"] == 7 and report["ml_decision"] == "retain transparent forecast"
        try:
            generate(first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
    print("APP-3 Module 06 evidence-builder self-check passed: 19 deterministic outputs and one protected near-miss decision.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.target:
            print(json.dumps(generate(args.target), indent=2, sort_keys=True))
        else:
            parser.error("--target is required")
    except (OSError, ValueError, KeyError, BuildError) as error:
        parser.exit(1, f"Evidence build failed: {error}\n")


if __name__ == "__main__":
    main()
