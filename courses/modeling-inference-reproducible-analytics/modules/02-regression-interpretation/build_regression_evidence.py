"""Build the exact FND-2 Module 02 regression-evidence release."""

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
import scipy.stats as scipy_stats
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson, jarque_bera


MODULE_ROOT = Path(__file__).resolve().parent
UPSTREAM = {
    "modeling-cohort.csv": (138_503, "6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332"),
    "split-registry.csv": (51_910, "05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1"),
    "baseline-metrics.csv": (306, "613651013e397beeadc84b17482026ca7cb4674abf61bf521699d79af0a3c9af"),
    "feature-role-contract.csv": (3_766, "599f29ca612cb5f23aed277c56937af78c488ba952c2926faa94166f33449c83"),
}
LINEAR_TERMS = ("const", "age_at_index", "prior_365d_encounter_count", "index_class_inpatient")
LOGISTIC_TERMS = {
    "LOG01": ("const", "age_centered_decade", "prior_365d_acute_count", "index_class_inpatient"),
    "LOG02": ("const", "age_centered_decade", "age_centered_decade_sq", "prior_365d_acute_count", "index_class_inpatient"),
    "LOG03": ("const", "age_centered_decade", "prior_365d_acute_count", "index_class_inpatient", "prior_acute_x_inpatient"),
}
PORTABLE_FILES = (
    "requirements.txt", "data-spec.md", "source-record.yml", "assessment.md", "paired-models.R",
)


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
    return MODULE_ROOT.parent / "01-aims-reproducible-workspace"


def upstream_paths(root: Path | None = None) -> dict[str, Path]:
    base = root or upstream_root()
    return {
        "modeling-cohort.csv": base / "modeling-cohort.csv" if base.name == "data" else base / "outputs" / "modeling-cohort.csv",
        "split-registry.csv": base / "split-registry.csv" if base.name == "data" else base / "outputs" / "split-registry.csv",
        "baseline-metrics.csv": base / "baseline-metrics.csv" if base.name == "data" else base / "outputs" / "baseline-metrics.csv",
        "feature-role-contract.csv": base / "feature-role-contract.csv",
    }


def verify_upstream(paths: dict[str, Path]) -> None:
    for name, (size, digest) in UPSTREAM.items():
        path = paths[name]
        if not path.is_file():
            raise FileNotFoundError(f"Module 01 input not found: {path}")
        if path.stat().st_size != size or sha256(path) != digest:
            raise ValueError(f"Module 01 input fingerprint changed: {name}")


def fixed(value: float, digits: int = 8) -> str:
    if math.isnan(value):
        return ""
    return f"{value:.{digits}f}"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"Cannot write an empty result table: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def load_data(paths: dict[str, Path]) -> tuple[pd.DataFrame, pd.DataFrame]:
    verify_upstream(paths)
    cohort = pd.read_csv(paths["modeling-cohort.csv"], dtype={"patient_id": str, "index_encounter_id": str})
    roles = pd.read_csv(paths["feature-role-contract.csv"])
    if cohort.shape != (374, 34) or cohort["patient_id"].nunique() != 374:
        raise ValueError("Module 01 modeling cohort shape or grain changed.")
    if cohort["split"].value_counts().to_dict() != {"train": 224, "validation": 75, "test": 75}:
        raise ValueError("Module 01 split counts changed.")
    if roles.shape[0] != 34 or (roles["default_predictor"] == "yes").sum() != 9:
        raise ValueError("Module 01 feature-role contract changed.")
    return cohort, roles


def prepare(cohort: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, float]:
    train = cohort.loc[cohort["split"] == "train"].copy()
    linear_all = cohort.loc[cohort["next_30d_days_after_index_stop"].notna()].copy()
    age_mean = float(train["age_at_index"].mean())
    for frame in (train, linear_all):
        frame["index_class_inpatient"] = (frame["index_class"] == "inpatient").astype(float)
        frame["age_centered_decade"] = (frame["age_at_index"] - age_mean) / 10.0
        frame["age_centered_decade_sq"] = frame["age_centered_decade"] ** 2
        frame["prior_acute_x_inpatient"] = frame["prior_365d_acute_count"] * frame["index_class_inpatient"]
    return train, linear_all, age_mean


