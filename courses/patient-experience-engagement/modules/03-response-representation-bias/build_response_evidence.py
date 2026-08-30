"""Build the APP-2 Module 03 public frame and synthetic response evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
GENERATED_FILES = (
    "data/public/adult-inpatient-frame.csv",
    "data/synthetic/response-study.csv",
    "outputs/source-profile.csv",
    "outputs/public-saq-response.csv",
    "outputs/response-flow.csv",
    "outputs/subgroup-response.csv",
    "outputs/item-missingness.csv",
    "outputs/weight-cells.csv",
    "outputs/weight-diagnostics.csv",
    "outputs/estimate-comparison.csv",
    "outputs/invariant-checks.csv",
    "build-report.json",
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


def draw(generator_id: str, person_id: str, label: str) -> float:
    payload = f"{generator_id}|{person_id}|{label}".encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") / 2**64


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def load_categories() -> dict[tuple[str, int], str]:
    return {(row["field"], int(row["code"])): row["label"] for row in read_csv(MODULE_ROOT / "data/category-map.csv")}


def category(categories: dict[tuple[str, int], str], field: str, value: int | None) -> str:
    if value is None or value < 0:
        return "missing or inapplicable"
    return categories.get((field, value), f"unmapped code {value}")


def fields() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row in read_csv(MODULE_ROOT / "data/field-map.csv"):
        result.append({**row, "start": int(row["start"]), "end": int(row["end"])})
    return result


def parse_line(line: str, layout: list[dict[str, object]]) -> dict[str, object]:
    record: dict[str, object] = {}
    for field in layout:
        raw = line[int(field["start"]) - 1:int(field["end"])].strip()
        if field["kind"] == "text":
            value: object = raw
        elif not raw:
            value = None
        elif field["kind"] == "decimal":
            value = float(raw)
        else:
            value = int(raw)
        record[str(field["source_name"])] = value
    return record


def verify_sources() -> tuple[int, int]:
    rows = read_csv(MODULE_ROOT / "data/source-inventory.csv")
    if len(rows) != 5:
        raise ValueError("Source inventory must contain five official files")
    total = 0
    pages = 0
    for row in rows:
        path = MODULE_ROOT / row["relative_path"]
        if not path.is_file():
            raise FileNotFoundError(f"Missing official source: {row['relative_path']}")
        size = path.stat().st_size
        if size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise ValueError(f"Official source fingerprint changed: {row['relative_path']}")
        total += size
        pages += int(row["pages"] or 0)
    return total, pages


def public_rows(contract: dict[str, object]) -> tuple[list[dict[str, object]], dict[str, object]]:
    layout = fields()
    categories = load_categories()
    target = contract["target"]
    source_rows = positive_rows = line_width = 0
    selected: list[dict[str, object]] = []
    archive = MODULE_ROOT / "data/raw/h256dat.zip"
    with zipfile.ZipFile(archive) as bundle:
        if bundle.namelist() != ["h256.dat"]:
            raise ValueError("HC-256 archive must contain only h256.dat")
        with bundle.open("h256.dat") as handle:
            for raw in handle:
                line = raw.decode("ascii").rstrip("\r\n")
                source_rows += 1
                line_width = max(line_width, len(line))
                record = parse_line(line, layout)
                weight = float(record["PERWT24F"] or 0)
                if weight > 0:
                    positive_rows += 1
                age = record["AGE24X"]
                discharges = record["IPDIS24"]
                if weight <= 0 or age is None or int(age) < int(target["age_minimum"]) or discharges is None or int(discharges) < int(target["minimum_inpatient_discharges"]):
                    continue
                selected.append(record)
    selected.sort(key=lambda row: str(row["DUPERSID"]))
    released: list[dict[str, object]] = []
    for index, row in enumerate(selected, 1):
        age = int(row["AGE24X"])
        poverty = int(row["POVCAT24"])
        released.append({
            "frame_record_id": f"FRAME-{index:04d}",
            "data_class": "public_derived_meps_hc256",
            "age_band": "18-44" if age < 45 else ("45-64" if age < 65 else "65+"),
            "sex": category(categories, "SEX", row["SEX"]),
            "race_ethnicity": category(categories, "RACETHX", row["RACETHX"]),
            "other_language_at_home": category(categories, "OTHLGSPK", row["OTHLGSPK"]),
            "health_status": category(categories, "RTHLTH53", row["RTHLTH53"]),
            "poverty_category": category(categories, "POVCAT24", row["POVCAT24"]),
            "income_group": "lower income" if poverty in (1, 2, 3) else "middle or high income",
            "insurance_coverage": category(categories, "INSCOV24", row["INSCOV24"]),
            "proxy_status": category(categories, "PROXY24", row["PROXY24"]),
            "interview_language": category(categories, "INTVLANG", row["INTVLANG"]),
            "region": category(categories, "REGION24", row["REGION24"]),
            "panel": int(row["PANEL"]),
            "inpatient_discharges": int(row["IPDIS24"]),
            "base_person_weight": fmt(float(row["PERWT24F"]), 6),
            "variance_stratum": int(row["VARSTR"]),
            "variance_psu": int(row["VARPSU"]),
            "public_saq_status": category(categories, "SAQELIG", row["SAQELIG"]),
            "_person_id": row["DUPERSID"],
            "_age": age,
            "_other_language": row["OTHLGSPK"] == 1,
            "_poor_health": row["RTHLTH53"] in (4, 5),
            "_lower_income": poverty in (1, 2, 3),
            "_proxy": row["PROXY24"] == 2,
            "_saq_code": row["SAQELIG"],
        })
    profile = {"source_rows": source_rows, "positive_weight_rows": positive_rows, "line_width": line_width}
    return released, profile


def synthetic_rows(public: list[dict[str, object]], contract: dict[str, object]) -> list[dict[str, object]]:
    generator = contract["generator"]
    generator_id = generator["id"]
    mode_rule = generator["mode"]
    result: list[dict[str, object]] = []
    for row in public:
        person_id = str(row["_person_id"])
        mode_draw = draw(generator_id, person_id, "mode")
        mode = "mail" if mode_draw < mode_rule["mail_upper"] else ("phone" if mode_draw < mode_rule["phone_upper"] else "web")
        age65 = int(row["_age"]) >= 65
        other_language = bool(row["_other_language"])
        poor_health = bool(row["_poor_health"])
        lower_income = bool(row["_lower_income"])
        proxy = bool(row["_proxy"])

        rule = generator["another_facility_probability"]
        facility_probability = rule["intercept"] + rule["age_65_plus"] * age65 + rule["fair_or_poor_health"] * poor_health + rule["proxy"] * proxy
        home = draw(generator_id, person_id, "facility") >= facility_probability

        rule = generator["q22_yes_probability"]
        q22_probability = clamp(rule["intercept"] + rule["lower_income"] * lower_income + rule["other_language"] * other_language + rule["fair_or_poor_health"] * poor_health + rule["age_65_plus"] * age65, rule["minimum"], rule["maximum"])
        q22_yes = draw(generator_id, person_id, "q22") < q22_probability
        rule = generator["q23_yes_probability"]
        q23_probability = clamp(rule["intercept"] + rule["lower_income"] * lower_income + rule["other_language"] * other_language + rule["fair_or_poor_health"] * poor_health + rule["age_65_plus"] * age65, rule["minimum"], rule["maximum"])
        q23_yes = draw(generator_id, person_id, "q23") < q23_probability

        rule = generator["response_probability"]
        response_probability = rule["intercept"]
        response_probability += rule["age_18_44"] * (row["age_band"] == "18-44")
        response_probability += rule["age_65_plus"] * age65
        response_probability += rule["other_language"] * other_language
        response_probability += rule["fair_or_poor_health"] * poor_health
        response_probability += rule["lower_income"] * lower_income
        response_probability += rule["proxy"] * proxy
        response_probability += rule[mode]
        response_probability += rule["home_and_both_yes"] * (home and q22_yes and q23_yes)
        response_probability = clamp(response_probability, rule["minimum"], rule["maximum"])
        responded = draw(generator_id, person_id, "response") < response_probability

        q22_missing = q23_missing = False
        if responded and home:
            rule = generator["q22_missing_probability"]
            q22_missing = draw(generator_id, person_id, "m22") < rule["intercept"] + rule["other_language"] * other_language + rule["fair_or_poor_health"] * poor_health + rule["mail"] * (mode == "mail")
            rule = generator["q23_missing_probability"]
            q23_missing = draw(generator_id, person_id, "m23") < rule["intercept"] + rule["other_language"] * other_language + rule["lower_income"] * lower_income + rule["mail"] * (mode == "mail")

        q21_truth = "home_or_other" if home else "another_health_facility"
        q22_truth = ("yes" if q22_yes else "no") if home else "not_applicable"
        q23_truth = ("yes" if q23_yes else "no") if home else "not_applicable"
        if not responded:
            q21_observed = q22_observed = q23_observed = "not_observed_total_nonresponse"
        elif not home:
            q21_observed, q22_observed, q23_observed = q21_truth, "not_applicable", "not_applicable"
        else:
            q21_observed = q21_truth
            q22_observed = "missing" if q22_missing else q22_truth
            q23_observed = "missing" if q23_missing else q23_truth
        result.append({
            "frame_record_id": row["frame_record_id"],
            "data_class": "synthetic_procedural_response_overlay",
            "invited": "yes",
            "assigned_mode": mode,
            "q21_truth": q21_truth,
            "q22_truth": q22_truth,
            "q23_truth": q23_truth,
            "response_probability": fmt(response_probability, 6),
            "response_status": "respondent" if responded else "nonrespondent",
            "q21_observed": q21_observed,
            "q22_observed": q22_observed,
            "q23_observed": q23_observed,
            "response_cell": f"{row['age_band']}|{row['other_language_at_home']}|{row['income_group']}",
            "raw_response_factor": "",
            "bounded_response_factor": "",
            "analysis_weight": "",
            "_q22_yes": q22_yes,
            "_q23_yes": q23_yes,
        })
    return result


def apply_weights(public: list[dict[str, object]], synthetic: list[dict[str, object]], contract: dict[str, object]) -> list[dict[str, object]]:
    cells: dict[str, dict[str, float]] = defaultdict(lambda: {"frame_n": 0, "respondent_n": 0, "frame_weight": 0.0, "respondent_weight": 0.0})
    for frame, response in zip(public, synthetic, strict=True):
        cell = str(response["response_cell"])
        weight = float(frame["base_person_weight"])
        cells[cell]["frame_n"] += 1
        cells[cell]["frame_weight"] += weight
        if response["response_status"] == "respondent":
            cells[cell]["respondent_n"] += 1
            cells[cell]["respondent_weight"] += weight
    bounds = contract["weighting"]
    rows: list[dict[str, object]] = []
    for cell in sorted(cells):
        values = cells[cell]
        raw = values["frame_weight"] / values["respondent_weight"]
        bounded = clamp(raw, bounds["lower_bound"], bounds["upper_bound"])
        values["raw_factor"] = raw
        values["bounded_factor"] = bounded
        rows.append({
            "response_cell": cell,
            "frame_n": int(values["frame_n"]),
            "respondent_n": int(values["respondent_n"]),
            "frame_base_weight": fmt(values["frame_weight"], 6),
            "respondent_base_weight": fmt(values["respondent_weight"], 6),
            "raw_response_factor": fmt(raw, 8),
            "bounded_response_factor": fmt(bounded, 8),
            "bound_hit": "yes" if bounded != raw else "no",
            "support_flag": "limited_support" if values["frame_n"] < 30 or values["respondent_n"] < 30 else "adequate_for_descriptive_adjustment",
        })
    for frame, response in zip(public, synthetic, strict=True):
        values = cells[str(response["response_cell"])]
        response["raw_response_factor"] = fmt(values["raw_factor"], 8)
        response["bounded_response_factor"] = fmt(values["bounded_factor"], 8)
        if response["response_status"] == "respondent":
            response["analysis_weight"] = fmt(float(frame["base_person_weight"]) * values["bounded_factor"], 6)
    return rows


def subgroup_rows(public: list[dict[str, object]], synthetic: list[dict[str, object]]) -> list[dict[str, object]]:
    dimensions = (
        ("age_band", lambda p, s: p["age_band"]),
        ("sex", lambda p, s: p["sex"]),
        ("race_ethnicity", lambda p, s: p["race_ethnicity"]),
        ("other_language_at_home", lambda p, s: p["other_language_at_home"]),
        ("poverty_category", lambda p, s: p["poverty_category"]),
        ("health_status", lambda p, s: p["health_status"]),
        ("proxy_status", lambda p, s: p["proxy_status"]),
        ("interview_language", lambda p, s: p["interview_language"]),
        ("insurance_coverage", lambda p, s: p["insurance_coverage"]),
        ("region", lambda p, s: p["region"]),
        ("assigned_mode", lambda p, s: s["assigned_mode"]),
    )
    total_weight = sum(float(row["base_person_weight"]) for row in public)
    response_weight = sum(float(p["base_person_weight"]) for p, s in zip(public, synthetic, strict=True) if s["response_status"] == "respondent")
    total_rate = 100 * response_weight / total_weight
    output: list[dict[str, object]] = []
    for name, getter in dimensions:
        groups: dict[str, list[int]] = defaultdict(list)
        for index, (frame, response) in enumerate(zip(public, synthetic, strict=True)):
            groups[str(getter(frame, response))].append(index)
        for group in sorted(groups):
            indexes = groups[group]
            respondents = [index for index in indexes if synthetic[index]["response_status"] == "respondent"]
            frame_weight = sum(float(public[index]["base_person_weight"]) for index in indexes)
            respondent_weight = sum(float(public[index]["base_person_weight"]) for index in respondents)
            weighted_rate = 100 * respondent_weight / frame_weight
            output.append({
                "dimension": name,
                "group": group,
                "frame_n": len(indexes),
                "respondent_n": len(respondents),
                "unweighted_response_percent": fmt(100 * len(respondents) / len(indexes)),
                "frame_base_weight": fmt(frame_weight, 6),
                "respondent_base_weight": fmt(respondent_weight, 6),
                "base_weighted_response_percent": fmt(weighted_rate),
                "difference_from_total_pp": fmt(weighted_rate - total_rate),
                "support_flag": "limited_support" if len(indexes) < 30 or len(respondents) < 30 else "adequate_for_descriptive_audit",
            })
    return output


def item_rows(public: list[dict[str, object]], synthetic: list[dict[str, object]]) -> list[dict[str, object]]:
    dimensions = (
        ("total", lambda p, s: "all applicable respondents"),
        ("age_band", lambda p, s: p["age_band"]),
        ("other_language_at_home", lambda p, s: p["other_language_at_home"]),
        ("assigned_mode", lambda p, s: s["assigned_mode"]),
    )
    output: list[dict[str, object]] = []
    for item in ("q22", "q23"):
        for dimension, getter in dimensions:
            groups: dict[str, list[int]] = defaultdict(list)
            for index, (frame, response) in enumerate(zip(public, synthetic, strict=True)):
                if response["response_status"] == "respondent" and response["q21_truth"] == "home_or_other":
                    groups[str(getter(frame, response))].append(index)
            for group in sorted(groups):
                indexes = groups[group]
                missing = sum(synthetic[index][f"{item}_observed"] == "missing" for index in indexes)
                output.append({
                    "item": item.upper(),
                    "dimension": dimension,
                    "group": group,
                    "applicable_respondents": len(indexes),
                    "answered_n": len(indexes) - missing,
                    "missing_n": missing,
                    "missing_percent": fmt(100 * missing / len(indexes)),
                    "support_flag": "limited_support" if len(indexes) < 30 else "adequate_for_descriptive_audit",
                })
    return output


def estimate(public: list[dict[str, object]], synthetic: list[dict[str, object]], item: str, estimator: str) -> tuple[int, float]:
    numerator = denominator = 0.0
    count = 0
    for frame, response in zip(public, synthetic, strict=True):
        if response["q21_truth"] != "home_or_other":
            continue
        if estimator == "full_frame_truth":
            included = True
            weight = float(frame["base_person_weight"])
        else:
            included = response["response_status"] == "respondent" and response[f"{item}_observed"] in ("yes", "no")
            weight = 1.0 if estimator == "respondent_unweighted" else float(frame["base_person_weight"])
            if included and estimator == "respondent_response_adjusted":
                weight = float(response["analysis_weight"])
        if included:
            count += 1
            denominator += weight
            numerator += weight * bool(response[f"_{item}_yes"])
    return count, 100 * numerator / denominator


def estimate_rows(public: list[dict[str, object]], synthetic: list[dict[str, object]]) -> list[dict[str, object]]:
    estimators = (
        ("full_frame_truth", "PERWT24F across all synthetically applicable frame records"),
        ("respondent_unweighted", "equal weight among item-answering synthetic respondents"),
        ("respondent_base_weighted", "PERWT24F among item-answering synthetic respondents"),
        ("respondent_response_adjusted", "PERWT24F times bounded teaching response factor"),
    )
    item_values: dict[tuple[str, str], tuple[int, float]] = {}
    for item in ("q22", "q23"):
        for estimator, _ in estimators:
            item_values[(item, estimator)] = estimate(public, synthetic, item, estimator)
    output: list[dict[str, object]] = []
    for item in ("q22", "q23", "teaching_composite"):
        truth = item_values[(item, "full_frame_truth")][1] if item != "teaching_composite" else sum(item_values[(part, "full_frame_truth")][1] for part in ("q22", "q23")) / 2
        for estimator, definition in estimators:
            if item == "teaching_composite":
                count_text = f"Q22={item_values[('q22', estimator)][0]};Q23={item_values[('q23', estimator)][0]}"
                value = sum(item_values[(part, estimator)][1] for part in ("q22", "q23")) / 2
            else:
                count_text = str(item_values[(item, estimator)][0])
                value = item_values[(item, estimator)][1]
            bias = value - truth
            output.append({
                "measure": item.upper() if item != "teaching_composite" else item,
                "estimator": estimator,
                "answered_n": count_text,
                "estimate_percent": fmt(value),
                "truth_percent": fmt(truth),
                "bias_pp": fmt(bias),
                "absolute_bias_pp": fmt(abs(bias)),
                "weight_definition": definition,
                "claim_boundary": "synthetic procedural comparison only; not a real patient-experience estimate",
            })
    return output


def weight_diagnostics(public: list[dict[str, object]], synthetic: list[dict[str, object]]) -> list[dict[str, object]]:
    respondents = [(p, s) for p, s in zip(public, synthetic, strict=True) if s["response_status"] == "respondent"]
    rows: list[dict[str, object]] = []
    for label, getter in (
        ("respondent_base_weight", lambda p, s: float(p["base_person_weight"])),
        ("respondent_response_adjusted_weight", lambda p, s: float(s["analysis_weight"])),
    ):
        values = [getter(p, s) for p, s in respondents]
        total = sum(values)
        mean = total / len(values)
        sd = math.sqrt(sum((value - mean) ** 2 for value in values) / len(values))
        rows.append({
            "weight_set": label,
            "n": len(values),
            "sum": fmt(total, 6),
            "minimum": fmt(min(values), 6),
            "maximum": fmt(max(values), 6),
            "mean": fmt(mean, 6),
            "coefficient_of_variation": fmt(sd / mean),
            "kish_effective_n": fmt(total**2 / sum(value**2 for value in values)),
            "largest_weight_share_percent": fmt(100 * max(values) / total),
        })
    return rows


def build(target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    source_bytes, source_pages = verify_sources()
    contract = json.loads((MODULE_ROOT / "response-contract.json").read_text(encoding="utf-8"))
    public, profile = public_rows(contract)
    synthetic = synthetic_rows(public, contract)
    cell_rows = apply_weights(public, synthetic, contract)
    subgroup = subgroup_rows(public, synthetic)
    items = item_rows(public, synthetic)
    estimates = estimate_rows(public, synthetic)
    diagnostics = weight_diagnostics(public, synthetic)

    target.mkdir(parents=True)
    public_fields = [key for key in public[0] if not key.startswith("_")]
    synthetic_fields = [key for key in synthetic[0] if not key.startswith("_")]
    write_csv(target / GENERATED_FILES[0], public_fields, [{key: row[key] for key in public_fields} for row in public])
    write_csv(target / GENERATED_FILES[1], synthetic_fields, [{key: row[key] for key in synthetic_fields} for row in synthetic])

    target_weight = sum(float(row["base_person_weight"]) for row in public)
    respondents = [index for index, row in enumerate(synthetic) if row["response_status"] == "respondent"]
    respondent_weight = sum(float(public[index]["base_person_weight"]) for index in respondents)
    public_saq = [index for index, row in enumerate(public) if row["_saq_code"] in (1, 2)]
    public_saq_has = [index for index in public_saq if public[index]["_saq_code"] == 1]
    public_saq_weight = sum(float(public[index]["base_person_weight"]) for index in public_saq)
    public_saq_has_weight = sum(float(public[index]["base_person_weight"]) for index in public_saq_has)

    source_profile = [
        {"metric": "official_source_files", "value": 5, "unit": "files", "evidence": "source inventory and fingerprints"},
        {"metric": "official_source_bytes", "value": source_bytes, "unit": "bytes", "evidence": "five retained official files"},
        {"metric": "official_pdf_pages", "value": source_pages, "unit": "pages", "evidence": "HC-256 documentation and codebook"},
        {"metric": "source_rows", "value": profile["source_rows"], "unit": "people", "evidence": "full h256.dat"},
        {"metric": "fixed_width_characters", "value": profile["line_width"], "unit": "characters", "evidence": "maximum decoded record width"},
        {"metric": "positive_person_weight_rows", "value": profile["positive_weight_rows"], "unit": "people", "evidence": "PERWT24F greater than zero"},
        {"metric": "target_rows", "value": len(public), "unit": "people", "evidence": "age 18 plus positive weight and IPDIS24 at least one"},
        {"metric": "target_base_weighted_population", "value": fmt(target_weight, 6), "unit": "people", "evidence": "sum PERWT24F in target"},
        {"metric": "variance_strata_in_target", "value": len({row["variance_stratum"] for row in public}), "unit": "strata", "evidence": "distinct VARSTR"},
        {"metric": "panels_in_target", "value": len({row["panel"] for row in public}), "unit": "panels", "evidence": "distinct PANEL"},
    ]
    write_csv(target / "outputs/source-profile.csv", ["metric", "value", "unit", "evidence"], source_profile)
    public_saq_rows = [{
        "population": "adult positive-weight people with at least one 2024 inpatient discharge and SAQELIG 1 or 2",
        "eligible_n": len(public_saq),
        "has_saq_data_n": len(public_saq_has),
        "unweighted_has_data_percent": fmt(100 * len(public_saq_has) / len(public_saq)),
        "eligible_base_weight": fmt(public_saq_weight, 6),
        "has_data_base_weight": fmt(public_saq_has_weight, 6),
        "base_weighted_has_data_percent": fmt(100 * public_saq_has_weight / public_saq_weight),
        "interpretation": "real public MEPS SAQ data-status example; not HCAHPS response and not synthetic generator truth",
    }]
    write_csv(target / "outputs/public-saq-response.csv", list(public_saq_rows[0]), public_saq_rows)

    respondent_home = [index for index in respondents if synthetic[index]["q21_truth"] == "home_or_other"]
    q22_answered = [index for index in respondent_home if synthetic[index]["q22_observed"] in ("yes", "no")]
    q23_answered = [index for index in respondent_home if synthetic[index]["q23_observed"] in ("yes", "no")]
    flow_values = (
        ("public_analytic_target", list(range(len(public))), "MEPS public-derived adults with positive weight and at least one inpatient discharge"),
        ("teaching_sampling_frame", list(range(len(public))), "complete teaching frame by construction"),
        ("invited", list(range(len(public))), "every frame member invited once"),
        ("respondents", respondents, "synthetic total response"),
        ("respondent_q21_home", respondent_home, "synthetic Q22 and Q23 applicability among respondents"),
        ("q22_answered", q22_answered, "Q22 yes or no with item-specific denominator"),
        ("q23_answered", q23_answered, "Q23 yes or no with item-specific denominator"),
    )
    flow = []
    for stage, indexes, note in flow_values:
        flow.append({
            "stage": stage,
            "count": len(indexes),
            "percent_of_frame": fmt(100 * len(indexes) / len(public)),
            "base_weighted_population": fmt(sum(float(public[index]["base_person_weight"]) for index in indexes), 6),
            "notes": note,
        })
    write_csv(target / "outputs/response-flow.csv", list(flow[0]), flow)
    write_csv(target / "outputs/subgroup-response.csv", list(subgroup[0]), subgroup)
    write_csv(target / "outputs/item-missingness.csv", list(items[0]), items)
    write_csv(target / "outputs/weight-cells.csv", list(cell_rows[0]), cell_rows)
    write_csv(target / "outputs/weight-diagnostics.csv", list(diagnostics[0]), diagnostics)
    write_csv(target / "outputs/estimate-comparison.csv", list(estimates[0]), estimates)

    expected = contract["expected_reference"]
    estimate_lookup = {(row["measure"], row["estimator"]): float(row["absolute_bias_pp"]) for row in estimates}
    improved = all(estimate_lookup[(measure, "respondent_response_adjusted")] < estimate_lookup[(measure, "respondent_base_weighted")] for measure in ("Q22", "Q23", "teaching_composite"))
    residual = all(estimate_lookup[(measure, "respondent_response_adjusted")] > 0 for measure in ("Q22", "Q23", "teaching_composite"))
    checks = [
        ("I01", "official source suite fingerprinted", "5 files", f"{5} files", True),
        ("I02", "archive contains only h256.dat", "h256.dat", "h256.dat", True),
        ("I03", "full source row count", contract["target"]["source_rows"], profile["source_rows"], profile["source_rows"] == contract["target"]["source_rows"]),
        ("I04", "fixed-width record length", 4690, profile["line_width"], profile["line_width"] == 4690),
        ("I05", "positive person-weight row count", contract["target"]["positive_person_weight_rows"], profile["positive_weight_rows"], profile["positive_weight_rows"] == contract["target"]["positive_person_weight_rows"]),
        ("I06", "target and frame count", contract["target"]["target_rows"], len(public), len(public) == contract["target"]["target_rows"]),
        ("I07", "target weighted population", fmt(contract["target"]["target_weighted_population"], 6), fmt(target_weight, 6), abs(target_weight - contract["target"]["target_weighted_population"]) < 0.000001),
        ("I08", "frame identifiers unique", len(public), len({row["frame_record_id"] for row in public}), len(public) == len({row["frame_record_id"] for row in public})),
        ("I09", "every frame record invited", len(public), sum(row["invited"] == "yes" for row in synthetic), all(row["invited"] == "yes" for row in synthetic)),
        ("I10", "constructed frame coverage", "100.00000000", fmt(100 * len(synthetic) / len(public)), len(synthetic) == len(public)),
        ("I11", "synthetic respondents", expected["respondents"], len(respondents), len(respondents) == expected["respondents"]),
        ("I12", "full-frame Q21 home truth", expected["full_frame_q21_home"], sum(row["q21_truth"] == "home_or_other" for row in synthetic), sum(row["q21_truth"] == "home_or_other" for row in synthetic) == expected["full_frame_q21_home"]),
        ("I13", "respondent Q21 home", expected["respondent_q21_home"], len(respondent_home), len(respondent_home) == expected["respondent_q21_home"]),
        ("I14", "Q22 answered count", expected["q22_answered"], len(q22_answered), len(q22_answered) == expected["q22_answered"]),
        ("I15", "Q23 answered count", expected["q23_answered"], len(q23_answered), len(q23_answered) == expected["q23_answered"]),
        ("I16", "nonrespondents have no observed item", "all unobserved", "all unobserved", all(row["q22_observed"] == row["q23_observed"] == "not_observed_total_nonresponse" for row in synthetic if row["response_status"] == "nonrespondent")),
        ("I17", "Q21 another facility preserves not applicable", "all not applicable", "all not applicable", all(row["q22_truth"] == row["q23_truth"] == "not_applicable" for row in synthetic if row["q21_truth"] == "another_health_facility")),
        ("I18", "response cell count", expected["response_cells"], len(cell_rows), len(cell_rows) == expected["response_cells"]),
        ("I19", "response factor cap hits", expected["response_factor_cap_hits"], sum(row["bound_hit"] == "yes" for row in cell_rows), sum(row["bound_hit"] == "yes" for row in cell_rows) == expected["response_factor_cap_hits"]),
        ("I20", "bounded factors do not exceed 3", "maximum 3.0", max(float(row["bounded_response_factor"]) for row in cell_rows), max(float(row["bounded_response_factor"]) for row in cell_rows) <= 3),
        ("I21", "bounded adjustment improves both items and composite", "all improve", "all improve" if improved else "not all improve", improved),
        ("I22", "residual known-truth bias remains visible", "all nonzero", "all nonzero" if residual else "zero found", residual),
        ("I23", "public SAQ eligible and has-data counts", f"{expected['public_saq_eligible']}/{expected['public_saq_has_data']}", f"{len(public_saq)}/{len(public_saq_has)}", len(public_saq) == expected["public_saq_eligible"] and len(public_saq_has) == expected["public_saq_has_data"]),
    ]
    invariant_rows = [{"check_id": check_id, "check": name, "expected": expected_value, "actual": actual, "status": "pass" if passed else "fail"} for check_id, name, expected_value, actual, passed in checks]
    write_csv(target / "outputs/invariant-checks.csv", list(invariant_rows[0]), invariant_rows)
    failed = [row["check_id"] for row in invariant_rows if row["status"] != "pass"]
    if failed:
        raise ValueError(f"Evidence invariants failed: {', '.join(failed)}")

    report = {
        "status": "pass",
        "source": {"files": 5, "bytes": source_bytes, "pdf_pages": source_pages, **profile},
        "target": {"rows": len(public), "base_weighted_population": fmt(target_weight, 6), "frame_coverage_percent": 100.0},
        "synthetic_response": {
            "respondents": len(respondents), "unweighted_response_percent": fmt(100 * len(respondents) / len(public)),
            "base_weighted_response_percent": fmt(100 * respondent_weight / target_weight),
            "full_frame_q21_home": sum(row["q21_truth"] == "home_or_other" for row in synthetic),
            "respondent_q21_home": len(respondent_home), "q22_answered": len(q22_answered), "q23_answered": len(q23_answered),
        },
        "public_saq": {"eligible": len(public_saq), "has_data": len(public_saq_has), "unweighted_has_data_percent": fmt(100 * len(public_saq_has) / len(public_saq)), "base_weighted_has_data_percent": fmt(100 * public_saq_has_weight / public_saq_weight)},
        "weighting": {"cells": len(cell_rows), "cap": contract["weighting"]["upper_bound"], "cap_hits": sum(row["bound_hit"] == "yes" for row in cell_rows)},
        "estimates": {row["measure"]: {candidate["estimator"]: {"estimate_percent": candidate["estimate_percent"], "bias_pp": candidate["bias_pp"]} for candidate in estimates if candidate["measure"] == row["measure"]} for row in estimates},
        "invariant_checks": len(invariant_rows),
    }
    (target / "build-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    report["generated_files"] = len(GENERATED_FILES)
    report["generated_bytes"] = sum((target / relative).stat().st_size for relative in GENERATED_FILES)
    report["generated_sha256"] = {relative: sha256(target / relative) for relative in GENERATED_FILES}
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module03-evidence-") as temp_dir:
        base = Path(temp_dir)
        first, second = base / "first", base / "second"
        one = build(first)
        two = build(second)
        assert one["generated_sha256"] == two["generated_sha256"]
        assert one["synthetic_response"]["respondents"] == 782
        assert one["weighting"]["cap_hits"] == 1
        try:
            build(first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Evidence builder overwrote an existing target")
    print("APP-2 Module 03 evidence builder self-check passed: 1,255 frame rows, 782 respondents, and byte-identical outputs.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.target:
            print(json.dumps(build(args.target), indent=2))
        else:
            parser.error("--target is required unless --self-check is used")
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
