"""Generate and verify the deterministic CGH-ED-01 operational teaching release."""

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
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GENERATOR_VERSION = "0.1.0"
RELEASE_ID = "cgh-ed-01-operational-v1"
SEED = "73002"
START = datetime(2024, 1, 1, tzinfo=timezone.utc)
DAYS = 364
SHIFT_NAMES = ("night", "day", "evening")
SHIFT_HOURS = {"night": 0, "day": 8, "evening": 16}
GRAINS = {
    "encounters": "one raw encounter row plus one seeded duplicate",
    "process-events": "one recorded event state per encounter and time",
    "staffing": "one synthetic role per arrival shift",
    "queue-snapshots": "one service queue per 30-minute interval",
    "safety-events": "one true event or reviewed non-event candidate",
    "calendar-demand": "one arrival shift",
    "scenarios": "one predeclared scenario without results",
    "known-truth": "one generated mechanism or null condition",
    "defect-register": "one seeded raw defect",
}
FIELDS = {
    "encounters": [
        "encounter_id", "person_id", "service_id", "arrival_shift_id", "arrival_at",
        "age_years", "acuity", "arrival_mode", "access_support_group", "disposition",
        "departure_at", "left_before_seen_flag", "return_to_encounter_id",
        "return_within_72h_flag", "source_row_status", "defect_flag", "synthetic_flag",
    ],
    "process-events": [
        "event_id", "encounter_id", "service_id", "event_type", "event_at",
        "event_sequence", "source_row_status", "defect_flag", "synthetic_flag",
    ],
    "staffing": [
        "staffing_id", "service_id", "shift_id", "shift_start", "role", "scheduled_count",
        "actual_count", "shift_hours", "scheduled_staff_hours", "actual_staff_hours",
        "overtime_hours", "absence_hours", "source_row_status", "defect_flag", "synthetic_flag",
    ],
    "queue-snapshots": [
        "snapshot_id", "service_id", "interval_start", "interval_end", "shift_id",
        "queue_start", "arrivals", "service_starts", "exits_without_service", "queue_end",
        "clinician_count", "staffed_clinician_hours_interval", "occupancy_proxy",
        "source_row_status", "defect_flag", "synthetic_flag",
    ],
    "safety-events": [
        "candidate_id", "encounter_id", "service_id", "event_at", "event_class",
        "known_true_event_flag", "trigger_flag", "incident_report_flag", "review_status",
        "severity", "source_row_status", "defect_flag", "synthetic_flag",
    ],
    "calendar-demand": [
        "shift_id", "date", "shift_name", "shift_start", "day_of_week", "week_index",
        "season", "holiday_flag", "synthetic_special_event_flag", "arrival_count",
        "source_row_status", "defect_flag", "synthetic_flag",
    ],
    "scenarios": [
        "scenario_id", "name", "change_type", "trigger_rule", "capacity_change",
        "workflow_change", "eligible_period", "outcome_measures", "balancing_measures",
        "results_status", "source_row_status", "defect_flag", "synthetic_flag",
    ],
    "known-truth": [
        "truth_id", "domain", "start_date", "end_date", "scope", "mechanism",
        "expected_direction", "release_use", "disclosure_timing", "synthetic_flag",
    ],
    "defect-register": [
        "defect_id", "table_name", "affected_key", "defect_type", "raw_effect",
        "repair_rule", "clean_disposition", "affected_measure", "owner",
        "synthetic_flag", "status",
    ],
}
FIELD_DEFINITIONS = {
    "encounter_id": "stable synthetic encounter identifier",
    "person_id": "stable synthetic person token used only for return linkage",
    "service_id": "fictional service identifier",
    "arrival_shift_id": "arrival shift assigned from the recorded arrival time",
    "arrival_at": "recorded encounter arrival timestamp",
    "age_years": "synthetic age at arrival in completed years",
    "acuity": "synthetic five-level urgency category where 1 is highest urgency",
    "arrival_mode": "synthetic arrival mode",
    "access_support_group": "synthetic service-support category used to test access measurement",
    "disposition": "recorded encounter disposition",
    "departure_at": "recorded encounter departure timestamp",
    "left_before_seen_flag": "1 when the encounter ended before clinician contact",
    "return_to_encounter_id": "prior encounter linked to a synthetic return within 72 hours",
    "return_within_72h_flag": "1 when a later synthetic encounter links back within 72 hours",
    "event_id": "stable synthetic process-event identifier",
    "event_type": "declared process state",
    "event_at": "recorded process-event timestamp",
    "event_sequence": "expected order of the process state",
    "staffing_id": "stable synthetic staffing-row identifier",
    "shift_id": "stable date and shift identifier",
    "shift_start": "start timestamp for the eight-hour arrival shift",
    "role": "synthetic workforce role",
    "scheduled_count": "scheduled synthetic staff count",
    "actual_count": "actual synthetic staff count after absence",
    "shift_hours": "scheduled hours in the shift",
    "scheduled_staff_hours": "scheduled count multiplied by shift hours",
    "actual_staff_hours": "actual count multiplied by shift hours plus overtime",
    "overtime_hours": "synthetic hours worked beyond the scheduled count-hours",
    "absence_hours": "scheduled count-hours not supplied because of absence",
    "snapshot_id": "stable queue-snapshot identifier",
    "interval_start": "start of the 30-minute queue interval",
    "interval_end": "end of the 30-minute queue interval",
    "queue_start": "encounters waiting for first clinician contact at interval start",
    "arrivals": "qualifying arrivals during the interval",
    "service_starts": "first clinician contacts during the interval",
    "exits_without_service": "left-before-seen departures during the interval",
    "queue_end": "queue_start plus arrivals minus service starts and exits without service",
    "clinician_count": "physician and advanced-practice clinician count for the shift",
    "staffed_clinician_hours_interval": "clinician count multiplied by one half hour",
    "occupancy_proxy": "queue end divided by clinician count and bounded for display",
    "candidate_id": "stable synthetic safety-review candidate identifier",
    "event_class": "error, near miss, adverse event, harm, or reviewed non-event",
    "known_true_event_flag": "generated truth used to evaluate surveillance",
    "trigger_flag": "1 when the synthetic surveillance trigger fired",
    "incident_report_flag": "1 when a synthetic incident report was submitted",
    "review_status": "status of synthetic safety review",
    "severity": "synthetic event-severity category",
    "date": "calendar date for the arrival shift",
    "shift_name": "night, day, or evening arrival shift",
    "day_of_week": "English weekday name",
    "week_index": "one-based week number within the 52-week release",
    "season": "calendar season used as a forecast feature",
    "holiday_flag": "1 for a declared synthetic holiday date",
    "synthetic_special_event_flag": "1 during a declared generated demand event",
    "arrival_count": "raw encounter arrivals assigned to the shift",
    "scenario_id": "stable predeclared scenario identifier",
    "name": "plain-language scenario name",
    "change_type": "capacity, workflow, combined, or no-change classification",
    "trigger_rule": "predeclared condition that would activate the scenario",
    "capacity_change": "predeclared capacity assumption without a result",
    "workflow_change": "predeclared workflow assumption without a result",
    "eligible_period": "period for later scenario evaluation",
    "outcome_measures": "declared later outcome measures",
    "balancing_measures": "declared later balancing measures",
    "results_status": "states that scenario results are not present in Module 02",
    "truth_id": "stable generated-truth identifier",
    "domain": "generated mechanism domain",
    "start_date": "first date on which the mechanism applies",
    "end_date": "last date on which the mechanism applies",
    "scope": "shift, subgroup, service, or release scope",
    "mechanism": "generated mechanism or null condition",
    "expected_direction": "direction expected if the mechanism is recovered",
    "release_use": "later module that may use the truth record",
    "disclosure_timing": "when learners may compare results with generated truth",
    "defect_id": "stable seeded-defect identifier",
    "table_name": "raw table containing the seeded defect",
    "affected_key": "row or relationship affected by the defect",
    "defect_type": "duplicate, missing, invalid, impossible, or inconsistent classification",
    "raw_effect": "observable effect in the immutable raw layer",
    "repair_rule": "predeclared deterministic clean-layer rule",
    "clean_disposition": "repair, quarantine, deduplicate, or retain unavailable",
    "affected_measure": "measure or invariant changed by the defect",
    "owner": "role accountable for the repair decision",
    "source_row_status": "original or seeded-defect source status",
    "defect_flag": "seeded defect ID or blank",
    "synthetic_flag": "must equal 1 for every row",
    "status": "open or closed defect disposition",
}