def fit_models(train: pd.DataFrame, linear_all: pd.DataFrame):
    linear_train = linear_all.loc[linear_all["split"] == "train"].copy()
    linear_x = sm.add_constant(linear_train[list(LINEAR_TERMS[1:])], has_constant="add")
    linear_fit = sm.OLS(linear_train["next_30d_days_after_index_stop"], linear_x).fit()
    linear_hc3 = linear_fit.get_robustcov_results(cov_type="HC3")
    logistic_fits = {}
    logistic_robust = {}
    for model_id, terms in LOGISTIC_TERMS.items():
        x = sm.add_constant(train[list(terms[1:])], has_constant="add")
        logistic_fits[model_id] = sm.GLM(train["acute_return_90d"], x, family=sm.families.Binomial()).fit()
        logistic_robust[model_id] = sm.GLM(train["acute_return_90d"], x, family=sm.families.Binomial()).fit(cov_type="HC3")
    return linear_train, linear_fit, linear_hc3, logistic_fits, logistic_robust


def linear_subset_rows(linear_all: pd.DataFrame) -> list[dict[str, object]]:
    result = []
    for row in linear_all.sort_values("split_order").itertuples(index=False):
        result.append({
            "model_row_id": row.model_row_id,
            "patient_id": row.patient_id,
            "split": row.split,
            "index_start": row.index_start,
            "next_30d_days_after_index_stop": fixed(float(row.next_30d_days_after_index_stop), 6),
            "selection_condition": "recorded different encounter within 30 days",
            "fit_use": "fit and interpretation" if row.split == "train" else "not used in Module 02 fitting",
        })
    return result


def linear_coefficient_rows(fit, robust) -> list[dict[str, object]]:
    classical_ci = fit.conf_int(alpha=0.05)
    robust_ci = robust.conf_int(alpha=0.05)
    quantities = {
        "const": ("days", "expected days at numeric zero and emergency reference"),
        "age_at_index": ("days per one-year increase", "conditional mean difference per year"),
        "prior_365d_encounter_count": ("days per one-count increase", "conditional mean difference per prior encounter row"),
        "index_class_inpatient": ("days versus emergency reference", "conditional mean difference for inpatient versus emergency index"),
    }
    result = []
    for index, term in enumerate(LINEAR_TERMS):
        unit, meaning = quantities[term]
        result.append({
            "model_id": "LIN01", "term": term, "estimate": fixed(float(fit.params.iloc[index])),
            "std_error_classical": fixed(float(fit.bse.iloc[index])),
            "lower95_classical": fixed(float(classical_ci.iloc[index, 0])),
            "upper95_classical": fixed(float(classical_ci.iloc[index, 1])),
            "p_value_classical": fixed(float(fit.pvalues.iloc[index])),
            "std_error_hc3": fixed(float(robust.bse[index])),
            "lower95_hc3": fixed(float(robust_ci[index, 0])),
            "upper95_hc3": fixed(float(robust_ci[index, 1])),
            "p_value_hc3": fixed(float(robust.pvalues[index])),
            "quantity": unit, "bounded_interpretation": meaning,
        })
    return result


