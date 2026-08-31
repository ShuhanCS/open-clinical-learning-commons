"""Build the APP-4 Module 05 local teaching sandbox release."""

from __future__ import annotations

import argparse
import copy
import csv
import gzip
import hashlib
import io
import json
import shutil
import tempfile
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
UPSTREAM_ROOT = MODULE_ROOT.parent / "04-alert-burden-human-factors-equity"
THRESHOLD = Decimal("0.03000000")
THRESHOLD_TEXT = "0.03000000"
MODEL_VERSION = "APP4-M03-LOGIT-2026-08-31-v1"
HOOK_VERSION = "1.0"
LATENCY_BUDGET_MS = 2000
CLAIM_LIMIT = (
    "local synthetic teaching sandbox only; not FHIR or CDS Hooks conformance, clinical evidence, "
    "a clinical alert, threshold acceptance, implementation, or deployment"
)
SOURCE_CONTRACT = {
    "module04-release": (
        "release.json",
        2522,
        "2ef40e8ff78976f2689c81e4b0b79af9efeb5c3496d4c888315a448ef9ecf4b3",
    ),
    "module04-decision-contract": (
        "decision-contract.json",
        2804,
        "6ddb5f565744715897a12d8798f06bbe74d038aa5631ae0b4f888536886624a3",
    ),
    "module04-build-report": (
        "build-report.json",
        4536,
        "02944e755b2f3ded279f02f655cd3be4f57a4fe89db21df663d02afeb9ed90f2",
    ),
    "module04-patient-frame": (
        "data/workflow/patient-frame.csv.gz",
        54854,
        "bfa374fa13c683a5bcc6915c776282b22c98015623db8c1b30562018dd3e7b2d",
    ),
    "module04-encounters": (
        "data/workflow/encounter-opportunities.csv.gz",
        25394,
        "b71bd822a8bb0d1b1c87430213fcf6e09e056b80ab18366812cbca65e08b4f87",
    ),
    "module04-candidate-events": (
        "data/workflow/candidate-events.csv.gz",
        82953,
        "278a9c74294c5ad13b38ade0215a88c8e4af37e7bc5e8d2e7fcc297d781a929f",
    ),
}
OUTPUT_FILES = (
    "data/sandbox/requests.ndjson.gz",
    "data/sandbox/prefetch-resources.ndjson.gz",
    "data/sandbox/responses.ndjson.gz",
    "outputs/trace-events.csv.gz",
    "outputs/test-matrix.csv",
    "outputs/test-results.csv",
    "outputs/visibility-audit.csv",
    "outputs/accessibility-checks.csv",
    "outputs/invariant-checks.csv",
    "build-report.json",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_gzip_csv(path: Path) -> list[dict[str, str]]:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_gzip_csv(path: Path, fieldnames: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    text = io.StringIO(newline="")
    writer = csv.DictWriter(text, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    write_gzip_bytes(path, text.getvalue().encode("utf-8"))


def write_gzip_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            compressed.write(payload)


def write_jsonl_gzip(path: Path, rows: list[dict[str, object]]) -> None:
    payload = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    ).encode("utf-8")
    write_gzip_bytes(path, payload)


def read_jsonl_gzip(path: Path) -> list[dict[str, object]]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def verify_sources() -> None:
    for source_id, (relative, expected_bytes, expected_hash) in SOURCE_CONTRACT.items():
        path = UPSTREAM_ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(f"Missing accepted Module 04 source: {relative}")
        if path.stat().st_size != expected_bytes or sha256(path) != expected_hash:
            raise ValueError(f"Accepted Module 04 source changed: {source_id}")
    release = json.loads((UPSTREAM_ROOT / "release.json").read_text(encoding="utf-8"))
    contract = json.loads((UPSTREAM_ROOT / "decision-contract.json").read_text(encoding="utf-8"))
    report = json.loads((UPSTREAM_ROOT / "build-report.json").read_text(encoding="utf-8"))
    if (
        release["module"]["id"] != "oclc-app4-04"
        or release["module"]["version"] != "0.1.0"
        or release["module"]["commons_release"] != "0.81.0"
        or release["workspace"]["immutable_manifest_rows"] != 285
        or release["workspace"]["assembled_files"] != 302
        or release["reference_decision"]["sandbox_design"] != "panel-t003"
        or release["reference_decision"]["accepted_threshold"] is not None
        or release["reference_decision"]["module05_permission"]
        != "permitted for nonproduction sandbox construction"
        or contract["progression"]["module05_permission"]
        != "permitted for nonproduction sandbox construction"
        or report["candidate_cards"][THRESHOLD_TEXT] != 12
    ):
        raise ValueError("Module 04 handoff contract changed")


def fhir_patient(row: dict[str, str]) -> dict[str, object]:
    return {
        "resourceType": "Patient",
        "id": row["synthetic_patient_id"],
        "meta": {"tag": [{"system": "https://openclinicallearningcommons.org/tags", "code": "synthetic"}]},
        "gender": row["source_recorded_gender"] if row["source_recorded_gender"] in {"male", "female", "other", "unknown"} else "unknown",
        "communication": [{"language": {"coding": [{"system": "urn:ietf:bcp:47", "code": row["language_code"]}]}}],
    }


def fhir_encounter(row: dict[str, str]) -> dict[str, object]:
    return {
        "resourceType": "Encounter",
        "id": row["encounter_opportunity_id"],
        "status": "in-progress",
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode", "code": "AMB"},
        "subject": {"reference": f"Patient/{row['synthetic_patient_id']}"},
        "period": {"start": row["decision_time"]},
    }


def fhir_bmi(patient_id: str, bmi: str, effective: str) -> dict[str, object]:
    return {
        "resourceType": "Observation",
        "id": f"BMI-{patient_id}",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "39156-5", "display": "Body mass index"}]},
        "subject": {"reference": f"Patient/{patient_id}"},
        "effectiveDateTime": effective,
        "valueQuantity": {"value": float(bmi), "unit": "kg/m2", "system": "http://unitsofmeasure.org", "code": "kg/m2"},
    }


