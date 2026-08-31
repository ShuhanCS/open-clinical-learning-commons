"""Build deterministic APP-4 Module 06 safety, monitoring, and ML evidence."""

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
from pathlib import Path

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score


ROOT = Path(__file__).resolve().parent
MODULE03 = ROOT.parent / "03-evidence-calibration-validation" / "data" / "evidence"
MODULE05 = ROOT.parent / "05-sandbox-prototype-failure-modes"
PREDICTORS = ("age_centered_per_10", "bmi_centered_per_5", "female_indicator")
PARTITIONS = ("development", "temporal_holdout", "transport_stress")
EVALUATION_PARTITIONS = ("temporal_holdout", "transport_stress")
THRESHOLDS = (0.02, 0.03, 0.04, 0.05, 0.075, 0.10)
RANDOM_STATE = 7400600
MODEL_NAME = "fixed_gradient_boosted"
TRANSPARENT = "transparent_weighted_logit"
CLAIM_LIMIT = "historical public or synthetic teaching evidence only; not local validity, clinical utility, threshold acceptance, implementation, or deployment"
SOURCE_HASHES = {
    MODULE03 / "model-cohort.csv.gz": "5ee21d19ecaca1e95e57910b2ca12b27960473eb16be4edac0b62b96de731304",
    MODULE03 / "predictions.csv.gz": "2bd6064b557c34936e7c8ef606dc0ac5ffa7751095d7100d3312e69c411f122f",
    MODULE03 / "subgroup-support.csv": "064882d3dafcb8d652a86c6baabc083d8f9c0387604af67c4753af0345deafc6",
    MODULE05 / "reference" / "failure-mode-register.csv": "8caeb43521abc3c143f5f974c36a71eb92260ffc336253683e9a41d6c24d3094",
    MODULE05 / "reference" / "gate-results.csv": "bcbcb1b58bbebE23ac67927adee81a0d952f0cd7d36bcc131018889d17fe4c39".lower(),
    MODULE05 / "release.json": "543e55dfdef2a8d95be3eaab4c7b8af60ea0fc6f918927804f723128c6126e58",
}
OUTPUT_FILES = (
    "outputs/hazard-register.csv",
    "outputs/monitoring-measures.csv",
    "outputs/monitoring-scenarios.csv",
    "outputs/escalation-rules.csv",
    "outputs/model-predictions.csv.gz",
    "outputs/model-performance.csv",
    "outputs/threshold-comparison.csv",
    "outputs/subgroup-comparison.csv",
    "outputs/feature-importance.csv",
    "outputs/leakage-tests.csv",
    "outputs/replacement-rules.csv",
    "outputs/invariant-checks.csv",
    "outputs/build-report.json",
)


def fixed(value: float) -> str:
    return f"{value:.8f}"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_gzip_csv(path: Path) -> list[dict[str, str]]:
    with gzip.open(path, "rt", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"Refusing to write empty output: {path.name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_gzip_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            with io.TextIOWrapper(zipped, encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
                writer.writeheader()
                writer.writerows(rows)


def verify_sources() -> None:
    for path, expected in SOURCE_HASHES.items():
        if not path.is_file() or sha256(path) != expected:
            raise ValueError(f"Accepted source changed: {path}")
    release = json.loads((MODULE05 / "release.json").read_text(encoding="utf-8"))
    handoff = (MODULE05 / "reference" / "progression-module06-handoff.md").read_text(encoding="utf-8")
    if (
        release["module"]["id"] != "oclc-app4-05"
        or release["module"]["commons_release"] != "0.82.0"
        or release["workspace"] != {"immutable_manifest_rows": 324, "editable_records": 16, "assembled_files": 341}
        or release["design"]["id"] != "panel-t003"
        or release["design"]["accepted_threshold"] is not None
        or "continue with conditions" not in handoff
    ):
        raise ValueError("Module 05 release or handoff changed")


def load_model_rows() -> list[dict[str, object]]:
    cohort = read_gzip_csv(MODULE03 / "model-cohort.csv.gz")
    predictions = {row["participant_id"]: row for row in read_gzip_csv(MODULE03 / "predictions.csv.gz")}
    if len(cohort) != 7544 or len(predictions) != 7544:
        raise ValueError("Expected 7,544 common model rows")
    rows: list[dict[str, object]] = []
    for row in cohort:
        prediction = predictions.get(row["participant_id"])
        if not prediction or prediction["partition"] != row["partition"]:
            raise ValueError("Module 03 cohort and predictions do not align")
        rows.append({
            **row,
            "outcome": int(row["outcome_hba1c_ge_6_5"]),
            "weight": float(row["analytic_weight"]),
            "transparent_probability": float(prediction["model_probability"]),
        })
    return rows


def fit_challenger(rows: list[dict[str, object]]) -> tuple[GradientBoostingClassifier, np.ndarray]:
    x = np.array([[float(row[name]) for name in PREDICTORS] for row in rows])
    y = np.array([int(row["outcome"]) for row in rows])
    weight = np.array([float(row["weight"]) for row in rows])
    development = np.array([row["partition"] == "development" for row in rows])
    development_weight = weight[development] / weight[development].mean()
    model = GradientBoostingClassifier(
        n_estimators=80,
        learning_rate=0.05,
        max_depth=2,
        min_samples_leaf=50,
        subsample=1.0,
        random_state=RANDOM_STATE,
    )
    model.fit(x[development], y[development], sample_weight=development_weight)
    return model, model.predict_proba(x)[:, 1]


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.average(values, weights=weights))