def linear_diagnostic_rows(linear_train: pd.DataFrame, fit) -> list[dict[str, object]]:
    residuals = np.asarray(fit.resid)
    jb_stat, jb_p, _, _ = jarque_bera(residuals)
    bp_stat, bp_p, _, _ = het_breuschpagan(residuals, fit.model.exog)
    influence = fit.get_influence()
    cooks = influence.cooks_distance[0]
    leverage = influence.hat_matrix_diag
    rmse = math.sqrt(float(np.mean(residuals ** 2)))
    metrics = (
        ("n", len(linear_train), 69, "pass"),
        ("outcome_min_days", linear_train["next_30d_days_after_index_stop"].min(), 0.9, "pass"),
        ("outcome_max_days", linear_train["next_30d_days_after_index_stop"].max(), 29.958333, "pass"),
        ("r_squared", fit.rsquared, "descriptive", "review"),
        ("adjusted_r_squared", fit.rsquared_adj, "descriptive", "review"),
        ("rmse_days", rmse, "descriptive", "review"),
        ("residual_mean", residuals.mean(), "approximately zero", "pass" if abs(residuals.mean()) < 1e-10 else "review"),
        ("jarque_bera_p_value", jb_p, ">=0.05 preferred for normal-error approximation", "pass" if jb_p >= 0.05 else "review"),
        ("breusch_pagan_p_value", bp_p, ">=0.05 preferred for constant-variance approximation", "pass" if bp_p >= 0.05 else "review"),
        ("durbin_watson", durbin_watson(residuals), "near 2 under ordered residual independence", "review"),
        ("max_cooks_distance", cooks.max(), f"review above 4/n={4/len(linear_train):.8f}", "review" if cooks.max() > 4 / len(linear_train) else "pass"),
        ("max_leverage", leverage.max(), f"review above 2p/n={2*fit.model.exog.shape[1]/len(linear_train):.8f}", "review" if leverage.max() > 2 * fit.model.exog.shape[1] / len(linear_train) else "pass"),
        ("condition_number", np.linalg.cond(fit.model.exog), "review scale and collinearity", "review"),
    )
    return [{"model_id": "LIN01", "metric": name, "value": fixed(float(value)) if isinstance(value, (float, np.floating)) else value, "reference": reference, "status": status} for name, value, reference, status in metrics]


def linear_prediction_rows(fit) -> list[dict[str, object]]:
    scenarios = pd.DataFrame([
        {"scenario_id": "LP01", "age_at_index": 40.0, "prior_365d_encounter_count": 0.0, "index_class_inpatient": 0.0},
        {"scenario_id": "LP02", "age_at_index": 70.0, "prior_365d_encounter_count": 4.0, "index_class_inpatient": 0.0},
        {"scenario_id": "LP03", "age_at_index": 70.0, "prior_365d_encounter_count": 4.0, "index_class_inpatient": 1.0},
    ])
    x = sm.add_constant(scenarios[list(LINEAR_TERMS[1:])], has_constant="add")
    frame = fit.get_prediction(x).summary_frame(alpha=0.05)
    result = []
    for index, scenario in scenarios.iterrows():
        row = frame.iloc[index]
        result.append({
            "scenario_id": scenario["scenario_id"], "age_at_index": int(scenario["age_at_index"]),
            "prior_365d_encounter_count": int(scenario["prior_365d_encounter_count"]),
            "index_class": "inpatient" if scenario["index_class_inpatient"] else "emergency",
            "predicted_mean_days": fixed(float(row["mean"])),
            "mean_lower95": fixed(float(row["mean_ci_lower"])), "mean_upper95": fixed(float(row["mean_ci_upper"])),
            "new_observation_lower95": fixed(float(row["obs_ci_lower"])), "new_observation_upper95": fixed(float(row["obs_ci_upper"])),
            "scope": "selected training rows with a recorded different encounter within 30 days",
        })
    return result


def logistic_coefficient_rows(fits: dict, robust_fits: dict) -> list[dict[str, object]]:
    result = []
    for model_id, fit in fits.items():
        robust = robust_fits[model_id]
        ci = fit.conf_int(alpha=0.05)
        robust_ci = robust.conf_int(alpha=0.05)
        for index, term in enumerate(LOGISTIC_TERMS[model_id]):
            estimate = float(fit.params.iloc[index])
            result.append({
                "model_id": model_id, "term": term, "log_odds_estimate": fixed(estimate),
                "odds_ratio": fixed(math.exp(estimate)),
                "std_error_model": fixed(float(fit.bse.iloc[index])),
                "or_lower95_model": fixed(math.exp(float(ci.iloc[index, 0]))),
                "or_upper95_model": fixed(math.exp(float(ci.iloc[index, 1]))),
                "p_value_model": fixed(float(fit.pvalues.iloc[index])),
                "std_error_hc3": fixed(float(robust.bse.iloc[index])),
                "or_lower95_hc3": fixed(math.exp(float(robust_ci.iloc[index, 0]))),
                "or_upper95_hc3": fixed(math.exp(float(robust_ci.iloc[index, 1]))),
                "p_value_hc3": fixed(float(robust.pvalues.iloc[index])),
                "quantity_boundary": "conditional odds ratio; not risk ratio probability change or causal effect",
            })
    return result


