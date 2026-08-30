"""Build the exact FND-2 Module 03 prediction-evaluation release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, brier_score_loss, confusion_matrix, log_loss, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


MODULE_ROOT = Path(__file__).resolve().parent
SEED = 20260830
BOOTSTRAPS = 2000
UPSTREAM = {
    "modeling-cohort.csv": (138_503, "6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332"),
    "split-registry.csv": (51_910, "05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1"),
    "baseline-metrics.csv": (306, "613651013e397beeadc84b17482026ca7cb4674abf61bf521699d79af0a3c9af"),
    "feature-role-contract.csv": (3_766, "599f29ca612cb5f23aed277c56937af78c488ba952c2926faa94166f33449c83"),
    "formula-registry.csv": (771, "fc69d6146eec729969b571b535c13027e9b875d34dd99637f0dc0d9b934239a6"),
    "model-matrix-fields.csv": (1_535, "7a91e166796ae1030518da95e49f6a19ecc687d7cf5784f76718509c0abc9c38"),
    "assumption-register.csv": (2_181, "7c6322667a383458a34aea49b687d1a6716aaaf0f780ccf060f1c99d671956e3"),
}
LOG_FEATURES = ["age_centered_decade", "prior_365d_acute_count", "index_class_inpatient"]
NUMERIC_FEATURES = ["age_at_index", "prior_365d_encounter_count", "prior_365d_acute_count", "prior_365d_condition_count", "prior_365d_medication_count"]
CATEGORICAL_FEATURES = ["gender", "race", "ethnicity", "index_class"]
LEAKED_FEATURES = ["next_30d_state", "endpoint_90d"]
PORTABLE_FILES = ("requirements.txt", "data-spec.md", "source-record.yml", "assessment.md", "model-contract.json")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def upstream_root() -> Path:
    local = MODULE_ROOT / "data"
    if all((local / name).is_file() for name in UPSTREAM):
        return local
    return MODULE_ROOT.parent


def upstream_paths(root: Path | None = None) -> dict[str, Path]:
    base = root or upstream_root()
    local = base.name == "data"
    return {
        "modeling-cohort.csv": base / "modeling-cohort.csv" if local else base / "01-aims-reproducible-workspace" / "outputs" / "modeling-cohort.csv",
        "split-registry.csv": base / "split-registry.csv" if local else base / "01-aims-reproducible-workspace" / "outputs" / "split-registry.csv",
        "baseline-metrics.csv": base / "baseline-metrics.csv" if local else base / "01-aims-reproducible-workspace" / "outputs" / "baseline-metrics.csv",
        "feature-role-contract.csv": base / "feature-role-contract.csv" if local else base / "01-aims-reproducible-workspace" / "feature-role-contract.csv",
        "formula-registry.csv": base / "formula-registry.csv" if local else base / "02-regression-interpretation" / "formula-registry.csv",
        "model-matrix-fields.csv": base / "model-matrix-fields.csv" if local else base / "02-regression-interpretation" / "outputs" / "model-matrix-fields.csv",
        "assumption-register.csv": base / "assumption-register.csv" if local else base / "02-regression-interpretation" / "outputs" / "assumption-register.csv",
    }


def verify_upstream(paths: dict[str, Path]) -> None:
    for name, (size, digest) in UPSTREAM.items():
        path = paths[name]
        if not path.is_file() or path.stat().st_size != size or sha256(path) != digest:
            raise ValueError(f"Upstream fingerprint changed: {name}")


def fixed(value: float, digits: int = 8) -> str:
    return "" if math.isnan(value) else f"{value:.{digits}f}"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def load(paths: dict[str, Path]) -> tuple[pd.DataFrame, float]:
    verify_upstream(paths)
    cohort = pd.read_csv(paths["modeling-cohort.csv"])
    baseline = pd.read_csv(paths["baseline-metrics.csv"])
    if cohort.shape != (374, 34) or cohort["split"].value_counts().to_dict() != {"train": 224, "validation": 75, "test": 75}:
        raise ValueError("Modeling cohort shape or split changed.")
    probability = float(baseline.loc[0, "constant_probability"])
    return cohort, probability


def prepare(cohort: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, float]:
    train = cohort.loc[cohort["split"] == "train"].copy()
    validation = cohort.loc[cohort["split"] == "validation"].copy()
    test = cohort.loc[cohort["split"] == "test"].copy()
    age_mean = float(train["age_at_index"].mean())
    for frame in (train, validation, test):
        frame["age_centered_decade"] = (frame["age_at_index"] - age_mean) / 10
        frame["index_class_inpatient"] = (frame["index_class"] == "inpatient").astype(int)
    return train, validation, test, age_mean


def models() -> dict[str, Pipeline]:
    logistic = Pipeline([
        ("scale", StandardScaler()),
        ("model", LogisticRegression(C=np.inf, solver="lbfgs", max_iter=10_000, random_state=SEED)),
    ])
    preprocess = ColumnTransformer([
        ("numeric", StandardScaler(), NUMERIC_FEATURES),
        ("categorical", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAL_FEATURES),
    ])
    forest = Pipeline([
        ("preprocess", preprocess),
        ("model", RandomForestClassifier(n_estimators=300, max_depth=4, min_samples_leaf=20, class_weight=None, random_state=SEED, n_jobs=1)),
    ])
    leaked = Pipeline([
        ("preprocess", ColumnTransformer([("leaked", OneHotEncoder(handle_unknown="ignore", sparse_output=False), LEAKED_FEATURES)])),
        ("model", LogisticRegression(C=np.inf, solver="lbfgs", max_iter=10_000, random_state=SEED)),
    ])
    return {"LOG01": logistic, "ML01": forest, "LEAK01": leaked}


def feature_set(model_id: str) -> list[str]:
    return LOG_FEATURES if model_id == "LOG01" else NUMERIC_FEATURES + CATEGORICAL_FEATURES if model_id == "ML01" else LEAKED_FEATURES


def metric_values(y: np.ndarray, probability: np.ndarray) -> dict[str, float]:
    return {
        "roc_auc": roc_auc_score(y, probability),
        "average_precision": average_precision_score(y, probability),
        "brier": brier_score_loss(y, probability),
        "log_loss": log_loss(y, probability, labels=[0, 1]),
    }


def resampling_rows(train: pd.DataFrame, baseline_probability: float) -> list[dict[str, object]]:
    splitter = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    result = []
    y = train["acute_return_90d"].to_numpy()
    for fold, (fit_index, holdout_index) in enumerate(splitter.split(train, y), start=1):
        y_fit, y_holdout = y[fit_index], y[holdout_index]
        fold_baseline = float(y_fit.mean())
        candidates = {"BASE": np.repeat(fold_baseline, len(holdout_index))}
        for model_id, model in {key: value for key, value in models().items() if key != "LEAK01"}.items():
            features = feature_set(model_id)
            fitted = clone(model).fit(train.iloc[fit_index][features], y_fit)
            candidates[model_id] = fitted.predict_proba(train.iloc[holdout_index][features])[:, 1]
        for model_id, probabilities in candidates.items():
            metrics = metric_values(y_holdout, probabilities)
            result.append({
                "model_id": model_id, "fold": fold, "fit_rows": len(fit_index), "holdout_rows": len(holdout_index),
                "holdout_positives": int(y_holdout.sum()), "baseline_probability": fixed(fold_baseline),
                **{name: fixed(value) for name, value in metrics.items()},
                "partition_rule": "five-fold stratified resampling inside training only",
            })
    return result


def validation_predictions(train: pd.DataFrame, validation: pd.DataFrame, baseline_probability: float):
    fitted = {}
    probabilities = {"BASE": np.repeat(baseline_probability, len(validation))}
    for model_id, model in models().items():
        features = feature_set(model_id)
        fitted[model_id] = model.fit(train[features], train["acute_return_90d"])
        probabilities[model_id] = fitted[model_id].predict_proba(validation[features])[:, 1]
    rows = []
    for model_id, values in probabilities.items():
        for position, (_, row) in enumerate(validation.iterrows()):
            rows.append({
                "model_id": model_id, "model_row_id": row["model_row_id"], "patient_id": row["patient_id"],
                "split": "validation", "position": position + 1, "observed": int(row["acute_return_90d"]),
                "probability": fixed(float(values[position])), "eligible_for_selection": "no" if model_id == "LEAK01" else "yes",
            })
    return fitted, probabilities, rows


def validation_comparison_rows(validation: pd.DataFrame, probabilities: dict[str, np.ndarray]) -> list[dict[str, object]]:
    y = validation["acute_return_90d"].to_numpy()
    result = []
    for model_id in ("BASE", "LOG01", "ML01", "LEAK01"):
        metrics = metric_values(y, probabilities[model_id])
        result.append({
            "model_id": model_id, "rows": len(y), "positives": int(y.sum()), "negatives": int(len(y) - y.sum()),
            **{name: fixed(value) for name, value in metrics.items()},
            "eligible": "no" if model_id == "LEAK01" else "yes",
            "reason": "prohibited post-index and outcome-derived predictors" if model_id == "LEAK01" else "declared comparison",
        })
    return result


def selection_rows(comparison: list[dict[str, object]]) -> list[dict[str, object]]:
    by_id = {row["model_id"]: row for row in comparison}
    result = []
    for model_id in ("BASE", "LOG01", "ML01", "LEAK01"):
        row = by_id[model_id]
        if model_id == "BASE":
            passes = "comparator"
            status = "retained baseline"
        elif model_id == "LEAK01":
            passes = "no"
            status = "rejected before performance review"
        else:
            passes_bool = float(row["brier"]) <= float(by_id["BASE"]["brier"]) and float(row["roc_auc"]) >= 0.55 and float(row["average_precision"]) >= float(by_id["BASE"]["average_precision"])
            passes = "yes" if passes_bool else "no"
            status = "selected" if model_id == "ML01" and passes_bool else "not selected"
        result.append({
            "model_id": model_id, "eligible": row["eligible"], "brier_not_worse_than_baseline": "not applicable" if model_id in {"BASE", "LEAK01"} else "yes" if float(row["brier"]) <= float(by_id["BASE"]["brier"]) else "no",
            "roc_auc_at_least_0_55": "not applicable" if model_id in {"BASE", "LEAK01"} else "yes" if float(row["roc_auc"]) >= 0.55 else "no",
            "average_precision_not_worse_than_baseline": "not applicable" if model_id in {"BASE", "LEAK01"} else "yes" if float(row["average_precision"]) >= float(by_id["BASE"]["average_precision"]) else "no",
            "passes_rule": passes, "selection_status": status,
        })
    if sum(row["selection_status"] == "selected" for row in result) != 1:
        raise ValueError("Selection rule did not choose exactly one eligible candidate.")
    return result


def threshold_rows(validation: pd.DataFrame, probability: np.ndarray) -> tuple[list[dict[str, object]], float]:
    y = validation["acute_return_90d"].to_numpy()
    result = []
    candidates = []
    for threshold in sorted(set(float(value) for value in probability)):
        tn, fp, fn, tp = confusion_matrix(y, probability >= threshold, labels=[0, 1]).ravel()
        sensitivity = tp / (tp + fn)
        specificity = tn / (tn + fp)
        ppv = tp / (tp + fp) if tp + fp else 0.0
        npv = tn / (tn + fn) if tn + fn else 0.0
        meets = sensitivity >= 5 / 7
        if meets:
            candidates.append((int(fp), -threshold, threshold))
        result.append({
            "threshold": fixed(threshold), "tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp),
            "sensitivity": fixed(sensitivity), "specificity": fixed(specificity), "ppv": fixed(ppv), "npv": fixed(npv),
            "meets_minimum_validation_sensitivity": "yes" if meets else "no",
        })
    selected = min(candidates)[2]
    return result, selected


def test_prediction_rows(test: pd.DataFrame, selected_model: Pipeline, threshold: float, baseline_probability: float) -> tuple[np.ndarray, list[dict[str, object]]]:
    probability = selected_model.predict_proba(test[NUMERIC_FEATURES + CATEGORICAL_FEATURES])[:, 1]
    result = []
    for position, (_, row) in enumerate(test.iterrows()):
        result.append({
            "model_row_id": row["model_row_id"], "patient_id": row["patient_id"], "index_start": row["index_start"],
            "observed": int(row["acute_return_90d"]), "baseline_probability": fixed(baseline_probability),
            "selected_probability": fixed(float(probability[position])), "locked_threshold": fixed(threshold),
            "selected_label": int(probability[position] >= threshold),
        })
    return probability, result


def bootstrap_intervals(y: np.ndarray, probability: np.ndarray, threshold: float) -> dict[str, tuple[float, float]]:
    rng = np.random.default_rng(SEED)
    positive = np.flatnonzero(y == 1)
    negative = np.flatnonzero(y == 0)
    values = {name: [] for name in ("roc_auc", "average_precision", "brier", "log_loss", "sensitivity", "specificity", "ppv", "npv")}
    for _ in range(BOOTSTRAPS):
        index = np.concatenate((rng.choice(positive, len(positive), replace=True), rng.choice(negative, len(negative), replace=True)))
        yy, pp = y[index], probability[index]
        values["roc_auc"].append(roc_auc_score(yy, pp))
        values["average_precision"].append(average_precision_score(yy, pp))
        values["brier"].append(brier_score_loss(yy, pp))
        values["log_loss"].append(log_loss(yy, pp, labels=[0, 1]))
        tn, fp, fn, tp = confusion_matrix(yy, pp >= threshold, labels=[0, 1]).ravel()
        values["sensitivity"].append(tp / (tp + fn))
        values["specificity"].append(tn / (tn + fp))
        values["ppv"].append(tp / (tp + fp) if tp + fp else 0.0)
        values["npv"].append(tn / (tn + fn) if tn + fn else 0.0)
    return {name: tuple(np.quantile(series, [0.025, 0.975])) for name, series in values.items()}


def test_metric_rows(test: pd.DataFrame, selected_probability: np.ndarray, threshold: float, baseline_probability: float) -> list[dict[str, object]]:
    y = test["acute_return_90d"].to_numpy()
    result = []
    for model_id, probability, applied_threshold in (
        ("BASE", np.repeat(baseline_probability, len(y)), baseline_probability),
        ("ML01", selected_probability, threshold),
    ):
        metrics = metric_values(y, probability)
        tn, fp, fn, tp = confusion_matrix(y, probability >= applied_threshold, labels=[0, 1]).ravel()
        metrics.update({"sensitivity": tp / (tp + fn), "specificity": tn / (tn + fp), "ppv": tp / (tp + fp) if tp + fp else 0.0, "npv": tn / (tn + fn) if tn + fn else 0.0})
        intervals = bootstrap_intervals(y, probability, applied_threshold)
        for metric, value in metrics.items():
            lower, upper = intervals[metric]
            result.append({
                "model_id": model_id, "metric": metric, "point": fixed(value), "lower95_stratified_bootstrap": fixed(float(lower)),
                "upper95_stratified_bootstrap": fixed(float(upper)), "rows": len(y), "positives": int(y.sum()), "bootstrap_replicates": BOOTSTRAPS,
                "interpretation_limit": "four positive test outcomes; interval is conditional teaching evidence",
            })
    return result


def confusion_rows(test: pd.DataFrame, probability: np.ndarray, threshold: float) -> list[dict[str, object]]:
    tn, fp, fn, tp = confusion_matrix(test["acute_return_90d"], probability >= threshold, labels=[0, 1]).ravel()
    return [
        {"cell": "true_negative", "observed": 0, "predicted": 0, "n": int(tn)},
        {"cell": "false_positive", "observed": 0, "predicted": 1, "n": int(fp)},
        {"cell": "false_negative", "observed": 1, "predicted": 0, "n": int(fn)},
        {"cell": "true_positive", "observed": 1, "predicted": 1, "n": int(tp)},
    ]


def calibration_rows(test: pd.DataFrame, probability: np.ndarray) -> list[dict[str, object]]:
    ordered = pd.DataFrame({"model_row_id": test["model_row_id"].to_numpy(), "observed": test["acute_return_90d"].to_numpy(), "probability": probability}).sort_values(["probability", "model_row_id"]).reset_index(drop=True)
    ordered["group"] = np.repeat(np.arange(1, 6), 15)
    result = []
    for group, rows in ordered.groupby("group"):
        result.append({
            "group": int(group), "rows": len(rows), "positives": int(rows["observed"].sum()),
            "mean_probability": fixed(float(rows["probability"].mean())), "observed_proportion": fixed(float(rows["observed"].mean())),
            "minimum_probability": fixed(float(rows["probability"].min())), "maximum_probability": fixed(float(rows["probability"].max())),
            "limit": "15-row teaching group; not a stable calibration estimate",
        })
    return result


def subgroup_rows(test: pd.DataFrame, probability: np.ndarray, threshold: float) -> list[dict[str, object]]:
    frame = test.copy()
    frame["probability"] = probability
    result = []
    for field in ("gender", "race", "ethnicity", "index_class"):
        for category, rows in frame.groupby(field, dropna=False):
            y = rows["acute_return_90d"].to_numpy()
            p = rows["probability"].to_numpy()
            events = int(y.sum())
            nonevents = len(y) - events
            suppressed = len(y) < 20 or events < 2 or nonevents < 2
            tn, fp, fn, tp = confusion_matrix(y, p >= threshold, labels=[0, 1]).ravel()
            result.append({
                "field": field, "category": category, "rows": len(y), "positives": events, "negatives": nonevents,
                "roc_auc": "" if suppressed else fixed(roc_auc_score(y, p)),
                "sensitivity": "" if suppressed else fixed(tp / (tp + fn)), "specificity": "" if suppressed else fixed(tn / (tn + fp)),
                "ppv": "" if suppressed else fixed(tp / (tp + fp) if tp + fp else 0.0),
                "suppressed": "yes" if suppressed else "no", "reason": "fewer than 20 rows or fewer than 2 outcomes/nonoutcomes" if suppressed else "descriptive teaching estimate; no fairness ranking",
            })
    return result


def feature_name_rows(fitted_model: Pipeline) -> list[dict[str, object]]:
    names = fitted_model.named_steps["preprocess"].get_feature_names_out()
    return [{"position": index + 1, "transformed_feature": name, "source_family": "numeric" if name.startswith("numeric__") else "categorical", "fit_partition": "train only"} for index, name in enumerate(names)]


def leaked_failure_rows(comparison: list[dict[str, object]]) -> list[dict[str, object]]:
    row = next(item for item in comparison if item["model_id"] == "LEAK01")
    return [{
        "model_id": "LEAK01", "prohibited_fields": "next_30d_state|endpoint_90d", "validation_roc_auc": row["roc_auc"],
        "validation_average_precision": row["average_precision"], "validation_brier": row["brier"],
        "failure": "post-index and outcome-derived information violates Module 01 prediction time",
        "selection_eligibility": "never eligible", "required_action": "reject and retain only as a critique fixture",
    }]


def check_rows(train, validation, test, comparison, selection, threshold, test_predictions, confusion, calibration, subgroups, features, leaked) -> list[dict[str, object]]:
    selected = next(row for row in selection if row["selection_status"] == "selected")
    counts = {row["cell"]: row["n"] for row in confusion}
    checks = (
        ("CHK01", "train rows", len(train), 224), ("CHK02", "validation rows", len(validation), 75), ("CHK03", "test rows", len(test), 75),
        ("CHK04", "train positives", int(train["acute_return_90d"].sum()), 25), ("CHK05", "validation positives", int(validation["acute_return_90d"].sum()), 7), ("CHK06", "test positives", int(test["acute_return_90d"].sum()), 4),
        ("CHK07", "validation comparison models", len(comparison), 4), ("CHK08", "selected model", selected["model_id"], "ML01"),
        ("CHK09", "leaked model rejected", leaked[0]["selection_eligibility"], "never eligible"), ("CHK10", "threshold locked", fixed(threshold), "0.08513264"),
        ("CHK11", "test prediction rows", len(test_predictions), 75), ("CHK12", "test confusion total", sum(counts.values()), 75),
        ("CHK13", "test true negatives", counts["true_negative"], 48), ("CHK14", "test false positives", counts["false_positive"], 23),
        ("CHK15", "test false negatives", counts["false_negative"], 2), ("CHK16", "test true positives", counts["true_positive"], 2),
        ("CHK17", "calibration groups", len(calibration), 5), ("CHK18", "calibration rows", sum(row["rows"] for row in calibration), 75),
        ("CHK19", "transformed features", len(features), 15), ("CHK20", "subgroup rows", len(subgroups), 10),
        ("CHK21", "test outcomes conserved", sum(row["observed"] for row in test_predictions), 4), ("CHK22", "bootstrap replicates", BOOTSTRAPS, 2000),
    )
    return [{"check_id": i, "check": label, "observed": observed, "expected": expected, "status": "pass" if observed == expected else "fail"} for i, label, observed, expected in checks]


def svg_calibration(rows: list[dict[str, object]]) -> str:
    points = " ".join(f'{60 + float(r["mean_probability"])*500:.2f},{340 - float(r["observed_proportion"])*280:.2f}' for r in rows)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="400" viewBox="0 0 640 400" role="img" aria-labelledby="title desc"><title id="title">Test calibration teaching groups</title><desc id="desc">Five 15-row groups compare mean predicted probability with observed outcome proportion. Exact values are in calibration-table.csv. Four outcomes make this display imprecise.</desc><rect width="640" height="400" fill="white"/><line x1="60" y1="340" x2="560" y2="60" stroke="#777" stroke-dasharray="6 6"/><polyline points="{points}" fill="none" stroke="#1f49b6" stroke-width="3"/><g fill="#1f49b6">''' + "".join(f'<circle cx="{60 + float(r["mean_probability"])*500:.2f}" cy="{340 - float(r["observed_proportion"])*280:.2f}" r="6"/>' for r in rows) + '''</g><text x="260" y="385" font-size="16">Mean predicted probability</text><text x="18" y="220" font-size="16" transform="rotate(-90 18 220)">Observed proportion</text></svg>\n'''


def svg_threshold(rows: list[dict[str, object]], selected: float) -> str:
    sampled = rows[::max(1, len(rows)//30)]
    sens = " ".join(f'{60 + float(r["threshold"])*2500:.2f},{340 - float(r["sensitivity"])*280:.2f}' for r in sampled)
    spec = " ".join(f'{60 + float(r["threshold"])*2500:.2f},{340 - float(r["specificity"])*280:.2f}' for r in sampled)
    x = 60 + selected*2500
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="400" viewBox="0 0 640 400" role="img" aria-labelledby="title desc"><title id="title">Validation threshold evidence</title><desc id="desc">Sensitivity and specificity across exact validation probability thresholds. The locked threshold is {selected:.8f}. Exact counts are in threshold-table.csv.</desc><rect width="640" height="400" fill="white"/><polyline points="{sens}" fill="none" stroke="#1f49b6" stroke-width="3"/><polyline points="{spec}" fill="none" stroke="#0f766e" stroke-width="3"/><line x1="{x:.2f}" y1="50" x2="{x:.2f}" y2="340" stroke="#d97706" stroke-width="3"/><text x="250" y="385" font-size="16">Threshold</text><text x="18" y="220" font-size="16" transform="rotate(-90 18 220)">Metric value</text><text x="420" y="70" fill="#1f49b6">Sensitivity</text><text x="420" y="92" fill="#0f766e">Specificity</text></svg>\n'''


def build_outputs(paths: dict[str, Path], target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    cohort, baseline_probability = load(paths)
    train, validation, test, age_mean = prepare(cohort)
    resampling = resampling_rows(train, baseline_probability)
    fitted, probabilities, validation_prediction_table = validation_predictions(train, validation, baseline_probability)
    comparison = validation_comparison_rows(validation, probabilities)
    selection = selection_rows(comparison)
    thresholds, threshold = threshold_rows(validation, probabilities["ML01"])
    selected_model = fitted["ML01"]
    selected_probability, test_predictions = test_prediction_rows(test, selected_model, threshold, baseline_probability)
    test_metrics = test_metric_rows(test, selected_probability, threshold, baseline_probability)
    confusion = confusion_rows(test, selected_probability, threshold)
    calibration = calibration_rows(test, selected_probability)
    subgroups = subgroup_rows(test, selected_probability, threshold)
    features = feature_name_rows(selected_model)
    leaked = leaked_failure_rows(comparison)
    threshold_decision = [{"model_id": "ML01", "locked_threshold": fixed(threshold), "validation_minimum_sensitivity": fixed(5/7), "selection_rule": "among thresholds with at least 5 of 7 validation positives select fewest false positives then highest threshold", "locked_before_test": "yes"}]
    outputs = {
        "resampling-results.csv": resampling, "validation-predictions.csv": validation_prediction_table,
        "validation-comparison.csv": comparison, "model-selection-record.csv": selection,
        "threshold-table.csv": thresholds, "threshold-decision.csv": threshold_decision,
        "test-predictions.csv": test_predictions, "test-metrics.csv": test_metrics,
        "confusion-table.csv": confusion, "calibration-table.csv": calibration,
        "subgroup-metrics.csv": subgroups, "transformed-feature-names.csv": features,
        "leaked-model-failure.csv": leaked,
    }
    outputs["prediction-checks.csv"] = check_rows(train, validation, test, comparison, selection, threshold, test_predictions, confusion, calibration, subgroups, features, leaked)
    failed_checks = [row for row in outputs["prediction-checks.csv"] if row["status"] != "pass"]
    if failed_checks:
        raise ValueError(f"Prediction release check failed: {failed_checks}")
    target.mkdir(parents=True)
    report: dict[str, object] = {
        "status": "pass", "version": "0.1.0", "seed": SEED, "bootstrap_replicates": BOOTSTRAPS,
        "age_center_training_mean": fixed(age_mean, 12), "baseline_probability": fixed(baseline_probability, 12),
        "upstream": {name: {"bytes": path.stat().st_size, "sha256": sha256(path)} for name, path in paths.items()},
        "partitions": {"train": 224, "validation": 75, "test": 75, "positive_outcomes": {"train": 25, "validation": 7, "test": 4}},
        "selection": {"model_id": "ML01", "locked_threshold": fixed(threshold), "test_opened_after_lock": True},
        "test_confusion": {row["cell"]: row["n"] for row in confusion}, "outputs": {},
        "decision": {"reference_recommendation": "continue to validity review with conditions", "model_use": "teaching use only"},
    }
    for name, rows in outputs.items():
        path = target / name
        write_csv(path, rows)
        report["outputs"][name] = {"rows": len(rows), "fields": len(rows[0]), "bytes": path.stat().st_size, "sha256": sha256(path)}
    (target / "calibration.svg").write_text(svg_calibration(calibration), encoding="utf-8", newline="")
    (target / "threshold.svg").write_text(svg_threshold(thresholds, threshold), encoding="utf-8", newline="")
    for name in ("calibration.svg", "threshold.svg"):
        path = target / name
        report["outputs"][name] = {"bytes": path.stat().st_size, "sha256": sha256(path)}
    (target / "build-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="")
    return report


def build_workspace(paths: dict[str, Path], target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_upstream(paths)
    shutil.copytree(MODULE_ROOT / "learner-template", target)
    for name in PORTABLE_FILES:
        shutil.copy2(MODULE_ROOT / name, target / name)
    shutil.copy2(__file__, target / Path(__file__).name)
    shutil.copy2(MODULE_ROOT / "validate_prediction_evidence.py", target / "validate_prediction_evidence.py")
    data = target / "data"
    data.mkdir()
    for name, path in paths.items():
        shutil.copy2(path, data / name)
    return build_outputs(upstream_paths(data), target / "outputs")


def self_check() -> None:
    paths = upstream_paths()
    with tempfile.TemporaryDirectory(prefix="fnd2-module03-build-") as temp_dir:
        root = Path(temp_dir)
        outputs = root / "outputs"
        report = build_outputs(paths, outputs)
        assert report["selection"]["model_id"] == "ML01"
        assert report["test_confusion"] == {"true_negative": 48, "false_positive": 23, "false_negative": 2, "true_positive": 2}
        try:
            build_outputs(paths, outputs)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not refuse an existing target.")
        workspace = root / "learner-workspace"
        workspace_report = build_workspace(paths, workspace)
        reproduced = workspace / "reproduced-outputs"
        reproduced_report = build_outputs(upstream_paths(workspace / "data"), reproduced)
        assert reproduced_report["outputs"] == workspace_report["outputs"]
    print("FND-2 Module 03 builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path)
    parser.add_argument("--build-reference", action="store_true")
    parser.add_argument("--outputs-only", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check(); return
    if args.build_reference:
        print(json.dumps(build_outputs(upstream_paths(), MODULE_ROOT / "outputs"), indent=2)); return
    if args.target is None:
        parser.error("target is required unless --self-check or --build-reference is used")
    print(json.dumps(build_outputs(upstream_paths(), args.target.resolve()) if args.outputs_only else build_workspace(upstream_paths(), args.target.resolve()), indent=2))


if __name__ == "__main__":
    main()
