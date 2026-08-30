"""Build the exact FND-2 Module 05 forecasting and temporal-validation evidence."""

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
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import Holt
from statsmodels.tsa.stattools import adfuller


MODULE_ROOT = Path(__file__).resolve().parent
FOLD_ORIGINS = (74, 78, 82, 86, 90)
HORIZON = 4
SEASONAL_LAG = 52
UPSTREAM = {
    "nhsn-hospital-capacity-jurisdiction-2024-2026.csv": (428203, "8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1"),
    "ma-hospital-capacity-time-2024-2026.csv": (11170, "394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616"),
    "module-04-release.json": (7013, "ffcf57c30d77be5c2271488a4d2dd08cc44d430cc590025e918c0ec8f1c4e12e"),
    "module-04-progression.md": (1157, "fdfce797f69c80e71ff26a7fa6c3499c2c3c25069174560ae1441253ef1fb646"),
    "module-04-threat-register.csv": (1887, "ce1257bf019959f24b01706744612a28999ebe4524c7567ff860983f9f3190c3"),
}
PORTABLE_FILES = ("requirements.txt", "data-spec.md", "source-record.yml", "forecast-contract.json", "assessment.md")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fixed(value: float, digits: int = 8) -> str:
    return f"{value:.{digits}f}"


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
    repo = course.parents[1]
    da730 = repo / "courses" / "data-visualization" / "modules" / "08-time-process-variation" / "data"
    module04 = course / "modules" / "04-validity-adjustment-longitudinal"
    return {
        "nhsn-hospital-capacity-jurisdiction-2024-2026.csv": da730 / "nhsn_hospital_capacity_jurisdiction_2024_2026.csv",
        "ma-hospital-capacity-time-2024-2026.csv": da730 / "ma_hospital_capacity_time_2024_2026.csv",
        "module-04-release.json": module04 / "release.json",
        "module-04-progression.md": module04 / "progression-decision.md",
        "module-04-threat-register.csv": module04 / "outputs" / "validity-threat-register.csv",
    }


def verify_upstream(paths: dict[str, Path]) -> None:
    for name, (size, digest) in UPSTREAM.items():
        path = paths[name]
        if not path.is_file() or path.stat().st_size != size or sha256(path) != digest:
            raise ValueError(f"Accepted upstream fingerprint changed: {name}")


def load_series(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path, parse_dates=["week_end"])
    if len(frame) != 94 or frame["week_index"].tolist() != list(range(1, 95)):
        raise ValueError("Massachusetts series must contain ordered week indexes 1 through 94.")
    gaps = frame["week_end"].diff().dropna().dt.days
    if not bool((gaps == 7).all()):
        raise ValueError("Massachusetts week order is not consecutive.")
    component_sum = frame[["covid_new_admissions", "flu_new_admissions", "rsv_new_admissions"]].sum(axis=1)
    if not np.array_equal(component_sum.to_numpy(), frame["total_respiratory_new_admissions"].to_numpy()):
        raise ValueError("Forecast target no longer reconciles to the three source counts.")
    return frame


def target_contract(frame: pd.DataFrame) -> list[dict[str, object]]:
    return [{
        "contract_id": "FC01",
        "unit": "Massachusetts jurisdiction-week aggregate across reporting hospitals",
        "target": "total_respiratory_new_admissions",
        "source_unit": "new admissions reported in the week",
        "horizon_weeks": HORIZON,
        "refresh_cadence": "weekly teaching refresh after source verification",
        "first_source_week": frame.iloc[0]["week_end"].date().isoformat(),
        "last_source_week": frame.iloc[-1]["week_end"].date().isoformat(),
        "decision": "compare introductory forecasting methods under time-ordered backtesting",
        "prohibited_use": "single-hospital staffing, capacity, care, or deployment decision",
    }]


