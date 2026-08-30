"""Build the exact FND-2 Module 04 validity, adjustment, and longitudinal evidence."""

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
import statsmodels.api as sm
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from statsmodels.duration.hazard_regression import PHReg


MODULE_ROOT = Path(__file__).resolve().parent
SEED = 20260830
UPSTREAM = {
    "checkpoint-release.json": (4914, "03c147d2e75cd446a43b9d56e49495df69af90d42d2b14ad4d860aea9d67239f"),
    "checkpoint-contract.json": (2351, "e32c4d31b675fe7943ed22f432464938a258fc0bb4e7d40e2ac688791dcbad93"),
    "checkpoint-progression.md": (1502, "42207a796e0ee0f6af29b9941cae6f19a273725d4b4ea2527c54c789b5c36470"),
    "modeling-cohort.csv": (138503, "6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332"),
    "split-registry.csv": (51910, "05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1"),
    "linear-subset-registry.csv": (17195, "547e21378c40241ae33982da67eebc58ef5a67bb89bfdda1638b9cb3ab85696b"),
    "assumption-register.csv": (2181, "7c6322667a383458a34aea49b687d1a6716aaaf0f780ccf060f1c99d671956e3"),
    "prediction-model-contract.json": (2831, "0aab6eb29fbcbd921e191c62d5a0a44554de0a683fd560359991fcc9db034015"),
    "prediction-progression.md": (1665, "063c10d34c03e9a9a6dfb05781dd373abec4c8d6ff5a8db3076e918db6cc3334"),
}
PORTABLE_FILES = (
    "requirements.txt", "data-spec.md", "source-record.yml", "assessment.md",
    "dag.mmd", "paired-longitudinal-survival.R",
)
NUMERIC_CONFOUNDERS = ["age", "baseline_severity", "comorbidity_count"]
CATEGORICAL_CONFOUNDERS = ["site"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fixed(value: float, digits: int = 8) -> str:
    return "" if math.isnan(value) else f"{value:.{digits}f}"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"Cannot write empty table: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def upstream_paths(root: Path | None = None) -> dict[str, Path]:
    if root is not None:
        return {name: root / name for name in UPSTREAM}
    course = MODULE_ROOT.parents[1]
    checkpoint = course / "checkpoints" / "01-modeling-readiness-release"
    modules = course / "modules"
    return {
        "checkpoint-release.json": checkpoint / "release.json",
        "checkpoint-contract.json": checkpoint / "checkpoint-contract.json",
        "checkpoint-progression.md": checkpoint / "reference" / "progression-decision.md",
        "modeling-cohort.csv": modules / "01-aims-reproducible-workspace" / "outputs" / "modeling-cohort.csv",
        "split-registry.csv": modules / "01-aims-reproducible-workspace" / "outputs" / "split-registry.csv",
        "linear-subset-registry.csv": modules / "02-regression-interpretation" / "outputs" / "linear-subset-registry.csv",
        "assumption-register.csv": modules / "02-regression-interpretation" / "outputs" / "assumption-register.csv",
        "prediction-model-contract.json": modules / "03-prediction-evaluation" / "model-contract.json",
        "prediction-progression.md": modules / "03-prediction-evaluation" / "progression-decision.md",
    }


def verify_upstream(paths: dict[str, Path]) -> None:
    for name, (size, digest) in UPSTREAM.items():
        path = paths[name]
        if not path.is_file() or path.stat().st_size != size or sha256(path) != digest:
            raise ValueError(f"Accepted upstream fingerprint changed: {name}")


def generate_treatment(rng: np.random.Generator, n: int = 600) -> pd.DataFrame:
    site = rng.choice(np.array(["A", "B", "C"]), size=n, p=[0.45, 0.35, 0.20])
    age = np.clip(rng.normal(62, 12, n), 25, 90)
    comorbidity = rng.poisson(np.clip(1.2 + (age - 45) / 35, 0.4, 3.5))
    site_severity = np.select([site == "B", site == "C"], [2.0, 5.0], default=0.0)
    severity = np.clip(45 + 0.32 * (age - 60) + 3.2 * comorbidity + site_severity + rng.normal(0, 7, n), 10, 95)
    logit = -0.8 + 0.055 * (severity - 50) + 0.22 * comorbidity + np.select([site == "B", site == "C"], [-0.15, 0.35], default=0.0)
    probability = 1 / (1 + np.exp(-logit))
    treatment = rng.binomial(1, probability)
    shared_noise = rng.normal(0, 5, n)
    site_outcome = np.select([site == "B", site == "C"], [1.5, 3.0], default=0.0)
    y0 = 38 + 0.48 * severity + 1.1 * comorbidity + site_outcome + shared_noise
    y1 = y0 - 6.0
    outcome = np.where(treatment == 1, y1, y0)
    early_response = severity - 4.0 * treatment + rng.normal(0, 4, n)
    missing_probability = 1 / (1 + np.exp(-(-2.0 + 0.025 * (age - 60) + 0.45 * (site == "C"))))
    missing = rng.binomial(1, missing_probability).astype(bool)
    observed_severity = severity.copy()
    observed_severity[missing] = np.nan
    return pd.DataFrame({
        "fixture_id": [f"SYNV{index:04d}" for index in range(1, n + 1)],
        "age": age.round(6), "baseline_severity": severity.round(6),
        "baseline_severity_observed": observed_severity.round(6),
        "baseline_severity_missing": missing.astype(int), "comorbidity_count": comorbidity,
        "site": site, "treatment": treatment, "assignment_probability_true": probability.round(8),
        "early_response_mediator": early_response.round(6), "outcome_30d": outcome.round(6),
        "true_y0": y0.round(6), "true_y1": y1.round(6), "true_individual_effect": np.repeat(-6.0, n),
        "synthetic": "yes",
    })


def propensity_pipeline(include_missing: bool = False) -> Pipeline:
    numeric = NUMERIC_CONFOUNDERS + (["severity_missing"] if include_missing else [])
    return Pipeline([
        ("preprocess", ColumnTransformer([
            ("numeric", StandardScaler(), numeric),
            ("categorical", OneHotEncoder(drop="first", handle_unknown="ignore", sparse_output=False), CATEGORICAL_CONFOUNDERS),
        ])),
        ("model", LogisticRegression(C=np.inf, solver="lbfgs", max_iter=10_000, random_state=SEED)),
    ])


def fit_propensity(frame: pd.DataFrame, severity: pd.Series, include_missing: bool = False) -> tuple[np.ndarray, np.ndarray, tuple[float, float]]:
    x = frame[["age", "comorbidity_count", "site"]].copy()
    x["baseline_severity"] = severity.to_numpy()
    if include_missing:
        x["severity_missing"] = frame["baseline_severity_missing"].to_numpy()
    probability = propensity_pipeline(include_missing).fit(x, frame["treatment"]).predict_proba(x)[:, 1]
    probability = np.clip(probability, 0.02, 0.98)
    weight = np.where(frame["treatment"].to_numpy() == 1, 1 / probability, 1 / (1 - probability))
    lower, upper = np.quantile(weight, [0.01, 0.99])
    return probability, np.clip(weight, lower, upper), (float(lower), float(upper))


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.sum(values * weights) / np.sum(weights))