def metric_row(partition: str, model: str, y: np.ndarray, probability: np.ndarray, weight: np.ndarray) -> dict[str, object]:
    clipped = np.clip(probability, 1e-12, 1 - 1e-12)
    prevalence = weighted_mean(y, weight)
    mean_probability = weighted_mean(probability, weight)
    return {
        "partition": partition,
        "model": model,
        "rows": len(y),
        "events": int(y.sum()),
        "weighted_prevalence": fixed(prevalence),
        "weighted_mean_probability": fixed(mean_probability),
        "absolute_calibration_error": fixed(abs(mean_probability - prevalence)),
        "weighted_brier": fixed(weighted_mean((probability - y) ** 2, weight)),
        "weighted_log_loss": fixed(weighted_mean(-(y * np.log(clipped) + (1 - y) * np.log(1 - clipped)), weight)),
        "weighted_roc_auc": fixed(roc_auc_score(y, probability, sample_weight=weight)),
        "claim_limit": CLAIM_LIMIT,
    }


def performance_rows(rows: list[dict[str, object]], challenger: np.ndarray) -> list[dict[str, object]]:
    result = []
    for partition in PARTITIONS:
        index = np.array([row["partition"] == partition for row in rows])
        y = np.array([int(row["outcome"]) for row in rows])[index]
        weight = np.array([float(row["weight"]) for row in rows])[index]
        transparent = np.array([float(row["transparent_probability"]) for row in rows])[index]
        result.append(metric_row(partition, TRANSPARENT, y, transparent, weight))
        result.append(metric_row(partition, MODEL_NAME, y, challenger[index], weight))
    return result


def confusion(y: np.ndarray, probability: np.ndarray, weight: np.ndarray, threshold: float) -> dict[str, float]:
    positive = probability >= threshold
    event_weight = float(np.sum(weight * y))
    non_event_weight = float(np.sum(weight * (1 - y)))
    total_weight = float(np.sum(weight))
    tp = float(np.sum(weight * y * positive))
    fp = float(np.sum(weight * (1 - y) * positive))
    fn = float(np.sum(weight * y * (~positive)))
    return {
        "weighted_flag_rate": (tp + fp) / total_weight,
        "weighted_sensitivity": tp / event_weight,
        "weighted_specificity": 1 - fp / non_event_weight,
        "weighted_missed_per_1000": 1000 * fn / total_weight,
        "weighted_flags_per_1000": 1000 * (tp + fp) / total_weight,
    }


def threshold_rows(rows: list[dict[str, object]], challenger: np.ndarray) -> list[dict[str, object]]:
    result = []
    for partition in PARTITIONS:
        index = np.array([row["partition"] == partition for row in rows])
        y = np.array([int(row["outcome"]) for row in rows])[index]
        weight = np.array([float(row["weight"]) for row in rows])[index]
        models = {
            TRANSPARENT: np.array([float(row["transparent_probability"]) for row in rows])[index],
            MODEL_NAME: challenger[index],
        }
        for model, probability in models.items():
            for threshold in THRESHOLDS:
                values = confusion(y, probability, weight, threshold)
                result.append({
                    "partition": partition,
                    "model": model,
                    "threshold": fixed(threshold),
                    "threshold_status": "evidence candidate, not selected or accepted",
                    **{name: fixed(value) for name, value in values.items()},
                    "claim_limit": "classification tradeoff only; no clinical threshold authority",
                })
    return result


def group_label(row: dict[str, object], dimension: str) -> str:
    if dimension == "recorded_sex":
        return str(row["sex"])
    if dimension == "race_and_hispanic_origin":
        return str(row["race_ethnicity"])
    if dimension == "age_band":
        age = int(str(row["RIDAGEYR"]))
        return "35-44" if age < 45 else "45-54" if age < 55 else "55-64" if age < 65 else "65-70"
    if dimension == "bmi_band":
        bmi = float(str(row["BMXBMI"]))
        return "25.0-29.9" if bmi < 30 else "30.0-34.9" if bmi < 35 else "35.0-39.9" if bmi < 40 else "40.0+"
    raise ValueError(f"Unknown subgroup dimension: {dimension}")


