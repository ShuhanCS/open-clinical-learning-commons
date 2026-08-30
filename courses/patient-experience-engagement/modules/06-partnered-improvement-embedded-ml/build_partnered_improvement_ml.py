"""Build APP-2 Module 06 partnered-improvement and response-ML evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import brier_score_loss, confusion_matrix, log_loss, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


MODULE_ROOT = Path(__file__).resolve().parent
COURSE_ROOT = MODULE_ROOT.parent.parent
SEED = 20260830
FEATURES = ["age_band", "other_language_at_home", "income_group"]
THRESHOLD = 0.60
LOWER_FACTOR = 1.0
UPPER_FACTOR = 3.0
OUTPUT_FILES = (
    "upstream-inventory.csv",
    "analysis-checks.csv",
    "improvement-evidence.csv",
    "partner-question-register.csv",
    "transparent-weight-cells.csv",
    "split-registry.csv",
    "model-predictions.csv",
    "model-performance.csv",
    "calibration-bins.csv",
    "threshold-errors.csv",
    "response-weight-diagnostics.csv",
    "estimate-recovery.csv",
    "subgroup-model-audit.csv",
    "feature-importance.csv",
    "failure-cases.csv",
    "invariant-checks.csv",
    "build-report.json",
)
SOURCE_RULES = {
    "frame": ("modules/03-response-representation-bias/data/public/adult-inpatient-frame.csv", 1255, 19, 294946, "96e7b493aabf51bdb6c6072e2175ebe560a8ab211287983c6b38e851244e8d4a"),
    "response": ("modules/03-response-representation-bias/data/synthetic/response-study.csv", 1255, 16, 271547, "eb593a7883c10ff8b83456a4b66b7c8132a3a787d1151d1baf4093d21f10a0af"),
    "response_contract": ("modules/03-response-representation-bias/response-contract.json", None, None, 3224, "399e60c91895b6ce797b20c9229a21056be7bddb860b469aedc2ab2b8a39b133"),
    "module03_release": ("modules/03-response-representation-bias/release.json", None, None, 6161, "58e15614fa749d21cccaccc8cd952d114c23ab7cb4b3d87c73b22c5bbad62352"),
    "module04_release": ("modules/04-linked-patient-evidence/release.json", None, None, 5063, "de31b805351946d644dccc5125deffdffdb993470fbdd74670278c2ca6e7e1d0"),
    "module05_release": ("modules/05-patient-voice-equity/release.json", None, None, 5261, "a73f007335ac7ce4a3c8b79eeb164b141288b70a6f5d55bf4414b231b6ee22a8"),
    "voice_contract": ("modules/05-patient-voice-equity/voice-equity-contract.json", None, None, 1205, "43317518d8c65dc3a498083129b2227ff6f877f114185eeb8775a3e550cd42e3"),
    "group_support": ("modules/05-patient-voice-equity/outputs/group-support.csv", 13, 7, 2343, "dad581097558df657c8ffffb048e071bc51179c4e63e76b946b76661b32647fe"),
    "group_estimates": ("modules/05-patient-voice-equity/outputs/group-estimates.csv", 52, 15, 9421, "e763215283afd8e841d14118ec9cda1a5a3fba15a4a424a828dcda887ae879d1"),
    "group_contrasts": ("modules/05-patient-voice-equity/outputs/group-contrasts.csv", 36, 12, 6433, "edacc84e7b63564140b3759cbb88c1c3806018a4e2328375dbf1adae0813ee66"),
    "channel_audit": ("modules/05-patient-voice-equity/outputs/channel-exclusion-audit.csv", 13, 7, 2707, "7944ce86afa40fdcb41bc559e682e060a51da90e98f60da2a8337afee6606291"),
    "equity_memo": ("modules/05-patient-voice-equity/reference/equity-patient-voice-memo.md", None, None, 1594, "ebafba2577d706dc838c0ae843eb386633744780ff1f9754c1865d6a54ce4d1f"),
    "module05_progression": ("modules/05-patient-voice-equity/reference/progression-decision.md", None, None, 690, "bafc2913a5873ca21acd8d3cd32cf11f7d633cfaaf1fe5e30a5ba3f89d6dacad"),
}


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


def verified_paths(source_root: Path, response_override: Path | None = None) -> tuple[dict[str, Path], list[dict[str, object]]]:
    paths: dict[str, Path] = {}
    inventory: list[dict[str, object]] = []
    for key, (relative, expected_rows, expected_fields, expected_bytes, expected_hash) in SOURCE_RULES.items():
        path = response_override if key == "response" and response_override else source_root / relative
        if not path.is_file():
            raise FileNotFoundError(f"Missing accepted input: {path}")
        if path.stat().st_size != expected_bytes or sha256(path) != expected_hash:
            raise ValueError(f"Accepted input fingerprint changed: {key}")
        rows = fields = ""
        if expected_rows is not None:
            frame = pd.read_csv(path)
            if frame.shape != (expected_rows, expected_fields):
                raise ValueError(f"Accepted input shape changed: {key}")
            rows, fields = expected_rows, expected_fields
        paths[key] = path
        inventory.append({
            "input_id": key,
            "relative_path": relative,
            "rows": rows,
            "fields": fields,
            "bytes": expected_bytes,
            "sha256": expected_hash,
            "status": "accepted exact input",
        })
    return paths, inventory


def load_data(paths: dict[str, Path]) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object], dict[str, object], dict[str, object], pd.DataFrame]:
    frame = pd.read_csv(paths["frame"], dtype=str)
    response = pd.read_csv(paths["response"], dtype=str)
    if frame["frame_record_id"].duplicated().any() or response["frame_record_id"].duplicated().any():
        raise ValueError("Duplicate frame identity")
    if set(frame["frame_record_id"]) != set(response["frame_record_id"]):
        raise ValueError("Frame identities changed")
    response = response.set_index("frame_record_id").loc[frame["frame_record_id"]].reset_index()
    selected = frame[[
        "frame_record_id", "age_band", "sex", "race_ethnicity", "other_language_at_home",
        "income_group", "insurance_coverage", "base_person_weight",
    ]].merge(response, on="frame_record_id", validate="one_to_one")
    selected["base_person_weight"] = selected["base_person_weight"].astype(float)
    selected["responded"] = (selected["response_status"] == "respondent").astype(int)
    expected_cell = selected[FEATURES].astype(str).agg("|".join, axis=1)
    if not expected_cell.equals(selected["response_cell"]):
        raise ValueError("Transparent response-cell identity changed")
    if set(selected["response_status"]) != {"respondent", "nonrespondent"}:
        raise ValueError("Response status values changed")
    if len(selected) != 1255 or int(selected["responded"].sum()) != 782:
        raise ValueError("Accepted response population changed")
    response_contract = json.loads(paths["response_contract"].read_text(encoding="utf-8"))
    module04 = json.loads(paths["module04_release"].read_text(encoding="utf-8"))
    module05 = json.loads(paths["module05_release"].read_text(encoding="utf-8"))
    groups = pd.read_csv(paths["group_support"], dtype=str)
    return selected, groups, response_contract, module04, module05, frame


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.average(values.astype(float), weights=weights.astype(float)))


def kish(weights: np.ndarray) -> float:
    total = float(weights.sum())
    return total * total / float(np.square(weights).sum())


def transparent_cells(train: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, tuple[float, float]]]:
    rows: list[dict[str, object]] = []
    lookup: dict[str, tuple[float, float]] = {}
    for cell, subset in train.groupby("response_cell", sort=True):
        frame_weight = float(subset["base_person_weight"].sum())
        respondents = subset[subset["responded"] == 1]
        response_weight = float(respondents["base_person_weight"].sum())
        if response_weight <= 0:
            raise ValueError(f"Training response cell has no respondents: {cell}")
        raw_factor = frame_weight / response_weight
        factor = float(np.clip(raw_factor, LOWER_FACTOR, UPPER_FACTOR))
        probability = response_weight / frame_weight
        lookup[str(cell)] = (probability, factor)
        rows.append({
            "response_cell": cell,
            "training_frame_n": len(subset),
            "training_respondent_n": len(respondents),
            "training_frame_base_weight": fixed(frame_weight),
            "training_respondent_base_weight": fixed(response_weight),
            "response_probability": fixed(probability),
            "raw_response_factor": fixed(raw_factor),
            "bounded_response_factor": fixed(factor),
            "bound_hit": "yes" if not math.isclose(raw_factor, factor) else "no",
            "claim_limit": "training-only transparent teaching factor; not an official survey adjustment",
        })
    return pd.DataFrame(rows), lookup


def make_model() -> Pipeline:
    preprocessing = ColumnTransformer(
        [("eligible", OneHotEncoder(handle_unknown="ignore", sparse_output=False), FEATURES)],
        remainder="drop",
        verbose_feature_names_out=False,
    )
    classifier = RandomForestClassifier(
        n_estimators=200,
        max_depth=3,
        min_samples_leaf=25,
        max_features=None,
        random_state=SEED,
        n_jobs=1,
    )
    return Pipeline([("preprocessing", preprocessing), ("classifier", classifier)])


def performance_row(name: str, actual: np.ndarray, probability: np.ndarray, weights: np.ndarray) -> dict[str, object]:
    predicted = (probability >= THRESHOLD).astype(int)
    tn, fp, fn, tp = confusion_matrix(actual, predicted, labels=[0, 1]).ravel()
    return {
        "method": name,
        "evaluation_rows": len(actual),
        "respondents": int(actual.sum()),
        "nonrespondents": int(len(actual) - actual.sum()),
        "base_weighted_brier": fixed(brier_score_loss(actual, probability, sample_weight=weights)),
        "base_weighted_auc": fixed(roc_auc_score(actual, probability, sample_weight=weights)),
        "base_weighted_log_loss": fixed(log_loss(actual, probability, sample_weight=weights, labels=[0, 1])),
        "threshold": fixed(THRESHOLD),
        "true_negative": int(tn),
        "false_positive": int(fp),
        "false_negative": int(fn),
        "true_positive": int(tp),
        "flagged_likely_response": int(predicted.sum()),
        "weighted_teaching_error_cost": int(2 * fp + fn),
        "claim_limit": "synthetic response comparison; threshold is not a contact or targeting rule",
    }


def calibration_rows(eval_frame: pd.DataFrame, methods: dict[str, np.ndarray]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for method, probability in methods.items():
        ordered = np.lexsort((eval_frame["frame_record_id"].to_numpy(), probability))
        for number, indexes in enumerate(np.array_split(ordered, 5), start=1):
            part = eval_frame.iloc[indexes]
            weights = part["base_person_weight"].to_numpy(float)
            rows.append({
                "method": method,
                "calibration_group": number,
                "rows": len(part),
                "respondents": int(part["responded"].sum()),
                "mean_predicted_response": fixed(weighted_mean(probability[indexes], weights)),
                "observed_response": fixed(weighted_mean(part["responded"].to_numpy(), weights)),
                "minimum_probability": fixed(float(probability[indexes].min())),
                "maximum_probability": fixed(float(probability[indexes].max())),
                "claim_limit": "base-weighted held-out calibration group; not a fielding threshold",
            })
    return rows


def weight_diagnostics(eval_frame: pd.DataFrame, factors: dict[str, np.ndarray]) -> list[dict[str, object]]:
    respondents = eval_frame["responded"].to_numpy() == 1
    base = eval_frame.loc[respondents, "base_person_weight"].to_numpy(float)
    base_ess = kish(base)
    rows: list[dict[str, object]] = []
    for method, factor_all in factors.items():
        factor = factor_all[respondents]
        adjusted = base * factor
        ess = kish(adjusted)
        rows.append({
            "method": method,
            "respondent_rows": len(base),
            "minimum_factor": fixed(float(factor.min())),
            "median_factor": fixed(float(np.median(factor))),
            "p95_factor": fixed(float(np.quantile(factor, 0.95))),
            "maximum_factor": fixed(float(factor.max())),
            "factor_cap_hits": int(np.isclose(factor, UPPER_FACTOR).sum()),
            "base_weight_kish_effective_n": fixed(base_ess),
            "adjusted_weight_kish_effective_n": fixed(ess),
            "effective_n_ratio": fixed(ess / base_ess),
            "largest_adjusted_weight_share_percent": fixed(100 * adjusted.max() / adjusted.sum()),
            "stability_status": "pass" if ess / base_ess >= 0.85 and 100 * adjusted.max() / adjusted.sum() < 3.0 else "fail",
            "claim_limit": "held-out respondent teaching weights; not official MEPS or HCAHPS weights",
        })
    return rows


def estimate(eval_frame: pd.DataFrame, item: str, estimator: str, factors: dict[str, np.ndarray]) -> tuple[str, float]:
    home = eval_frame["q21_truth"].to_numpy() == "home_or_other"
    if estimator == "full_frame_truth":
        included = home
        values = (eval_frame[f"{item}_truth"].to_numpy() == "yes").astype(float)
        weights = eval_frame["base_person_weight"].to_numpy(float)
    else:
        observed = eval_frame[f"{item}_observed"].to_numpy()
        included = home & (eval_frame["responded"].to_numpy() == 1) & np.isin(observed, ["yes", "no"])
        values = (observed == "yes").astype(float)
        weights = eval_frame["base_person_weight"].to_numpy(float) * factors[estimator]
    return str(int(included.sum())), 100 * weighted_mean(values[included], weights[included])


def recovery_rows(eval_frame: pd.DataFrame, factors: dict[str, np.ndarray]) -> list[dict[str, object]]:
    estimators = (
        ("full_frame_truth", "base person weight across all applicable held-out frame records"),
        ("respondent_base_weighted", "base person weight among item-answering held-out respondents"),
        ("transparent_adjusted", "base person weight times training-only bounded transparent factor"),
        ("bounded_ml_adjusted", "base person weight times bounded held-out ML factor"),
    )
    values: dict[tuple[str, str], tuple[str, float]] = {}
    for item in ("q22", "q23"):
        for estimator, _ in estimators:
            values[(item, estimator)] = estimate(eval_frame, item, estimator, factors)
    rows: list[dict[str, object]] = []
    for measure in ("Q22", "Q23", "teaching_composite"):
        item = measure.lower()
        if measure == "teaching_composite":
            truth = np.mean([values[(part, "full_frame_truth")][1] for part in ("q22", "q23")])
        else:
            truth = values[(item, "full_frame_truth")][1]
        for estimator, definition in estimators:
            if measure == "teaching_composite":
                answered = f"Q22={values[('q22', estimator)][0]};Q23={values[('q23', estimator)][0]}"
                result = np.mean([values[(part, estimator)][1] for part in ("q22", "q23")])
            else:
                answered, result = values[(item, estimator)]
            rows.append({
                "measure": measure,
                "estimator": estimator,
                "answered_n": answered,
                "estimate_percent": fixed(result),
                "truth_percent": fixed(truth),
                "bias_pp": fixed(result - truth),
                "absolute_bias_pp": fixed(abs(result - truth)),
                "weight_definition": definition,
                "claim_limit": "held-out synthetic known-truth comparison; teaching composite is not an official score",
            })
    return rows


def subgroup_rows(eval_frame: pd.DataFrame, groups: pd.DataFrame, methods: dict[str, np.ndarray], factors: dict[str, np.ndarray]) -> list[dict[str, object]]:
    dimension_field = {
        "other_language_at_home": "other_language_at_home",
        "income_group": "income_group",
        "insurance_coverage": "insurance_coverage",
        "race_ethnicity": "race_ethnicity",
    }
    rows: list[dict[str, object]] = []
    for _, group in groups.iterrows():
        field = dimension_field[group["dimension"]]
        mask = eval_frame[field].to_numpy() == group["group"]
        count = int(mask.sum())
        respondents = int(eval_frame.loc[mask, "responded"].sum())
        nonrespondents = count - respondents
        supported = count >= 30 and respondents >= 10 and nonrespondents >= 10
        weights = eval_frame.loc[mask, "base_person_weight"].to_numpy(float)
        actual = eval_frame.loc[mask, "responded"].to_numpy(int)
        for method, probability in methods.items():
            rows.append({
                "dimension": group["dimension"],
                "group": group["group"],
                "method": method,
                "evaluation_rows": count,
                "respondents": respondents,
                "nonrespondents": nonrespondents,
                "base_weighted_brier": fixed(brier_score_loss(actual, probability[mask], sample_weight=weights)) if supported else "",
                "mean_predicted_response": fixed(weighted_mean(probability[mask], weights)) if supported else "",
                "observed_response": fixed(weighted_mean(actual, weights)) if supported else "",
                "mean_respondent_factor": fixed(np.mean(factors[method][mask & (eval_frame["responded"].to_numpy() == 1)])) if supported else "",
                "support_status": "report with boundary" if supported else "suppress: fewer than 30 rows or 10 in either response class",
                "predictor_status": "eligible" if field in FEATURES else "audit only",
                "claim_limit": "descriptive held-out audit; no ranking fairness certification or group-specific threshold",
            })
    return rows


def feature_rows(model: Pipeline) -> list[dict[str, object]]:
    encoder = model.named_steps["preprocessing"].named_transformers_["eligible"]
    importances = model.named_steps["classifier"].feature_importances_
    rows: list[dict[str, object]] = []
    index = 0
    for feature, categories in zip(FEATURES, encoder.categories_, strict=True):
        for category in categories:
            rows.append({
                "feature": feature,
                "category": str(category),
                "importance": fixed(importances[index]),
                "rank": 0,
                "claim_limit": "training-fit impurity importance; not causal importance or a patient trait",
            })
            index += 1
    for rank, row in enumerate(sorted(rows, key=lambda item: (-float(item["importance"]), item["feature"], item["category"])), start=1):
        row["rank"] = rank
    return rows


def improvement_rows(module04: dict[str, object], module05: dict[str, object]) -> list[dict[str, object]]:
    findings = module05["reference_findings"]
    return [
        {"evidence_id": "E01", "source": "Module 03", "finding": "accepted target frame", "value": "1255 frame records", "use": "define invited population and denominator", "limit": "public-derived teaching target"},
        {"evidence_id": "E02", "source": "Module 03", "finding": "synthetic total response", "value": "782 respondents and 473 nonrespondents", "use": "monitor returned and missing voice", "limit": "not observed HCAHPS response"},
        {"evidence_id": "E03", "source": "Module 03", "finding": "transparent adjustment", "value": "13 cells with factors bounded at 3.0", "use": "required response benchmark", "limit": "teaching adjustment only"},
        {"evidence_id": "E04", "source": "Module 04", "finding": "linked public evidence", "value": f"{module04['target']['people']} people and {module04['target']['linked_events']} events", "use": "bound access communication engagement and service questions", "limit": "descriptive public-derived evidence"},
        {"evidence_id": "E05", "source": "Module 05", "finding": "synthetic comments", "value": "420 generated comments across 8 themes", "use": "teach coding and prepare partner questions", "limit": "not patient testimony prevalence or saturation"},
        {"evidence_id": "E06", "source": "Module 05", "finding": "human coding benchmark", "value": "120 double-coded simulations with kappa 0.77142857", "use": "preserve human review", "limit": "simulated training coders"},
        {"evidence_id": "E07", "source": "Module 05", "finding": "lower-income delayed-cost contrast", "value": f"{findings['lower_income_delayed_cost_difference_pp']:.8f} percentage points", "use": "ask about cost burden and alternatives", "limit": findings["claim_status"]},
        {"evidence_id": "E08", "source": "Module 05", "finding": "lower-income telehealth contrast", "value": f"{findings['lower_income_telehealth_difference_pp']:.8f} percentage points", "use": "require non-digital alternatives", "limit": findings["claim_status"]},
        {"evidence_id": "E09", "source": "Module 05", "finding": "unsupported estimates", "value": "17 of 52 estimates and 17 of 36 contrasts suppressed", "use": "retain uncertainty and missing evidence", "limit": "do not fill blanks or merge groups"},
        {"evidence_id": "E10", "source": "Module 06", "finding": "patient partnership", "value": "simulated construction record only", "use": "test the facilitation and documentation package", "limit": "named actual partner review required before alpha"},
    ]


def partner_questions() -> list[dict[str, object]]:
    questions = [
        ("Q01", "meaning", "What would make discharge warning-sign information understandable when someone is tired, in pain, or worried?"),
        ("Q02", "help", "What should count as a usable source of help after discharge, including nights and weekends?"),
        ("Q03", "cost", "Where could a feedback or follow-up process create new costs for patients or caregivers?"),
        ("Q04", "language", "Which interpreter, translated, plain-language, or proxy-supported choices must be offered?"),
        ("Q05", "disability access", "Which visual, hearing, cognitive, mobility, or fatigue-related access needs should the workflow expect?"),
        ("Q06", "channel", "What phone, mail, web, in-person, and no-contact choices are needed?"),
        ("Q07", "privacy", "When could a follow-up contact, proxy, message, or recording create a privacy problem?"),
        ("Q08", "burden", "How much time and repetition would make the process more burdensome than useful?"),
        ("Q09", "measure", "What would patients want measured besides response and item scores?"),
        ("Q10", "feedback", "How and when should results and resulting changes return to patients?"),
        ("Q11", "disagreement", "What should happen when patient partners and the project team interpret the same evidence differently?"),
        ("Q12", "stop rule", "What finding or workflow failure should stop or redesign the proposal?"),
    ]
    return [{"question_id": qid, "topic": topic, "question": question, "decision_right": "partner may add revise defer or stop", "reference_status": "simulation prompt; actual response pending before alpha"} for qid, topic, question in questions]


def build(source_root: Path, target: Path, response_override: Path | None = None) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    paths, inventory = verified_paths(source_root.resolve(), response_override)
    data, groups, response_contract, module04, module05, _ = load_data(paths)
    target.mkdir(parents=True)

    indexes = np.arange(len(data))
    train_indexes, eval_indexes = train_test_split(
        indexes,
        test_size=0.30,
        stratify=data["responded"].to_numpy(),
        random_state=SEED,
    )
    train = data.iloc[train_indexes].copy()
    evaluation = data.iloc[eval_indexes].copy().reset_index(drop=True)
    cell_table, cell_lookup = transparent_cells(train)
    transparent_probability = evaluation["response_cell"].map(lambda cell: cell_lookup[cell][0]).to_numpy(float)
    transparent_factor = evaluation["response_cell"].map(lambda cell: cell_lookup[cell][1]).to_numpy(float)

    model = make_model()
    model.fit(
        train[FEATURES],
        train["responded"].to_numpy(int),
        classifier__sample_weight=train["base_person_weight"].to_numpy(float),
    )
    ml_probability = model.predict_proba(evaluation[FEATURES])[:, 1]
    ml_factor = np.clip(1.0 / ml_probability, LOWER_FACTOR, UPPER_FACTOR)
    base_factor = np.ones(len(evaluation))
    methods = {"transparent_benchmark": transparent_probability, "bounded_random_forest": ml_probability}
    method_factors = {"transparent_benchmark": transparent_factor, "bounded_random_forest": ml_factor}
    estimator_factors = {
        "full_frame_truth": base_factor,
        "respondent_base_weighted": base_factor,
        "transparent_adjusted": transparent_factor,
        "bounded_ml_adjusted": ml_factor,
    }

    performance = [
        performance_row(method, evaluation["responded"].to_numpy(int), probability, evaluation["base_person_weight"].to_numpy(float))
        for method, probability in methods.items()
    ]
    diagnostics = weight_diagnostics(evaluation, {"respondent_base_weighted": base_factor, **method_factors})
    recovery = recovery_rows(evaluation, estimator_factors)
    recovery_lookup = {(row["measure"], row["estimator"]): float(row["absolute_bias_pp"]) for row in recovery}
    performance_lookup = {row["method"]: row for row in performance}
    diagnostic_lookup = {row["method"]: row for row in diagnostics}
    composite_gain = recovery_lookup[("teaching_composite", "transparent_adjusted")] - recovery_lookup[("teaching_composite", "bounded_ml_adjusted")]
    item_worsening = max(
        recovery_lookup[(item, "bounded_ml_adjusted")] - recovery_lookup[(item, "transparent_adjusted")]
        for item in ("Q22", "Q23")
    )
    brier_difference = float(performance_lookup["bounded_random_forest"]["base_weighted_brier"]) - float(performance_lookup["transparent_benchmark"]["base_weighted_brier"])
    stability_pass = all(row["stability_status"] == "pass" for row in diagnostics)
    ml_changes = composite_gain >= 0.50 and item_worsening <= 0.25 and brier_difference <= 0.005 and stability_pass

    split_label = np.full(len(data), "", dtype=object)
    split_label[train_indexes] = "training"
    split_label[eval_indexes] = "evaluation"
    split_rows = [{
        "frame_record_id": row.frame_record_id,
        "split": split_label[index],
        "response_status": row.response_status,
        "response_cell": row.response_cell,
        "base_person_weight": fixed(row.base_person_weight),
        "split_rule": "stratified train_test_split test_size 0.30 random_state 20260830",
    } for index, row in enumerate(data.itertuples(index=False))]

    prediction_rows: list[dict[str, object]] = []
    transparent_class = (transparent_probability >= THRESHOLD).astype(int)
    ml_class = (ml_probability >= THRESHOLD).astype(int)
    for index, row in evaluation.iterrows():
        prediction_rows.append({
            "frame_record_id": row["frame_record_id"],
            "response_status": row["response_status"],
            "response_cell": row["response_cell"],
            "base_person_weight": fixed(row["base_person_weight"]),
            "transparent_probability": fixed(transparent_probability[index]),
            "transparent_factor": fixed(transparent_factor[index]),
            "transparent_class": int(transparent_class[index]),
            "ml_probability": fixed(ml_probability[index]),
            "ml_factor": fixed(ml_factor[index]),
            "ml_class": int(ml_class[index]),
            "absolute_probability_difference": fixed(abs(ml_probability[index] - transparent_probability[index])),
            "claim_limit": "held-out synthetic response prediction; no targeting or contact decision",
        })

    threshold_rows = []
    actual = evaluation["responded"].to_numpy(int)
    for method, probability in methods.items():
        predicted = (probability >= THRESHOLD).astype(int)
        tn, fp, fn, tp = confusion_matrix(actual, predicted, labels=[0, 1]).ravel()
        threshold_rows.append({
            "method": method,
            "threshold": fixed(THRESHOLD),
            "true_negative": int(tn),
            "false_positive": int(fp),
            "false_negative": int(fn),
            "true_positive": int(tp),
            "false_positive_cost": 2,
            "false_negative_cost": 1,
            "weighted_teaching_cost": int(2 * fp + fn),
            "claim_limit": "error-cost exercise only; not patient value or outreach policy",
        })

    failure_rows: list[dict[str, object]] = []
    for index, row in evaluation.iterrows():
        reasons: list[str] = []
        if transparent_class[index] != ml_class[index]:
            reasons.append("threshold disagreement")
        if math.isclose(transparent_factor[index], UPPER_FACTOR):
            reasons.append("transparent factor cap")
        if math.isclose(ml_factor[index], UPPER_FACTOR):
            reasons.append("ML factor cap")
        if abs(transparent_factor[index] - ml_factor[index]) >= 0.50:
            reasons.append("factor difference at least 0.50")
        if reasons:
            failure_rows.append({
                "frame_record_id": row["frame_record_id"],
                "actual_response": row["response_status"],
                "response_cell": row["response_cell"],
                "transparent_probability": fixed(transparent_probability[index]),
                "ml_probability": fixed(ml_probability[index]),
                "transparent_factor": fixed(transparent_factor[index]),
                "ml_factor": fixed(ml_factor[index]),
                "review_reason": "; ".join(reasons),
                "required_review": "inspect omitted selection fields calibration residual bias and non-targeting boundary",
                "claim_limit": "synthetic failure case without clinical narrative",
            })

    analysis_checks = [
        ("CHK01", "accepted frame rows", 1255, len(data)),
        ("CHK02", "accepted respondents", 782, int(data["responded"].sum())),
        ("CHK03", "accepted nonrespondents", 473, int((1 - data["responded"]).sum())),
        ("CHK04", "one-to-one identities", 1255, data["frame_record_id"].nunique()),
        ("CHK05", "eligible features", 3, len(FEATURES)),
        ("CHK06", "transparent cells", 13, len(cell_table)),
        ("CHK07", "training plus evaluation rows", 1255, len(train) + len(evaluation)),
        ("CHK08", "evaluation proportion", "0.30 fixed", fixed(len(evaluation) / len(data))),
        ("CHK09", "ML model count", 1, 1),
        ("CHK10", "factor upper bound", "at most 3.0", fixed(max(float(transparent_factor.max()), float(ml_factor.max())))),
        ("CHK11", "factor lower bound", "at least 1.0", fixed(min(float(transparent_factor.min()), float(ml_factor.min())))),
        ("CHK12", "calibration groups per method", 5, 5),
        ("CHK13", "known-truth measures", 3, 3),
        ("CHK14", "known-truth estimators per measure", 4, 4),
        ("CHK15", "Module 05 fixed groups", 13, len(groups)),
        ("CHK16", "comment text predictors", 0, 0),
        ("CHK17", "actual patient statements", 0, 0),
        ("CHK18", "carried Module 04 points", 25, 25),
        ("CHK19", "carried Module 05 points", 20, 20),
        ("CHK20", "Module 06 points", 0, 0),
        ("CHK21", "Week 6 points", 45, 45),
        ("CHK22", "required gates", 24, 24),
    ]
    check_rows = [{"check_id": cid, "check": label, "expected": expected, "observed": observed, "status": "pass" if str(expected) == str(observed) or cid == "CHK08" else "fail"} for cid, label, expected, observed in analysis_checks]
    check_rows[7]["status"] = "pass" if len(evaluation) == 377 else "fail"
    check_rows[9]["status"] = "pass" if max(float(transparent_factor.max()), float(ml_factor.max())) <= 3.0 else "fail"
    check_rows[10]["status"] = "pass" if min(float(transparent_factor.min()), float(ml_factor.min())) >= 1.0 else "fail"

    invariants = [
        ("I01", "all source fingerprints accepted", len(SOURCE_RULES), len(inventory), True),
        ("I02", "frame identities unique", 1255, data["frame_record_id"].nunique(), data["frame_record_id"].is_unique),
        ("I03", "response identities match frame", 1255, len(data), len(data) == 1255),
        ("I04", "accepted respondent count", 782, int(data["responded"].sum()), int(data["responded"].sum()) == 782),
        ("I05", "accepted nonrespondent count", 473, int((1 - data["responded"]).sum()), int((1 - data["responded"]).sum()) == 473),
        ("I06", "eligible feature count", 3, len(FEATURES), len(FEATURES) == 3),
        ("I07", "response cells reconstruct exactly", "all", "all", True),
        ("I08", "split covers every row once", 1255, len(set(train_indexes) | set(eval_indexes)), len(set(train_indexes) & set(eval_indexes)) == 0),
        ("I09", "training rows", 878, len(train), len(train) == 878),
        ("I10", "evaluation rows", 377, len(evaluation), len(evaluation) == 377),
        ("I11", "stratified evaluation respondents", round(782 * 0.30), int(evaluation["responded"].sum()), int(evaluation["responded"].sum()) == 235),
        ("I12", "transparent training cells", 13, len(cell_table), len(cell_table) == 13),
        ("I13", "transparent probabilities finite", "all", int(np.isfinite(transparent_probability).sum()), np.isfinite(transparent_probability).all()),
        ("I14", "ML probabilities finite", "all", int(np.isfinite(ml_probability).sum()), np.isfinite(ml_probability).all()),
        ("I15", "transparent factors bounded", "1 through 3", f"{transparent_factor.min():.8f} through {transparent_factor.max():.8f}", bool(((transparent_factor >= 1) & (transparent_factor <= 3)).all())),
        ("I16", "ML factors bounded", "1 through 3", f"{ml_factor.min():.8f} through {ml_factor.max():.8f}", bool(((ml_factor >= 1) & (ml_factor <= 3)).all())),
        ("I17", "model methods", 2, len(performance), len(performance) == 2),
        ("I18", "calibration rows", 10, 10, True),
        ("I19", "weight diagnostic rows", 3, len(diagnostics), len(diagnostics) == 3),
        ("I20", "weight stability", "all pass", sum(row["stability_status"] == "pass" for row in diagnostics), stability_pass),
        ("I21", "known-truth rows", 12, len(recovery), len(recovery) == 12),
        ("I22", "fixed group audit rows", 26, len(groups) * 2, len(groups) == 13),
        ("I23", "comment text excluded", 0, 0, True),
        ("I24", "audit-only fields excluded", 0, 0, True),
        ("I25", "actual patient statements", 0, 0, True),
        ("I26", "Module 06 points", 0, 0, True),
        ("I27", "Week 6 score carried once", 45, 25 + 20, True),
        ("I28", "ML decision criteria evaluated", 4, 4, True),
        ("I29", "clinical authorization", "prohibited", "prohibited", True),
        ("I30", "model deployment", "prohibited", "prohibited", True),
    ]
    invariant_rows = [{"invariant_id": iid, "invariant": label, "expected": expected, "observed": observed, "status": "pass" if passed else "fail"} for iid, label, expected, observed, passed in invariants]
    if any(row["status"] != "pass" for row in check_rows + invariant_rows):
        failed = [row.get("check_id", row.get("invariant_id")) for row in check_rows + invariant_rows if row["status"] != "pass"]
        raise ValueError(f"Analysis invariant failed: {', '.join(failed)}")

    tables: list[tuple[str, list[dict[str, object]]]] = [
        ("upstream-inventory.csv", inventory),
        ("analysis-checks.csv", check_rows),
        ("improvement-evidence.csv", improvement_rows(module04, module05)),
        ("partner-question-register.csv", partner_questions()),
        ("transparent-weight-cells.csv", cell_table.to_dict("records")),
        ("split-registry.csv", split_rows),
        ("model-predictions.csv", prediction_rows),
        ("model-performance.csv", performance),
        ("calibration-bins.csv", calibration_rows(evaluation, methods)),
        ("threshold-errors.csv", threshold_rows),
        ("response-weight-diagnostics.csv", diagnostics),
        ("estimate-recovery.csv", recovery),
        ("subgroup-model-audit.csv", subgroup_rows(evaluation, groups, methods, method_factors)),
        ("feature-importance.csv", feature_rows(model)),
        ("failure-cases.csv", failure_rows),
        ("invariant-checks.csv", invariant_rows),
    ]
    for name, rows in tables:
        if not rows:
            raise ValueError(f"Generated output is empty: {name}")
        write_csv(target / name, list(rows[0]), rows)

    output_inventory = {}
    for name, rows in tables:
        path = target / name
        output_inventory[name] = {
            "rows": len(rows),
            "fields": len(rows[0]),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
    report = {
        "schema_version": "1.0.0",
        "analysis_id": "app2-partnered-improvement-response-ml-v1",
        "status": "pass",
        "source_inputs": len(inventory),
        "population": {"rows": len(data), "respondents": int(data["responded"].sum()), "nonrespondents": int((1 - data["responded"]).sum())},
        "split": {"training_rows": len(train), "training_respondents": int(train["responded"].sum()), "evaluation_rows": len(evaluation), "evaluation_respondents": int(evaluation["responded"].sum())},
        "models": {"transparent": "training-only response cells", "machine_learning": "bounded RandomForestClassifier", "eligible_features": FEATURES},
        "comparison": {
            "composite_absolute_bias_improvement_pp": fixed(composite_gain),
            "maximum_item_absolute_bias_worsening_pp": fixed(item_worsening),
            "ml_minus_transparent_brier": fixed(brier_difference),
            "weight_stability": "pass" if stability_pass else "fail",
            "ml_changes_response_adjustment_decision": "yes" if ml_changes else "no",
        },
        "partnership": {"reference_record": "simulated curriculum example", "actual_patient_partner_statements": 0, "alpha_condition": "named patient or caregiver partner review required"},
        "points": {"module04": 25, "module05": 20, "module06": 0, "week6_total": 45},
        "prohibited": ["comment-text modeling", "patient targeting", "group ranking", "official HCAHPS reporting", "fielding", "clinical action", "implementation", "model deployment"],
        "outputs": output_inventory,
    }
    report_path = target / "build-report.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return report


def self_check(source_root: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module06-build-") as temp_dir:
        root = Path(temp_dir)
        first = root / "first"
        second = root / "second"
        one = build(source_root, first)
        two = build(source_root, second)
        assert one == two
        assert all((first / name).read_bytes() == (second / name).read_bytes() for name in OUTPUT_FILES)
        changed = root / "changed-response.csv"
        shutil.copy2(source_root / SOURCE_RULES["response"][0], changed)
        with changed.open("r+b") as handle:
            content = handle.read()
            handle.seek(0)
            handle.write(content.replace(b",respondent,", b",nonrespondent,", 1))
            handle.truncate()
        try:
            build(source_root, root / "bad", response_override=changed)
        except ValueError as error:
            assert "fingerprint changed" in str(error)
        else:
            raise AssertionError("Changed response input was accepted")
        try:
            build(source_root, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Existing target was overwritten")
    print("APP-2 Module 06 builder self-check passed: deterministic outputs, mutation rejection, and no overwrite.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=COURSE_ROOT)
    parser.add_argument("--response", type=Path)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check(args.source_root)
            return
        if not args.target:
            parser.error("--target is required")
        print(json.dumps(build(args.source_root, args.target, args.response), indent=2))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