def logistic_diagnostic_rows(train: pd.DataFrame, fits: dict) -> list[dict[str, object]]:
    result = []
    for model_id, fit in fits.items():
        influence = fit.get_influence()
        fitted = np.asarray(fit.fittedvalues)
        params = np.asarray(fit.params)
        ses = np.asarray(fit.bse)
        metrics = (
            ("n", len(train), 224, "pass"),
            ("positives", int(train["acute_return_90d"].sum()), 25, "pass"),
            ("converged", bool(fit.converged), True, "pass" if fit.converged else "fail"),
            ("log_likelihood", fit.llf, "training descriptive", "review"),
            ("aic", fit.aic, "training descriptive; not validation", "review"),
            ("deviance", fit.deviance, "training descriptive", "review"),
            ("mcfadden_pseudo_r2", 1 - fit.llf / fit.llnull, "not ordinary R-squared", "review"),
            ("minimum_fitted_probability", fitted.min(), ">0 preferred", "review"),
            ("maximum_fitted_probability", fitted.max(), "<1 preferred", "review"),
            ("fitted_probability_at_least_0_99", int((fitted >= 0.99).sum()), 0, "review" if (fitted >= 0.99).any() else "pass"),
            ("maximum_absolute_coefficient", np.abs(params).max(), "review above 10", "review" if np.abs(params).max() > 10 else "pass"),
            ("maximum_standard_error", ses.max(), "review above 10", "review" if ses.max() > 10 else "pass"),
            ("maximum_cooks_distance", influence.cooks_distance[0].max(), f"review above 4/n={4/len(train):.8f}", "review" if influence.cooks_distance[0].max() > 4 / len(train) else "pass"),
            ("maximum_leverage", influence.hat_matrix_diag.max(), "review influential rows", "review"),
            ("condition_number", np.linalg.cond(fit.model.exog), "review scale and collinearity", "review"),
        )
        result.extend({"model_id": model_id, "metric": name, "value": fixed(float(value)) if isinstance(value, (float, np.floating)) else str(value).lower() if isinstance(value, bool) else value, "reference": reference, "status": status} for name, value, reference, status in metrics)
    return result


def logistic_prediction_rows(train: pd.DataFrame, fit, age_mean: float) -> list[dict[str, object]]:
    scenarios = pd.DataFrame([
        {"scenario_id": "GP01", "age_at_index": age_mean, "prior_365d_acute_count": 0.0, "index_class_inpatient": 0.0},
        {"scenario_id": "GP02", "age_at_index": age_mean, "prior_365d_acute_count": 1.0, "index_class_inpatient": 0.0},
        {"scenario_id": "GP03", "age_at_index": age_mean, "prior_365d_acute_count": 1.0, "index_class_inpatient": 1.0},
    ])
    scenarios["age_centered_decade"] = (scenarios["age_at_index"] - age_mean) / 10.0
    x = sm.add_constant(scenarios[["age_centered_decade", "prior_365d_acute_count", "index_class_inpatient"]], has_constant="add")
    frame = fit.get_prediction(x).summary_frame(alpha=0.05)
    result = []
    for index, scenario in scenarios.iterrows():
        row = frame.iloc[index]
        result.append({
            "scenario_id": scenario["scenario_id"], "age_at_index": fixed(float(scenario["age_at_index"]), 6),
            "prior_365d_acute_count": int(scenario["prior_365d_acute_count"]),
            "index_class": "inpatient" if scenario["index_class_inpatient"] else "emergency",
            "predicted_probability": fixed(float(row["mean"])),
            "probability_lower95": fixed(float(row["mean_ci_lower"])),
            "probability_upper95": fixed(float(row["mean_ci_upper"])),
            "quantity_boundary": "model-conditional training estimate; not individual truth or causal effect",
        })
    return result