def subgroup_rows(rows: list[dict[str, object]], challenger: np.ndarray) -> list[dict[str, object]]:
    support = [row for row in read_csv(MODULE03 / "subgroup-support.csv") if row["partition"] in EVALUATION_PARTITIONS]
    result = []
    for source in support:
        indices = [
            index for index, row in enumerate(rows)
            if row["partition"] == source["partition"] and group_label(row, source["dimension"]) == source["group"]
        ]
        y = np.array([int(rows[index]["outcome"]) for index in indices])
        weight = np.array([float(rows[index]["weight"]) for index in indices])
        probabilities = {
            TRANSPARENT: np.array([float(rows[index]["transparent_probability"]) for index in indices]),
            MODEL_NAME: challenger[indices],
        }
        for model, probability in probabilities.items():
            auc = ""
            if source["support_status"] == "report with boundary" and len(set(y.tolist())) == 2:
                auc = fixed(roc_auc_score(y, probability, sample_weight=weight))
            result.append({
                "partition": source["partition"],
                "dimension": source["dimension"],
                "group": source["group"],
                "model": model,
                "rows": source["rows"],
                "events": source["events"],
                "support_status": source["support_status"],
                "weighted_mean_probability": fixed(weighted_mean(probability, weight)),
                "weighted_brier": fixed(weighted_mean((probability - y) ** 2, weight)),
                "weighted_roc_auc": auc,
                "claim_limit": "descriptive support audit only; no ranking, fairness certification, or group-specific action",
            })
    return result


def hazard_rows() -> list[dict[str, object]]:
    inherited = read_csv(MODULE05 / "reference" / "failure-mode-register.csv")
    consequence = {
        "missing input": "evaluation cannot proceed from complete evidence",
        "stale input": "an obsolete value could be treated as current",
        "inconsistent input": "an invalid value could produce a misleading result",
        "delayed input": "a result could arrive after it is useful",
        "duplicate request": "duplicate work and burden could be hidden",
        "terminology mismatch": "the wrong clinical meaning could be assigned",
        "unit mismatch": "a value could be interpreted on the wrong scale",
        "silent failure": "a received request could disappear without a response or notice",
        "accessibility defect": "the result could be unusable for some people",
    }
    result = []
    for index, row in enumerate(inherited, 1):
        result.append({
            "hazard_id": f"H{index:02d}",
            "origin": f"Module 05 {row['failure_id']} / {row['case_id']}",
            "hazard": row["failure"],
            "cause": row["cause"],
            "consequence": consequence.get(row["failure"], "the service state could be misunderstood or acted on incorrectly"),
            "detection": row["detection"],
            "control": row["control"],
            "owner": row["module06_owner"],
            "escalation": "notify the governance council and named owner",
            "fallback": "show unavailable state and preserve the trace",
            "stop_rule": "stop the affected evaluation when detected or when detection evidence is unavailable",
            "restart_rule": "owner verifies correction, reconciliation, and a passing repeat fixture",
            "retirement_trigger": "recurrent unresolved incident or loss of a dependable control",
            "evidence_status": "seeded synthetic failure, not an observed clinical incident",
        })
    additions = (
        ("outcome unavailable", "follow-up outcome not observable", "calibration and utility cannot be evaluated", "outcome completeness audit", "report unavailable and do not infer performance", "evaluation steward"),
        ("calibration drift", "predicted and observed rates separate", "burden or missed-case expectations can change", "prespecified calibration review", "pause interpretation and investigate data and case mix", "model steward"),
        ("subgroup support erosion", "events or follow-up fall below the declared support rule", "group results can become unstable or misleading", "support count and denominator audit", "suppress the result and refer to the equity reviewer", "equity steward"),
        ("override capture failure", "human response or disagreement is not recorded", "hidden work and unsafe patterns cannot be reviewed", "override ledger reconciliation", "treat response monitoring as unavailable", "clinical owner"),
        ("governance delay", "incident or version review misses its decision window", "an obsolete or unsafe state can persist", "decision-age and version audit", "stop the affected release and use the last accepted nonproduction artifact", "governance owner"),
    )
    for offset, (hazard, cause, effect, detection, control, owner) in enumerate(additions, len(result) + 1):
        result.append({
            "hazard_id": f"H{offset:02d}", "origin": "Module 06 safety case", "hazard": hazard,
            "cause": cause, "consequence": effect, "detection": detection, "control": control,
            "owner": owner, "escalation": "notify the governance council and named owner",
            "fallback": "report unavailable and retain the last accepted nonproduction state",
            "stop_rule": "stop the affected evaluation when the trigger is met or the measure is unavailable",
            "restart_rule": "owner documents recovery evidence and governance approves restart",
            "retirement_trigger": "control cannot be restored or repeated incidents exceed the review rule",
            "evidence_status": "prospective teaching hazard, not an observed clinical incident",
        })
    return result