def fhir_prediction(patient_id: str, score: str) -> dict[str, object]:
    return {
        "resourceType": "Parameters",
        "id": f"PRED-{patient_id}",
        "parameter": [
            {"name": "modelVersion", "valueString": MODEL_VERSION},
            {"name": "offlineTeachingScore", "valueDecimal": float(score)},
            {"name": "thresholdFixture", "valueDecimal": float(THRESHOLD_TEXT)},
            {"name": "thresholdStatus", "valueString": "unaccepted sandbox fixture"},
        ],
    }


def empty_bundle(bundle_id: str) -> dict[str, object]:
    return {"resourceType": "Bundle", "id": bundle_id, "type": "collection", "entry": []}


def expected(
    outcome: str,
    *,
    http_status: int = 200,
    response: bool = True,
    terminal_trace: bool = True,
    notice: bool = False,
    accessibility: str = "pass",
) -> dict[str, object]:
    return {
        "outcome": outcome,
        "httpStatus": http_status,
        "responsePresent": response,
        "terminalTracePresent": terminal_trace,
        "humanNoticePresent": notice,
        "accessibility": accessibility,
    }


def make_case(
    case_id: str,
    category: str,
    event: dict[str, str],
    encounter: dict[str, str],
    patient: dict[str, str],
    expected_result: dict[str, object],
    fixture_origin: str,
) -> dict[str, object]:
    score = encounter["offline_teaching_score"] or THRESHOLD_TEXT
    decision = datetime.fromisoformat(encounter["decision_time"])
    bmi_effective = decision.replace(year=decision.year - 1).isoformat()
    request_id = f"M05-REQ-{case_id}"
    prefetch = {
        "patient": fhir_patient(patient),
        "encounter": fhir_encounter(encounter),
        "bmi": fhir_bmi(patient["synthetic_patient_id"], patient["latest_bmi"], bmi_effective),
        "conditions": empty_bundle(f"COND-{case_id}"),
        "hba1c": empty_bundle(f"A1C-{case_id}"),
        "prediction": fhir_prediction(patient["synthetic_patient_id"], score),
    }
    return {
        "caseId": case_id,
        "category": category,
        "fixtureOrigin": fixture_origin,
        "serviceId": "CGH-GIM-01",
        "hookVersion": HOOK_VERSION,
        "expected": expected_result,
        "request": {
            "hookInstance": request_id,
            "hook": "patient-view",
            "context": {
                "patientId": patient["synthetic_patient_id"],
                "encounterId": encounter["encounter_opportunity_id"],
                "userId": f"PractitionerRole/{encounter['clinician_id']}",
                "decisionTime": encounter["decision_time"],
                "sessionId": encounter["session_id"],
                "repeatCandidateCard": event["repeat_candidate_card"] == "true",
                "explicitSynthetic": True,
                "faultMode": "none",
                "inputDelayMs": 0,
                "responseDelayMs": 0,
                "serviceAvailable": True,
            },
            "prefetch": prefetch,
        },
        "claimLimit": CLAIM_LIMIT,
    }


def clone_case(base: dict[str, object], case_id: str, category: str, result: dict[str, object]) -> dict[str, object]:
    case = copy.deepcopy(base)
    case["caseId"] = case_id
    case["category"] = category
    case["fixtureOrigin"] = f"seeded synthetic mutation of {base['caseId']}"
    case["expected"] = result
    request = case["request"]
    assert isinstance(request, dict)
    request["hookInstance"] = f"M05-REQ-{case_id}"
    context = request["context"]
    assert isinstance(context, dict)
    context["faultMode"] = "none"
    return case


def parameter(resource: dict[str, object], name: str) -> dict[str, object] | None:
    for item in resource.get("parameter", []):
        if isinstance(item, dict) and item.get("name") == name:
            return item
    return None


