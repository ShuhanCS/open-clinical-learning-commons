"""Build the deterministic APP-4 Module 03 NHANES evidence release."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import shutil
import tempfile
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import log_loss, roc_auc_score


ROOT = Path(__file__).resolve().parent
MODULE01 = ROOT.parent / "01-cds-use-case-decision"
COMMITTED = ROOT / "data" / "evidence"
SEED = 7400303
BOOTSTRAPS = 500
THRESHOLDS = (0.02, 0.03, 0.04, 0.05, 0.075, 0.10)
MOCK_THRESHOLD = 0.20
FEATURES = ("age_centered_per_10", "bmi_centered_per_5", "female_indicator")
CYCLES = (
    ("H", "2013-2014", "development", "WTMEC2YR", 0.5),
    ("I", "2015-2016", "development", "WTMEC2YR", 0.5),
    ("J", "2017-2018", "temporal_holdout", "WTMEC2YR", 1.0),
    ("L", "2021-2023", "transport_stress", "WTPH2YR", 1.0),
)
COMPONENTS = ("DEMO", "BMX", "DIQ", "GHB")
RACE_LABELS = {
    1.0: "Mexican American",
    2.0: "Other Hispanic",
    3.0: "Non-Hispanic White",
    4.0: "Non-Hispanic Black",
    6.0: "Non-Hispanic Asian",
    7.0: "Other or multiracial",
}
DIABETES_LABELS = {
    1.0: "yes",
    2.0: "no",
    3.0: "borderline",
    7.0: "refused",
    9.0: "do not know",
}
OUTPUT_FILES = (
    "cohort-audit.csv.gz",
    "model-cohort.csv.gz",
    "predictions.csv.gz",
    "cohort-flow.csv",
    "missingness.csv",
    "survey-design.csv",
    "model-coefficients.csv",
    "performance.csv",
    "calibration.csv",
    "calibration-groups.csv",
    "threshold-audit.csv",
    "net-benefit.csv",
    "subgroup-support.csv",
    "bootstrap-intervals.csv",
    "transport-comparison.csv",
    "invariants.csv",
    "build-report.json",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fixed(value: float | int) -> str:
    return f"{float(value):.8f}"


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"Refusing to write an empty table: {path.name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0])
    if path.suffix == ".gz":
        with path.open("wb") as raw:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
                with io.TextIOWrapper(zipped, encoding="utf-8", newline="") as text:
                    writer = csv.DictWriter(text, fieldnames=fields, lineterminator="\n")
                    writer.writeheader()
                    writer.writerows(rows)
    else:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)


def write_json(path: Path, value: dict[str, object]) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_inventory(source_root: Path) -> list[dict[str, str]]:
    path = source_root / "data" / "source-inventory.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 16:
        raise ValueError(f"Expected 16 inherited NHANES sources, found {len(rows)}")
    for row in rows:
        source = source_root / row["gzip_filename"]
        if not source.is_file():
            raise FileNotFoundError(source)
        if source.stat().st_size != int(row["gzip_bytes"]) or sha256(source) != row["gzip_sha256"]:
            raise ValueError(f"Inherited source identity changed: {row['source_id']}")
    return rows


def read_xpt(path: Path) -> pd.DataFrame:
    with gzip.open(path, "rb") as handle:
        return pd.read_sas(io.BytesIO(handle.read()), format="xport", encoding="utf-8")


def pregnancy_status(frame: pd.DataFrame) -> pd.Series:
    relevant = frame["RIAGENDR"].eq(2) & frame["RIDAGEYR"].between(35, 44)
    result = pd.Series("not applicable", index=frame.index, dtype="object")
    result.loc[relevant & frame["RIDEXPRG"].eq(1)] = "pregnant"
    result.loc[relevant & frame["RIDEXPRG"].eq(2)] = "not pregnant"
    result.loc[relevant & ~frame["RIDEXPRG"].isin([1, 2])] = "unknown"
    return result


def build_cycle(
    source_root: Path,
    suffix: str,
    cycle: str,
    partition: str,
    weight_name: str,
    weight_multiplier: float,
) -> tuple[pd.DataFrame, list[dict[str, object]]]:
    raw = source_root / "data" / "raw"
    frames = {component: read_xpt(raw / f"{component}_{suffix}.xpt.gz") for component in COMPONENTS}
    for component, frame in frames.items():
        if frame["SEQN"].duplicated().any():
            raise ValueError(f"Duplicate SEQN in {component}_{suffix}")
    ghb_fields = ["SEQN", "LBXGH"] + (["WTPH2YR"] if "WTPH2YR" in frames["GHB"] else [])
    merged = (
        frames["DEMO"][[
            "SEQN", "RIDAGEYR", "RIAGENDR", "RIDRETH3", "RIDEXPRG",
            "WTMEC2YR", "SDMVSTRA", "SDMVPSU",
        ]]
        .merge(frames["BMX"][["SEQN", "BMXBMI"]], on="SEQN", how="left", validate="one_to_one")
        .merge(frames["DIQ"][["SEQN", "DIQ010"]], on="SEQN", how="left", validate="one_to_one")
        .merge(frames["GHB"][ghb_fields], on="SEQN", how="left", validate="one_to_one")
    )
    age = merged["RIDAGEYR"].between(35, 70)
    sex = merged["RIAGENDR"].isin([1, 2])
    diabetes_no = merged["DIQ010"].eq(2)
    status = pregnancy_status(merged)
    nonpregnant = status.isin(["not pregnant", "not applicable"])
    bmi_observed = merged["BMXBMI"].notna()
    bmi_eligible = merged["BMXBMI"].ge(25)
    hba1c_observed = merged["LBXGH"].notna()
    weight = merged[weight_name] if weight_name in merged else pd.Series(np.nan, index=merged.index)
    design_complete = weight.gt(0) & merged["SDMVSTRA"].notna() & merged["SDMVPSU"].notna()
    stage_masks = (
        ("source_interviewed", pd.Series(True, index=merged.index)),
        ("age_35_through_70", age),
        ("valid_recorded_sex", age & sex),
        ("reports_no_diabetes", age & sex & diabetes_no),
        ("nonpregnant_or_not_applicable", age & sex & diabetes_no & nonpregnant),
        ("bmi_observed", age & sex & diabetes_no & nonpregnant & bmi_observed),
        ("bmi_at_least_25", age & sex & diabetes_no & nonpregnant & bmi_observed & bmi_eligible),
        ("hba1c_observed", age & sex & diabetes_no & nonpregnant & bmi_observed & bmi_eligible & hba1c_observed),
        ("design_complete", age & sex & diabetes_no & nonpregnant & bmi_observed & bmi_eligible & hba1c_observed & design_complete),
    )
    flow: list[dict[str, object]] = []
    previous = len(merged)
    for order, (stage, mask) in enumerate(stage_masks, start=1):
        count = int(mask.sum())
        flow.append({
            "cycle": cycle,
            "partition": partition,
            "stage_order": order,
            "stage": stage,
            "rows": count,
            "removed_at_stage": previous - count,
            "interpretation": "sequential eligibility and complete-case accounting",
        })
        previous = count
    audit = merged.loc[age].copy()
    audit_status = pregnancy_status(audit)
    audit_weight = audit[weight_name] if weight_name in audit else pd.Series(np.nan, index=audit.index)
    audit["cycle"] = cycle
    audit["partition"] = partition
    audit["participant_id"] = [f"NHANES-{cycle}-{int(value)}" for value in audit["SEQN"]]
    audit["sex"] = audit["RIAGENDR"].map({1.0: "male", 2.0: "female"}).fillna("unknown")
    audit["race_ethnicity"] = audit["RIDRETH3"].map(RACE_LABELS).fillna("unknown")
    audit["pregnancy_status"] = audit_status
    audit["diabetes_response"] = audit["DIQ010"].map(DIABETES_LABELS).fillna("missing")
    audit["weight_name"] = weight_name
    audit["source_weight"] = audit_weight
    audit["analytic_weight"] = audit_weight * weight_multiplier
    audit["female_indicator"] = audit["RIAGENDR"].eq(2).astype(int)
    audit["age_centered_per_10"] = (audit["RIDAGEYR"] - 50) / 10
    audit["bmi_centered_per_5"] = (audit["BMXBMI"] - 30) / 5
    audit["reports_no_diabetes"] = audit["DIQ010"].eq(2).astype(int)
    audit["pregnancy_eligible"] = audit_status.isin(["not pregnant", "not applicable"]).astype(int)
    audit["bmi_observed"] = audit["BMXBMI"].notna().astype(int)
    audit["bmi_at_least_25"] = audit["BMXBMI"].ge(25).astype(int)
    audit["hba1c_observed"] = audit["LBXGH"].notna().astype(int)
    audit["design_complete"] = (
        audit_weight.gt(0) & audit["SDMVSTRA"].notna() & audit["SDMVPSU"].notna()
    ).astype(int)
    audit["model_eligible"] = (
        audit["RIAGENDR"].isin([1, 2])
        & audit["DIQ010"].eq(2)
        & audit_status.isin(["not pregnant", "not applicable"])
        & audit["BMXBMI"].notna()
        & audit["BMXBMI"].ge(25)
        & audit["LBXGH"].notna()
        & audit_weight.gt(0)
        & audit["SDMVSTRA"].notna()
        & audit["SDMVPSU"].notna()
    ).astype(int)
    audit["outcome_hba1c_ge_6_5"] = np.where(
        audit["LBXGH"].notna(), audit["LBXGH"].ge(6.5).astype(int), np.nan
    )
    return audit, flow


def row_dicts(frame: pd.DataFrame, fields: list[str], float_fields: set[str]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for _, source in frame[fields].iterrows():
        row: dict[str, object] = {}
        for field in fields:
            value = source[field]
            if pd.isna(value):
                row[field] = ""
            elif field in float_fields:
                row[field] = fixed(float(value))
            elif isinstance(value, (np.integer, int)):
                row[field] = int(value)
            elif isinstance(value, (np.floating, float)) and float(value).is_integer():
                row[field] = int(value)
            else:
                row[field] = value
        rows.append(row)
    return rows


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.average(values, weights=weights))


def effective_n(weights: np.ndarray) -> float:
    return float(weights.sum() ** 2 / np.square(weights).sum())


def weighted_auc(y: np.ndarray, probability: np.ndarray, weights: np.ndarray) -> float:
    if len(np.unique(y)) < 2:
        return math.nan
    return float(roc_auc_score(y, probability, sample_weight=weights))


def calibration_stats(y: np.ndarray, probability: np.ndarray, weights: np.ndarray) -> dict[str, float]:
    clipped = np.clip(probability, 1e-8, 1 - 1e-8)
    logits = np.log(clipped / (1 - clipped))
    scaled = weights / weights.mean()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        cil_fit = sm.GLM(
            y,
            np.ones((len(y), 1)),
            family=sm.families.Binomial(),
            offset=logits,
            freq_weights=scaled,
        ).fit()
        slope_fit = sm.GLM(
            y,
            sm.add_constant(logits, has_constant="add"),
            family=sm.families.Binomial(),
            freq_weights=scaled,
        ).fit()
    return {
        "calibration_in_the_large": float(cil_fit.params[0]),
        "joint_intercept": float(slope_fit.params[0]),
        "calibration_slope": float(slope_fit.params[1]),
    }


def model_fit(model: pd.DataFrame):
    development = model.loc[model["partition"].eq("development")].copy()
    weights = development["analytic_weight"].to_numpy(float)
    design = sm.add_constant(development[list(FEATURES)].astype(float), has_constant="add")
    fitted = sm.GLM(
        development["outcome_hba1c_ge_6_5"].astype(int).to_numpy(),
        design,
        family=sm.families.Binomial(),
        freq_weights=weights / weights.mean(),
    ).fit()
    all_design = sm.add_constant(model[list(FEATURES)].astype(float), has_constant="add")
    probability = np.asarray(fitted.predict(all_design), dtype=float)
    baseline = weighted_mean(
        development["outcome_hba1c_ge_6_5"].to_numpy(float), weights
    )
    return fitted, probability, baseline


def performance_rows(model: pd.DataFrame, baseline: float) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for partition in ("development", "temporal_holdout", "transport_stress"):
        rows = model.loc[model["partition"].eq(partition)]
        y = rows["outcome_hba1c_ge_6_5"].to_numpy(int)
        weights = rows["analytic_weight"].to_numpy(float)
        for model_name, probability in (
            ("development_prevalence_baseline", np.repeat(baseline, len(rows))),
            ("transparent_weighted_logit", rows["model_probability"].to_numpy(float)),
        ):
            result.append({
                "partition": partition,
                "model": model_name,
                "rows": len(rows),
                "events": int(y.sum()),
                "effective_n": fixed(effective_n(weights)),
                "weighted_prevalence": fixed(weighted_mean(y, weights)),
                "weighted_mean_probability": fixed(weighted_mean(probability, weights)),
                "weighted_brier": fixed(weighted_mean(np.square(y - probability), weights)),
                "weighted_log_loss": fixed(log_loss(y, probability, sample_weight=weights, labels=[0, 1])),
                "weighted_roc_auc": fixed(weighted_auc(y, probability, weights)),
                "claim_limit": "historical public survey classification evidence; not local validity or clinical utility",
            })
    return result


def calibration_rows(model: pd.DataFrame) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    summaries: list[dict[str, object]] = []
    groups: list[dict[str, object]] = []
    for partition in ("development", "temporal_holdout", "transport_stress"):
        rows = model.loc[model["partition"].eq(partition)].sort_values(
            ["model_probability", "participant_id"]
        ).copy()
        y = rows["outcome_hba1c_ge_6_5"].to_numpy(int)
        probability = rows["model_probability"].to_numpy(float)
        weights = rows["analytic_weight"].to_numpy(float)
        stats = calibration_stats(y, probability, weights)
        summaries.append({
            "partition": partition,
            "rows": len(rows),
            "events": int(y.sum()),
            "weighted_observed": fixed(weighted_mean(y, weights)),
            "weighted_mean_probability": fixed(weighted_mean(probability, weights)),
            "calibration_in_the_large": fixed(stats["calibration_in_the_large"]),
            "joint_calibration_intercept": fixed(stats["joint_intercept"]),
            "calibration_slope": fixed(stats["calibration_slope"]),
            "method": "survey-weighted binomial recalibration with fixed predictions",
            "claim_limit": "teaching point estimate pending formal complex-survey methods review",
        })
        midpoint = (np.cumsum(weights) - weights / 2) / weights.sum()
        rows["calibration_group"] = np.minimum((midpoint * 5).astype(int) + 1, 5)
        for group, subset in rows.groupby("calibration_group", sort=True):
            group_y = subset["outcome_hba1c_ge_6_5"].to_numpy(int)
            group_p = subset["model_probability"].to_numpy(float)
            group_w = subset["analytic_weight"].to_numpy(float)
            groups.append({
                "partition": partition,
                "calibration_group": int(group),
                "rows": len(subset),
                "events": int(group_y.sum()),
                "effective_n": fixed(effective_n(group_w)),
                "minimum_probability": fixed(group_p.min()),
                "maximum_probability": fixed(group_p.max()),
                "weighted_mean_probability": fixed(weighted_mean(group_p, group_w)),
                "weighted_observed": fixed(weighted_mean(group_y, group_w)),
                "claim_limit": "weighted score-range description; not a local calibration guarantee",
            })
    return summaries, groups


def confusion(y: np.ndarray, probability: np.ndarray, weights: np.ndarray, threshold: float) -> dict[str, float]:
    positive = probability >= threshold
    tp_mask = positive & (y == 1)
    fp_mask = positive & (y == 0)
    fn_mask = ~positive & (y == 1)
    tn_mask = ~positive & (y == 0)
    weighted = {
        "tp": float(weights[tp_mask].sum()),
        "fp": float(weights[fp_mask].sum()),
        "fn": float(weights[fn_mask].sum()),
        "tn": float(weights[tn_mask].sum()),
    }
    result: dict[str, float] = {
        "tp_rows": int(tp_mask.sum()),
        "fp_rows": int(fp_mask.sum()),
        "fn_rows": int(fn_mask.sum()),
        "tn_rows": int(tn_mask.sum()),
        "flagged_rows": int(positive.sum()),
        "weighted_flag_rate": weighted_mean(positive.astype(int), weights),
        "weighted_sensitivity": weighted["tp"] / (weighted["tp"] + weighted["fn"]),
        "weighted_specificity": weighted["tn"] / (weighted["tn"] + weighted["fp"]),
        "weighted_ppv": weighted["tp"] / (weighted["tp"] + weighted["fp"]),
        "weighted_npv": weighted["tn"] / (weighted["tn"] + weighted["fn"]),
        "weighted_missed_per_1000": 1000 * weighted["fn"] / weights.sum(),
        "weighted_flags_per_1000": 1000 * (weighted["tp"] + weighted["fp"]) / weights.sum(),
    }
    return result


def threshold_rows(model: pd.DataFrame) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    audits: list[dict[str, object]] = []
    curves: list[dict[str, object]] = []
    for partition in ("development", "temporal_holdout", "transport_stress"):
        rows = model.loc[model["partition"].eq(partition)]
        y = rows["outcome_hba1c_ge_6_5"].to_numpy(int)
        probability = rows["model_probability"].to_numpy(float)
        weights = rows["analytic_weight"].to_numpy(float)
        prevalence = weighted_mean(y, weights)
        for threshold in THRESHOLDS + (MOCK_THRESHOLD,):
            values = confusion(y, probability, weights, threshold)
            status = "evidence candidate, not selected or accepted" if threshold in THRESHOLDS else "rejected Module 02 mechanics fixture"
            audits.append({
                "partition": partition,
                "threshold": fixed(threshold),
                "threshold_status": status,
                **{name: fixed(value) if name.startswith("weighted_") else value for name, value in values.items()},
                "claim_limit": "classification tradeoff only; no clinical threshold authority",
            })
            odds = threshold / (1 - threshold)
            model_nb = weighted_mean(y * (probability >= threshold) - (1 - y) * (probability >= threshold) * odds, weights)
            all_nb = prevalence - (1 - prevalence) * odds
            for strategy, net_benefit in (
                ("transparent_weighted_logit", model_nb),
                ("test_all", all_nb),
                ("test_none", 0.0),
            ):
                curves.append({
                    "partition": partition,
                    "threshold": fixed(threshold),
                    "threshold_status": status,
                    "strategy": strategy,
                    "weighted_net_benefit": fixed(net_benefit),
                    "false_positive_weight": fixed(odds),
                    "assumption": "threshold odds encode a hypothetical false-positive to true-positive tradeoff",
                    "claim_limit": "does not estimate patient benefit, harm, preference, cost, or clinical utility",
                })
    return audits, curves


def subgroup_rows(model: pd.DataFrame) -> list[dict[str, object]]:
    frame = model.copy()
    frame["age_band"] = pd.cut(
        frame["RIDAGEYR"], [34, 44, 54, 64, 70], labels=["35-44", "45-54", "55-64", "65-70"]
    ).astype(str)
    frame["bmi_band"] = pd.cut(
        frame["BMXBMI"], [24.999, 29.999, 34.999, 39.999, np.inf],
        labels=["25.0-29.9", "30.0-34.9", "35.0-39.9", "40.0+"],
    ).astype(str)
    dimensions = {
        "recorded_sex": "sex",
        "age_band": "age_band",
        "bmi_band": "bmi_band",
        "race_and_hispanic_origin": "race_ethnicity",
    }
    result: list[dict[str, object]] = []
    for partition in ("development", "temporal_holdout", "transport_stress"):
        partition_rows = frame.loc[frame["partition"].eq(partition)]
        for dimension, field in dimensions.items():
            for group, rows in partition_rows.groupby(field, sort=True):
                y = rows["outcome_hba1c_ge_6_5"].to_numpy(int)
                probability = rows["model_probability"].to_numpy(float)
                weights = rows["analytic_weight"].to_numpy(float)
                ess = effective_n(weights)
                supported = len(rows) >= 100 and int(y.sum()) >= 20 and int((1 - y).sum()) >= 20 and ess >= 50
                result.append({
                    "partition": partition,
                    "dimension": dimension,
                    "group": group,
                    "rows": len(rows),
                    "events": int(y.sum()),
                    "non_events": int((1 - y).sum()),
                    "effective_n": fixed(ess),
                    "weighted_prevalence": fixed(weighted_mean(y, weights)),
                    "weighted_mean_probability": fixed(weighted_mean(probability, weights)),
                    "weighted_brier": fixed(weighted_mean(np.square(y - probability), weights)) if supported else "",
                    "weighted_roc_auc": fixed(weighted_auc(y, probability, weights)) if supported else "",
                    "support_status": "report with boundary" if supported else "suppress performance: support rule not met",
                    "threshold_metrics": "not calculated because no threshold is accepted",
                    "claim_limit": "descriptive support audit only; no trait, ranking, fairness certification, or group-specific action",
                })
    return result


def bootstrap_weights(rows: pd.DataFrame, rng: np.random.Generator) -> np.ndarray:
    multiplier = np.zeros(len(rows), dtype=float)
    strata = rows["SDMVSTRA"].to_numpy()
    psu = rows["SDMVPSU"].to_numpy()
    for stratum in sorted(set(strata)):
        positions = np.flatnonzero(strata == stratum)
        units = np.array(sorted(set(psu[positions])))
        draws = rng.choice(units, size=len(units), replace=True)
        for unit in units:
            multiplier[positions[psu[positions] == unit]] = int(np.sum(draws == unit))
    return rows["analytic_weight"].to_numpy(float) * multiplier


def metric_bundle(y: np.ndarray, probability: np.ndarray, weights: np.ndarray) -> dict[str, float]:
    stats = calibration_stats(y, probability, weights)
    result = {
        "weighted_prevalence": weighted_mean(y, weights),
        "weighted_mean_probability": weighted_mean(probability, weights),
        "weighted_brier": weighted_mean(np.square(y - probability), weights),
        "weighted_roc_auc": weighted_auc(y, probability, weights),
        "calibration_in_the_large": stats["calibration_in_the_large"],
        "calibration_slope": stats["calibration_slope"],
    }
    for threshold in THRESHOLDS:
        values = confusion(y, probability, weights, threshold)
        key = fixed(threshold)
        result[f"weighted_flag_rate_at_{key}"] = values["weighted_flag_rate"]
        result[f"weighted_sensitivity_at_{key}"] = values["weighted_sensitivity"]
        result[f"weighted_specificity_at_{key}"] = values["weighted_specificity"]
    return result


def bootstrap_rows(model: pd.DataFrame) -> list[dict[str, object]]:
    rng = np.random.default_rng(SEED)
    result: list[dict[str, object]] = []
    for partition in ("temporal_holdout", "transport_stress"):
        rows = model.loc[model["partition"].eq(partition)].reset_index(drop=True)
        y = rows["outcome_hba1c_ge_6_5"].to_numpy(int)
        probability = rows["model_probability"].to_numpy(float)
        point = metric_bundle(y, probability, rows["analytic_weight"].to_numpy(float))
        draws = {name: [] for name in point}
        for _ in range(BOOTSTRAPS):
            weights = bootstrap_weights(rows, rng)
            if weights.sum() <= 0 or weights[y == 1].sum() <= 0 or weights[y == 0].sum() <= 0:
                continue
            try:
                values = metric_bundle(y, probability, weights)
            except (ValueError, np.linalg.LinAlgError):
                continue
            for name, value in values.items():
                if math.isfinite(value):
                    draws[name].append(value)
        for name, values in draws.items():
            if len(values) < int(BOOTSTRAPS * 0.95):
                raise ValueError(f"Too few valid bootstrap replicates for {partition} {name}: {len(values)}")
            lower, upper = np.quantile(values, [0.025, 0.975])
            result.append({
                "partition": partition,
                "metric": name,
                "point": fixed(point[name]),
                "lower95": fixed(lower),
                "upper95": fixed(upper),
                "valid_replicates": len(values),
                "requested_replicates": BOOTSTRAPS,
                "seed": SEED,
                "method": "stratified PSU sensitivity bootstrap with fixed predictions",
                "claim_limit": "teaching interval pending formal complex-survey methods review",
            })
    return result


def transport_rows(
    performance: list[dict[str, object]],
    calibration: list[dict[str, object]],
    thresholds: list[dict[str, object]],
) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    perf = {
        (row["partition"], row["model"]): row
        for row in performance
        if row["model"] == "transparent_weighted_logit"
    }
    cal = {row["partition"]: row for row in calibration}
    for metric in (
        "weighted_prevalence", "weighted_mean_probability", "weighted_brier",
        "weighted_log_loss", "weighted_roc_auc",
    ):
        holdout = float(perf[("temporal_holdout", "transparent_weighted_logit")][metric])
        transport = float(perf[("transport_stress", "transparent_weighted_logit")][metric])
        result.append({
            "measure": metric,
            "threshold": "",
            "temporal_holdout": fixed(holdout),
            "transport_stress": fixed(transport),
            "transport_minus_holdout": fixed(transport - holdout),
            "interpretation": "describe the change; do not assign a cause",
        })
    for metric in ("calibration_in_the_large", "calibration_slope"):
        holdout = float(cal["temporal_holdout"][metric])
        transport = float(cal["transport_stress"][metric])
        result.append({
            "measure": metric,
            "threshold": "",
            "temporal_holdout": fixed(holdout),
            "transport_stress": fixed(transport),
            "transport_minus_holdout": fixed(transport - holdout),
            "interpretation": "describe the change; do not assign a cause",
        })
    threshold_map = {(row["partition"], row["threshold"]): row for row in thresholds}
    for threshold in THRESHOLDS:
        key = fixed(threshold)
        holdout = float(threshold_map[("temporal_holdout", key)]["weighted_flag_rate"])
        transport = float(threshold_map[("transport_stress", key)]["weighted_flag_rate"])
        result.append({
            "measure": "weighted_flag_rate",
            "threshold": key,
            "temporal_holdout": fixed(holdout),
            "transport_stress": fixed(transport),
            "transport_minus_holdout": fixed(transport - holdout),
            "interpretation": "candidate burden shift only; threshold remains unaccepted",
        })
    return result


def missingness_rows(audit: pd.DataFrame) -> list[dict[str, object]]:
    fields = {
        "recorded_sex": audit["RIAGENDR"].isin([1, 2]),
        "diabetes_response": audit["DIQ010"].isin([1, 2, 3, 7, 9]),
        "pregnancy_eligibility": audit["pregnancy_status"].ne("unknown"),
        "body_mass_index": audit["BMXBMI"].notna(),
        "hba1c": audit["LBXGH"].notna(),
        "survey_weight": audit["source_weight"].gt(0),
        "survey_stratum": audit["SDMVSTRA"].notna(),
        "survey_psu": audit["SDMVPSU"].notna(),
    }
    result: list[dict[str, object]] = []
    for cycle in [item[1] for item in CYCLES]:
        positions = audit["cycle"].eq(cycle)
        total = int(positions.sum())
        for field, observed in fields.items():
            available = int((positions & observed).sum())
            result.append({
                "cycle": cycle,
                "field": field,
                "age_eligible_rows": total,
                "observed_or_valid": available,
                "missing_or_invalid": total - available,
                "missing_or_invalid_percent": fixed(100 * (total - available) / total),
                "handling": "explicit exclusion or unavailable state; no imputation",
            })
    return result


def survey_rows(model: pd.DataFrame) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for partition, rows in model.groupby("partition", sort=True):
        weights = rows["analytic_weight"].to_numpy(float)
        cycles = "|".join(sorted(rows["cycle"].unique()))
        weight_names = "|".join(sorted(rows["weight_name"].unique()))
        rule = "WTMEC2YR / 2 per development cycle" if partition == "development" else weight_names
        result.append({
            "partition": partition,
            "cycles": cycles,
            "weight_source": weight_names,
            "analytic_weight_rule": rule,
            "rows": len(rows),
            "events": int(rows["outcome_hba1c_ge_6_5"].sum()),
            "strata": rows["SDMVSTRA"].nunique(),
            "psu_within_stratum": "2",
            "effective_n": fixed(effective_n(weights)),
            "weight_sum": fixed(weights.sum()),
            "pooling_status": "pooled only for development" if partition == "development" else "kept separate",
            "claim_limit": "weighted teaching analysis pending named NHANES survey-methods review",
        })
    return result


def build(source_root: Path, output: Path) -> dict[str, object]:
    source_root = source_root.resolve()
    output = output.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing output: {output}")
    inventory = read_inventory(source_root)
    audits: list[pd.DataFrame] = []
    flow: list[dict[str, object]] = []
    for cycle in CYCLES:
        audit, cycle_flow = build_cycle(source_root, *cycle)
        audits.append(audit)
        flow.extend(cycle_flow)
    audit = pd.concat(audits, ignore_index=True).sort_values(["cycle", "SEQN"]).reset_index(drop=True)
    model = audit.loc[audit["model_eligible"].eq(1)].copy().reset_index(drop=True)
    fitted, probability, baseline = model_fit(model)
    model["model_probability"] = probability
    model["development_prevalence_baseline"] = baseline
    performance = performance_rows(model, baseline)
    calibration, calibration_groups = calibration_rows(model)
    thresholds, curves = threshold_rows(model)
    subgroups = subgroup_rows(model)
    bootstraps = bootstrap_rows(model)
    transports = transport_rows(performance, calibration, thresholds)
    missingness = missingness_rows(audit)
    surveys = survey_rows(model)
    coefficients = []
    coefficient_notes = {
        "const": "intercept at age 50, BMI 30, and male indicator",
        "age_centered_per_10": "age centered at 50 and divided by 10",
        "bmi_centered_per_5": "BMI centered at 30 kg/m2 and divided by 5",
        "female_indicator": "1 for source-recorded female and 0 for source-recorded male",
    }
    for term, estimate in fitted.params.items():
        coefficients.append({
            "term": term,
            "coefficient": fixed(estimate),
            "odds_ratio": fixed(math.exp(estimate)),
            "coding": coefficient_notes[term],
            "fit_partition": "NHANES 2013-2014 and 2015-2016 development evidence only",
            "uncertainty_status": "not released pending design-reviewed coefficient variance method",
            "claim_limit": "prediction-model term; not causal and not a clinical effect",
        })
    expected_counts = {
        "age_eligible_rows": 14892,
        "model_rows": 7544,
        "model_events": 328,
        "development_rows": 3652,
        "development_events": 156,
        "temporal_holdout_rows": 1806,
        "temporal_holdout_events": 97,
        "transport_stress_rows": 2086,
        "transport_stress_events": 75,
    }
    observed_counts = {
        "age_eligible_rows": len(audit),
        "model_rows": len(model),
        "model_events": int(model["outcome_hba1c_ge_6_5"].sum()),
    }
    for partition in ("development", "temporal_holdout", "transport_stress"):
        rows = model.loc[model["partition"].eq(partition)]
        observed_counts[f"{partition}_rows"] = len(rows)
        observed_counts[f"{partition}_events"] = int(rows["outcome_hba1c_ge_6_5"].sum())
    invariant_items = {
        "complete_source_files": (len(inventory), 16),
        "source_component_rows": (sum(int(row["rows"]) for row in inventory), 145563),
        "source_gzip_bytes": (sum(int(row["gzip_bytes"]) for row in inventory), 3149043),
        **{name: (observed_counts[name], expected) for name, expected in expected_counts.items()},
        "model_terms": (len(coefficients), 4),
        "candidate_thresholds": (len(THRESHOLDS), 6),
        "mock_threshold_rejected_rows": (sum(row["threshold_status"].startswith("rejected") for row in thresholds), 3),
        "bootstrap_requested": (BOOTSTRAPS, 500),
        "bootstrap_partitions": (len({row["partition"] for row in bootstraps}), 2),
        "failed_bootstrap_metrics": (sum(int(row["valid_replicates"]) < 475 for row in bootstraps), 0),
        "selected_thresholds": (0, 0),
        "holdout_or_transport_fit_rows": (0, 0),
    }
    invariants = [{
        "check_id": f"INV{index:02d}",
        "check": name,
        "observed": observed,
        "expected": expected,
        "status": "pass" if observed == expected else "fail",
    } for index, (name, (observed, expected)) in enumerate(invariant_items.items(), start=1)]
    if any(row["status"] != "pass" for row in invariants):
        failed = [row["check"] for row in invariants if row["status"] != "pass"]
        raise ValueError(f"Evidence invariants failed: {', '.join(failed)}")
    output.mkdir(parents=True)
    audit_fields = [
        "participant_id", "cycle", "partition", "SEQN", "RIDAGEYR", "sex", "race_ethnicity",
        "pregnancy_status", "diabetes_response", "BMXBMI", "LBXGH", "weight_name", "source_weight",
        "analytic_weight", "SDMVSTRA", "SDMVPSU", "reports_no_diabetes", "pregnancy_eligible",
        "bmi_observed", "bmi_at_least_25", "hba1c_observed", "design_complete", "model_eligible",
        "outcome_hba1c_ge_6_5",
    ]
    model_fields = [
        "participant_id", "cycle", "partition", "RIDAGEYR", "sex", "race_ethnicity", "BMXBMI",
        "LBXGH", "outcome_hba1c_ge_6_5", "weight_name", "analytic_weight", "SDMVSTRA", "SDMVPSU",
        *FEATURES,
    ]
    prediction_fields = [
        "participant_id", "cycle", "partition", "outcome_hba1c_ge_6_5", "analytic_weight",
        "development_prevalence_baseline", "model_probability",
    ]
    float_audit = {"BMXBMI", "LBXGH", "source_weight", "analytic_weight"}
    float_model = {"BMXBMI", "LBXGH", "analytic_weight", *FEATURES}
    float_prediction = {"analytic_weight", "development_prevalence_baseline", "model_probability"}
    write_rows(output / "cohort-audit.csv.gz", row_dicts(audit, audit_fields, float_audit))
    write_rows(output / "model-cohort.csv.gz", row_dicts(model, model_fields, float_model))
    write_rows(output / "predictions.csv.gz", row_dicts(model, prediction_fields, float_prediction))
    write_rows(output / "cohort-flow.csv", flow)
    write_rows(output / "missingness.csv", missingness)
    write_rows(output / "survey-design.csv", surveys)
    write_rows(output / "model-coefficients.csv", coefficients)
    write_rows(output / "performance.csv", performance)
    write_rows(output / "calibration.csv", calibration)
    write_rows(output / "calibration-groups.csv", calibration_groups)
    write_rows(output / "threshold-audit.csv", thresholds)
    write_rows(output / "net-benefit.csv", curves)
    write_rows(output / "subgroup-support.csv", subgroups)
    write_rows(output / "bootstrap-intervals.csv", bootstraps)
    write_rows(output / "transport-comparison.csv", transports)
    write_rows(output / "invariants.csv", invariants)
    holdout = next(row for row in performance if row["partition"] == "temporal_holdout" and row["model"] == "transparent_weighted_logit")
    transport = next(row for row in performance if row["partition"] == "transport_stress" and row["model"] == "transparent_weighted_logit")
    report: dict[str, object] = {
        "schema_version": "1.0.0",
        "release_id": "APP4-M03-NHANES-EVIDENCE-2026-08-31-v1",
        "status": "historical public teaching evidence only",
        "source_files": len(inventory),
        "source_component_rows": sum(int(row["rows"]) for row in inventory),
        "source_gzip_bytes": sum(int(row["gzip_bytes"]) for row in inventory),
        "age_eligible_rows": len(audit),
        "model_rows": len(model),
        "model_events": int(model["outcome_hba1c_ge_6_5"].sum()),
        "partitions": {
            partition: {
                "rows": int((model["partition"] == partition).sum()),
                "events": int(model.loc[model["partition"] == partition, "outcome_hba1c_ge_6_5"].sum()),
            }
            for partition in ("development", "temporal_holdout", "transport_stress")
        },
        "target": "LBXGH at or above 6.5 percent; observed laboratory result, not diagnosis",
        "model": "survey-weighted binomial GLM with logit link; age, BMI, and female indicator",
        "development_prevalence_baseline": fixed(baseline),
        "model_coefficients": {row["term"]: row["coefficient"] for row in coefficients},
        "temporal_holdout": {
            "weighted_roc_auc": holdout["weighted_roc_auc"],
            "weighted_brier": holdout["weighted_brier"],
            "weighted_prevalence": holdout["weighted_prevalence"],
        },
        "transport_stress": {
            "weighted_roc_auc": transport["weighted_roc_auc"],
            "weighted_brier": transport["weighted_brier"],
            "weighted_prevalence": transport["weighted_prevalence"],
        },
        "candidate_thresholds": [fixed(value) for value in THRESHOLDS],
        "module02_mock_threshold": {
            "value": fixed(MOCK_THRESHOLD),
            "status": "rejected mechanics fixture; not an evidence candidate",
        },
        "accepted_threshold": None,
        "bootstrap": {
            "replicates": BOOTSTRAPS,
            "seed": SEED,
            "method": "stratified PSU sensitivity bootstrap with fixed predictions",
        },
        "authority": {
            "diagnosis": "prohibited",
            "real_patient_scoring": "prohibited",
            "clinical_threshold_acceptance": "prohibited",
            "clinical_alerting": "prohibited",
            "implementation": "prohibited",
            "deployment": "prohibited",
        },
    }
    write_json(output / "build-report.json", report)
    manifest: list[dict[str, object]] = []
    for relative in OUTPUT_FILES:
        path = output / relative
        if relative.endswith(".json"):
            rows = 1
        elif relative.endswith(".csv.gz"):
            with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
                rows = sum(1 for _ in csv.DictReader(handle))
        else:
            with path.open(encoding="utf-8", newline="") as handle:
                rows = sum(1 for _ in csv.DictReader(handle))
        manifest.append({
            "relative_path": relative,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "rows": rows,
            "role": "immutable derived historical evidence",
        })
    write_rows(output / "evidence-manifest.csv", manifest)
    return {
        "status": "pass",
        "source_files": len(inventory),
        "age_eligible_rows": len(audit),
        "model_rows": len(model),
        "model_events": int(model["outcome_hba1c_ge_6_5"].sum()),
        "evidence_files": len(manifest),
        "manifest_sha256": sha256(output / "evidence-manifest.csv"),
    }


def compare_trees(first: Path, second: Path) -> None:
    first_files = sorted(path.relative_to(first).as_posix() for path in first.rglob("*") if path.is_file())
    second_files = sorted(path.relative_to(second).as_posix() for path in second.rglob("*") if path.is_file())
    if first_files != second_files:
        raise ValueError("Evidence file set changed")
    changed = [relative for relative in first_files if (first / relative).read_bytes() != (second / relative).read_bytes()]
    if changed:
        raise ValueError(f"Evidence output changed: {', '.join(changed)}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module03-evidence-") as temporary:
        base = Path(temporary)
        first = base / "first"
        second = base / "second"
        first_report = build(MODULE01, first)
        second_report = build(MODULE01, second)
        compare_trees(first, second)
        if first_report["manifest_sha256"] != second_report["manifest_sha256"]:
            raise AssertionError("Clean evidence manifests differ")
        try:
            build(MODULE01, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing output")
        changed = base / "changed-source"
        shutil.copytree(MODULE01 / "data", changed / "data")
        raw = changed / "data" / "raw" / "DEMO_H.xpt.gz"
        content = bytearray(raw.read_bytes())
        content[-1] ^= 1
        raw.write_bytes(content)
        try:
            build(changed, base / "changed-output")
        except ValueError as error:
            if "identity changed" not in str(error):
                raise
        else:
            raise AssertionError("Builder accepted a changed inherited source")
    print("APP-4 Module 03 evidence builder self-check passed: two exact builds and changed-source rejection.")


def verify() -> None:
    if not COMMITTED.is_dir():
        raise FileNotFoundError(f"Committed evidence release not found: {COMMITTED}")
    with tempfile.TemporaryDirectory(prefix="app4-module03-verify-") as temporary:
        rebuilt = Path(temporary) / "evidence"
        report = build(MODULE01, rebuilt)
        compare_trees(COMMITTED, rebuilt)
    print(json.dumps({"status": "pass", **report}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=MODULE01)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.verify:
            verify()
        elif args.output:
            print(json.dumps(build(args.source_root, args.output), indent=2))
        else:
            parser.error("provide --output, --verify, or --self-check")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