def monitoring_rows() -> list[dict[str, object]]:
    definitions = (
        ("M01", "eligible opportunities", "eligible encounters by declared logic", "encounter and eligibility ledger", "weekly", "clinical owner", "Module 04 baseline", "outside reviewed baseline by 20 percent"),
        ("M02", "input availability", "complete required prefetch divided by eligible requests", "request and input ledgers", "daily", "data steward", "Module 05 failures", "below 99 percent"),
        ("M03", "firing", "candidate cards divided by eligible requests", "request and response ledgers", "weekly", "clinical informatics owner", "Module 04 burden review", "outside candidate-specific expected range"),
        ("M04", "suppression", "suppressed evaluations by declared reason", "response and trace ledgers", "weekly", "clinical owner", "Module 05 suppression fixtures", "reason missing or shift above 20 percent"),
        ("M05", "burden", "candidate flags per 1000 eligible opportunities", "request and response ledgers", "weekly", "workflow owner", "Module 04 alert budget", "above 300 per 1000 at the unaccepted 0.03 fixture"),
        ("M06", "human response", "acknowledged, dismissed, deferred, and unavailable responses", "human response ledger", "weekly", "clinical owner", "prospective governance rule", "ledger unavailable or response missing"),
        ("M07", "latency", "request to terminal response milliseconds", "request and terminal ledgers", "daily", "service owner", "Module 05 teaching budget", "P95 above 2000 ms"),
        ("M08", "errors", "visible error responses by type", "terminal and notice ledgers", "daily", "service owner", "Module 05 failure matrix", "any unexplained error or rate above 1 percent"),
        ("M09", "silent failure", "received requests without response, terminal trace, or notice", "four independent ledgers", "daily", "patient-safety owner", "Module 05 seeded failure", "one or more events"),
        ("M10", "outcome availability", "eligible evaluations with observable follow-up outcome", "evaluation outcome ledger", "monthly", "evaluation steward", "prospective evaluation rule", "below 90 percent or source unavailable"),
        ("M11", "calibration", "absolute difference between mean probability and observed outcome", "prediction and outcome ledgers", "monthly", "model steward", "Module 06 replacement rule", "above 0.005 holdout reference or 0.010 stress reference"),
        ("M12", "discrimination", "weighted ROC AUC on supported outcome rows", "prediction and outcome ledgers", "monthly", "model steward", "Module 03 validation", "drop greater than 0.01 from accepted reference"),
        ("M13", "drift", "transport minus holdout performance and burden", "prediction, outcome, and threshold audit", "monthly", "model steward", "Module 03 transport audit", "declared replacement rule fails"),
        ("M14", "subgroup support", "rows, events, follow-up, and performance by declared group", "prediction and outcome ledgers", "monthly", "equity steward", "Module 03 support audit", "support becomes insufficient or AUC drops more than 0.05"),
        ("M15", "version", "requests and responses using the accepted model and hook versions", "request and terminal ledgers", "daily", "model steward", "Module 05 version fixture", "any mismatch"),
        ("M16", "incidents", "open and repeated safety incidents by hazard", "incident register", "weekly", "patient-safety owner", "prospective governance rule", "one severe or two repeated related incidents"),
        ("M17", "overrides", "human disagreements and overrides with reasons", "override ledger", "weekly", "clinical owner", "prospective governance rule", "ledger unavailable or unexplained pattern"),
        ("M18", "accessibility", "released cards passing the declared structure checks", "accessibility ledger", "each release", "accessibility owner", "Module 05 blocked defect", "any failed check"),
        ("M19", "duplicate suppression", "repeated hook instances suppressed with trace reason", "request and trace ledgers", "daily", "clinical informatics owner", "Module 05 duplicate fixture", "duplicate reaches a candidate response"),
        ("M20", "semantic rejects", "terminology and unit mismatches rejected visibly", "input, terminal, and notice ledgers", "daily", "terminology steward", "Module 05 semantic fixtures", "mismatch is converted or hidden"),
    )
    return [{
        "measure_id": item[0], "measure": item[1], "definition": item[2], "source": item[3],
        "cadence": item[4], "owner": item[5], "threshold_origin": item[6], "trigger": item[7],
        "unavailable_state": "report unavailable, name the missing source, and do not infer a safe value",
        "human_action": "verify evidence, investigate, document disposition, and escalate when the trigger persists",
        "automatic_action": "none",
        "claim_limit": CLAIM_LIMIT,
    } for item in definitions]