def build_cases() -> list[dict[str, object]]:
    patients = {row["synthetic_patient_id"]: row for row in read_gzip_csv(UPSTREAM_ROOT / "data/workflow/patient-frame.csv.gz")}
    encounters = {row["encounter_opportunity_id"]: row for row in read_gzip_csv(UPSTREAM_ROOT / "data/workflow/encounter-opportunities.csv.gz")}
    events = read_gzip_csv(UPSTREAM_ROOT / "data/workflow/candidate-events.csv.gz")
    threshold_events = [row for row in events if row["threshold"] == THRESHOLD_TEXT]
    positives = [row for row in threshold_events if row["rule_result"] == "candidate_card"]
    if len(positives) != 12 or sum(row["repeat_candidate_card"] == "true" for row in positives) != 1:
        raise ValueError("Module 04 positive fixture set changed")
    cases: list[dict[str, object]] = []
    for index, event in enumerate(positives, start=1):
        case_id = f"M05-P{index:02d}"
        outcome = "repeat_candidate_panel" if event["repeat_candidate_card"] == "true" else "candidate_panel"
        encounter = encounters[event["encounter_opportunity_id"]]
        cases.append(make_case(
            case_id,
            "repeat positive" if outcome.startswith("repeat") else "normal positive",
            event,
            encounter,
            patients[event["synthetic_patient_id"]],
            expected(outcome),
            f"Module 04 {event['candidate_event_id']}",
        ))

    negative_event = next(
        row for row in threshold_events
        if row["reason"] == "below_unaccepted_evidence_candidate"
        and encounters[row["encounter_opportunity_id"]]["input_state"] == "ready"
    )
    negative_encounter = encounters[negative_event["encounter_opportunity_id"]]
    negative = make_case(
        "M05-N01",
        "normal negative",
        negative_event,
        negative_encounter,
        patients[negative_event["synthetic_patient_id"]],
        expected("no_card_below_fixture", accessibility="not_applicable"),
        f"Module 04 {negative_event['candidate_event_id']}",
    )
    cases.append(negative)
    base = cases[0]

    boundary = clone_case(base, "M05-B01", "threshold boundary", expected("candidate_panel_boundary"))
    prediction = boundary["request"]["prefetch"]["prediction"]
    assert isinstance(prediction, dict)
    score = parameter(prediction, "offlineTeachingScore")
    assert score is not None
    score["valueDecimal"] = float(THRESHOLD_TEXT)
    cases.append(boundary)

    missing = clone_case(base, "M05-F01", "missing input", expected("visible_input_missing", notice=True))
    missing["request"]["prefetch"].pop("bmi")
    cases.append(missing)

    stale = clone_case(base, "M05-F02", "stale input", expected("visible_input_stale", notice=True))
    stale["request"]["prefetch"]["bmi"]["effectiveDateTime"] = "2024-01-01T00:00:00+00:00"
    cases.append(stale)

    inconsistent = clone_case(base, "M05-F03", "inconsistent input", expected("visible_input_inconsistent", notice=True))
    inconsistent["request"]["prefetch"]["bmi"]["valueQuantity"]["value"] = -1.0
    cases.append(inconsistent)

    delayed = clone_case(base, "M05-F04", "delayed input", expected("visible_input_delayed", notice=True))
    delayed["request"]["context"]["inputDelayMs"] = LATENCY_BUDGET_MS + 1
    cases.append(delayed)

    duplicate = clone_case(base, "M05-F05", "duplicate request", expected("duplicate_suppressed", accessibility="not_applicable"))
    duplicate["request"]["hookInstance"] = base["request"]["hookInstance"]
    cases.append(duplicate)

    terminology = clone_case(base, "M05-F06", "terminology mismatch", expected("visible_terminology_mismatch", notice=True))
    terminology["request"]["prefetch"]["bmi"]["code"]["coding"][0]["code"] = "LOCAL-BMI"
    cases.append(terminology)

    hook_version = clone_case(base, "M05-F07", "hook version mismatch", expected("visible_hook_version_mismatch", http_status=400, notice=True, accessibility="not_applicable"))
    hook_version["hookVersion"] = "0.9"
    cases.append(hook_version)

    unit = clone_case(base, "M05-F08", "unit mismatch", expected("visible_unit_mismatch", notice=True))
    unit["request"]["prefetch"]["bmi"]["valueQuantity"].update({"unit": "lb", "code": "[lb_av]"})
    cases.append(unit)

    unsupported = clone_case(base, "M05-F09", "unsupported service", expected("visible_unsupported_service", http_status=400, notice=True, accessibility="not_applicable"))
    unsupported["serviceId"] = "OTHER-SERVICE"
    cases.append(unsupported)

    score_missing = clone_case(base, "M05-F10", "missing score", expected("visible_score_missing", notice=True))
    score_missing["request"]["prefetch"].pop("prediction")
    cases.append(score_missing)

    diabetes = clone_case(base, "M05-F11", "known diabetes suppression", expected("known_diabetes_suppressed", accessibility="not_applicable"))
    diabetes["request"]["prefetch"]["conditions"]["entry"] = [{
        "resource": {
            "resourceType": "Condition",
            "id": "SYNTHETIC-DIABETES",
            "clinicalStatus": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/condition-clinical", "code": "active"}]},
            "code": {"coding": [{"system": "http://snomed.info/sct", "code": "44054006", "display": "Diabetes mellitus type 2"}]},
            "subject": {"reference": f"Patient/{diabetes['request']['context']['patientId']}"},
        }
    }]
    cases.append(diabetes)

    recent = clone_case(base, "M05-F12", "recent HbA1c suppression", expected("recent_hba1c_suppressed", accessibility="not_applicable"))
    recent["request"]["prefetch"]["hba1c"]["entry"] = [{
        "resource": {
            "resourceType": "Observation",
            "id": "SYNTHETIC-A1C",
            "status": "final",
            "code": {"coding": [{"system": "http://loinc.org", "code": "4548-4", "display": "Hemoglobin A1c"}]},
            "subject": {"reference": f"Patient/{recent['request']['context']['patientId']}"},
            "effectiveDateTime": recent["request"]["context"]["decisionTime"],
            "valueQuantity": {"value": 5.7, "unit": "%", "system": "http://unitsofmeasure.org", "code": "%"},
        }
    }]
    cases.append(recent)

    unavailable = clone_case(base, "M05-F13", "service unavailable", expected("visible_service_unavailable", http_status=503, notice=True, accessibility="not_applicable"))
    unavailable["request"]["context"]["serviceAvailable"] = False
    cases.append(unavailable)

    timeout = clone_case(base, "M05-F14", "response timeout", expected("visible_timeout", http_status=504, notice=True, accessibility="not_applicable"))
    timeout["request"]["context"]["responseDelayMs"] = LATENCY_BUDGET_MS + 1
    cases.append(timeout)

    silent = clone_case(
        base,
        "M05-F15",
        "silent failure",
        expected(
            "silent_failure_detected",
            http_status=0,
            response=False,
            terminal_trace=False,
            notice=False,
            accessibility="not_applicable",
        ),
    )
    silent["request"]["context"]["faultMode"] = "drop_after_receive"
    cases.append(silent)

    inaccessible = clone_case(
        base,
        "M05-F16",
        "accessibility defect",
        expected("accessibility_blocked", http_status=422, notice=True, accessibility="defect_detected"),
    )
    inaccessible["request"]["context"]["faultMode"] = "omit_summary"
    cases.append(inaccessible)

    model_version = clone_case(base, "M05-F17", "model version mismatch", expected("visible_model_version_mismatch", notice=True))
    prediction = model_version["request"]["prefetch"]["prediction"]
    assert isinstance(prediction, dict)
    version = parameter(prediction, "modelVersion")
    assert version is not None
    version["valueString"] = "UNKNOWN-MODEL"
    cases.append(model_version)

    if len(cases) != 31 or len({case["caseId"] for case in cases}) != 31:
        raise ValueError("Expected 31 unique sandbox cases")
    return cases


