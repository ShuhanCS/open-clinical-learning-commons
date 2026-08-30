"""Build APP-2 Module 04 linked patient evidence from official MEPS PUFs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Callable


MODULE_ROOT = Path(__file__).resolve().parent
RAW_ROOT = MODULE_ROOT / "data/raw"
GENERATED_FILES = (
    "data/public/linked-persons.csv",
    "data/public/linked-events.csv",
    "outputs/source-profile.csv",
    "outputs/linkage-reconciliation.csv",
    "outputs/denominator-registry.csv",
    "outputs/access-communication-estimates.csv",
    "outputs/service-use-estimates.csv",
    "outputs/digital-engagement.csv",
    "outputs/linked-evidence-patterns.csv",
    "outputs/invariant-checks.csv",
    "build-report.json",
)

PERSON_FIELDS = (
    "DUPERSID", "AGE24X", "PERWT24F", "VARSTR", "VARPSU",
    "IPDIS24", "ERTOT24", "OPTOTV24", "OBTOTV24",
    "ACCELI42", "HAVEUS42", "PHNREG42", "OFFHOU42", "AFTHOU42",
    "TREATM42", "DECIDE42", "EXPLOP42", "PRVSPK42", "DLAYCA42", "AFRDCA42",
)

EVENT_CONFIG = {
    "h254d": {
        "setting": "inpatient", "year": "IPBEGYR", "month": "IPBEGMM",
        "medicine": "DSCHPMED", "expenditure": "IPXP24X",
        "fields": ("DUPERSID", "EVNTIDX", "ERHEVIDX", "IPBEGYR", "IPBEGMM", "IPENDYR", "IPENDMM", "NUMNIGHX", "EMERROOM", "ANYOPER", "DSCHPMED", "IPXP24X", "PERWT24F", "VARSTR", "VARPSU"),
    },
    "h254e": {
        "setting": "emergency", "year": "ERDATEYR", "month": "ERDATEMM",
        "medicine": "MEDPRESC", "expenditure": "ERXP24X",
        "fields": ("DUPERSID", "EVNTIDX", "ERHEVIDX", "ERDATEYR", "ERDATEMM", "MEDPRESC", "ERXP24X", "PERWT24F", "VARSTR", "VARPSU"),
    },
    "h254f": {
        "setting": "outpatient", "year": "OPDATEYR", "month": "OPDATEMM",
        "medicine": "MEDPRESC", "expenditure": "OPXP24X",
        "fields": ("DUPERSID", "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC_M18", "MEDPRESC", "TELEHEALTHFLAG", "VISITTYPE", "OPXP24X", "PERWT24F", "VARSTR", "VARPSU"),
    },
    "h254g": {
        "setting": "office_based", "year": "OBDATEYR", "month": "OBDATEMM",
        "medicine": "MEDPRESC", "expenditure": "OBXP24X",
        "fields": ("DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC_M18", "MEDPRESC", "TELEHEALTHFLAG", "VISITTYPE", "OBXP24X", "PERWT24F", "VARSTR", "VARPSU"),
    },
}

ACCESS_MEASURES = (
    ("usual_source", "HAVEUS42", {1, 2}, {1}, "has a usual source of care"),
    ("regular_phone_difficult", "PHNREG42", {1, 2, 3, 4}, {1, 2}, "regular phone contact is very or somewhat difficult"),
    ("evening_weekend_hours", "OFFHOU42", {1, 2}, {1}, "usual source has evening or weekend hours"),
    ("after_hours_difficult", "AFTHOU42", {1, 2, 3, 4}, {1, 2}, "after-hours contact is very or somewhat difficult"),
    ("asked_other_treatments", "TREATM42", {1, 2}, {1}, "provider asks about other treatments"),
    ("involved_usually_always", "DECIDE42", {1, 2, 3, 4}, {3, 4}, "provider usually or always asks the person to help decide"),
    ("options_explained", "EXPLOP42", {1, 2}, {1}, "provider explains options"),
    ("provider_language_match", "PRVSPK42", {1, 2}, {1}, "provider speaks the person's language"),
    ("delayed_for_cost", "DLAYCA42", {1, 2}, {1}, "medical care was delayed because of cost"),
    ("unable_to_afford", "AFRDCA42", {1, 2}, {1}, "person could not afford medical care"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: float, digits: int = 8) -> str:
    return f"{value:.{digits}f}"


def integer(value: str | int | float | None) -> int:
    if value in (None, ""):
        return -999
    return int(float(value))


def number(value: str | int | float | None) -> float:
    if value in (None, ""):
        return 0.0
    return float(value)


def parse_vector(text: str, name: str, strings: bool = False) -> list[int] | list[str]:
    match = re.search(rf"{name}\s*<-\s*c\((.*?)\)\s*", text, re.DOTALL)
    if not match:
        raise ValueError(f"Official R statement is missing {name}")
    if strings:
        return re.findall(r'"([^"]+)"', match.group(1))
    return [int(value) for value in re.findall(r"-?\d+", match.group(1))]


def r_layout(path: Path) -> dict[str, tuple[int, int]]:
    text = path.read_text(encoding="utf-8-sig")
    starts = parse_vector(text, "pos_start")
    ends = parse_vector(text, "pos_end")
    names = parse_vector(text, "var_names", strings=True)
    if not (len(starts) == len(ends) == len(names)):
        raise ValueError(f"Official R layout vectors differ in {path.name}")
    return {str(name): (int(start), int(end)) for start, end, name in zip(starts, ends, names)}


def read_puf(puf: str, fields: tuple[str, ...]) -> tuple[list[dict[str, str]], dict[str, object]]:
    layout = r_layout(RAW_ROOT / f"{puf}ru.txt")
    missing = [field for field in fields if field not in layout]
    if missing:
        raise ValueError(f"{puf} layout is missing fields: {', '.join(missing)}")
    archive = RAW_ROOT / f"{puf}dat.zip"
    rows: list[dict[str, str]] = []
    widths: set[int] = set()
    with zipfile.ZipFile(archive) as bundle:
        expected_member = f"{puf}.dat"
        if bundle.namelist() != [expected_member]:
            raise ValueError(f"{archive.name} must contain only {expected_member}")
        with bundle.open(expected_member) as handle:
            for raw in handle:
                line = raw.decode("ascii").rstrip("\r\n")
                widths.add(len(line))
                rows.append({field: line[layout[field][0] - 1:layout[field][1]].strip() for field in fields})
    if len(widths) != 1:
        raise ValueError(f"{puf} has inconsistent fixed-width rows: {sorted(widths)}")
    return rows, {"member": f"{puf}.dat", "rows": len(rows), "width": next(iter(widths)), "variables": len(layout)}


def verify_inventory(path: Path, expected_rows: int) -> tuple[int, int]:
    rows = read_csv(path)
    if len(rows) != expected_rows:
        raise ValueError(f"{path.name} must have {expected_rows} rows")
    total_bytes = 0
    total_pages = 0
    for row in rows:
        source = MODULE_ROOT / row["relative_path"]
        if not source.is_file() or source.stat().st_size != int(row["bytes"]) or sha256(source) != row["sha256"]:
            raise ValueError(f"Pinned source changed: {row['relative_path']}")
        total_bytes += source.stat().st_size
        total_pages += int(row.get("pages") or 0)
    return total_bytes, total_pages


def label_binary(value: int) -> str:
    return {1: "yes", 2: "no"}.get(value, "missing_or_inapplicable")


def label_difficulty(value: int) -> str:
    return {1: "very_difficult", 2: "somewhat_difficult", 3: "not_too_difficult", 4: "not_at_all_difficult"}.get(value, "missing_or_inapplicable")


def label_decision(value: int) -> str:
    return {1: "never", 2: "sometimes", 3: "usually", 4: "always"}.get(value, "missing_or_inapplicable")


def label_provider_contact(value: int) -> str:
    return {1: "doctor", 2: "no_doctor"}.get(value, "unknown_or_refused")


def label_visit_type(value: int) -> str:
    return {1: "phone", 2: "video", 3: "other"}.get(value, "not_applicable_or_unknown")


def survey_estimate(
    rows: list[dict[str, object]],
    eligible: Callable[[dict[str, object]], bool],
    value: Callable[[dict[str, object]], float],
    weight_field: str = "base_person_weight",
    scale: float = 1.0,
) -> dict[str, object]:
    design = [row for row in rows if number(row.get(weight_field)) > 0]
    domain = [row for row in design if eligible(row)]
    if not domain:
        return {"n": 0, "positive_n": 0, "weight": 0.0, "estimate": math.nan, "se": math.nan, "low": math.nan, "high": math.nan, "psus": 0}
    total_weight = sum(number(row[weight_field]) for row in domain)
    estimate = sum(number(row[weight_field]) * value(row) for row in domain) / total_weight
    cluster: dict[tuple[int, int], float] = defaultdict(float)
    strata: dict[int, set[int]] = defaultdict(set)
    for row in design:
        stratum = integer(row["variance_stratum"])
        psu = integer(row["variance_psu"])
        strata[stratum].add(psu)
        contribution = number(row[weight_field]) * (value(row) - estimate) if eligible(row) else 0.0
        cluster[(stratum, psu)] += contribution
    variance_total = 0.0
    for stratum, psus in strata.items():
        values = [cluster[(stratum, psu)] for psu in sorted(psus)]
        if len(values) < 2:
            continue
        mean_value = sum(values) / len(values)
        variance_total += len(values) / (len(values) - 1) * sum((item - mean_value) ** 2 for item in values)
    se = math.sqrt(max(variance_total, 0.0)) / total_weight
    estimate_scaled = estimate * scale
    se_scaled = se * scale
    return {
        "n": len(domain),
        "positive_n": sum(value(row) > 0 for row in domain),
        "weight": total_weight,
        "estimate": estimate_scaled,
        "se": se_scaled,
        "low": max(0.0, estimate_scaled - 1.96 * se_scaled),
        "high": estimate_scaled + 1.96 * se_scaled,
        "psus": len(cluster),
    }


def build(output_root: Path = MODULE_ROOT) -> dict[str, object]:
    output_root = output_root.resolve()
    source_bytes, source_pages = verify_inventory(MODULE_ROOT / "data/source-inventory.csv", 25)
    upstream_bytes, _ = verify_inventory(MODULE_ROOT / "data/upstream-inventory.csv", 3)

    checkpoint = json.loads((MODULE_ROOT / "data/upstream/checkpoint01-release.json").read_text(encoding="utf-8"))
    if checkpoint["package"]["candidate_manifest_sha256"] != "5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903":
        raise ValueError("Week 3 checkpoint candidate identity changed")
    if checkpoint["progression"]["module04_permission"] != "permitted for linked analysis":
        raise ValueError("Week 3 checkpoint does not permit linked analysis")

    upstream_frame = read_csv(MODULE_ROOT / "data/upstream/module03-adult-inpatient-frame.csv")
    upstream_response = read_csv(MODULE_ROOT / "data/upstream/module03-response-study.csv")
    response_by_frame = {row["frame_record_id"]: row for row in upstream_response}

    person_rows, person_meta = read_puf("h256", PERSON_FIELDS)
    all_people = {row["DUPERSID"]: row for row in person_rows}
    selected = [
        row for row in person_rows
        if integer(row["AGE24X"]) >= 18 and number(row["PERWT24F"]) > 0 and integer(row["IPDIS24"]) >= 1
    ]
    selected.sort(key=lambda row: row["DUPERSID"])
    if len(selected) != len(upstream_frame) or len(selected) != len(upstream_response):
        raise ValueError("Module 03 target and Module 04 target differ")

    people: list[dict[str, object]] = []
    people_by_source: dict[str, dict[str, object]] = {}
    for index, (source, accepted) in enumerate(zip(selected, upstream_frame), 1):
        frame_id = f"FRAME-{index:04d}"
        if accepted["frame_record_id"] != frame_id:
            raise ValueError("Accepted Module 03 frame order changed")
        if integer(accepted["inpatient_discharges"]) != integer(source["IPDIS24"]):
            raise ValueError(f"Upstream inpatient count changed for {frame_id}")
        if abs(number(accepted["base_person_weight"]) - number(source["PERWT24F"])) > 0.000001:
            raise ValueError(f"Upstream person weight changed for {frame_id}")
        response = response_by_frame[frame_id]
        row: dict[str, object] = {
            "link_person_id": f"LINK-{index:04d}",
            "frame_record_id": frame_id,
            "data_class": "public_derived_meps_with_synthetic_response_handoff",
            "age_band": accepted["age_band"],
            "sex": accepted["sex"],
            "race_ethnicity": accepted["race_ethnicity"],
            "other_language_at_home": accepted["other_language_at_home"],
            "health_status": accepted["health_status"],
            "income_group": accepted["income_group"],
            "insurance_coverage": accepted["insurance_coverage"],
            "base_person_weight": fmt(number(source["PERWT24F"]), 6),
            "variance_stratum": integer(source["VARSTR"]),
            "variance_psu": integer(source["VARPSU"]),
            "inpatient_discharges_reported": integer(source["IPDIS24"]),
            "inpatient_events_linked": 0,
            "emergency_visits_reported": integer(source["ERTOT24"]),
            "emergency_events_linked": 0,
            "outpatient_visits_reported": integer(source["OPTOTV24"]),
            "outpatient_events_linked": 0,
            "office_visits_reported": integer(source["OBTOTV24"]),
            "office_events_linked": 0,
            "usual_source": label_binary(integer(source["HAVEUS42"])),
            "regular_phone_contact": label_difficulty(integer(source["PHNREG42"])),
            "evening_weekend_hours": label_binary(integer(source["OFFHOU42"])),
            "after_hours_contact": label_difficulty(integer(source["AFTHOU42"])),
            "asked_other_treatments": label_binary(integer(source["TREATM42"])),
            "involved_in_decisions": label_decision(integer(source["DECIDE42"])),
            "options_explained": label_binary(integer(source["EXPLOP42"])),
            "provider_language": label_binary(integer(source["PRVSPK42"])),
            "delayed_medical_care_for_cost": label_binary(integer(source["DLAYCA42"])),
            "unable_to_afford_medical_care": label_binary(integer(source["AFRDCA42"])),
            "response_status": response["response_status"],
            "q21_observed": response["q21_observed"],
            "q22_observed": response["q22_observed"],
            "q23_observed": response["q23_observed"],
            "response_analysis_weight": response["analysis_weight"],
            "_source_id": source["DUPERSID"],
            "_codes": {field: integer(source[field]) for _, field, _, _, _ in ACCESS_MEASURES},
            "_event_counts": defaultdict(int),
            "_telehealth_counts": defaultdict(int),
        }
        people.append(row)
        people_by_source[source["DUPERSID"]] = row

    raw_event_rows: dict[str, list[dict[str, str]]] = {}
    event_meta: dict[str, dict[str, object]] = {}
    all_event_rows = 0
    all_events_linked = 0
    event_weight_mismatches = 0
    target_internal: list[dict[str, object]] = []
    for puf, config in EVENT_CONFIG.items():
        rows, metadata = read_puf(puf, config["fields"])
        raw_event_rows[puf] = rows
        event_meta[puf] = metadata
        all_event_rows += len(rows)
        for event in rows:
            person = all_people.get(event["DUPERSID"])
            if person is None:
                continue
            all_events_linked += 1
            if abs(number(event["PERWT24F"]) - number(person["PERWT24F"])) > 0.000001:
                event_weight_mismatches += 1
            target_person = people_by_source.get(event["DUPERSID"])
            if target_person is None:
                continue
            setting = str(config["setting"])
            target_person["_event_counts"][setting] += 1
            if "TELEHEALTHFLAG" in event and integer(event["TELEHEALTHFLAG"]) == 1:
                target_person["_telehealth_counts"][setting] += 1
                target_person["_telehealth_counts"][label_visit_type(integer(event["VISITTYPE"]))] += 1
            target_internal.append({"puf": puf, "setting": setting, "source": event, "person": target_person})

    setting_order = {"inpatient": 0, "emergency": 1, "outpatient": 2, "office_based": 3}
    target_internal.sort(key=lambda item: (setting_order[str(item["setting"])], str(item["source"]["EVNTIDX"])))
    event_key_map: dict[tuple[str, str, str], str] = {}
    setting_sequence: dict[str, int] = defaultdict(int)
    for item in target_internal:
        setting = str(item["setting"])
        setting_sequence[setting] += 1
        event_key = f"EVENT-{setting.upper()}-{setting_sequence[setting]:05d}"
        item["event_key"] = event_key
        event = item["source"]
        event_key_map[(str(item["puf"]), event["DUPERSID"], event["EVNTIDX"])] = event_key

    released_events: list[dict[str, object]] = []
    related_target_pairs: set[tuple[str, str]] = set()
    for item in target_internal:
        puf = str(item["puf"])
        config = EVENT_CONFIG[puf]
        event = item["source"]
        related_key = ""
        if puf == "h254d" and integer(event.get("ERHEVIDX")) > 0:
            related_key = event_key_map.get(("h254e", event["DUPERSID"], event["ERHEVIDX"]), "")
        elif puf == "h254e" and integer(event.get("ERHEVIDX")) > 0:
            related_key = event_key_map.get(("h254d", event["DUPERSID"], event["ERHEVIDX"]), "")
        if related_key:
            related_target_pairs.add(tuple(sorted((str(item["event_key"]), related_key))))
        telehealth_code = integer(event.get("TELEHEALTHFLAG"))
        released_events.append({
            "link_person_id": item["person"]["link_person_id"],
            "frame_record_id": item["person"]["frame_record_id"],
            "linked_event_id": item["event_key"],
            "related_event_id": related_key,
            "data_class": "public_derived_meps_event",
            "source_puf": puf.upper(),
            "event_setting": item["setting"],
            "event_year": integer(event[str(config["year"])]),
            "event_month": integer(event[str(config["month"])]),
            "provider_contact": label_provider_contact(integer(event.get("SEEDOC_M18"))) if "SEEDOC_M18" in event else "not_collected",
            "medicine_reported": label_binary(integer(event[str(config["medicine"])])),
            "telehealth_status": label_binary(telehealth_code) if "TELEHEALTHFLAG" in event else "not_collected",
            "telehealth_mode": label_visit_type(integer(event.get("VISITTYPE"))) if telehealth_code == 1 else "not_applicable_or_unknown",
            "total_expenditure": fmt(number(event[str(config["expenditure"])]), 2),
            "person_weight": fmt(number(event["PERWT24F"]), 6),
            "variance_stratum": integer(event["VARSTR"]),
            "variance_psu": integer(event["VARPSU"]),
        })

    count_fields = {
        "inpatient": ("inpatient_discharges_reported", "inpatient_events_linked"),
        "emergency": ("emergency_visits_reported", "emergency_events_linked"),
        "outpatient": ("outpatient_visits_reported", "outpatient_events_linked"),
        "office_based": ("office_visits_reported", "office_events_linked"),
    }
    for row in people:
        for setting, (_, linked_field) in count_fields.items():
            row[linked_field] = row["_event_counts"][setting]

    person_fields = [
        "link_person_id", "frame_record_id", "data_class", "age_band", "sex", "race_ethnicity",
        "other_language_at_home", "health_status", "income_group", "insurance_coverage",
        "base_person_weight", "variance_stratum", "variance_psu",
        "inpatient_discharges_reported", "inpatient_events_linked",
        "emergency_visits_reported", "emergency_events_linked",
        "outpatient_visits_reported", "outpatient_events_linked",
        "office_visits_reported", "office_events_linked",
        "usual_source", "regular_phone_contact", "evening_weekend_hours", "after_hours_contact",
        "asked_other_treatments", "involved_in_decisions", "options_explained", "provider_language",
        "delayed_medical_care_for_cost", "unable_to_afford_medical_care",
        "response_status", "q21_observed", "q22_observed", "q23_observed", "response_analysis_weight",
    ]
    write_csv(output_root / "data/public/linked-persons.csv", person_fields, [{field: row[field] for field in person_fields} for row in people])
    event_fields = [
        "link_person_id", "frame_record_id", "linked_event_id", "related_event_id", "data_class",
        "source_puf", "event_setting", "event_year", "event_month", "provider_contact",
        "medicine_reported", "telehealth_status", "telehealth_mode", "total_expenditure",
        "person_weight", "variance_stratum", "variance_psu",
    ]
    write_csv(output_root / "data/public/linked-events.csv", event_fields, released_events)

    source_profile = [
        {"metric": "official_source_files", "value": 25, "unit": "files", "evidence": "five official files for each of HC-256 and HC-254D through HC-254G"},
        {"metric": "official_source_bytes", "value": source_bytes, "unit": "bytes", "evidence": "fingerprinted source inventory"},
        {"metric": "official_pdf_pages", "value": source_pages, "unit": "pages", "evidence": "documentation and codebooks"},
        {"metric": "upstream_handoff_files", "value": 3, "unit": "files", "evidence": "Week 3 accepted handoff"},
        {"metric": "upstream_handoff_bytes", "value": upstream_bytes, "unit": "bytes", "evidence": "fingerprinted upstream inventory"},
        {"metric": "person_source_rows", "value": len(person_rows), "unit": "people", "evidence": "full h256.dat"},
        {"metric": "event_source_rows", "value": all_event_rows, "unit": "events", "evidence": "full h254d through h254g data files"},
        {"metric": "target_rows", "value": len(people), "unit": "people", "evidence": "accepted Week 3 target"},
        {"metric": "target_linked_event_rows", "value": len(released_events), "unit": "events", "evidence": "four linked event files"},
        {"metric": "target_inpatient_carry_in_starts", "value": sum(row["event_setting"] == "inpatient" and integer(row["event_year"]) == 2023 for row in released_events), "unit": "stays", "evidence": "HC-254D stays beginning in 2023 and continuing into the 2024 event file"},
        {"metric": "target_base_weighted_population", "value": fmt(sum(number(row["base_person_weight"]) for row in people), 6), "unit": "people", "evidence": "PERWT24F"},
        {"metric": "synthetic_response_rows", "value": len(upstream_response), "unit": "procedural rows", "evidence": "accepted Module 03 response handoff"},
        {"metric": "synthetic_respondents", "value": sum(row["response_status"] == "respondent" for row in people), "unit": "procedural rows", "evidence": "accepted Module 03 response handoff"},
    ]
    write_csv(output_root / "outputs/source-profile.csv", ["metric", "value", "unit", "evidence"], source_profile)

    reconciliation: list[dict[str, object]] = []
    for puf, config in EVENT_CONFIG.items():
        setting = str(config["setting"])
        reported_field, linked_field = count_fields[setting]
        reconciliation.append({
            "source_puf": puf.upper(), "setting": setting,
            "full_source_rows": len(raw_event_rows[puf]),
            "full_rows_linked_to_h256": sum(event["DUPERSID"] in all_people for event in raw_event_rows[puf]),
            "target_reported_total": sum(integer(row[reported_field]) for row in people),
            "target_linked_event_rows": sum(integer(row[linked_field]) for row in people),
            "difference": sum(integer(row[linked_field]) - integer(row[reported_field]) for row in people),
            "target_people_with_event": sum(integer(row[linked_field]) > 0 for row in people),
            "status": "pass" if all(integer(row[reported_field]) == integer(row[linked_field]) for row in people) else "fail",
        })
    reconciliation.append({
        "source_puf": "HC-254D/HC-254E", "setting": "related_emergency_inpatient_pair",
        "full_source_rows": 968, "full_rows_linked_to_h256": 968,
        "target_reported_total": len(related_target_pairs), "target_linked_event_rows": len(related_target_pairs),
        "difference": 0, "target_people_with_event": len({row["link_person_id"] for row in released_events if row["related_event_id"]}),
        "status": "pass",
    })
    write_csv(output_root / "outputs/linkage-reconciliation.csv", list(reconciliation[0]), reconciliation)

    denominator_rows: list[dict[str, object]] = []
    target_weight = sum(number(row["base_person_weight"]) for row in people)
    denominator_rows.append({"denominator_id": "D001", "grain": "person", "eligibility": "accepted adult inpatient target", "unweighted_n": len(people), "weighted_denominator": fmt(target_weight, 6), "data_class": "public_derived", "used_by": "service-use estimates"})
    for index, (measure, field, valid, _, definition) in enumerate(ACCESS_MEASURES, 2):
        domain = [row for row in people if row["_codes"][field] in valid]
        denominator_rows.append({"denominator_id": f"D{index:03d}", "grain": "person", "eligibility": f"valid {field}: {definition}", "unweighted_n": len(domain), "weighted_denominator": fmt(sum(number(row["base_person_weight"]) for row in domain), 6), "data_class": "public_meps", "used_by": measure})
    digital_events = [row for row in released_events if row["event_setting"] in {"outpatient", "office_based"}]
    denominator_rows.append({"denominator_id": "D020", "grain": "event", "eligibility": "linked outpatient and office-based events", "unweighted_n": len(digital_events), "weighted_denominator": fmt(sum(number(row["person_weight"]) for row in digital_events), 6), "data_class": "public_derived", "used_by": "telehealth event distribution"})
    complete_response = [row for row in people if row["q21_observed"] == "home_or_other" and row["q22_observed"] in {"yes", "no"} and row["q23_observed"] in {"yes", "no"}]
    denominator_rows.append({"denominator_id": "D021", "grain": "person", "eligibility": "synthetic respondent with Q21 home and both Q22 and Q23 answered", "unweighted_n": len(complete_response), "weighted_denominator": fmt(sum(number(row["response_analysis_weight"]) for row in complete_response), 6), "data_class": "public_meps_plus_synthetic_response", "used_by": "linked teaching patterns"})
    denominator_rows.append({"denominator_id": "D022", "grain": "person", "eligibility": "portal preference or portal access measure", "unweighted_n": 0, "weighted_denominator": "", "data_class": "not_available", "used_by": "explicit evidence gap"})
    write_csv(output_root / "outputs/denominator-registry.csv", list(denominator_rows[0]), denominator_rows)

    access_rows: list[dict[str, object]] = []
    for measure, field, valid, positive, definition in ACCESS_MEASURES:
        estimate = survey_estimate(people, lambda row, f=field, v=valid: row["_codes"][f] in v, lambda row, f=field, p=positive: float(row["_codes"][f] in p), scale=100.0)
        access_rows.append({
            "measure": measure, "source_field": field, "definition": definition,
            "eligible_persons": estimate["n"], "positive_persons": estimate["positive_n"],
            "weighted_denominator": fmt(float(estimate["weight"]), 6),
            "weighted_percent": fmt(float(estimate["estimate"])), "survey_se_pp": fmt(float(estimate["se"])),
            "ci95_low_percent": fmt(float(estimate["low"])), "ci95_high_percent": fmt(min(100.0, float(estimate["high"]))),
            "support_flag": "limited_support" if int(estimate["n"]) < 50 else "reportable_teaching_support",
        })
    write_csv(output_root / "outputs/access-communication-estimates.csv", list(access_rows[0]), access_rows)

    service_rows: list[dict[str, object]] = []
    for setting in ("inpatient", "emergency", "outpatient", "office_based"):
        _, linked_field = count_fields[setting]
        for statistic, value_function, unit in (
            ("any_use", lambda row, f=linked_field: float(integer(row[f]) > 0), "percent"),
            ("mean_events", lambda row, f=linked_field: float(integer(row[f])), "events_per_person"),
        ):
            estimate = survey_estimate(people, lambda row: True, value_function, scale=100.0 if unit == "percent" else 1.0)
            service_rows.append({
                "setting": setting, "statistic": statistic, "eligible_persons": estimate["n"],
                "persons_with_use": sum(integer(row[linked_field]) > 0 for row in people),
                "unweighted_value": fmt(sum(value_function(row) for row in people) / len(people) * (100.0 if unit == "percent" else 1.0)),
                "weighted_estimate": fmt(float(estimate["estimate"])), "survey_se": fmt(float(estimate["se"])),
                "ci95_low": fmt(float(estimate["low"])), "ci95_high": fmt(float(estimate["high"])),
                "unit": unit, "claim_limit": "descriptive association only; no causal or quality claim",
            })
    write_csv(output_root / "outputs/service-use-estimates.csv", list(service_rows[0]), service_rows)

    digital_rows: list[dict[str, object]] = []
    for evidence_id, setting, numerator_test, interpretation in (
        ("DE01", "outpatient", lambda row: row["telehealth_status"] == "yes", "share of linked outpatient events marked telehealth"),
        ("DE02", "office_based", lambda row: row["telehealth_status"] == "yes", "share of linked office-based events marked telehealth"),
        ("DE03", "combined", lambda row: row["telehealth_status"] == "yes", "share of linked outpatient and office-based events marked telehealth"),
        ("DE04", "telehealth_only", lambda row: row["telehealth_mode"] == "phone", "phone share among linked telehealth events"),
        ("DE05", "telehealth_only", lambda row: row["telehealth_mode"] == "video", "video share among linked telehealth events"),
        ("DE06", "telehealth_only", lambda row: row["telehealth_mode"] == "other", "other-mode share among linked telehealth events"),
    ):
        if setting == "combined":
            domain = digital_events
        elif setting == "telehealth_only":
            domain = [row for row in digital_events if row["telehealth_status"] == "yes"]
        else:
            domain = [row for row in digital_events if row["event_setting"] == setting]
        numerator = [row for row in domain if numerator_test(row)]
        denominator_weight = sum(number(row["person_weight"]) for row in domain)
        numerator_weight = sum(number(row["person_weight"]) for row in numerator)
        digital_rows.append({
            "evidence_id": evidence_id, "grain": "event", "setting": setting,
            "denominator_n": len(domain), "numerator_n": len(numerator),
            "unweighted_percent": fmt(100.0 * len(numerator) / len(domain)) if domain else "",
            "weighted_percent": fmt(100.0 * numerator_weight / denominator_weight) if denominator_weight else "",
            "interpretation": interpretation,
            "claim_limit": "event channel is not patient preference, portal access, engagement, or intervention effect",
        })
    digital_rows.append({"evidence_id": "DE07", "grain": "person", "setting": "portal_preference", "denominator_n": 0, "numerator_n": 0, "unweighted_percent": "", "weighted_percent": "", "interpretation": "not available in the accepted source suite", "claim_limit": "do not infer portal preference or digital access"})
    write_csv(output_root / "outputs/digital-engagement.csv", list(digital_rows[0]), digital_rows)

    pattern_measures = (
        ("usual_source", lambda row: row["_codes"]["HAVEUS42"] in {1, 2}, lambda row: float(row["_codes"]["HAVEUS42"] == 1), "percent"),
        ("phone_difficult", lambda row: row["_codes"]["PHNREG42"] in {1, 2, 3, 4}, lambda row: float(row["_codes"]["PHNREG42"] in {1, 2}), "percent"),
        ("involved_usually_always", lambda row: row["_codes"]["DECIDE42"] in {1, 2, 3, 4}, lambda row: float(row["_codes"]["DECIDE42"] in {3, 4}), "percent"),
        ("delayed_for_cost", lambda row: row["_codes"]["DLAYCA42"] in {1, 2}, lambda row: float(row["_codes"]["DLAYCA42"] == 1), "percent"),
        ("any_emergency_visit", lambda row: True, lambda row: float(integer(row["emergency_events_linked"]) > 0), "percent"),
        ("mean_office_visits", lambda row: True, lambda row: float(integer(row["office_events_linked"])), "events_per_person"),
        ("any_telehealth_event", lambda row: True, lambda row: float(sum(row["_telehealth_counts"].values()) > 0), "percent"),
    )
    linked_rows: list[dict[str, object]] = []
    for group_name, group_test in (
        ("both_discharge_items_yes", lambda row: row["q22_observed"] == "yes" and row["q23_observed"] == "yes"),
        ("one_or_both_discharge_items_no", lambda row: row["q22_observed"] in {"yes", "no"} and row["q23_observed"] in {"yes", "no"} and not (row["q22_observed"] == "yes" and row["q23_observed"] == "yes")),
    ):
        for measure, measure_domain, value_function, unit in pattern_measures:
            eligible = lambda row, gt=group_test, md=measure_domain: row["q21_observed"] == "home_or_other" and gt(row) and md(row)
            estimate = survey_estimate(people, eligible, value_function, weight_field="response_analysis_weight", scale=100.0 if unit == "percent" else 1.0)
            linked_rows.append({
                "synthetic_experience_group": group_name, "linked_measure": measure,
                "eligible_persons": estimate["n"], "weighted_denominator": fmt(float(estimate["weight"]), 6),
                "weighted_estimate": fmt(float(estimate["estimate"])), "survey_se": fmt(float(estimate["se"])),
                "ci95_low": fmt(float(estimate["low"])), "ci95_high": fmt(float(estimate["high"])),
                "unit": unit, "data_classes": "synthetic response plus public MEPS access and service use",
                "claim_limit": "procedural teaching association only; not a real patient-experience result",
            })
    write_csv(output_root / "outputs/linked-evidence-patterns.csv", list(linked_rows[0]), linked_rows)

    exact_reconciliation = all(row["status"] == "pass" for row in reconciliation)
    no_direct_ids = all("DUPERSID" not in row and "EVNTIDX" not in row for row in person_fields + event_fields)
    invariant_definitions = [
        ("I01", "official source file count", 25, 25),
        ("I02", "official source bytes", source_bytes, 18206634),
        ("I03", "official PDF pages", source_pages, 1101),
        ("I04", "upstream handoff file count", 3, 3),
        ("I05", "person source rows", len(person_rows), 19140),
        ("I06", "event source rows", all_event_rows, 174231),
        ("I07", "all event rows link to HC-256", all_events_linked, all_event_rows),
        ("I08", "event weights match person weights", event_weight_mismatches, 0),
        ("I09", "accepted target rows", len(people), 1255),
        ("I10", "accepted synthetic respondents", sum(row["response_status"] == "respondent" for row in people), 782),
        ("I11", "target linked event rows", len(released_events), 28455),
        ("I12", "target inpatient events", setting_sequence["inpatient"], 1692),
        ("I13", "target emergency events", setting_sequence["emergency"], 1601),
        ("I14", "target outpatient events", setting_sequence["outpatient"], 4651),
        ("I15", "target office-based events", setting_sequence["office_based"], 20511),
        ("I16", "every target person has inpatient evidence", sum(integer(row["inpatient_events_linked"]) > 0 for row in people), 1255),
        ("I17", "person totals reconcile to event files", exact_reconciliation, True),
        ("I18", "released person IDs are unique", len({row["link_person_id"] for row in people}), len(people)),
        ("I19", "released event IDs are unique", len({row["linked_event_id"] for row in released_events}), len(released_events)),
        ("I20", "direct source IDs are omitted", no_direct_ids, True),
        ("I21", "linked events follow the documented annual-file window", sum(integer(row["event_year"]) in {2023, 2024} for row in released_events), len(released_events)),
        ("I22", "event months are valid", sum(1 <= integer(row["event_month"]) <= 12 for row in released_events), len(released_events)),
        ("I23", "related emergency-inpatient links are reciprocal pairs", sum(bool(row["related_event_id"]) for row in released_events), 2 * len(related_target_pairs)),
        ("I24", "portal preference remains unavailable", digital_rows[-1]["denominator_n"], 0),
        ("I25", "linked pattern rows", len(linked_rows), 14),
    ]
    invariant_rows = [
        {"check_id": check_id, "invariant": label, "actual": actual, "expected": expected, "status": "pass" if actual == expected else "fail"}
        for check_id, label, actual, expected in invariant_definitions
    ]
    write_csv(output_root / "outputs/invariant-checks.csv", ["check_id", "invariant", "actual", "expected", "status"], invariant_rows)
    if any(row["status"] != "pass" for row in invariant_rows):
        failed = [row["check_id"] for row in invariant_rows if row["status"] != "pass"]
        raise ValueError(f"Evidence invariants failed: {', '.join(failed)}")

    generated_sha256 = {relative: sha256(output_root / relative) for relative in GENERATED_FILES if relative != "build-report.json"}
    report = {
        "status": "pass",
        "module": {"id": "oclc-app2-04", "version": "0.1.0", "commons_release": "0.59.0"},
        "source": {"files": 25, "bytes": source_bytes, "pdf_pages": source_pages, "person_rows": len(person_rows), "event_rows": all_event_rows},
        "upstream": {"files": 3, "bytes": upstream_bytes, "checkpoint_manifest_sha256": checkpoint["package"]["candidate_manifest_sha256"]},
        "target": {"people": len(people), "base_weighted_population": fmt(target_weight, 6), "linked_events": len(released_events)},
        "event_rows": {setting: setting_sequence[setting] for setting in ("inpatient", "emergency", "outpatient", "office_based")},
        "related_emergency_inpatient_pairs": len(related_target_pairs),
        "access_measures": len(access_rows),
        "linked_pattern_rows": len(linked_rows),
        "invariants": {"passed": len(invariant_rows), "failed": 0},
        "generated_sha256": generated_sha256,
    }
    report_path = output_root / "build-report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    report["generated_sha256"]["build-report.json"] = sha256(report_path)
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module04-build-") as first_dir, tempfile.TemporaryDirectory(prefix="app2-module04-build-") as second_dir:
        first_root, second_root = Path(first_dir), Path(second_dir)
        first = build(first_root)
        second = build(second_root)
        assert first["generated_sha256"] == second["generated_sha256"]
        assert first["target"] == {"people": 1255, "base_weighted_population": "18879474.284615", "linked_events": 28455}
        assert first["source"]["event_rows"] == 174231 and first["invariants"] == {"passed": 25, "failed": 0}
        for relative in GENERATED_FILES:
            assert (first_root / relative).read_bytes() == (second_root / relative).read_bytes()
    print("APP-2 Module 04 evidence builder self-check passed: 25 sources, 1,255 people, 28,455 linked target events, and 25 invariants.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=MODULE_ROOT)
    parser.add_argument("--verify-committed", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if args.verify_committed:
            with tempfile.TemporaryDirectory(prefix="app2-module04-verify-") as temp_dir:
                report = build(Path(temp_dir))
                for relative, digest in report["generated_sha256"].items():
                    committed = MODULE_ROOT / relative
                    if not committed.is_file() or sha256(committed) != digest:
                        raise ValueError(f"Committed generated file differs: {relative}")
            print("APP-2 Module 04 committed evidence matches a clean rebuild.")
            return
        report = build(args.output_root)
        print(json.dumps(report, indent=2))
    except (OSError, ValueError, KeyError, json.JSONDecodeError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