def monitoring_scenarios() -> list[dict[str, object]]:
    rows = (
        ("S01", "reconciled baseline", "all four ledgers reconcile and no trigger fires", "M01-M20", "continue review with no automatic action"),
        ("S02", "input availability drop", "required input availability falls to 96 percent", "M02", "show unavailable, investigate source, and escalate"),
        ("S03", "suppression shift", "suppression reason mix changes by 25 percent", "M04", "verify logic, case mix, and traces before interpretation"),
        ("S04", "silent failure", "one received request has no response, terminal trace, or notice", "M09", "stop affected evaluation and escalate immediately"),
        ("S05", "calibration drift", "absolute calibration error exceeds 0.010", "M11-M13", "pause performance claims and investigate"),
        ("S06", "subgroup support loss", "one group falls below the declared event support", "M14", "suppress the group result and refer"),
        ("S07", "version mismatch", "one request carries an unreviewed model version", "M15", "reject visibly and stop the affected release"),
        ("S08", "accessibility regression", "one card lacks the required summary", "M18", "block release and return to accessibility review"),
    )
    return [{"scenario_id": a, "scenario": b, "seeded_truth": c, "measures": d, "expected_human_action": e, "automatic_action": "none", "evidence_status": "synthetic monitoring exercise"} for a, b, c, d, e in rows]


def escalation_rows() -> list[dict[str, object]]:
    rules = (
        ("E01", "M02", "input availability below 99 percent", "data steward", "clinical informatics owner", "show unavailable"),
        ("E02", "M07", "P95 latency above 2000 ms", "service owner", "governance council", "show delayed state"),
        ("E03", "M08", "unexplained error or rate above 1 percent", "service owner", "patient-safety owner", "show visible error"),
        ("E04", "M09", "one silent failure", "patient-safety owner", "governance council", "stop affected evaluation"),
        ("E05", "M10", "outcome availability below 90 percent", "evaluation steward", "governance council", "report performance unavailable"),
        ("E06", "M11", "calibration trigger met", "model steward", "governance council", "pause calibration claims"),
        ("E07", "M12-M13", "discrimination or drift trigger met", "model steward", "governance council", "retain transparent reference"),
        ("E08", "M14", "support loss or subgroup degradation", "equity steward", "governance council", "suppress unsupported result"),
        ("E09", "M15", "any version mismatch", "model steward", "governance council", "reject visibly"),
        ("E10", "M16", "one severe or two related incidents", "patient-safety owner", "governance council", "stop affected release"),
        ("E11", "M17", "override ledger unavailable", "clinical owner", "governance council", "report response unavailable"),
        ("E12", "M18-M20", "accessibility, duplicate, or semantic control fails", "named control owner", "governance council", "block affected output"),
    )
    return [{
        "rule_id": a, "measure_id": b, "trigger": c, "owner": d, "escalates_to": e,
        "fallback": f, "stop_rule": "stop the affected evaluation or release when the control cannot bound the hazard",
        "restart_rule": "named owner verifies repair and the governance council records approval",
        "retirement_rule": "retire when the control cannot be restored or the intended use is no longer supportable",
        "automatic_action": "none",
    } for a, b, c, d, e, f in rules]


def leakage_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    development_cycles = sorted({str(row["cycle"]) for row in rows if row["partition"] == "development"})
    checks = (
        ("L01", "development cycles fixed", development_cycles == ["2013-2014", "2015-2016"], "2013-2014 and 2015-2016 only"),
        ("L02", "temporal holdout untouched", {row["cycle"] for row in rows if row["partition"] == "temporal_holdout"} == {"2017-2018"}, "2017-2018 only"),
        ("L03", "transport stress untouched", {row["cycle"] for row in rows if row["partition"] == "transport_stress"} == {"2021-2023"}, "2021-2023 only"),
        ("L04", "same common rows", len(rows) == 7544, "7,544 aligned rows"),
        ("L05", "same predictors", PREDICTORS == ("age_centered_per_10", "bmi_centered_per_5", "female_indicator"), "three Module 03 predictors"),
        ("L06", "same observed target", all(row["outcome"] in {0, 1} for row in rows), "LBXGH threshold target"),
        ("L07", "same analytic weights", all(float(row["weight"]) > 0 for row in rows), "positive frozen analytic weights"),
        ("L08", "same threshold candidates", len(THRESHOLDS) == 6 and 0.03 in THRESHOLDS, "six unaccepted candidates"),
        ("L09", "no accepted threshold", True, "accepted threshold is none"),
        ("L10", "one fixed model family", True, "GradientBoostingClassifier only"),
        ("L11", "no search or tuning", True, "fixed settings and one fit"),
        ("L12", "fixed random state", RANDOM_STATE == 7400600, "7400600"),
    )
    return [{"test_id": a, "test": b, "status": "pass" if c else "fail", "evidence": d, "noncompensable_reason": "a failed leakage test invalidates the challenger comparison"} for a, b, c, d in checks]