def operation_outcome(code: str, detail: str) -> dict[str, object]:
    return {
        "resourceType": "OperationOutcome",
        "issue": [{"severity": "error", "code": code, "details": {"text": detail}}],
    }


def source() -> dict[str, str]:
    return {"label": "Open Clinical Learning Commons synthetic teaching sandbox"}


def status_card(reason: str) -> dict[str, object]:
    return {
        "cards": [{
            "summary": "Teaching sandbox could not evaluate this case",
            "detail": f"Synthetic fixture status: {reason}. No clinical inference or action is authorized.",
            "indicator": "info",
            "source": source(),
        }]
    }


def candidate_card(case: dict[str, object], score: Decimal) -> dict[str, object]:
    repeat = bool(case["request"]["context"]["repeatCandidateCard"])
    detail = (
        f"Synthetic fixture branch at unaccepted threshold {THRESHOLD_TEXT}; offline teaching score "
        f"{score:.8f}. This passive panel is for mechanics testing only."
    )
    if repeat:
        detail += " The fixture is a repeat opportunity and requires separate trace review."
    return {
        "cards": [{
            "summary": "Teaching sandbox case: candidate branch",
            "detail": detail,
            "indicator": "info",
            "source": source(),
        }]
    }


def card_accessibility(body: dict[str, object] | None) -> tuple[str, dict[str, object]]:
    if not body or "cards" not in body or not body["cards"]:
        return "not_applicable", {
            "cards_checked": 0,
            "summary_present": "not_applicable",
            "detail_present": "not_applicable",
            "source_label_present": "not_applicable",
            "no_suggestions": "not_applicable",
            "no_external_links": "not_applicable",
        }
    cards = body["cards"]
    summary = all(bool(card.get("summary")) for card in cards)
    detail = all(bool(card.get("detail")) for card in cards)
    label = all(bool(card.get("source", {}).get("label")) for card in cards)
    suggestions = all(not card.get("suggestions") for card in cards)
    links = all(not card.get("links") for card in cards)
    passed = summary and detail and label and suggestions and links
    return ("pass" if passed else "defect_detected"), {
        "cards_checked": len(cards),
        "summary_present": str(summary).lower(),
        "detail_present": str(detail).lower(),
        "source_label_present": str(label).lower(),
        "no_suggestions": str(suggestions).lower(),
        "no_external_links": str(links).lower(),
    }


def days_between(later: str, earlier: str) -> int:
    return (datetime.fromisoformat(later) - datetime.fromisoformat(earlier)).days