def effect(frame: pd.DataFrame, weights: np.ndarray | None = None) -> float:
    treated = frame["treatment"].to_numpy() == 1
    y = frame["outcome_30d"].to_numpy()
    w = np.ones(len(frame)) if weights is None else weights
    return weighted_mean(y[treated], w[treated]) - weighted_mean(y[~treated], w[~treated])


def treatment_evidence(frame: pd.DataFrame) -> tuple[dict[str, object], dict[str, object]]:
    full_p, full_w, full_limits = fit_propensity(frame, frame["baseline_severity"])
    complete = frame.loc[frame["baseline_severity_observed"].notna()].copy()
    cc_p, cc_w, cc_limits = fit_propensity(complete, complete["baseline_severity_observed"])
    median = float(frame["baseline_severity_observed"].median())
    estimates = []

    def add(method: str, data: pd.DataFrame, estimate: float, note: str) -> None:
        estimates.append({"method": method, "rows": len(data), "treated": int(data["treatment"].sum()), "estimate_treated_minus_untreated": fixed(estimate), "target": "600-person synthetic ATE; lower outcome is better", "interpretation": note})

    add("known synthetic truth", frame, float((frame["true_y1"] - frame["true_y0"]).mean()), "generator audit only")
    add("unadjusted", frame, effect(frame), "confounded by treatment assignment")
    add("full-data IPTW audit", frame, effect(frame, full_w), "uses complete generated severity; not ordinarily observed")
    add("complete-case IPTW", complete, effect(complete, cc_w), "changes observed analysis rows")
    sensitivity = {}
    for label, delta in (("median plus indicator", 0.0), ("low delta", -6.0), ("high delta", 6.0)):
        imputed = frame["baseline_severity_observed"].fillna(median + delta)
        p, w, limits = fit_propensity(frame, imputed, include_missing=True)
        add(label, frame, effect(frame, w), f"missing severity set to observed median plus {delta:.1f}; missing indicator included")
        sensitivity[label] = {"probability": p, "weight": w, "limits": limits, "severity": imputed}
    return {
        "full_probability": full_p, "full_weight": full_w, "full_limits": full_limits,
        "complete": complete, "cc_probability": cc_p, "cc_weight": cc_w, "cc_limits": cc_limits,
        "median": median, "sensitivity": sensitivity,
    }, {"estimates": estimates}