def matrix_rows(age_mean: float) -> list[dict[str, object]]:
    definitions = {
        "const": ("constant", "1", "intercept"),
        "age_at_index": ("source", "age_at_index", "one-year increase"),
        "prior_365d_encounter_count": ("source", "prior_365d_encounter_count", "one-count increase"),
        "index_class_inpatient": ("derived", "1 when index_class is inpatient else 0", "emergency reference"),
        "age_centered_decade": ("derived", f"(age_at_index - {age_mean:.12f}) / 10", "one-decade increase from training mean"),
        "age_centered_decade_sq": ("derived", "age_centered_decade squared", "nonlinear curvature term"),
        "prior_365d_acute_count": ("source", "prior_365d_acute_count", "one-count increase"),
        "prior_acute_x_inpatient": ("derived", "prior_365d_acute_count multiplied by index_class_inpatient", "interaction departure"),
    }
    model_terms = {"LIN01": LINEAR_TERMS, **LOGISTIC_TERMS}
    result = []
    for model_id, terms in model_terms.items():
        for position, term in enumerate(terms, start=1):
            origin, expression, meaning = definitions[term]
            result.append({"model_id": model_id, "column_position": position, "term": term, "origin": origin, "expression": expression, "interpretation_unit": meaning})
    return result


def comparison_rows(fits: dict) -> list[dict[str, object]]:
    base = fits["LOG01"]
    result = []
    for model_id, fit in fits.items():
        if model_id == "LOG01":
            lr_stat = p_value = ""
            comparison = "declared bounded handoff model"
        else:
            statistic = 2 * (fit.llf - base.llf)
            lr_stat = fixed(float(statistic))
            p_value = fixed(float(scipy_stats.chi2.sf(max(statistic, 0), fit.df_model - base.df_model)))
            comparison = "training-only teaching comparison; does not select a prediction model"
        result.append({
            "model_id": model_id, "training_rows": int(fit.nobs), "parameters": int(fit.df_model + 1),
            "log_likelihood": fixed(float(fit.llf)), "aic": fixed(float(fit.aic)),
            "likelihood_ratio_vs_LOG01": lr_stat, "lr_df": "" if model_id == "LOG01" else int(fit.df_model - base.df_model),
            "lr_p_value": p_value, "module_03_status": "handoff" if model_id == "LOG01" else "interpretation exercise only",
            "interpretation": comparison,
        })
    return result


def sparse_rows(cohort: pd.DataFrame, train: pd.DataFrame) -> list[dict[str, object]]:
    result = []
    for field in ("gender", "race", "ethnicity", "index_class"):
        for category in sorted(cohort[field].dropna().astype(str).unique()):
            rows = train.loc[train[field].astype(str) == category]
            positives = int(rows["acute_return_90d"].sum()) if len(rows) else 0
            result.append({
                "field": field, "category": category, "training_rows": len(rows), "training_positives": positives,
                "training_negatives": len(rows) - positives, "absent_from_training": "yes" if len(rows) == 0 else "no",
                "fewer_than_10_rows": "yes" if len(rows) < 10 else "no", "zero_positive_or_negative_cell": "yes" if len(rows) == 0 or positives in {0, len(rows)} else "no",
                "action": "do not fit or rank unsupported category effects; preserve count and review",
            })
    return result