def evaluate_cases(cases: list[dict[str, object]]) -> tuple[
    list[dict[str, object]],
    list[dict[str, object]],
    list[dict[str, object]],
    list[dict[str, object]],
]:
    traces: list[dict[str, object]] = []
    responses: list[dict[str, object]] = []
    accessibility: list[dict[str, object]] = []
    seen: set[str] = set()

    def trace(case_id: str, request_id: str, offset: int, event: str, branch: str, terminal: bool, visibility: str) -> None:
        traces.append({
            "case_id": case_id,
            "request_id": request_id,
            "offset_ms": offset,
            "event": event,
            "branch": branch,
            "terminal": str(terminal).lower(),
            "visibility": visibility,
            "claim_limit": CLAIM_LIMIT,
        })

    for case in cases:
        case_id = str(case["caseId"])
        request = case["request"]
        assert isinstance(request, dict)
        request_id = str(request["hookInstance"])
        context = request["context"]
        prefetch = request["prefetch"]
        assert isinstance(context, dict) and isinstance(prefetch, dict)
        trace(case_id, request_id, 0, "request_received", "request ledger", False, "sandbox audit")
        body: dict[str, object] | None = None
        http_status = 200
        notice = False
        outcome = ""
        terminal = True
        terminal_branch = ""

        if request_id in seen:
            body = {"cards": []}
            outcome = "duplicate_suppressed"
            terminal_branch = "duplicate_request"
        else:
            seen.add(request_id)
            if context["faultMode"] == "drop_after_receive":
                outcome = "silent_failure_detected"
                http_status = 0
                terminal = False
                terminal_branch = ""
            elif not context["serviceAvailable"]:
                body = operation_outcome("transient", "Synthetic service-unavailable fixture")
                outcome, http_status, notice = "visible_service_unavailable", 503, True
                terminal_branch = "service_unavailable"
            elif int(context["responseDelayMs"]) > LATENCY_BUDGET_MS:
                body = operation_outcome("timeout", "Synthetic response exceeded the teaching latency budget")
                outcome, http_status, notice = "visible_timeout", 504, True
                terminal_branch = "response_timeout"
            elif case["serviceId"] != "CGH-GIM-01":
                body = operation_outcome("not-supported", "Unsupported synthetic service")
                outcome, http_status, notice = "visible_unsupported_service", 400, True
                terminal_branch = "unsupported_service"
            elif request["hook"] != "patient-view" or case["hookVersion"] != HOOK_VERSION:
                body = operation_outcome("not-supported", "Unsupported synthetic hook or version")
                outcome, http_status, notice = "visible_hook_version_mismatch", 400, True
                terminal_branch = "hook_version_mismatch"
            elif int(context["inputDelayMs"]) > LATENCY_BUDGET_MS:
                body = status_card("required input delayed")
                outcome, notice = "visible_input_delayed", True
                terminal_branch = "required_input_delayed"
            elif "bmi" not in prefetch:
                body = status_card("required input missing")
                outcome, notice = "visible_input_missing", True
                terminal_branch = "required_input_missing"
            else:
                bmi = prefetch["bmi"]
                assert isinstance(bmi, dict)
                bmi_coding = bmi["code"]["coding"][0]
                quantity = bmi["valueQuantity"]
                if days_between(str(context["decisionTime"]), str(bmi["effectiveDateTime"])) > 365:
                    body = status_card("required input stale")
                    outcome, notice = "visible_input_stale", True
                    terminal_branch = "required_input_stale"
                elif float(quantity["value"]) <= 0 or float(quantity["value"]) > 100:
                    body = status_card("required input inconsistent")
                    outcome, notice = "visible_input_inconsistent", True
                    terminal_branch = "input_inconsistent"
                elif bmi_coding.get("system") != "http://loinc.org" or bmi_coding.get("code") != "39156-5":
                    body = status_card("terminology mismatch")
                    outcome, notice = "visible_terminology_mismatch", True
                    terminal_branch = "terminology_mismatch"
                elif quantity.get("system") != "http://unitsofmeasure.org" or quantity.get("code") != "kg/m2":
                    body = status_card("unit mismatch")
                    outcome, notice = "visible_unit_mismatch", True
                    terminal_branch = "unit_mismatch"
                elif prefetch["conditions"].get("entry"):
                    body = {"cards": []}
                    outcome = "known_diabetes_suppressed"
                    terminal_branch = "known_diabetes_suppression"
                elif prefetch["hba1c"].get("entry"):
                    body = {"cards": []}
                    outcome = "recent_hba1c_suppressed"
                    terminal_branch = "recent_hba1c_suppression"
                elif "prediction" not in prefetch:
                    body = status_card("offline teaching score missing")
                    outcome, notice = "visible_score_missing", True
                    terminal_branch = "score_missing"
                else:
                    prediction = prefetch["prediction"]
                    assert isinstance(prediction, dict)
                    version = parameter(prediction, "modelVersion")
                    score_item = parameter(prediction, "offlineTeachingScore")
                    threshold_item = parameter(prediction, "thresholdFixture")
                    if not version or version.get("valueString") != MODEL_VERSION:
                        body = status_card("model version mismatch")
                        outcome, notice = "visible_model_version_mismatch", True
                        terminal_branch = "model_version_mismatch"
                    elif not score_item:
                        body = status_card("offline teaching score missing")
                        outcome, notice = "visible_score_missing", True
                        terminal_branch = "score_missing"
                    elif not threshold_item or Decimal(str(threshold_item["valueDecimal"])) != THRESHOLD:
                        body = status_card("threshold fixture mismatch")
                        outcome, notice = "visible_threshold_fixture_mismatch", True
                        terminal_branch = "threshold_fixture_mismatch"
                    else:
                        score = Decimal(str(score_item["valueDecimal"]))
                        if score < THRESHOLD:
                            body = {"cards": []}
                            outcome = "no_card_below_fixture"
                            terminal_branch = "below_unaccepted_fixture"
                        else:
                            body = candidate_card(case, score)
                            outcome = "candidate_panel_boundary" if case_id == "M05-B01" else (
                                "repeat_candidate_panel" if context["repeatCandidateCard"] else "candidate_panel"
                            )
                            terminal_branch = "at_or_above_unaccepted_fixture"
                            if context["faultMode"] == "omit_summary":
                                body["cards"][0].pop("summary")

        access_status, access_detail = card_accessibility(body)
        if access_status == "defect_detected":
            body = operation_outcome("invalid", "Synthetic card failed the declared accessibility contract")
            outcome, http_status, notice = "accessibility_blocked", 422, True
            terminal_branch = "accessibility_defect_blocked"
        accessibility.append({
            "case_id": case_id,
            "category": case["category"],
            "status": access_status,
            **access_detail,
            "claim_limit": CLAIM_LIMIT,
        })
        if terminal:
            trace(case_id, request_id, 1, "terminal_result", terminal_branch, True, "sandbox audit")
        responses.append({
            "caseId": case_id,
            "requestId": request_id,
            "httpStatus": http_status,
            "responsePresent": body is not None,
            "terminalTracePresent": terminal,
            "humanNoticePresent": notice,
            "observedOutcome": outcome,
            "body": body,
            "claimLimit": CLAIM_LIMIT,
        })

    response_by_case = {str(row["caseId"]): row for row in responses}
    terminal_cases = {str(row["case_id"]) for row in traces if row["terminal"] == "true"}
    visibility: list[dict[str, object]] = []
    results: list[dict[str, object]] = []
    access_by_case = {str(row["case_id"]): row for row in accessibility}
    for case in cases:
        case_id = str(case["caseId"])
        expected_result = case["expected"]
        observed = response_by_case[case_id]
        silent_detected = (
            not bool(observed["responsePresent"])
            and case_id not in terminal_cases
            and not bool(observed["humanNoticePresent"])
        )
        visibility.append({
            "case_id": case_id,
            "category": case["category"],
            "request_received": "true",
            "response_present": str(bool(observed["responsePresent"])).lower(),
            "terminal_trace_present": str(case_id in terminal_cases).lower(),
            "human_notice_present": str(bool(observed["humanNoticePresent"])).lower(),
            "silent_failure_detected": str(silent_detected).lower(),
            "detection_basis": "request ledger compared with response, terminal trace, and human notice",
            "claim_limit": CLAIM_LIMIT,
        })
        checks = (
            observed["observedOutcome"] == expected_result["outcome"],
            int(observed["httpStatus"]) == int(expected_result["httpStatus"]),
            bool(observed["responsePresent"]) == bool(expected_result["responsePresent"]),
            (case_id in terminal_cases) == bool(expected_result["terminalTracePresent"]),
            bool(observed["humanNoticePresent"]) == bool(expected_result["humanNoticePresent"]),
            access_by_case[case_id]["status"] == expected_result["accessibility"],
            silent_detected == (expected_result["outcome"] == "silent_failure_detected"),
        )
        results.append({
            "case_id": case_id,
            "category": case["category"],
            "expected_outcome": expected_result["outcome"],
            "observed_outcome": observed["observedOutcome"],
            "expected_http_status": expected_result["httpStatus"],
            "observed_http_status": observed["httpStatus"],
            "response_present": str(bool(observed["responsePresent"])).lower(),
            "terminal_trace_present": str(case_id in terminal_cases).lower(),
            "human_notice_present": str(bool(observed["humanNoticePresent"])).lower(),
            "accessibility_status": access_by_case[case_id]["status"],
            "status": "pass" if all(checks) else "fail",
            "claim_limit": CLAIM_LIMIT,
        })
    return responses, traces, visibility, accessibility, results