def propensity_rows(frame: pd.DataFrame, evidence: dict[str, object]) -> list[dict[str, object]]:
    result = []
    probability = evidence["full_probability"]
    weights = evidence["full_weight"]
    for index, row in frame.iterrows():
        result.append({"fixture_id": row["fixture_id"], "treatment": int(row["treatment"]), "propensity": fixed(float(probability[index])), "ate_weight_truncated": fixed(float(weights[index])), "fit_fields": "age|baseline_severity|comorbidity_count|site", "fit_scope": "600-person full-data synthetic audit"})
    return result


def overlap_rows(frame: pd.DataFrame, evidence: dict[str, object]) -> list[dict[str, object]]:
    p = evidence["full_probability"]
    treated = frame["treatment"].to_numpy() == 1
    common_low = max(float(p[treated].min()), float(p[~treated].min()))
    common_high = min(float(p[treated].max()), float(p[~treated].max()))
    result = []
    for group, mask in (("untreated", ~treated), ("treated", treated)):
        result.append({"record_type": "group summary", "group": group, "bin": "all", "rows": int(mask.sum()), "minimum_propensity": fixed(float(p[mask].min())), "maximum_propensity": fixed(float(p[mask].max())), "common_support_low": fixed(common_low), "common_support_high": fixed(common_high), "outside_common_support": int(((p[mask] < common_low) | (p[mask] > common_high)).sum())})
    bins = np.linspace(0, 1, 11)
    for index in range(10):
        in_bin = (p >= bins[index]) & (p < bins[index + 1] if index < 9 else p <= bins[index + 1])
        for group, mask in (("untreated", ~treated), ("treated", treated)):
            result.append({"record_type": "score bin", "group": group, "bin": f"{bins[index]:.1f}-{bins[index + 1]:.1f}", "rows": int((in_bin & mask).sum()), "minimum_propensity": "", "maximum_propensity": "", "common_support_low": fixed(common_low), "common_support_high": fixed(common_high), "outside_common_support": ""})
    return result


def smd(x1: np.ndarray, x0: np.ndarray, w1: np.ndarray | None = None, w0: np.ndarray | None = None) -> tuple[float, float, float]:
    w1 = np.ones(len(x1)) if w1 is None else w1
    w0 = np.ones(len(x0)) if w0 is None else w0
    m1, m0 = weighted_mean(x1, w1), weighted_mean(x0, w0)
    v1 = weighted_mean((x1 - m1) ** 2, w1)
    v0 = weighted_mean((x0 - m0) ** 2, w0)
    denominator = math.sqrt((v1 + v0) / 2)
    return m1, m0, 0.0 if denominator == 0 else (m1 - m0) / denominator


def balance_rows(frame: pd.DataFrame, weights: np.ndarray) -> list[dict[str, object]]:
    treated = frame["treatment"].to_numpy() == 1
    features = {name: frame[name].to_numpy(dtype=float) for name in NUMERIC_CONFOUNDERS}
    for category in ("B", "C"):
        features[f"site_{category}"] = (frame["site"].to_numpy() == category).astype(float)
    result = []
    for name, values in features.items():
        pre1, pre0, pre = smd(values[treated], values[~treated])
        post1, post0, post = smd(values[treated], values[~treated], weights[treated], weights[~treated])
        result.append({"covariate": name, "treated_mean_unweighted": fixed(pre1), "untreated_mean_unweighted": fixed(pre0), "smd_unweighted": fixed(pre), "treated_mean_weighted": fixed(post1), "untreated_mean_weighted": fixed(post0), "smd_weighted": fixed(post), "absolute_weighted_smd_below_0_10": "yes" if abs(post) < 0.10 else "no"})
    return result