def fold_registry(frame: pd.DataFrame) -> list[dict[str, object]]:
    rows = []
    for number, origin in enumerate(FOLD_ORIGINS, start=1):
        rows.append({
            "fold_id": f"F{number:02d}", "train_start_index": 1, "train_end_index": origin,
            "train_rows": origin, "train_end_week": frame.iloc[origin - 1]["week_end"].date().isoformat(),
            "test_start_index": origin + 1, "test_end_index": origin + HORIZON,
            "test_rows": HORIZON, "test_start_week": frame.iloc[origin]["week_end"].date().isoformat(),
            "test_end_week": frame.iloc[origin + HORIZON - 1]["week_end"].date().isoformat(),
            "overlap_with_other_test_folds": "none", "future_rows_in_fit": 0,
        })
    return rows


def benchmark_registry() -> list[dict[str, object]]:
    return [
        {"model_id": "LAST", "role": "minimum benchmark", "eligible": "yes", "rule": "repeat the last observed training value", "information": "training rows only"},
        {"model_id": "SNAIVE52", "role": "seasonal benchmark", "eligible": "yes", "rule": "use the target from 52 weeks before each forecasted week", "information": "training rows only; every target has lag-52 history"},
        {"model_id": "HOLT_DAMPED", "role": "guided candidate", "eligible": "yes", "rule": "optimized additive level and damped trend, refit inside each fold", "information": "training rows only"},
        {"model_id": "ARIMA111", "role": "recognition example", "eligible": "no", "rule": "ARIMA(1,1,1) with drift fit once at final origin", "information": "read parameters and residual checks; not candidate-selected"},
    ]


def backtest(frame: pd.DataFrame) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    y = frame["total_respiratory_new_admissions"].astype(float).to_numpy()
    predictions: list[dict[str, object]] = []
    parameters: list[dict[str, object]] = []
    intervals: list[dict[str, object]] = []
    for number, origin in enumerate(FOLD_ORIGINS, start=1):
        fold_id = f"F{number:02d}"
        train = y[:origin]
        actual = y[origin:origin + HORIZON]
        fit = Holt(train, damped_trend=True, initialization_method="estimated").fit(optimized=True)
        candidate = np.asarray(fit.forecast(HORIZON), dtype=float)
        params = fit.params
        parameters.append({
            "fold_id": fold_id, "train_rows": origin,
            "smoothing_level": fixed(float(params["smoothing_level"])),
            "smoothing_trend": fixed(float(params["smoothing_trend"])),
            "damping_trend": fixed(float(params["damping_trend"])),
            "initial_level": fixed(float(params["initial_level"])),
            "initial_trend": fixed(float(params["initial_trend"])),
            "sse": fixed(float(fit.sse)), "optimization": "statsmodels optimized within fold",
        })
        sigma = float(np.sqrt(np.mean(np.square(np.asarray(fit.resid, dtype=float)))))
        model_predictions = {
            "LAST": np.repeat(train[-1], HORIZON),
            "SNAIVE52": np.asarray([y[index - SEASONAL_LAG] for index in range(origin, origin + HORIZON)]),
            "HOLT_DAMPED": candidate,
        }
        for model_id, values in model_predictions.items():
            for step, (value, observed) in enumerate(zip(values, actual, strict=True), start=1):
                row = frame.iloc[origin + step - 1]
                error = float(observed - value)
                predictions.append({
                    "fold_id": fold_id, "model_id": model_id, "origin_index": origin,
                    "origin_week": frame.iloc[origin - 1]["week_end"].date().isoformat(),
                    "horizon_week": step, "target_index": int(row["week_index"]),
                    "target_week": row["week_end"].date().isoformat(), "actual": fixed(float(observed)),
                    "prediction": fixed(float(value)), "error_actual_minus_prediction": fixed(error),
                    "absolute_error": fixed(abs(error)), "squared_error": fixed(error * error),
                    "absolute_percentage_error": fixed(abs(error) / float(observed) * 100.0),
                    "reporting_coverage_pct": fixed(float(row["hospitals_reporting_occupancy_pct"]), 2),
                    "future_rows_in_fit": 0,
                })
        for step, (value, observed) in enumerate(zip(candidate, actual, strict=True), start=1):
            margin = 1.96 * sigma * math.sqrt(step)
            lower, upper = max(0.0, float(value - margin)), float(value + margin)
            intervals.append({
                "fold_id": fold_id, "horizon_week": step, "target_index": origin + step,
                "target_week": frame.iloc[origin + step - 1]["week_end"].date().isoformat(),
                "prediction": fixed(float(value)), "lower95_reading": fixed(lower), "upper95_reading": fixed(upper),
                "actual": fixed(float(observed)), "covered": "yes" if lower <= observed <= upper else "no",
                "method": "1.96 times training residual RMSE times square root horizon; illustrative, not calibrated",
            })
    return predictions, parameters, intervals


