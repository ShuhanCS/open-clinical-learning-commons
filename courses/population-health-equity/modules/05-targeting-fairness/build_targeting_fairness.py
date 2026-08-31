"""Build and verify APP-5 Module 05 targeting and fairness outputs."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import itertools
import json
import sqlite3
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SQL_FILES = (
    "01-link-evidence-and-fictional-planning.sql",
    "02-apply-and-reconcile-rules.sql",
    "03-audit-consequences-and-sensitivity.sql",
    "04-audit-release.sql",
)
OUTPUT_TABLES = (
    ("candidate-source-profile.csv", "candidate_source_profile"),
    ("linked-candidate-table.csv.gz", "candidate_release"),
    ("rule-assignments.csv.gz", "rule_assignments"),
    ("rule-summary.csv", "rule_summary"),
    ("county-concentration.csv", "county_concentration"),
    ("group-consequences.csv", "group_consequences"),
    ("rule-overlap.csv", "rule_overlap"),
    ("sensitivity-results.csv", "sensitivity_results"),
    ("query-checks.csv", "query_checks"),
)


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


def stable_int(rule_id: str, tract_fips: str) -> int:
    return int(hashlib.sha256(f"73055|{rule_id}|{tract_fips}".encode("utf-8")).hexdigest()[:16], 16)


def format_value(value: object) -> object:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.10f}".rstrip("0").rstrip(".")
    return value


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def csv_bytes(fields: list[str], rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows([{field: format_value(row.get(field)) for field in fields} for row in rows])
    return output.getvalue().encode("utf-8")


def deterministic_gzip(raw: bytes) -> bytes:
    output = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
        zipped.write(raw)
    return output.getvalue()


def write_rows(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    raw = csv_bytes(fields, rows)
    path.write_bytes(deterministic_gzip(raw) if path.suffix == ".gz" else raw)


def load_inputs(root: Path) -> tuple[list[dict[str, object]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    _, public_rows = read_csv(root / "upstream/module04-reference/outputs/tract-map-table.csv")
    public = {row["tract_fips"]: row for row in public_rows if row["modeled_crude_prevalence_percent"]}
    planning_fields, planning_rows = read_csv(root / "data/raw/fictional-planning-layer.csv.gz")
    _, rules = read_csv(root / "data/rule-definitions.csv")
    _, variants = read_csv(root / "data/sensitivity-variants.csv")
    require(len(public) == len(planning_rows) == 1597, "Accepted public and fictional tract counts changed")
    require(planning_fields[0:4] == ["scenario_id", "synthetic_source_id", "tract_fips", "county_fips"], "Fictional planning schema changed")
    planning = {row["tract_fips"]: row for row in planning_rows}
    require(set(public) == set(planning), "Public and fictional tract keys differ")
    candidates: list[dict[str, object]] = []
    for tract_fips in sorted(public):
        p = public[tract_fips]
        s = planning[tract_fips]
        require(p["county_fips"] == s["county_fips"], f"County mismatch: {tract_fips}")
        candidates.append(
            {
                "tract_fips": tract_fips,
                "county_fips": p["county_fips"],
                "county_name": p["county_name"],
                "modeled_crude_prevalence_percent": float(p["modeled_crude_prevalence_percent"]),
                "modeled_low_confidence_limit": float(p["modeled_low_confidence_limit"]),
                "modeled_high_confidence_limit": float(p["modeled_high_confidence_limit"]),
                "interval_width_percentage_points": float(p["interval_width_percentage_points"]),
                "places_adult_population_field": int(p["places_adult_population_field"]),
                "support_state": p["support_state"],
                "public_source_release": p["source_release"],
                "public_evidence_role": "accepted public modeled area-level estimate",
                "synthetic_source_id": s["synthetic_source_id"],
                "fictional_capacity_places": int(s["fictional_capacity_places"]),
                "fictional_travel_minutes": int(s["fictional_travel_minutes"]),
                "fictional_staff_readiness": s["fictional_staff_readiness"],
                "fictional_language_access_ready": int(s["fictional_language_access_ready"]),
                "fictional_disability_access_ready": int(s["fictional_disability_access_ready"]),
                "fictional_community_review_state": s["fictional_community_review_state"],
                "fictional_unresolved_questions": int(s["fictional_unresolved_questions"]),
                "fictional_objection_state": s["fictional_objection_state"],
                "fictional_delivery_burden_score": int(s["fictional_delivery_burden_score"]),
                "accountable_owner": s["accountable_owner"],
                "synthetic_flag": int(s["synthetic_flag"]),
                "synthetic_planning_role": "fictional capacity, access, review, objection, and burden conditions",
                "claim_limit": "public modeled context and fictional planning conditions remain separate; neither authorizes real action",
            }
        )
    require(len(rules) == 4 and len(variants) == 20, "Rule or sensitivity contract changed")
    return candidates, rules, variants, planning_rows


def ordered_selection(
    rule_id: str,
    candidates: list[dict[str, object]],
    count: int,
    variant_id: str = "base",
) -> list[dict[str, object]]:
    reverse_tie = variant_id == "equal-geographic-reverse-tie"
    if rule_id == "equal_geographic":
        if variant_id == "equal-geographic-no-county-quota":
            return sorted(candidates, key=lambda row: stable_int(rule_id, str(row["tract_fips"])))[:count]
        by_county: dict[str, list[dict[str, object]]] = defaultdict(list)
        for row in candidates:
            by_county[str(row["county_fips"])].append(row)
        require(count % 14 == 0, "Equal geographic sensitivity count must divide across 14 counties")
        per_county = count // 14
        selected: list[dict[str, object]] = []
        for county in sorted(by_county):
            ordered = sorted(
                by_county[county],
                key=lambda row: stable_int(rule_id, str(row["tract_fips"])),
                reverse=reverse_tie,
            )
            selected.extend(ordered[:per_county])
        return selected

    if rule_id == "need_based":
        pool = candidates
        if variant_id == "need-based-supported-only":
            pool = [row for row in pool if row["support_state"] == "supported_for_teaching_display"]
        criterion = "modeled_low_confidence_limit" if variant_id == "need-based-lower-bound" else "modeled_crude_prevalence_percent"
        return sorted(
            pool,
            key=lambda row: (
                -float(row[criterion]),
                float(row["interval_width_percentage_points"]),
                stable_int(rule_id, str(row["tract_fips"])),
            ),
        )[:count]

    if rule_id == "capacity_aware":
        minimum = 20 if variant_id == "capacity-minimum-20" else 10
        pool = [row for row in candidates if int(row["fictional_capacity_places"]) >= minimum]
        if variant_id == "capacity-access-ready":
            pool = [
                row for row in pool
                if row["fictional_language_access_ready"] == 1 and row["fictional_disability_access_ready"] == 1
            ]
        staff_order = {"ready": 0, "conditional": 1, "not_ready": 2}
        return sorted(
            pool,
            key=lambda row: (
                -int(row["fictional_capacity_places"]),
                staff_order[str(row["fictional_staff_readiness"])],
                -(int(row["fictional_language_access_ready"]) + int(row["fictional_disability_access_ready"])),
                int(row["fictional_delivery_burden_score"]),
                int(row["fictional_travel_minutes"]),
                stable_int(rule_id, str(row["tract_fips"])),
            ),
        )[:count]

    if rule_id == "community_review":
        allowed_reviews = {"ready_for_planning_review"}
        if variant_id == "community-include-revision":
            allowed_reviews.add("needs_revision")
        pool = [
            row for row in candidates
            if row["fictional_community_review_state"] in allowed_reviews
            and row["fictional_objection_state"] == "no_recorded_objection"
            and row["fictional_language_access_ready"] == 1
            and row["fictional_disability_access_ready"] == 1
            and int(row["fictional_capacity_places"]) >= 10
        ]
        ordered = sorted(
            pool,
            key=lambda row: (
                int(row["fictional_unresolved_questions"]),
                int(row["fictional_delivery_burden_score"]),
                -int(row["fictional_capacity_places"]),
                -float(row["modeled_crude_prevalence_percent"]),
                stable_int(rule_id, str(row["tract_fips"])),
            ),
        )
        maximum = 2 if variant_id == "community-max-two-county" else 3
        selected = []
        county_counts: Counter[str] = Counter()
        for row in ordered:
            county = str(row["county_fips"])
            if county_counts[county] >= maximum:
                continue
            selected.append(row)
            county_counts[county] += 1
            if len(selected) == count:
                break
        return selected

    raise BuildError(f"Unknown rule: {rule_id}")


def reasons(rule_id: str, row: dict[str, object], selected: bool) -> tuple[str, str]:
    if selected:
        inclusion = {
            "equal_geographic": "selected by the fixed source-independent county tie breaker",
            "need_based": "inside the first 28 under the declared modeled area-level criterion",
            "capacity_aware": "inside the first 28 under the declared fictional capacity and readiness order",
            "community_review": "passes fictional review, objection, access, capacity, county-limit, and teaching-order conditions",
        }[rule_id]
        return inclusion, ""
    if rule_id == "community_review":
        failures = []
        if row["fictional_community_review_state"] != "ready_for_planning_review": failures.append("review not ready")
        if row["fictional_objection_state"] != "no_recorded_objection": failures.append("unresolved objection")
        if row["fictional_language_access_ready"] != 1: failures.append("language-access plan not ready")
        if row["fictional_disability_access_ready"] != 1: failures.append("disability-access plan not ready")
        if int(row["fictional_capacity_places"]) < 10: failures.append("capacity below ten places")
        return "", "; ".join(failures) if failures else "outside the first 28 after the county concentration limit"
    exclusion = {
        "equal_geographic": "not selected by the fixed source-independent county tie breaker",
        "need_based": "outside the first 28 under the declared modeled area-level criterion",
        "capacity_aware": "fictional capacity below ten places" if int(row["fictional_capacity_places"]) < 10 else "outside the first 28 under the declared fictional capacity and readiness order",
    }[rule_id]
    return "", exclusion


def build_assignments(candidates: list[dict[str, object]], rules: list[dict[str, str]]) -> tuple[list[dict[str, object]], dict[str, set[str]]]:
    assignments: list[dict[str, object]] = []
    selected_sets: dict[str, set[str]] = {}
    for rule in rules:
        rule_id = rule["rule_id"]
        ordered = ordered_selection(rule_id, candidates, 28)
        require(len(ordered) == 28, f"Base rule cannot fill 28 awards: {rule_id}")
        order_map = {str(row["tract_fips"]): index for index, row in enumerate(ordered, start=1)}
        selected_sets[rule_id] = set(order_map)
        for row in candidates:
            selected = str(row["tract_fips"]) in order_map
            inclusion, exclusion = reasons(rule_id, row, selected)
            assignments.append(
                {
                    "rule_id": rule_id,
                    "rule_name": rule["rule_name"],
                    "fairness_definition": rule["fairness_definition"],
                    "tract_fips": row["tract_fips"],
                    "county_fips": row["county_fips"],
                    "county_name": row["county_name"],
                    "selected": int(selected),
                    "selection_order": order_map.get(str(row["tract_fips"])),
                    "allocated_places": 10 if selected else 0,
                    "inclusion_reason": inclusion,
                    "exclusion_reason": exclusion,
                    "modeled_crude_prevalence_percent": row["modeled_crude_prevalence_percent"],
                    "interval_width_percentage_points": row["interval_width_percentage_points"],
                    "support_state": row["support_state"],
                    "fictional_capacity_places": row["fictional_capacity_places"],
                    "fictional_travel_minutes": row["fictional_travel_minutes"],
                    "fictional_staff_readiness": row["fictional_staff_readiness"],
                    "fictional_language_access_ready": row["fictional_language_access_ready"],
                    "fictional_disability_access_ready": row["fictional_disability_access_ready"],
                    "fictional_community_review_state": row["fictional_community_review_state"],
                    "fictional_unresolved_questions": row["fictional_unresolved_questions"],
                    "fictional_objection_state": row["fictional_objection_state"],
                    "fictional_delivery_burden_score": row["fictional_delivery_burden_score"],
                    "automatic_action": 0,
                    "accountable_owner": row["accountable_owner"],
                    "interpretation_limit": "fictional comparison only; selection is not real need, eligibility, outreach, funding, allocation, service, consent, or authority",
                }
            )
    require(len(assignments) == 6388, "Assignment row count changed")
    return assignments, selected_sets


def summary_rows(assignments: list[dict[str, object]], rules: list[dict[str, str]]) -> list[dict[str, object]]:
    rows = []
    for rule in rules:
        group = [row for row in assignments if row["rule_id"] == rule["rule_id"]]
        selected = [row for row in group if row["selected"] == 1]
        rows.append(
            {
                "rule_id": rule["rule_id"],
                "rule_name": rule["rule_name"],
                "fairness_definition": rule["fairness_definition"],
                "candidate_tracts": len(group),
                "selected_tracts": len(selected),
                "excluded_tracts": len(group) - len(selected),
                "allocated_places": sum(int(row["allocated_places"]) for row in selected),
                "selected_counties": len({row["county_fips"] for row in selected}),
                "selected_limited_support": sum(row["support_state"] == "limited_support_review" for row in selected),
                "mean_selected_modeled_prevalence_percent": sum(float(row["modeled_crude_prevalence_percent"]) for row in selected) / len(selected),
                "fictional_selected_capacity_places": sum(int(row["fictional_capacity_places"]) for row in selected),
                "selected_staff_not_ready": sum(row["fictional_staff_readiness"] == "not_ready" for row in selected),
                "selected_language_access_gaps": sum(row["fictional_language_access_ready"] == 0 for row in selected),
                "selected_disability_access_gaps": sum(row["fictional_disability_access_ready"] == 0 for row in selected),
                "selected_high_travel": sum(int(row["fictional_travel_minutes"]) >= 60 for row in selected),
                "selected_high_burden": sum(int(row["fictional_delivery_burden_score"]) >= 4 for row in selected),
                "selected_review_ready": sum(row["fictional_community_review_state"] == "ready_for_planning_review" for row in selected),
                "selected_unresolved_objections": sum(row["fictional_objection_state"] == "unresolved_objection" for row in selected),
                "selected_unresolved_questions": sum(int(row["fictional_unresolved_questions"]) for row in selected),
                "possible_benefit": "280 fictional program places if all assumptions hold",
                "possible_harm": "exclusion, delay, burden, access failure, capacity failure, or treating a classroom rule as authority",
                "interpretation_limit": "rule comparison, not a validated fairness result or real allocation decision",
            }
        )
    return rows


def county_rows(assignments: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for rule_id in sorted({str(row["rule_id"]) for row in assignments}):
        group = [row for row in assignments if row["rule_id"] == rule_id]
        for county_fips in sorted({str(row["county_fips"]) for row in group}):
            county = [row for row in group if row["county_fips"] == county_fips]
            selected = [row for row in county if row["selected"] == 1]
            rows.append(
                {
                    "rule_id": rule_id,
                    "county_fips": county_fips,
                    "county_name": county[0]["county_name"],
                    "candidate_tracts": len(county),
                    "selected_tracts": len(selected),
                    "allocated_places": sum(int(row["allocated_places"]) for row in selected),
                    "share_of_rule_awards": len(selected) / 28,
                    "selected_limited_support": sum(row["support_state"] == "limited_support_review" for row in selected),
                    "selected_high_burden": sum(int(row["fictional_delivery_burden_score"]) >= 4 for row in selected),
                    "interpretation_limit": "fictional geographic concentration audit; not a county need or funding statement",
                }
            )
    return rows


def group_rows(root: Path, selected_sets: dict[str, set[str]]) -> list[dict[str, object]]:
    path = root / "upstream/module04-reference/upstream/checkpoint-reference/candidate/module-03/outputs/published-tract-group-rates.csv.gz"
    _, margins = read_csv(path)
    groups = sorted({(row["equity_dimension"], row["dimension_label"], row["group_id"], row["group_label"]) for row in margins})
    require(len(margins) == 30343 and len(groups) == 19, "Accepted synthetic equity margin shape changed")
    rows = []
    for rule_id, selected in sorted(selected_sets.items()):
        for dimension, dimension_label, group_id, group_label in groups:
            subset = [row for row in margins if row["equity_dimension"] == dimension and row["group_id"] == group_id]
            selected_rows = [row for row in subset if row["tract_fips"] in selected]
            unselected_rows = [row for row in subset if row["tract_fips"] not in selected]
            rows.append(
                {
                    "rule_id": rule_id,
                    "equity_dimension": dimension,
                    "dimension_label": dimension_label,
                    "group_id": group_id,
                    "group_label": group_label,
                    "selected_publishable_population": sum(int(row["published_population_count"]) for row in selected_rows if row["published_population_count"]),
                    "unselected_publishable_population": sum(int(row["published_population_count"]) for row in unselected_rows if row["published_population_count"]),
                    "selected_publishable_rows": sum(row["support_state"] == "publishable" for row in selected_rows),
                    "selected_suppressed_rows": sum(row["support_state"] != "publishable" for row in selected_rows),
                    "unselected_publishable_rows": sum(row["support_state"] == "publishable" for row in unselected_rows),
                    "unselected_suppressed_rows": sum(row["support_state"] != "publishable" for row in unselected_rows),
                    "interpretation_limit": "published synthetic marginal coverage only; suppressed values stay unavailable and dimensions cannot be combined into people",
                }
            )
    return rows


def overlap_rows(selected_sets: dict[str, set[str]]) -> list[dict[str, object]]:
    rows = []
    for left, right in itertools.combinations(sorted(selected_sets), 2):
        intersection = selected_sets[left] & selected_sets[right]
        union = selected_sets[left] | selected_sets[right]
        rows.append(
            {
                "left_rule_id": left,
                "right_rule_id": right,
                "shared_selected_tracts": len(intersection),
                "left_only_tracts": len(selected_sets[left] - selected_sets[right]),
                "right_only_tracts": len(selected_sets[right] - selected_sets[left]),
                "jaccard_overlap": len(intersection) / len(union),
                "interpretation_limit": "rule turnover exposes decision dependence; it is not validation of either rule",
            }
        )
    return rows


def sensitivity_rows(
    candidates: list[dict[str, object]],
    variants: list[dict[str, str]],
    base_sets: dict[str, set[str]],
) -> list[dict[str, object]]:
    rows = []
    by_tract = {str(row["tract_fips"]): row for row in candidates}
    for variant in variants:
        requested = int(variant["award_count"])
        variant_id = variant["variant_id"]
        rule_id = variant["rule_id"]
        selected_rows = ordered_selection(rule_id, candidates, requested, variant_id)
        selected = {str(row["tract_fips"]) for row in selected_rows}
        base = base_sets[rule_id]
        rows.append(
            {
                "variant_id": variant_id,
                "rule_id": rule_id,
                "variant_type": variant["variant_type"],
                "parameter": variant["parameter"],
                "parameter_value": variant["parameter_value"],
                "requested_awards": requested,
                "actual_selected": len(selected),
                "constraint_status": "filled" if len(selected) == requested else "shortfall",
                "retained_from_base": len(selected & base),
                "added_from_base": len(selected - base),
                "removed_from_base": len(base - selected),
                "selected_counties": len({by_tract[key]["county_fips"] for key in selected}),
                "fictional_capacity_places": sum(int(by_tract[key]["fictional_capacity_places"]) for key in selected),
                "limited_support_selected": sum(by_tract[key]["support_state"] == "limited_support_review" for key in selected),
                "language_access_gaps": sum(by_tract[key]["fictional_language_access_ready"] == 0 for key in selected),
                "disability_access_gaps": sum(by_tract[key]["fictional_disability_access_ready"] == 0 for key in selected),
                "unresolved_objections": sum(by_tract[key]["fictional_objection_state"] == "unresolved_objection" for key in selected),
                "high_burden": sum(int(by_tract[key]["fictional_delivery_burden_score"]) >= 4 for key in selected),
                "interpretation_limit": "predeclared fictional sensitivity, not a search for a preferred answer or real action rule",
            }
        )
    return rows


def create_table(connection: sqlite3.Connection, name: str, fields: list[str], rows: list[dict[str, object]]) -> None:
    connection.execute(f'DROP TABLE IF EXISTS "{name}"')
    connection.execute(f'CREATE TABLE "{name}" ({", ".join(f"[{field}]" for field in fields)})')
    connection.executemany(
        f'INSERT INTO "{name}" VALUES ({", ".join("?" for _ in fields)})',
        [[row.get(field) for field in fields] for row in rows],
    )


def table_rows(connection: sqlite3.Connection, name: str) -> tuple[list[str], list[dict[str, object]]]:
    cursor = connection.execute(f'SELECT * FROM "{name}"')
    fields = [description[0] for description in cursor.description or []]
    return fields, [dict(zip(fields, row)) for row in cursor.fetchall()]


def execute_sql(connection: sqlite3.Connection, sql_root: Path) -> dict[str, str]:
    hashes = {}
    for filename in SQL_FILES:
        path = sql_root / filename
        require(path.is_file(), f"SQL file is missing: {filename}")
        text = path.read_text(encoding="utf-8")
        require("REPLACE" not in text, f"SQL file is incomplete: {filename}")
        connection.executescript(text)
        hashes[filename] = sha256(path)
    return hashes


def build(root: Path, output: Path) -> dict[str, object]:
    output = output.resolve()
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {output}")
    output.mkdir(parents=True)
    candidates, rules, variants, planning = load_inputs(root)
    assignments, selected_sets = build_assignments(candidates, rules)
    summaries = summary_rows(assignments, rules)
    counties = county_rows(assignments)
    groups = group_rows(root, selected_sets)
    overlaps = overlap_rows(selected_sets)
    sensitivities = sensitivity_rows(candidates, variants, selected_sets)
    profile = [
        {
            "scenario_id": "FMA-DP-01",
            "candidate_tracts": len(candidates),
            "counties": len({row["county_fips"] for row in candidates}),
            "public_release": "CDC PLACES 2025 census-tract release",
            "synthetic_release": planning[0]["synthetic_source_id"],
            "fictional_capacity_places": sum(int(row["fictional_capacity_places"]) for row in candidates),
            "review_ready_tracts": sum(row["fictional_community_review_state"] == "ready_for_planning_review" for row in candidates),
            "unresolved_objection_tracts": sum(row["fictional_objection_state"] == "unresolved_objection" for row in candidates),
            "language_access_ready_tracts": sum(int(row["fictional_language_access_ready"]) for row in candidates),
            "disability_access_ready_tracts": sum(int(row["fictional_disability_access_ready"]) for row in candidates),
            "resource_places_per_rule": 280,
            "awards_per_rule": 28,
            "award_places": 10,
            "claim_limit": "public modeled evidence and synthetic planning assumptions remain separate and authorize no real action",
        }
    ]

    tables = {
        "candidate_source_profile": profile,
        "candidate_release": candidates,
        "rule_assignments": assignments,
        "rule_summary": summaries,
        "county_concentration": counties,
        "group_consequences": groups,
        "rule_overlap": overlaps,
        "sensitivity_results": sensitivities,
    }
    connection = sqlite3.connect(":memory:")
    for name, rows in tables.items():
        create_table(connection, name, list(rows[0]), rows)
    sql_root = root / "reference/sql" if (root / "reference/sql").is_dir() else root / "sql"
    sql_hashes = execute_sql(connection, sql_root)
    checks = connection.execute("SELECT check_id, status FROM query_checks ORDER BY check_id").fetchall()
    require(len(checks) == 40 and all(status == "pass" for _, status in checks), "One or more SQL checks failed")

    output_meta: dict[str, dict[str, object]] = {}
    for filename, table in OUTPUT_TABLES:
        fields, rows = table_rows(connection, table)
        path = output / filename
        write_rows(path, fields, rows)
        output_meta[filename] = {
            "rows": len(rows),
            "columns": len(fields),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
    findings = {
        "candidate_tracts": len(candidates),
        "rules": len(rules),
        "assignments": len(assignments),
        "selected_per_rule": 28,
        "fictional_places_per_rule": 280,
        "county_consequence_rows": len(counties),
        "group_consequence_rows": len(groups),
        "overlap_rows": len(overlaps),
        "sensitivity_variants": len(sensitivities),
        "sensitivity_shortfalls": sum(row["constraint_status"] == "shortfall" for row in sensitivities),
        "query_checks": len(checks),
        "failed_query_checks": 0,
        "rule_summaries": {row["rule_id"]: row for row in summaries},
    }
    report = {
        "schema_version": "1.0.0",
        "module_id": "oclc-app5-05",
        "module_version": "0.1.0",
        "commons_release": "0.92.0",
        "upstream": {
            "module_id": "oclc-app5-04",
            "module_version": "0.1.0",
            "commons_release": "0.91.0",
            "reference_files": 287,
            "handoff_manifest_sha256": sha256(root / "upstream/module04-handoff-manifest.csv"),
        },
        "synthetic_source": {
            "source_id": planning[0]["synthetic_source_id"],
            "rows": len(planning),
            "seed": int(planning[0]["seed"]),
            "manifest_sha256": sha256(root / "data/synthetic-source-manifest.csv"),
            "independent_of_public_prevalence": True,
        },
        "resource_contract": {
            "fictional_places": 280,
            "awards": 28,
            "places_per_award": 10,
            "partial_awards": False,
            "automatic_action": False,
        },
        "findings": findings,
        "sql_sha256": sql_hashes,
        "outputs": output_meta,
        "interpretation_status": "fictional rule comparison only; no real need, consent, eligibility, outreach, funding, allocation, community action, service, implementation, production connection, or deployment conclusion",
    }
    report_path = output / "build-report.json"
    report_path.write_bytes((json.dumps(report, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    connection.close()
    return report


def compare_outputs(left: Path, right: Path) -> None:
    left_files = {path.relative_to(left).as_posix(): sha256(path) for path in left.rglob("*") if path.is_file()}
    right_files = {path.relative_to(right).as_posix(): sha256(path) for path in right.rglob("*") if path.is_file()}
    differences = sorted(path for path in left_files.keys() | right_files.keys() if left_files.get(path) != right_files.get(path))
    require(not differences, f"Two targeting and fairness builds differ: {', '.join(differences)}")


def verify(root: Path = ROOT) -> dict[str, object]:
    committed = root / "outputs"
    require(committed.is_dir(), "Committed outputs are missing")
    with tempfile.TemporaryDirectory(prefix="app5-module05-verify-") as temporary:
        generated = Path(temporary) / "outputs"
        report = build(root, generated)
        compare_outputs(committed, generated)
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module05-build-") as temporary:
        base = Path(temporary)
        first = base / "first"
        second = base / "second"
        report = build(ROOT, first)
        build(ROOT, second)
        compare_outputs(first, second)
        require(report["findings"]["candidate_tracts"] == 1597, "Candidate count changed")
        require(report["findings"]["assignments"] == 6388, "Assignment count changed")
        require(report["findings"]["query_checks"] == 40, "Query check count changed")
        try:
            build(ROOT, first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Targeting builder overwrote an existing target")
    committed = verify(ROOT)
    print(
        "APP-5 Module 05 targeting-fairness self-check passed: "
        f"{committed['findings']['candidate_tracts']} candidates, "
        f"{committed['findings']['assignments']} assignments, and "
        f"{committed['findings']['query_checks']} query checks."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
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
            print(json.dumps(build(ROOT, args.output or (ROOT / "outputs")), indent=2, sort_keys=True))
        elif args.output:
            print(json.dumps(build(ROOT, args.output), indent=2, sort_keys=True))
        else:
            parser.error("use --write, --verify, --self-check, or provide --output")
    except (OSError, ValueError, KeyError, sqlite3.Error, BuildError) as error:
        parser.exit(1, f"Targeting and fairness build failed: {error}\n")


if __name__ == "__main__":
    main()