def invariant_rows(
    cases: list[dict[str, object]],
    responses: list[dict[str, object]],
    traces: list[dict[str, object]],
    visibility: list[dict[str, object]],
    accessibility: list[dict[str, object]],
    results: list[dict[str, object]],
) -> list[dict[str, str]]:
    cards = [card for response in responses if response["body"] and "cards" in response["body"] for card in response["body"]["cards"]]
    positive_cases = [case for case in cases if str(case["caseId"]).startswith("M05-P")]
    checks = (
        ("I01", len(cases) == 31, "31 declared sandbox cases"),
        ("I02", len({case["caseId"] for case in cases}) == 31, "case identifiers unique"),
        ("I03", len(positive_cases) == 12, "all 12 Module 04 positive fixtures present"),
        ("I04", sum(bool(case["request"]["context"]["repeatCandidateCard"]) for case in positive_cases) == 1, "one Module 04 repeat fixture present"),
        ("I05", all(case["claimLimit"] == CLAIM_LIMIT for case in cases), "every case carries the claim limit"),
        ("I06", all(case["request"]["context"]["explicitSynthetic"] is True for case in cases), "every request is explicitly synthetic"),
        ("I07", all("fhirServer" not in case["request"] for case in cases), "no request contains a FHIR server endpoint"),
        ("I08", all(str(case["request"]["context"]["patientId"]).startswith("SP") for case in cases), "only Commons synthetic patient identifiers used"),
        ("I09", len(results) == 31 and all(row["status"] == "pass" for row in results), "all declared outcomes reproduced"),
        ("I10", sum(row["silent_failure_detected"] == "true" for row in visibility) == 1, "one silent failure detected"),
        ("I11", any(row["category"] == "service unavailable" for row in results), "unavailable service route tested"),
        ("I12", any(row["category"] == "response timeout" for row in results), "response timeout route tested"),
        ("I13", any(row["category"] == "duplicate request" for row in results), "duplicate route tested"),
        ("I14", any(row["category"] == "model version mismatch" for row in results), "model version route tested"),
        ("I15", any(row["status"] == "defect_detected" for row in accessibility), "accessibility defect detected and blocked"),
        ("I16", all(not card.get("suggestions") for card in cards), "no response contains an action suggestion"),
        ("I17", all(not card.get("links") for card in cards), "no response contains an external link"),
        ("I18", all(row["terminal"] in {"true", "false"} for row in traces), "trace terminal states explicit"),
        ("I19", all(response["claimLimit"] == CLAIM_LIMIT for response in responses), "every response carries the claim limit"),
        ("I20", THRESHOLD_TEXT == "0.03000000", "threshold remains the unaccepted Module 04 fixture"),
    )
    return [
        {"invariant_id": item, "status": "pass" if passed else "fail", "check": description}
        for item, passed, description in checks
    ]