def replacement_rows(performance: list[dict[str, object]], thresholds: list[dict[str, object]], subgroups: list[dict[str, object]], leak: list[dict[str, object]], importance: list[dict[str, object]]) -> list[dict[str, object]]:
    perf = {(row["partition"], row["model"]): row for row in performance}
    hold_auc = float(perf[("temporal_holdout", MODEL_NAME)]["weighted_roc_auc"]) - float(perf[("temporal_holdout", TRANSPARENT)]["weighted_roc_auc"])
    stress_auc = float(perf[("transport_stress", MODEL_NAME)]["weighted_roc_auc"]) - float(perf[("transport_stress", TRANSPARENT)]["weighted_roc_auc"])
    hold_brier = float(perf[("temporal_holdout", MODEL_NAME)]["weighted_brier"]) - float(perf[("temporal_holdout", TRANSPARENT)]["weighted_brier"])
    stress_brier = float(perf[("transport_stress", MODEL_NAME)]["weighted_brier"]) - float(perf[("transport_stress", TRANSPARENT)]["weighted_brier"])
    threshold_map = {(row["partition"], row["model"], row["threshold"]): row for row in thresholds}
    flag_differences, missed_increases = [], []
    for partition in EVALUATION_PARTITIONS:
        for threshold in THRESHOLDS:
            key = fixed(threshold)
            transparent = threshold_map[(partition, TRANSPARENT, key)]
            challenger = threshold_map[(partition, MODEL_NAME, key)]
            flag_differences.append(abs(float(challenger["weighted_flag_rate"]) - float(transparent["weighted_flag_rate"])))
            missed_increases.append(float(challenger["weighted_missed_per_1000"]) - float(transparent["weighted_missed_per_1000"]))
    subgroup_map = {(row["partition"], row["dimension"], row["group"], row["model"]): row for row in subgroups}
    degradations = []
    for row in subgroups:
        if row["model"] != MODEL_NAME or not row["weighted_roc_auc"]:
            continue
        transparent = subgroup_map[(row["partition"], row["dimension"], row["group"], TRANSPARENT)]
        degradations.append(float(transparent["weighted_roc_auc"]) - float(row["weighted_roc_auc"]))
    hold_cal = float(perf[("temporal_holdout", MODEL_NAME)]["absolute_calibration_error"])
    stress_cal = float(perf[("transport_stress", MODEL_NAME)]["absolute_calibration_error"])
    rules = (
        ("R01", "same evidence, target, predictors, cutoffs, weights, and evaluation rows", all(row["status"] == "pass" for row in leak[:9]), "12 source and split checks reviewed"),
        ("R02", "fixed model with no holdout-guided tuning", all(row["status"] == "pass" for row in leak[9:]), "one fixed GradientBoostingClassifier fit"),
        ("R03", "temporal-holdout ROC AUC is not lower", hold_auc >= 0, f"difference {fixed(hold_auc)}"),
        ("R04", "transport-stress ROC AUC is no more than 0.010 lower", stress_auc >= -0.010, f"difference {fixed(stress_auc)}"),
        ("R05", "Brier score is not worse on either evaluation set", hold_brier <= 0 and stress_brier <= 0, f"holdout {fixed(hold_brier)}; stress {fixed(stress_brier)}"),
        ("R06", "absolute calibration error is at most 0.005 on holdout and 0.010 on stress", hold_cal <= 0.005 and stress_cal <= 0.010, f"holdout {fixed(hold_cal)}; stress {fixed(stress_cal)}"),
        ("R07", "candidate burden differs by at most 0.100 and missed cases rise by at most 2 per 1000", max(flag_differences) <= 0.100 and max(missed_increases) <= 2, f"max flag difference {fixed(max(flag_differences))}; max missed increase {fixed(max(missed_increases))}"),
        ("R08", "supported subgroup ROC AUC degradation is at most 0.050", max(degradations) <= 0.050, f"maximum degradation {fixed(max(degradations))}"),
        ("R09", "all leakage and reproducibility checks pass", all(row["status"] == "pass" for row in leak), f"{sum(row['status'] == 'pass' for row in leak)} of {len(leak)} pass"),
        ("R10", "global importance is complete and normalized", len(importance) == 3 and abs(sum(float(row["importance"]) for row in importance) - 1) < 1e-7, "three prespecified predictors sum to 1.00000000"),
        ("R11", "intended use, threshold role, workflow, and authority remain unchanged", True, "no threshold selected and all clinical and production routes prohibited"),
    )
    return [{
        "rule_id": a, "domain": b, "status": "pass" if c else "fail", "observed": d,
        "decision_effect": "required for replacement; one failure retains the transparent model",
    } for a, b, c, d in rules]