class ReleaseError(RuntimeError):
    pass


def iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def dt(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def uniform(key: str, index: int = 0) -> float:
    digest = hashlib.sha256(f"{SEED}|{key}|{index}".encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") / 2**64


def normal(key: str) -> float:
    first = max(uniform(key, 0), 1e-12)
    second = uniform(key, 1)
    return math.sqrt(-2.0 * math.log(first)) * math.cos(2.0 * math.pi * second)


def choose(key: str, choices: list[tuple[str, float]]) -> str:
    value = uniform(key)
    cumulative = 0.0
    for label, probability in choices:
        cumulative += probability
        if value < cumulative:
            return label
    return choices[-1][0]


def bounded_int(value: float, low: int, high: int) -> int:
    return max(low, min(high, int(round(value))))


def season(day: datetime) -> str:
    month = day.month
    if month in {12, 1, 2}:
        return "winter"
    if month in {3, 4, 5}:
        return "spring"
    if month in {6, 7, 8}:
        return "summer"
    return "fall"


def shift_id(day: datetime, shift_name: str) -> str:
    return f"{day:%Y%m%d}-{shift_name}"


def shift_for_time(value: datetime) -> str:
    if value.hour < 8:
        name = "night"
    elif value.hour < 16:
        name = "day"
    else:
        name = "evening"
    return shift_id(value, name)


def half_hour(value: datetime) -> datetime:
    minute = 0 if value.minute < 30 else 30
    return value.replace(minute=minute, second=0, microsecond=0)


def gzip_bytes(raw: bytes) -> bytes:
    output = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
        zipped.write(raw)
    return output.getvalue()


def csv_bytes(fields: list[str], rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def generate() -> dict[str, list[dict[str, object]]]:
    calendar: list[dict[str, object]] = []
    staffing: list[dict[str, object]] = []
    encounters: list[dict[str, object]] = []
    events: list[dict[str, object]] = []
    safety: list[dict[str, object]] = []
    staff_by_shift: dict[str, dict[str, int]] = {}
    holiday_dates = {"2024-01-01", "2024-07-04", "2024-11-28", "2024-12-25"}
    bases = {"night": 27.0, "day": 49.0, "evening": 42.0}
    weekday_factor = {0: 1.10, 1: 1.02, 2: 1.00, 3: 1.01, 4: 1.06, 5: 0.92, 6: 0.89}
    staffing_counts = {
        "night": {"physician": 2, "advanced_practice_clinician": 1, "registered_nurse": 5, "technician": 2},
        "day": {"physician": 4, "advanced_practice_clinician": 3, "registered_nurse": 9, "technician": 4},
        "evening": {"physician": 3, "advanced_practice_clinician": 2, "registered_nurse": 8, "technician": 3},
    }
    shift_plan: list[tuple[datetime, str, int, str]] = []
    for day_index in range(DAYS):
        day = START + timedelta(days=day_index)
        week_index = day_index // 7 + 1
        for name in SHIFT_NAMES:
            sid = shift_id(day, name)
            start = day + timedelta(hours=SHIFT_HOURS[name])
            seasonal = 1.0 + 0.10 * math.cos(2 * math.pi * (day_index - 15) / 364)
            signal = 1.10 if 27 <= week_index <= 32 else 1.0
            holiday = 1 if f"{day:%Y-%m-%d}" in holiday_dates else 0
            holiday_factor = 0.90 if holiday else 1.0
            expected = bases[name] * weekday_factor[day.weekday()] * seasonal * signal * holiday_factor
            count = max(8, int(round(expected + math.sqrt(expected) * normal(f"count|{sid}"))))
            shift_plan.append((start, name, count, sid))
            calendar.append({
                "shift_id": sid, "date": f"{day:%Y-%m-%d}", "shift_name": name,
                "shift_start": iso(start), "day_of_week": day.strftime("%A"),
                "week_index": week_index, "season": season(day), "holiday_flag": holiday,
                "synthetic_special_event_flag": 1 if 27 <= week_index <= 32 else 0,
                "arrival_count": count, "source_row_status": "original", "defect_flag": "",
                "synthetic_flag": 1,
            })
            staff_by_shift[sid] = {}
            for role_index, (role, scheduled) in enumerate(staffing_counts[name].items(), start=1):
                absent = 1 if uniform(f"absence|{sid}|{role}") < (0.035 if role in {"physician", "advanced_practice_clinician"} else 0.055) else 0
                actual = max(1, scheduled - absent)
                overtime = 0
                if uniform(f"overtime|{sid}|{role}") < 0.08:
                    overtime = 2 if role in {"physician", "advanced_practice_clinician"} else 4
                scheduled_hours = scheduled * 8
                actual_hours = actual * 8 + overtime
                staff_by_shift[sid][role] = actual
                staffing.append({
                    "staffing_id": f"ST-{day_index + 1:03d}-{SHIFT_NAMES.index(name) + 1}-{role_index}",
                    "service_id": "CGH-ED-01", "shift_id": sid, "shift_start": iso(start),
                    "role": role, "scheduled_count": scheduled, "actual_count": actual,
                    "shift_hours": 8, "scheduled_staff_hours": scheduled_hours,
                    "actual_staff_hours": actual_hours, "overtime_hours": overtime,
                    "absence_hours": absent * 8, "source_row_status": "original",
                    "defect_flag": "", "synthetic_flag": 1,
                })

    event_number = 0
    recent_discharges: list[tuple[str, datetime, str]] = []
    returned_index_ids: set[str] = set()
    original_by_id: dict[str, dict[str, object]] = {}
    underlying_events: list[dict[str, object]] = []
    encounter_number = 0
    for shift_start, name, count, sid in shift_plan:
        clinicians = staff_by_shift[sid]["physician"] + staff_by_shift[sid]["advanced_practice_clinician"]
        congestion = count / max(clinicians * 8.0, 1.0)
        week_index = (shift_start.date() - START.date()).days // 7 + 1
        for within in range(count):
            encounter_number += 1
            eid = f"E{encounter_number:06d}"
            offset = ((within + uniform(f"arrival|{eid}")) / count) * 8 * 60
            arrival = shift_start + timedelta(minutes=offset)
            recent_discharges = [item for item in recent_discharges if arrival - timedelta(hours=72) <= item[1] <= arrival and item[2] not in returned_index_ids]
            return_to = ""
            if recent_discharges and uniform(f"return|{eid}") < 0.042:
                index = min(len(recent_discharges) - 1, int(uniform(f"return-pick|{eid}") * len(recent_discharges)))
                person_id, _, return_to = recent_discharges[index]
                returned_index_ids.add(return_to)
            else:
                person_id = f"P{encounter_number:06d}"
            acuity = choose(f"acuity|{eid}", [("1", 0.05), ("2", 0.18), ("3", 0.44), ("4", 0.25), ("5", 0.08)])
            access = choose(f"access|{eid}", [("standard", 0.78), ("language_support", 0.14), ("mobility_support", 0.08)])
            age = bounded_int(18 + uniform(f"age|{eid}") * 72, 18, 90)
            ambulance_probability = {"1": 0.75, "2": 0.44, "3": 0.20, "4": 0.07, "5": 0.03}[acuity]
            arrival_mode = "ambulance" if uniform(f"mode|{eid}") < ambulance_probability else "walk_in"
            triage_delay = bounded_int(3 + 7 * congestion + 5 * uniform(f"triage|{eid}"), 1, 45)
            acuity_room = {"1": 2, "2": 8, "3": 18, "4": 30, "5": 38}[acuity]
            room_delay = bounded_int(acuity_room + 22 * congestion + 18 * uniform(f"room|{eid}"), 2, 180)
            clinician_after_room = {"1": 2, "2": 7, "3": 14, "4": 22, "5": 28}[acuity]
            support_delay = 10 if access == "language_support" and name in {"night", "evening"} else 4 if access == "mobility_support" else 0
            known_bottleneck_delay = 18 if 35 <= week_index <= 44 and name == "evening" else 0
            clinician_delay = bounded_int(room_delay + clinician_after_room + 24 * congestion + support_delay + known_bottleneck_delay + 12 * uniform(f"clinician|{eid}"), room_delay + 1, 300)
            low_acuity = acuity in {"4", "5"}
            lbbs_probability = 0.0
            if low_acuity:
                logit = -4.2 + 0.025 * clinician_delay + (0.35 if access == "language_support" else 0.0)
                lbbs_probability = 1.0 / (1.0 + math.exp(-logit))
            left = uniform(f"lbbs|{eid}") < lbbs_probability
            triage_time = arrival + timedelta(minutes=triage_delay)
            roomed_time = arrival + timedelta(minutes=room_delay)
            clinician_time = arrival + timedelta(minutes=clinician_delay)
            if left:
                leave_delay = bounded_int(max(triage_delay + 5, clinician_delay * (0.55 + 0.2 * uniform(f"leave|{eid}"))), 15, 240)
                disposition = "left_before_seen"
                departure = arrival + timedelta(minutes=leave_delay)
            else:
                disposition = choose(f"disposition|{eid}", [("discharge", 0.72), ("admit", 0.19), ("transfer", 0.04), ("observation", 0.05)])
                service_base = {"1": 230, "2": 190, "3": 130, "4": 90, "5": 65}[acuity]
                disposition_add = {"discharge": 25, "admit": 110, "transfer": 160, "observation": 90}[disposition]
                service_minutes = bounded_int(service_base + disposition_add + 70 * uniform(f"service|{eid}"), 45, 540)
                disposition_time = clinician_time + timedelta(minutes=max(20, service_minutes - 20))
                departure = clinician_time + timedelta(minutes=service_minutes)
            encounter = {
                "encounter_id": eid, "person_id": person_id, "service_id": "CGH-ED-01",
                "arrival_shift_id": sid, "arrival_at": iso(arrival), "age_years": age,
                "acuity": acuity, "arrival_mode": arrival_mode, "access_support_group": access,
                "disposition": disposition, "departure_at": iso(departure),
                "left_before_seen_flag": 1 if left else 0, "return_to_encounter_id": return_to,
                "return_within_72h_flag": 0, "source_row_status": "original",
                "defect_flag": "", "synthetic_flag": 1,
            }
            encounters.append(encounter)
            original_by_id[eid] = encounter
            if return_to:
                original_by_id[return_to]["return_within_72h_flag"] = 1
            if not left and disposition == "discharge":
                recent_discharges.append((person_id, departure, eid))

            states: list[tuple[str, datetime, int]] = [("arrival", arrival, 1), ("triage", triage_time, 2)]
            if not left:
                states.extend([("roomed", roomed_time, 3), ("clinician", clinician_time, 4), ("disposition", disposition_time, 5)])
            states.append(("departure", departure, 6))
            for event_type, event_at, sequence in states:
                event_number += 1
                event = {
                    "event_id": f"EV{event_number:07d}", "encounter_id": eid,
                    "service_id": "CGH-ED-01", "event_type": event_type,
                    "event_at": iso(event_at), "event_sequence": sequence,
                    "source_row_status": "original", "defect_flag": "", "synthetic_flag": 1,
                }
                events.append(event)
                underlying_events.append(dict(event))

            if not left:
                true_probability = 0.020 + (0.008 if acuity in {"1", "2"} else 0.0)
                safety_value = uniform(f"safety|{eid}")
                if safety_value < true_probability:
                    event_class = choose(f"safety-class|{eid}", [("error", 0.35), ("near_miss", 0.30), ("adverse_event", 0.25), ("harm", 0.10)])
                    trigger_probability = {"error": 0.64, "near_miss": 0.70, "adverse_event": 0.84, "harm": 0.94}[event_class]
                    report_probability = {"error": 0.24, "near_miss": 0.34, "adverse_event": 0.63, "harm": 0.86}[event_class]
                    severity = {"error": "none", "near_miss": "none", "adverse_event": "temporary", "harm": "serious"}[event_class]
                    safety.append({
                        "candidate_id": f"SC{len(safety) + 1:06d}", "encounter_id": eid,
                        "service_id": "CGH-ED-01", "event_at": iso(clinician_time + timedelta(minutes=15)),
                        "event_class": event_class, "known_true_event_flag": 1,
                        "trigger_flag": 1 if uniform(f"trigger|{eid}") < trigger_probability else 0,
                        "incident_report_flag": 1 if uniform(f"report|{eid}") < report_probability else 0,
                        "review_status": "reviewed", "severity": severity,
                        "source_row_status": "original", "defect_flag": "", "synthetic_flag": 1,
                    })
                elif uniform(f"false-trigger|{eid}") < 0.010:
                    safety.append({
                        "candidate_id": f"SC{len(safety) + 1:06d}", "encounter_id": eid,
                        "service_id": "CGH-ED-01", "event_at": iso(clinician_time + timedelta(minutes=20)),
                        "event_class": "reviewed_non_event", "known_true_event_flag": 0,
                        "trigger_flag": 1, "incident_report_flag": 0,
                        "review_status": "reviewed", "severity": "none",
                        "source_row_status": "original", "defect_flag": "", "synthetic_flag": 1,
                    })

    interval_counts: dict[datetime, Counter[str]] = defaultdict(Counter)
    for encounter in encounters:
        interval_counts[half_hour(dt(str(encounter["arrival_at"])))] ["arrivals"] += 1
        if int(encounter["left_before_seen_flag"]) == 1:
            interval_counts[half_hour(dt(str(encounter["departure_at"])))] ["exits"] += 1
    for event in underlying_events:
        if event["event_type"] == "clinician":
            interval_counts[half_hour(dt(str(event["event_at"])))] ["starts"] += 1
    queue: list[dict[str, object]] = []
    queue_value = 0
    interval = START
    last_interval = START + timedelta(days=DAYS + 1)
    snapshot_number = 0
    while interval < last_interval:
        snapshot_number += 1
        counts = interval_counts[interval]
        start_queue = queue_value
        queue_value = start_queue + counts["arrivals"] - counts["starts"] - counts["exits"]
        if queue_value < 0:
            raise ReleaseError(f"Generated queue went negative at {iso(interval)}")
        sid = shift_for_time(interval)
        staff = staff_by_shift.get(sid, {"physician": 0, "advanced_practice_clinician": 0})
        clinicians = staff.get("physician", 0) + staff.get("advanced_practice_clinician", 0)
        occupancy = round(min(queue_value / max(clinicians * 4, 1), 9.9999), 4)
        queue.append({
            "snapshot_id": f"QS{snapshot_number:06d}", "service_id": "CGH-ED-01",
            "interval_start": iso(interval), "interval_end": iso(interval + timedelta(minutes=30)),
            "shift_id": sid, "queue_start": start_queue, "arrivals": counts["arrivals"],
            "service_starts": counts["starts"], "exits_without_service": counts["exits"],
            "queue_end": queue_value, "clinician_count": clinicians,
            "staffed_clinician_hours_interval": round(clinicians * 0.5, 2),
            "occupancy_proxy": f"{occupancy:.4f}", "source_row_status": "original",
            "defect_flag": "", "synthetic_flag": 1,
        })
        interval += timedelta(minutes=30)

    completed = [row for row in encounters if int(row["left_before_seen_flag"]) == 0]
    selected = {
        "D001": encounters[100], "D002": encounters[200], "D003": encounters[300],
        "D004": encounters[400], "D005": completed[500], "D007": completed[600],
        "D008": completed[700],
    }
    defects: list[dict[str, object]] = []

    duplicate = dict(selected["D001"])
    duplicate["source_row_status"] = "seeded_defect"
    duplicate["defect_flag"] = "D001"
    encounters.append(duplicate)
    defects.append(defect("D001", "encounters", str(duplicate["encounter_id"]), "duplicate", "duplicate encounter row inflates raw arrival and denominator counts", "retain the first encounter_id row", "deduplicate", "all encounter denominators", "data-quality reviewer"))

    selected["D002"]["arrival_at"] = ""
    selected["D002"]["source_row_status"] = "seeded_defect"
    selected["D002"]["defect_flag"] = "D002"
    defects.append(defect("D002", "encounters", str(selected["D002"]["encounter_id"]), "missing", "encounter arrival is blank while the arrival event remains", "recover from the unique arrival process event", "repair", "arrival clocks and shift attribution", "measure steward"))

    selected["D003"]["service_id"] = "010001"
    selected["D003"]["source_row_status"] = "seeded_defect"
    selected["D003"]["defect_flag"] = "D003"
    defects.append(defect("D003", "encounters", str(selected["D003"]["encounter_id"]), "invalid", "public-like facility identifier violates the fictional-service boundary", "exclude any encounter whose service_id is not CGH-ED-01", "quarantine", "service population", "source steward"))

    selected["D004"]["age_years"] = 17
    selected["D004"]["source_row_status"] = "seeded_defect"
    selected["D004"]["defect_flag"] = "D004"
    defects.append(defect("D004", "encounters", str(selected["D004"]["encounter_id"]), "invalid", "age is outside the declared adult service population", "exclude age under 18 from the analytic population", "quarantine", "adult encounter denominator", "clinical reviewer"))

    selected["D005"]["departure_at"] = iso(dt(str(selected["D005"]["arrival_at"])) - timedelta(hours=1))
    selected["D005"]["source_row_status"] = "seeded_defect"
    selected["D005"]["defect_flag"] = "D005"
    defects.append(defect("D005", "encounters", str(selected["D005"]["encounter_id"]), "impossible", "encounter departure precedes arrival", "recover from the unique departure process event", "repair", "arrival-to-departure time", "measure steward"))

    duplicate_event = next(row for row in events if row["encounter_id"] == selected["D001"]["encounter_id"] and row["event_type"] == "arrival")
    event_copy = dict(duplicate_event)
    event_copy["source_row_status"] = "seeded_defect"
    event_copy["defect_flag"] = "D006"
    events.append(event_copy)
    defects.append(defect("D006", "process-events", str(event_copy["event_id"]), "duplicate", "duplicate event inflates raw event counts", "retain the first event_id row", "deduplicate", "event completion and sequence", "data-quality reviewer"))

    triage_event = next(row for row in events if row["encounter_id"] == selected["D007"]["encounter_id"] and row["event_type"] == "triage")
    roomed_event = next(row for row in events if row["encounter_id"] == selected["D007"]["encounter_id"] and row["event_type"] == "roomed")
    triage_event["event_at"], roomed_event["event_at"] = roomed_event["event_at"], triage_event["event_at"]
    for row in (triage_event, roomed_event):
        row["source_row_status"] = "seeded_defect"
        row["defect_flag"] = "D007"
    defects.append(defect("D007", "process-events", str(selected["D007"]["encounter_id"]), "impossible", "triage and rooming timestamps are swapped", "swap the two timestamps only for the declared defect pair", "repair", "ordered-event completion", "clinical process reviewer"))

    missing_clinician = next(row for row in events if row["encounter_id"] == selected["D008"]["encounter_id"] and row["event_type"] == "clinician")
    events.remove(missing_clinician)
    selected["D008"]["source_row_status"] = "seeded_defect"
    selected["D008"]["defect_flag"] = "D008"
    defects.append(defect("D008", "process-events", str(selected["D008"]["encounter_id"]), "missing", "completed encounter has no recorded clinician contact", "retain the encounter and mark clinician-time measures unavailable", "retain unavailable", "arrival-to-clinician support", "measure steward"))

    queue[1000]["queue_end"] = -3
    queue[1000]["source_row_status"] = "seeded_defect"
    queue[1000]["defect_flag"] = "D009"
    defects.append(defect("D009", "queue-snapshots", str(queue[1000]["snapshot_id"]), "impossible", "raw queue end is negative", "recalculate from queue start arrivals service starts and exits", "repair", "queue conservation", "operations reviewer"))

    staffing[500]["actual_staff_hours"] = -8
    staffing[500]["source_row_status"] = "seeded_defect"
    staffing[500]["defect_flag"] = "D010"
    defects.append(defect("D010", "staffing", str(staffing[500]["staffing_id"]), "impossible", "actual staff hours are negative", "recalculate from actual count shift hours and overtime", "repair", "staffed hours and utilization", "workforce reviewer"))

    if len(safety) < 101:
        raise ReleaseError("Safety generator produced too few rows for the defect contract")
    safety_copy = dict(safety[100])
    safety_copy["source_row_status"] = "seeded_defect"
    safety_copy["defect_flag"] = "D011"
    safety.append(safety_copy)
    defects.append(defect("D011", "safety-events", str(safety_copy["candidate_id"]), "duplicate", "duplicate candidate inflates safety and surveillance counts", "retain the first candidate_id row", "deduplicate", "safety rate and surveillance diagnostics", "safety reviewer"))

    calendar[200]["arrival_count"] = int(calendar[200]["arrival_count"]) + 5
    calendar[200]["source_row_status"] = "seeded_defect"
    calendar[200]["defect_flag"] = "D012"
    defects.append(defect("D012", "calendar-demand", str(calendar[200]["shift_id"]), "inconsistent", "shift arrival count exceeds linked raw encounters by five", "derive accepted demand from clean encounters grouped by arrival shift", "repair", "arrivals per shift", "forecasting reviewer"))

    scenarios = [
        scenario("S00", "No change", "no_change", "none", "none", "none"),
        scenario("S01", "Flex clinician coverage", "capacity", "activate only under a later predeclared demand threshold", "one additional synthetic clinician block", "none"),
        scenario("S02", "Fast-track activation", "workflow", "activate only under a later predeclared queue threshold", "no net staff addition", "route eligible low-acuity encounters through a bounded fast-track process"),
        scenario("S03", "Combined bounded rule", "combined", "activate only when both later thresholds are met", "one additional synthetic clinician block", "bounded fast-track routing"),
    ]
    truths = [
        truth("KT01", "release", "2024-01-01", "2024-12-29", "service", "all operational records are synthetic and have no public hospital source", "no public linkage", "all modules", "at release"),
        truth("KT02", "demand", "2024-01-01", "2024-12-29", "service", "smooth winter seasonality is present in generated arrivals", "higher winter demand", "Module 04", "after independent forecast review"),
        truth("KT03", "demand", "2024-01-01", "2024-12-29", "weekday", "Monday arrival demand is generated above the weekly reference level", "higher Monday demand", "Module 04", "after independent forecast review"),
        truth("KT04", "demand", "2024-07-01", "2024-08-11", "weeks 27 through 32", "a bounded synthetic special-event demand increase is present", "higher demand", "Modules 03 and 04", "after independent signal review"),
        truth("KT05", "flow", "2024-08-26", "2024-11-03", "evening shifts in weeks 35 through 44", "first-clinician delay receives an added generated process delay", "higher arrival-to-clinician time", "Module 03", "after independent bottleneck review"),
        truth("KT06", "access", "2024-01-01", "2024-12-29", "language-support encounters on night and evening shifts", "the fictional process adds support delay because immediate language support is not always available", "higher delay and possible left-before-seen burden", "Modules 03 through 07", "after support and governance review"),
        truth("KT07", "safety", "2024-01-01", "2024-12-29", "true synthetic safety events", "incident reporting probability is lower than complete known truth and differs by event class", "undercapture", "Module 03", "after surveillance calculation"),
        truth("KT08", "variation", "2024-01-01", "2024-12-29", "all other periods", "routine random variation remains after declared generated mechanisms", "no guaranteed signal", "Module 03", "after chart construction"),
        truth("KT09", "scenario", "2024-01-01", "2024-12-29", "S01 through S03", "scenario effects are not generated in Module 02", "no result available", "Module 05", "after scenario model validation"),
        truth("KT10", "scenario", "2024-01-01", "2024-12-29", "at least one later sensitivity condition", "the course must retain a null or failed improvement condition", "no guaranteed benefit", "Modules 05 through 07", "after sensitivity analysis"),
    ]
    return {
        "encounters": encounters, "process-events": events, "staffing": staffing,
        "queue-snapshots": queue, "safety-events": safety, "calendar-demand": calendar,
        "scenarios": scenarios, "known-truth": truths, "defect-register": defects,
    }


def defect(defect_id: str, table: str, key: str, kind: str, effect: str, rule: str, disposition: str, measure: str, owner: str) -> dict[str, object]:
    return {"defect_id": defect_id, "table_name": table, "affected_key": key, "defect_type": kind, "raw_effect": effect, "repair_rule": rule, "clean_disposition": disposition, "affected_measure": measure, "owner": owner, "synthetic_flag": 1, "status": "open for learner repair"}


def scenario(identifier: str, name: str, change_type: str, trigger: str, capacity: str, workflow: str) -> dict[str, object]:
    return {"scenario_id": identifier, "name": name, "change_type": change_type, "trigger_rule": trigger, "capacity_change": capacity, "workflow_change": workflow, "eligible_period": "to be declared in Module 05", "outcome_measures": "arrival-to-clinician; arrival-to-departure; throughput", "balancing_measures": "left before seen; 72-hour return; safety; subgroup gap; overtime", "results_status": "not run in Module 02", "source_row_status": "original", "defect_flag": "", "synthetic_flag": 1}


def truth(identifier: str, domain: str, start: str, end: str, scope: str, mechanism: str, direction: str, use: str, timing: str) -> dict[str, object]:
    return {"truth_id": identifier, "domain": domain, "start_date": start, "end_date": end, "scope": scope, "mechanism": mechanism, "expected_direction": direction, "release_use": use, "disclosure_timing": timing, "synthetic_flag": 1}


def write_dictionary(target: Path) -> None:
    fields = ["field_id", "table", "field", "data_type", "grain", "field_class", "definition", "missing_meaning", "allowed_use", "prohibited_interpretation"]
    rows = []
    number = 0
    numeric_tokens = ("count", "hours", "flag", "sequence", "queue", "arrivals", "starts", "exits", "age", "acuity", "week_index", "arrival_count", "occupancy")
    for table, table_fields in FIELDS.items():
        for name in table_fields:
            number += 1
            data_type = "integer" if any(token in name for token in numeric_tokens) and not name.endswith("_id") else "text"
            if name.endswith("_at") or name in {"shift_start", "interval_start", "interval_end", "event_at", "arrival_at", "departure_at"}:
                data_type = "UTC timestamp"
            definition = FIELD_DEFINITIONS.get(name, name.replace("_", " "))
            missing = "not permitted" if name in {table_fields[0], "synthetic_flag"} else "blank means unavailable or not applicable under the declared state"
            rows.append({
                "field_id": f"D{number:03d}", "table": f"{table}.csv.gz", "field": name,
                "data_type": data_type, "grain": GRAINS[table],
                "field_class": "synthetic audit" if name in {"source_row_status", "defect_flag", "synthetic_flag"} else "synthetic source",
                "definition": definition, "missing_meaning": missing,
                "allowed_use": "curriculum construction, measure validation, and synthetic teaching analysis",
                "prohibited_interpretation": "real patient, hospital, clinician, workforce, prevalence, quality, staffing, causal, or implementation claim",
            })
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_release(output_root: Path) -> list[dict[str, object]]:
    raw_root = output_root / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    tables = generate()
    manifest = []
    for table in GRAINS:
        rows = tables[table]
        raw = csv_bytes(FIELDS[table], rows)
        zipped = gzip_bytes(raw)
        filename = f"{table}.csv.gz"
        (raw_root / filename).write_bytes(zipped)
        manifest.append({
            "source_id": f"{RELEASE_ID}:{table}", "relative_path": f"data/raw/{filename}",
            "grain": GRAINS[table], "rows": len(rows), "columns": len(FIELDS[table]),
            "raw_bytes": len(raw), "raw_sha256": sha256_bytes(raw), "gzip_bytes": len(zipped),
            "gzip_sha256": sha256_bytes(zipped), "generator_version": GENERATOR_VERSION,
            "seed": SEED, "synthetic_flag": 1,
        })
    manifest_fields = ["source_id", "relative_path", "grain", "rows", "columns", "raw_bytes", "raw_sha256", "gzip_bytes", "gzip_sha256", "generator_version", "seed", "synthetic_flag"]
    with (output_root / "operational-source-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=manifest_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)
    write_dictionary(output_root / "data-dictionary.csv")
    return manifest


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def verify(root: Path = ROOT) -> dict[str, object]:
    data_root = root / "data"
    manifest = read_manifest(data_root / "operational-source-manifest.csv")
    if len(manifest) != 9:
        raise ReleaseError(f"Expected nine raw sources, found {len(manifest)}")
    total_rows = 0
    for row in manifest:
        table = Path(row["relative_path"]).name.removesuffix(".csv.gz")
        path = root / row["relative_path"]
        zipped = path.read_bytes()
        raw = gzip.decompress(zipped)
        if len(zipped) != int(row["gzip_bytes"]) or sha256_bytes(zipped) != row["gzip_sha256"]:
            raise ReleaseError(f"Gzip identity mismatch: {table}")
        if len(raw) != int(row["raw_bytes"]) or sha256_bytes(raw) != row["raw_sha256"]:
            raise ReleaseError(f"Raw identity mismatch: {table}")
        reader = csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""))
        rows = list(reader)
        if reader.fieldnames != FIELDS[table] or len(rows) != int(row["rows"]):
            raise ReleaseError(f"Shape mismatch: {table}")
        if any(item["synthetic_flag"] != "1" for item in rows):
            raise ReleaseError(f"Non-synthetic row found: {table}")
        total_rows += len(rows)
    return {"tables": len(manifest), "total_rows": total_rows, "manifest_rows": {Path(row["relative_path"]).stem.replace(".csv", ""): int(row["rows"]) for row in manifest}}


def self_check() -> None:
    committed = verify()
    with tempfile.TemporaryDirectory(prefix="app3-module02-generate-") as temp_dir:
        temp = Path(temp_dir)
        generated_data = temp / "data"
        build_release(generated_data)
        generated_manifest = read_manifest(generated_data / "operational-source-manifest.csv")
        committed_manifest = read_manifest(ROOT / "data/operational-source-manifest.csv")
        if generated_manifest != committed_manifest:
            raise AssertionError("Regenerated source manifest differs from the committed release")
        for row in committed_manifest:
            relative = Path(row["relative_path"]).relative_to("data")
            if (generated_data / relative).read_bytes() != (ROOT / row["relative_path"]).read_bytes():
                raise AssertionError(f"Regenerated source differs: {row['relative_path']}")
        changed = temp / "changed"
        shutil.copytree(ROOT / "data", changed / "data")
        first = changed / committed_manifest[0]["relative_path"]
        first.write_bytes(first.read_bytes() + b"x")
        try:
            verify(changed)
        except (OSError, ReleaseError):
            pass
        else:
            raise AssertionError("Verifier accepted a changed source")
    print(f"APP-3 Module 02 generator self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.write:
            output = (args.output_root or (ROOT / "data")).resolve()
            print(json.dumps({"status": "pass", "sources": build_release(output)}, indent=2))
        else:
            print(json.dumps(verify(), indent=2))
    except (OSError, ValueError, KeyError, ReleaseError) as error:
        parser.exit(1, f"Operational release generation failed: {error}\n")


if __name__ == "__main__":
    main()