def selection_rows(cohort: pd.DataFrame, subset: pd.DataFrame) -> list[dict[str, object]]:
    selected = set(subset["model_row_id"])
    frame = cohort.copy()
    frame["selected_timing"] = frame["model_row_id"].isin(selected)
    result = []
    for field in ("age_at_index", "prior_365d_encounter_count", "prior_365d_acute_count", "prior_365d_condition_count", "prior_365d_medication_count", "acute_return_90d"):
        yes = frame.loc[frame["selected_timing"], field].astype(float)
        no = frame.loc[~frame["selected_timing"], field].astype(float)
        _, _, standardized = smd(yes.to_numpy(), no.to_numpy())
        result.append({"field": field, "selected_rows": len(yes), "nonselected_rows": len(no), "selected_mean": fixed(float(yes.mean())), "nonselected_mean": fixed(float(no.mean())), "standardized_difference": fixed(standardized), "boundary": "descriptive selection evidence; not a correction model"})
    for category in ("emergency", "inpatient"):
        values = (frame["index_class"] == category).astype(float)
        yes = values[frame["selected_timing"]].to_numpy()
        no = values[~frame["selected_timing"]].to_numpy()
        _, _, standardized = smd(yes, no)
        result.append({"field": f"index_class_{category}", "selected_rows": int(frame["selected_timing"].sum()), "nonselected_rows": int((~frame["selected_timing"]).sum()), "selected_mean": fixed(float(yes.mean())), "nonselected_mean": fixed(float(no.mean())), "standardized_difference": fixed(standardized), "boundary": "descriptive selection evidence; not a correction model"})
    return result


def missingness_rows(frame: pd.DataFrame) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    missing = int(frame["baseline_severity_observed"].isna().sum())
    profile = [
        {"field": "baseline_severity_observed", "rows": len(frame), "missing": missing, "percent_missing": fixed(missing / len(frame)), "timing": "pre-treatment measurement", "generator": "missing probability depends on observed age and site", "learner_boundary": "MAR is known from generator but remains an assumption in ordinary observed data"},
        {"field": "outcome_30d", "rows": len(frame), "missing": 0, "percent_missing": fixed(0), "timing": "post-treatment outcome", "generator": "complete synthetic outcome", "learner_boundary": "no outcome imputation in this exercise"},
    ]
    assumptions = [
        {"mechanism": "MCAR", "status": "not primary", "statement": "missingness independent of observed and unobserved severity", "testable_from_observed_data": "no", "sensitivity_action": "compare as conceptual alternative"},
        {"mechanism": "MAR", "status": "primary teaching assumption", "statement": "missingness independent of severity after observed age and site", "testable_from_observed_data": "no", "sensitivity_action": "median plus indicator bounded analysis"},
        {"mechanism": "MNAR", "status": "sensitivity", "statement": "missing severity differs after conditioning on observed age and site", "testable_from_observed_data": "no", "sensitivity_action": "low and high delta shifts"},
    ]
    return profile, assumptions