def metric_rows(predictions: list[dict[str, object]], group_fields: tuple[str, ...]) -> list[dict[str, object]]:
    groups: dict[tuple[str, ...], list[dict[str, object]]] = {}
    for row in predictions:
        key = tuple(str(row[field]) for field in group_fields)
        groups.setdefault(key, []).append(row)
    output = []
    for key in sorted(groups):
        rows = groups[key]
        errors = np.asarray([float(row["error_actual_minus_prediction"]) for row in rows])
        item: dict[str, object] = {field: value for field, value in zip(group_fields, key, strict=True)}
        item.update({
            "predictions": len(rows), "mae": fixed(float(np.mean(np.abs(errors)))),
            "rmse": fixed(float(np.sqrt(np.mean(np.square(errors))))),
            "bias_actual_minus_prediction": fixed(float(np.mean(errors))),
            "mape_pct": fixed(float(np.mean([float(row["absolute_percentage_error"]) for row in rows]))),
            "minimum_actual": fixed(min(float(row["actual"]) for row in rows)),
            "maximum_actual": fixed(max(float(row["actual"]) for row in rows)),
            "unit": "reported new admissions per week",
        })
        output.append(item)
    return output


def failure_rows(predictions: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for model in ("LAST", "SNAIVE52", "HOLT_DAMPED"):
        selected = [row for row in predictions if row["model_id"] == model]
        errors = [float(row["error_actual_minus_prediction"]) for row in selected]
        worst = max(selected, key=lambda row: float(row["absolute_error"]))
        rows.append({
            "model_id": model, "underpredictions": sum(error > 0 for error in errors),
            "overpredictions": sum(error < 0 for error in errors), "exact_predictions": sum(error == 0 for error in errors),
            "worst_target_week": worst["target_week"], "worst_actual": worst["actual"],
            "worst_prediction": worst["prediction"], "worst_absolute_error": worst["absolute_error"],
            "failure_reading": "errors occur during a steep seasonal decline and late low-count turn; inspect, do not edit source values",
        })
    return rows


def decomposition_rows(frame: pd.DataFrame) -> list[dict[str, object]]:
    training = frame.iloc[:90].copy()
    target = training["total_respiratory_new_admissions"].astype(float)
    trend = target.rolling(window=13, center=True, min_periods=13).mean()
    return [{
        "week_index": int(row.week_index), "week_end": row.week_end.date().isoformat(),
        "observed": fixed(float(row.total_respiratory_new_admissions)),
        "centered_13_week_trend": "" if pd.isna(trend.iloc[index]) else fixed(float(trend.iloc[index])),
        "remainder_observed_minus_trend": "" if pd.isna(trend.iloc[index]) else fixed(float(target.iloc[index] - trend.iloc[index])),
        "fit_boundary": "final-origin training rows 1-90 only; descriptive decomposition, not causal explanation",
    } for index, row in enumerate(training.itertuples(index=False))]


def stationarity_rows(frame: pd.DataFrame) -> list[dict[str, object]]:
    y = frame.iloc[:90]["total_respiratory_new_admissions"].astype(float).to_numpy()
    rows = []
    for label, values in (("level", y), ("first difference", np.diff(y))):
        statistic, pvalue, used_lag, nobs, critical, _ = adfuller(values, autolag="AIC")
        rows.append({
            "series": label, "rows": len(values), "adf_statistic": fixed(float(statistic)),
            "p_value": fixed(float(pvalue)), "used_lag": int(used_lag), "nobs": int(nobs),
            "critical_5pct": fixed(float(critical["5%"])),
            "reading": "provided stationarity diagnostic; not a mechanical model-selection rule",
        })
    return rows


def arima_rows(frame: pd.DataFrame) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    y = frame["total_respiratory_new_admissions"].astype(float).to_numpy()
    train = y[:90]
    fit = ARIMA(train, order=(1, 1, 1), trend="t").fit()
    parameters = [{
        "model_id": "ARIMA111", "parameter": name, "estimate": fixed(float(value)),
        "std_error": fixed(float(error)), "role": "recognition only; not eligible in candidate comparison",
    } for name, value, error in zip(fit.param_names, fit.params, fit.bse, strict=True)]
    forecast = fit.get_forecast(steps=4)
    interval = np.asarray(forecast.conf_int(alpha=0.05), dtype=float)
    predictions = []
    for step, (predicted, bounds, actual) in enumerate(zip(forecast.predicted_mean, interval, y[90:94], strict=True), start=1):
        predictions.append({
            "model_id": "ARIMA111", "origin_index": 90, "horizon_week": step,
            "target_index": 90 + step, "target_week": frame.iloc[89 + step]["week_end"].date().isoformat(),
            "prediction": fixed(float(predicted)), "lower95_model_reading": fixed(float(bounds[0])),
            "upper95_model_reading": fixed(float(bounds[1])), "actual": fixed(float(actual)),
            "boundary": "provided ARIMA-family reading; not selected or approved for operations",
        })
    residuals = np.asarray(fit.resid, dtype=float)
    lb = acorr_ljungbox(residuals, lags=[4, 8], return_df=True)
    diagnostics = [{
        "model_id": "ARIMA111", "diagnostic": "Ljung-Box", "lag": int(lag),
        "statistic": fixed(float(lb.loc[lag, "lb_stat"])), "p_value": fixed(float(lb.loc[lag, "lb_pvalue"])),
        "reading": "residual autocorrelation check for recognition; p-value is not proof of adequacy",
    } for lag in (4, 8)]
    return parameters, predictions, diagnostics


def coverage_rows(frame: pd.DataFrame, predictions: list[dict[str, object]]) -> list[dict[str, object]]:
    candidate = {(row["fold_id"], int(row["target_index"])): row for row in predictions if row["model_id"] == "HOLT_DAMPED"}
    rows = []
    for number, origin in enumerate(FOLD_ORIGINS, start=1):
        fold_id = f"F{number:02d}"
        for index in range(origin, origin + HORIZON):
            source = frame.iloc[index]
            pred = candidate[(fold_id, index + 1)]
            rows.append({
                "fold_id": fold_id, "week_index": index + 1, "week_end": source["week_end"].date().isoformat(),
                "hospitals_reporting_occupancy": int(source["hospitals_reporting_occupancy"]),
                "hospitals_reporting_occupancy_pct": fixed(float(source["hospitals_reporting_occupancy_pct"]), 2),
                "reporting_gap_pct": fixed(float(source["reporting_gap_pct"]), 2),
                "actual_admissions": pred["actual"], "candidate_absolute_error": pred["absolute_error"],
                "use": "context only; never a correction weight or invented denominator",
            })
    return rows


def svg_forecast(frame: pd.DataFrame, predictions: list[dict[str, object]], intervals: list[dict[str, object]]) -> str:
    width, height, left, right, top, bottom = 960, 520, 80, 25, 55, 70
    plot_w, plot_h = width - left - right, height - top - bottom
    y_max = max(float(frame["total_respiratory_new_admissions"].max()), max(float(row["upper95_reading"]) for row in intervals))
    x = lambda index: left + (index - 1) / 93 * plot_w
    y = lambda value: top + (y_max - value) / y_max * plot_h
    actual_points = " ".join(f"{x(int(row.week_index)):.2f},{y(float(row.total_respiratory_new_admissions)):.2f}" for row in frame.itertuples())
    final = [row for row in predictions if row["fold_id"] == "F05"]
    colors = {"LAST": "#64748b", "SNAIVE52": "#d97706", "HOLT_DAMPED": "#0f766e"}
    lines = []
    for model_id in colors:
        rows = [row for row in final if row["model_id"] == model_id]
        points = [(90, float(frame.iloc[89]["total_respiratory_new_admissions"]))] + [(int(row["target_index"]), float(row["prediction"])) for row in rows]
        lines.append(f'<polyline fill="none" stroke="{colors[model_id]}" stroke-width="3" points="' + " ".join(f"{x(i):.2f},{y(v):.2f}" for i, v in points) + '"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Massachusetts weekly respiratory admissions and final backtest fold</title>
<desc id="desc">Actual reported jurisdiction totals for 94 weeks, with last-value, 52-week seasonal-naive, and damped-Holt predictions for weeks 91 through 94. Exact values are in forecast-predictions.csv.</desc>
<rect width="100%" height="100%" fill="#ffffff"/><text x="{left}" y="30" font-family="Arial" font-size="20" fill="#0f172a">Weekly reported respiratory admissions: final four-week fold</text>
<line x1="{left}" y1="{top + plot_h}" x2="{width-right}" y2="{top + plot_h}" stroke="#475569"/><line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" stroke="#475569"/>
<polyline fill="none" stroke="#1f49b6" stroke-width="2" points="{actual_points}"/>{''.join(lines)}
<text x="{left}" y="{height-25}" font-family="Arial" font-size="13" fill="#334155">Weeks 1-94; final forecast origin is week 90</text>
<text x="{left+480}" y="{height-25}" font-family="Arial" font-size="13" fill="#1f49b6">Actual</text><text x="{left+540}" y="{height-25}" font-family="Arial" font-size="13" fill="#64748b">Last</text><text x="{left+590}" y="{height-25}" font-family="Arial" font-size="13" fill="#d97706">Seasonal naive</text><text x="{left+700}" y="{height-25}" font-family="Arial" font-size="13" fill="#0f766e">Damped Holt</text>
</svg>'''


def check_rows(frame: pd.DataFrame, folds: list[dict[str, object]], predictions: list[dict[str, object]], metrics: list[dict[str, object]], intervals: list[dict[str, object]], coverage: list[dict[str, object]], arima_predictions: list[dict[str, object]]) -> list[dict[str, object]]:
    metric = {row["model_id"]: row for row in metrics}
    facts = [
        ("C01", len(frame), 94), ("C02", frame["week_index"].nunique(), 94),
        ("C03", int((frame["week_end"].diff().dropna().dt.days == 7).sum()), 93),
        ("C04", len(folds), 5), ("C05", sum(int(row["test_rows"]) for row in folds), 20),
        ("C06", sum(int(row["future_rows_in_fit"]) for row in folds), 0),
        ("C07", len(predictions), 60), ("C08", len([row for row in predictions if row["model_id"] == "LAST"]), 20),
        ("C09", len([row for row in predictions if row["model_id"] == "SNAIVE52"]), 20),
        ("C10", len([row for row in predictions if row["model_id"] == "HOLT_DAMPED"]), 20),
        ("C11", len(metrics), 3), ("C12", float(metric["HOLT_DAMPED"]["mae"]) < float(metric["LAST"]["mae"]), True),
        ("C13", float(metric["HOLT_DAMPED"]["mae"]) < float(metric["SNAIVE52"]["mae"]), True),
        ("C14", len(intervals), 20), ("C15", len(coverage), 20), ("C16", len(arima_predictions), 4),
        ("C17", int(frame["total_respiratory_new_admissions"].isna().sum()), 0),
        ("C18", int(frame.iloc[:90]["week_index"].max()), 90), ("C19", int(frame.iloc[90:]["week_index"].min()), 91),
        ("C20", int((frame["hospitals_reporting_occupancy_pct"] > 0).sum()), 94),
    ]
    return [{"check_id": check_id, "observed": str(observed), "expected": str(expected), "status": "pass" if observed == expected else "fail", "meaning": "frozen forecast-release invariant"} for check_id, observed, expected in facts]


def build_outputs(paths: dict[str, Path], target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_upstream(paths)
    frame = load_series(paths["ma-hospital-capacity-time-2024-2026.csv"])
    folds = fold_registry(frame)
    predictions, parameters, intervals = backtest(frame)
    aggregate = metric_rows(predictions, ("model_id",))
    fold_metrics = metric_rows(predictions, ("fold_id", "model_id"))
    horizon_metrics = metric_rows(predictions, ("horizon_week", "model_id"))
    arima_parameters, arima_predictions, residuals = arima_rows(frame)
    coverage = coverage_rows(frame, predictions)
    outputs: dict[str, list[dict[str, object]]] = {
        "forecast-target.csv": target_contract(frame), "temporal-folds.csv": folds,
        "benchmark-registry.csv": benchmark_registry(), "forecast-predictions.csv": predictions,
        "holt-parameters.csv": parameters, "forecast-interval-reading.csv": intervals,
        "aggregate-metrics.csv": aggregate, "fold-metrics.csv": fold_metrics,
        "horizon-metrics.csv": horizon_metrics, "failure-analysis.csv": failure_rows(predictions),
        "reporting-coverage-context.csv": coverage, "decomposition-reading.csv": decomposition_rows(frame),
        "stationarity-reading.csv": stationarity_rows(frame), "arima-parameters.csv": arima_parameters,
        "arima-forecast-reading.csv": arima_predictions, "residual-diagnostics.csv": residuals,
    }
    outputs["forecast-checks.csv"] = check_rows(frame, folds, predictions, aggregate, intervals, coverage, arima_predictions)
    failed = [row for row in outputs["forecast-checks.csv"] if row["status"] != "pass"]
    if failed:
        raise ValueError(f"Forecast release checks failed: {failed}")
    target.mkdir(parents=True)
    report: dict[str, object] = {
        "status": "pass", "version": "0.1.0", "upstream": {name: {"bytes": path.stat().st_size, "sha256": sha256(path)} for name, path in paths.items()},
        "series": {"rows": 94, "start": "2024-11-09", "end": "2026-08-22", "target": "total_respiratory_new_admissions"},
        "backtest": {"folds": 5, "horizon_weeks": 4, "test_predictions_per_model": 20, "test_week_indexes": "75-94"},
        "models": {row["model_id"]: {"mae": row["mae"], "rmse": row["rmse"], "bias_actual_minus_prediction": row["bias_actual_minus_prediction"], "mape_pct": row["mape_pct"]} for row in aggregate},
        "outputs": {}, "decision": {"reference": "continue to Module 06 with conditions", "candidate": "HOLT_DAMPED", "use": "public-data forecasting teaching only"},
    }
    for name, rows in outputs.items():
        path = target / name
        write_csv(path, rows)
        report["outputs"][name] = {"rows": len(rows), "fields": len(rows[0]), "bytes": path.stat().st_size, "sha256": sha256(path)}
    svg = target / "forecast.svg"
    svg.write_text(svg_forecast(frame, predictions, intervals), encoding="utf-8", newline="")
    report["outputs"]["forecast.svg"] = {"bytes": svg.stat().st_size, "sha256": sha256(svg)}
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
    shutil.copy2(MODULE_ROOT / "validate_forecast_evidence.py", target / "validate_forecast_evidence.py")
    data = target / "data"
    data.mkdir()
    for name, path in paths.items():
        shutil.copy2(path, data / name)
    return build_outputs(upstream_paths(data), target / "outputs")


def self_check() -> None:
    paths = upstream_paths()
    with tempfile.TemporaryDirectory(prefix="fnd2-module05-build-") as temp_dir:
        root = Path(temp_dir)
        first = root / "outputs"
        report = build_outputs(paths, first)
        assert report["backtest"]["folds"] == 5 and float(report["models"]["HOLT_DAMPED"]["mae"]) < float(report["models"]["LAST"]["mae"])
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
    print("FND-2 Module 05 builder self-check passed.")


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
