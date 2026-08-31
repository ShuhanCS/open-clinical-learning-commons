"""Validate an APP-5 Module 05 learner or complete workspace."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True


ROOT = Path(__file__).resolve().parent
EXPECTED_COMPLETE_CHECKS = 2406
EXPECTED_LEARNER_CHECKS = 2230
EXPECTED_FAILURE_ROUTES = 24
EXPECTED_HANDOFF_SHA256 = "0670760f650e0d13cfd4c5dc85ab26fdce5779cc86d35b3d3c27d6a3cc7738dd"
EXPECTED_SOURCE_MANIFEST_SHA256 = "a9a9cd10e67164cd8c47df667f2e559f17f8baa0e2308740ce4c9d9e675c0319"
EXPECTED_OUTPUTS = {
    "build-report.json": (8356, "d2b2621c6b97365fb9751902d7c1eac091567d6d8f2e5b5188fc4f4bafaa700a"),
    "candidate-source-profile.csv": (496, "262b8807f10aadb466595dd52ce3f6fcc30e0208a493b90814ce6fdbb4ea235c"),
    "county-concentration.csv": (7609, "d8e5b41f1199f8ef2e6cf8dd0ae58cbdab55bf177337b662096863b0c2733df0"),
    "group-consequences.csv": (17922, "029c81cc2ef5cef1c92ff0ca68f2eae11b09330fe23c03fbcf5a14cd53f9581a"),
    "linked-candidate-table.csv.gz": (34393, "957fc1bd320b5c9c4745e2789a0f86df4f73968b73724dabf11793eb9d411be1"),
    "query-checks.csv": (1702, "307268a47860099e3fa36e11d383b50d60afebfdbeb9c392b9f1083038a7f3a3"),
    "rule-assignments.csv.gz": (103785, "33f502587ff16b291ddadd83a6ba96600616d84837d86e4bff3c467808b568ce"),
    "rule-overlap.csv": (858, "92048bd15ea8902f4ea123e9ce998f9ff532b3492687d01096fcd1aecbd70c21"),
    "rule-summary.csv": (2132, "e0c3743fd00da6512a7e7843fc2e7b901b01419fa2c6715b26958894f66551c8"),
    "sensitivity-results.csv": (4597, "97181653260ea933d08415ad5e3de20a4f728315b090ec87d80bf3e120939ada"),
}
RECORD_FILES = (
    "decision-and-resource-contract.md",
    "rule-definitions.csv",
    "inclusion-exclusion-burden-audit.csv",
    "fairness-definition-tradeoff.md",
    "geographic-concentration-review.csv",
    "group-consequence-suppression-review.csv",
    "access-capacity-review.md",
    "sensitivity-analysis.md",
    "benefit-harm-balancing-register.csv",
    "community-review-recourse.md",
    "accountable-owner-record.md",
    "responsible-claims-audit.csv",
    "week6-component-score.csv",
    "gate-results.csv",
    "progression-decision.md",
    "reproducibility-check.md",
    "ai-use.md",
)
SQL_FILES = (
    "sql/01-link-evidence-and-fictional-planning.sql",
    "sql/02-apply-and-reconcile-rules.sql",
    "sql/03-audit-consequences-and-sensitivity.sql",
    "sql/04-audit-release.sql",
)


class ValidationError(RuntimeError):
    pass


class Auditor:
    def __init__(self) -> None:
        self.count = 0

    def check(self, condition: bool, message: str) -> None:
        self.count += 1
        if not condition:
            raise ValidationError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def open_csv(path: Path):
    return gzip.open(path, "rt", encoding="utf-8", newline="") if path.suffix == ".gz" else path.open(encoding="utf-8", newline="")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with open_csv(path) as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_script(root: Path, script: str, *args: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(root / script), *args],
        text=True,
        capture_output=True,
        env=environment,
        check=False,
    )
    if completed.returncode:
        raise ValidationError(completed.stderr.strip() or completed.stdout.strip())


def validate_manifest(root: Path, mode: str, audit: Auditor) -> list[dict[str, str]]:
    path = root / "release-manifest.csv"
    audit.check(path.is_file(), "Release manifest is missing")
    fields, rows = read_csv(path)
    audit.check(fields == ["relative_path", "bytes", "sha256", "role"], "Release manifest header changed")
    expected_rows = 318 if mode == "complete" else 308
    expected_files = 340 if mode == "complete" else 330
    audit.check(len(rows) == expected_rows, "Release manifest row count changed")
    audit.check([row["relative_path"] for row in rows] == sorted(row["relative_path"] for row in rows), "Release manifest is not sorted")
    audit.check(len({row["relative_path"] for row in rows}) == len(rows), "Release manifest paths are not unique")
    for row in rows:
        relative = Path(row["relative_path"])
        audit.check(not relative.is_absolute() and ".." not in relative.parts, f"Unsafe release path: {relative}")
        file_path = root / relative
        audit.check(file_path.is_file(), f"Release file is missing: {relative}")
        audit.check(file_path.stat().st_size == int(row["bytes"]), f"Release byte count changed: {relative}")
        audit.check(sha256(file_path) == row["sha256"], f"Release SHA-256 changed: {relative}")
    actual_files = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    expected_set = {row["relative_path"] for row in rows} | {"release-manifest.csv"} | set(RECORD_FILES) | set(SQL_FILES)
    audit.check(actual_files == expected_set, "Workspace file set changed")
    audit.check(len(actual_files) == expected_files, "Workspace file count changed")
    return rows


def validate_upstream(root: Path, audit: Auditor) -> None:
    manifest_path = root / "upstream/module04-handoff-manifest.csv"
    fields, rows = read_csv(manifest_path)
    audit.check(fields == ["relative_path", "bytes", "sha256", "role"], "Module 04 handoff header changed")
    audit.check(len(rows) == 287, "Module 04 handoff row count changed")
    audit.check(sha256(manifest_path) == EXPECTED_HANDOFF_SHA256, "Module 04 handoff identity changed")
    audit.check([row["relative_path"] for row in rows] == sorted(row["relative_path"] for row in rows), "Module 04 handoff is not sorted")
    for row in rows:
        path = root / "upstream" / row["relative_path"]
        audit.check(path.is_file(), f"Module 04 handoff file is missing: {row['relative_path']}")
        audit.check(path.stat().st_size == int(row["bytes"]), f"Module 04 handoff bytes changed: {row['relative_path']}")
        audit.check(sha256(path) == row["sha256"], f"Module 04 handoff SHA-256 changed: {row['relative_path']}")
    release = read_json(root / "upstream/module04-reference/release.json")
    audit.check(release["module_id"] == "oclc-app5-04", "Module 04 ID changed")
    audit.check(release["commons_release"] == "0.91.0", "Module 04 Commons release changed")
    audit.check(release["reference_decision"]["score"] == 10, "Module 04 score changed")
    audit.check(release["reference_decision"]["gates_passed"] == 22, "Module 04 gates changed")
    audit.check(release["reference_decision"]["module05_permission"] == "permitted for curriculum construction", "Module 05 upstream permission changed")


def validate_source(root: Path, audit: Auditor) -> None:
    manifest_path = root / "data/synthetic-source-manifest.csv"
    fields, rows = read_csv(manifest_path)
    audit.check(fields[0:4] == ["source_id", "relative_path", "format", "rows"], "Synthetic manifest header changed")
    audit.check(len(rows) == 4, "Synthetic manifest row count changed")
    audit.check(sha256(manifest_path) == EXPECTED_SOURCE_MANIFEST_SHA256, "Synthetic manifest identity changed")
    for row in rows:
        path = root / "data" / row["relative_path"]
        audit.check(path.is_file(), f"Synthetic source file is missing: {row['relative_path']}")
        audit.check(path.stat().st_size == int(row["bytes"]), f"Synthetic source bytes changed: {row['relative_path']}")
        audit.check(sha256(path) == row["sha256"], f"Synthetic source SHA-256 changed: {row['relative_path']}")
        audit.check(row["synthetic_flag"] == "1", "Synthetic source flag changed")
        audit.check(row["seed"] == "73055", "Synthetic source seed changed")
    planning_fields, planning = read_csv(root / "data/raw/fictional-planning-layer.csv.gz")
    audit.check(len(planning_fields) == 18, "Fictional planning column count changed")
    audit.check(len(planning) == 1597, "Fictional planning row count changed")
    audit.check(len({row["tract_fips"] for row in planning}) == 1597, "Fictional planning keys changed")
    audit.check({row["synthetic_flag"] for row in planning} == {"1"}, "Fictional planning flag changed")
    audit.check({row["seed"] for row in planning} == {"73055"}, "Fictional planning seed changed")
    audit.check({row["synthetic_source_id"] for row in planning} == {"fma-dp-01-fictional-planning-v1"}, "Fictional source identity changed")
    audit.check(all(row["claim_limit"] for row in planning), "Fictional planning claim limit is missing")
    _, rules = read_csv(root / "data/rule-definitions.csv")
    audit.check(len(rules) == 4, "Rule definition count changed")
    audit.check({row["rule_id"] for row in rules} == {"equal_geographic", "need_based", "capacity_aware", "community_review"}, "Rule IDs changed")
    audit.check(all(row["automatic_action"] == "0" for row in rules), "Rule definition grants automatic action")
    audit.check(all(row["resource_places"] == "280" and row["base_awards"] == "28" and row["award_places"] == "10" for row in rules), "Rule resource contract changed")
    _, variants = read_csv(root / "data/sensitivity-variants.csv")
    audit.check(len(variants) == 20, "Sensitivity variant count changed")
    audit.check(Counter(row["rule_id"] for row in variants) == {"equal_geographic": 5, "need_based": 5, "capacity_aware": 5, "community_review": 5}, "Sensitivity variants are unbalanced")


def validate_outputs(root: Path, audit: Auditor) -> None:
    for filename, (expected_bytes, expected_hash) in EXPECTED_OUTPUTS.items():
        path = root / "outputs" / filename
        audit.check(path.is_file(), f"Output is missing: {filename}")
        audit.check(path.stat().st_size == expected_bytes, f"Output bytes changed: {filename}")
        audit.check(sha256(path) == expected_hash, f"Output SHA-256 changed: {filename}")
    report = read_json(root / "outputs/build-report.json")
    audit.check(report["module_id"] == "oclc-app5-05", "Build report module ID changed")
    audit.check(report["commons_release"] == "0.92.0", "Build report release changed")
    audit.check(report["upstream"]["handoff_manifest_sha256"] == EXPECTED_HANDOFF_SHA256, "Build report handoff identity changed")
    audit.check(report["synthetic_source"]["manifest_sha256"] == EXPECTED_SOURCE_MANIFEST_SHA256, "Build report source identity changed")
    audit.check(report["synthetic_source"]["independent_of_public_prevalence"] is True, "Synthetic independence statement changed")
    audit.check(report["resource_contract"] == {"automatic_action": False, "awards": 28, "fictional_places": 280, "partial_awards": False, "places_per_award": 10}, "Build resource contract changed")
    audit.check(report["findings"]["candidate_tracts"] == 1597, "Build candidate count changed")
    audit.check(report["findings"]["assignments"] == 6388, "Build assignment count changed")
    audit.check(report["findings"]["query_checks"] == 40 and report["findings"]["failed_query_checks"] == 0, "Build SQL check result changed")
    audit.check(report["findings"]["sensitivity_shortfalls"] == 2, "Sensitivity shortfall count changed")

    _, candidates = read_csv(root / "outputs/linked-candidate-table.csv.gz")
    audit.check(len(candidates) == 1597, "Candidate output row count changed")
    audit.check(len({row["tract_fips"] for row in candidates}) == 1597, "Candidate output keys changed")
    audit.check({row["public_source_release"] for row in candidates} == {"CDC PLACES 2025 census-tract release"}, "Candidate public source changed")
    audit.check({row["synthetic_source_id"] for row in candidates} == {"fma-dp-01-fictional-planning-v1"}, "Candidate synthetic source changed")
    audit.check(sum(row["support_state"] == "limited_support_review" for row in candidates) == 49, "Candidate support accounting changed")
    audit.check(all(row["public_evidence_role"] == "accepted public modeled area-level estimate" for row in candidates), "Public evidence role changed")
    audit.check(all(row["synthetic_planning_role"] == "fictional capacity, access, review, objection, and burden conditions" for row in candidates), "Synthetic planning role changed")

    _, assignments = read_csv(root / "outputs/rule-assignments.csv.gz")
    audit.check(len(assignments) == 6388, "Assignment output row count changed")
    audit.check(len({(row["rule_id"], row["tract_fips"]) for row in assignments}) == 6388, "Assignment keys changed")
    for rule_id in ("equal_geographic", "need_based", "capacity_aware", "community_review"):
        rows = [row for row in assignments if row["rule_id"] == rule_id]
        selected = [row for row in rows if row["selected"] == "1"]
        audit.check(len(rows) == 1597, f"Candidate count changed for {rule_id}")
        audit.check(len(selected) == 28, f"Selected count changed for {rule_id}")
        audit.check(sum(int(row["allocated_places"]) for row in selected) == 280, f"Allocated places changed for {rule_id}")
        audit.check(all(row["allocated_places"] == "10" for row in selected), f"Partial selected award found for {rule_id}")
        audit.check(all(row["allocated_places"] == "0" for row in rows if row["selected"] == "0"), f"Excluded award found for {rule_id}")
        audit.check(all(row["automatic_action"] == "0" for row in rows), f"Automatic action found for {rule_id}")
        audit.check(all(row["inclusion_reason"] for row in selected), f"Selected reason missing for {rule_id}")
        audit.check(all(row["exclusion_reason"] for row in rows if row["selected"] == "0"), f"Exclusion reason missing for {rule_id}")
    community = [row for row in assignments if row["rule_id"] == "community_review" and row["selected"] == "1"]
    audit.check(all(int(row["fictional_capacity_places"]) >= 10 for row in community), "Community capacity filter changed")
    audit.check(all(row["fictional_community_review_state"] == "ready_for_planning_review" for row in community), "Community review filter changed")
    audit.check(all(row["fictional_objection_state"] == "no_recorded_objection" for row in community), "Community objection filter changed")
    audit.check(all(row["fictional_language_access_ready"] == "1" and row["fictional_disability_access_ready"] == "1" for row in community), "Community access filter changed")
    audit.check(max(Counter(row["county_fips"] for row in community).values()) <= 3, "Community county limit changed")

    _, summaries = read_csv(root / "outputs/rule-summary.csv")
    audit.check(len(summaries) == 4, "Rule summary count changed")
    summary = {row["rule_id"]: row for row in summaries}
    audit.check(summary["equal_geographic"]["selected_counties"] == "14", "Equal county coverage changed")
    audit.check(summary["need_based"]["selected_limited_support"] == "26", "Need support result changed")
    audit.check(summary["capacity_aware"]["fictional_selected_capacity_places"] == "1120", "Capacity result changed")
    audit.check(summary["community_review"]["selected_counties"] == "11", "Community county coverage changed")
    audit.check(summary["community_review"]["selected_high_travel"] == "12", "Community travel result changed")

    _, counties = read_csv(root / "outputs/county-concentration.csv")
    audit.check(len(counties) == 56, "County consequence row count changed")
    equal = [row for row in counties if row["rule_id"] == "equal_geographic"]
    audit.check(len(equal) == 14 and all(row["selected_tracts"] == "2" for row in equal), "Equal county allocation changed")
    need = [row for row in counties if row["rule_id"] == "need_based"]
    audit.check(max(int(row["selected_tracts"]) for row in need) == 12, "Need concentration changed")

    _, groups = read_csv(root / "outputs/group-consequences.csv")
    audit.check(len(groups) == 76, "Group consequence row count changed")
    audit.check(Counter(row["rule_id"] for row in groups) == {"equal_geographic": 19, "need_based": 19, "capacity_aware": 19, "community_review": 19}, "Group consequence rule count changed")
    audit.check(sum(int(row["selected_suppressed_rows"]) for row in groups) > 0, "Selected suppression was erased")
    audit.check(all("suppressed values stay unavailable" in row["interpretation_limit"] for row in groups), "Group suppression limit changed")

    _, overlaps = read_csv(root / "outputs/rule-overlap.csv")
    audit.check(len(overlaps) == 6, "Rule overlap count changed")
    audit.check(sum(row["shared_selected_tracts"] == "0" for row in overlaps) == 4, "Rule disagreement result changed")
    _, sensitivities = read_csv(root / "outputs/sensitivity-results.csv")
    audit.check(len(sensitivities) == 20, "Sensitivity output count changed")
    audit.check(sum(row["constraint_status"] == "shortfall" for row in sensitivities) == 2, "Sensitivity shortfall output changed")
    indexed = {row["variant_id"]: row for row in sensitivities}
    audit.check(indexed["equal-geographic-reverse-tie"]["retained_from_base"] == "0", "Tie-break sensitivity changed")
    audit.check(indexed["need-based-supported-only"]["retained_from_base"] == "2", "Support sensitivity changed")
    audit.check(indexed["community-max-two-county"]["actual_selected"] == "26", "County-limit sensitivity changed")
    _, checks = read_csv(root / "outputs/query-checks.csv")
    audit.check(len(checks) == 40, "Query check count changed")
    audit.check(all(row["status"] == "pass" for row in checks), "One or more query checks failed")


def validate_records(root: Path, mode: str, audit: Auditor) -> None:
    texts = []
    for relative in RECORD_FILES + SQL_FILES:
        path = root / relative
        audit.check(path.is_file(), f"Editable file is missing: {relative}")
        text = path.read_text(encoding="utf-8")
        texts.append(text)
        if mode == "complete":
            audit.check("REPLACE" not in text, f"Reference file contains a placeholder: {relative}")
        else:
            audit.check("REPLACE" in text, f"Learner file lacks a REPLACE prompt: {relative}")
    joined = "\n".join(texts)
    if mode == "complete":
        for phrase in (
            "280 fictional program places",
            "1,569 unselected",
            "least unacceptable fictional planning candidate",
            "suppressed values remain unavailable",
            "appeal",
            "pause",
            "stop",
            "FMA-DP-01 fictional resource-allocation owner",
            "15 of 15",
            "26 of 26 pass",
            "40 of 40 pass",
            "Module 06 permission",
            "deployment: `prohibited`",
        ):
            audit.check(phrase in joined, f"Reference evidence is missing: {phrase}")
        _, scores = read_csv(root / "week6-component-score.csv")
        audit.check(len(scores) == 5, "Score row count changed")
        audit.check(sum(int(row["points_awarded"]) for row in scores[:4]) == 15, "Scored points changed")
        audit.check(scores[-1]["points_awarded"] == "15" and scores[-1]["status"] == "pass", "Total score changed")
        _, gates = read_csv(root / "gate-results.csv")
        audit.check(len(gates) == 26, "Gate row count changed")
        audit.check([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 27)], "Gate IDs changed")
        audit.check(all(row["status"] == "pass" and row["blocking_if_failed"] == "yes" for row in gates), "Gate result changed")
        _, claims = read_csv(root / "responsible-claims-audit.csv")
        audit.check(len(claims) == 12, "Claims audit row count changed")
        audit.check(sum(row["decision"] == "reject" for row in claims) == 9, "Claims rejection count changed")
        audit.check(sum(row["decision"] == "revise" for row in claims) == 2, "Claims revision count changed")
        audit.check(sum(row["decision"] == "accept_with_conditions" for row in claims) == 1, "Conditional claim count changed")
        audit.check("appeal" in (root / "community-review-recourse.md").read_text(encoding="utf-8"), "Community appeal route is missing")
        audit.check("FMA-DP-01 fictional resource-allocation owner" in (root / "accountable-owner-record.md").read_text(encoding="utf-8"), "Accountable owner is missing")
        audit.check("AI may choose the rule." not in joined, "AI received rule-selection authority")
        audit.check("Automatic rule use: `permitted`" not in joined, "Progression grants automatic rule use")
        audit.check("authorizes real allocation" not in joined.lower(), "Reference grants real allocation authority")


def validate_controls(root: Path, mode: str, audit: Auditor) -> None:
    audit.check((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version changed")
    contract = read_json(root / "targeting-contract.json")
    release = read_json(root / "release.json")
    audit.check(contract["module"]["id"] == "oclc-app5-05", "Contract module ID changed")
    audit.check(contract["module"]["commons_release"] == "0.92.0", "Contract Commons release changed")
    audit.check(contract["source"]["independent_of_public_prevalence"] is True, "Contract source independence changed")
    audit.check(contract["resource"] == {"fictional_places": 280, "awards": 28, "places_per_award": 10, "partial_awards": False, "carryover": False, "automatic_action": False}, "Contract resource changed")
    audit.check(contract["analysis"]["rules"] == 4 and contract["analysis"]["assignment_rows"] == 6388, "Contract analysis shape changed")
    audit.check(contract["assessment"]["points"] == 15 and contract["assessment"]["noncompensable_gates"] == 26, "Contract assessment changed")
    expected_workspace = {"learner_files": 330, "learner_manifest_rows": 308, "reference_files": 340, "reference_manifest_rows": 318, "editable_records": 17, "editable_sql_files": 4}
    audit.check(contract["workspace"] == expected_workspace, "Contract workspace changed")
    audit.check(release["module_id"] == "oclc-app5-05" and release["commons_release"] == "0.92.0", "Release identity changed")
    audit.check(release["course_points"] == 15 and release["week6_checkpoint_points_after_acceptance"] == 25, "Release points changed")
    audit.check(release["targeting_release"]["candidate_tracts"] == 1597 and release["targeting_release"]["assignment_rows"] == 6388, "Release targeting shape changed")
    audit.check(release["reference_decision"]["score"] == 15 and release["reference_decision"]["gates_passed"] == 26, "Release score or gates changed")
    audit.check(release["reference_decision"]["progression"] == "continue with conditions", "Release progression changed")
    audit.check(release["reference_decision"]["module06_permission"] == "permitted for curriculum construction", "Module 06 permission changed")
    audit.check(release["reference_decision"]["week6_checkpoint_permission"].startswith("not yet"), "Week 6 checkpoint boundary changed")
    audit.check(release["reference_decision"]["automatic_rule_use"] == "prohibited", "Automatic rule use changed")
    for key in ("real_priority_or_eligibility", "outreach", "allocation_or_funding", "real_community_action", "service_delivery", "implementation", "deployment"):
        audit.check(release["reference_decision"][key] == "prohibited", f"Release authority changed: {key}")
    for key, value in contract["authority"].items():
        if key == "fictional_rule_comparison":
            audit.check(value == "permitted", "Fictional rule comparison permission changed")
        elif key == "fictional_intervention_planning":
            audit.check(value == "reserved for Module 06", "Module 06 reservation changed")
        else:
            audit.check(value == "prohibited", f"Contract authority changed: {key}")
    if EXPECTED_COMPLETE_CHECKS and EXPECTED_LEARNER_CHECKS:
        expected_validation = {
            "complete_checks": EXPECTED_COMPLETE_CHECKS,
            "starter_checks": EXPECTED_LEARNER_CHECKS,
            "protected_failure_routes": EXPECTED_FAILURE_ROUTES,
            "copied_answer_rejected": True,
            "complete_mode_starter_rejected": True,
            "two_upstream_freezes_match": True,
            "two_source_generations_match": True,
            "two_targeting_builds_match": True,
            "two_reference_workspaces_match": True,
        }
        audit.check(release["validation"] == expected_validation, "Release validation contract changed")

    authored = [root / name for name in ("README.md", "assessment.md", "instructor-notes.md", "data-spec.md", "source-record.yml", "targeting-contract.json", "release.json")]
    authored += [root / name for name in RECORD_FILES + SQL_FILES]
    text = "\n".join(path.read_text(encoding="utf-8") for path in authored)
    audit.check("—" not in text and "–" not in text, "Authored text contains an em or en dash")
    audit.check("C:\\Users\\" not in text, "Authored text contains a personal path")
    audit.check("deployment permitted" not in text.lower(), "Authored text grants deployment")


def validate(root: Path, mode: str = "complete", reproduce: bool = True) -> int:
    root = root.resolve()
    if mode not in {"complete", "learner"}:
        raise ValidationError(f"Unknown validation mode: {mode}")
    audit = Auditor()
    validate_manifest(root, mode, audit)
    validate_upstream(root, audit)
    validate_source(root, audit)
    validate_controls(root, mode, audit)
    validate_records(root, mode, audit)
    if mode == "complete":
        validate_outputs(root, audit)
        if reproduce:
            run_script(root, "freeze_upstream.py")
            run_script(root, "generate_fictional_planning.py", "--verify")
            run_script(root, "build_targeting_fairness.py", "--verify")
            audit.check(True, "Reproduction scripts passed")
    else:
        audit.check(not (root / "outputs").exists(), "Learner workspace contains reference outputs")
    return audit.count


def refresh_manifest(root: Path, relative: str) -> None:
    path = root / "release-manifest.csv"
    fields, rows = read_csv(path)
    for row in rows:
        if row["relative_path"] == relative:
            target = root / relative
            row["bytes"] = str(target.stat().st_size)
            row["sha256"] = sha256(target)
            break
    else:
        raise AssertionError(f"Manifest row not found: {relative}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def rewrite_csv(path: Path, mutate) -> None:
    fields, rows = read_csv(path)
    mutate(rows)
    output = io_csv(fields, rows)
    if path.suffix == ".gz":
        import io
        buffer = io.BytesIO()
        with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, mtime=0) as zipped:
            zipped.write(output)
        path.write_bytes(buffer.getvalue())
    else:
        path.write_bytes(output)


def io_csv(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    import io
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def expect_rejected(root: Path, mutation_name: str, mutate, files: tuple[str, ...]) -> None:
    originals = {relative: (root / relative).read_bytes() for relative in files}
    manifest_original = (root / "release-manifest.csv").read_bytes()
    try:
        mutate(root)
        for relative in files:
            if (root / relative).is_file() and any(row["relative_path"] == relative for row in read_csv(root / "release-manifest.csv")[1]):
                refresh_manifest(root, relative)
        try:
            validate(root, "complete", reproduce=False)
        except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError):
            return
        raise AssertionError(f"Validator accepted protected failure route: {mutation_name}")
    finally:
        for relative, content in originals.items():
            (root / relative).write_bytes(content)
        (root / "release-manifest.csv").write_bytes(manifest_original)


def self_check() -> None:
    from build_workspace import assemble

    with tempfile.TemporaryDirectory(prefix="app5-module05-validator-") as temporary:
        base = Path(temporary)
        reference = base / "reference"
        learner = base / "learner"
        assemble(reference, reference=True)
        assemble(learner, reference=False)
        complete_checks = validate(reference, "complete", reproduce=True)
        learner_checks = validate(learner, "learner", reproduce=False)

        run_script(reference, "validate_workspace.py", str(reference))
        run_script(learner, "validate_workspace.py", str(learner), "--mode", "learner")

        copied = learner / "fairness-definition-tradeoff.md"
        copied.write_bytes((reference / "fairness-definition-tradeoff.md").read_bytes())
        try:
            validate(learner, "learner", reproduce=False)
        except ValidationError:
            pass
        else:
            raise AssertionError("Learner validation accepted copied reference answers")
        copied.write_bytes((ROOT / "template/fairness-definition-tradeoff.md").read_bytes())
        try:
            validate(learner, "complete", reproduce=False)
        except ValidationError:
            pass
        else:
            raise AssertionError("Complete validation accepted a learner workspace")

        mutations = [
            ("upstream payload byte", lambda r: (r / "upstream/module04-reference/VERSION").write_text("0.1.1\n", encoding="utf-8"), ("upstream/module04-reference/VERSION",)),
            ("upstream manifest identity", lambda r: (r / "upstream/module04-handoff-manifest.csv").write_bytes((r / "upstream/module04-handoff-manifest.csv").read_bytes() + b"\n"), ("upstream/module04-handoff-manifest.csv",)),
            ("fictional source byte", lambda r: (r / "data/raw/fictional-planning-layer.csv.gz").write_bytes((r / "data/raw/fictional-planning-layer.csv.gz").read_bytes() + b"x"), ("data/raw/fictional-planning-layer.csv.gz",)),
            ("fifth rule", lambda r: (r / "data/rule-definitions.csv").write_bytes((r / "data/rule-definitions.csv").read_bytes() + b"fifth,invalid,invalid,invalid,invalid,10,28,280,0,invalid\n"), ("data/rule-definitions.csv",)),
            ("resource contract", lambda r: _edit_json(r / "targeting-contract.json", lambda d: d["resource"].__setitem__("fictional_places", 300)), ("targeting-contract.json",)),
            ("partial award", lambda r: rewrite_csv(r / "outputs/rule-assignments.csv.gz", lambda rows: rows[0].__setitem__("allocated_places", "5")), ("outputs/rule-assignments.csv.gz",)),
            ("automatic assignment", lambda r: rewrite_csv(r / "outputs/rule-assignments.csv.gz", lambda rows: rows[0].__setitem__("automatic_action", "1")), ("outputs/rule-assignments.csv.gz",)),
            ("public role relabel", lambda r: rewrite_csv(r / "outputs/linked-candidate-table.csv.gz", lambda rows: rows[0].__setitem__("public_evidence_role", "observed need")), ("outputs/linked-candidate-table.csv.gz",)),
            ("suppressed value zero", lambda r: rewrite_csv(r / "outputs/group-consequences.csv", lambda rows: rows[0].__setitem__("selected_suppressed_rows", "0")), ("outputs/group-consequences.csv",)),
            ("missing sensitivity", lambda r: rewrite_csv(r / "outputs/sensitivity-results.csv", lambda rows: rows.pop()), ("outputs/sensitivity-results.csv",)),
            ("equal county breach", lambda r: rewrite_csv(r / "outputs/county-concentration.csv", lambda rows: next(row for row in rows if row["rule_id"] == "equal_geographic").__setitem__("selected_tracts", "3")), ("outputs/county-concentration.csv",)),
            ("community selected objection", lambda r: rewrite_csv(r / "outputs/rule-assignments.csv.gz", lambda rows: next(row for row in rows if row["rule_id"] == "community_review" and row["selected"] == "1").__setitem__("fictional_objection_state", "unresolved_objection")), ("outputs/rule-assignments.csv.gz",)),
            ("score changed", lambda r: rewrite_csv(r / "week6-component-score.csv", lambda rows: rows[-1].__setitem__("points_awarded", "14")), ("week6-component-score.csv",)),
            ("failed gate", lambda r: rewrite_csv(r / "gate-results.csv", lambda rows: rows[0].__setitem__("status", "fail")), ("gate-results.csv",)),
            ("missing appeal", lambda r: (r / "community-review-recourse.md").write_text((r / "community-review-recourse.md").read_text(encoding="utf-8").replace("appeal", "review request"), encoding="utf-8"), ("community-review-recourse.md",)),
            ("missing owner", lambda r: (r / "accountable-owner-record.md").write_text((r / "accountable-owner-record.md").read_text(encoding="utf-8").replace("FMA-DP-01 fictional resource-allocation owner", "unassigned"), encoding="utf-8"), ("accountable-owner-record.md",)),
            ("AI chooses rule", lambda r: (r / "ai-use.md").write_text((r / "ai-use.md").read_text(encoding="utf-8") + "\nAI may choose the rule.\n", encoding="utf-8"), ("ai-use.md",)),
            ("automatic progression", lambda r: (r / "progression-decision.md").write_text((r / "progression-decision.md").read_text(encoding="utf-8").replace("Automatic rule use: `prohibited`", "Automatic rule use: `permitted`"), encoding="utf-8"), ("progression-decision.md",)),
            ("eligibility permitted", lambda r: _edit_json(r / "release.json", lambda d: d["reference_decision"].__setitem__("real_priority_or_eligibility", "permitted")), ("release.json",)),
            ("deployment permitted", lambda r: _edit_json(r / "release.json", lambda d: d["reference_decision"].__setitem__("deployment", "permitted")), ("release.json",)),
            ("source dependence", lambda r: _edit_json(r / "targeting-contract.json", lambda d: d["source"].__setitem__("independent_of_public_prevalence", False)), ("targeting-contract.json",)),
            ("Module 06 permission removed", lambda r: _edit_json(r / "release.json", lambda d: d["reference_decision"].__setitem__("module06_permission", "prohibited")), ("release.json",)),
            ("claim copied as need", lambda r: (r / "responsible-claims-audit.csv").write_text((r / "responsible-claims-audit.csv").read_text(encoding="utf-8") + "TC13,Public values prove need,accept,none,none\n", encoding="utf-8"), ("responsible-claims-audit.csv",)),
            ("real allocation wording", lambda r: (r / "decision-and-resource-contract.md").write_text((r / "decision-and-resource-contract.md").read_text(encoding="utf-8") + "\nThis release authorizes real allocation.\n", encoding="utf-8"), ("decision-and-resource-contract.md",)),
        ]
        for name, mutate, files in mutations:
            expect_rejected(reference, name, mutate, files)

    if EXPECTED_COMPLETE_CHECKS:
        assert complete_checks == EXPECTED_COMPLETE_CHECKS, (complete_checks, EXPECTED_COMPLETE_CHECKS)
    if EXPECTED_LEARNER_CHECKS:
        assert learner_checks == EXPECTED_LEARNER_CHECKS, (learner_checks, EXPECTED_LEARNER_CHECKS)
    assert len(mutations) == EXPECTED_FAILURE_ROUTES
    print(f"APP-5 Module 05 complete validation passed: {complete_checks} checks.")
    print(f"APP-5 Module 05 learner validation passed: {learner_checks} checks.")
    print(
        "APP-5 Module 05 validator self-check passed: reference, learner, copied-validator, copied-answer, "
        f"complete-mode learner, and {len(mutations)} protected failure routes rejected."
    )


def _edit_json(path: Path, mutate) -> None:
    data = read_json(path)
    mutate(data)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--mode", choices=("complete", "learner"), default="complete")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            checks = validate(args.workspace, args.mode, reproduce=args.mode == "complete")
            print(f"APP-5 Module 05 {args.mode} validation passed: {checks} checks.")
        else:
            parser.error("workspace is required unless --self-check is used")
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