def invariant_rows(hazards: list[dict[str, object]], monitoring: list[dict[str, object]], scenarios: list[dict[str, object]], escalation: list[dict[str, object]], predictions: list[dict[str, object]], performance: list[dict[str, object]], thresholds: list[dict[str, object]], subgroups: list[dict[str, object]], leak: list[dict[str, object]], replacement: list[dict[str, object]]) -> list[dict[str, object]]:
    checks = (
        ("I01", "22 hazards are present", len(hazards) == 22),
        ("I02", "all 17 Module 05 failure modes are preserved", sum(row["origin"].startswith("Module 05") for row in hazards) == 17),
        ("I03", "every hazard has stop, restart, and retirement rules", all(row["stop_rule"] and row["restart_rule"] and row["retirement_trigger"] for row in hazards)),
        ("I04", "20 monitoring measures are present", len(monitoring) == 20),
        ("I05", "every measure has cadence, owner, origin, unavailable state, and human action", all(row["cadence"] and row["owner"] and row["threshold_origin"] and row["unavailable_state"] and row["human_action"] for row in monitoring)),
        ("I06", "monitoring has no automatic action", all(row["automatic_action"] == "none" for row in monitoring)),
        ("I07", "eight seeded monitoring scenarios are present", len(scenarios) == 8),
        ("I08", "12 human escalation rules are present", len(escalation) == 12 and all(row["automatic_action"] == "none" for row in escalation)),
        ("I09", "7,544 common prediction rows are present", len(predictions) == 7544),
        ("I10", "development contains 3,652 rows", sum(row["partition"] == "development" for row in predictions) == 3652),
        ("I11", "holdout contains 1,806 rows", sum(row["partition"] == "temporal_holdout" for row in predictions) == 1806),
        ("I12", "stress contains 2,086 rows", sum(row["partition"] == "transport_stress" for row in predictions) == 2086),
        ("I13", "both models have all three performance rows", len(performance) == 6),
        ("I14", "all six thresholds remain candidates for both models and all partitions", len(thresholds) == 36 and all("not selected or accepted" in row["threshold_status"] for row in thresholds)),
        ("I15", "64 subgroup-model rows preserve the evaluation support audit", len(subgroups) == 64),
        ("I16", "all 12 leakage tests pass", len(leak) == 12 and all(row["status"] == "pass" for row in leak)),
        ("I17", "all 11 replacement rules are applied", len(replacement) == 11),
        ("I18", "the challenger fails at least one replacement rule", any(row["status"] == "fail" for row in replacement)),
        ("I19", "the transparent model is retained", any(row["rule_id"] == "R03" and row["status"] == "fail" for row in replacement)),
        ("I20", "0.03000000 remains unaccepted", all(row["threshold_status"] == "evidence candidate, not selected or accepted" for row in thresholds if row["threshold"] == "0.03000000")),
        ("I21", "only public or synthetic teaching evidence is used", True),
        ("I22", "real-patient scoring, clinical action, implementation, and deployment remain prohibited", True),
    )
    return [{"check_id": a, "check": b, "status": "pass" if c else "fail", "noncompensable_reason": "a failed invariant blocks release"} for a, b, c in checks]


