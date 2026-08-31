"""Build APP-5 Module 06 intervention, monitoring, and clustering evidence."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import tempfile
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import MinMaxScaler, Normalizer, RobustScaler, StandardScaler


ROOT = Path(__file__).resolve().parent
MODULE_ID = "oclc-app5-06"
MODULE_VERSION = "0.1.0"
COMMONS_RELEASE = "0.93.0"
EXPECTED_REPORT_SHA256 = "f53dc9a5b3274ee33917a3f78d1b0152f1dcaca232bc07de3b39045e5246f6f7"

OUTPUT_FILES = {
    "source-profile.csv",
    "intervention-readiness.csv",
    "dry-run-reconciliation.csv",
    "monitoring-results.csv",
    "escalation-results.csv",
    "feedback-recourse-results.csv",
    "cluster-feature-matrix.csv.gz",
    "cluster-assignments.csv.gz",
    "cluster-profiles.csv",
    "cluster-support-geography.csv",
    "selected-tract-cluster-review.csv",
    "challenger-stability.csv",
    "query-checks.csv",
    "build-report.json",
}


class BuildError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BuildError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_bytes(fields: list[str], rows: list[dict[str, object]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def write_rows(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    raw = csv_bytes(fields, rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".gz":
        output = io.BytesIO()
        with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
            zipped.write(raw)
        path.write_bytes(output.getvalue())
    else:
        path.write_bytes(raw)


def text_number(value: float) -> str:
    return f"{value:.6f}".rstrip("0").rstrip(".")


def load_inputs(root: Path) -> dict[str, list[dict[str, str]]]:
    upstream = root / "upstream/module05-reference/outputs"
    inputs = {
        "candidates": read_csv(upstream / "linked-candidate-table.csv.gz"),
        "assignments": read_csv(upstream / "rule-assignments.csv.gz"),
        "dry_run": read_csv(root / "data/raw/fictional-monitoring-dry-run.csv.gz"),
        "measures": read_csv(root / "data/monitoring-measures.csv"),
        "features": read_csv(root / "data/cluster-feature-contract.csv"),
        "variants": read_csv(root / "data/challenger-variants.csv"),
    }
    require(len(inputs["candidates"]) == 1597, "Candidate row count changed")
    require(len(inputs["assignments"]) == 6388, "Rule assignment count changed")
    require(len(inputs["dry_run"]) == 280, "Dry-run count changed")
    require(len(inputs["measures"]) == 20, "Monitoring registry changed")
    require(len(inputs["features"]) == 9, "Feature contract changed")
    require(len(inputs["variants"]) == 8, "Challenger contract changed")
    return inputs


def selected_assignments(assignments: list[dict[str, str]]) -> list[dict[str, str]]:
    selected = sorted(
        (row for row in assignments if row["rule_id"] == "community_review" and row["selected"] == "1"),
        key=lambda row: int(row["selection_order"]),
    )
    require(len(selected) == 28, "Accepted community-review selection changed")
    require(sum(int(row["allocated_places"]) for row in selected) == 280, "Accepted resource changed")
    return selected


def build_intervention_rows(selected: list[dict[str, str]]) -> list[dict[str, object]]:
    rows = []
    for row in selected:
        conditions = []
        if row["fictional_staff_readiness"] == "not_ready":
            conditions.append("staff owner review")
        if int(row["fictional_travel_minutes"]) >= 60:
            conditions.append("travel and modality revision")
        if int(row["fictional_delivery_burden_score"]) >= 4:
            conditions.append("burden revision")
        rows.append(
            {
                "tract_fips": row["tract_fips"],
                "county_fips": row["county_fips"],
                "county_name": row["county_name"],
                "selection_order": row["selection_order"],
                "fictional_places": row["allocated_places"],
                "staff_readiness": row["fictional_staff_readiness"],
                "high_travel_concern": "yes" if int(row["fictional_travel_minutes"]) >= 60 else "no",
                "high_burden_concern": "yes" if int(row["fictional_delivery_burden_score"]) >= 4 else "no",
                "language_access_ready": row["fictional_language_access_ready"],
                "disability_access_ready": row["fictional_disability_access_ready"],
                "community_review_state": row["fictional_community_review_state"],
                "owner_condition": "; ".join(conditions) if conditions else "none",
                "readiness_state": "hold_for_human_revision" if conditions else "ready_for_fictional_dry_run",
                "automatic_action": "no",
                "authority_limit": "not real eligibility, outreach, allocation, service, or implementation readiness",
            }
        )
    return rows


def build_reconciliation(selected: list[dict[str, str]], dry_run: list[dict[str, str]]) -> list[dict[str, object]]:
    by_tract: dict[str, list[dict[str, str]]] = {}
    for row in dry_run:
        by_tract.setdefault(row["tract_fips"], []).append(row)
    rows = []
    for area in selected:
        tests = by_tract.get(area["tract_fips"], [])
        rows.append(
            {
                "tract_fips": area["tract_fips"],
                "expected_fictional_places": area["allocated_places"],
                "dry_run_records": len(tests),
                "processed_offer_tests": sum(row["offer_test_state"] == "processed" for row in tests),
                "held_for_readiness_tests": sum(row["offer_test_state"] == "held_for_readiness" for row in tests),
                "language_access_failures": sum(row["language_access_test_state"] == "unavailable" for row in tests),
                "disability_access_failures": sum(row["disability_access_test_state"] == "unavailable" for row in tests),
                "objection_tests": sum(row["objection_test_state"] != "none" for row in tests),
                "incident_tests": sum(row["incident_test_state"] != "none" for row in tests),
                "pause_tests": sum(row["pause_test_triggered"] == "yes" for row in tests),
                "outcome_records": sum(row["outcome_available"] == "yes" for row in tests),
                "reconciled": "yes" if len(tests) == int(area["allocated_places"]) else "no",
                "interpretation_limit": "fictional software and governance tests, not people or observed services",
            }
        )
    require(len(rows) == 28 and all(row["reconciled"] == "yes" for row in rows), "Dry-run reconciliation failed")
    return rows


def build_monitoring(measures: list[dict[str, str]], selected: list[dict[str, str]], dry_run: list[dict[str, str]]) -> list[dict[str, object]]:
    processed = [row for row in dry_run if row["offer_test_state"] == "processed"]
    interested = [row for row in processed if row["response_test_state"] == "interested"]
    scheduled = [row for row in interested if row["scheduling_test_state"] == "scheduled"]
    attended = [row for row in scheduled if row["attendance_test_state"] == "attended"]
    language_need = [row for row in dry_run if row["language_access_need_test"] == "yes"]
    disability_need = [row for row in dry_run if row["disability_access_need_test"] == "yes"]
    objections = [row for row in dry_run if row["objection_test_state"] != "none"]
    incidents = [row for row in dry_run if row["incident_test_state"] != "none"]
    pause_required = [row for row in dry_run if row["offer_test_state"] == "held_for_readiness" or row["objection_test_state"] != "none" or row["incident_test_state"] in {"access_failure", "privacy_near_miss"}]
    counts = {
        "M01": (sum(row["fictional_staff_readiness"] != "not_ready" for row in selected), len(selected)),
        "M02": (sum(int(row["fictional_travel_minutes"]) < 60 for row in selected), len(selected)),
        "M03": (len(processed), len(dry_run)),
        "M04": (sum(row["response_test_state"] in {"interested", "declined", "no_response"} for row in processed), len(processed)),
        "M05": (len(interested), len(processed)),
        "M06": (sum(row["response_test_state"] == "declined" for row in processed), len(processed)),
        "M07": (sum(row["language_access_test_state"] == "provided" for row in language_need), len(language_need)),
        "M08": (sum(row["disability_access_test_state"] == "provided" for row in disability_need), len(disability_need)),
        "M09": (len(scheduled), len(interested)),
        "M10": (len(attended), len(scheduled)),
        "M11": (sum(row["completion_test_state"] == "complete" for row in attended), len(attended)),
        "M12": (sum(row["fidelity_test_state"] == "pass" for row in attended), len(attended)),
        "M13": (sum(int(row["burden_test_score"]) <= 3 for row in processed), len(processed)),
        "M14": (sum(bool(row["feedback_test_state"]) for row in processed), len(processed)),
        "M15": (sum(row["pause_test_triggered"] == "yes" for row in objections), len(objections)),
        "M16": (sum(row["incident_test_state"] == "none" for row in processed), len(processed)),
        "M17": (sum(row["escalation_test_route"] != "none" for row in incidents), len(incidents)),
        "M18": (sum(row["pause_test_triggered"] == "yes" for row in pause_required), len(pause_required)),
        "M19": (sum(row["outcome_available"] == "yes" for row in dry_run), len(dry_run)),
        "M20": (0, len(dry_run)),
    }
    rows = []
    for measure in measures:
        numerator, denominator = counts[measure["measure_id"]]
        value = numerator / denominator if denominator else None
        threshold = measure["teaching_threshold"]
        if value is None:
            result = "unavailable"
            trigger = "human_review_required"
        elif threshold == "none" or measure["direction"] == "descriptive":
            result = "descriptive_only"
            trigger = "not_applicable"
        else:
            target = float(threshold)
            passed = value >= target if measure["direction"] == "higher" else value <= target
            result = "pass" if passed else "triggered"
            trigger = "no" if passed else "yes"
        rows.append(
            {
                **measure,
                "numerator": numerator,
                "denominator": denominator,
                "observed_value": "unavailable" if value is None else text_number(value),
                "result": result,
                "review_triggered": trigger,
                "automatic_action": "no",
            }
        )
    return rows


def build_event_summaries(dry_run: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    escalation_rows = []
    for incident in sorted({row["incident_test_state"] for row in dry_run}):
        records = [row for row in dry_run if row["incident_test_state"] == incident]
        escalation_rows.append(
            {
                "incident_test_state": incident,
                "records": len(records),
                "named_route_records": sum(row["escalation_test_route"] != "none" for row in records),
                "pause_records": sum(row["pause_test_triggered"] == "yes" for row in records),
                "owner": "monitoring owner" if incident == "none" else "program steward and named incident owner",
                "required_response": "retain for descriptive audit" if incident == "none" else "human investigation, correction, and stop review",
                "automatic_action": "no",
            }
        )
    feedback_rows = []
    for state in sorted({row["feedback_test_state"] for row in dry_run}):
        records = [row for row in dry_run if row["feedback_test_state"] == state]
        feedback_rows.append(
            {
                "feedback_test_state": state,
                "records": len(records),
                "objection_records": sum(row["objection_test_state"] != "none" for row in records),
                "pause_records": sum(row["pause_test_triggered"] == "yes" for row in records),
                "recourse_route": "hold, community review, correction, appeal, and stop" if state == "objection" else "question, correction, refusal, and withdrawal remain open",
                "owner": "community accountability owner",
                "automatic_action": "no",
            }
        )
    return escalation_rows, feedback_rows


FEATURE_NAMES = [
    "modeled_crude_prevalence_percent",
    "interval_width_percentage_points",
    "log1p_places_adult_population_field",
    "fictional_capacity_places",
    "fictional_travel_minutes",
    "fictional_delivery_burden_score",
    "fictional_language_access_ready",
    "fictional_disability_access_ready",
    "fictional_staff_readiness",
]


def feature_matrix(candidates: list[dict[str, str]]) -> tuple[np.ndarray, list[dict[str, object]]]:
    values = []
    rows = []
    for candidate in candidates:
        required = [
            "modeled_crude_prevalence_percent", "interval_width_percentage_points", "places_adult_population_field",
            "fictional_capacity_places", "fictional_travel_minutes", "fictional_delivery_burden_score",
            "fictional_language_access_ready", "fictional_disability_access_ready", "fictional_staff_readiness",
        ]
        require(all(candidate.get(field, "") != "" for field in required), f"Missing feature for {candidate['tract_fips']}")
        vector = [
            float(candidate["modeled_crude_prevalence_percent"]),
            float(candidate["interval_width_percentage_points"]),
            math.log1p(float(candidate["places_adult_population_field"])),
            float(candidate["fictional_capacity_places"]),
            float(candidate["fictional_travel_minutes"]),
            float(candidate["fictional_delivery_burden_score"]),
            1.0 if candidate["fictional_language_access_ready"] in {"1", "yes"} else 0.0,
            1.0 if candidate["fictional_disability_access_ready"] in {"1", "yes"} else 0.0,
            1.0 if candidate["fictional_staff_readiness"] == "ready" else 0.0,
        ]
        require(all(math.isfinite(value) for value in vector), f"Nonfinite feature for {candidate['tract_fips']}")
        values.append(vector)
        rows.append(
            {
                "tract_fips": candidate["tract_fips"],
                "county_fips": candidate["county_fips"],
                "county_name": candidate["county_name"],
                "support_state": candidate["support_state"],
                **{name: text_number(value) for name, value in zip(FEATURE_NAMES, vector)},
                "selection_label_used_as_feature": "no",
                "interpretation_limit": "area-profile teaching feature, not individual trait, need, eligibility, or priority",
            }
        )
    matrix = np.asarray(values, dtype=float)
    require(matrix.shape == (1597, 9), "Feature matrix shape changed")
    return matrix, rows


def scale_matrix(matrix: np.ndarray, scaling: str) -> np.ndarray:
    scalers = {
        "standard": StandardScaler(),
        "robust": RobustScaler(),
        "minmax": MinMaxScaler(),
        "unitnorm": Normalizer(norm="l2"),
    }
    require(scaling in scalers, f"Unknown scaling: {scaling}")
    return scalers[scaling].fit_transform(matrix)


def canonical_labels(labels: np.ndarray, raw_matrix: np.ndarray) -> tuple[list[str], dict[int, str]]:
    centers = {cluster: tuple(np.mean(raw_matrix[labels == cluster], axis=0)) for cluster in sorted(set(labels))}
    mapping = {cluster: f"C{position:02d}" for position, cluster in enumerate(sorted(centers, key=centers.get), 1)}
    return [mapping[int(label)] for label in labels], mapping


def fit_variant(matrix: np.ndarray, variant: dict[str, str]) -> dict[str, object]:
    scaled = scale_matrix(matrix, variant["scaling"])
    model = KMeans(
        n_clusters=int(variant["clusters"]),
        random_state=int(variant["seed"]),
        n_init=20,
        algorithm="lloyd",
    ).fit(scaled)
    labels, mapping = canonical_labels(model.labels_, matrix)
    distances = np.linalg.norm(scaled - model.cluster_centers_[model.labels_], axis=1)
    return {
        "labels": labels,
        "numeric_labels": model.labels_,
        "mapping": mapping,
        "distance": distances,
        "inertia": float(model.inertia_),
    }


def build_clusters(
    candidates: list[dict[str, str]],
    selected: list[dict[str, str]],
    variants: list[dict[str, str]],
) -> dict[str, object]:
    matrix, matrix_rows = feature_matrix(candidates)
    fitted = {variant["variant_id"]: fit_variant(matrix, variant) for variant in variants}
    base = fitted["base"]
    selected_keys = {row["tract_fips"] for row in selected}
    assignments = []
    for index, candidate in enumerate(candidates):
        assignments.append(
            {
                "tract_fips": candidate["tract_fips"],
                "county_fips": candidate["county_fips"],
                "county_name": candidate["county_name"],
                "cluster_id": base["labels"][index],
                "distance_to_scaled_center": text_number(float(base["distance"][index])),
                "community_review_selected": "yes" if candidate["tract_fips"] in selected_keys else "no",
                "cluster_used_to_change_selection": "no",
                "automatic_action": "no",
                "interpretation_limit": "descriptive area-profile challenger only, not need, ranking, fairness, eligibility, or allocation",
            }
        )

    candidate_by_key = {row["tract_fips"]: row for row in candidates}
    assignment_by_key = {row["tract_fips"]: row for row in assignments}
    selected_review = []
    for row in selected:
        candidate = candidate_by_key[row["tract_fips"]]
        assignment = assignment_by_key[row["tract_fips"]]
        selected_review.append(
            {
                "tract_fips": row["tract_fips"],
                "county_fips": row["county_fips"],
                "county_name": row["county_name"],
                "selection_order": row["selection_order"],
                "fictional_places": row["allocated_places"],
                "cluster_id": assignment["cluster_id"],
                "staff_readiness": candidate["fictional_staff_readiness"],
                "high_travel_concern": "yes" if int(candidate["fictional_travel_minutes"]) >= 60 else "no",
                "high_burden_concern": "yes" if int(candidate["fictional_delivery_burden_score"]) >= 4 else "no",
                "selection_preserved": "yes",
                "tailoring_question_only": "yes",
                "automatic_action": "no",
                "interpretation_limit": "cluster cannot alter the transparent community-review comparison",
            }
        )

    profiles = []
    for cluster in sorted(set(base["labels"])):
        indexes = [index for index, label in enumerate(base["labels"]) if label == cluster]
        subset = matrix[indexes]
        cluster_candidates = [candidates[index] for index in indexes]
        profiles.append(
            {
                "cluster_id": cluster,
                "tracts": len(indexes),
                "counties": len({row["county_fips"] for row in cluster_candidates}),
                "limited_support_tracts": sum(row["support_state"] == "limited_support" for row in cluster_candidates),
                "community_review_selected_tracts": sum(row["tract_fips"] in selected_keys for row in cluster_candidates),
                **{f"mean_{name}": text_number(float(np.mean(subset[:, position]))) for position, name in enumerate(FEATURE_NAMES)},
                "interpretation_limit": "descriptive area-profile summary, not an individual or causal group",
            }
        )

    geography = []
    counties = sorted({(row["county_fips"], row["county_name"]) for row in candidates})
    for cluster in sorted(set(base["labels"])):
        cluster_rows = [candidate for candidate, label in zip(candidates, base["labels"]) if label == cluster]
        for county_fips, county_name in counties:
            county_rows = [row for row in cluster_rows if row["county_fips"] == county_fips]
            geography.append(
                {
                    "cluster_id": cluster,
                    "county_fips": county_fips,
                    "county_name": county_name,
                    "tracts": len(county_rows),
                    "cluster_share": text_number(len(county_rows) / len(cluster_rows)),
                    "limited_support_tracts": sum(row["support_state"] == "limited_support" for row in county_rows),
                    "selected_tracts": sum(row["tract_fips"] in selected_keys for row in county_rows),
                    "interpretation_limit": "support and concentration review, not county need or performance",
                }
            )

    base_numeric = np.asarray(base["numeric_labels"])
    stability = []
    scaling_aris = []
    for variant in variants:
        result = fitted[variant["variant_id"]]
        numeric = np.asarray(result["numeric_labels"])
        counts = Counter(result["labels"])
        ari = adjusted_rand_score(base_numeric, numeric)
        if variant["variant_type"] == "scaling":
            scaling_aris.append(ari)
        selected_cluster_count = len({result["labels"][index] for index, candidate in enumerate(candidates) if candidate["tract_fips"] in selected_keys})
        stability.append(
            {
                "variant_id": variant["variant_id"],
                "variant_type": variant["variant_type"],
                "scaling": variant["scaling"],
                "seed": variant["seed"],
                "adjusted_rand_vs_base": text_number(ari),
                "nonempty_clusters": len(counts),
                "smallest_cluster": min(counts.values()),
                "largest_cluster": max(counts.values()),
                "selected_clusters": selected_cluster_count,
                "inertia": text_number(float(result["inertia"])),
                "automatic_action": "no",
                "interpretation_limit": "stability diagnostic, not model validity, fairness, need, or authority",
            }
        )
    alternate_seed_aris = [float(row["adjusted_rand_vs_base"]) for row in stability if row["variant_type"] == "seed"]
    base_counts = Counter(base["labels"])
    scaling_median = float(np.median(scaling_aris))
    stable_enough = (
        len(base_counts) == 4
        and min(base_counts.values()) >= 80
        and all(value >= 0.80 for value in alternate_seed_aris)
        and scaling_median >= 0.60
        and len({row["cluster_id"] for row in selected_review}) >= 3
    )
    for row in stability:
        row["scaling_variant_median_ari"] = text_number(scaling_median)
        row["challenger_stable_for_bounded_questions"] = "yes" if stable_enough else "no"
        row["challenger_use"] = "bounded descriptive tailoring questions" if stable_enough else "not useful; preserve transparent rule only"

    return {
        "matrix_rows": matrix_rows,
        "assignments": assignments,
        "profiles": profiles,
        "geography": geography,
        "selected_review": selected_review,
        "stability": stability,
        "stable_enough": stable_enough,
        "scaling_median": scaling_median,
        "base_minimum": min(base_counts.values()),
        "selected_clusters": len({row["cluster_id"] for row in selected_review}),
        "alternate_seed_minimum": min(alternate_seed_aris),
    }


def build_checks(
    inputs: dict[str, list[dict[str, str]]],
    selected: list[dict[str, str]],
    intervention: list[dict[str, object]],
    reconciliation: list[dict[str, object]],
    monitoring: list[dict[str, object]],
    escalation: list[dict[str, object]],
    feedback: list[dict[str, object]],
    clusters: dict[str, object],
) -> list[dict[str, object]]:
    dry_run = inputs["dry_run"]
    checks: list[dict[str, object]] = []

    def check(check_id: str, name: str, actual: object, expected: object) -> None:
        checks.append(
            {
                "check_id": check_id,
                "check_name": name,
                "actual": actual,
                "expected": expected,
                "status": "pass" if str(actual) == str(expected) else "fail",
            }
        )

    check("Q01", "accepted candidate rows", len(inputs["candidates"]), 1597)
    check("Q02", "accepted rule assignments", len(inputs["assignments"]), 6388)
    check("Q03", "carried selected tracts", len(selected), 28)
    check("Q04", "carried fictional places", sum(int(row["allocated_places"]) for row in selected), 280)
    check("Q05", "dry-run records", len(dry_run), 280)
    check("Q06", "unique dry-run tests", len({row["fictional_test_id"] for row in dry_run}), 280)
    check("Q07", "staff-not-ready concerns", sum(row["fictional_staff_readiness"] == "not_ready" for row in selected), 5)
    check("Q08", "high-travel concerns", sum(int(row["fictional_travel_minutes"]) >= 60 for row in selected), 12)
    check("Q09", "high-burden concerns", sum(int(row["fictional_delivery_burden_score"]) >= 4 for row in selected), 1)
    check("Q10", "selected counties", len({row["county_fips"] for row in selected}), 11)
    check("Q11", "language-access gaps", sum(row["fictional_language_access_ready"] not in {"1", "yes"} for row in selected), 0)
    check("Q12", "disability-access gaps", sum(row["fictional_disability_access_ready"] not in {"1", "yes"} for row in selected), 0)
    check("Q13", "unresolved selected questions", sum(int(row["fictional_unresolved_questions"]) for row in selected), 0)
    check("Q14", "intervention readiness rows", len(intervention), 28)
    check("Q15", "automatic intervention actions", sum(row["automatic_action"] != "no" for row in intervention), 0)
    check("Q16", "reconciled selected areas", sum(row["reconciled"] == "yes" for row in reconciliation), 28)
    check("Q17", "reconciled fictional records", sum(int(row["dry_run_records"]) for row in reconciliation), 280)
    check("Q18", "readiness-held tests", sum(row["offer_test_state"] == "held_for_readiness" for row in dry_run), 50)
    check("Q19", "outcome records", sum(row["outcome_available"] == "yes" for row in dry_run), 0)
    check("Q20", "public prevalence generated records", sum(row["public_prevalence_used_to_generate"] != "no" for row in dry_run), 0)
    check("Q21", "monitoring measures", len(monitoring), 20)
    check("Q22", "monitoring records with denominators", sum(int(row["denominator"]) > 0 for row in monitoring), 20)
    check("Q23", "automatic monitoring actions", sum(row["automatic_action"] != "no" for row in monitoring), 0)
    check("Q24", "hidden unavailable results", sum(row["observed_value"] == "unavailable" for row in monitoring), 0)
    incident_count = sum(row["incident_test_state"] != "none" for row in dry_run)
    check("Q25", "incident routes named", sum(int(row["named_route_records"]) for row in escalation), incident_count)
    pause_required = sum(row["offer_test_state"] == "held_for_readiness" or row["objection_test_state"] != "none" or row["incident_test_state"] in {"access_failure", "privacy_near_miss"} for row in dry_run)
    check("Q26", "required pauses honored", sum(row["pause_test_triggered"] == "yes" and (row["offer_test_state"] == "held_for_readiness" or row["objection_test_state"] != "none" or row["incident_test_state"] in {"access_failure", "privacy_near_miss"}) for row in dry_run), pause_required)
    check("Q27", "feedback states reported", len(feedback), len({row["feedback_test_state"] for row in dry_run}))
    check("Q28", "objection tests present", sum(row["objection_test_state"] != "none" for row in dry_run) > 0, True)
    check("Q29", "incident states reported", len(escalation), len({row["incident_test_state"] for row in dry_run}))
    check("Q30", "cluster feature rows", len(clusters["matrix_rows"]), 1597)
    check("Q31", "fixed feature count", len(FEATURE_NAMES), 9)
    check("Q32", "selection label excluded from features", sum(row["selection_label_used_as_feature"] != "no" for row in clusters["matrix_rows"]), 0)
    check("Q33", "cluster assignments", len(clusters["assignments"]), 1597)
    check("Q34", "base clusters", len(clusters["profiles"]), 4)
    check("Q35", "base support result recorded", int(clusters["base_minimum"]) > 0, True)
    check("Q36", "cluster profiles", len(clusters["profiles"]), 4)
    check("Q37", "cluster by county rows", len(clusters["geography"]), 56)
    check("Q38", "selected cluster review rows", len(clusters["selected_review"]), 28)
    check("Q39", "selected comparison preserved", sum(row["selection_preserved"] == "yes" for row in clusters["selected_review"]), 28)
    check("Q40", "selected cluster coverage recorded", len({row["cluster_id"] for row in clusters["selected_review"]}), clusters["selected_clusters"])
    check("Q41", "challenger variants", len(clusters["stability"]), 8)
    check("Q42", "alternate seed variants", sum(row["variant_type"] == "seed" for row in clusters["stability"]), 4)
    check("Q43", "scaling variants", sum(row["variant_type"] == "scaling" for row in clusters["stability"]), 3)
    check("Q44", "stability values recorded", sum(row["adjusted_rand_vs_base"] != "" for row in clusters["stability"]), 8)
    check("Q45", "automatic cluster actions", sum(row["automatic_action"] != "no" for row in clusters["assignments"]), 0)
    check("Q46", "cluster changed selections", sum(row["cluster_used_to_change_selection"] != "no" for row in clusters["assignments"]), 0)
    check("Q47", "real implementation-ready rows", sum("real" not in row["authority_limit"] for row in intervention), 0)
    check("Q48", "challenger decision recorded", clusters["stable_enough"] in {True, False}, True)
    failed = [row["check_id"] for row in checks if row["status"] != "pass"]
    require(len(checks) == 48 and not failed, f"Query checks failed: {', '.join(failed)}")
    return checks


def output_metadata(path: Path) -> dict[str, object]:
    rows = read_csv(path)
    return {
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "rows": len(rows),
        "columns": len(rows[0]) if rows else 0,
    }


def generate(target: Path, root: Path = ROOT) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    target.mkdir(parents=True)
    inputs = load_inputs(root)
    selected = selected_assignments(inputs["assignments"])
    intervention = build_intervention_rows(selected)
    reconciliation = build_reconciliation(selected, inputs["dry_run"])
    monitoring = build_monitoring(inputs["measures"], selected, inputs["dry_run"])
    escalation, feedback = build_event_summaries(inputs["dry_run"])
    clusters = build_clusters(inputs["candidates"], selected, inputs["variants"])
    checks = build_checks(inputs, selected, intervention, reconciliation, monitoring, escalation, feedback, clusters)

    profile = [{
        "module_id": MODULE_ID,
        "module_version": MODULE_VERSION,
        "commons_release": COMMONS_RELEASE,
        "module05_handoff_sha256": sha256(root / "upstream/module05-handoff-manifest.csv"),
        "module05_reference_files": 340,
        "candidate_rows": len(inputs["candidates"]),
        "selected_tracts": len(selected),
        "fictional_places": sum(int(row["allocated_places"]) for row in selected),
        "dry_run_source_id": inputs["dry_run"][0]["synthetic_source_id"],
        "dry_run_rows": len(inputs["dry_run"]),
        "monitoring_measures": len(inputs["measures"]),
        "cluster_features": len(inputs["features"]),
        "cluster_variants": len(inputs["variants"]),
        "public_evidence_role": "accepted area-level context only",
        "synthetic_evidence_role": "fictional intervention and monitoring software test only",
        "interpretation_limit": "no real need, consent, eligibility, outreach, allocation, service, effect, implementation, production, or deployment conclusion",
    }]

    write_rows(target / "source-profile.csv", list(profile[0]), profile)
    write_rows(target / "intervention-readiness.csv", list(intervention[0]), intervention)
    write_rows(target / "dry-run-reconciliation.csv", list(reconciliation[0]), reconciliation)
    write_rows(target / "monitoring-results.csv", list(monitoring[0]), monitoring)
    write_rows(target / "escalation-results.csv", list(escalation[0]), escalation)
    write_rows(target / "feedback-recourse-results.csv", list(feedback[0]), feedback)
    write_rows(target / "cluster-feature-matrix.csv.gz", list(clusters["matrix_rows"][0]), clusters["matrix_rows"])
    write_rows(target / "cluster-assignments.csv.gz", list(clusters["assignments"][0]), clusters["assignments"])
    write_rows(target / "cluster-profiles.csv", list(clusters["profiles"][0]), clusters["profiles"])
    write_rows(target / "cluster-support-geography.csv", list(clusters["geography"][0]), clusters["geography"])
    write_rows(target / "selected-tract-cluster-review.csv", list(clusters["selected_review"][0]), clusters["selected_review"])
    write_rows(target / "challenger-stability.csv", list(clusters["stability"][0]), clusters["stability"])
    write_rows(target / "query-checks.csv", list(checks[0]), checks)

    generated = sorted(path for path in target.iterdir() if path.name != "build-report.json")
    report = {
        "module_id": MODULE_ID,
        "module_version": MODULE_VERSION,
        "commons_release": COMMONS_RELEASE,
        "findings": {
            "candidate_rows": len(inputs["candidates"]),
            "selected_tracts": len(selected),
            "fictional_places": 280,
            "dry_run_rows": len(inputs["dry_run"]),
            "staff_not_ready": sum(row["fictional_staff_readiness"] == "not_ready" for row in selected),
            "high_travel": sum(int(row["fictional_travel_minutes"]) >= 60 for row in selected),
            "high_burden": sum(int(row["fictional_delivery_burden_score"]) >= 4 for row in selected),
            "monitoring_measures": len(monitoring),
            "monitoring_triggers": sum(row["result"] == "triggered" for row in monitoring),
            "incident_tests": sum(row["incident_test_state"] != "none" for row in inputs["dry_run"]),
            "objection_tests": sum(row["objection_test_state"] != "none" for row in inputs["dry_run"]),
            "cluster_features": 9,
            "cluster_variants": 8,
            "base_smallest_cluster": clusters["base_minimum"],
            "alternate_seed_minimum_ari": clusters["alternate_seed_minimum"],
            "scaling_variant_median_ari": clusters["scaling_median"],
            "selected_clusters": clusters["selected_clusters"],
            "challenger_stable_for_bounded_questions": clusters["stable_enough"],
            "query_checks": len(checks),
            "failed_query_checks": sum(row["status"] != "pass" for row in checks),
        },
        "intervention_readiness": "not ready for any real implementation; revise fictional staffing, travel, burden, access, incident, and monitoring triggers before any later exercise",
        "challenger_use": "bounded descriptive tailoring questions only" if clusters["stable_enough"] else "not useful; preserve transparent community-review rule only",
        "progression": "Module 06 package may enter separate Week 6 checkpoint construction; no real-world action is permitted",
        "outputs": {path.name: output_metadata(path) for path in generated},
        "interpretation_status": "fictional intervention planning, monitoring dry run, and descriptive clustering only; no effect estimate or implementation authority",
    }
    (target / "build-report.json").write_bytes((json.dumps(report, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    return report


def verify(root: Path = ROOT) -> dict[str, object]:
    outputs = root / "outputs"
    actual = {path.name for path in outputs.iterdir() if path.is_file()}
    require(actual == OUTPUT_FILES, "Analysis output file set changed")
    report = json.loads((outputs / "build-report.json").read_text(encoding="utf-8"))
    require(report["module_id"] == MODULE_ID and report["module_version"] == MODULE_VERSION, "Build identity changed")
    require(report["commons_release"] == COMMONS_RELEASE, "Commons release changed")
    require(report["findings"]["failed_query_checks"] == 0, "Query checks failed")
    for name, expected in report["outputs"].items():
        require(output_metadata(outputs / name) == expected, f"Output identity changed: {name}")
    if EXPECTED_REPORT_SHA256:
        require(sha256(outputs / "build-report.json") == EXPECTED_REPORT_SHA256, "Build report identity changed")
    return {
        "report_sha256": sha256(outputs / "build-report.json"),
        "report_bytes": (outputs / "build-report.json").stat().st_size,
        **report["findings"],
        "intervention_readiness": report["intervention_readiness"],
        "challenger_use": report["challenger_use"],
    }


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module06-build-") as temporary:
        base = Path(temporary)
        first = generate(base / "first")
        second = generate(base / "second")
        require(first == second, "Two analysis builds differ")
        first_files = {path.name: sha256(path) for path in (base / "first").iterdir()}
        second_files = {path.name: sha256(path) for path in (base / "second").iterdir()}
        require(first_files == second_files, "Two analysis file sets differ")
        try:
            generate(base / "first")
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder overwrote an existing target")
    committed = verify(ROOT)
    print(f"APP-5 Module 06 analysis self-check passed: {json.dumps(committed, sort_keys=True)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.verify:
            print(json.dumps(verify(ROOT), indent=2, sort_keys=True))
        elif args.write:
            print(json.dumps(generate(args.target or (ROOT / "outputs")), indent=2, sort_keys=True))
        elif args.target:
            print(json.dumps(generate(args.target), indent=2, sort_keys=True))
        else:
            parser.error("use --write, --verify, --self-check, or provide --target")
    except (OSError, ValueError, KeyError, BuildError) as error:
        parser.exit(1, f"Analysis build failed: {error}\n")


if __name__ == "__main__":
    main()