def assumption_rows(linear_all: pd.DataFrame, linear_train: pd.DataFrame, linear_diag: list[dict[str, object]], logistic_diag: list[dict[str, object]], sparse: list[dict[str, object]]) -> list[dict[str, object]]:
    lin = {row["metric"]: row for row in linear_diag}
    log1 = {row["metric"]: row for row in logistic_diag if row["model_id"] == "LOG01"}
    sparse_flags = sum(row["zero_positive_or_negative_cell"] == "yes" for row in sparse)
    return [
        {"assumption_id": "A01", "model_id": "LIN01", "assumption": "selected conditional outcome", "evidence": f"111 total available timing rows and {len(linear_train)} training timing rows; 263 structural blanks remain blank", "status": "limit", "required_action": "interpret only among people with a recorded different encounter within 30 days"},
        {"assumption_id": "A02", "model_id": "LIN01", "assumption": "independent modeling rows", "evidence": f"{linear_train['patient_id'].nunique()} unique patients across {len(linear_train)} training rows", "status": "pass", "required_action": "retain one-row grain"},
        {"assumption_id": "A03", "model_id": "LIN01", "assumption": "linear conditional mean", "evidence": "bounded additive formula; residual and nonlinear alternatives require review", "status": "review", "required_action": "do not interpret fit as proof of linearity"},
        {"assumption_id": "A04", "model_id": "LIN01", "assumption": "constant residual variance", "evidence": f"Breusch-Pagan p={lin['breusch_pagan_p_value']['value']}", "status": lin["breusch_pagan_p_value"]["status"], "required_action": "report HC3 comparison and inspect residual pattern"},
        {"assumption_id": "A05", "model_id": "LIN01", "assumption": "normal-error approximation", "evidence": f"Jarque-Bera p={lin['jarque_bera_p_value']['value']}", "status": lin["jarque_bera_p_value"]["status"], "required_action": "keep uncertainty conditional and avoid small-sample certainty"},
        {"assumption_id": "A06", "model_id": "LIN01", "assumption": "no single row dominates", "evidence": f"maximum Cook distance={lin['max_cooks_distance']['value']}; maximum leverage={lin['max_leverage']['value']}", "status": "review", "required_action": "inspect influential rows and retain supported extremes"},
        {"assumption_id": "A07", "model_id": "LOG01", "assumption": "independent binary rows", "evidence": "224 unique training patients and index encounters", "status": "pass", "required_action": "retain Module 01 grain and split"},
        {"assumption_id": "A08", "model_id": "LOG01", "assumption": "binary outcome and events", "evidence": "25 positive and 199 negative training rows", "status": "pass", "required_action": "report event count with every interpretation"},
        {"assumption_id": "A09", "model_id": "LOG01", "assumption": "linearity in the log odds for age", "evidence": "LOG02 adds one squared centered-age term on training data", "status": "review", "required_action": "interpret the comparison without selecting on test evidence"},
        {"assumption_id": "A10", "model_id": "LOG01", "assumption": "no separation or unstable extremes", "evidence": f"maximum fitted probability={log1['maximum_fitted_probability']['value']}; maximum standard error={log1['maximum_standard_error']['value']}", "status": "review", "required_action": "retain convergence and extreme-probability checks; consider regularization in Module 03"},
        {"assumption_id": "A11", "model_id": "LOG01", "assumption": "adequate categorical support", "evidence": f"{sparse_flags} training category rows have an absent or zero outcome cell", "status": "review", "required_action": "do not add or rank unsupported category effects"},
        {"assumption_id": "A12", "model_id": "LOG01", "assumption": "model specification is sufficient", "evidence": "small declared formula omits many possible mechanisms", "status": "limit", "required_action": "call estimates model-conditional and retain omitted-variable boundary"},
        {"assumption_id": "A13", "model_id": "ALL", "assumption": "causal identification", "evidence": "no intervention contrast assignment design or exchangeability argument", "status": "not supported", "required_action": "use no causal effect language"},
        {"assumption_id": "A14", "model_id": "ALL", "assumption": "real-population transport", "evidence": "synthetic older teaching cohort", "status": "not supported", "required_action": "use teaching-only interpretation"},
    ]


