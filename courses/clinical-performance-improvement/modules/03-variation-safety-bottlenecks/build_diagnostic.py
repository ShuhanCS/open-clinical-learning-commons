"""Build the APP-3 Module 03 variation, safety, and bottleneck evidence."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import html
import json
import math
import shutil
import statistics
import tempfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASELINE_END = 24
OUTPUT_FILES = (
    "variation-series.csv", "control-limits.csv", "signal-audit.csv",
    "weekly-safety.csv", "safety-surveillance.csv", "process-stage-comparison.csv",
    "bottleneck-reconciliation.csv", "subgroup-window-support.csv",
    "diagnostic-findings.json", "weekly-arrival-to-clinician-xmr.svg",
    "weekly-left-before-seen-p-chart.svg", "weekly-incident-report-u-chart.svg",
    "process-stage-comparison.svg",
)


class DiagnosticError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path, compressed: bool = False) -> list[dict[str, str]]:
    opener = gzip.open if compressed else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def value(item: float | int | None, digits: int = 6) -> str:
    if item is None:
        return ""
    if isinstance(item, int):
        return str(item)
    return str(round(item, digits))


def poisson_quantile(expected: float, probability: float) -> int:
    if expected <= 0:
        return 0
    mass = math.exp(-expected)
    cumulative = mass
    count = 0
    while cumulative < probability:
        count += 1
        mass *= expected / count
        cumulative += mass
        if count > 10000:
            raise DiagnosticError("Poisson quantile did not converge")
    return count


def parse_time(text: str) -> datetime | None:
    return datetime.fromisoformat(text.replace("Z", "+00:00")) if text else None


def minutes(first: datetime | None, second: datetime | None) -> float | None:
    return (second - first).total_seconds() / 60 if first and second and second >= first else None


def signal_rows(chart_id: str, points: list[dict[str, object]], center: float, limits: bool = True) -> list[dict[str, object]]:
    signals: list[dict[str, object]] = []
    if limits:
        for point in points:
            observed = float(point["value"])
            lower = point.get("lower")
            upper = point.get("upper")
            if lower is not None and upper is not None and (observed < float(lower) or observed > float(upper)):
                signals.append({
                    "chart_id": chart_id, "rule_id": "R1", "signal_week": point["week"],
                    "start_week": point["week"], "end_week": point["week"],
                    "direction": "high" if observed > float(upper) else "low",
                    "observed_value": value(observed),
                    "boundary_value": value(float(upper) if observed > float(upper) else float(lower)),
                })

    sides = [1 if float(point["value"]) > center else -1 if float(point["value"]) < center else 0 for point in points]
    start = 0
    while start < len(points):
        side = sides[start]
        end = start + 1
        while side and end < len(points) and sides[end] == side:
            end += 1
        if side and end - start >= 8:
            signals.append({
                "chart_id": chart_id, "rule_id": "R2", "signal_week": points[start + 7]["week"],
                "start_week": points[start]["week"], "end_week": points[end - 1]["week"],
                "direction": "above" if side == 1 else "below",
                "observed_value": value(float(points[start + 7]["value"])), "boundary_value": value(center),
            })
        start = end if end > start else start + 1

    differences = [0]
    for index in range(1, len(points)):
        current = float(points[index]["value"])
        prior = float(points[index - 1]["value"])
        differences.append(1 if current > prior else -1 if current < prior else 0)
    start = 1
    while start < len(points):
        direction = differences[start]
        end = start + 1
        while direction and end < len(points) and differences[end] == direction:
            end += 1
        if direction and end - start >= 5:
            signals.append({
                "chart_id": chart_id, "rule_id": "R3", "signal_week": points[start + 4]["week"],
                "start_week": points[start - 1]["week"], "end_week": points[end - 1]["week"],
                "direction": "increasing" if direction == 1 else "decreasing",
                "observed_value": value(float(points[start + 4]["value"])), "boundary_value": "",
            })
        start = end if end > start else start + 1
    return signals


def svg_line(title: str, description: str, points: list[dict[str, object]], signal_weeks: set[int], unit: str) -> str:
    width, height = 960, 440
    left, right, top, bottom = 72, 30, 52, 58
    all_values = [float(row["value"]) for row in points]
    for row in points:
        for key in ("center", "lower", "upper"):
            if row.get(key) not in (None, ""):
                all_values.append(float(row[key]))
    low, high = min(all_values), max(all_values)
    padding = (high - low) * 0.08 or 1
    low -= padding
    high += padding

    def x(week: int) -> float:
        return left + (week - 1) * (width - left - right) / 51

    def y(number: float) -> float:
        return top + (high - number) * (height - top - bottom) / (high - low)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">{html.escape(title)}</title>",
        f"<desc id=\"desc\">{html.escape(description)}</desc>",
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{left}" y="28" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#172033">{html.escape(title)}</text>',
    ]
    for tick in range(5):
        number = low + tick * (high - low) / 4
        yy = y(number)
        lines.append(f'<line x1="{left}" y1="{yy:.2f}" x2="{width-right}" y2="{yy:.2f}" stroke="#d7dde8"/>')
        lines.append(f'<text x="{left-8}" y="{yy+4:.2f}" text-anchor="end" font-family="Arial, sans-serif" font-size="11" fill="#465166">{number:.1f}</text>')
    for week in (1, 8, 16, 24, 32, 40, 48, 52):
        xx = x(week)
        lines.append(f'<text x="{xx:.2f}" y="{height-32}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#465166">{week}</text>')
    for key, color, dash in (("upper", "#b33a3a", "6 4"), ("center", "#3a536f", ""), ("lower", "#b33a3a", "6 4")):
        available = [row for row in points if row.get(key) not in (None, "")]
        if available:
            coords = " ".join(f'{x(int(row["week"])):.2f},{y(float(row[key])):.2f}' for row in available)
            dashed = f' stroke-dasharray="{dash}"' if dash else ""
            lines.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="1.5"{dashed}/>')
    coords = " ".join(f'{x(int(row["week"])):.2f},{y(float(row["value"])):.2f}' for row in points)
    lines.append(f'<polyline points="{coords}" fill="none" stroke="#145da0" stroke-width="2"/>')
    for row in points:
        week = int(row["week"])
        xx, yy = x(week), y(float(row["value"]))
        if week in signal_weeks:
            lines.append(f'<rect x="{xx-4:.2f}" y="{yy-4:.2f}" width="8" height="8" fill="#c43b32" stroke="#172033"><title>Week {week} signal: {float(row["value"]):.3f} {html.escape(unit)}</title></rect>')
            lines.append(f'<text x="{xx:.2f}" y="{yy-8:.2f}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="#8c1d18">S</text>')
        else:
            lines.append(f'<circle cx="{xx:.2f}" cy="{yy:.2f}" r="2.4" fill="#145da0"><title>Week {week}: {float(row["value"]):.3f} {html.escape(unit)}</title></circle>')
    lines.extend([
        f'<text x="{(left+width-right)/2:.2f}" y="{height-8}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#172033">Week</text>',
        f'<text x="15" y="{height/2:.2f}" transform="rotate(-90 15 {height/2:.2f})" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#172033">{html.escape(unit)}</text>',
        f'<rect x="{width-225}" y="20" width="8" height="8" fill="#c43b32" stroke="#172033"/><text x="{width-211}" y="28" font-family="Arial, sans-serif" font-size="10" fill="#172033">S = predeclared signal</text>',
        "</svg>\n",
    ])
    return "\n".join(lines)


def svg_stage(rows: list[dict[str, object]]) -> str:
    width, height = 1040, 500
    left, right, top, bottom = 80, 30, 70, 110
    contexts = ["baseline_evening", "target_evening", "contemporaneous_day_night", "recovery_evening"]
    context_labels = ["Baseline evening", "Target evening", "Day/night control", "Recovery evening"]
    stages = ["arrival_to_triage", "triage_to_roomed", "roomed_to_clinician", "clinician_to_disposition", "disposition_to_departure"]
    stage_labels = ["Arrival to triage", "Triage to roomed", "Roomed to clinician", "Clinician to disposition", "Disposition to departure"]
    lookup = {(str(row["context_id"]), str(row["stage_id"])): float(row["median_minutes"]) for row in rows}
    maximum = max(lookup.values()) * 1.12
    plot_width = width - left - right
    plot_height = height - top - bottom
    group_width = plot_width / len(stages)
    bar_width = group_width / 5
    colors = ["#4c78a8", "#e45756", "#72b7b2", "#f2cf5b"]
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Median process-stage time across four predeclared comparisons</title>',
        '<desc id="desc">Grouped bars show baseline evening, target evening in Weeks 35 through 44, contemporaneous day and night, and recovery evening medians for five process stages. Every bar has a numeric label.</desc>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{left}" y="30" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#172033">Median process-stage time</text>',
    ]
    for tick in range(5):
        number = tick * maximum / 4
        yy = top + plot_height - number / maximum * plot_height
        lines.append(f'<line x1="{left}" y1="{yy:.2f}" x2="{width-right}" y2="{yy:.2f}" stroke="#d7dde8"/>')
        lines.append(f'<text x="{left-8}" y="{yy+4:.2f}" text-anchor="end" font-family="Arial, sans-serif" font-size="11" fill="#465166">{number:.0f}</text>')
    for stage_index, stage in enumerate(stages):
        group_x = left + stage_index * group_width
        for context_index, context in enumerate(contexts):
            number = lookup[(context, stage)]
            bar_height = number / maximum * plot_height
            xx = group_x + (context_index + 0.45) * bar_width
            yy = top + plot_height - bar_height
            abbreviation = ["B", "T", "C", "R"][context_index]
            lines.append(f'<rect x="{xx:.2f}" y="{yy:.2f}" width="{bar_width*.8:.2f}" height="{bar_height:.2f}" fill="{colors[context_index]}"><title>{html.escape(context_labels[context_index])}, {html.escape(stage_labels[stage_index])}: {number:.1f} minutes</title></rect>')
            lines.append(f'<text x="{xx+bar_width*.4:.2f}" y="{yy-4:.2f}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="#172033">{abbreviation} {number:.0f}</text>')
        label_x = group_x + group_width / 2
        lines.append(f'<text x="{label_x:.2f}" y="{height-bottom+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#172033">{html.escape(stage_labels[stage_index])}</text>')
    for index, label in enumerate(context_labels):
        xx = left + index * 210
        lines.append(f'<rect x="{xx}" y="{height-40}" width="11" height="11" fill="{colors[index]}"/><text x="{xx+16}" y="{height-30}" font-family="Arial, sans-serif" font-size="11" fill="#172033">{["B", "T", "C", "R"][index]} = {html.escape(label)}</text>')
    lines.extend([
        f'<text x="18" y="{height/2:.2f}" transform="rotate(-90 18 {height/2:.2f})" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#172033">Median minutes</text>',
        "</svg>\n",
    ])
    return "\n".join(lines)


def build(root: Path, output: Path) -> dict[str, object]:
    import freeze_upstream

    root = root.resolve()
    output = output.resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"Refusing to overwrite nonempty output target: {output}")
    output.mkdir(parents=True, exist_ok=True)
    handoff = freeze_upstream.verify(root)
    upstream = root / "upstream"
    weekly = read_csv(upstream / "weekly-metrics.csv")
    shifts = read_csv(upstream / "shift-metrics.csv")
    encounters = read_csv(upstream / "encounter-measures.csv.gz", compressed=True)
    safety = read_csv(upstream / "safety-events.csv.gz", compressed=True)
    if len(weekly) != 52 or len(shifts) != 1092 or len(encounters) != 43628:
        raise DiagnosticError("Upstream analytic shapes changed")

    weekly.sort(key=lambda row: int(row["week_index"]))
    baseline = [row for row in weekly if int(row["week_index"]) <= BASELINE_END]
    p_center = sum(int(row["left_before_seen"]) for row in baseline) / sum(int(row["arrivals"]) for row in baseline)
    x_values = [float(row["shift_median_arrival_to_clinician_mean"]) for row in baseline]
    x_center = statistics.mean(x_values)
    mr_bar = statistics.mean(abs(x_values[index] - x_values[index - 1]) for index in range(1, len(x_values)))
    x_lower, x_upper = x_center - 2.66 * mr_bar, x_center + 2.66 * mr_bar
    mr_upper = 3.267 * mr_bar
    arrivals_center = statistics.median(int(row["arrivals"]) for row in baseline)

    encounter_by_id = {row["encounter_id"]: row for row in encounters}
    weekly_safety = {index: {
        "week_index": index, "completed_encounters": 0, "known_true_events": 0,
        "trigger_true_positives": 0, "incident_true_positives": 0,
        "trigger_false_positives": 0, "reviewed_non_events": 0,
    } for index in range(1, 53)}
    for row in encounters:
        if row["completed_flag"] == "1":
            weekly_safety[int(row["week_index"])]["completed_encounters"] += 1
    accepted_safety: list[dict[str, str]] = []
    seen_candidates: set[str] = set()
    for row in safety:
        if row["candidate_id"] in seen_candidates or row["encounter_id"] not in encounter_by_id:
            continue
        seen_candidates.add(row["candidate_id"])
        accepted_safety.append(row)
        week = int(encounter_by_id[row["encounter_id"]]["week_index"])
        target = weekly_safety[week]
        truth = int(row["known_true_event_flag"])
        trigger = int(row["trigger_flag"])
        incident = int(row["incident_report_flag"])
        target["known_true_events"] += truth
        target["trigger_true_positives"] += int(truth == 1 and trigger == 1)
        target["incident_true_positives"] += int(truth == 1 and incident == 1)
        target["trigger_false_positives"] += int(truth == 0 and trigger == 1)
        target["reviewed_non_events"] += int(row["event_class"] == "reviewed_non_event")
    baseline_safety = [weekly_safety[index] for index in range(1, BASELINE_END + 1)]
    u_center = sum(int(row["incident_true_positives"]) for row in baseline_safety) / sum(int(row["completed_encounters"]) for row in baseline_safety)

    charts: dict[str, list[dict[str, object]]] = {"C01": [], "C02": [], "C03": [], "C04": []}
    prior_x: float | None = None
    for row in weekly:
        week = int(row["week_index"])
        arrivals = int(row["arrivals"])
        lbbs = int(row["left_before_seen"])
        p_value = 100 * lbbs / arrivals
        p_sigma = math.sqrt(p_center * (1 - p_center) / arrivals)
        charts["C01"].append({"week": week, "value": p_value, "center": 100 * p_center, "lower": 100 * max(0, p_center - 3 * p_sigma), "upper": 100 * min(1, p_center + 3 * p_sigma), "numerator": lbbs, "denominator": arrivals, "moving_range": None, "moving_range_upper": None})
        x_value = float(row["shift_median_arrival_to_clinician_mean"])
        charts["C02"].append({"week": week, "value": x_value, "center": x_center, "lower": x_lower, "upper": x_upper, "numerator": None, "denominator": 3, "moving_range": abs(x_value - prior_x) if prior_x is not None else None, "moving_range_upper": mr_upper})
        prior_x = x_value
        safety_row = weekly_safety[week]
        completed = int(safety_row["completed_encounters"])
        incidents = int(safety_row["incident_true_positives"])
        expected = u_center * completed
        low_count = poisson_quantile(expected, 0.00135)
        high_count = poisson_quantile(expected, 0.99865)
        charts["C03"].append({"week": week, "value": 1000 * incidents / completed, "center": 1000 * u_center, "lower": 1000 * low_count / completed, "upper": 1000 * high_count / completed, "numerator": incidents, "denominator": completed, "moving_range": None, "moving_range_upper": None})
        charts["C04"].append({"week": week, "value": arrivals, "center": arrivals_center, "lower": None, "upper": None, "numerator": arrivals, "denominator": None, "moving_range": None, "moving_range_upper": None})

    signals = []
    for chart_id, points in charts.items():
        signals.extend(signal_rows(chart_id, points, float(points[0]["center"]), limits=chart_id != "C04"))
    signals.sort(key=lambda row: (str(row["chart_id"]), int(row["signal_week"]), str(row["rule_id"])))
    for index, row in enumerate(signals, 1):
        row["signal_id"] = f"S{index:03d}"
        row["review_disposition"] = "review generated context; signal is not proof of cause"
        row["claim_limit"] = "synthetic service only; no automated action"
    signal_by_week: dict[tuple[str, int], list[str]] = defaultdict(list)
    for row in signals:
        signal_by_week[(str(row["chart_id"]), int(row["signal_week"]))].append(str(row["signal_id"]))

    chart_names = {
        "C01": ("weekly_left_before_seen", "p-chart", "percent"),
        "C02": ("weekly_arrival_to_clinician", "XmR", "minutes"),
        "C03": ("weekly_incident_reports", "exact Poisson u-chart", "reports per 1000 completed encounters"),
        "C04": ("weekly_arrivals", "run chart", "encounters"),
    }
    variation_rows: list[dict[str, object]] = []
    for chart_id, points in charts.items():
        measure, family, unit = chart_names[chart_id]
        for point in points:
            week = int(point["week"])
            variation_rows.append({
                "chart_id": chart_id, "measure": measure, "chart_family": family,
                "week_index": week, "baseline_status": "baseline" if week <= BASELINE_END else "evaluation",
                "numerator": value(point["numerator"]), "denominator": value(point["denominator"]),
                "value": value(float(point["value"])), "unit": unit,
                "centerline": value(float(point["center"])), "lower_limit": value(point["lower"]),
                "upper_limit": value(point["upper"]), "moving_range": value(point["moving_range"]),
                "moving_range_upper_limit": value(point["moving_range_upper"]),
                "signal_ids": "|".join(signal_by_week[(chart_id, week)]),
                "interpretation_status": "review signal; do not infer cause" if signal_by_week[(chart_id, week)] else "no predeclared signal at this point",
                "synthetic_flag": 1,
            })
    variation_fields = ["chart_id", "measure", "chart_family", "week_index", "baseline_status", "numerator", "denominator", "value", "unit", "centerline", "lower_limit", "upper_limit", "moving_range", "moving_range_upper_limit", "signal_ids", "interpretation_status", "synthetic_flag"]
    write_csv(output / "variation-series.csv", variation_fields, variation_rows)

    control_rows = [
        {"chart_id": "C01", "measure": "weekly_left_before_seen", "chart_family": "p-chart", "baseline_weeks": "1-24", "centerline": value(100 * p_center), "lower_limit_rule": "max(0,pbar-3*sqrt(pbar*(1-pbar)/n))*100", "upper_limit_rule": "min(1,pbar+3*sqrt(pbar*(1-pbar)/n))*100", "moving_range_center": "", "moving_range_upper": "", "low_count_rule": "not applicable", "decision_use": "detect a change in the weekly balancing proportion", "interpretation_limit": "signal is not cause"},
        {"chart_id": "C02", "measure": "weekly_arrival_to_clinician", "chart_family": "XmR", "baseline_weeks": "1-24", "centerline": value(x_center), "lower_limit_rule": value(x_lower), "upper_limit_rule": value(x_upper), "moving_range_center": value(mr_bar), "moving_range_upper": value(mr_upper), "low_count_rule": "not applicable", "decision_use": "detect a change in weekly clinician-delay summary", "interpretation_limit": "weekly value is a mean of three shift medians"},
        {"chart_id": "C03", "measure": "weekly_incident_reports", "chart_family": "exact Poisson u-chart", "baseline_weeks": "1-24", "centerline": value(1000 * u_center), "lower_limit_rule": "Poisson 0.00135 count quantile divided by weekly completed encounters times 1000", "upper_limit_rule": "Poisson 0.99865 count quantile divided by weekly completed encounters times 1000", "moving_range_center": "", "moving_range_upper": "", "low_count_rule": "preserve integer count limits and zero boundary", "decision_use": "review changes in synthetic incident-report capture", "interpretation_limit": "incident-report rate is not event prevalence"},
        {"chart_id": "C04", "measure": "weekly_arrivals", "chart_family": "run chart", "baseline_weeks": "1-24", "centerline": value(arrivals_center), "lower_limit_rule": "not calculated", "upper_limit_rule": "not calculated", "moving_range_center": "", "moving_range_upper": "", "low_count_rule": "not applicable", "decision_use": "show temporal demand pattern before Module 04 forecasting", "interpretation_limit": "seasonal and calendar structure makes unadjusted control limits inappropriate"},
    ]
    control_fields = ["chart_id", "measure", "chart_family", "baseline_weeks", "centerline", "lower_limit_rule", "upper_limit_rule", "moving_range_center", "moving_range_upper", "low_count_rule", "decision_use", "interpretation_limit"]
    write_csv(output / "control-limits.csv", control_fields, control_rows)
    signal_fields = ["signal_id", "chart_id", "rule_id", "signal_week", "start_week", "end_week", "direction", "observed_value", "boundary_value", "review_disposition", "claim_limit"]
    write_csv(output / "signal-audit.csv", signal_fields, signals)

    weekly_safety_rows: list[dict[str, object]] = []
    for week in range(1, 53):
        row = weekly_safety[week]
        completed = int(row["completed_encounters"])
        truth = int(row["known_true_events"])
        tp = int(row["trigger_true_positives"])
        reports = int(row["incident_true_positives"])
        fp = int(row["trigger_false_positives"])
        negatives = completed - truth
        weekly_safety_rows.append({
            **row,
            "trigger_sensitivity_percent": value(100 * tp / truth if truth else None, 4),
            "incident_capture_percent": value(100 * reports / truth if truth else None, 4),
            "trigger_specificity_percent": value(100 * (negatives - fp) / negatives if negatives else None, 4),
            "incident_reports_per_1000_completed": value(1000 * reports / completed, 4),
            "synthetic_flag": 1,
        })
    weekly_safety_fields = ["week_index", "completed_encounters", "known_true_events", "trigger_true_positives", "incident_true_positives", "trigger_false_positives", "reviewed_non_events", "trigger_sensitivity_percent", "incident_capture_percent", "trigger_specificity_percent", "incident_reports_per_1000_completed", "synthetic_flag"]
    write_csv(output / "weekly-safety.csv", weekly_safety_fields, weekly_safety_rows)

    class_order = ["overall", "error", "near_miss", "adverse_event", "harm", "reviewed_non_event"]
    class_counts: dict[str, dict[str, int]] = {name: {"known": 0, "trigger_tp": 0, "incident_tp": 0, "trigger_fp": 0, "reviewed": 0} for name in class_order}
    for row in accepted_safety:
        event_class = row["event_class"]
        truth = int(row["known_true_event_flag"])
        trigger = int(row["trigger_flag"])
        incident = int(row["incident_report_flag"])
        for key in ("overall", event_class):
            target = class_counts[key]
            target["known"] += truth
            target["trigger_tp"] += int(truth == 1 and trigger == 1)
            target["incident_tp"] += int(truth == 1 and incident == 1)
            target["trigger_fp"] += int(truth == 0 and trigger == 1)
            target["reviewed"] += 1
    safety_rows: list[dict[str, object]] = []
    completed_total = sum(int(row["completed_encounters"]) for row in weekly_safety.values())
    for event_class in class_order:
        counts = class_counts[event_class]
        known = counts["known"]
        negatives = completed_total - known if event_class == "overall" else None
        safety_rows.append({
            "event_class": event_class, "completed_encounters": completed_total,
            "reviewed_candidates": counts["reviewed"], "known_true_events": known,
            "trigger_true_positives": counts["trigger_tp"], "incident_true_positives": counts["incident_tp"],
            "trigger_false_positives": counts["trigger_fp"],
            "trigger_sensitivity_percent": value(100 * counts["trigger_tp"] / known if known else None, 4),
            "incident_capture_percent": value(100 * counts["incident_tp"] / known if known else None, 4),
            "trigger_specificity_percent": value(100 * (negatives - counts["trigger_fp"]) / negatives if negatives else None, 4),
            "surveillance_limit": "reviewed non-event" if event_class == "reviewed_non_event" else "synthetic detection performance; not prevalence",
            "synthetic_flag": 1,
        })
    safety_fields = ["event_class", "completed_encounters", "reviewed_candidates", "known_true_events", "trigger_true_positives", "incident_true_positives", "trigger_false_positives", "trigger_sensitivity_percent", "incident_capture_percent", "trigger_specificity_percent", "surveillance_limit", "synthetic_flag"]
    write_csv(output / "safety-surveillance.csv", safety_fields, safety_rows)

    for row in encounters:
        times = [parse_time(row[name]) for name in ("arrival_at", "triage_at", "roomed_at", "clinician_at", "disposition_at", "departure_at")]
        row["_stages"] = [minutes(times[index], times[index + 1]) for index in range(5)]  # type: ignore[assignment]
    contexts = [
        ("baseline_evening", "Weeks 1-24 evening", lambda row: row["shift_name"] == "evening" and int(row["week_index"]) <= 24),
        ("target_evening", "Weeks 35-44 evening", lambda row: row["shift_name"] == "evening" and 35 <= int(row["week_index"]) <= 44),
        ("contemporaneous_day_night", "Weeks 35-44 day and night", lambda row: row["shift_name"] != "evening" and 35 <= int(row["week_index"]) <= 44),
        ("recovery_evening", "Weeks 45-52 evening", lambda row: row["shift_name"] == "evening" and 45 <= int(row["week_index"]) <= 52),
    ]
    stages = [
        ("arrival_to_triage", 0), ("triage_to_roomed", 1), ("roomed_to_clinician", 2),
        ("clinician_to_disposition", 3), ("disposition_to_departure", 4),
    ]
    stage_rows: list[dict[str, object]] = []
    for context_id, context, predicate in contexts:
        selected = [row for row in encounters if predicate(row) and row["completed_flag"] == "1"]
        for stage_id, stage_index in stages:
            values = [float(row["_stages"][stage_index]) for row in selected if row["_stages"][stage_index] is not None]  # type: ignore[index]
            stage_rows.append({
                "context_id": context_id, "context": context, "stage_id": stage_id,
                "eligible_completed_encounters": len(selected), "available_clocks": len(values),
                "unavailable_clocks": len(selected) - len(values), "median_minutes": value(statistics.median(values), 3),
                "mean_minutes": value(statistics.mean(values), 3), "synthetic_flag": 1,
            })
    stage_fields = ["context_id", "context", "stage_id", "eligible_completed_encounters", "available_clocks", "unavailable_clocks", "median_minutes", "mean_minutes", "synthetic_flag"]
    write_csv(output / "process-stage-comparison.csv", stage_fields, stage_rows)

    def encounter_summary(predicate: object) -> dict[str, float]:
        selected = [row for row in encounters if predicate(row)]  # type: ignore[operator]
        return {"accepted": len(selected), "lbbs_percent": 100 * sum(int(row["left_before_seen_flag"]) for row in selected) / len(selected)}

    def shift_summary(predicate: object) -> dict[str, float]:
        selected = [row for row in shifts if predicate(row)]  # type: ignore[operator]
        def median_field(name: str) -> float:
            values = [float(row[name]) for row in selected if row[name] != ""]
            return statistics.median(values)
        return {
            "shifts": len(selected), "arrival_to_clinician": median_field("median_arrival_to_clinician_minutes"),
            "mean_queue_end": median_field("mean_queue_end"), "max_queue_end": median_field("max_queue_end"),
            "throughput_per_clinician_hour": median_field("completed_encounters_per_clinician_hour"),
            "clinician_hours_per_arrival": median_field("clinician_staff_hours_per_arrival"),
            "overtime_per_shift": sum(float(row["overtime_hours"]) for row in selected) / len(selected),
        }

    context_predicates = {
        "baseline": lambda row: row["shift_name"] == "evening" and int(row["week_index"]) <= 24,
        "target": lambda row: row["shift_name"] == "evening" and 35 <= int(row["week_index"]) <= 44,
        "control": lambda row: row["shift_name"] != "evening" and 35 <= int(row["week_index"]) <= 44,
        "recovery": lambda row: row["shift_name"] == "evening" and 45 <= int(row["week_index"]) <= 52,
    }
    encounter_summaries = {name: encounter_summary(predicate) for name, predicate in context_predicates.items()}
    shift_summaries = {name: shift_summary(predicate) for name, predicate in context_predicates.items()}
    stage_lookup = {(row["context_id"], row["stage_id"]): float(row["median_minutes"]) for row in stage_rows}
    metrics = [
        ("roomed_to_clinician_median", "minutes", {"baseline": stage_lookup[("baseline_evening", "roomed_to_clinician")], "target": stage_lookup[("target_evening", "roomed_to_clinician")], "control": stage_lookup[("contemporaneous_day_night", "roomed_to_clinician")], "recovery": stage_lookup[("recovery_evening", "roomed_to_clinician")]}, "yes", "localizes the constrained stage but not its root cause"),
        ("arrival_to_clinician_shift_median", "minutes", {name: summary["arrival_to_clinician"] for name, summary in shift_summaries.items()}, "yes", "shift median does not identify a single encounter cause"),
        ("mean_queue_end_shift_median", "encounters waiting", {name: summary["mean_queue_end"] for name, summary in shift_summaries.items()}, "yes", "queue supports congestion but not cause"),
        ("max_queue_end_shift_median", "encounters waiting", {name: summary["max_queue_end"] for name, summary in shift_summaries.items()}, "yes", "maximum is sensitive to short intervals"),
        ("completed_per_clinician_hour_shift_median", "encounters per hour", {name: summary["throughput_per_clinician_hour"] for name, summary in shift_summaries.items()}, "partial", "lower than baseline but not lower than the contemporaneous control; not a productivity target"),
        ("clinician_hours_per_arrival_shift_median", "hours per encounter", {name: summary["clinician_hours_per_arrival"] for name, summary in shift_summaries.items()}, "no", "descriptive staffing evidence does not establish cause or adequacy"),
        ("left_before_seen_percent", "percent", {name: summary["lbbs_percent"] for name, summary in encounter_summaries.items()}, "yes", "balancing signal does not explain why an encounter left"),
        ("overtime_hours_per_shift", "hours", {name: summary["overtime_per_shift"] for name, summary in shift_summaries.items()}, "no", "does not establish burden or authorize staffing change"),
    ]
    bottleneck_rows = [{
        "evidence_id": f"B{index:02d}", "metric": name, "unit": unit,
        "baseline_evening": value(values["baseline"], 4), "target_evening": value(values["target"], 4),
        "contemporaneous_day_night": value(values["control"], 4), "recovery_evening": value(values["recovery"], 4),
        "target_minus_baseline": value(values["target"] - values["baseline"], 4),
        "supports_bounded_diagnosis": supports, "interpretation_limit": limit,
    } for index, (name, unit, values, supports, limit) in enumerate(metrics, 1)]
    bottleneck_fields = ["evidence_id", "metric", "unit", "baseline_evening", "target_evening", "contemporaneous_day_night", "recovery_evening", "target_minus_baseline", "supports_bounded_diagnosis", "interpretation_limit"]
    write_csv(output / "bottleneck-reconciliation.csv", bottleneck_fields, bottleneck_rows)

    subgroup_rows: list[dict[str, object]] = []
    windows = [
        ("full_release", "Weeks 1-52 all shifts", lambda row: True),
        ("target_evening", "Weeks 35-44 evening", context_predicates["target"]),
    ]
    for window_id, window, predicate in windows:
        for group in ("language_support", "mobility_support", "standard"):
            selected = [row for row in encounters if predicate(row) and row["access_support_group"] == group]  # type: ignore[operator]
            clinician = [float(row["arrival_to_clinician_minutes"]) for row in selected if row["arrival_to_clinician_minutes"]]
            lbbs = sum(int(row["left_before_seen_flag"]) for row in selected)
            subgroup_rows.append({
                "window_id": window_id, "window": window, "access_support_group": group,
                "eligible_encounters": len(selected), "clinician_time_available": len(clinician),
                "clinician_time_unavailable": len(selected) - len(clinician), "left_before_seen": lbbs,
                "left_before_seen_percent": value(100 * lbbs / len(selected), 4),
                "median_arrival_to_clinician_minutes": value(statistics.median(clinician), 3),
                "teaching_support_threshold": 1000,
                "support_status": "supported" if len(selected) >= 1000 else "not supported",
                "interpretation_limit": "synthetic support check; no real disparity or causal claim",
            })
    subgroup_fields = ["window_id", "window", "access_support_group", "eligible_encounters", "clinician_time_available", "clinician_time_unavailable", "left_before_seen", "left_before_seen_percent", "median_arrival_to_clinician_minutes", "teaching_support_threshold", "support_status", "interpretation_limit"]
    write_csv(output / "subgroup-window-support.csv", subgroup_fields, subgroup_rows)

    signal_fields = {(row["chart_id"], row["rule_id"], int(row["signal_week"])) for row in signals}
    findings = {
        "schema_version": "1.0.0", "module_id": "oclc-app3-03", "module_version": "0.1.0",
        "commons_release": "0.68.0", "upstream": handoff,
        "baseline_weeks": [1, 24], "evaluation_weeks": [25, 52],
        "control_charts": {
            "p_chart_center_percent": round(100 * p_center, 6),
            "xmr_center_minutes": round(x_center, 6), "xmr_moving_range_mean": round(mr_bar, 6),
            "xmr_lower_minutes": round(x_lower, 6), "xmr_upper_minutes": round(x_upper, 6),
            "incident_u_center_per_1000": round(1000 * u_center, 6),
            "arrival_run_median": arrivals_center, "signal_records": len(signals),
        },
        "expected_signal_recovery": {
            "xmr_high_point_week_44": ("C02", "R1", 44) in signal_fields,
            "xmr_high_run_by_week_42": ("C02", "R2", 42) in signal_fields,
            "p_chart_high_point_week_44": ("C01", "R1", 44) in signal_fields,
            "p_chart_high_run_by_week_49": ("C01", "R2", 49) in signal_fields,
            "xmr_baseline_high_run_by_week_11": ("C02", "R2", 11) in signal_fields,
            "incident_low_run_by_week_40": ("C03", "R2", 40) in signal_fields,
        },
        "known_truth_review": {
            "KT04_demand_event": "not isolated by the unadjusted arrival run chart; defer seasonal adjustment to Module 04",
            "KT05_first_clinician_delay": "recovered by the evaluation run and stage reconciliation",
            "KT06_access_support_delay": "visible in full-release summaries; target-window language and mobility groups remain below support threshold",
            "KT07_safety_undercapture": "recovered by class-specific truth, trigger, incident, and reviewed-non-event counts",
            "KT08_routine_variation": "signals outside KT05 remain review prompts and are not treated as generated causes",
        },
        "bounded_diagnosis": {
            "status": "supported for the fictional release",
            "scope": "evening shifts in Weeks 35 through 44",
            "stage": "roomed_to_clinician",
            "baseline_median_minutes": stage_lookup[("baseline_evening", "roomed_to_clinician")],
            "target_median_minutes": stage_lookup[("target_evening", "roomed_to_clinician")],
            "recovery_median_minutes": stage_lookup[("recovery_evening", "roomed_to_clinician")],
            "root_cause_status": "not established",
            "staffing_change_status": "not authorized",
        },
        "safety": {
            "known_true_events": class_counts["overall"]["known"],
            "trigger_true_positives": class_counts["overall"]["trigger_tp"],
            "incident_true_positives": class_counts["overall"]["incident_tp"],
            "trigger_false_positives": class_counts["overall"]["trigger_fp"],
            "trigger_sensitivity_percent": round(100 * class_counts["overall"]["trigger_tp"] / class_counts["overall"]["known"], 4),
            "incident_capture_percent": round(100 * class_counts["overall"]["incident_tp"] / class_counts["overall"]["known"], 4),
            "trigger_specificity_percent": round(100 * ((completed_total - class_counts["overall"]["known"]) - class_counts["overall"]["trigger_fp"]) / (completed_total - class_counts["overall"]["known"]), 4),
            "temporal_incident_signal_status": "no exact Poisson limit breach",
        },
        "subgroup": {
            "full_release_supported_groups": sum(row["support_status"] == "supported" and row["window_id"] == "full_release" for row in subgroup_rows),
            "target_window_supported_groups": sum(row["support_status"] == "supported" and row["window_id"] == "target_evening" for row in subgroup_rows),
            "target_window_claim_status": "not supported",
        },
        "progression": "continue with conditions",
        "week3_checkpoint_permission": "permitted for curriculum construction",
        "claim_limit": "synthetic bounded process diagnosis only; no root-cause, staffing, clinical, causal, or implementation authorization",
    }
    (output / "diagnostic-findings.json").write_text(json.dumps(findings, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")

    signal_weeks = {chart_id: {int(row["signal_week"]) for row in signals if row["chart_id"] == chart_id} for chart_id in charts}
    (output / "weekly-left-before-seen-p-chart.svg").write_text(svg_line(
        "Weekly left-before-seen p-chart", "Weekly synthetic left-before-seen percent with variable three-sigma binomial limits based on Weeks 1 through 24. Red squares labelled S mark predeclared signals.", charts["C01"], signal_weeks["C01"], "Percent",
    ), encoding="utf-8", newline="\n")
    (output / "weekly-arrival-to-clinician-xmr.svg").write_text(svg_line(
        "Weekly arrival-to-clinician XmR chart", "Weekly mean of three shift medians with an XmR centerline and limits based on Weeks 1 through 24. Red squares labelled S mark predeclared signals.", charts["C02"], signal_weeks["C02"], "Minutes",
    ), encoding="utf-8", newline="\n")
    (output / "weekly-incident-report-u-chart.svg").write_text(svg_line(
        "Weekly incident-report exact u-chart", "Weekly synthetic incident reports per 1,000 completed encounters with exact Poisson count limits. Red squares labelled S would mark predeclared signals.", charts["C03"], signal_weeks["C03"], "Reports per 1,000",
    ), encoding="utf-8", newline="\n")
    (output / "process-stage-comparison.svg").write_text(svg_stage(stage_rows), encoding="utf-8", newline="\n")

    return findings


def verify_committed(root: Path = ROOT) -> dict[str, object]:
    output = root / "outputs"
    missing = [name for name in OUTPUT_FILES if not (output / name).is_file()]
    if missing:
        raise DiagnosticError(f"Missing committed output: {', '.join(missing)}")
    findings = json.loads((output / "diagnostic-findings.json").read_text(encoding="utf-8"))
    if findings["module_id"] != "oclc-app3-03" or findings["commons_release"] != "0.68.0":
        raise DiagnosticError("Committed diagnostic identity mismatch")
    if findings["bounded_diagnosis"]["target_median_minutes"] != 66.0 or findings["safety"]["known_true_events"] != 894:
        raise DiagnosticError("Committed diagnostic findings mismatch")
    return {"outputs": len(OUTPUT_FILES), "signal_records": findings["control_charts"]["signal_records"], "target_stage_median": 66.0}


def self_check() -> None:
    committed = verify_committed()
    with tempfile.TemporaryDirectory(prefix="app3-module03-diagnostic-") as temp_dir:
        base = Path(temp_dir)
        first = base / "first"
        second = base / "second"
        one = build(ROOT, first)
        two = build(ROOT, second)
        if one != two:
            raise AssertionError("Two independent diagnostic findings differ")
        for name in OUTPUT_FILES:
            if (first / name).read_bytes() != (second / name).read_bytes():
                raise AssertionError(f"Two independent outputs differ: {name}")
            if (first / name).read_bytes() != (ROOT / "outputs" / name).read_bytes():
                raise AssertionError(f"Regenerated output differs from committed output: {name}")
        try:
            build(ROOT, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect a nonempty output target")
    print(f"APP-3 Module 03 diagnostic self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.write:
            output = args.output or (args.root / "outputs")
            print(json.dumps(build(args.root, output), indent=2))
        else:
            print(json.dumps(verify_committed(args.root.resolve()), indent=2))
    except (OSError, ValueError, KeyError, DiagnosticError) as error:
        parser.exit(1, f"Diagnostic build failed: {error}\n")


if __name__ == "__main__":
    main()
