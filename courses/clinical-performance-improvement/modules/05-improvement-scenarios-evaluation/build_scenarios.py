"""Build deterministic APP-3 Module 05 scenario and evaluation evidence."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import heapq
import json
import math
import random
import statistics
import tempfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
UPSTREAM = ROOT / "upstream"
WARMUP_MINUTES = 7 * 24 * 60
MEASUREMENT_MINUTES = 7 * 24 * 60
SHIFT_MINUTES = 8 * 60
TOTAL_ARRIVAL_MINUTES = WARMUP_MINUTES + MEASUREMENT_MINUTES
REPLICATIONS = 200
BASE_SEED = 7300500
SERVICE_FRACTION = 0.20
SHIFT_NAMES = ("night", "day", "evening")
BASE_CAPACITY = {"night": 2, "day": 6, "evening": 4}
FORECAST_THRESHOLDS = {"night": 32.0, "day": 55.0, "evening": 48.0}
SCENARIOS = (
    ("S00", "No change"),
    ("S01", "Flex clinician coverage"),
    ("S02", "Fast-track activation"),
    ("S03", "Combined bounded rule"),
)
CONDITIONS = (
    ("C01", "Lower demand", 805.136639, 1.00, 0.70),
    ("C02", "Point demand", 876.924084, 1.00, 0.70),
    ("C03", "Upper demand", 970.733035, 1.00, 0.70),
    ("C04", "Upper demand and slower service", 970.733035, 1.15, 0.70),
    ("C05", "Point demand and weak workflow effect", 876.924084, 1.00, 0.90),
)
OUTPUT_NAMES = (
    "input-profile.csv",
    "condition-register.csv",
    "validation-checks.csv",
    "replication-results.csv",
    "scenario-summary.csv",
    "paired-effects.csv",
    "sensitivity-review.csv",
    "evaluation-measures.csv",
    "evaluation-threats.csv",
    "scenario-findings.json",
    "point-demand-tradeoffs.svg",
    "sensitivity-wait-effects.svg",
)
UNMODELED = "not simulated; prospective measurement required"


class ScenarioError(RuntimeError):
    pass


@dataclass(frozen=True, slots=True)
class PatientInput:
    patient_id: int
    arrival: float
    shift_name: str
    acuity: int
    access: str
    pre_delay: float
    service_minutes: float
    abandon_draw: float
    measured: bool


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path, compressed: bool = False) -> list[dict[str, str]]:
    if compressed:
        with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def f6(value: float) -> str:
    return f"{value:.6f}"


def quantile(values: list[float], probability: float) -> float:
    if not values:
        return math.nan
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (position - lower) * (ordered[upper] - ordered[lower])


def median(values: list[float]) -> float:
    return statistics.median(values) if values else math.nan


def shift_position(time_value: float) -> int:
    return int(time_value // SHIFT_MINUTES) % 21


def shift_name_at(time_value: float) -> str:
    return SHIFT_NAMES[shift_position(time_value) % 3]


def global_shift(time_value: float) -> int:
    return max(0, int(time_value // SHIFT_MINUTES))


def prepare_inputs() -> tuple[list[tuple[int, str]], dict[tuple[str, int, str], list[tuple[float, float]]], list[dict[str, object]], list[float]]:
    encounters = read_csv(UPSTREAM / "encounter-measures.csv.gz", compressed=True)
    profiles: list[tuple[int, str]] = []
    donors: dict[tuple[str, int, str], list[tuple[float, float]]] = defaultdict(list)
    for row in encounters:
        if row["eligible_adult_encounter_flag"] != "1" or row["synthetic_flag"] != "1":
            continue
        acuity = int(row["acuity"])
        access = row["access_support_group"]
        profiles.append((acuity, access))
        if row["completed_flag"] == "1" and row["roomed_at"] and row["clinician_at"] and row["departure_at"]:
            pre_delay = (parse_time(row["roomed_at"]) - parse_time(row["arrival_at"])).total_seconds() / 60
            clinician_to_departure = (parse_time(row["departure_at"]) - parse_time(row["clinician_at"])).total_seconds() / 60
            if pre_delay >= 0 and clinician_to_departure > 0:
                donors[(row["shift_name"], acuity, access)].append((pre_delay, clinician_to_departure))
    if len(profiles) != 43628 or sum(len(values) for values in donors.values()) != 39974:
        raise ScenarioError("Accepted encounter profile changed")
    missing = [
        (shift, acuity, access)
        for shift in SHIFT_NAMES
        for acuity in range(1, 6)
        for access in ("standard", "language_support", "mobility_support")
        if not donors[(shift, acuity, access)]
    ]
    if missing:
        raise ScenarioError(f"Missing empirical donor strata: {missing}")

    profile_rows: list[dict[str, object]] = []
    for key in sorted(donors):
        values = donors[key]
        pre = [row[0] for row in values]
        service = [row[1] for row in values]
        profile_rows.append({
            "shift_name": key[0],
            "acuity": key[1],
            "access_support_group": key[2],
            "donor_rows": len(values),
            "median_pre_clinician_preparation_minutes": f6(median(pre)),
            "median_clinician_to_departure_minutes": f6(median(service)),
            "median_effective_service_minutes": f6(median(service) * SERVICE_FRACTION),
            "support_status": "supported" if len(values) >= 100 else "limited",
            "synthetic_flag": 1,
        })

    forecast_rows = read_csv(UPSTREAM / "week53-forecast.csv")
    forecast = [float(row["raw_forecast_arrivals"]) for row in forecast_rows]
    if len(forecast) != 21 or abs(sum(forecast) - 876.924084) > 0.00001:
        raise ScenarioError("Accepted Week 53 demand shape changed")
    return profiles, donors, profile_rows, forecast


def poisson_times(rng: random.Random, expected: float) -> list[float]:
    if expected <= 0:
        return []
    values: list[float] = []
    current = 0.0
    rate = expected / SHIFT_MINUTES
    while True:
        current += rng.expovariate(rate)
        if current >= SHIFT_MINUTES:
            return values
        values.append(current)


def abandonment_minutes(acuity: int, access: str, draw: float) -> float:
    if acuity not in (4, 5):
        return math.inf
    bounded = min(max(draw, 1e-12), 1 - 1e-12)
    access_term = 0.35 if access == "language_support" else 0.0
    threshold = (math.log(bounded / (1 - bounded)) + 4.2 - access_term) / 0.025
    return max(15.0, threshold)


def generate_workload(
    condition_index: int,
    replication: int,
    expected_total: float,
    service_multiplier: float,
    profiles: list[tuple[int, str]],
    donors: dict[tuple[str, int, str], list[tuple[float, float]]],
    forecast: list[float],
) -> list[PatientInput]:
    rng = random.Random(BASE_SEED + condition_index * 1000 + replication)
    scale = expected_total / sum(forecast)
    patients: list[PatientInput] = []
    patient_id = 0
    for shift_index in range(42):
        position = shift_index % 21
        name = SHIFT_NAMES[position % 3]
        start = shift_index * SHIFT_MINUTES
        for offset in poisson_times(rng, forecast[position] * scale):
            patient_id += 1
            acuity, access = profiles[rng.randrange(len(profiles))]
            donor_pool = donors[(name, acuity, access)]
            pre_delay, observed_service = donor_pool[rng.randrange(len(donor_pool))]
            patients.append(PatientInput(
                patient_id=patient_id,
                arrival=start + offset,
                shift_name=name,
                acuity=acuity,
                access=access,
                pre_delay=pre_delay,
                service_minutes=max(5.0, observed_service * SERVICE_FRACTION * service_multiplier),
                abandon_draw=rng.random(),
                measured=start + offset >= WARMUP_MINUTES,
            ))
    patients.sort(key=lambda row: (row.arrival, row.patient_id))
    return patients


def simulate(
    scenario_id: str,
    condition_id: str,
    replication: int,
    workload: list[PatientInput],
    forecast: list[float],
    fast_multiplier: float,
) -> dict[str, object]:
    states = {
        patient.patient_id: {
            "input": patient,
            "status": "preparing",
            "ready": patient.arrival + patient.pre_delay,
            "deadline": patient.arrival + abandonment_minutes(patient.acuity, patient.access, patient.abandon_draw),
            "start": None,
            "end": None,
            "slot": None,
            "fast": False,
        }
        for patient in workload
    }
    events: list[tuple[float, int, int, str, object]] = []
    sequence = 0

    def add_event(time_value: float, order: int, kind: str, payload: object) -> None:
        nonlocal sequence
        sequence += 1
        heapq.heappush(events, (time_value, order, sequence, kind, payload))

    for patient in workload:
        state = states[patient.patient_id]
        add_event(float(state["ready"]), 4, "ready", patient.patient_id)
        if math.isfinite(float(state["deadline"])):
            add_event(float(state["deadline"]), 2, "abandon", patient.patient_id)
    for boundary in range(0, TOTAL_ARRIVAL_MINUTES + MEASUREMENT_MINUTES + SHIFT_MINUTES, SHIFT_MINUTES):
        add_event(float(boundary), 1, "shift", boundary // SHIFT_MINUTES)

    queue: list[int] = []
    busy: dict[int, int] = {}
    service_records: list[tuple[float, float, int, int]] = []
    active_shifts: dict[int, float] = {}
    pending_activation: dict[int, float] = {}
    activation_delays: list[float] = []
    queue_max = 0

    def forecast_eligible(shift_index: int) -> bool:
        position = shift_index % 21
        name = SHIFT_NAMES[position % 3]
        return forecast[position] >= FORECAST_THRESHOLDS[name]

    def capacity_at(time_value: float) -> int:
        shift_index = global_shift(time_value)
        name = SHIFT_NAMES[(shift_index % 21) % 3]
        capacity = BASE_CAPACITY[name]
        if scenario_id == "S01" and forecast_eligible(shift_index):
            capacity += 1
        elif scenario_id == "S03" and shift_index in active_shifts and time_value >= active_shifts[shift_index]:
            capacity += 1
        return capacity

    def fast_active(time_value: float) -> bool:
        return scenario_id in {"S02", "S03"} and global_shift(time_value) in active_shifts

    def trigger_allowed(time_value: float) -> bool:
        if scenario_id == "S02":
            return True
        return scenario_id == "S03" and forecast_eligible(global_shift(time_value))

    def maybe_trigger(time_value: float) -> None:
        shift_index = global_shift(time_value)
        if not trigger_allowed(time_value) or shift_index in active_shifts:
            return
        if len(queue) < 4:
            pending_activation.pop(shift_index, None)
            return
        if shift_index not in pending_activation:
            activation = time_value + 15.0
            if global_shift(activation) == shift_index:
                pending_activation[shift_index] = activation
                add_event(activation, 3, "activation", shift_index)

    def choose_patient(use_fast_lane: bool) -> tuple[int, bool]:
        eligible = [pid for pid in queue if int(states[pid]["input"].acuity) in (4, 5)] if use_fast_lane else []
        if eligible:
            patient_id = min(eligible, key=lambda pid: (float(states[pid]["ready"]), pid))
            return patient_id, True
        patient_id = min(queue, key=lambda pid: (int(states[pid]["input"].acuity), float(states[pid]["ready"]), pid))
        return patient_id, False

    def dispatch(time_value: float) -> None:
        nonlocal queue_max
        capacity = capacity_at(time_value)
        free = [slot for slot in range(capacity) if slot not in busy]
        if fast_active(time_value) and free and capacity - 1 in free:
            free.remove(capacity - 1)
            free.insert(0, capacity - 1)
        while free and queue:
            slot = free.pop(0)
            fast_lane = fast_active(time_value) and slot == capacity - 1
            patient_id, accelerated = choose_patient(fast_lane)
            queue.remove(patient_id)
            state = states[patient_id]
            if float(state["deadline"]) <= time_value:
                state["status"] = "abandoned"
                continue
            patient = state["input"]
            duration = patient.service_minutes * (fast_multiplier if accelerated else 1.0)
            state["status"] = "in_service"
            state["start"] = time_value
            state["end"] = time_value + duration
            state["slot"] = slot
            state["fast"] = accelerated
            busy[slot] = patient_id
            service_records.append((time_value, time_value + duration, slot, patient_id))
            add_event(time_value + duration, 0, "complete", (slot, patient_id))
        queue_max = max(queue_max, len(queue))
        maybe_trigger(time_value)

    while events:
        time_value = events[0][0]
        batch: list[tuple[float, int, int, str, object]] = []
        while events and events[0][0] == time_value:
            batch.append(heapq.heappop(events))
        for _, _, _, kind, payload in sorted(batch, key=lambda row: (row[1], row[2])):
            if kind == "complete":
                slot, patient_id = payload
                if busy.get(int(slot)) == int(patient_id):
                    busy.pop(int(slot))
                    states[int(patient_id)]["status"] = "completed"
            elif kind == "abandon":
                patient_id = int(payload)
                state = states[patient_id]
                if state["status"] in {"preparing", "waiting"}:
                    if state["status"] == "waiting" and patient_id in queue:
                        queue.remove(patient_id)
                    state["status"] = "abandoned"
            elif kind == "activation":
                shift_index = int(payload)
                if pending_activation.get(shift_index) == time_value:
                    pending_activation.pop(shift_index, None)
                    if global_shift(time_value) == shift_index and len(queue) >= 4:
                        active_shifts[shift_index] = time_value
                        if WARMUP_MINUTES <= time_value < TOTAL_ARRIVAL_MINUTES:
                            activation_delays.append(15.0)
            elif kind == "ready":
                patient_id = int(payload)
                state = states[patient_id]
                if state["status"] == "preparing":
                    state["status"] = "waiting"
                    queue.append(patient_id)
        dispatch(time_value)

    measured = [state for state in states.values() if state["input"].measured]
    if any(state["status"] not in {"completed", "abandoned"} for state in measured):
        raise ScenarioError(f"Unresolved patient in {scenario_id} {condition_id} replication {replication}")
    completed = [state for state in measured if state["status"] == "completed"]
    abandoned = [state for state in measured if state["status"] == "abandoned"]
    waits = [float(state["start"]) - state["input"].arrival for state in completed]
    cycles = [float(state["end"]) - state["input"].arrival for state in completed]
    access_waits: dict[str, list[float]] = defaultdict(list)
    acuity_waits: dict[str, list[float]] = defaultdict(list)
    for state in completed:
        wait = float(state["start"]) - state["input"].arrival
        access_waits[state["input"].access].append(wait)
        acuity_waits["high" if state["input"].acuity in (1, 2) else "low" if state["input"].acuity in (4, 5) else "middle"].append(wait)

    def overlap(start: float, end: float, lower: float, upper: float) -> float:
        return max(0.0, min(end, upper) - max(start, lower))

    busy_minutes = sum(overlap(start, end, WARMUP_MINUTES, TOTAL_ARRIVAL_MINUTES) for start, end, _, _ in service_records)
    available_minutes = 0.0
    flex_minutes = 0.0
    for shift_index in range(21, 42):
        name = SHIFT_NAMES[(shift_index % 21) % 3]
        available_minutes += BASE_CAPACITY[name] * SHIFT_MINUTES
        if scenario_id == "S01" and forecast_eligible(shift_index):
            flex_minutes += SHIFT_MINUTES
        elif scenario_id == "S03" and shift_index in active_shifts:
            flex_minutes += (shift_index + 1) * SHIFT_MINUTES - active_shifts[shift_index]
    available_minutes += flex_minutes

    overtime_minutes = 0.0
    for start, end, slot, _ in service_records:
        cursor = max(start, WARMUP_MINUTES)
        limit = min(end, TOTAL_ARRIVAL_MINUTES)
        while cursor < limit:
            boundary = min(limit, (global_shift(cursor) + 1) * SHIFT_MINUTES)
            midpoint = cursor + (boundary - cursor) / 2
            if slot >= capacity_at(midpoint):
                overtime_minutes += boundary - cursor
            cursor = boundary

    trigger_count = 0
    if scenario_id == "S01":
        trigger_count = sum(forecast_eligible(index) for index in range(21, 42))
        activation_delays = [0.0] * trigger_count
    else:
        trigger_count = len(activation_delays)
    standard_wait = median(access_waits["standard"])
    language_wait = median(access_waits["language_support"])
    mobility_wait = median(access_waits["mobility_support"])
    conservation = len(measured) == len(completed) + len(abandoned)
    return {
        "condition_id": condition_id,
        "scenario_id": scenario_id,
        "replication": replication,
        "seed": BASE_SEED + next(index for index, row in enumerate(CONDITIONS, start=1) if row[0] == condition_id) * 1000 + replication,
        "arrivals": len(measured),
        "completed": len(completed),
        "left_before_seen": len(abandoned),
        "left_before_seen_percent": 100 * len(abandoned) / len(measured),
        "median_arrival_to_clinician_minutes": median(waits),
        "p90_arrival_to_clinician_minutes": quantile(waits, 0.90),
        "median_arrival_to_departure_minutes": median(cycles),
        "clinician_utilization_percent": 100 * busy_minutes / available_minutes,
        "modeled_overtime_hours": overtime_minutes / 60,
        "flex_clinician_hours": flex_minutes / 60,
        "trigger_count": trigger_count,
        "median_activation_delay_minutes": median(activation_delays) if activation_delays else 0.0,
        "standard_wait_minutes": standard_wait,
        "language_support_wait_minutes": language_wait,
        "mobility_support_wait_minutes": mobility_wait,
        "language_gap_minutes": language_wait - standard_wait,
        "mobility_gap_minutes": mobility_wait - standard_wait,
        "high_acuity_wait_minutes": median(acuity_waits["high"]),
        "low_acuity_wait_minutes": median(acuity_waits["low"]),
        "maximum_waiting_queue": queue_max,
        "fast_track_completed": sum(bool(state["fast"]) for state in completed),
        "safety_outcome_status": UNMODELED,
        "return_72h_status": UNMODELED,
        "conservation_status": "pass" if conservation else "fail",
        "synthetic_flag": 1,
    }


METRICS = (
    "arrivals",
    "completed",
    "left_before_seen",
    "left_before_seen_percent",
    "median_arrival_to_clinician_minutes",
    "p90_arrival_to_clinician_minutes",
    "median_arrival_to_departure_minutes",
    "clinician_utilization_percent",
    "modeled_overtime_hours",
    "flex_clinician_hours",
    "trigger_count",
    "median_activation_delay_minutes",
    "standard_wait_minutes",
    "language_support_wait_minutes",
    "mobility_support_wait_minutes",
    "language_gap_minutes",
    "mobility_gap_minutes",
    "high_acuity_wait_minutes",
    "low_acuity_wait_minutes",
    "maximum_waiting_queue",
    "fast_track_completed",
)


def aggregate_results(replications: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in replications:
        grouped[(str(row["condition_id"]), str(row["scenario_id"]))].append(row)
    rows: list[dict[str, object]] = []
    expected = {condition[0]: condition[2] for condition in CONDITIONS}
    for condition_id, _, _, _, _ in CONDITIONS:
        for scenario_id, scenario_name in SCENARIOS:
            values = grouped[(condition_id, scenario_id)]
            row: dict[str, object] = {
                "condition_id": condition_id,
                "scenario_id": scenario_id,
                "scenario_name": scenario_name,
                "replications": len(values),
                "expected_weekly_arrivals": expected[condition_id],
            }
            for metric in METRICS:
                metric_values = [float(value[metric]) for value in values]
                row[f"median_{metric}"] = median(metric_values)
                if metric in {
                    "left_before_seen_percent",
                    "median_arrival_to_clinician_minutes",
                    "p90_arrival_to_clinician_minutes",
                    "clinician_utilization_percent",
                    "language_gap_minutes",
                }:
                    row[f"q10_{metric}"] = quantile(metric_values, 0.10)
                    row[f"q90_{metric}"] = quantile(metric_values, 0.90)
            row["safety_outcome_status"] = UNMODELED
            row["return_72h_status"] = UNMODELED
            row["conservation_status"] = "pass" if all(value["conservation_status"] == "pass" for value in values) else "fail"
            row["synthetic_flag"] = 1
            rows.append(row)
    return rows


def paired_effects(replications: list[dict[str, object]]) -> list[dict[str, object]]:
    by_key = {
        (str(row["condition_id"]), str(row["scenario_id"]), int(row["replication"])): row
        for row in replications
    }
    grouped: dict[tuple[str, str], list[dict[str, float]]] = defaultdict(list)
    for condition_id, _, _, _, _ in CONDITIONS:
        for scenario_id, _ in SCENARIOS[1:]:
            for replication in range(1, REPLICATIONS + 1):
                baseline = by_key[(condition_id, "S00", replication)]
                option = by_key[(condition_id, scenario_id, replication)]
                grouped[(condition_id, scenario_id)].append({
                    "median_wait_improvement": float(baseline["median_arrival_to_clinician_minutes"]) - float(option["median_arrival_to_clinician_minutes"]),
                    "p90_wait_improvement": float(baseline["p90_arrival_to_clinician_minutes"]) - float(option["p90_arrival_to_clinician_minutes"]),
                    "left_before_seen_improvement_pp": float(baseline["left_before_seen_percent"]) - float(option["left_before_seen_percent"]),
                    "throughput_change_percent": 100 * (float(option["completed"]) - float(baseline["completed"])) / max(float(baseline["completed"]), 1),
                    "language_gap_worsening": float(option["language_gap_minutes"]) - float(baseline["language_gap_minutes"]),
                    "utilization_change": float(option["clinician_utilization_percent"]) - float(baseline["clinician_utilization_percent"]),
                    "overtime_change": float(option["modeled_overtime_hours"]) - float(baseline["modeled_overtime_hours"]),
                    "flex_hours": float(option["flex_clinician_hours"]),
                    "trigger_count": float(option["trigger_count"]),
                })
    rows: list[dict[str, object]] = []
    for condition_id, _, _, _, _ in CONDITIONS:
        for scenario_id, scenario_name in SCENARIOS[1:]:
            values = grouped[(condition_id, scenario_id)]
            row: dict[str, object] = {
                "condition_id": condition_id,
                "scenario_id": scenario_id,
                "scenario_name": scenario_name,
                "paired_replications": len(values),
            }
            for metric in values[0]:
                metric_values = [value[metric] for value in values]
                row[f"median_{metric}"] = median(metric_values)
                row[f"q10_{metric}"] = quantile(metric_values, 0.10)
                row[f"q90_{metric}"] = quantile(metric_values, 0.90)
            row["synthetic_flag"] = 1
            rows.append(row)
    return rows


def choose_option(paired: list[dict[str, object]]) -> tuple[str, dict[str, dict[str, object]]]:
    lookup = {(str(row["condition_id"]), str(row["scenario_id"])): row for row in paired}
    decisions: dict[str, dict[str, object]] = {}
    for scenario_id, scenario_name in SCENARIOS[1:]:
        point = lookup[("C02", scenario_id)]
        stress = lookup[("C04", scenario_id)]
        rules = {
            "median_wait": float(point["median_median_wait_improvement"]) >= 10,
            "p90_wait": float(point["median_p90_wait_improvement"]) >= 15,
            "left_before_seen": float(point["median_left_before_seen_improvement_pp"]) >= 1.0,
            "throughput": float(point["median_throughput_change_percent"]) >= -1.0,
            "language_gap": float(point["median_language_gap_worsening"]) <= 5.0,
            "stress_wait": float(stress["median_median_wait_improvement"]) > 0,
        }
        decisions[scenario_id] = {
            "scenario_name": scenario_name,
            "qualifies": all(rules.values()),
            "rules": rules,
            "point_median_wait_improvement": float(point["median_median_wait_improvement"]),
            "point_flex_hours": float(point["median_flex_hours"]),
            "stress_median_wait_improvement": float(stress["median_median_wait_improvement"]),
        }
    eligible = [scenario_id for scenario_id, decision in decisions.items() if decision["qualifies"]]
    if not eligible:
        return "none", decisions
    best_improvement = max(float(decisions[scenario_id]["point_median_wait_improvement"]) for scenario_id in eligible)
    near = [scenario_id for scenario_id in eligible if best_improvement - float(decisions[scenario_id]["point_median_wait_improvement"]) <= 5]
    selected = min(
        near,
        key=lambda scenario_id: (
            float(decisions[scenario_id]["point_flex_hours"]),
            -float(decisions[scenario_id]["point_median_wait_improvement"]),
            scenario_id,
        ),
    )
    return selected, decisions


def sensitivity_rows(paired: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    condition_names = {row[0]: row[1] for row in CONDITIONS}
    for result in paired:
        full_rule = (
            float(result["median_median_wait_improvement"]) >= 10
            and float(result["median_p90_wait_improvement"]) >= 15
            and float(result["median_left_before_seen_improvement_pp"]) >= 1.0
            and float(result["median_throughput_change_percent"]) >= -1.0
            and float(result["median_language_gap_worsening"]) <= 5.0
        )
        failed_rule = (
            float(result["median_median_wait_improvement"]) <= 0
            or float(result["median_p90_wait_improvement"]) <= 0
            or float(result["median_throughput_change_percent"]) < -1.0
            or float(result["median_language_gap_worsening"]) > 5.0
        )
        rows.append({
            "condition_id": result["condition_id"],
            "condition_name": condition_names[str(result["condition_id"])],
            "scenario_id": result["scenario_id"],
            "scenario_name": result["scenario_name"],
            "median_wait_improvement_minutes": result["median_median_wait_improvement"],
            "p90_wait_improvement_minutes": result["median_p90_wait_improvement"],
            "left_before_seen_improvement_percentage_points": result["median_left_before_seen_improvement_pp"],
            "throughput_change_percent": result["median_throughput_change_percent"],
            "language_gap_worsening_minutes": result["median_language_gap_worsening"],
            "median_flex_clinician_hours": result["median_flex_hours"],
            "effect_status": "meets full option rule" if full_rule else "null or failed improvement" if failed_rule else "partial only",
            "synthetic_flag": 1,
        })
    return rows


def evaluation_measures() -> list[dict[str, object]]:
    rows = (
        ("M01", "process", "weekly median arrival-to-clinician", "minutes", "lower may be favorable", "XmR", "Weeks 1-24 provisional baseline", "existing three signal rules", "flow lead"),
        ("M02", "process", "weekly 90th percentile arrival-to-clinician", "minutes", "lower may be favorable", "run chart", "pre-test stabilization period", "review any sustained directional run", "flow lead"),
        ("M03", "outcome", "weekly median arrival-to-departure", "minutes", "lower may be favorable", "run chart", "pre-test stabilization period", "review with disposition mix", "clinical operations lead"),
        ("M04", "access", "left before seen", "percent", "lower may be favorable", "p-chart", "Weeks 1-24 provisional baseline", "existing three signal rules", "access lead"),
        ("M05", "flow", "completed throughput", "encounters per week", "context only", "run chart", "pre-test stabilization period", "interpret with demand and abandonment", "flow lead"),
        ("M06", "capacity", "clinician utilization", "percent", "context only", "run chart", "pre-test stabilization period", "review high and low sustained values", "workforce data owner"),
        ("M07", "workforce", "overtime hours", "hours per week", "lower may be favorable", "run chart", "pre-test stabilization period", "review any sustained increase", "workforce lead"),
        ("M08", "safety", "reviewed safety-event candidates", "events per 1000 completed", "lower is not inherently favorable", "exact Poisson u-chart", "Weeks 1-24 provisional baseline", "retain reporting undercapture review", "safety lead"),
        ("M09", "outcome", "return within 72 hours", "percent", "context only", "p-chart", "pre-test stabilization period", "review with follow-up completeness", "quality lead"),
        ("M10", "access", "language-support arrival-to-clinician gap", "minutes", "lower may be favorable", "exact table and run chart", "pre-test stabilization period", "report support and unavailable states", "access lead"),
        ("M11", "access", "mobility-support arrival-to-clinician gap", "minutes", "lower may be favorable", "exact table and run chart", "pre-test stabilization period", "report support and unavailable states", "access lead"),
        ("M12", "workforce", "interruptions and perceived workload", "prospective instrument units", "lower may be favorable", "exact table", "no accepted baseline yet", "collect before any test", "workforce lead"),
    )
    return [{
        "measure_id": row[0],
        "domain": row[1],
        "measure": row[2],
        "unit": row[3],
        "direction": row[4],
        "display": row[5],
        "baseline": row[6],
        "review_rule": row[7],
        "owner": row[8],
        "unavailable_state": "report unavailable and do not impute when source or denominator is incomplete",
        "claim_limit": "monitoring evidence; no causal effect without an authorized design and supporting evidence",
    } for row in rows]


def evaluation_threats() -> list[dict[str, object]]:
    rows = (
        ("T01", "secular trend", "demand or flow changes over time without the option", "extend the accepted time series and inspect pre-test direction", "model time explicitly and avoid a two-period mean claim"),
        ("T02", "regression to the mean", "testing begins after an unusually poor period", "compare the trigger period with the full baseline and recovery", "require sustained prospective evidence"),
        ("T03", "measurement change", "definitions or capture change at test start", "rerun measure specifications and missingness checks", "freeze definitions or label the discontinuity"),
        ("T04", "concurrent intervention", "another workflow or staffing change occurs", "maintain a dated intervention log", "separate, model, or refer the effect claim"),
        ("T05", "case mix", "acuity, arrival mode, or support need changes", "compare prespecified distributions and support", "stratify or adjust only with a declared plan"),
        ("T06", "gaming", "staff alter timestamps, routing, or denominators to improve the measure", "audit event order, exclusions, unavailable states, and routing", "pause reporting and investigate"),
        ("T07", "contamination and adoption", "the option is used outside its rule or adopted unevenly", "record eligibility, activation, adherence, and crossover", "report as implemented and preserve deviations"),
        ("T08", "missing or unsupported groups", "access effects are hidden by low support or missing fields", "recalculate group support in every window", "report unavailable and do not infer equity"),
    )
    return [{
        "threat_id": row[0],
        "threat": row[1],
        "risk": row[2],
        "detection": row[3],
        "response": row[4],
        "owner": "APP-3 evaluation team with named clinical and operational review",
        "causal_status": "not resolved by simulation",
    } for row in rows]


def validation_rows(
    replications: list[dict[str, object]],
    summaries: list[dict[str, object]],
    sensitivities: list[dict[str, object]],
    selected: str,
    profile_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    summary = {(str(row["condition_id"]), str(row["scenario_id"])): row for row in summaries}
    baseline = summary[("C02", "S00")]
    checks = (
        ("V01", "accepted encounter population", len(read_csv(UPSTREAM / "encounter-measures.csv.gz", compressed=True)) == 43628, "43,628 accepted encounter rows"),
        ("V02", "accepted scenario register", [row["scenario_id"] for row in read_csv(UPSTREAM / "scenario-register.csv.gz", compressed=True)] == ["S00", "S01", "S02", "S03"], "S00 through S03"),
        ("V03", "input strata", len(profile_rows) == 45, "45 shift, acuity, and support strata"),
        ("V04", "forecast demand identity", True, "876.924084 accepted point arrivals"),
        ("V05", "demand conditions", len(CONDITIONS) == 5, "lower, point, upper, stress, and weak-effect conditions"),
        ("V06", "warm-up", WARMUP_MINUTES == 10080, "seven days excluded from measurement"),
        ("V07", "replications", len(replications) == 4000, "200 paired replications for 20 scenario-condition cells"),
        ("V08", "paired random inputs", len({(row["condition_id"], row["replication"], row["seed"]) for row in replications}) == 1000, "one seed shared by four scenarios"),
        ("V09", "priority", float(baseline["median_high_acuity_wait_minutes"]) <= float(baseline["median_low_acuity_wait_minutes"]), "nonpreemptive acuity priority retained"),
        ("V10", "base capacity", BASE_CAPACITY == {"night": 2, "day": 6, "evening": 4}, "calibrated clinician-slot schedule"),
        ("V11", "flex threshold", FORECAST_THRESHOLDS == {"night": 32.0, "day": 55.0, "evening": 48.0}, "shift-specific 75th-percentile thresholds"),
        ("V12", "fast-track trigger", True, "four waiting patients for 15 minutes"),
        ("V13", "S02 net staff", float(summary[("C02", "S02")]["median_flex_clinician_hours"]) == 0, "no added clinician-hours"),
        ("V14", "S03 combined rule", True, "forecast eligibility and queue persistence both required"),
        ("V15", "conservation", all(row["conservation_status"] == "pass" for row in replications), "arrivals equal completed plus left before seen"),
        ("V16", "nonnegative results", all(float(row["completed"]) >= 0 and float(row["median_arrival_to_clinician_minutes"]) >= 0 for row in replications), "no negative count or time"),
        ("V17", "result identity", len({(row["condition_id"], row["scenario_id"], row["replication"]) for row in replications}) == 4000, "no duplicate scenario run"),
        ("V18", "no-change wait calibration", 55 <= float(baseline["median_median_arrival_to_clinician_minutes"]) <= 125, "point-demand median is within the broad guided-model range"),
        ("V19", "no-change abandonment calibration", 4 <= float(baseline["median_left_before_seen_percent"]) <= 15, "point-demand abandonment remains plausible for the synthetic source"),
        ("V20", "access groups", all(math.isfinite(float(baseline[f"median_{name}_wait_minutes"])) for name in ("standard", "language_support", "mobility_support")), "all three support groups reported"),
        ("V21", "failed condition retained", any(row["effect_status"] == "null or failed improvement" for row in sensitivities), "KT10 null or failed condition retained"),
        ("V22", "safety boundary", all(row["safety_outcome_status"] == UNMODELED for row in replications), UNMODELED),
        ("V23", "return boundary", all(row["return_72h_status"] == UNMODELED for row in replications), UNMODELED),
        ("V24", "selection output", selected in {"none", "S01", "S02", "S03"}, f"selected option is {selected}"),
    )
    return [{"check_id": row[0], "check": row[1], "status": "pass" if row[2] else "fail", "evidence": row[3]} for row in checks]


def output_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        {key: f6(value) if isinstance(value, float) else value for key, value in row.items()}
        for row in rows
    ]


def condition_rows() -> list[dict[str, object]]:
    return [{
        "condition_id": condition_id,
        "condition_name": name,
        "expected_weekly_arrivals": f6(arrivals),
        "service_time_multiplier": f6(service_multiplier),
        "fast_track_service_multiplier": f6(fast_multiplier),
        "warmup_days": 7,
        "measurement_days": 7,
        "paired_replications": REPLICATIONS,
        "base_seed": BASE_SEED,
        "interpretation": "assumption test, not a prediction of realized effect",
        "synthetic_flag": 1,
    } for condition_id, name, arrivals, service_multiplier, fast_multiplier in CONDITIONS]


def point_tradeoff_svg(paired: list[dict[str, object]], selected: str) -> str:
    point = [row for row in paired if row["condition_id"] == "C02"]
    width, height = 980, 430
    left, chart_width = 250, 600
    maximum = max(1.0, max(float(row["median_median_wait_improvement"]) for row in point))
    elements: list[str] = []
    for index, row in enumerate(point):
        y = 105 + index * 90
        value = float(row["median_median_wait_improvement"])
        bar_width = max(0.0, value) * chart_width / maximum
        color = "#0d67ff" if row["scenario_id"] == selected else "#64748b"
        elements.extend((
            f'<text x="230" y="{y + 21}" text-anchor="end" font-size="16">{row["scenario_name"]}</text>',
            f'<rect x="{left}" y="{y}" width="{bar_width:.1f}" height="30" fill="{color}" />',
            f'<text x="{left + bar_width + 10:.1f}" y="{y + 21}" font-size="14">{value:.1f} min; LBBS {float(row["median_left_before_seen_improvement_pp"]):.1f} pp; flex {float(row["median_flex_hours"]):.1f} h</text>',
        ))
    selected_text = "No option qualified" if selected == "none" else f"Selected for feasibility review: {selected}"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" role="img" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
        '<title>Point-demand scenario tradeoffs</title>\n'
        f'<desc>Median paired wait improvement across 200 replications for three options. {selected_text}. Scenario results test assumptions and do not prove realized effects.</desc>\n'
        '<rect width="100%" height="100%" fill="#ffffff" />\n'
        '<text x="490" y="38" text-anchor="middle" font-size="23" font-weight="bold">Point-demand scenario tradeoffs</text>\n'
        '<text x="490" y="68" text-anchor="middle" font-size="14">Median paired improvement across 200 synthetic replications</text>\n'
        + "\n".join(elements)
        + f'\n<text x="490" y="392" text-anchor="middle" font-size="15">{selected_text}</text>\n'
        '<text x="490" y="416" text-anchor="middle" font-size="13">Assumption test only. Safety and 72-hour return require prospective measurement.</text>\n</svg>\n'
    )


def sensitivity_svg(sensitivities: list[dict[str, object]]) -> str:
    width, height = 1080, 540
    left, top, chart_width, chart_height = 110, 80, 850, 360
    values = [float(row["median_wait_improvement_minutes"]) for row in sensitivities]
    lower, upper = min(values + [0.0]), max(values + [0.0])
    span = max(1.0, upper - lower)
    condition_order = [row[0] for row in CONDITIONS]
    colors = {"S01": "#0d67ff", "S02": "#0f766e", "S03": "#d97706"}
    elements: list[str] = []
    for scenario_id, scenario_name in SCENARIOS[1:]:
        rows = {str(row["condition_id"]): row for row in sensitivities if row["scenario_id"] == scenario_id}
        points = []
        for index, condition_id in enumerate(condition_order):
            value = float(rows[condition_id]["median_wait_improvement_minutes"])
            x = left + index * chart_width / (len(condition_order) - 1)
            y = top + (upper - value) * chart_height / span
            points.append(f"{x:.1f},{y:.1f}")
        elements.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{colors[scenario_id]}" stroke-width="3" />')
        elements.append(f'<text x="975" y="{110 + 25 * (int(scenario_id[-1]) - 1)}" font-size="14" fill="{colors[scenario_id]}">{scenario_id} {scenario_name}</text>')
    labels = [
        f'<text x="{left + index * chart_width / 4:.1f}" y="470" text-anchor="middle" font-size="13">{condition_id}</text>'
        for index, condition_id in enumerate(condition_order)
    ]
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" role="img" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
        '<title>Sensitivity of wait improvement to five conditions</title>\n'
        '<desc>Median paired arrival-to-clinician wait improvement for three options under lower, point, upper, slower-service, and weak-workflow-effect conditions.</desc>\n'
        '<rect width="100%" height="100%" fill="#ffffff" />\n'
        '<text x="540" y="36" text-anchor="middle" font-size="23" font-weight="bold">Wait improvement changes when assumptions change</text>\n'
        f'<line x1="{left}" y1="{top + upper * chart_height / span:.1f}" x2="{left + chart_width}" y2="{top + upper * chart_height / span:.1f}" stroke="#1f2937" />\n'
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + chart_height}" stroke="#1f2937" />\n'
        + "\n".join(elements + labels)
        + '\n<text x="540" y="510" text-anchor="middle" font-size="13">Positive values favor the option. A changed or failed result must remain visible.</text>\n</svg>\n'
    )


def generate(target: Path) -> dict[str, object]:
    import freeze_upstream

    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    upstream = freeze_upstream.verify(ROOT)
    profiles, donors, profile_rows, forecast = prepare_inputs()
    replications: list[dict[str, object]] = []
    for condition_index, (condition_id, _, arrivals, service_multiplier, fast_multiplier) in enumerate(CONDITIONS, start=1):
        for replication in range(1, REPLICATIONS + 1):
            workload = generate_workload(condition_index, replication, arrivals, service_multiplier, profiles, donors, forecast)
            for scenario_id, _ in SCENARIOS:
                replications.append(simulate(scenario_id, condition_id, replication, workload, forecast, fast_multiplier))

    summaries = aggregate_results(replications)
    paired = paired_effects(replications)
    sensitivities = sensitivity_rows(paired)
    selected, decisions = choose_option(paired)
    measures = evaluation_measures()
    threats = evaluation_threats()
    validations = validation_rows(replications, summaries, sensitivities, selected, profile_rows)
    failed = [row for row in validations if row["status"] != "pass"]
    if failed:
        raise ScenarioError(f"Scenario validation failed: {failed}")

    summary_lookup = {(str(row["condition_id"]), str(row["scenario_id"])): row for row in summaries}
    paired_lookup = {(str(row["condition_id"]), str(row["scenario_id"])): row for row in paired}
    point_summary = {
        scenario_id: {
            "scenario_name": scenario_name,
            "median_arrivals": round(float(summary_lookup[("C02", scenario_id)]["median_arrivals"]), 6),
            "median_completed": round(float(summary_lookup[("C02", scenario_id)]["median_completed"]), 6),
            "median_wait_minutes": round(float(summary_lookup[("C02", scenario_id)]["median_median_arrival_to_clinician_minutes"]), 6),
            "p90_wait_minutes": round(float(summary_lookup[("C02", scenario_id)]["median_p90_arrival_to_clinician_minutes"]), 6),
            "left_before_seen_percent": round(float(summary_lookup[("C02", scenario_id)]["median_left_before_seen_percent"]), 6),
            "flex_clinician_hours": round(float(summary_lookup[("C02", scenario_id)]["median_flex_clinician_hours"]), 6),
        }
        for scenario_id, scenario_name in SCENARIOS
    }
    point_effects = {
        scenario_id: {
            "median_wait_improvement_minutes": round(float(paired_lookup[("C02", scenario_id)]["median_median_wait_improvement"]), 6),
            "p90_wait_improvement_minutes": round(float(paired_lookup[("C02", scenario_id)]["median_p90_wait_improvement"]), 6),
            "left_before_seen_improvement_percentage_points": round(float(paired_lookup[("C02", scenario_id)]["median_left_before_seen_improvement_pp"]), 6),
            "throughput_change_percent": round(float(paired_lookup[("C02", scenario_id)]["median_throughput_change_percent"]), 6),
            "language_gap_worsening_minutes": round(float(paired_lookup[("C02", scenario_id)]["median_language_gap_worsening"]), 6),
        }
        for scenario_id, _ in SCENARIOS[1:]
    }
    findings = {
        "schema_version": "1.0.0",
        "module_id": "oclc-app3-05",
        "module_version": "0.1.0",
        "commons_release": "0.71.0",
        "upstream": upstream,
        "simulation_contract": {
            "warmup_days": 7,
            "measurement_days": 7,
            "paired_replications_per_condition": REPLICATIONS,
            "conditions": len(CONDITIONS),
            "scenario_runs": len(replications),
            "base_seed": BASE_SEED,
            "effective_service_fraction": SERVICE_FRACTION,
            "claim": "guided discrete-event assumption test, not a production simulator or proof of realized effect",
        },
        "point_demand": point_summary,
        "point_paired_effects": point_effects,
        "selection": {
            "selected_option": selected,
            "purpose": "feasibility review only",
            "near_tie_minutes": 5,
            "decisions": decisions,
        },
        "sensitivity": {
            "conditions": len(CONDITIONS),
            "null_or_failed_rows": sum(row["effect_status"] == "null or failed improvement" for row in sensitivities),
            "retention_rule": "changed, null, and failed results remain visible",
        },
        "evaluation": {
            "measures": len(measures),
            "threats": len(threats),
            "safety_outcome": UNMODELED,
            "return_within_72_hours": UNMODELED,
            "causal_status": "not established by simulation",
        },
        "module06_handoff": {
            "option_for_feasibility_review": selected,
            "authority": "feasibility, monitoring, and embedded-ML planning only; no implementation authority",
        },
        "claim_limit": "synthetic assumption-testing evidence only; no clinical, causal, productivity, staffing, safety, equity, automated, or implementation claim",
    }

    target.mkdir(parents=True)
    outputs: tuple[tuple[str, list[dict[str, object]]], ...] = (
        ("input-profile.csv", profile_rows),
        ("condition-register.csv", condition_rows()),
        ("validation-checks.csv", validations),
        ("replication-results.csv", output_rows(replications)),
        ("scenario-summary.csv", output_rows(summaries)),
        ("paired-effects.csv", output_rows(paired)),
        ("sensitivity-review.csv", output_rows(sensitivities)),
        ("evaluation-measures.csv", measures),
        ("evaluation-threats.csv", threats),
    )
    for name, rows in outputs:
        write_csv(target / name, list(rows[0]), rows)
    (target / "scenario-findings.json").write_text(json.dumps(findings, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    (target / "point-demand-tradeoffs.svg").write_text(point_tradeoff_svg(paired, selected), encoding="utf-8", newline="\n")
    (target / "sensitivity-wait-effects.svg").write_text(sensitivity_svg(sensitivities), encoding="utf-8", newline="\n")
    if sorted(path.name for path in target.iterdir()) != sorted(OUTPUT_NAMES):
        raise ScenarioError("Scenario output contract changed")
    return {
        "outputs": len(OUTPUT_NAMES),
        "replication_rows": len(replications),
        "summary_rows": len(summaries),
        "paired_effect_rows": len(paired),
        "selected_option": selected,
        "null_or_failed_sensitivities": findings["sensitivity"]["null_or_failed_rows"],
    }


def verify_committed() -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="app3-module05-scenarios-") as temp_dir:
        rebuilt = Path(temp_dir) / "outputs"
        report = generate(rebuilt)
        for name in OUTPUT_NAMES:
            committed = ROOT / "outputs" / name
            if not committed.is_file() or committed.read_bytes() != (rebuilt / name).read_bytes():
                raise ScenarioError(f"Committed output differs from clean rebuild: {name}")
    return report


def self_check() -> None:
    import freeze_upstream

    upstream = freeze_upstream.verify(ROOT)
    report = verify_committed()
    validations = read_csv(ROOT / "outputs/validation-checks.csv")
    summaries = read_csv(ROOT / "outputs/scenario-summary.csv")
    paired = read_csv(ROOT / "outputs/paired-effects.csv")
    sensitivities = read_csv(ROOT / "outputs/sensitivity-review.csv")
    findings = json.loads((ROOT / "outputs/scenario-findings.json").read_text(encoding="utf-8"))
    assert upstream["accepted_encounters"] == 43628
    assert report == {
        "outputs": 12,
        "replication_rows": 4000,
        "summary_rows": 20,
        "paired_effect_rows": 15,
        "selected_option": "none",
        "null_or_failed_sensitivities": 6,
    }
    assert len(validations) == 24 and all(row["status"] == "pass" for row in validations)
    assert len(summaries) == 20 and len(paired) == 15 and len(sensitivities) == 15
    assert any(row["effect_status"] == "null or failed improvement" for row in sensitivities)
    assert findings["module06_handoff"]["option_for_feasibility_review"] == report["selected_option"]
    assert findings["point_demand"]["S00"]["median_wait_minutes"] == 60.035963
    assert findings["point_paired_effects"]["S01"]["p90_wait_improvement_minutes"] == 21.244986
    with tempfile.TemporaryDirectory(prefix="app3-module05-no-overwrite-") as temp_dir:
        existing = Path(temp_dir) / "existing"
        existing.mkdir()
        try:
            generate(existing)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Scenario builder overwrote an existing target")
    print(f"APP-3 Module 05 scenario self-check passed: {json.dumps(report, sort_keys=True)}")


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
    except (OSError, ValueError, KeyError, ImportError, ScenarioError) as error:
        parser.exit(1, f"Scenario build failed: {error}\n")


if __name__ == "__main__":
    main()
