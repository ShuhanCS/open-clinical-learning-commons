"""Build APP-1 Module 06 equity, improvement, and bounded-ML evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import brier_score_loss, confusion_matrix, log_loss, roc_auc_score


MODULE_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = MODULE_ROOT.parent.parent
DEFAULT_COHORT = COURSE_ROOT / "modules/02-longitudinal-cohorts-followup/outputs/analysis-cohort.csv"
DEFAULT_EXPECTED = COURSE_ROOT / "modules/04-risk-adjustment-fair-comparison/outputs/expected-outcomes.csv"
DEFAULT_CARE = COURSE_ROOT / "modules/05-clinical-variation-patterns-of-care/outputs/care-patterns.csv"
SEED = 20260830
BOOTSTRAPS = 1000
THRESHOLD = 0.20
FEATURES = ["age_decade_from_40", "any_prior_acute", "prior_365d_condition_count", "index_inpatient"]
SOURCE_RULES = {
    "cohort": {"rows": 476, "fields": 49, "bytes": 200699, "sha256": "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5"},
    "care": {"rows": 476, "fields": 26, "bytes": 99475, "sha256": "c5d372e777ff3b190859e7c418b87c4f165776b84fb86346db700fa39f516a6e"},
    "expected": {"rows": 476, "fields": 12, "bytes": 54320, "sha256": "e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e"},
}
OUTPUT_FILES = (
    "analysis-checks.csv", "bootstrap-comparison.csv", "build-report.json", "calibration-bins.csv",
    "equity-summary.csv", "failure-cases.csv", "feature-importance.csv", "model-performance.csv",
    "model-predictions.csv", "pathway-edges.csv", "pathway-figure.svg", "pathway-nodes.csv",
    "split-registry.csv", "subgroup-model-audit.csv", "threshold-errors.csv",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fixed(value: float | int | None) -> str:
    if value is None or pd.isna(value):
        return ""
    return f"{float(value):.8f}"


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def verify_csv(path: Path, rule: dict[str, object], label: str) -> pd.DataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"Missing {label}: {path}")
    if path.stat().st_size != rule["bytes"] or sha256(path) != rule["sha256"]:
        raise ValueError(f"{label} fingerprint changed")
    frame = pd.read_csv(path)
    if frame.shape != (rule["rows"], rule["fields"]):
        raise ValueError(f"{label} shape changed")
    return frame


def load(cohort_path: Path, care_path: Path, expected_path: Path) -> pd.DataFrame:
    cohort = verify_csv(cohort_path, SOURCE_RULES["cohort"], "analysis cohort")
    care = verify_csv(care_path, SOURCE_RULES["care"], "care patterns")
    expected = verify_csv(expected_path, SOURCE_RULES["expected"], "expected outcomes")
    id_sets = [set(frame["patient_id"]) for frame in (cohort, care, expected)]
    if len(id_sets[0]) != 476 or not (id_sets[0] == id_sets[1] == id_sets[2]):
        raise ValueError("Accepted patient identities changed")
    if any(frame["patient_id"].duplicated().any() for frame in (cohort, care, expected)):
        raise ValueError("Duplicate patient identity")
    selected = cohort[[
        "patient_id", "index_start", "age_at_index", "gender", "race", "ethnicity",
        "prior_365d_acute_count", "prior_365d_condition_count", "index_encounter_class",
    ]].merge(care[["patient_id", "landmark_exposure", "event_indicator"]], on="patient_id", validate="one_to_one")
    selected = selected.merge(expected[[
        "patient_id", "age_decade_from_40", "any_prior_acute", "prior_365d_condition_count",
        "index_inpatient", "expected_probability", "event_indicator",
    ]], on=["patient_id", "prior_365d_condition_count", "event_indicator"], validate="one_to_one")
    selected["age_band"] = pd.cut(selected["age_at_index"], bins=[17, 44, 64, np.inf], labels=["18-44", "45-64", "65+"]).astype(str)
    return selected.sort_values(["index_start", "patient_id"], kind="stable").reset_index(drop=True)


def wilson(numerator: int, denominator: int) -> tuple[float, float]:
    z = 1.959963984540054
    proportion = numerator / denominator
    denominator_term = 1 + z * z / denominator
    center = (proportion + z * z / (2 * denominator)) / denominator_term
    margin = z * math.sqrt(proportion * (1 - proportion) / denominator + z * z / (4 * denominator * denominator)) / denominator_term
    return center - margin, center + margin


def contract_rows() -> list[dict[str, str]]:
    with (MODULE_ROOT / "equity-contract.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def equity_rows(frame: pd.DataFrame) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    dimension_field = {
        "age_band": "age_band", "source_recorded_gender": "gender",
        "source_recorded_race": "race", "source_recorded_ethnicity": "ethnicity",
    }
    for contract in contract_rows():
        field = dimension_field[contract["dimension"]]
        group = contract["group"]
        subset = frame[frame[field].astype(str) == group]
        people = len(subset)
        followup = int(subset["landmark_exposure"].sum())
        complement = people - followup
        process_ok = people >= 30 and followup >= 5 and complement >= 5
        events = int(subset["event_indicator"].sum())
        non_events = people - events
        expected_events = float(subset["expected_probability"].sum())
        outcome_ok = people >= 30 and events >= 5 and non_events >= 5 and expected_events >= 5
        lower, upper = wilson(followup, people) if process_ok else (None, None)
        outcome_lower, outcome_upper = wilson(events, people) if outcome_ok else (None, None)
        rows.append({
            "dimension": contract["dimension"], "group": group, "people": people,
            "field_missing": int(frame[field].isna().sum()),
            "followup_numerator": followup if process_ok else "", "followup_denominator": people,
            "followup_proportion": fixed(followup / people) if process_ok else "",
            "followup_lower95": fixed(lower), "followup_upper95": fixed(upper),
            "followup_support": "report with boundary" if process_ok else "suppress: process support rule",
            "outcome_events": events if outcome_ok else "", "outcome_non_events": non_events if outcome_ok else "",
            "outcome_proportion": fixed(events / people) if outcome_ok else "",
            "outcome_lower95": fixed(outcome_lower), "outcome_upper95": fixed(outcome_upper),
            "expected_events": fixed(expected_events) if outcome_ok else "",
            "observed_expected_ratio": fixed(events / expected_events) if outcome_ok else "",
            "outcome_support": "report with boundary" if outcome_ok else "suppress: outcome support rule",
            "claim_limit": contract["claim_limit"],
        })
    return rows


def pathway_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    nodes = [
        {"node_id": "N01", "label": "Landmark-eligible people", "count": 476, "evidence_status": "observed", "meaning": "accepted analysis population"},
        {"node_id": "N02", "label": "Recorded scheduled follow-up by day 30", "count": 129, "evidence_status": "observed", "meaning": "qualifying source record present"},
        {"node_id": "N03", "label": "No qualifying follow-up record by day 30", "count": 347, "evidence_status": "observed", "meaning": "qualifying source record absent"},
        {"node_id": "N04", "label": "Recorded follow-up and later acute return", "count": 25, "evidence_status": "observed", "meaning": "record pattern not a causal pathway"},
        {"node_id": "N05", "label": "Recorded follow-up and no later acute return", "count": 104, "evidence_status": "observed", "meaning": "record pattern not benefit"},
        {"node_id": "N06", "label": "No qualifying record and later acute return", "count": 62, "evidence_status": "observed", "meaning": "record pattern not preventability"},
        {"node_id": "N07", "label": "No qualifying record and no later acute return", "count": 285, "evidence_status": "observed", "meaning": "record pattern not lack of need"},
        {"node_id": "N08", "label": "Offer documented", "count": "", "evidence_status": "prospective collection", "meaning": "not observed retrospectively"},
        {"node_id": "N09", "label": "Preference and acceptance documented", "count": "", "evidence_status": "prospective collection", "meaning": "not observed retrospectively"},
        {"node_id": "N10", "label": "Appointment status before discharge", "count": "", "evidence_status": "prospective collection", "meaning": "not observed retrospectively"},
        {"node_id": "N11", "label": "Completion barriers and burden", "count": "", "evidence_status": "prospective collection", "meaning": "not observed retrospectively"},
    ]
    edges = [
        {"edge_id": "E01", "from_node": "N01", "to_node": "N02", "count": 129, "evidence_status": "observed"},
        {"edge_id": "E02", "from_node": "N01", "to_node": "N03", "count": 347, "evidence_status": "observed"},
        {"edge_id": "E03", "from_node": "N02", "to_node": "N04", "count": 25, "evidence_status": "observed"},
        {"edge_id": "E04", "from_node": "N02", "to_node": "N05", "count": 104, "evidence_status": "observed"},
        {"edge_id": "E05", "from_node": "N03", "to_node": "N06", "count": 62, "evidence_status": "observed"},
        {"edge_id": "E06", "from_node": "N03", "to_node": "N07", "count": 285, "evidence_status": "observed"},
        {"edge_id": "E07", "from_node": "N01", "to_node": "N08", "count": "", "evidence_status": "proposed collection"},
        {"edge_id": "E08", "from_node": "N08", "to_node": "N09", "count": "", "evidence_status": "proposed collection"},
        {"edge_id": "E09", "from_node": "N09", "to_node": "N10", "count": "", "evidence_status": "proposed collection"},
        {"edge_id": "E10", "from_node": "N10", "to_node": "N11", "count": "", "evidence_status": "proposed collection"},
    ]
    return nodes, edges


def pathway_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="980" height="660" viewBox="0 0 980 660" role="img" aria-labelledby="title desc">
<title id="title">Observed follow-up record pathway and proposed prospective collection</title>
<desc id="desc">Among 476 synthetic people, 129 have a scheduled follow-up record by day 30 and 347 do not. Later acute returns number 25 and 62 respectively. A separate dashed pathway shows offer, preference, appointment status, completion, barriers, and burden as proposed data collection, not observed facts. Exact values are in pathway-nodes.csv and pathway-edges.csv.</desc>
<rect width="980" height="660" fill="white"/><style>.t{font:16px Arial,sans-serif;fill:#172033}.s{font:13px Arial,sans-serif;fill:#475569}.o{fill:#e8f0ff;stroke:#1f49b6;stroke-width:2}.p{fill:#ecfdf5;stroke:#0f766e;stroke-width:2;stroke-dasharray:7 5}.l{stroke:#64748b;stroke-width:2;fill:none}.d{stroke:#0f766e;stroke-width:2;stroke-dasharray:7 5;fill:none}</style>
<text x="40" y="36" class="t" font-weight="bold">Observed source-record pathway</text><text x="40" y="58" class="s">Records do not establish offer, access, preference, completion, burden, need, quality, or benefit.</text>
<path class="l" d="M490 125 L260 205 M490 125 L720 205 M260 275 L150 355 M260 275 L370 355 M720 275 L610 355 M720 275 L830 355"/>
<g class="o"><rect x="350" y="80" width="280" height="70" rx="8"/><rect x="110" y="205" width="300" height="70" rx="8"/><rect x="570" y="205" width="300" height="70" rx="8"/><rect x="45" y="355" width="210" height="70" rx="8"/><rect x="275" y="355" width="210" height="70" rx="8"/><rect x="505" y="355" width="210" height="70" rx="8"/><rect x="735" y="355" width="210" height="70" rx="8"/></g>
<g text-anchor="middle" class="t"><text x="490" y="108">Landmark eligible</text><text x="490" y="133">476</text><text x="260" y="233">Follow-up record</text><text x="260" y="258">129</text><text x="720" y="233">No qualifying record</text><text x="720" y="258">347</text><text x="150" y="383">Later return</text><text x="150" y="408">25</text><text x="380" y="383">No later return</text><text x="380" y="408">104</text><text x="610" y="383">Later return</text><text x="610" y="408">62</text><text x="840" y="383">No later return</text><text x="840" y="408">285</text></g>
<text x="40" y="478" class="t" font-weight="bold">Proposed collection for a bounded prospective test</text><path class="d" d="M160 545 L340 545 L520 545 L700 545"/><g class="p"><rect x="50" y="510" width="220" height="70" rx="8"/><rect x="280" y="510" width="220" height="70" rx="8"/><rect x="510" y="510" width="220" height="70" rx="8"/><rect x="740" y="510" width="210" height="70" rx="8"/></g><g text-anchor="middle" class="t"><text x="160" y="540">Offer documented</text><text x="160" y="563" class="s">not observed</text><text x="390" y="540">Preference / acceptance</text><text x="390" y="563" class="s">not observed</text><text x="620" y="540">Appointment status</text><text x="620" y="563" class="s">not observed</text><text x="845" y="535">Completion, barriers,</text><text x="845" y="557">and burden</text></g><text x="40" y="625" class="s">Dashed green nodes are proposed measurements, not inferred events. Structured alternative: pathway-display.md.</text></svg>
'''


def fit_models(frame: pd.DataFrame):
    train = frame.iloc[:333].copy()
    evaluation = frame.iloc[333:].copy()
    x_train = train[FEATURES].astype(float)
    x_eval = evaluation[FEATURES].astype(float)
    y_train = train["event_indicator"].astype(int).to_numpy()
    y_eval = evaluation["event_indicator"].astype(int).to_numpy()
    transparent = sm.GLM(y_train, sm.add_constant(x_train, has_constant="add"), family=sm.families.Binomial()).fit()
    transparent_probability = np.asarray(transparent.predict(sm.add_constant(x_eval, has_constant="add")))
    forest = RandomForestClassifier(n_estimators=200, max_depth=3, min_samples_leaf=15, max_features=None, random_state=SEED, n_jobs=1)
    forest.fit(x_train, y_train)
    forest_probability = forest.predict_proba(x_eval)[:, 1]
    return train, evaluation, transparent, forest, {"transparent": transparent_probability, "bounded_rf": forest_probability}


def calibration_fit(y: np.ndarray, probability: np.ndarray) -> tuple[float, float]:
    clipped = np.clip(probability, 1e-8, 1 - 1e-8)
    logits = np.log(clipped / (1 - clipped))
    fitted = sm.GLM(y, sm.add_constant(logits, has_constant="add"), family=sm.families.Binomial()).fit()
    return float(fitted.params[0]), float(fitted.params[1])


def performance_rows(evaluation: pd.DataFrame, probabilities: dict[str, np.ndarray]) -> list[dict[str, object]]:
    y = evaluation["event_indicator"].astype(int).to_numpy()
    rows = []
    for model, probability in probabilities.items():
        predicted = probability >= THRESHOLD
        tn, fp, fn, tp = confusion_matrix(y, predicted, labels=[0, 1]).ravel()
        intercept, slope = calibration_fit(y, probability)
        rows.append({
            "model": model, "evaluation_rows": len(y), "events": int(y.sum()),
            "brier": fixed(brier_score_loss(y, probability)), "roc_auc": fixed(roc_auc_score(y, probability)),
            "log_loss": fixed(log_loss(y, probability)), "calibration_intercept": fixed(intercept),
            "calibration_slope": fixed(slope), "threshold": fixed(THRESHOLD), "tn": int(tn), "fp": int(fp),
            "fn": int(fn), "tp": int(tp), "sensitivity": fixed(tp / (tp + fn)),
            "specificity": fixed(tn / (tn + fp)), "flagged": int(fp + tp),
            "weighted_error_cost": int(fn * 3 + fp),
        })
    return rows


def bootstrap_rows(evaluation: pd.DataFrame, probabilities: dict[str, np.ndarray]) -> list[dict[str, object]]:
    y = evaluation["event_indicator"].astype(int).to_numpy()
    positive = np.flatnonzero(y == 1)
    negative = np.flatnonzero(y == 0)
    rng = np.random.default_rng(SEED)
    differences = {"brier": [], "roc_auc": []}
    for _ in range(BOOTSTRAPS):
        sample = np.concatenate((rng.choice(positive, len(positive), replace=True), rng.choice(negative, len(negative), replace=True)))
        yy = y[sample]
        simple = probabilities["transparent"][sample]
        machine = probabilities["bounded_rf"][sample]
        differences["brier"].append(brier_score_loss(yy, machine) - brier_score_loss(yy, simple))
        differences["roc_auc"].append(roc_auc_score(yy, machine) - roc_auc_score(yy, simple))
    point = {
        "brier": brier_score_loss(y, probabilities["bounded_rf"]) - brier_score_loss(y, probabilities["transparent"]),
        "roc_auc": roc_auc_score(y, probabilities["bounded_rf"]) - roc_auc_score(y, probabilities["transparent"]),
    }
    return [{
        "metric": metric, "comparison": "bounded_rf minus transparent", "point_difference": fixed(point[metric]),
        "lower95": fixed(np.quantile(values, 0.025)), "upper95": fixed(np.quantile(values, 0.975)),
        "replicates": BOOTSTRAPS, "seed": SEED, "method": "paired stratified person bootstrap",
    } for metric, values in differences.items()]


def calibration_rows(evaluation: pd.DataFrame, probabilities: dict[str, np.ndarray]) -> list[dict[str, object]]:
    rows = []
    y = evaluation["event_indicator"].astype(int).to_numpy()
    patient = evaluation["patient_id"].astype(str).to_numpy()
    for model, probability in probabilities.items():
        order = np.lexsort((patient, probability))
        for group_number, positions in enumerate(np.array_split(order, 5), start=1):
            rows.append({
                "model": model, "calibration_group": group_number, "rows": len(positions),
                "events": int(y[positions].sum()), "mean_probability": fixed(probability[positions].mean()),
                "observed_proportion": fixed(y[positions].mean()),
                "limit": "small teaching group; use model-level calibration intercept and slope",
            })
    return rows


def prediction_rows(evaluation: pd.DataFrame, probabilities: dict[str, np.ndarray]) -> list[dict[str, object]]:
    rows = []
    for position, (_, item) in enumerate(evaluation.iterrows()):
        rows.append({
            "patient_id": item["patient_id"], "index_start": item["index_start"], "event_indicator": int(item["event_indicator"]),
            "transparent_probability": fixed(probabilities["transparent"][position]),
            "transparent_flag": int(probabilities["transparent"][position] >= THRESHOLD),
            "bounded_rf_probability": fixed(probabilities["bounded_rf"][position]),
            "bounded_rf_flag": int(probabilities["bounded_rf"][position] >= THRESHOLD),
            "threshold": fixed(THRESHOLD),
        })
    return rows


def threshold_rows(evaluation: pd.DataFrame, probabilities: dict[str, np.ndarray]) -> list[dict[str, object]]:
    y = evaluation["event_indicator"].astype(int).to_numpy()
    rows = []
    for model, probability in probabilities.items():
        predicted = probability >= THRESHOLD
        tn, fp, fn, tp = confusion_matrix(y, predicted, labels=[0, 1]).ravel()
        for error_type, count, unit_cost in (("true_negative", tn, 0), ("false_positive", fp, 1), ("false_negative", fn, 3), ("true_positive", tp, 0)):
            rows.append({
                "model": model, "threshold": fixed(THRESHOLD), "classification": error_type,
                "count": int(count), "unit_cost": unit_cost, "weighted_cost": int(count * unit_cost),
                "cost_status": "educational sensitivity scenario not clinical value",
            })
    return rows


def subgroup_rows(evaluation: pd.DataFrame, probabilities: dict[str, np.ndarray]) -> list[dict[str, object]]:
    evaluation = evaluation.copy()
    evaluation["age_band"] = pd.cut(evaluation["age_at_index"], bins=[17, 44, 64, np.inf], labels=["18-44", "45-64", "65+"]).astype(str)
    fields = {
        "age_band": "age_band", "source_recorded_gender": "gender",
        "source_recorded_race": "race", "source_recorded_ethnicity": "ethnicity",
    }
    rows = []
    for contract in contract_rows():
        positions = np.flatnonzero(evaluation[fields[contract["dimension"]]].astype(str).to_numpy() == contract["group"])
        y = evaluation.iloc[positions]["event_indicator"].astype(int).to_numpy()
        support = len(y) >= 30 and int(y.sum()) >= 5 and int((1 - y).sum()) >= 5
        for model, probability in probabilities.items():
            values = probability[positions]
            if support:
                predicted = values >= THRESHOLD
                tn, fp, fn, tp = confusion_matrix(y, predicted, labels=[0, 1]).ravel()
            else:
                fp = fn = ""
            rows.append({
                "dimension": contract["dimension"], "group": contract["group"], "model": model,
                "evaluation_rows": len(y), "events": int(y.sum()), "non_events": int(len(y) - y.sum()),
                "support": "report with boundary" if support else "suppress: model-audit support rule",
                "brier": fixed(brier_score_loss(y, values)) if support else "",
                "roc_auc": fixed(roc_auc_score(y, values)) if support else "",
                "false_positives": fp, "false_negatives": fn,
                "claim_limit": "descriptive synthetic audit only; no fairness certification ranking or group-specific action",
            })
    return rows


def failure_rows(evaluation: pd.DataFrame, probabilities: dict[str, np.ndarray]) -> list[dict[str, object]]:
    rows = []
    for model, probability in probabilities.items():
        predicted = probability >= THRESHOLD
        y = evaluation["event_indicator"].astype(int).to_numpy()
        false_negative_positions = np.flatnonzero((y == 1) & ~predicted)
        for position in false_negative_positions:
            item = evaluation.iloc[position]
            rows.append({
                "model": model, "error_type": "false_negative", "patient_id_or_aggregate": item["patient_id"],
                "count": 1, "probability_or_mean": fixed(probability[position]), "event_indicator": 1,
                "age_decade_from_40": fixed(item["age_decade_from_40"]), "any_prior_acute": int(item["any_prior_acute"]),
                "prior_365d_condition_count": int(item["prior_365d_condition_count"]), "index_inpatient": int(item["index_inpatient"]),
                "review_boundary": "baseline feature review only; no invented clinical story",
            })
        false_positive_positions = np.flatnonzero((y == 0) & predicted)
        rows.append({
            "model": model, "error_type": "false_positive_aggregate", "patient_id_or_aggregate": "all false positives",
            "count": len(false_positive_positions), "probability_or_mean": fixed(probability[false_positive_positions].mean()),
            "event_indicator": 0, "age_decade_from_40": "", "any_prior_acute": "",
            "prior_365d_condition_count": "", "index_inpatient": "",
            "review_boundary": "aggregate workload review; no patient-level action or clinical value claim",
        })
    return rows


def check_rows(frame: pd.DataFrame, train: pd.DataFrame, evaluation: pd.DataFrame, equity: list[dict[str, object]], performance: list[dict[str, object]], bootstrap: list[dict[str, object]], subgroups: list[dict[str, object]], failures: list[dict[str, object]]) -> list[dict[str, object]]:
    performance_by_model = {row["model"]: row for row in performance}
    checks = [
        ("CHK01", "accepted people", len(frame), 476), ("CHK02", "accepted outcomes", int(frame["event_indicator"].sum()), 87),
        ("CHK03", "recorded follow-up", int(frame["landmark_exposure"].sum()), 129), ("CHK04", "equity groups", len(equity), 12),
        ("CHK05", "training rows", len(train), 333), ("CHK06", "training events", int(train["event_indicator"].sum()), 70),
        ("CHK07", "evaluation rows", len(evaluation), 143), ("CHK08", "evaluation events", int(evaluation["event_indicator"].sum()), 17),
        ("CHK09", "fixed features", len(FEATURES), 4), ("CHK10", "fixed threshold", fixed(THRESHOLD), "0.20000000"),
        ("CHK11", "bootstrap replicates", BOOTSTRAPS, 1000), ("CHK12", "model rows", len(performance), 2),
        ("CHK13", "transparent weighted cost", performance_by_model["transparent"]["weighted_error_cost"], 44),
        ("CHK14", "bounded RF weighted cost", performance_by_model["bounded_rf"]["weighted_error_cost"], 67),
        ("CHK15", "paired comparisons", len(bootstrap), 2), ("CHK16", "subgroup audit rows", len(subgroups), 24),
        ("CHK17", "supported subgroup model rows", sum(row["support"] == "report with boundary" for row in subgroups), 12),
        ("CHK18", "false-negative and aggregate rows", len(failures), 17),
        ("CHK19", "source-recorded gender missing", int(frame["gender"].isna().sum()), 0),
        ("CHK20", "small groups remain separate", sum(row["followup_support"].startswith("suppress") for row in equity), 2),
    ]
    return [{"check_id": check_id, "check": label, "observed": observed, "expected": expected, "status": "pass" if str(observed) == str(expected) else "fail"} for check_id, label, observed, expected in checks]


def build(cohort_path: Path, care_path: Path, expected_path: Path, target: Path) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    frame = load(cohort_path, care_path, expected_path)
    target.mkdir(parents=True)
    equity = equity_rows(frame)
    nodes, edges = pathway_rows()
    train, evaluation, transparent, forest, probabilities = fit_models(frame)
    performance = performance_rows(evaluation, probabilities)
    bootstrap = bootstrap_rows(evaluation, probabilities)
    calibration = calibration_rows(evaluation, probabilities)
    predictions = prediction_rows(evaluation, probabilities)
    thresholds = threshold_rows(evaluation, probabilities)
    subgroups = subgroup_rows(evaluation, probabilities)
    failures = failure_rows(evaluation, probabilities)
    checks = check_rows(frame, train, evaluation, equity, performance, bootstrap, subgroups, failures)
    if any(row["status"] != "pass" for row in checks):
        failed = [row["check_id"] for row in checks if row["status"] != "pass"]
        raise ValueError(f"Analysis check failed: {', '.join(failed)}")

    split = [{
        "patient_id": row.patient_id, "index_start": row.index_start,
        "split": "training" if position < 333 else "evaluation", "split_order": position + 1,
        "event_indicator": int(row.event_indicator), "prediction_time": "day-30 landmark",
    } for position, row in enumerate(frame.itertuples(index=False))]
    features = [{"model": "bounded_rf", "feature": feature, "importance": fixed(importance), "interpretation": "model allocation only; not causal importance"} for feature, importance in zip(FEATURES, forest.feature_importances_)]

    write_csv(target / "analysis-checks.csv", ["check_id", "check", "observed", "expected", "status"], checks)
    write_csv(target / "equity-summary.csv", list(equity[0]), equity)
    write_csv(target / "pathway-nodes.csv", list(nodes[0]), nodes)
    write_csv(target / "pathway-edges.csv", list(edges[0]), edges)
    (target / "pathway-figure.svg").write_text(pathway_svg(), encoding="utf-8", newline="")
    write_csv(target / "split-registry.csv", list(split[0]), split)
    write_csv(target / "model-predictions.csv", list(predictions[0]), predictions)
    write_csv(target / "model-performance.csv", list(performance[0]), performance)
    write_csv(target / "bootstrap-comparison.csv", list(bootstrap[0]), bootstrap)
    write_csv(target / "calibration-bins.csv", list(calibration[0]), calibration)
    write_csv(target / "threshold-errors.csv", list(thresholds[0]), thresholds)
    write_csv(target / "subgroup-model-audit.csv", list(subgroups[0]), subgroups)
    write_csv(target / "feature-importance.csv", list(features[0]), features)
    write_csv(target / "failure-cases.csv", list(failures[0]), failures)

    performance_by_model = {row["model"]: row for row in performance}
    report = {
        "status": "pass", "module": "oclc-app1-06", "module_version": "0.1.0", "commons_release": "0.54.0",
        "sources": {name: {**rule, "access": "read-only accepted CSV extract"} for name, rule in SOURCE_RULES.items()},
        "population": {"people": 476, "recorded_followup": 129, "events": 87, "training_rows": 333, "training_events": 70, "evaluation_rows": 143, "evaluation_events": 17},
        "models": {"transparent": "binomial GLM logit", "bounded_rf": "RandomForestClassifier", "features": FEATURES, "threshold": fixed(THRESHOLD), "seed": SEED, "bootstrap_replicates": BOOTSTRAPS},
        "reference_findings": {
            "transparent_brier": performance_by_model["transparent"]["brier"], "bounded_rf_brier": performance_by_model["bounded_rf"]["brier"],
            "transparent_auc": performance_by_model["transparent"]["roc_auc"], "bounded_rf_auc": performance_by_model["bounded_rf"]["roc_auc"],
            "transparent_weighted_error_cost": 44, "bounded_rf_weighted_error_cost": 67,
            "ml_changes_improvement_decision": "no", "equity_conclusion": "question retained; key access states are not observed",
            "implementation_authorization": "not authorized",
        },
        "analysis_checks": len(checks), "outputs": list(OUTPUT_FILES),
        "claim_boundary": "synthetic curriculum evidence only; no real access fairness ranking clinical use or deployment",
    }
    (target / "build-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="")
    return {
        "status": "pass", "output_files": len(OUTPUT_FILES),
        "output_bytes": sum(path.stat().st_size for path in target.iterdir()),
        "output_sha256": {path.name: sha256(path) for path in sorted(target.iterdir())},
    }


def self_check(cohort: Path, care: Path, expected: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="app1-module06-build-") as temp_dir:
        base = Path(temp_dir)
        first, second = base / "first", base / "second"
        one = build(cohort, care, expected, first)
        two = build(cohort, care, expected, second)
        assert one == two
        assert one["output_files"] == 15
        assert {path.name: sha256(path) for path in first.iterdir()} == {path.name: sha256(path) for path in second.iterdir()}
        try:
            build(cohort, care, expected, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder overwrote an existing target")
    print("APP-1 Module 06 builder self-check passed: 15 deterministic outputs and existing-target rejection.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cohort", type=Path, default=DEFAULT_COHORT)
    parser.add_argument("--care", type=Path, default=DEFAULT_CARE)
    parser.add_argument("--expected", type=Path, default=DEFAULT_EXPECTED)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check(args.cohort, args.care, args.expected)
            return
        if not args.target:
            parser.error("--target is required")
        print(json.dumps(build(args.cohort, args.care, args.expected, args.target), indent=2))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
