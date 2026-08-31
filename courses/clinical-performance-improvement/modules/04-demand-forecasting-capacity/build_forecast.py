"""Build deterministic APP-3 Module 04 forecast and capacity evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import statistics
import tempfile
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parent
UPSTREAM = ROOT / "upstream"
OUTPUT_NAMES = (
    "folds.csv",
    "forecast-predictions.csv",
    "error-summary.csv",
    "error-slices.csv",
    "week53-forecast.csv",
    "capacity-implication.csv",
    "littles-law-check.csv",
    "forecast-findings.json",
    "forecast-error-comparison.svg",
    "week53-demand-forecast.svg",
)
METHODS = ("last_value", "seasonal_naive", "seasonal_exponential_smoothing")
METHOD_LABELS = {
    "last_value": "Last value",
    "seasonal_naive": "Seasonal naive",
    "seasonal_exponential_smoothing": "Seasonal exponential smoothing",
}
PERIOD = 21
ALPHA = 0.30
GAMMA = 0.20


class ForecastError(RuntimeError):
    pass


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


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def f6(value: float) -> str:
    return f"{value:.6f}"


def round_half_up(value: float) -> int:
    return math.floor(value + 0.5)


def quantile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (position - lower) * (ordered[upper] - ordered[lower])


def season(value: str) -> str:
    month = datetime.strptime(value, "%Y-%m-%d").month
    if month in (12, 1, 2):
        return "winter"
    if month in (3, 4, 5):
        return "spring"
    if month in (6, 7, 8):
        return "summer"
    return "fall"


def seasonal_smoothing(train: list[int], horizon: int = PERIOD) -> list[float]:
    if len(train) < PERIOD * 2:
        raise ForecastError("Seasonal smoothing requires at least two complete weeks")
    level = sum(train[:PERIOD]) / PERIOD
    seasonal = [train[index] - level for index in range(PERIOD)]
    for index in range(PERIOD, len(train)):
        old_seasonal = seasonal[index - PERIOD]
        level = ALPHA * (train[index] - old_seasonal) + (1 - ALPHA) * level
        seasonal.append(GAMMA * (train[index] - level) + (1 - GAMMA) * old_seasonal)
    current_seasonal = seasonal[-PERIOD:]
    return [max(0.0, level + current_seasonal[index % PERIOD]) for index in range(horizon)]


def metrics(records: list[dict[str, object]]) -> dict[str, float]:
    errors = [float(row["forecast"]) - int(row["actual"]) for row in records]
    actual_total = sum(int(row["actual"]) for row in records)
    return {
        "mae": sum(abs(error) for error in errors) / len(errors),
        "rmse": math.sqrt(sum(error * error for error in errors) / len(errors)),
        "bias": sum(errors) / len(errors),
        "wape": 100 * sum(abs(error) for error in errors) / actual_total,
        "under": sum(-error for error in errors if error < 0),
        "over": sum(error for error in errors if error > 0),
        "actual_mean": actual_total / len(records),
        "forecast_mean": sum(float(row["forecast"]) for row in records) / len(records),
    }


def validate_source(rows: list[dict[str, str]]) -> None:
    if len(rows) != 1092:
        raise ForecastError(f"Expected 1,092 shifts, found {len(rows)}")
    expected_shifts = ("night", "day", "evening")
    for index, row in enumerate(rows):
        expected_week = index // PERIOD + 1
        if int(row["week_index"]) != expected_week:
            raise ForecastError(f"Shift order changed at {row['shift_id']}")
        if row["shift_name"] != expected_shifts[index % 3]:
            raise ForecastError(f"Within-day shift order changed at {row['shift_id']}")
        if row["synthetic_flag"] != "1" or int(row["arrivals"]) < 0:
            raise ForecastError(f"Invalid synthetic demand row: {row['shift_id']}")
    dates = [datetime.strptime(row["date"], "%Y-%m-%d").date() for row in rows]
    if dates[0] != date(2024, 1, 1) or dates[-1] != date(2024, 12, 29):
        raise ForecastError("Accepted date range changed")


def forecast_rows(source: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    arrivals = [int(row["arrivals"]) for row in source]
    predictions: list[dict[str, object]] = []
    folds: list[dict[str, object]] = []
    for test_week in range(25, 53):
        fold_id = f"F{test_week - 24:02d}"
        start = (test_week - 1) * PERIOD
        train = arrivals[:start]
        actual = arrivals[start:start + PERIOD]
        candidates = {
            "last_value": [float(train[-1])] * PERIOD,
            "seasonal_naive": [float(value) for value in train[-PERIOD:]],
            "seasonal_exponential_smoothing": seasonal_smoothing(train),
        }
        for method in METHODS:
            for horizon, (row, observed, predicted) in enumerate(
                zip(source[start:start + PERIOD], actual, candidates[method], strict=True), start=1
            ):
                predictions.append({
                    "fold_id": fold_id,
                    "method": method,
                    "target_shift_id": row["shift_id"],
                    "target_date": row["date"],
                    "shift_name": row["shift_name"],
                    "horizon_shift": horizon,
                    "actual": observed,
                    "forecast": predicted,
                    "holiday_flag": int(row["holiday_flag"]),
                    "special_event_flag": int(row["synthetic_special_event_flag"]),
                    "synthetic_flag": 1,
                })
        folds.append({
            "fold_id": fold_id,
            "issue_shift_id": source[start - 1]["shift_id"],
            "issue_date": source[start - 1]["date"],
            "train_start_week": 1,
            "train_end_week": test_week - 1,
            "train_rows": len(train),
            "test_week": test_week,
            "test_start_date": source[start]["date"],
            "test_end_date": source[start + PERIOD - 1]["date"],
            "horizon_shifts": PERIOD,
            "special_event_shifts": sum(int(row["synthetic_special_event_flag"]) for row in source[start:start + PERIOD]),
            "synthetic_flag": 1,
        })
    return predictions, folds


def select_method(predictions: list[dict[str, object]]) -> tuple[str, dict[str, dict[str, float]]]:
    by_method = {
        method: metrics([row for row in predictions if row["method"] == method])
        for method in METHODS
    }
    best_mae = min(result["mae"] for result in by_method.values())
    eligible = [method for method in METHODS if by_method[method]["mae"] <= best_mae + 0.25]
    return eligible[0], by_method


def build_error_slices(selected_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in selected_rows:
        day = datetime.strptime(str(row["target_date"]), "%Y-%m-%d").strftime("%A")
        keys = (
            ("shift", str(row["shift_name"])),
            ("day_of_week", day),
            ("holiday", "yes" if row["holiday_flag"] else "no"),
            ("special_event", "yes" if row["special_event_flag"] else "no"),
            ("season", season(str(row["target_date"]))),
        )
        for key in keys:
            grouped[key].append(row)
    type_order = {"shift": 0, "day_of_week": 1, "holiday": 2, "special_event": 3, "season": 4}
    rows = []
    for (slice_type, slice_value), records in sorted(grouped.items(), key=lambda item: (type_order[item[0][0]], item[0][1])):
        result = metrics(records)
        rows.append({
            "slice_type": slice_type,
            "slice_value": slice_value,
            "rows": len(records),
            "actual_mean_arrivals": f6(result["actual_mean"]),
            "forecast_mean_arrivals": f6(result["forecast_mean"]),
            "mae_arrivals": f6(result["mae"]),
            "rmse_arrivals": f6(result["rmse"]),
            "bias_arrivals": f6(result["bias"]),
            "underforecast_arrivals": f6(result["under"]),
            "overforecast_arrivals": f6(result["over"]),
            "support_status": "supported" if len(records) >= PERIOD else "not supported",
            "synthetic_flag": 1,
        })
    return rows


def little_law_rows(source: list[dict[str, str]]) -> list[dict[str, object]]:
    contexts = (
        ("baseline_all", "Weeks 1-24, all shifts", lambda row: int(row["week_index"]) <= 24),
        ("evaluation_all", "Weeks 25-52, all shifts", lambda row: int(row["week_index"]) >= 25),
        ("target_evening", "Weeks 35-44, evening shifts", lambda row: 35 <= int(row["week_index"]) <= 44 and row["shift_name"] == "evening"),
        ("recovery_evening", "Weeks 45-52, evening shifts", lambda row: 45 <= int(row["week_index"]) <= 52 and row["shift_name"] == "evening"),
    )
    output = []
    for context_id, label, keep in contexts:
        records = [row for row in source if keep(row)]
        rate = sum(int(row["arrivals"]) for row in records) / (8 * len(records))
        wait_hours = statistics.median(float(row["median_arrival_to_clinician_minutes"]) for row in records) / 60
        implied_queue = rate * wait_hours
        observed_queue = statistics.mean(float(row["mean_queue_end"]) for row in records)
        output.append({
            "context_id": context_id,
            "context": label,
            "shifts": len(records),
            "arrival_rate_per_hour": f6(rate),
            "median_arrival_to_clinician_hours": f6(wait_hours),
            "lambda_times_w": f6(implied_queue),
            "mean_queue_end_snapshot": f6(observed_queue),
            "signed_gap": f6(implied_queue - observed_queue),
            "equilibrium_status": "not established",
            "interpretation_limit": "rate uses arrivals, W is a median elapsed time, and L is a mean queue-end snapshot",
            "synthetic_flag": 1,
        })
    return output


def error_svg(summary: list[dict[str, object]]) -> str:
    width, height = 860, 430
    left, top, chart_height = 100, 70, 260
    max_mae = max(float(row["mae_arrivals"]) for row in summary)
    colors = ("#61758a", "#2d7d8a", "#1f49b6")
    bars = []
    for index, (row, color) in enumerate(zip(summary, colors, strict=True)):
        x = 150 + index * 230
        value = float(row["mae_arrivals"])
        bar_height = chart_height * value / (max_mae * 1.15)
        y = top + chart_height - bar_height
        bars.append(f'<rect x="{x}" y="{y:.1f}" width="120" height="{bar_height:.1f}" fill="{color}" />')
        bars.append(f'<text x="{x + 60}" y="{y - 10:.1f}" text-anchor="middle" font-size="17">{value:.3f}</text>')
        label = METHOD_LABELS[str(row["method"])].replace(" ", "&#160;")
        bars.append(f'<text x="{x + 60}" y="360" text-anchor="middle" font-size="14">{label}</text>')
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" role="img" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
        '<title>Mean absolute forecast error by transparent method</title>\n'
        '<desc>Seasonal exponential smoothing has the lowest mean absolute error at 5.937 arrivals per shift, followed by seasonal naive at 7.095 and last value at 10.776.</desc>\n'
        '<rect width="100%" height="100%" fill="#ffffff" />\n'
        '<text x="430" y="35" text-anchor="middle" font-size="23" font-weight="bold">Forecast error on 588 common shifts</text>\n'
        f'<line x1="{left}" y1="{top + chart_height}" x2="800" y2="{top + chart_height}" stroke="#1f2937" />\n'
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + chart_height}" stroke="#1f2937" />\n'
        '<text x="25" y="210" transform="rotate(-90 25 210)" text-anchor="middle" font-size="15">MAE, arrivals per shift</text>\n'
        + "\n".join(bars)
        + '\n<text x="430" y="410" text-anchor="middle" font-size="13">Lower is better. Exact values are available in error-summary.csv.</text>\n</svg>\n'
    )


def week53_svg(future: list[dict[str, object]], lower: float, upper: float) -> str:
    width, height = 1060, 470
    left, top, chart_width, chart_height = 70, 70, 930, 280
    values = [float(row["raw_forecast_arrivals"]) for row in future]
    max_value = max(values) * 1.15
    points = []
    labels = []
    for index, (row, value) in enumerate(zip(future, values, strict=True)):
        x = left + index * chart_width / (len(values) - 1)
        y = top + chart_height - chart_height * value / max_value
        points.append(f"{x:.1f},{y:.1f}")
        if index % 3 == 1:
            labels.append(f'<text x="{x:.1f}" y="380" text-anchor="middle" font-size="12">{str(row["date"])[5:]}</text>')
    circles = [f'<circle cx="{point.split(",")[0]}" cy="{point.split(",")[1]}" r="3" fill="#1f49b6" />' for point in points]
    total = sum(values)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" role="img" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
        '<title>Selected Week 53 arrival-demand forecast</title>\n'
        f'<desc>The 21-shift seasonal exponential-smoothing forecast totals {total:.3f} arrivals. The empirical 80 percent actual-equivalent weekly range is {lower:.3f} to {upper:.3f} arrivals.</desc>\n'
        '<rect width="100%" height="100%" fill="#ffffff" />\n'
        '<text x="530" y="34" text-anchor="middle" font-size="23" font-weight="bold">Week 53 forecast by eight-hour shift</text>\n'
        f'<line x1="{left}" y1="{top + chart_height}" x2="{left + chart_width}" y2="{top + chart_height}" stroke="#1f2937" />\n'
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + chart_height}" stroke="#1f2937" />\n'
        f'<polyline points="{" ".join(points)}" fill="none" stroke="#1f49b6" stroke-width="3" />\n'
        + "\n".join(circles + labels)
        + f'\n<text x="530" y="420" text-anchor="middle" font-size="15">Point total {total:.3f}; empirical weekly range {lower:.3f} to {upper:.3f} arrivals</text>\n'
        '<text x="530" y="448" text-anchor="middle" font-size="13">This is a synthetic planning forecast, not a staffing order or demand guarantee.</text>\n</svg>\n'
    )


def generate(target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    target.mkdir(parents=True)
    _, source = read_csv(UPSTREAM / "shift-metrics.csv")
    validate_source(source)
    predictions, folds = forecast_rows(source)
    selected, by_method = select_method(predictions)
    selected_rows = [row for row in predictions if row["method"] == selected]

    summary = []
    for method in METHODS:
        result = by_method[method]
        summary.append({
            "method": method,
            "evaluation_rows": len([row for row in predictions if row["method"] == method]),
            "mae_arrivals": f6(result["mae"]),
            "rmse_arrivals": f6(result["rmse"]),
            "bias_arrivals": f6(result["bias"]),
            "wape_percent": f6(result["wape"]),
            "underforecast_arrivals": f6(result["under"]),
            "overforecast_arrivals": f6(result["over"]),
            "selected_flag": 1 if method == selected else 0,
            "selection_reason": "lowest eligible MAE beyond the 0.25-arrival tie tolerance" if method == selected else "eligible comparison method",
            "synthetic_flag": 1,
        })

    fold_errors = []
    for fold in folds:
        records = [row for row in selected_rows if row["fold_id"] == fold["fold_id"]]
        result = metrics(records)
        actual_total = sum(int(row["actual"]) for row in records)
        forecast_total = sum(float(row["forecast"]) for row in records)
        fold.update({
            "selected_method": selected,
            "actual_arrivals": actual_total,
            "forecast_arrivals": f6(forecast_total),
            "forecast_error": f6(forecast_total - actual_total),
            "fold_mae_arrivals": f6(result["mae"]),
        })
        fold_errors.append(forecast_total - actual_total)

    error_slices = build_error_slices(selected_rows)
    next_forecast = seasonal_smoothing([int(row["arrivals"]) for row in source])
    first_future = datetime.strptime(source[-1]["date"], "%Y-%m-%d").date() + timedelta(days=1)
    shift_names = [row["shift_name"] for row in source[-PERIOD:]]
    future = []
    for index, (shift_name, value) in enumerate(zip(shift_names, next_forecast, strict=True)):
        target_date = first_future + timedelta(days=index // 3)
        future.append({
            "forecast_shift_id": f"{target_date:%Y%m%d}-{shift_name}",
            "date": target_date.isoformat(),
            "shift_name": shift_name,
            "horizon_shift": index + 1,
            "selected_method": selected,
            "raw_forecast_arrivals": f6(value),
            "planning_arrivals": round_half_up(value),
            "holiday_flag": 1 if target_date == date(2025, 1, 1) else 0,
            "prediction_status": "future synthetic planning estimate; actual unavailable",
            "synthetic_flag": 1,
        })

    point_forecast = sum(next_forecast)
    lower_arrivals = point_forecast - quantile(fold_errors, 0.90)
    upper_arrivals = point_forecast - quantile(fold_errors, 0.10)
    baseline_rows = [row for row in source if int(row["week_index"]) <= 24]
    anchor = statistics.median(float(row["clinician_staff_hours_per_arrival"]) for row in baseline_rows)
    weekly_hours: dict[int, float] = defaultdict(float)
    for row in baseline_rows:
        weekly_hours[int(row["week_index"])] += float(row["clinician_staff_hours"])
    historical_hours = list(weekly_hours.values())
    weekly_mae = statistics.mean(abs(error) for error in fold_errors)
    capacity_values = (
        ("C01", "baseline planning conversion", anchor, "clinician-hours per arrival", "Weeks 1-24", "median accepted shift value", "historical conversion, not required staffing"),
        ("C02", "historical weekly clinician-hours minimum", min(historical_hours), "clinician-hours", "Weeks 1-24", "accepted shift sum", "historical observation, not minimum safe capacity"),
        ("C03", "historical weekly clinician-hours median", statistics.median(historical_hours), "clinician-hours", "Weeks 1-24", "accepted shift sum", "historical observation, not a target"),
        ("C04", "historical weekly clinician-hours maximum", max(historical_hours), "clinician-hours", "Weeks 1-24", "accepted shift sum", "historical observation, not maximum useful capacity"),
        ("C05", "Week 53 raw forecast total", point_forecast, "arrivals", "Week 53", selected, "forecast, not guaranteed demand"),
        ("C06", "Week 53 rounded shift forecast total", float(sum(int(row["planning_arrivals"]) for row in future)), "arrivals", "Week 53", "sum of shift-level half-up rounding", "presentation total only"),
        ("C07", "Week 53 empirical lower actual-equivalent", lower_arrivals, "arrivals", "Week 53", "10th and 90th fold-total error inversion", "empirical range, not calibrated coverage"),
        ("C08", "Week 53 empirical upper actual-equivalent", upper_arrivals, "arrivals", "Week 53", "10th and 90th fold-total error inversion", "empirical range, not calibrated coverage"),
        ("C09", "Week 53 point planning conversion", point_forecast * anchor, "clinician-hours", "Week 53", "raw forecast times C01", "planning equivalent, not a staffing recommendation"),
        ("C10", "Week 53 lower planning conversion", lower_arrivals * anchor, "clinician-hours", "Week 53", "C07 times C01", "planning equivalent, not a staffing floor"),
        ("C11", "Week 53 upper planning conversion", upper_arrivals * anchor, "clinician-hours", "Week 53", "C08 times C01", "planning equivalent, not a staffing ceiling"),
        ("C12", "selected-model mean absolute weekly total error", weekly_mae, "arrivals", "28 evaluation weeks", "mean absolute fold-total error", "fold-total error remains operationally material"),
        ("C13", "weekly error planning conversion", weekly_mae * anchor, "clinician-hours", "28 evaluation weeks", "C12 times C01", "error equivalent, not observed shortage or excess"),
    )
    capacity = [{
        "quantity_id": item[0], "quantity": item[1], "value": f6(item[2]), "unit": item[3],
        "period": item[4], "source_or_rule": item[5], "interpretation_limit": item[6], "synthetic_flag": 1,
    } for item in capacity_values]
    little = little_law_rows(source)

    prediction_output = []
    for row in predictions:
        error = float(row["forecast"]) - int(row["actual"])
        prediction_output.append({
            "fold_id": row["fold_id"], "method": row["method"], "target_shift_id": row["target_shift_id"],
            "target_date": row["target_date"], "shift_name": row["shift_name"], "horizon_shift": row["horizon_shift"],
            "actual_arrivals": row["actual"], "forecast_arrivals": f6(float(row["forecast"])),
            "signed_error": f6(error), "absolute_error": f6(abs(error)), "squared_error": f6(error * error),
            "underforecast_arrivals": f6(max(0.0, -error)), "overforecast_arrivals": f6(max(0.0, error)),
            "holiday_flag": row["holiday_flag"], "special_event_flag": row["special_event_flag"],
            "synthetic_flag": 1,
        })

    selected_folds = sorted(folds, key=lambda row: float(row["fold_mae_arrivals"]), reverse=True)
    special_slice = next(row for row in error_slices if row["slice_type"] == "special_event" and row["slice_value"] == "yes")
    routine_slice = next(row for row in error_slices if row["slice_type"] == "special_event" and row["slice_value"] == "no")
    findings = {
        "schema_version": "1.0.0",
        "module_id": "oclc-app3-04",
        "module_version": "0.1.0",
        "commons_release": "0.70.0",
        "upstream": {"checkpoint_id": "oclc-app3-cp01", "candidate_files": 137, "frozen_files": 23, "shift_rows": 1092},
        "contract": {"target": "arrivals per eight-hour shift", "horizon_shifts": 21, "folds": 28, "evaluation_rows_per_method": 588, "seasonal_period_shifts": 21, "alpha": ALPHA, "gamma": GAMMA},
        "selected_method": selected,
        "method_metrics": {method: {key: round(value, 6) for key, value in by_method[method].items() if key in {"mae", "rmse", "bias", "wape", "under", "over"}} for method in METHODS},
        "failure_review": {
            "highest_mae_fold": selected_folds[0]["fold_id"],
            "highest_mae_test_week": selected_folds[0]["test_week"],
            "highest_fold_mae_arrivals": float(selected_folds[0]["fold_mae_arrivals"]),
            "special_event_mae_arrivals": float(special_slice["mae_arrivals"]),
            "routine_mae_arrivals": float(routine_slice["mae_arrivals"]),
        },
        "week53": {
            "start_date": future[0]["date"], "end_date": future[-1]["date"],
            "raw_forecast_arrivals": round(point_forecast, 6),
            "rounded_shift_total_arrivals": sum(int(row["planning_arrivals"]) for row in future),
            "empirical_actual_equivalent_lower": round(lower_arrivals, 6),
            "empirical_actual_equivalent_upper": round(upper_arrivals, 6),
        },
        "capacity": {
            "baseline_anchor_clinician_hours_per_arrival": round(anchor, 6),
            "point_planning_clinician_hours": round(point_forecast * anchor, 6),
            "lower_planning_clinician_hours": round(lower_arrivals * anchor, 6),
            "upper_planning_clinician_hours": round(upper_arrivals * anchor, 6),
            "historical_baseline_weekly_clinician_hours": {"minimum": min(historical_hours), "median": statistics.median(historical_hours), "maximum": max(historical_hours)},
            "staffing_recommendation": "not authorized",
        },
        "littles_law": {"rows": len(little), "equilibrium_status": "not established", "use": "bounded consistency check only"},
        "progression": "continue with conditions",
        "module05_permission": "permitted for improvement scenario and evaluation construction",
        "claim_limit": "synthetic forecast and planning implication only; no demand guarantee, staffing, productivity, equilibrium, root-cause, clinical, automated, causal, scenario-effect, or implementation authority",
    }

    write_csv(target / "folds.csv", list(folds[0]), folds)
    write_csv(target / "forecast-predictions.csv", list(prediction_output[0]), prediction_output)
    write_csv(target / "error-summary.csv", list(summary[0]), summary)
    write_csv(target / "error-slices.csv", list(error_slices[0]), error_slices)
    write_csv(target / "week53-forecast.csv", list(future[0]), future)
    write_csv(target / "capacity-implication.csv", list(capacity[0]), capacity)
    write_csv(target / "littles-law-check.csv", list(little[0]), little)
    (target / "forecast-findings.json").write_text(json.dumps(findings, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    (target / "forecast-error-comparison.svg").write_text(error_svg(summary), encoding="utf-8", newline="\n")
    (target / "week53-demand-forecast.svg").write_text(week53_svg(future, lower_arrivals, upper_arrivals), encoding="utf-8", newline="\n")
    if sorted(path.name for path in target.iterdir()) != sorted(OUTPUT_NAMES):
        raise ForecastError("Forecast output contract changed")
    return {"outputs": 10, "folds": 28, "prediction_rows": len(prediction_output), "selected_method": selected, "week53_raw_forecast": round(point_forecast, 6)}


def verify_committed() -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="app3-module04-forecast-") as temp_dir:
        rebuilt = Path(temp_dir) / "outputs"
        report = generate(rebuilt)
        for name in OUTPUT_NAMES:
            committed = ROOT / "outputs" / name
            if not committed.is_file() or committed.read_bytes() != (rebuilt / name).read_bytes():
                raise ForecastError(f"Committed output differs from clean rebuild: {name}")
    return report


def self_check() -> None:
    import freeze_upstream

    upstream = freeze_upstream.verify(ROOT)
    report = verify_committed()
    _, summary = read_csv(ROOT / "outputs/error-summary.csv")
    _, predictions = read_csv(ROOT / "outputs/forecast-predictions.csv")
    findings = json.loads((ROOT / "outputs/forecast-findings.json").read_text(encoding="utf-8"))
    expected = {
        "last_value": (10.775510, 13.291345, -3.391156, 27.479724),
        "seasonal_naive": (7.095238, 9.060079, -0.149660, 18.094288),
        "seasonal_exponential_smoothing": (5.937283, 7.307180, 0.008215, 15.141268),
    }
    for row in summary:
        observed = tuple(float(row[key]) for key in ("mae_arrivals", "rmse_arrivals", "bias_arrivals", "wape_percent"))
        if observed != expected[row["method"]]:
            raise AssertionError(f"Metric contract changed for {row['method']}: {observed}")
    assert upstream["shift_rows"] == 1092
    assert report == {"outputs": 10, "folds": 28, "prediction_rows": 1764, "selected_method": "seasonal_exponential_smoothing", "week53_raw_forecast": 876.924084}
    assert len(predictions) == 1764 and all(float(row["forecast_arrivals"]) >= 0 for row in predictions)
    assert findings["week53"] == {
        "start_date": "2024-12-30", "end_date": "2025-01-05", "raw_forecast_arrivals": 876.924084,
        "rounded_shift_total_arrivals": 878, "empirical_actual_equivalent_lower": 805.136639,
        "empirical_actual_equivalent_upper": 970.733035,
    }
    with tempfile.TemporaryDirectory(prefix="app3-module04-no-overwrite-") as temp_dir:
        existing = Path(temp_dir) / "existing"
        existing.mkdir()
        try:
            generate(existing)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Forecast builder overwrote an existing target")
    print(f"APP-3 Module 04 forecast self-check passed: {json.dumps(report, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.verify:
            print(json.dumps(verify_committed(), indent=2, sort_keys=True))
        elif args.write:
            print(json.dumps(generate((args.output or (ROOT / "outputs")).resolve()), indent=2, sort_keys=True))
        else:
            parser.error("use --write, --verify, or --self-check")
    except (OSError, ValueError, KeyError, ForecastError) as error:
        parser.exit(1, f"Forecast build failed: {error}\n")


if __name__ == "__main__":
    main()
