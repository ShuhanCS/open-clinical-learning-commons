"""Build deterministic APP-1 Module 03 survival evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import statsmodels
from scipy.stats import chi2, spearmanr
from statsmodels.duration.hazard_regression import PHReg


MODULE_ROOT = Path(__file__).resolve().parent
UPSTREAM = MODULE_ROOT.parent / "02-longitudinal-cohorts-followup" / "outputs" / "analysis-cohort.csv"
EXPECTED_SOURCE = {
    "rows": 476,
    "fields": 49,
    "bytes": 200699,
    "sha256": "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5",
}
FIXED_TIMES = (0, 30, 90, 180, 270, 335)
GROUPS = ((0, "no_recorded_followup"), (1, "scheduled_followup"))
OUTPUT_FILES = (
    "analysis-checks.csv", "cohort-summary.csv", "cox-model.csv", "death-audit.csv",
    "fixed-time-comparison.csv", "km-curve.svg", "km-event-table.csv", "km-risk-table.csv",
    "logrank.csv", "ph-check.csv", "build-report.json",
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


def loglog_interval(survival: float, greenwood: float) -> tuple[float, float]:
    if survival >= 1 or greenwood <= 0:
        return survival, survival
    if survival <= 0:
        return 0.0, 0.0
    standard = math.sqrt(greenwood) / abs(math.log(survival))
    center = math.log(-math.log(survival))
    z = 1.959963984540054
    return math.exp(-math.exp(center + z * standard)), math.exp(-math.exp(center - z * standard))


def km_rows(group: pd.DataFrame, exposure: int, label: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    survival = 1.0
    greenwood = 0.0
    for time in sorted(group["observed_time_days"].unique()):
        at_risk = int((group["observed_time_days"] >= time).sum())
        events = int(((group["observed_time_days"] == time) & (group["event_indicator"] == 1)).sum())
        censored = int(((group["observed_time_days"] == time) & (group["event_indicator"] == 0)).sum())
        factor = 1 - events / at_risk
        survival *= factor
        if events and at_risk > events:
            greenwood += events / (at_risk * (at_risk - events))
        standard_error = survival * math.sqrt(greenwood)
        lower, upper = loglog_interval(survival, greenwood)
        rows.append({
            "landmark_exposure": exposure, "group": label, "time_days": fixed(float(time)),
            "at_risk_before": at_risk, "events_at_time": events, "censored_at_time": censored,
            "conditional_event_free_factor": fixed(factor), "km_event_free_probability": fixed(survival),
            "greenwood_cumulative": fixed(greenwood), "standard_error": fixed(standard_error),
            "lower95": fixed(lower), "upper95": fixed(upper),
        })
    return rows


def estimate_at(event_rows: list[dict[str, object]], time: int) -> dict[str, object]:
    eligible = [row for row in event_rows if float(row["time_days"]) <= time]
    return eligible[-1] if eligible else {
        "km_event_free_probability": "1.00000000", "standard_error": "0.00000000",
        "lower95": "1.00000000", "upper95": "1.00000000",
    }


def logrank(frame: pd.DataFrame) -> dict[str, object]:
    observed = 0.0
    expected = 0.0
    variance = 0.0
    for time in sorted(frame.loc[frame["event_indicator"] == 1, "observed_time_days"].unique()):
        at = frame[frame["observed_time_days"] >= time]
        n = len(at)
        n1 = int((at["landmark_exposure"] == 1).sum())
        events = frame[(frame["observed_time_days"] == time) & (frame["event_indicator"] == 1)]
        d = len(events)
        d1 = int((events["landmark_exposure"] == 1).sum())
        observed += d1
        expected += d * n1 / n
        if n > 1:
            variance += n1 * (n - n1) * d * (n - d) / (n * n * (n - 1))
    statistic = (observed - expected) ** 2 / variance
    return {
        "groups": 2, "people": len(frame), "events": int(frame["event_indicator"].sum()),
        "observed_exposed_events": fixed(observed), "expected_exposed_events": fixed(expected),
        "variance": fixed(variance), "chi_square": fixed(statistic), "degrees_freedom": 1,
        "p_value": fixed(float(chi2.sf(statistic, 1))),
        "boundary": "two-sided group test; a large p-value does not prove equivalence or no clinical difference",
    }


def render_curve(path: Path, event_tables: dict[int, list[dict[str, object]]]) -> None:
    matplotlib.rcParams["svg.hashsalt"] = "oclc-app1-03"
    figure, axis = plt.subplots(figsize=(8, 5))
    styles = {0: ("#1f49b6", "-"), 1: ("#c2410c", "--")}
    for exposure, label in GROUPS:
        rows = event_tables[exposure]
        times = [0.0] + [float(row["time_days"]) for row in rows]
        values = [1.0] + [float(row["km_event_free_probability"]) for row in rows]
        color, linestyle = styles[exposure]
        axis.step(times, values, where="post", color=color, linestyle=linestyle, linewidth=2.2, label=label.replace("_", " "))
    axis.set(xlim=(0, 335), ylim=(0, 1.01), xlabel="Days after day-30 landmark", ylabel="Event-free probability")
    axis.set_title("Time to first later acute return by scheduled follow-up record")
    axis.grid(axis="y", color="#d1d5db", linewidth=0.6)
    axis.legend(loc="lower left", frameon=False)
    figure.text(0.5, 0.01, "Synthetic teaching cohort. Exact estimates and numbers at risk are in km-risk-table.csv.", ha="center", fontsize=8)
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
    frame = pd.read_csv(cohort_path)
    if len(frame) != EXPECTED_SOURCE["rows"] or len(frame.columns) != EXPECTED_SOURCE["fields"]:
        raise ValueError("Module 02 analysis-cohort shape changed")
    target.mkdir(parents=True)

    checks = {
        "people": len(frame), "unique_people": frame["patient_id"].nunique(),
        "landmark_eligible": int(frame["landmark_eligible_flag"].sum()),
        "scheduled_followup": int(frame["landmark_exposure"].sum()),
        "no_scheduled_followup": int((1 - frame["landmark_exposure"]).sum()),
        "events": int(frame["event_indicator"].sum()),
        "exposed_events": int(((frame["landmark_exposure"] == 1) & (frame["event_indicator"] == 1)).sum()),
        "unexposed_events": int(((frame["landmark_exposure"] == 0) & (frame["event_indicator"] == 1)).sum()),
        "administrative_censors": int((frame["censor_reason"] == "administrative_end").sum()),
        "competing_death_censors": int((frame["censor_reason"] == "competing_death").sum()),
        "later_deaths": int(frame["later_death_flag"].sum()),
        "later_deaths_before_event": int(frame["later_death_before_event_flag"].sum()),
        "positive_observed_time": int((frame["observed_time_days"] > 0).sum()),
        "maximum_observed_days": fixed(float(frame["observed_time_days"].max())),
        "extension_rows": int((frame["field_class"] == "synthetic_extension").sum()),
    }
    expected = {
        "people": 476, "unique_people": 476, "landmark_eligible": 476, "scheduled_followup": 129,
        "no_scheduled_followup": 347, "events": 87, "exposed_events": 25, "unexposed_events": 62,
        "administrative_censors": 389, "competing_death_censors": 0, "later_deaths": 3,
        "later_deaths_before_event": 0, "positive_observed_time": 476, "maximum_observed_days": "335.00000000",
        "extension_rows": 476,
    }
    if checks != expected:
        raise ValueError(f"Accepted survival cohort changed: {checks}")
    write_csv(target / "analysis-checks.csv", ["check_name", "observed_value", "expected_value", "status"], [
        {"check_name": name, "observed_value": value, "expected_value": expected[name], "status": "pass"}
        for name, value in checks.items()
    ])

    summary_rows = []
    for exposure, label in GROUPS:
        group = frame[frame["landmark_exposure"] == exposure]
        summary_rows.append({"landmark_exposure": exposure, "group": label, "people": len(group), "events": int(group["event_indicator"].sum()), "administrative_censors": int((group["censor_reason"] == "administrative_end").sum()), "competing_death_censors": int((group["censor_reason"] == "competing_death").sum()), "later_deaths_after_event": int(group["later_death_flag"].sum())})
    summary_rows.append({"landmark_exposure": "all", "group": "all", "people": 476, "events": 87, "administrative_censors": 389, "competing_death_censors": 0, "later_deaths_after_event": 3})
    write_csv(target / "cohort-summary.csv", list(summary_rows[0]), summary_rows)

    event_tables = {exposure: km_rows(frame[frame["landmark_exposure"] == exposure], exposure, label) for exposure, label in GROUPS}
    all_event_rows = event_tables[0] + event_tables[1]
    write_csv(target / "km-event-table.csv", list(all_event_rows[0]), all_event_rows)
    risk_rows = []
    for exposure, label in GROUPS:
        group = frame[frame["landmark_exposure"] == exposure]
        for time in FIXED_TIMES:
            estimate = estimate_at(event_tables[exposure], time)
            risk_rows.append({
                "landmark_exposure": exposure, "group": label, "time_days": time, "group_people": len(group),
                "at_risk_before": int((group["observed_time_days"] >= time).sum()),
                "cumulative_events": int(((group["event_indicator"] == 1) & (group["observed_time_days"] <= time)).sum()),
                "cumulative_censors": int(((group["event_indicator"] == 0) & (group["observed_time_days"] <= time)).sum()),
                "km_event_free_probability": estimate["km_event_free_probability"],
                "cumulative_event_risk": fixed(1 - float(estimate["km_event_free_probability"])),
                "standard_error": estimate["standard_error"], "lower95": estimate["lower95"], "upper95": estimate["upper95"],
            })
    write_csv(target / "km-risk-table.csv", list(risk_rows[0]), risk_rows)
    risk_by = {(row["landmark_exposure"], row["time_days"]): row for row in risk_rows}
    comparisons = []
    for time in FIXED_TIMES:
        no = risk_by[(0, time)]
        yes = risk_by[(1, time)]
        no_survival, yes_survival = float(no["km_event_free_probability"]), float(yes["km_event_free_probability"])
        comparisons.append({
            "time_days": time, "scheduled_followup_event_free": fixed(yes_survival), "scheduled_followup_lower95": yes["lower95"], "scheduled_followup_upper95": yes["upper95"],
            "no_followup_event_free": fixed(no_survival), "no_followup_lower95": no["lower95"], "no_followup_upper95": no["upper95"],
            "event_free_difference_exposed_minus_unexposed": fixed(yes_survival - no_survival),
            "event_risk_difference_exposed_minus_unexposed": fixed((1 - yes_survival) - (1 - no_survival)),
            "boundary": "descriptive fixed-time synthetic comparison; not adjusted or causal",
        })
    write_csv(target / "fixed-time-comparison.csv", list(comparisons[0]), comparisons)

    logrank_row = logrank(frame)
    write_csv(target / "logrank.csv", list(logrank_row), [logrank_row])
    exog = pd.DataFrame({"scheduled_followup": frame["landmark_exposure"].astype(float)})
    fit = PHReg(frame["observed_time_days"], exog, status=frame["event_indicator"], ties="efron").fit()
    coefficient = float(fit.params[0])
    lower, upper = fit.conf_int()[0]
    z_value = coefficient / float(fit.bse[0])
    cox_row = {
        "term": "scheduled_followup", "coefficient": fixed(coefficient), "standard_error": fixed(float(fit.bse[0])),
        "hazard_ratio": fixed(math.exp(coefficient)), "lower95": fixed(math.exp(float(lower))), "upper95": fixed(math.exp(float(upper))),
        "z_value": fixed(z_value), "p_value": fixed(float(chi2.sf(z_value * z_value, 1))), "people": 476, "events": 87, "censored": 389,
        "ties": "efron", "boundary": "unadjusted synthetic hazard ratio; not probability risk ratio adjusted comparison or causal effect",
    }
    write_csv(target / "cox-model.csv", list(cox_row), [cox_row])
    residuals = np.asarray(fit.schoenfeld_residuals)[:, 0]
    event_mask = frame["event_indicator"].to_numpy() == 1
    correlation, ph_p = spearmanr(residuals[event_mask], np.log(frame.loc[event_mask, "observed_time_days"].to_numpy()))
    ph_row = {
        "term": "scheduled_followup", "method": "event-level Schoenfeld residual Spearman correlation with log event time",
        "event_rows": int(event_mask.sum()), "correlation": fixed(float(correlation)), "p_value": fixed(float(ph_p)), "threshold": "0.05000000",
        "screen_result": "fail" if ph_p < 0.05 else "pass",
        "required_action": "do not use one constant hazard ratio as the main summary; foreground fixed-time evidence and refer time-varying modeling",
    }
    write_csv(target / "ph-check.csv", list(ph_row), [ph_row])

    deaths = frame[frame["later_death_flag"] == 1].sort_values("patient_id")
    death_rows = [{
        "patient_id": row.patient_id, "landmark_exposure": int(row.landmark_exposure), "first_later_acute_start": row.first_later_acute_start,
        "event_time_days": fixed(float(row.observed_time_days)), "later_death_date": row.later_death_date,
        "later_death_before_event_flag": int(row.later_death_before_event_flag), "relation": "death_after_first_later_acute_return",
    } for row in deaths.itertuples()]
    write_csv(target / "death-audit.csv", list(death_rows[0]), death_rows)
    render_curve(target / "km-curve.svg", event_tables)

    report = {
        "module": "oclc-app1-03", "module_version": "0.1.0", "commons_release": "0.51.0",
        "source": EXPECTED_SOURCE, "checks": checks,
        "reference": {"logrank": logrank_row, "cox": cox_row, "ph_screen": ph_row, "fixed_time_comparisons": comparisons},
        "libraries": {"matplotlib": matplotlib.__version__, "numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "statsmodels": statsmodels.__version__},
        "claim_boundary": "synthetic observational teaching evidence only",
    }
    (target / "build-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    return {"status": "pass", "output_files": len(OUTPUT_FILES), "output_bytes": sum((target / name).stat().st_size for name in OUTPUT_FILES), "checks": len(checks)}


def self_check(cohort: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="app1-module03-") as temp_dir:
        base = Path(temp_dir)
        first, second = base / "first", base / "second"
        one = build(cohort, first)
        two = build(cohort, second)
        assert one == two
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
    print("APP-1 Module 03 builder self-check passed: upstream fingerprint, survival evidence, determinism, and overwrite rules.")


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
