"""Build deterministic APP-1 Module 04 risk-adjustment evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import tempfile
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import statsmodels
import statsmodels.api as sm
from scipy.stats import chi2, rankdata


MODULE_ROOT = Path(__file__).resolve().parent
UPSTREAM = MODULE_ROOT.parent / "02-longitudinal-cohorts-followup" / "outputs" / "analysis-cohort.csv"
FIELD_CONTRACT = MODULE_ROOT / "field-role-contract.csv"
EXPECTED_SOURCE = {"rows": 476, "fields": 49, "bytes": 200699, "sha256": "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5"}
PREDICTORS = ("age_decade_from_40", "any_prior_acute", "prior_365d_condition_count", "index_inpatient")
MODEL_TERMS = ("intercept",) + PREDICTORS
SITE_ORDER = ("SITE-A", "SITE-B", "SITE-C", "SITE-D", "SITE-E", "SITE-F")
BOOTSTRAP_SAMPLES = 300
BOOTSTRAP_SEED = 20260830
OUTPUT_FILES = (
    "adjusted-association.csv", "analysis-checks.csv", "bootstrap-stability.csv", "build-report.json",
    "calibration-quintiles.csv", "comparison-figure.svg", "expected-outcomes.csv",
    "exposure-comparison.csv", "field-role-summary.csv", "model-coefficients.csv",
    "model-performance.csv", "site-case-mix.csv", "site-comparison.csv",
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


def add_predictors(frame: pd.DataFrame) -> pd.DataFrame:
    result = frame.copy()
    result["age_decade_from_40"] = (result["age_at_index"] - 40) / 10
    result["any_prior_acute"] = (result["prior_365d_acute_count"] > 0).astype(int)
    result["index_inpatient"] = (result["index_encounter_class"] == "inpatient").astype(int)
    return result


def design(frame: pd.DataFrame, exposure: bool = False) -> pd.DataFrame:
    columns = list(PREDICTORS) + (["landmark_exposure"] if exposure else [])
    return sm.add_constant(frame[columns].astype(float), has_constant="add")


def fit_model(frame: pd.DataFrame, exposure: bool = False):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return sm.GLM(frame["event_indicator"], design(frame, exposure=exposure), family=sm.families.Binomial()).fit(maxiter=100, disp=0)


def coefficient_rows(fit) -> list[dict[str, object]]:
    intervals = fit.conf_int()
    rows = []
    for index, source_term in enumerate(fit.params.index):
        term = "intercept" if source_term == "const" else source_term
        coefficient = float(fit.params.iloc[index])
        standard_error = float(fit.bse.iloc[index])
        lower, upper = (float(value) for value in intervals.iloc[index])
        z_value = coefficient / standard_error
        rows.append({
            "term": term, "coefficient": fixed(coefficient), "standard_error": fixed(standard_error),
            "odds_ratio": fixed(math.exp(coefficient)), "lower95": fixed(math.exp(lower)), "upper95": fixed(math.exp(upper)),
            "z_value": fixed(z_value), "p_value": fixed(float(chi2.sf(z_value * z_value, 1))),
            "role": "expected-outcome intercept" if term == "intercept" else "prespecified baseline predictor",
            "boundary": "apparent synthetic fixed-horizon association; not causal effect or transportable clinical coefficient",
        })
    return rows


def poisson_rate_interval(observed: int, expected: float, cohort_rate: float) -> tuple[float, float]:
    lower_count = 0.0 if observed == 0 else 0.5 * float(chi2.ppf(0.025, 2 * observed))
    upper_count = 0.5 * float(chi2.ppf(0.975, 2 * (observed + 1)))
    return lower_count / expected * cohort_rate, upper_count / expected * cohort_rate


def comparison_row(group: pd.DataFrame, label_field: str, label: str, cohort_rate: float) -> dict[str, object]:
    people = len(group)
    observed = int(group["event_indicator"].sum())
    expected = float(group["expected_probability"].sum())
    oe = observed / expected
    standardized = oe * cohort_rate
    lower, upper = poisson_rate_interval(observed, expected, cohort_rate)
    return {
        label_field: label, "people": people, "observed_events": observed, "crude_event_rate": fixed(observed / people),
        "expected_events": fixed(expected), "mean_expected_probability": fixed(expected / people),
        "observed_to_expected": fixed(oe), "standardized_event_rate": fixed(standardized),
        "standardized_lower95": fixed(lower), "standardized_upper95": fixed(upper),
    }


def render_site_figure(path: Path, rows: list[dict[str, object]], cohort_rate: float) -> None:
    matplotlib.rcParams["svg.hashsalt"] = "oclc-app1-04"
    figure, axis = plt.subplots(figsize=(8, 5))
    positions = np.arange(len(rows))
    values = np.array([float(row["standardized_event_rate"]) for row in rows])
    lower = values - np.array([float(row["standardized_lower95"]) for row in rows])
    upper = np.array([float(row["standardized_upper95"]) for row in rows]) - values
    axis.errorbar(positions, values, yerr=np.vstack([lower, upper]), fmt="o", color="#1f49b6", ecolor="#64748b", capsize=4, linewidth=1.5)
    axis.axhline(cohort_rate, color="#c2410c", linestyle="--", linewidth=1.5, label="cohort event rate")
    axis.set_xticks(positions, [row["teaching_site_id"] for row in rows])
    axis.set(xlabel="Synthetic teaching site", ylabel="Indirectly standardized event rate", ylim=(0, 0.5))
    axis.set_title("Synthetic teaching-site standardized rates, fixed order and not rankings")
    axis.grid(axis="y", color="#d1d5db", linewidth=0.6)
    axis.legend(frameon=False)
    figure.text(0.5, 0.01, "Poisson count intervals treat expected events as fixed. Exact evidence is in site-comparison.csv.", ha="center", fontsize=8)
    figure.tight_layout(rect=(0, 0.04, 1, 1))
    figure.savefig(path, format="svg", metadata={"Date": None})
    plt.close(figure)


def build(cohort_path: Path, target: Path) -> dict[str, object]:
    cohort_path = cohort_path.resolve()
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    if cohort_path.stat().st_size != EXPECTED_SOURCE["bytes"] or sha256(cohort_path) != EXPECTED_SOURCE["sha256"]:
        raise ValueError("Module 02 analysis-cohort fingerprint changed")
    frame = add_predictors(pd.read_csv(cohort_path))
    contract = pd.read_csv(FIELD_CONTRACT)
    if len(frame) != 476 or len(frame.columns) != 52 or len(contract) != 49 or set(contract["field"]) != set(pd.read_csv(cohort_path, nrows=0).columns):
        raise ValueError("Cohort or field-role contract changed")
    target.mkdir(parents=True)

    checks = {
        "people": len(frame), "unique_people": frame["patient_id"].nunique(), "events": int(frame["event_indicator"].sum()),
        "administrative_censors": int((frame["censor_reason"] == "administrative_end").sum()),
        "competing_death_censors": int((frame["censor_reason"] == "competing_death").sum()),
        "maximum_observed_days": fixed(float(frame["observed_time_days"].max())),
        "source_fields": 49, "field_contract_rows": len(contract), "baseline_predictors": len(PREDICTORS),
        "predictor_missing_values": int(frame[list(PREDICTORS)].isna().sum().sum()),
        "exposure_in_expected_model": int("landmark_exposure" in PREDICTORS),
        "site_in_expected_model": int("teaching_site_id" in PREDICTORS),
        "extension_in_expected_model": int(any(field in PREDICTORS for field in ("baseline_risk_score", "baseline_risk_rank", "baseline_risk_tier"))),
        "teaching_sites": frame["teaching_site_id"].nunique(), "scheduled_followup": int(frame["landmark_exposure"].sum()),
        "module03_ph_failure_carried": 1,
    }
    expected_checks = {"people": 476, "unique_people": 476, "events": 87, "administrative_censors": 389, "competing_death_censors": 0, "maximum_observed_days": "335.00000000", "source_fields": 49, "field_contract_rows": 49, "baseline_predictors": 4, "predictor_missing_values": 0, "exposure_in_expected_model": 0, "site_in_expected_model": 0, "extension_in_expected_model": 0, "teaching_sites": 6, "scheduled_followup": 129, "module03_ph_failure_carried": 1}
    if checks != expected_checks:
        raise ValueError(f"Adjustment invariants changed: {checks}")
    write_csv(target / "analysis-checks.csv", ["check_name", "observed_value", "expected_value", "status"], [{"check_name": name, "observed_value": value, "expected_value": expected_checks[name], "status": "pass"} for name, value in checks.items()])
    role_summary = []
    for role, rows in contract.groupby("role", sort=True):
        role_summary.append({"role": role, "fields": len(rows), "field_names": "|".join(rows["field"]), "expected_model_use": "yes" if role == "baseline_predictor" else "no"})
    write_csv(target / "field-role-summary.csv", list(role_summary[0]), role_summary)

    fit = fit_model(frame)
    frame["expected_probability"] = fit.predict(design(frame))
    coefficient_output = coefficient_rows(fit)
    write_csv(target / "model-coefficients.csv", list(coefficient_output[0]), coefficient_output)
    positives = int(frame["event_indicator"].sum())
    negatives = len(frame) - positives
    auc = (rankdata(frame["expected_probability"])[frame["event_indicator"].to_numpy() == 1].sum() - positives * (positives + 1) / 2) / (positives * negatives)
    brier = float(np.mean((frame["event_indicator"] - frame["expected_probability"]) ** 2))
    performance = [
        {"metric": "people", "value": str(len(frame)), "interpretation": "fitting cohort size"},
        {"metric": "events", "value": str(positives), "interpretation": "fixed-horizon outcomes"},
        {"metric": "event_prevalence", "value": fixed(positives / len(frame)), "interpretation": "cohort event rate"},
        {"metric": "brier_score", "value": fixed(brier), "interpretation": "apparent mean squared probability error; lower is better"},
        {"metric": "roc_auc", "value": fixed(float(auc)), "interpretation": "apparent rank discrimination; 0.5 is chance"},
        {"metric": "log_likelihood", "value": fixed(float(fit.llf)), "interpretation": "apparent fitted log likelihood"},
        {"metric": "deviance", "value": fixed(float(fit.deviance)), "interpretation": "apparent binomial deviance"},
        {"metric": "non_intercept_parameters", "value": str(len(PREDICTORS)), "interpretation": "prespecified baseline parameters"},
        {"metric": "events_per_non_intercept_parameter", "value": fixed(positives / len(PREDICTORS)), "interpretation": "descriptive support only"},
        {"metric": "sum_expected_events", "value": fixed(float(frame["expected_probability"].sum())), "interpretation": "in-sample intercept conservation"},
    ]
    write_csv(target / "model-performance.csv", list(performance[0]), performance)

    order = frame.sort_values(["expected_probability", "patient_id"], kind="mergesort").index
    frame["calibration_quintile"] = pd.Series(index=order, data=np.arange(len(frame)) * 5 // len(frame) + 1)
    calibration = []
    for quintile, group in frame.groupby("calibration_quintile", sort=True):
        observed = int(group["event_indicator"].sum())
        expected = float(group["expected_probability"].sum())
        calibration.append({"quintile": int(quintile), "people": len(group), "observed_events": observed, "expected_events": fixed(expected), "observed_rate": fixed(observed / len(group)), "mean_expected_probability": fixed(expected / len(group)), "observed_minus_expected": fixed(observed - expected), "support_status": "report with caution" if observed >= 10 and expected >= 10 else "sparse observed or expected events"})
    write_csv(target / "calibration-quintiles.csv", list(calibration[0]), calibration)

    rng = np.random.default_rng(BOOTSTRAP_SEED)
    estimates = []
    failures = 0
    for _ in range(BOOTSTRAP_SAMPLES):
        sample = frame.iloc[rng.integers(0, len(frame), len(frame))]
        try:
            estimates.append(fit_model(sample).params.to_numpy())
        except Exception:
            failures += 1
    matrix = np.asarray(estimates)
    bootstrap = []
    for index, term in enumerate(MODEL_TERMS):
        reference = float(fit.params.iloc[index])
        bootstrap.append({"term": term, "reference_coefficient": fixed(reference), "bootstrap_median": fixed(float(np.quantile(matrix[:, index], 0.5))), "bootstrap_lower2_5": fixed(float(np.quantile(matrix[:, index], 0.025))), "bootstrap_upper97_5": fixed(float(np.quantile(matrix[:, index], 0.975))), "same_sign_share": fixed(float(np.mean(np.sign(matrix[:, index]) == np.sign(reference)))), "successful_fits": len(estimates), "failed_fits": failures, "boundary": "person bootstrap stability screen; not corrected inference or external validation"})
    write_csv(target / "bootstrap-stability.csv", list(bootstrap[0]), bootstrap)

    expected_rows = []
    for row in frame.sort_values("patient_id").itertuples():
        expected_rows.append({"patient_id": row.patient_id, "event_indicator": int(row.event_indicator), "age_decade_from_40": fixed(float(row.age_decade_from_40)), "any_prior_acute": int(row.any_prior_acute), "prior_365d_condition_count": int(row.prior_365d_condition_count), "index_inpatient": int(row.index_inpatient), "expected_probability": fixed(float(row.expected_probability)), "observed_minus_expected": fixed(float(row.event_indicator - row.expected_probability)), "landmark_exposure": int(row.landmark_exposure), "teaching_site_id": row.teaching_site_id, "baseline_risk_tier": row.baseline_risk_tier, "site_field_class": row.field_class})
    write_csv(target / "expected-outcomes.csv", list(expected_rows[0]), expected_rows)

    cohort_rate = positives / len(frame)
    exposure_rows = []
    for exposure, label in ((0, "no_recorded_followup"), (1, "scheduled_followup")):
        row = comparison_row(frame[frame["landmark_exposure"] == exposure], "group", label, cohort_rate)
        row.update({"landmark_exposure": exposure, "support_status": "report with caution", "boundary": "descriptive baseline-expected comparison; not causal effect"})
        exposure_rows.append(row)
    exposure_fields = ["landmark_exposure", "group"] + [key for key in exposure_rows[0] if key not in {"landmark_exposure", "group"}]
    write_csv(target / "exposure-comparison.csv", exposure_fields, exposure_rows)
    adjusted_fit = fit_model(frame, exposure=True)
    index = list(adjusted_fit.params.index).index("landmark_exposure")
    coefficient = float(adjusted_fit.params.iloc[index])
    lower, upper = (float(value) for value in adjusted_fit.conf_int().iloc[index])
    standard_error = float(adjusted_fit.bse.iloc[index])
    z_value = coefficient / standard_error
    adjusted = [{"term": "landmark_exposure", "coefficient": fixed(coefficient), "standard_error": fixed(standard_error), "adjusted_odds_ratio": fixed(math.exp(coefficient)), "lower95": fixed(math.exp(lower)), "upper95": fixed(math.exp(upper)), "z_value": fixed(z_value), "p_value": fixed(float(chi2.sf(z_value * z_value, 1))), "baseline_predictors": "|".join(PREDICTORS), "people": 476, "events": 87, "boundary": "secondary adjusted observational odds ratio; not risk ratio hazard ratio or causal effect"}]
    write_csv(target / "adjusted-association.csv", list(adjusted[0]), adjusted)

    case_mix = []
    site_rows = []
    for site in SITE_ORDER:
        group = frame[frame["teaching_site_id"] == site]
        tiers = group["baseline_risk_tier"].value_counts()
        case_mix.append({"teaching_site_id": site, "people": len(group), "mean_age": fixed(float(group["age_at_index"].mean())), "any_prior_acute_people": int(group["any_prior_acute"].sum()), "mean_prior_conditions": fixed(float(group["prior_365d_condition_count"].mean())), "inpatient_indexes": int(group["index_inpatient"].sum()), "scheduled_followup": int(group["landmark_exposure"].sum()), "low_risk": int(tiers.get("low", 0)), "medium_risk": int(tiers.get("medium", 0)), "high_risk": int(tiers.get("high", 0)), "field_class": "synthetic_extension"})
        row = comparison_row(group, "teaching_site_id", site, cohort_rate)
        reasons = []
        if len(group) < 50: reasons.append("people below 50")
        if int(group["event_indicator"].sum()) < 10: reasons.append("observed events below 10")
        if float(group["expected_probability"].sum()) < 10: reasons.append("expected events below 10")
        if group["landmark_exposure"].nunique() < 2: reasons.append("exposure group absent")
        if group["baseline_risk_tier"].nunique() < 3: reasons.append("risk tier absent")
        row.update({"scheduled_followup": int(group["landmark_exposure"].sum()), "no_scheduled_followup": int((group["landmark_exposure"] == 0).sum()), "low_risk": int(tiers.get("low", 0)), "medium_risk": int(tiers.get("medium", 0)), "high_risk": int(tiers.get("high", 0)), "suppression_status": "suppress" if reasons else "report with caution", "suppression_reason": "|".join(reasons) if reasons else "all prespecified minimums met", "field_class": "synthetic_extension", "known_direct_site_effect": 0, "boundary": "synthetic site comparison in fixed order; not ranking or real facility performance"})
        site_rows.append(row)
    write_csv(target / "site-case-mix.csv", list(case_mix[0]), case_mix)
    site_fields = ["teaching_site_id"] + [key for key in site_rows[0] if key != "teaching_site_id"]
    write_csv(target / "site-comparison.csv", site_fields, site_rows)
    render_site_figure(target / "comparison-figure.svg", site_rows, cohort_rate)

    report = {
        "module": "oclc-app1-04", "module_version": "0.1.0", "commons_release": "0.52.0",
        "source": EXPECTED_SOURCE, "checks": checks,
        "model": {"formula": "event_indicator ~ age_decade_from_40 + any_prior_acute + prior_365d_condition_count + index_inpatient", "coefficients": coefficient_output, "performance": performance, "bootstrap": {"samples": BOOTSTRAP_SAMPLES, "seed": BOOTSTRAP_SEED, "successful": len(estimates), "failed": failures}},
        "reference": {"calibration": calibration, "exposure_comparison": exposure_rows, "adjusted_association": adjusted[0], "site_comparison": site_rows},
        "libraries": {"matplotlib": matplotlib.__version__, "numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "statsmodels": statsmodels.__version__},
        "claim_boundary": "synthetic fixed-horizon descriptive risk adjustment only",
    }
    (target / "build-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    return {"status": "pass", "output_files": len(OUTPUT_FILES), "output_bytes": sum((target / name).stat().st_size for name in OUTPUT_FILES), "checks": len(checks), "bootstrap_fits": len(estimates)}


def self_check(cohort: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="app1-module04-") as temp_dir:
        base = Path(temp_dir)
        first, second = base / "first", base / "second"
        one = build(cohort, first)
        two = build(cohort, second)
        assert one == two and one["bootstrap_fits"] == 300
        assert {name: sha256(first / name) for name in OUTPUT_FILES} == {name: sha256(second / name) for name in OUTPUT_FILES}
        try:
            build(cohort, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder overwrote an existing target")
        changed = base / "changed.csv"
        shutil.copy2(cohort, changed)
        changed.write_text(changed.read_text(encoding="utf-8").replace("SITE-B", "SITE-Z", 1), encoding="utf-8", newline="\n")
        try:
            build(changed, base / "changed-output")
        except ValueError as error:
            assert "fingerprint" in str(error)
        else:
            raise AssertionError("Builder accepted a changed upstream cohort")
    print("APP-1 Module 04 builder self-check passed: field roles, model, calibration, bootstrap, comparisons, determinism, and overwrite rules.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cohort", type=Path, default=UPSTREAM)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check(args.cohort)
            return
        if not args.target:
            parser.error("--target is required unless --self-check is used")
        print(json.dumps(build(args.cohort, args.target), indent=2))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