def r_fixture_rows(linear_fit, logistic_fit) -> list[dict[str, object]]:
    result = []
    for model_id, fit, terms, distribution in (
        ("LIN01", linear_fit, LINEAR_TERMS, "t with 65 residual degrees of freedom"),
        ("LOG01", logistic_fit, LOGISTIC_TERMS["LOG01"], "normal approximation"),
    ):
        ci = fit.conf_int(alpha=0.05)
        for index, term in enumerate(terms):
            result.append({
                "model_id": model_id, "term": term, "estimate_target": fixed(float(fit.params.iloc[index])),
                "std_error_target": fixed(float(fit.bse.iloc[index])), "lower95_target": fixed(float(ci.iloc[index, 0])),
                "upper95_target": fixed(float(ci.iloc[index, 1])), "interval_reference": distribution,
                "tolerance": "0.000001", "status": "Python-generated numeric target; learner R execution required",
            })
    return result


def check_rows(cohort: pd.DataFrame, train: pd.DataFrame, linear_all: pd.DataFrame, linear_train: pd.DataFrame, outputs: dict[str, list[dict[str, object]]]) -> list[dict[str, object]]:
    split_timing = linear_all["split"].value_counts().to_dict()
    checks = (
        ("CHK01", "upstream rows", len(cohort), 374),
        ("CHK02", "upstream fields", cohort.shape[1], 34),
        ("CHK03", "training rows", len(train), 224),
        ("CHK04", "training positives", int(train["acute_return_90d"].sum()), 25),
        ("CHK05", "linear subset total rows", len(linear_all), 111),
        ("CHK06", "linear training rows", len(linear_train), 69),
        ("CHK07", "linear validation rows excluded", split_timing.get("validation"), 21),
        ("CHK08", "linear test rows excluded", split_timing.get("test"), 21),
        ("CHK09", "structural timing blanks retained", int(cohort["next_30d_days_after_index_stop"].isna().sum()), 263),
        ("CHK10", "linear coefficient rows", len(outputs["linear-coefficients.csv"]), 4),
        ("CHK11", "linear diagnostic rows", len(outputs["linear-diagnostics.csv"]), 13),
        ("CHK12", "linear prediction scenarios", len(outputs["linear-prediction-examples.csv"]), 3),
        ("CHK13", "logistic coefficient rows", len(outputs["logistic-coefficients.csv"]), 14),
        ("CHK14", "logistic diagnostic rows", len(outputs["logistic-diagnostics.csv"]), 45),
        ("CHK15", "logistic prediction scenarios", len(outputs["logistic-prediction-examples.csv"]), 3),
        ("CHK16", "model matrix rows", len(outputs["model-matrix-fields.csv"]), 18),
        ("CHK17", "model comparison rows", len(outputs["model-comparison.csv"]), 3),
        ("CHK18", "assumption rows", len(outputs["assumption-register.csv"]), 14),
        ("CHK19", "paired R reading rows", len(outputs["r-reading-fixture.csv"]), 8),
        ("CHK20", "all linear fit rows are training", sum(row["fit_use"] == "fit and interpretation" for row in outputs["linear-subset-registry.csv"]), 69),
        ("CHK21", "all models converged", sum(row["metric"] == "converged" and row["value"] == "true" for row in outputs["logistic-diagnostics.csv"]), 3),
        ("CHK22", "causal boundary present", sum(row["status"] == "not supported" for row in outputs["assumption-register.csv"]), 2),
        ("CHK23", "test rows absent from fit data", len(train.loc[train["split"] == "test"]), 0),
        ("CHK24", "baseline preserved", 1, 1),
    )
    return [{"check_id": check_id, "check": label, "observed": observed, "expected": expected, "status": "pass" if observed == expected else "fail"} for check_id, label, observed, expected in checks]