def repeated_fixture(frame: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    random_intercept = rng.normal(0, 6, len(frame))
    rows = []
    for index, person in frame.iterrows():
        for visit, week in enumerate((0, 4, 8, 12), start=1):
            outcome = 45 + 0.35 * person["baseline_severity"] + random_intercept[index] - 0.30 * week - 0.8 * person["treatment"] - 0.18 * person["treatment"] * week + rng.normal(0, 3)
            rows.append({"fixture_id": person["fixture_id"], "visit": visit, "week": week, "treatment": int(person["treatment"]), "outcome": round(float(outcome), 6), "cluster": person["fixture_id"], "synthetic": "yes"})
    return pd.DataFrame(rows)


def longitudinal_rows(repeated: pd.DataFrame) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    x = pd.DataFrame({"const": 1.0, "week": repeated["week"], "treatment": repeated["treatment"], "treatment_x_week": repeated["treatment"] * repeated["week"]})
    ols = sm.OLS(repeated["outcome"], x).fit()
    cluster = ols.get_robustcov_results(cov_type="cluster", groups=repeated["fixture_id"])
    mixed = sm.MixedLM(repeated["outcome"], x, groups=repeated["fixture_id"]).fit(reml=True, method="lbfgs", disp=False)
    result = []
    for method, fit, params, ses in (("naive OLS", ols, np.asarray(ols.params), np.asarray(ols.bse)), ("cluster-robust OLS", cluster, np.asarray(cluster.params), np.asarray(cluster.bse)), ("random-intercept mixed model", mixed, np.asarray(mixed.fe_params), np.asarray(mixed.bse_fe))):
        for index, term in enumerate(x.columns):
            result.append({"method": method, "term": term, "estimate": fixed(float(params[index])), "std_error": fixed(float(ses[index])), "lower95": fixed(float(params[index] - 1.96 * ses[index])), "upper95": fixed(float(params[index] + 1.96 * ses[index])), "rows": len(repeated), "clusters": repeated["fixture_id"].nunique(), "boundary": "synthetic reading exercise; not a clinical longitudinal effect"})
    random_variance = float(mixed.cov_re.iloc[0, 0])
    residual = float(mixed.scale)
    variance = [
        {"component": "person_random_intercept", "variance": fixed(random_variance), "interpretation": "between-person residual variance"},
        {"component": "residual", "variance": fixed(residual), "interpretation": "within-person residual variance"},
        {"component": "intraclass_correlation", "variance": fixed(random_variance / (random_variance + residual)), "interpretation": "share of residual variance attributable to person clustering"},
    ]
    return result, variance


def survival_fixture(frame: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    log_rate = -3.25 + 0.020 * (frame["baseline_severity"].to_numpy() - 50) + 0.10 * frame["comorbidity_count"].to_numpy() - 0.30 * frame["treatment"].to_numpy()
    event_time = rng.exponential(1 / np.exp(log_rate))
    censor_time = rng.uniform(18, 60, len(frame))
    observed = np.minimum(event_time, censor_time)
    event = (event_time <= censor_time).astype(int)
    return pd.DataFrame({"fixture_id": frame["fixture_id"], "treatment": frame["treatment"], "age": frame["age"], "baseline_severity": frame["baseline_severity"], "comorbidity_count": frame["comorbidity_count"], "event_time_true": event_time.round(6), "censor_time": censor_time.round(6), "observed_time": observed.round(6), "event": event, "synthetic": "yes"})


def km_at(frame: pd.DataFrame, time: float) -> tuple[int, int, int, float]:
    ordered = frame.sort_values("observed_time")
    survival = 1.0
    for event_time in sorted(ordered.loc[(ordered["event"] == 1) & (ordered["observed_time"] <= time), "observed_time"].unique()):
        at_risk = int((ordered["observed_time"] >= event_time).sum())
        events = int(((ordered["observed_time"] == event_time) & (ordered["event"] == 1)).sum())
        survival *= 1 - events / at_risk
    return int((ordered["observed_time"] >= time).sum()), int(((ordered["event"] == 1) & (ordered["observed_time"] <= time)).sum()), int(((ordered["event"] == 0) & (ordered["observed_time"] <= time)).sum()), survival


def survival_rows(frame: pd.DataFrame) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    km = []
    for group, rows in frame.groupby("treatment"):
        for time in (0, 13, 26, 39, 52):
            at_risk, events, censored, survival = km_at(rows, time)
            km.append({"treatment": int(group), "week": time, "rows": len(rows), "at_risk": at_risk, "cumulative_events": events, "cumulative_censored": censored, "km_event_free_probability": fixed(survival), "boundary": "synthetic event-free teaching estimate"})
    exog = pd.DataFrame({"treatment": frame["treatment"], "age_decade": (frame["age"] - frame["age"].mean()) / 10, "severity_10": (frame["baseline_severity"] - frame["baseline_severity"].mean()) / 10, "comorbidity_count": frame["comorbidity_count"]})
    fit = PHReg(frame["observed_time"], exog, status=frame["event"], ties="efron").fit()
    interval = fit.conf_int()
    cox = []
    for index, term in enumerate(exog.columns):
        estimate = float(fit.params[index])
        cox.append({"term": term, "log_hazard_estimate": fixed(estimate), "hazard_ratio": fixed(math.exp(estimate)), "std_error": fixed(float(fit.bse[index])), "hr_lower95": fixed(math.exp(float(interval[index, 0]))), "hr_upper95": fixed(math.exp(float(interval[index, 1]))), "events": int(frame["event"].sum()), "censored": int((1 - frame["event"]).sum()), "boundary": "conditional hazard ratio in synthetic fixture; not risk ratio or causal effect"})
    return km, cox


def dag_nodes() -> list[dict[str, object]]:
    return [
        {"node_id": "A", "label": "Age", "role": "confounder", "timing": "pre-exposure"},
        {"node_id": "S", "label": "Baseline severity", "role": "confounder", "timing": "pre-exposure"},
        {"node_id": "C", "label": "Comorbidity count", "role": "confounder", "timing": "pre-exposure"},
        {"node_id": "H", "label": "Site", "role": "confounder/proxy", "timing": "pre-exposure"},
        {"node_id": "U", "label": "Clinical preference", "role": "unmeasured confounder", "timing": "pre-exposure"},
        {"node_id": "T", "label": "Treatment", "role": "exposure", "timing": "time zero"},
        {"node_id": "M", "label": "Early response", "role": "mediator", "timing": "post-exposure"},
        {"node_id": "Y", "label": "30-day symptom score", "role": "outcome", "timing": "post-exposure"},
        {"node_id": "R", "label": "Complete severity record", "role": "selection/collider", "timing": "analysis selection"},
    ]


def dag_edges() -> list[dict[str, object]]:
    edges = [("A", "S"), ("A", "T"), ("A", "Y"), ("C", "S"), ("C", "T"), ("C", "Y"), ("H", "S"), ("H", "T"), ("H", "Y"), ("S", "T"), ("S", "Y"), ("U", "T"), ("U", "Y"), ("T", "M"), ("M", "Y"), ("T", "Y"), ("A", "R"), ("H", "R")]
    return [{"edge_id": f"E{index:02d}", "from": source, "to": target, "meaning": "directed teaching assumption", "adjustment_implication": "do not adjust for mediator M; R is selection, not a baseline confounder"} for index, (source, target) in enumerate(edges, start=1)]


def validity_map_rows() -> list[dict[str, object]]:
    return [
        {"aim_id": "V01", "aim_class": "conditional description", "unit": "person with recorded next encounter", "time_zero": "index stop", "exposure_or_predictor": "declared LIN01 fields", "outcome": "days to recorded encounter", "population": "111 recorded timing rows", "supported_claim": "conditional mean association", "prohibited_claim": "full-cohort time to event"},
        {"aim_id": "V02", "aim_class": "prediction", "unit": "selected index per person", "time_zero": "index stop", "exposure_or_predictor": "pre-index and index-time fields", "outcome": "90-day acute return", "population": "374-person synthetic cohort", "supported_claim": "locked teaching prediction evidence", "prohibited_claim": "causal or deployment effect"},
        {"aim_id": "V03", "aim_class": "causal teaching contrast", "unit": "synthetic fixture person", "time_zero": "synthetic treatment assignment", "exposure_or_predictor": "treatment", "outcome": "30-day symptom score", "population": "600 generated people", "supported_claim": "method recovery against known synthetic truth", "prohibited_claim": "real treatment effectiveness"},
        {"aim_id": "V04", "aim_class": "longitudinal reading", "unit": "person-visit", "time_zero": "visit week 0", "exposure_or_predictor": "treatment and week", "outcome": "repeated symptom score", "population": "600 generated people at four visits", "supported_claim": "dependence-aware method reading", "prohibited_claim": "clinical longitudinal effect"},
        {"aim_id": "V05", "aim_class": "survival reading", "unit": "synthetic fixture person", "time_zero": "synthetic treatment assignment", "exposure_or_predictor": "treatment and baseline covariates", "outcome": "generated event time", "population": "600 generated people", "supported_claim": "KM and Cox quantity reading", "prohibited_claim": "clinical survival or causal effect"},
    ]


def threat_rows() -> list[dict[str, object]]:
    threats = [
        ("T01", "misaligned aim", "design", "claim", "narrow or stop"),
        ("T02", "post-index leakage", "measurement", "validity", "exclude and return"),
        ("T03", "unmeasured confounding", "design", "causal contrast", "refer"),
        ("T04", "collider adjustment", "analysis", "causal contrast", "remove or redefine"),
        ("T05", "poor propensity overlap", "analysis", "target population", "restrict or refer"),
        ("T06", "selected timing subset", "eligibility", "generalizability", "conditional claim or survival method"),
        ("T07", "structural blank as zero", "data", "outcome meaning", "stop and restore"),
        ("T08", "MAR assumption", "missingness", "adjusted estimate", "sensitivity and refer"),
        ("T09", "MNAR sensitivity", "missingness", "decision stability", "delta analysis"),
        ("T10", "within-person dependence", "analysis", "uncertainty", "cluster or mixed method"),
        ("T11", "censoring", "follow-up", "survival quantity", "KM/Cox and assumptions"),
        ("T12", "synthetic transport", "interpretation", "external validity", "teaching-only stop boundary"),
    ]
    return [{"threat_id": i, "threat": name, "design_stage": stage, "affected_claim": claim, "reference_action": action, "status": "material", "specialist_trigger": "yes" if action == "refer" or "refer" in action else "conditional", "module_05_implication": "carry boundary; forecast uses a distinct public time series"} for i, name, stage, claim, action in threats]


def svg_dag(nodes: list[dict[str, object]], edges: list[dict[str, object]]) -> str:
    positions = {"A": (80, 80), "C": (80, 180), "H": (80, 280), "S": (250, 140), "U": (250, 300), "T": (430, 180), "M": (590, 100), "Y": (750, 180), "R": (430, 320)}
    arrows = "".join(f'<line x1="{positions[e["from"]][0]}" y1="{positions[e["from"]][1]}" x2="{positions[e["to"]][0]}" y2="{positions[e["to"]][1]}" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>' for e in edges)
    boxes = "".join(f'<g><circle cx="{positions[n["node_id"]][0]}" cy="{positions[n["node_id"]][1]}" r="34" fill="#e0f2fe" stroke="#1f49b6" stroke-width="2"/><text x="{positions[n["node_id"]][0]}" y="{positions[n["node_id"]][1] + 5}" text-anchor="middle" font-size="14">{n["node_id"]}</text></g>' for n in nodes)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="410" viewBox="0 0 860 410" role="img" aria-labelledby="title desc"><title id="title">Synthetic treatment teaching DAG</title><desc id="desc">Directed graph with pre-exposure age, severity, comorbidity, site, and unmeasured preference; treatment exposure; early-response mediator; 30-day outcome; and complete-record selection. Exact nodes and edges are available in CSV files and dag.mmd.</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#64748b"/></marker></defs><rect width="860" height="410" fill="white"/>{arrows}{boxes}<text x="20" y="390" font-size="14">A age; C comorbidity; H site; S severity; U preference; T treatment; M mediator; Y outcome; R complete record</text></svg>\n'''


def check_rows(cohort, subset, treatment, repeated, survival, balance, estimates, profile, threats, nodes, edges) -> list[dict[str, object]]:
    selected = next(row for row in estimates if row["method"] == "known synthetic truth")
    checks = (
        ("CHK01", "cohort rows", len(cohort), 374), ("CHK02", "timing subset rows", len(subset), 111),
        ("CHK03", "structural blanks", int(cohort["next_30d_days_after_index_stop"].isna().sum()), 263),
        ("CHK04", "treatment fixture rows", len(treatment), 600), ("CHK05", "known effect", selected["estimate_treated_minus_untreated"], "-6.00000000"),
        ("CHK06", "missing severity rows", int(treatment["baseline_severity_missing"].sum()), int(profile[0]["missing"])),
        ("CHK07", "balance covariates", len(balance), 5), ("CHK08", "effect methods", len(estimates), 7),
        ("CHK09", "repeated rows", len(repeated), 2400), ("CHK10", "repeated people", repeated["fixture_id"].nunique(), 600),
        ("CHK11", "visits per person", repeated.groupby("fixture_id").size().nunique(), 1),
        ("CHK12", "survival rows", len(survival), 600), ("CHK13", "survival conserved", int(survival["event"].sum() + (1 - survival["event"]).sum()), 600),
        ("CHK14", "threat rows", len(threats), 12), ("CHK15", "dag nodes", len(nodes), 9), ("CHK16", "dag edges", len(edges), 18),
    )
    return [{"check_id": i, "check": label, "observed": observed, "expected": expected, "status": "pass" if observed == expected else "fail"} for i, label, observed, expected in checks]


def build_outputs(paths: dict[str, Path], target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_upstream(paths)
    rng = np.random.default_rng(SEED)
    cohort = pd.read_csv(paths["modeling-cohort.csv"])
    subset = pd.read_csv(paths["linear-subset-registry.csv"])
    treatment = generate_treatment(rng)
    evidence, effect_evidence = treatment_evidence(treatment)
    propensity = propensity_rows(treatment, evidence)
    overlap = overlap_rows(treatment, evidence)
    balance = balance_rows(treatment, evidence["full_weight"])
    selection = selection_rows(cohort, subset)
    missingness, mechanisms = missingness_rows(treatment)
    repeated = repeated_fixture(treatment, rng)
    longitudinal, variance = longitudinal_rows(repeated)
    survival = survival_fixture(treatment, rng)
    km, cox = survival_rows(survival)
    nodes, edges = dag_nodes(), dag_edges()
    threats = threat_rows()
    outputs: dict[str, object] = {
        "treatment-fixture.csv": treatment.to_dict("records"),
        "repeated-measures-fixture.csv": repeated.to_dict("records"),
        "survival-fixture.csv": survival.to_dict("records"),
        "analytic-aim-validity-map.csv": validity_map_rows(), "dag-nodes.csv": nodes,
        "dag-edges.csv": edges, "propensity-predictions.csv": propensity,
        "overlap-table.csv": overlap, "balance-table.csv": balance,
        "adjustment-estimates.csv": effect_evidence["estimates"], "selection-profile.csv": selection,
        "missingness-profile.csv": missingness, "missingness-mechanisms.csv": mechanisms,
        "longitudinal-models.csv": longitudinal, "mixed-variance.csv": variance,
        "kaplan-meier-table.csv": km, "cox-reading.csv": cox,
        "validity-threat-register.csv": threats,
    }
    outputs["validity-checks.csv"] = check_rows(cohort, subset, treatment, repeated, survival, balance, effect_evidence["estimates"], missingness, threats, nodes, edges)
    failed = [row for row in outputs["validity-checks.csv"] if row["status"] != "pass"]
    if failed:
        raise ValueError(f"Validity release checks failed: {failed}")
    target.mkdir(parents=True)
    report: dict[str, object] = {
        "status": "pass", "version": "0.1.0", "seed": SEED,
        "upstream": {name: {"bytes": path.stat().st_size, "sha256": sha256(path)} for name, path in paths.items()},
        "selection_case": {"cohort_rows": len(cohort), "timing_rows": len(subset), "structural_blanks": int(cohort["next_30d_days_after_index_stop"].isna().sum())},
        "treatment_case": {"rows": len(treatment), "treated": int(treatment["treatment"].sum()), "missing_severity": int(treatment["baseline_severity_missing"].sum()), "known_ate": "-6.00000000"},
        "repeated_case": {"rows": len(repeated), "people": repeated["fixture_id"].nunique(), "visits_per_person": 4},
        "survival_case": {"rows": len(survival), "events": int(survival["event"].sum()), "censored": int((1 - survival["event"]).sum())},
        "outputs": {}, "decision": {"reference": "continue with conditions", "module_05": "allowed with recorded conditions", "use": "synthetic teaching only"},
    }
    for name, rows in outputs.items():
        path = target / name
        write_csv(path, rows)
        report["outputs"][name] = {"rows": len(rows), "fields": len(rows[0]), "bytes": path.stat().st_size, "sha256": sha256(path)}
    dag_path = target / "dag.svg"
    dag_path.write_text(svg_dag(nodes, edges), encoding="utf-8", newline="")
    report["outputs"]["dag.svg"] = {"bytes": dag_path.stat().st_size, "sha256": sha256(dag_path)}
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
    shutil.copy2(MODULE_ROOT / "validate_validity_evidence.py", target / "validate_validity_evidence.py")
    data = target / "data"
    data.mkdir()
    for name, path in paths.items():
        shutil.copy2(path, data / name)
    return build_outputs(upstream_paths(data), target / "outputs")


def self_check() -> None:
    paths = upstream_paths()
    with tempfile.TemporaryDirectory(prefix="fnd2-module04-build-") as temp_dir:
        root = Path(temp_dir)
        first = root / "outputs"
        report = build_outputs(paths, first)
        assert report["treatment_case"]["rows"] == 600 and report["repeated_case"]["rows"] == 2400
        try:
            build_outputs(paths, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not refuse existing target")
        workspace = root / "learner"
        workspace_report = build_workspace(paths, workspace)
        reproduced = workspace / "reproduced-outputs"
        reproduced_report = build_outputs(upstream_paths(workspace / "data"), reproduced)
        assert workspace_report["outputs"] == reproduced_report["outputs"]
    print("FND-2 Module 04 builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path)
    parser.add_argument("--build-reference", action="store_true")
    parser.add_argument("--outputs-only", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if args.build_reference:
        print(json.dumps(build_outputs(upstream_paths(), MODULE_ROOT / "outputs"), indent=2))
        return
    if args.target is None:
        parser.error("target is required unless --self-check or --build-reference is used")
    report = build_outputs(upstream_paths(), args.target.resolve()) if args.outputs_only else build_workspace(upstream_paths(), args.target.resolve())
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