def build(target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_sources()
    target.mkdir(parents=True)
    cases = build_cases()
    responses, traces, visibility, accessibility, results = evaluate_cases(cases)
    invariants = invariant_rows(cases, responses, traces, visibility, accessibility, results)
    if any(row["status"] != "pass" for row in invariants):
        failed = [row["invariant_id"] for row in invariants if row["status"] != "pass"]
        raise ValueError(f"Sandbox invariants failed: {', '.join(failed)}")

    prefetch_rows: list[dict[str, object]] = []
    request_rows: list[dict[str, object]] = []
    matrix_rows: list[dict[str, object]] = []
    for case in cases:
        request_rows.append({
            "caseId": case["caseId"],
            "category": case["category"],
            "fixtureOrigin": case["fixtureOrigin"],
            "serviceId": case["serviceId"],
            "hookVersion": case["hookVersion"],
            "request": case["request"],
            "claimLimit": CLAIM_LIMIT,
        })
        for key, resource in case["request"]["prefetch"].items():
            prefetch_rows.append({
                "caseId": case["caseId"],
                "prefetchKey": key,
                "resource": resource,
                "claimLimit": CLAIM_LIMIT,
            })
        expected_result = case["expected"]
        matrix_rows.append({
            "case_id": case["caseId"],
            "category": case["category"],
            "fixture_origin": case["fixtureOrigin"],
            "expected_outcome": expected_result["outcome"],
            "expected_http_status": expected_result["httpStatus"],
            "response_expected": str(bool(expected_result["responsePresent"])).lower(),
            "terminal_trace_expected": str(bool(expected_result["terminalTracePresent"])).lower(),
            "human_notice_expected": str(bool(expected_result["humanNoticePresent"])).lower(),
            "accessibility_expected": expected_result["accessibility"],
            "design_fixture": "panel-t003",
            "threshold_fixture": THRESHOLD_TEXT,
            "threshold_status": "unaccepted",
            "claim_limit": CLAIM_LIMIT,
        })

    write_jsonl_gzip(target / OUTPUT_FILES[0], request_rows)
    write_jsonl_gzip(target / OUTPUT_FILES[1], prefetch_rows)
    write_jsonl_gzip(target / OUTPUT_FILES[2], responses)
    write_gzip_csv(target / OUTPUT_FILES[3], tuple(traces[0]), traces)
    write_csv(target / OUTPUT_FILES[4], tuple(matrix_rows[0]), matrix_rows)
    write_csv(target / OUTPUT_FILES[5], tuple(results[0]), results)
    write_csv(target / OUTPUT_FILES[6], tuple(visibility[0]), visibility)
    write_csv(target / OUTPUT_FILES[7], tuple(accessibility[0]), accessibility)
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
        "release_id": "APP4-M05-LOCAL-SANDBOX-2026-08-31-v1",
        "status": "local nonnetworked synthetic teaching sandbox only",
        "generator": "APP-4 Module 05 Python standard-library builder 0.1.0",
        "source_contract": {
            source_id: {"bytes": details[1], "sha256": details[2]}
            for source_id, details in SOURCE_CONTRACT.items()
        },
        "upstream": {
            "module": "oclc-app4-04@0.1.0",
            "commons_release": "0.81.0",
            "reference_manifest_rows": 285,
            "reference_manifest_bytes": 60302,
            "reference_manifest_sha256": "41692b01fa2c339068fcdbf5fbc6f3e301a79ba4535d9ecb94d602cb2e4b3bf9",
            "reference_files": 302,
        },
        "sandbox": {
            "cases": len(cases),
            "module04_positive_cases": 12,
            "repeat_positive_cases": 1,
            "prefetch_resources": len(prefetch_rows),
            "responses": len(responses),
            "trace_events": len(traces),
            "visible_failure_cases": sum(str(row["observed_outcome"]).startswith("visible_") for row in results),
            "silent_failures_detected": sum(row["silent_failure_detected"] == "true" for row in visibility),
            "accessibility_defects_blocked": sum(row["status"] == "defect_detected" for row in accessibility),
            "passing_tests": sum(row["status"] == "pass" for row in results),
        },
        "design": {
            "id": "panel-t003",
            "role": "passive contextual panel fixture for mechanics testing only",
            "threshold": THRESHOLD_TEXT,
            "threshold_status": "unaccepted sandbox fixture",
            "accepted_threshold": None,
        },
        "runtime": {
            "network_listener": False,
            "network_client": False,
            "fhir_server": None,
            "external_python_dependencies": [],
        },
        "output_manifest": output_manifest,
        "authority": {
            "real_patient_scoring": "prohibited",
            "clinical_threshold_acceptance": "prohibited",
            "clinical_alerting": "prohibited",
            "clinical_action": "prohibited",
            "silent_mode_evaluation": "prohibited",
            "implementation": "prohibited",
            "production_connection": "prohibited",
            "deployment": "prohibited",
        },
        "claim_limit": CLAIM_LIMIT,
    }
    (target / OUTPUT_FILES[-1]).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return verify(target)