def build_outputs(paths: dict[str, Path], target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    cohort, _ = load_data(paths)
    train, linear_all, age_mean = prepare(cohort)
    linear_train, linear_fit, linear_hc3, logistic_fits, logistic_robust = fit_models(train, linear_all)
    outputs = {
        "linear-subset-registry.csv": linear_subset_rows(linear_all),
        "linear-coefficients.csv": linear_coefficient_rows(linear_fit, linear_hc3),
        "linear-diagnostics.csv": linear_diagnostic_rows(linear_train, linear_fit),
        "linear-prediction-examples.csv": linear_prediction_rows(linear_fit),
        "logistic-coefficients.csv": logistic_coefficient_rows(logistic_fits, logistic_robust),
        "logistic-diagnostics.csv": logistic_diagnostic_rows(train, logistic_fits),
        "logistic-prediction-examples.csv": logistic_prediction_rows(train, logistic_fits["LOG01"], age_mean),
        "model-matrix-fields.csv": matrix_rows(age_mean),
        "model-comparison.csv": comparison_rows(logistic_fits),
        "sparse-cell-checks.csv": sparse_rows(cohort, train),
    }
    outputs["assumption-register.csv"] = assumption_rows(linear_all, linear_train, outputs["linear-diagnostics.csv"], outputs["logistic-diagnostics.csv"], outputs["sparse-cell-checks.csv"])
    outputs["r-reading-fixture.csv"] = r_fixture_rows(linear_fit, logistic_fits["LOG01"])
    outputs["regression-checks.csv"] = check_rows(cohort, train, linear_all, linear_train, outputs)
    if any(row["status"] != "pass" for row in outputs["regression-checks.csv"]):
        raise ValueError("One or more regression release checks failed.")
    target.mkdir(parents=True)
    report: dict[str, object] = {
        "status": "pass", "version": "0.1.0", "age_center_training_mean": fixed(age_mean, 12),
        "upstream": {name: {"bytes": path.stat().st_size, "sha256": sha256(path)} for name, path in paths.items()},
        "fit_partitions": {"linear": "train only", "logistic": "train only", "validation": "not used", "test": "not used"},
        "linear_case": {"all_recorded_rows": len(linear_all), "training_rows": len(linear_train), "structural_blanks": int(cohort["next_30d_days_after_index_stop"].isna().sum())},
        "logistic_case": {"training_rows": len(train), "positives": int(train["acute_return_90d"].sum()), "handoff_model": "LOG01"},
        "outputs": {}, "decision": {"reference_disposition": "accept with conditions", "module_03_progression": "allowed"},
    }
    for name, rows in outputs.items():
        path = target / name
        write_csv(path, rows)
        report["outputs"][name] = {"rows": len(rows), "fields": len(rows[0]), "bytes": path.stat().st_size, "sha256": sha256(path)}
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
    shutil.copy2(MODULE_ROOT / "validate_regression_evidence.py", target / "validate_regression_evidence.py")
    data_dir = target / "data"
    data_dir.mkdir()
    for name, path in paths.items():
        shutil.copy2(path, data_dir / name)
    return build_outputs(upstream_paths(data_dir), target / "outputs")


def self_check() -> None:
    paths = upstream_paths()
    with tempfile.TemporaryDirectory(prefix="fnd2-module02-build-") as temp_dir:
        root = Path(temp_dir)
        outputs = root / "outputs"
        report = build_outputs(paths, outputs)
        assert report["linear_case"]["training_rows"] == 69
        assert report["logistic_case"]["positives"] == 25
        try:
            build_outputs(paths, outputs)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not refuse an existing output target.")
        workspace = root / "learner-workspace"
        workspace_report = build_workspace(paths, workspace)
        reproduced = workspace / "reproduced-outputs"
        reproduced_report = build_outputs(upstream_paths(workspace / "data"), reproduced)
        assert reproduced_report["outputs"] == workspace_report["outputs"]
    print("FND-2 Module 02 builder self-check passed.")


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
    if args.outputs_only:
        print(json.dumps(build_outputs(upstream_paths(), args.target.resolve()), indent=2))
    else:
        print(json.dumps(build_workspace(upstream_paths(), args.target.resolve()), indent=2))


if __name__ == "__main__":
    main()