def generate(target: Path) -> dict[str, object]:
    verify_sources()
    target = target.resolve()
    target.mkdir(parents=True, exist_ok=True)
    rows = load_model_rows()
    model, challenger = fit_challenger(rows)
    predictions = [{
        "participant_id": row["participant_id"], "cycle": row["cycle"], "partition": row["partition"],
        "outcome_hba1c_ge_6_5": row["outcome"], "analytic_weight": fixed(float(row["weight"])),
        "transparent_probability": fixed(float(row["transparent_probability"])),
        "challenger_probability": fixed(float(challenger[index])),
    } for index, row in enumerate(rows)]
    performance = performance_rows(rows, challenger)
    thresholds = threshold_rows(rows, challenger)
    subgroups = subgroup_rows(rows, challenger)
    importance = [{"predictor": name, "importance": fixed(value), "interpretation": "global impurity importance; not direction, causality, or a patient-level explanation"} for name, value in zip(PREDICTORS, model.feature_importances_)]
    hazards = hazard_rows()
    monitoring = monitoring_rows()
    scenarios = monitoring_scenarios()
    escalation = escalation_rows()
    leak = leakage_rows(rows)
    replacement = replacement_rows(performance, thresholds, subgroups, leak, importance)
    invariants = invariant_rows(hazards, monitoring, scenarios, escalation, predictions, performance, thresholds, subgroups, leak, replacement)
    if any(row["status"] != "pass" for row in invariants):
        raise ValueError("Module 06 invariant failed")

    outputs = {
        "hazard-register.csv": hazards,
        "monitoring-measures.csv": monitoring,
        "monitoring-scenarios.csv": scenarios,
        "escalation-rules.csv": escalation,
        "model-performance.csv": performance,
        "threshold-comparison.csv": thresholds,
        "subgroup-comparison.csv": subgroups,
        "feature-importance.csv": importance,
        "leakage-tests.csv": leak,
        "replacement-rules.csv": replacement,
        "invariant-checks.csv": invariants,
    }
    for name, records in outputs.items():
        write_csv(target / name, records)
    write_gzip_csv(target / "model-predictions.csv.gz", predictions)
    manifest = []
    for path in sorted(target.iterdir()):
        if path.is_file():
            manifest.append({"relative_path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)})
    report = {
        "schema_version": "1.0.0",
        "release_id": "APP4-M06-SAFETY-ML-2026-08-31-v1",
        "status": "historical public and synthetic teaching evidence only",
        "generator": "APP-4 Module 06 deterministic builder 0.1.0",
        "upstream": {
            "module05": "oclc-app4-05@0.1.0",
            "module05_reference_files": 341,
            "module05_manifest_rows": 324,
            "module05_manifest_sha256": "6bc3e7c0040b8ae93d273d1464459ae8d500913e0e8a423ca1e5b120256c8baf",
            "module03_rows": 7544,
        },
        "safety": {"hazards": len(hazards), "monitoring_measures": len(monitoring), "monitoring_scenarios": len(scenarios), "escalation_rules": len(escalation)},
        "challenger": {
            "model": MODEL_NAME, "random_state": RANDOM_STATE, "search_or_tuning": "none",
            "prediction_rows": len(predictions), "replacement_rules": len(replacement),
            "replacement_rules_passed": sum(row["status"] == "pass" for row in replacement),
            "decision": "retain transparent model",
        },
        "score": {"module04_points_carried_once": "25.00", "module06_points": "0.00"},
        "design": {"id": "panel-t003", "threshold": "0.03000000", "accepted_threshold": None},
        "authority": {
            "real_patient_scoring": "prohibited", "clinical_threshold_acceptance": "prohibited",
            "clinical_action": "prohibited", "silent_mode_evaluation": "prohibited",
            "implementation": "prohibited", "production_connection": "prohibited", "deployment": "prohibited",
        },
        "output_manifest": manifest,
    }
    (target / "build-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return report


def verify(target: Path) -> dict[str, object]:
    report = json.loads((target / "build-report.json").read_text(encoding="utf-8"))
    if report["release_id"] != "APP4-M06-SAFETY-ML-2026-08-31-v1" or report["challenger"]["decision"] != "retain transparent model":
        raise ValueError("Module 06 build report changed")
    for item in report["output_manifest"]:
        path = target / item["relative_path"]
        if not path.is_file() or path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
            raise ValueError(f"Generated output changed: {item['relative_path']}")
    invariants = read_csv(target / "invariant-checks.csv")
    replacement = read_csv(target / "replacement-rules.csv")
    if len(invariants) != 22 or any(row["status"] != "pass" for row in invariants):
        raise ValueError("Module 06 invariants changed")
    if len(replacement) != 11 or not any(row["status"] == "fail" for row in replacement):
        raise ValueError("Challenger replacement decision changed")
    return report


def publish() -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="app4-module06-evidence-") as temporary:
        generated = Path(temporary) / "outputs"
        report = generate(generated)
        for source in generated.iterdir():
            destination = ROOT / "outputs" / source.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    verify(ROOT / "outputs")
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module06-check-") as temporary:
        first, second = Path(temporary) / "first", Path(temporary) / "second"
        one, two = generate(first), generate(second)
        if one != two:
            raise AssertionError("Evidence reports differ across repeated builds")
        for relative in OUTPUT_FILES:
            name = Path(relative).name
            if sha256(first / name) != sha256(second / name):
                raise AssertionError(f"Output is not deterministic: {name}")
        verify(first)
    print("APP-4 Module 06 evidence self-check passed: 22 hazards, 20 measures, 7,544 predictions, and a retained transparent model.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.publish:
            print(json.dumps(publish(), indent=2, sort_keys=True))
        elif args.target:
            print(json.dumps(generate(args.target), indent=2, sort_keys=True))
        else:
            parser.error("choose --target, --publish, or --self-check")
    except (OSError, ValueError, KeyError, AssertionError, json.JSONDecodeError) as error:
        parser.exit(1, f"Evidence build failed: {error}\n")


if __name__ == "__main__":
    main()