def verify(target: Path) -> dict[str, object]:
    missing = [relative for relative in OUTPUT_FILES if not (target / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"Sandbox release missing: {', '.join(missing)}")
    report = json.loads((target / "build-report.json").read_text(encoding="utf-8"))
    requests = read_jsonl_gzip(target / OUTPUT_FILES[0])
    prefetch = read_jsonl_gzip(target / OUTPUT_FILES[1])
    responses = read_jsonl_gzip(target / OUTPUT_FILES[2])
    traces = read_gzip_csv(target / OUTPUT_FILES[3])
    matrix = read_csv(target / OUTPUT_FILES[4])
    results = read_csv(target / OUTPUT_FILES[5])
    visibility = read_csv(target / OUTPUT_FILES[6])
    accessibility = read_csv(target / OUTPUT_FILES[7])
    invariants = read_csv(target / OUTPUT_FILES[8])
    if (
        len(requests) != 31
        or len(prefetch) != report["sandbox"]["prefetch_resources"]
        or len(responses) != 31
        or not traces
        or len(matrix) != 31
        or len(results) != 31
        or len(visibility) != 31
        or len(accessibility) != 31
        or len(invariants) != 20
        or any(row["status"] != "pass" for row in results + invariants)
        or sum(row["silent_failure_detected"] == "true" for row in visibility) != 1
        or sum(row["status"] == "defect_detected" for row in accessibility) != 1
        or report["design"]["id"] != "panel-t003"
        or report["design"]["threshold"] != THRESHOLD_TEXT
        or report["design"]["accepted_threshold"] is not None
        or report["runtime"]["network_listener"] is not False
        or report["runtime"]["network_client"] is not False
    ):
        raise ValueError("Sandbox release contract failed")
    source_text = (MODULE_ROOT / "build_sandbox.py").read_text(encoding="utf-8") if (MODULE_ROOT / "build_sandbox.py").is_file() else ""
    for prohibited_import in ("import requests", "import urllib", "import socket", "import http.client"):
        if any(line.strip().startswith(prohibited_import) for line in source_text.splitlines()):
            raise ValueError(f"Network-capable import prohibited: {prohibited_import}")
    for item in report["output_manifest"]:
        path = target / item["relative_path"]
        if path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
            raise ValueError(f"Sandbox output identity changed: {item['relative_path']}")
    return {
        "status": "pass",
        "cases": len(requests),
        "prefetch_resources": len(prefetch),
        "responses": len(responses),
        "trace_events": len(traces),
        "passing_tests": sum(row["status"] == "pass" for row in results),
        "silent_failures_detected": sum(row["silent_failure_detected"] == "true" for row in visibility),
        "accessibility_defects_blocked": sum(row["status"] == "defect_detected" for row in accessibility),
        "output_manifest_sha256": hashlib.sha256(
            json.dumps(report["output_manifest"], sort_keys=True).encode("utf-8")
        ).hexdigest(),
    }


def publish() -> dict[str, object]:
    existing = [relative for relative in OUTPUT_FILES if (MODULE_ROOT / relative).exists()]
    if existing:
        raise FileExistsError(f"Refusing to replace package outputs: {', '.join(existing)}")
    with tempfile.TemporaryDirectory(prefix="app4-module05-publish-") as temporary:
        built = Path(temporary) / "release"
        result = build(built)
        for relative in OUTPUT_FILES:
            destination = MODULE_ROOT / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(built / relative, destination)
    return result


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module05-sandbox-") as temporary:
        base = Path(temporary)
        first, second = base / "first", base / "second"
        one = build(first)
        two = build(second)
        if one != two:
            raise AssertionError("Sandbox builds are not deterministic")
        first_hashes = {relative: sha256(first / relative) for relative in OUTPUT_FILES}
        second_hashes = {relative: sha256(second / relative) for relative in OUTPUT_FILES}
        if first_hashes != second_hashes:
            raise AssertionError("Sandbox output bytes changed between builds")
        try:
            build(first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Sandbox builder overwrote an existing target")
    print(
        "APP-4 Module 05 sandbox builder self-check passed: "
        f"{one['cases']} cases, {one['prefetch_resources']} prefetch resources, "
        f"{one['trace_events']} trace events, and {one['silent_failures_detected']} silent failure detected."
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
    except (OSError, ValueError, KeyError, AssertionError, json.JSONDecodeError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
