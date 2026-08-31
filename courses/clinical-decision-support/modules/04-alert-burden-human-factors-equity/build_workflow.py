"""Build the deterministic APP-4 Module 04 synthetic workflow evidence."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import shutil
import statistics
import tempfile
from collections import Counter, defaultdict
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = MODULE_ROOT.parent.parent
MODULE02_ROOT = COURSE_ROOT / "modules/02-logic-triggers-data"
MODULE03_ROOT = COURSE_ROOT / "modules/03-evidence-calibration-validation"
CHECKPOINT_ROOT = COURSE_ROOT / "checkpoints/01-logic-evidence-validation-readiness"
REFERENCE_DATE = date(2026, 8, 31)
THRESHOLDS = (0.02, 0.03, 0.04, 0.05, 0.075, 0.10)
REPEAT_PATIENTS = 200
SESSIONS = 120
CLINICIANS = 12
ENCOUNTERS_PER_SESSION = 10
SOURCE_CONTRACT = {
    "module02-patient": (
        MODULE02_ROOT / "data/synthetic-release/fhir/Patient.ndjson.gz",
        235743,
        "167fc8a4d52d2195cfbcc7282dd390e647b13c48dc51cceb9d37d78131619b74",
    ),
    "module02-observation": (
        MODULE02_ROOT / "data/synthetic-release/fhir/Observation.ndjson.gz",
        21844378,
        "f2d7c14001ef3f656db0e51d23f5099a228c1f357e82d0b9c8134fa3751f6982",
    ),
    "module02-condition": (
        MODULE02_ROOT / "data/synthetic-release/fhir/Condition.ndjson.gz",
        1578721,
        "63ceed4bdebc61c8570302d474b464f872cb0412637569123decc580044556df",
    ),
    "module02-synthetic-release": (
        MODULE02_ROOT / "data/synthetic-release/synthetic-release.json",
        1089,
        "4daa5f934a949852c30ab2909aae6e6681532633fa6da7b96e64853a90419e28",
    ),
    "module03-threshold-audit": (
        MODULE03_ROOT / "data/evidence/threshold-audit.csv",
        5089,
        "51e98dad554bda526d9497ae31487cd7a1c237573ae17239c2063af3ed925e10",
    ),
    "module03-model-coefficients": (
        MODULE03_ROOT / "data/evidence/model-coefficients.csv",
        1149,
        "cfecfbadfc88a1b9ec9935ac5865627686731d5022a1cf691aa626a876ecbe0b",
    ),
    "module03-performance": (
        MODULE03_ROOT / "data/evidence/performance.csv",
        1413,
        "dd3abf11aef8fad8ea1f04a66e16e7c545a80975181f4914527e63d7e4a1d035",
    ),
    "checkpoint-contract": (
        CHECKPOINT_ROOT / "checkpoint-contract.json",
        2282,
        "3005bdaf4a28ae0cd4c6efd43c90d1c1272907a7a15275204fb961720458a931",
    ),
    "checkpoint-release": (
        CHECKPOINT_ROOT / "release.json",
        3489,
        "8f637bef551ebe5cb91e93b3b91fef51f25736d07168b904851405c703b62c03",
    ),
}
OUTPUT_FILES = (
    "data/workflow/patient-frame.csv.gz",
    "data/workflow/encounter-opportunities.csv.gz",
    "data/workflow/candidate-events.csv.gz",
    "outputs/workflow-profile.csv",
    "outputs/candidate-burden.csv",
    "outputs/design-comparison.csv",
    "outputs/session-burden.csv.gz",
    "outputs/equity-slices.csv",
    "outputs/invariant-checks.csv",
    "build-report.json",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def stable_number(value: str, modulus: int = 100) -> int:
    return int.from_bytes(hashlib.sha256(value.encode("utf-8")).digest()[:8], "big") % modulus


def fmt(value: float | None, places: int = 8) -> str:
    return "" if value is None else f"{value:.{places}f}"


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_gzip_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            with io.TextIOWrapper(zipped, encoding="utf-8", newline="") as text:
                writer = csv.DictWriter(text, fieldnames=fields, lineterminator="\n")
                writer.writeheader()
                writer.writerows(rows)


def read_gzip_csv(path: Path) -> list[dict[str, str]]:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def verify_sources() -> None:
    for source_id, (path, expected_bytes, expected_hash) in SOURCE_CONTRACT.items():
        if not path.is_file():
            raise FileNotFoundError(f"Missing accepted source {source_id}: {path}")
        if path.stat().st_size != expected_bytes or sha256(path) != expected_hash:
            raise ValueError(f"Accepted source identity changed: {source_id}")
    checkpoint = json.loads((CHECKPOINT_ROOT / "checkpoint-contract.json").read_text(encoding="utf-8"))
    if (
        checkpoint["checkpoint_id"] != "oclc-app4-cp01"
        or checkpoint["version"] != "0.1.0"
        or checkpoint["commons_release"] != "0.80.0"
        or checkpoint["accepted_component_files"] != 245
        or checkpoint["accepted_immutable_rows"] != 204
        or checkpoint["thresholds"]["evidence_candidates"] != list(THRESHOLDS)
        or checkpoint["thresholds"]["accepted"] is not None
    ):
        raise ValueError("Checkpoint 01 handoff contract changed")


def code_set(resource: dict[str, object]) -> set[str]:
    code = resource.get("code", {})
    if not isinstance(code, dict):
        return set()
    coding = code.get("coding", [])
    if not isinstance(coding, list):
        return set()
    return {
        str(item.get("code"))
        for item in coding
        if isinstance(item, dict) and item.get("code") is not None
    }


def patient_reference(resource: dict[str, object]) -> str:
    subject = resource.get("subject", {})
    if not isinstance(subject, dict):
        return ""
    return str(subject.get("reference", "")).split("/")[-1]


def language_group(resource: dict[str, object]) -> tuple[str, str]:
    communications = resource.get("communication", [])
    code = "unknown"
    if isinstance(communications, list) and communications:
        language = communications[0].get("language", {}) if isinstance(communications[0], dict) else {}
        codings = language.get("coding", []) if isinstance(language, dict) else []
        if isinstance(codings, list) and codings and isinstance(codings[0], dict):
            code = str(codings[0].get("code", "unknown"))
    if code in {"en", "en-US"}:
        return code, "english"
    if code.startswith("es"):
        return code, "spanish"
    return code, "other_language"


def age_on(birth_date: date, reference_date: date) -> int:
    return reference_date.year - birth_date.year - (
        (reference_date.month, reference_date.day) < (birth_date.month, birth_date.day)
    )


def build_patient_frame() -> tuple[list[dict[str, object]], dict[str, dict[str, object]]]:
    patients: dict[str, dict[str, object]] = {}
    patient_path = SOURCE_CONTRACT["module02-patient"][0]
    with gzip.open(patient_path, "rt", encoding="utf-8") as handle:
        for line in handle:
            resource = json.loads(line)
            source_id = str(resource["id"])
            birth = date.fromisoformat(str(resource["birthDate"]))
            language_code, access_group = language_group(resource)
            patients[source_id] = {
                "source_id": source_id,
                "age": age_on(birth, REFERENCE_DATE),
                "source_recorded_gender": str(resource.get("gender", "unknown")),
                "language_code": language_code,
                "language_access_group": access_group,
            }
    if len(patients) != 1000:
        raise ValueError(f"Expected 1,000 synthetic Patient rows, found {len(patients)}")

    latest_bmi: dict[str, tuple[datetime, float]] = {}
    latest_a1c: dict[str, tuple[datetime, float]] = {}
    observation_path = SOURCE_CONTRACT["module02-observation"][0]
    with gzip.open(observation_path, "rt", encoding="utf-8") as handle:
        for line in handle:
            resource = json.loads(line)
            codes = code_set(resource)
            if not ({"39156-5", "4548-4"} & codes):
                continue
            patient_id = patient_reference(resource)
            timestamp_value = resource.get("effectiveDateTime") or resource.get("issued")
            quantity = resource.get("valueQuantity", {})
            value = quantity.get("value") if isinstance(quantity, dict) else None
            if patient_id not in patients or not timestamp_value or value is None:
                continue
            timestamp = parse_timestamp(str(timestamp_value))
            target = latest_bmi if "39156-5" in codes else latest_a1c
            if patient_id not in target or timestamp > target[patient_id][0]:
                target[patient_id] = (timestamp, float(value))

    known_diabetes: set[str] = set()
    condition_path = SOURCE_CONTRACT["module02-condition"][0]
    with gzip.open(condition_path, "rt", encoding="utf-8") as handle:
        for line in handle:
            resource = json.loads(line)
            if "44054006" in code_set(resource):
                patient_id = patient_reference(resource)
                if patient_id in patients:
                    known_diabetes.add(patient_id)

    coefficients = {row["term"]: float(row["coefficient"]) for row in read_csv(SOURCE_CONTRACT["module03-model-coefficients"][0])}
    expected_terms = {"const", "age_centered_per_10", "bmi_centered_per_5", "female_indicator"}
    if set(coefficients) != expected_terms:
        raise ValueError("Module 03 coefficient contract changed")

    ordered_ids = sorted(patients, key=lambda value: hashlib.sha256(f"frame|{value}".encode()).hexdigest())
    rows: list[dict[str, object]] = []
    by_source: dict[str, dict[str, object]] = {}
    access_needs = ("none", "screen_reader", "low_vision", "motor_access", "cognitive_support")
    for index, source_id in enumerate(ordered_ids, start=1):
        source = patients[source_id]
        age = int(source["age"])
        gender = str(source["source_recorded_gender"])
        bmi_item = latest_bmi.get(source_id)
        bmi = None if bmi_item is None else bmi_item[1]
        a1c_item = latest_a1c.get(source_id)
        a1c_days = None if a1c_item is None else (REFERENCE_DATE - a1c_item[0].date()).days
        recent_a1c = a1c_days is not None and 0 <= a1c_days <= 365
        diabetes = source_id in known_diabetes
        reason = "eligible_frame"
        if not 35 <= age <= 70:
            reason = "age_outside_candidate_frame"
        elif bmi is None:
            reason = "bmi_absent_in_source"
        elif bmi < 25:
            reason = "bmi_below_candidate_frame"
        elif gender not in {"female", "male"}:
            reason = "source_gender_not_supported_by_fixed_model"
        elif diabetes:
            reason = "known_diabetes_suppression"
        elif recent_a1c:
            reason = "recent_hba1c_suppression"
        base_eligible = reason == "eligible_frame"
        score = None
        if base_eligible and bmi is not None:
            linear = (
                coefficients["const"]
                + coefficients["age_centered_per_10"] * ((age - 50) / 10)
                + coefficients["bmi_centered_per_5"] * ((bmi - 30) / 5)
                + coefficients["female_indicator"] * (1 if gender == "female" else 0)
            )
            score = 1 / (1 + math.exp(-linear))
        access_need = access_needs[min(stable_number(f"access|{source_id}") // 20, 4)]
        communication_need = "standard_english"
        if source["language_access_group"] == "spanish":
            communication_need = "qualified_spanish_language_support"
        elif source["language_access_group"] == "other_language":
            communication_need = "qualified_language_support"
        if access_need != "none":
            communication_need += f" plus {access_need} format"
        row = {
            "synthetic_patient_id": f"SP{index:04d}",
            "source_patient_sha256": hashlib.sha256(source_id.encode()).hexdigest(),
            "explicit_synthetic": "true",
            "age": age,
            "age_band": "18-34" if age < 35 else "35-44" if age < 45 else "45-54" if age < 55 else "55-64" if age < 65 else "65-70" if age <= 70 else "71+",
            "source_recorded_gender": gender,
            "language_code": source["language_code"],
            "language_access_group": source["language_access_group"],
            "scripted_disability_access_need": access_need,
            "scripted_communication_need": communication_need,
            "latest_bmi": fmt(bmi, 4),
            "bmi_band": "missing" if bmi is None else "below_25" if bmi < 25 else "25.0-29.9" if bmi < 30 else "30.0-34.9" if bmi < 35 else "35.0-39.9" if bmi < 40 else "40.0+",
            "known_diabetes_suppression": str(diabetes).lower(),
            "recent_hba1c_suppression": str(recent_a1c).lower(),
            "candidate_frame_status": "eligible" if base_eligible else "not_eligible",
            "candidate_frame_reason": reason,
            "offline_teaching_score": fmt(score),
            "score_status": "offline synthetic teaching score" if score is not None else "not_calculated",
            "claim_limit": "synthetic workflow frame only; not a patient record, local prevalence estimate, clinical score, or threshold decision",
        }
        rows.append(row)
        by_source[source_id] = row
    return rows, by_source


def weekday_dates(start: date, count: int) -> list[date]:
    result: list[date] = []
    current = start
    while len(result) < count:
        if current.weekday() < 5:
            result.append(current)
        current += timedelta(days=1)
    return result


def scripted_interaction(encounter_id: str) -> tuple[str, str, str, str]:
    bucket = stable_number(f"interaction|{encounter_id}")
    response = 20 + stable_number(f"response|{encounter_id}", 281)
    if bucket < 35:
        return "acknowledgment", "true", str(response), "3.0"
    if bucket < 60:
        return "dismissal", "true", str(response), "1.0"
    if bucket < 80:
        return "deferment", "true", str(response), "2.0"
    if bucket < 90:
        return "view_only", "true", str(response), "1.0"
    return "unresolved", "false", "", "0.5"


def build_encounters(patient_rows: list[dict[str, object]], by_source: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    source_by_synthetic = {row["synthetic_patient_id"]: source_id for source_id, row in by_source.items()}
    synthetic_ids = list(source_by_synthetic)
    primary = sorted(synthetic_ids, key=lambda value: hashlib.sha256(f"primary|{value}".encode()).hexdigest())
    repeats = sorted(synthetic_ids, key=lambda value: hashlib.sha256(f"repeat|{value}".encode()).hexdigest())[:REPEAT_PATIENTS]
    opportunities = [(patient_id, 1) for patient_id in primary] + [(patient_id, 2) for patient_id in repeats]
    if len(opportunities) != SESSIONS * ENCOUNTERS_PER_SESSION:
        raise ValueError("Synthetic schedule dimensions changed")
    patient_by_synthetic = {str(row["synthetic_patient_id"]): row for row in patient_rows}
    dates = weekday_dates(date(2026, 9, 1), 24)
    session_starts = (time(8, 0), time(9, 30), time(11, 0), time(13, 30), time(15, 0))
    rows: list[dict[str, object]] = []
    for index, (patient_id, occurrence) in enumerate(opportunities, start=1):
        session_index = (index - 1) // ENCOUNTERS_PER_SESSION
        within_session = (index - 1) % ENCOUNTERS_PER_SESSION
        session_id = f"WF-S{session_index + 1:03d}"
        day_value = dates[session_index // len(session_starts)]
        start_time = session_starts[session_index % len(session_starts)]
        decision = datetime.combine(day_value, start_time, tzinfo=timezone.utc) + timedelta(minutes=7 * within_session)
        patient = patient_by_synthetic[patient_id]
        input_bucket = stable_number(f"input|{patient_id}|{occurrence}")
        input_state = "ready" if input_bucket < 90 else "missing" if input_bucket < 94 else "stale" if input_bucket < 98 else "inconsistent"
        base_eligible = patient["candidate_frame_status"] == "eligible"
        interaction, viewed, response_seconds, task_minutes = scripted_interaction(f"WF-E{index:04d}")
        row = {
            "encounter_opportunity_id": f"WF-E{index:04d}",
            "synthetic_patient_id": patient_id,
            "explicit_synthetic": "true",
            "visit_occurrence": occurrence,
            "session_id": session_id,
            "clinician_id": f"CL{session_index % CLINICIANS + 1:02d}",
            "decision_time": decision.isoformat(),
            "candidate_frame_status": patient["candidate_frame_status"],
            "candidate_frame_reason": patient["candidate_frame_reason"],
            "input_state": input_state if base_eligible else "not_evaluated",
            "offline_teaching_score": patient["offline_teaching_score"] if base_eligible and input_state == "ready" else "",
            "scripted_competing_alerts_in_session": 6 + stable_number(f"competing|{session_id}", 13),
            "scripted_interaction_if_card": interaction,
            "scripted_view_if_card": viewed,
            "scripted_response_seconds_if_resolved": response_seconds,
            "scripted_task_minutes_if_card": task_minutes,
            "source_recorded_gender": patient["source_recorded_gender"],
            "age_band": patient["age_band"],
            "bmi_band": patient["bmi_band"],
            "language_access_group": patient["language_access_group"],
            "scripted_disability_access_need": patient["scripted_disability_access_need"],
            "scripted_communication_need": patient["scripted_communication_need"],
            "claim_limit": "scripted synthetic opportunity only; not an encounter, observed workload, clinician behavior, or clinical result",
        }
        rows.append(row)
    return rows


def build_candidate_events(encounters: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for threshold in THRESHOLDS:
        seen_patients: set[str] = set()
        threshold_text = fmt(threshold)
        for encounter in encounters:
            result = "no_card"
            reason = str(encounter["candidate_frame_reason"])
            score_value = encounter["offline_teaching_score"]
            if encounter["candidate_frame_status"] == "eligible":
                if encounter["input_state"] != "ready":
                    reason = f"input_{encounter['input_state']}"
                elif score_value and float(str(score_value)) >= threshold:
                    result = "candidate_card"
                    reason = "at_or_above_unaccepted_evidence_candidate"
                else:
                    reason = "below_unaccepted_evidence_candidate"
            patient_id = str(encounter["synthetic_patient_id"])
            repeat_card = result == "candidate_card" and patient_id in seen_patients
            if result == "candidate_card":
                seen_patients.add(patient_id)
            interaction = str(encounter["scripted_interaction_if_card"]) if result == "candidate_card" else "not_applicable"
            rows.append({
                "candidate_event_id": f"T{str(threshold).replace('.', '')}-{encounter['encounter_opportunity_id']}",
                "encounter_opportunity_id": encounter["encounter_opportunity_id"],
                "synthetic_patient_id": patient_id,
                "session_id": encounter["session_id"],
                "clinician_id": encounter["clinician_id"],
                "threshold": threshold_text,
                "threshold_status": "evidence candidate, not selected or accepted",
                "rule_result": result,
                "reason": reason,
                "repeat_candidate_card": str(repeat_card).lower(),
                "scripted_interaction": interaction,
                "scripted_viewed": encounter["scripted_view_if_card"] if result == "candidate_card" else "false",
                "scripted_response_seconds": encounter["scripted_response_seconds_if_resolved"] if result == "candidate_card" else "",
                "scripted_task_minutes": encounter["scripted_task_minutes_if_card"] if result == "candidate_card" else "0.0",
                "claim_limit": "offline synthetic comparison only; not an alert, observed response, threshold acceptance, or clinical recommendation",
            })
    return rows


def threshold_evidence() -> tuple[dict[str, dict[str, str]], dict[str, str]]:
    audit = {
        row["threshold"]: row
        for row in read_csv(SOURCE_CONTRACT["module03-threshold-audit"][0])
        if row["partition"] == "temporal_holdout" and row["threshold"] in {fmt(value) for value in THRESHOLDS}
    }
    if set(audit) != {fmt(value) for value in THRESHOLDS}:
        raise ValueError("All six temporal-holdout evidence candidates are required")
    rejected = [
        row for row in read_csv(SOURCE_CONTRACT["module03-threshold-audit"][0])
        if row["partition"] == "temporal_holdout" and row["threshold"] == "0.20000000"
    ]
    if len(rejected) != 1 or rejected[0]["threshold_status"] != "rejected Module 02 mechanics fixture":
        raise ValueError("The rejected 0.20 mechanics fixture changed")
    performance = [
        row for row in read_csv(SOURCE_CONTRACT["module03-performance"][0])
        if row["partition"] == "temporal_holdout" and row["model"] == "transparent_weighted_logit"
    ]
    if len(performance) != 1:
        raise ValueError("Temporal-holdout performance identity changed")
    return audit, performance[0]


def build_aggregates(encounters: list[dict[str, object]], candidate_events: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    events_by_threshold: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in candidate_events:
        events_by_threshold[str(row["threshold"])].append(row)
    encounter_by_id = {str(row["encounter_opportunity_id"]): row for row in encounters}
    evidence, temporal_performance = threshold_evidence()
    eligible = [row for row in encounters if row["candidate_frame_status"] == "eligible"]
    unavailable = [row for row in eligible if row["input_state"] != "ready"]
    burden_rows: list[dict[str, object]] = []
    design_rows: list[dict[str, object]] = []
    session_rows: list[dict[str, object]] = []
    equity_rows: list[dict[str, object]] = []
    dimension_fields = (
        ("age_band", "age_band"),
        ("source_recorded_gender", "source_recorded_gender"),
        ("language_access", "language_access_group"),
        ("disability_access", "scripted_disability_access_need"),
        ("bmi_band", "bmi_band"),
    )

    for threshold in THRESHOLDS:
        threshold_text = fmt(threshold)
        events = events_by_threshold[threshold_text]
        cards = [row for row in events if row["rule_result"] == "candidate_card"]
        interactions = Counter(str(row["scripted_interaction"]) for row in cards)
        response_seconds = [int(str(row["scripted_response_seconds"])) for row in cards if row["scripted_response_seconds"] != ""]
        sessions_with_cards = {str(row["session_id"]) for row in cards}
        repeats = sum(row["repeat_candidate_card"] == "true" for row in cards)
        burden = {
            "threshold": threshold_text,
            "threshold_status": "evidence candidate, not selected or accepted",
            "encounter_opportunities": len(encounters),
            "candidate_frame_encounters": len(eligible),
            "input_unavailable_encounters": len(unavailable),
            "ready_candidate_frame_encounters": len(eligible) - len(unavailable),
            "candidate_cards": len(cards),
            "cards_per_session": fmt(len(cards) / SESSIONS, 4),
            "sessions_with_cards": len(sessions_with_cards),
            "repeat_cards": repeats,
            "scripted_views": sum(row["scripted_viewed"] == "true" for row in cards),
            "scripted_acknowledgments": interactions["acknowledgment"],
            "scripted_dismissals": interactions["dismissal"],
            "scripted_deferments": interactions["deferment"],
            "scripted_view_only": interactions["view_only"],
            "scripted_unresolved": interactions["unresolved"],
            "scripted_median_response_seconds": fmt(statistics.median(response_seconds) if response_seconds else None, 2),
            "scripted_task_minutes": fmt(sum(float(str(row["scripted_task_minutes"])) for row in cards), 2),
            "claim_limit": "synthetic burden script only; no local workload, behavior, fatigue, misuse, care-quality, or threshold claim",
        }
        burden_rows.append(burden)

        for modality, design_name in (("interruptive_banner", "interruptive candidate banner"), ("passive_context_panel", "less interruptive passive contextual panel")):
            design_rows.append({
                "design_id": f"{'banner' if modality == 'interruptive_banner' else 'panel'}-t{str(threshold).replace('.', '')}",
                "design": design_name,
                "threshold": threshold_text,
                "threshold_status": "evidence candidate, not selected or accepted",
                "candidate_cards": len(cards),
                "interruption_events": len(cards) if modality == "interruptive_banner" else 0,
                "cards_per_session": burden["cards_per_session"],
                "sessions_with_cards": len(sessions_with_cards),
                "repeat_cards": repeats,
                "input_unavailable_encounters": len(unavailable),
                "scripted_task_minutes": burden["scripted_task_minutes"],
                "temporal_holdout_weighted_flags_per_1000": evidence[threshold_text]["weighted_flags_per_1000"],
                "temporal_holdout_weighted_missed_per_1000": evidence[threshold_text]["weighted_missed_per_1000"],
                "sandbox_case_sufficiency": "at least 10 scripted positive cases" if len(cards) >= 10 else "fewer than 10 scripted positive cases",
                "design_status": "comparison only, not selected by generated evidence",
                "claim_limit": "historical NHANES consequences and synthetic workflow counts are separate; no local utility or clinical authority",
            })

        by_session: dict[str, list[dict[str, object]]] = defaultdict(list)
        for event in events:
            by_session[str(event["session_id"])].append(event)
        for session_id in sorted(by_session):
            session_events = by_session[session_id]
            session_cards = [row for row in session_events if row["rule_result"] == "candidate_card"]
            encounter = encounter_by_id[str(session_events[0]["encounter_opportunity_id"])]
            session_rows.append({
                "threshold": threshold_text,
                "session_id": session_id,
                "clinician_id": encounter["clinician_id"],
                "encounters": len(session_events),
                "candidate_frame_encounters": sum(encounter_by_id[str(row["encounter_opportunity_id"])]["candidate_frame_status"] == "eligible" for row in session_events),
                "input_unavailable_encounters": sum(str(row["reason"]).startswith("input_") for row in session_events),
                "candidate_cards": len(session_cards),
                "repeat_cards": sum(row["repeat_candidate_card"] == "true" for row in session_cards),
                "scripted_competing_alerts": encounter["scripted_competing_alerts_in_session"],
                "scripted_task_minutes": fmt(sum(float(str(row["scripted_task_minutes"])) for row in session_cards), 2),
                "claim_limit": "scripted session only; not a staffing, capacity, fatigue, or workload estimate",
            })

        for dimension, field in dimension_fields:
            groups: dict[str, list[dict[str, object]]] = defaultdict(list)
            for encounter in eligible:
                groups[str(encounter[field])].append(encounter)
            card_ids = {str(row["encounter_opportunity_id"]) for row in cards}
            for group in sorted(groups):
                group_rows = groups[group]
                ready = [row for row in group_rows if row["input_state"] == "ready"]
                flagged = sum(str(row["encounter_opportunity_id"]) in card_ids for row in ready)
                supported = len(ready) >= 30 and flagged >= 10
                unavailable_count = len(group_rows) - len(ready)
                equity_rows.append({
                    "threshold": threshold_text,
                    "dimension": dimension,
                    "group": group,
                    "candidate_frame_encounters": len(group_rows),
                    "ready_encounters": len(ready),
                    "input_unavailable_encounters": unavailable_count,
                    "input_unavailable_rate": fmt(unavailable_count / len(group_rows), 6) if len(group_rows) >= 30 else "",
                    "candidate_cards": flagged,
                    "candidate_card_rate": fmt(flagged / len(ready), 6) if supported else "",
                    "support_status": "report synthetic comparison with boundary" if supported else "suppress candidate-card rate: support rule not met",
                    "interpretation": "scripted access and reach audit; no fairness conclusion or group-specific action",
                    "claim_limit": "synthetic repeated-encounter slice; not population prevalence, disparity proof, fairness certification, or targeting authority",
                })

    design_rows.append({
        "design_id": "no-alert",
        "design": "no alert",
        "threshold": "",
        "threshold_status": "not applicable",
        "candidate_cards": 0,
        "interruption_events": 0,
        "cards_per_session": "0.0000",
        "sessions_with_cards": 0,
        "repeat_cards": 0,
        "input_unavailable_encounters": len(unavailable),
        "scripted_task_minutes": "0.00",
        "temporal_holdout_weighted_flags_per_1000": "0.00000000",
        "temporal_holdout_weighted_missed_per_1000": fmt(float(temporal_performance["weighted_prevalence"]) * 1000),
        "sandbox_case_sufficiency": "no positive card cases by design",
        "design_status": "comparison only, not selected by generated evidence",
        "claim_limit": "no alert avoids card burden but cannot be interpreted as safe, preferred, or equivalent care",
    })
    return burden_rows, design_rows, session_rows, equity_rows


def build_profile(patient_rows: list[dict[str, object]], encounters: list[dict[str, object]], candidate_events: list[dict[str, object]], design_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    eligible_people = [row for row in patient_rows if row["candidate_frame_status"] == "eligible"]
    eligible_encounters = [row for row in encounters if row["candidate_frame_status"] == "eligible"]
    values = (
        ("synthetic_people", len(patient_rows), "one committed Synthea Patient row"),
        ("candidate_frame_people", len(eligible_people), "age, BMI, diabetes, and recent-HbA1c teaching frame"),
        ("encounter_opportunities", len(encounters), "scripted fictional service opportunities"),
        ("repeat_encounter_opportunities", sum(int(row["visit_occurrence"]) == 2 for row in encounters), "second scripted visits"),
        ("clinician_sessions", SESSIONS, "scripted sessions"),
        ("fictional_clinicians", CLINICIANS, "scripted clinician identifiers"),
        ("candidate_frame_encounters", len(eligible_encounters), "eligible before scripted input state"),
        ("unavailable_candidate_inputs", sum(row["input_state"] != "ready" for row in eligible_encounters), "missing, stale, or inconsistent scripted states"),
        ("candidate_event_rows", len(candidate_events), "six evidence candidates times every encounter opportunity"),
        ("design_rows", len(design_rows), "six banner, six passive-panel, and one no-alert comparison"),
    )
    return [
        {
            "measure": measure,
            "value": value,
            "definition": definition,
            "status": "synthetic teaching evidence",
            "claim_limit": "not local prevalence, workflow, workload, behavior, utility, safety, or deployment evidence",
        }
        for measure, value, definition in values
    ]


def invariant_rows(patient_rows: list[dict[str, object]], encounters: list[dict[str, object]], candidate_events: list[dict[str, object]], burden_rows: list[dict[str, object]], design_rows: list[dict[str, object]], session_rows: list[dict[str, object]], equity_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    flags = [int(row["candidate_cards"]) for row in burden_rows]
    checks = (
        ("I01", len(patient_rows) == 1000, "exact synthetic Patient frame"),
        ("I02", len(encounters) == 1200, "exact encounter opportunities"),
        ("I03", sum(int(row["visit_occurrence"]) == 2 for row in encounters) == 200, "exact repeat opportunities"),
        ("I04", len({row["session_id"] for row in encounters}) == 120, "exact session count"),
        ("I05", len({row["clinician_id"] for row in encounters}) == 12, "exact fictional clinician count"),
        ("I06", len(candidate_events) == 7200, "six candidates by 1,200 opportunities"),
        ("I07", {row["threshold"] for row in candidate_events} == {fmt(value) for value in THRESHOLDS}, "all six evidence candidates and no other value"),
        ("I08", all(row["threshold"] != "0.20000000" for row in candidate_events), "rejected 0.20 fixture excluded"),
        ("I09", all(row["threshold_status"] == "evidence candidate, not selected or accepted" for row in candidate_events), "no threshold acceptance"),
        ("I10", flags == sorted(flags, reverse=True), "candidate counts are monotone by threshold"),
        ("I11", len(design_rows) == 13, "six banner, six passive-panel, and no-alert designs"),
        ("I12", sum(row["design_id"] == "no-alert" and int(row["candidate_cards"]) == 0 for row in design_rows) == 1, "one zero-card no-alert design"),
        ("I13", len(session_rows) == 720, "six thresholds by 120 sessions"),
        ("I14", len(equity_rows) > 0, "equity and access slices released"),
        ("I15", all(row["candidate_card_rate"] == "" for row in equity_rows if row["support_status"].startswith("suppress")), "unsupported candidate-card rates are blank"),
        ("I16", all(row["explicit_synthetic"] == "true" for row in patient_rows), "patient frame explicitly synthetic"),
        ("I17", all(row["explicit_synthetic"] == "true" for row in encounters), "encounters explicitly synthetic"),
        ("I18", all(row["offline_teaching_score"] == "" for row in encounters if row["candidate_frame_status"] == "eligible" and row["input_state"] != "ready"), "unavailable inputs never receive an encounter score"),
        ("I19", any(row["scripted_interaction"] == "dismissal" for row in candidate_events), "dismissal script present without motive inference"),
        ("I20", all("not an alert" in row["claim_limit"] for row in candidate_events), "every candidate event denies alert authority"),
    )
    return [
        {"invariant_id": invariant_id, "status": "pass" if passed else "fail", "check": check}
        for invariant_id, passed, check in checks
    ]


def build(target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_sources()
    target.mkdir(parents=True)
    patient_rows, by_source = build_patient_frame()
    encounter_rows = build_encounters(patient_rows, by_source)
    candidate_rows = build_candidate_events(encounter_rows)
    burden_rows, design_rows, session_rows, equity_rows = build_aggregates(encounter_rows, candidate_rows)
    profile_rows = build_profile(patient_rows, encounter_rows, candidate_rows, design_rows)
    invariants = invariant_rows(patient_rows, encounter_rows, candidate_rows, burden_rows, design_rows, session_rows, equity_rows)
    if any(row["status"] != "pass" for row in invariants):
        failed = [row["invariant_id"] for row in invariants if row["status"] != "pass"]
        raise ValueError(f"Workflow invariants failed: {', '.join(failed)}")

    write_gzip_csv(target / OUTPUT_FILES[0], tuple(patient_rows[0]), patient_rows)
    write_gzip_csv(target / OUTPUT_FILES[1], tuple(encounter_rows[0]), encounter_rows)
    write_gzip_csv(target / OUTPUT_FILES[2], tuple(candidate_rows[0]), candidate_rows)
    write_csv(target / OUTPUT_FILES[3], tuple(profile_rows[0]), profile_rows)
    write_csv(target / OUTPUT_FILES[4], tuple(burden_rows[0]), burden_rows)
    write_csv(target / OUTPUT_FILES[5], tuple(design_rows[0]), design_rows)
    write_gzip_csv(target / OUTPUT_FILES[6], tuple(session_rows[0]), session_rows)
    write_csv(target / OUTPUT_FILES[7], tuple(equity_rows[0]), equity_rows)
    write_csv(target / OUTPUT_FILES[8], tuple(invariants[0]), invariants)

    output_manifest = [
        {
            "relative_path": relative,
            "bytes": (target / relative).stat().st_size,
            "sha256": sha256(target / relative),
        }
        for relative in OUTPUT_FILES[:-1]
    ]
    report = {
        "schema_version": "1.0.0",
        "release_id": "APP4-M04-SYNTHETIC-WORKFLOW-2026-08-31-v1",
        "status": "scripted synthetic workflow teaching evidence only",
        "generator": "APP-4 Module 04 Python standard-library builder 0.1.0",
        "source_contract": {
            source_id: {"bytes": details[1], "sha256": details[2]}
            for source_id, details in SOURCE_CONTRACT.items()
        },
        "workflow": {
            "synthetic_people": len(patient_rows),
            "candidate_frame_people": sum(row["candidate_frame_status"] == "eligible" for row in patient_rows),
            "encounter_opportunities": len(encounter_rows),
            "repeat_opportunities": sum(int(row["visit_occurrence"]) == 2 for row in encounter_rows),
            "candidate_frame_encounters": sum(row["candidate_frame_status"] == "eligible" for row in encounter_rows),
            "input_unavailable_encounters": sum(row["candidate_frame_status"] == "eligible" and row["input_state"] != "ready" for row in encounter_rows),
            "sessions": SESSIONS,
            "fictional_clinicians": CLINICIANS,
        },
        "candidate_thresholds": [fmt(value) for value in THRESHOLDS],
        "accepted_threshold": None,
        "module02_mock_threshold": {"value": "0.20000000", "status": "rejected mechanics fixture; excluded from Module 04 evidence"},
        "candidate_cards": {row["threshold"]: int(row["candidate_cards"]) for row in burden_rows},
        "designs": {"interruptive_banner": 6, "passive_context_panel": 6, "no_alert": 1},
        "human_design_selection": None,
        "output_manifest": output_manifest,
        "authority": {
            "real_patient_scoring": "prohibited",
            "clinical_threshold_acceptance": "prohibited",
            "clinical_alerting": "prohibited",
            "clinical_action": "prohibited",
            "implementation": "prohibited",
            "production_connection": "prohibited",
            "deployment": "prohibited",
        },
        "claim_limit": "NHANES evidence and synthetic workflow counts remain separate; this release does not establish local workflow, burden, behavior, utility, safety, equity, or clinical authority",
    }
    (target / OUTPUT_FILES[-1]).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return verify(target)


def verify(target: Path) -> dict[str, object]:
    missing = [relative for relative in OUTPUT_FILES if not (target / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Workflow release missing: {', '.join(missing)}")
    report = json.loads((target / "build-report.json").read_text(encoding="utf-8"))
    patient_rows = read_gzip_csv(target / OUTPUT_FILES[0])
    encounter_rows = read_gzip_csv(target / OUTPUT_FILES[1])
    candidate_rows = read_gzip_csv(target / OUTPUT_FILES[2])
    design_rows = read_csv(target / OUTPUT_FILES[5])
    session_rows = read_gzip_csv(target / OUTPUT_FILES[6])
    equity_rows = read_csv(target / OUTPUT_FILES[7])
    invariants = read_csv(target / OUTPUT_FILES[8])
    if (
        len(patient_rows) != 1000
        or len(encounter_rows) != 1200
        or len(candidate_rows) != 7200
        or len(design_rows) != 13
        or len(session_rows) != 720
        or not equity_rows
        or len(invariants) != 20
        or any(row["status"] != "pass" for row in invariants)
        or report["candidate_thresholds"] != [fmt(value) for value in THRESHOLDS]
        or report["accepted_threshold"] is not None
        or report["human_design_selection"] is not None
    ):
        raise ValueError("Workflow release contract failed")
    for item in report["output_manifest"]:
        path = target / item["relative_path"]
        if path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
            raise ValueError(f"Workflow output identity changed: {item['relative_path']}")
    return {
        "status": "pass",
        "patient_rows": len(patient_rows),
        "encounter_rows": len(encounter_rows),
        "candidate_rows": len(candidate_rows),
        "design_rows": len(design_rows),
        "session_rows": len(session_rows),
        "equity_rows": len(equity_rows),
        "candidate_cards": report["candidate_cards"],
        "output_manifest_sha256": hashlib.sha256(
            json.dumps(report["output_manifest"], sort_keys=True).encode("utf-8")
        ).hexdigest(),
    }


def publish() -> dict[str, object]:
    existing = [relative for relative in OUTPUT_FILES if (MODULE_ROOT / relative).exists()]
    if existing:
        raise FileExistsError(f"Refusing to replace package outputs: {', '.join(existing)}")
    with tempfile.TemporaryDirectory(prefix="app4-module04-publish-") as temporary:
        built = Path(temporary) / "release"
        result = build(built)
        for relative in OUTPUT_FILES:
            destination = MODULE_ROOT / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(built / relative, destination)
    return result


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module04-workflow-") as temporary:
        base = Path(temporary)
        first, second = base / "first", base / "second"
        one = build(first)
        two = build(second)
        if one != two:
            raise AssertionError("Workflow builds are not deterministic")
        first_hashes = {relative: sha256(first / relative) for relative in OUTPUT_FILES}
        second_hashes = {relative: sha256(second / relative) for relative in OUTPUT_FILES}
        if first_hashes != second_hashes:
            raise AssertionError("Workflow output bytes changed between builds")
        try:
            build(first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Workflow builder overwrote an existing target")
    print(
        "APP-4 Module 04 workflow builder self-check passed: "
        f"{one['patient_rows']} people, {one['encounter_rows']} opportunities, "
        f"{one['candidate_rows']} candidate rows, and {one['design_rows']} designs."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    selected = sum(bool(value) for value in (args.target, args.publish, args.verify, args.self_check))
    if selected != 1:
        parser.error("choose exactly one of --target, --publish, --verify, or --self-check")
    try:
        if args.target:
            result = build(args.target)
        elif args.publish:
            result = publish()
        elif args.verify:
            result = verify(args.verify)
        else:
            self_check()
            return
        print(json.dumps(result, indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
