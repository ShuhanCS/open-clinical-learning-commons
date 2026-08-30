"""Validate an APP-1 Module 01 decision-framing workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from decimal import Decimal
from pathlib import Path


PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    "VERSION", "decision-contract.json", "source-record.yml", "data-spec.md",
    "assessment.md", "profile_source.py", "validate_workspace.py",
    "data/source-table-inventory.csv", "data/source-feasibility.csv",
)
RECORD_FILES = (
    "care-pathway-decision-charter.md", "pathway-map.csv", "outcome-set.csv",
    "evidence-standard.csv", "stakeholder-map.csv", "improvement-options.csv",
    "source-feasibility-interpretation.md", "ai-use.md", "progression-decision.md",
)
EXPECTED_TABLES = (
    "allergies", "careplans", "conditions", "devices", "encounters", "imaging_studies",
    "immunizations", "medications", "observations", "organizations", "patients",
    "payer_transitions", "payers", "procedures", "providers", "supplies",
)
EXPECTED_FEASIBILITY = {
    "F01": "1171", "F02": "518", "F03": "9", "F04": "8", "F05": "25",
    "F06": "476", "F07": "129", "F08": "87", "F09": "25", "F10": "62",
    "F11": "64", "F12": "not ready",
}
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}


class ValidationError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    expected_files = set(IMMUTABLE_FILES) | set(RECORD_FILES) | {"release-manifest.csv"}
    require(root.is_dir(), "Workspace directory exists")
    actual_files = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    require(actual_files == expected_files and len(actual_files) == 19, "Workspace has exactly 19 expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.2.0", "Module version is 0.2.0")

    contract = json.loads((root / "decision-contract.json").read_text(encoding="utf-8"))
    require(contract["module"]["id"] == "oclc-app1-01" and contract["module"]["commons_release"] == "0.49.1", "Module identity matches")
    require(contract["module"]["hours"] == 15.5 and contract["package"] == {"immutable_manifest_rows": 9, "editable_records": 9, "assembled_files": 19}, "Workload and package contract match")
    require(contract["assessment"] == {"readiness_points": 20, "minimum_points": 16, "criteria": 5, "noncompensable_gates": 12, "course_points_awarded_here": 0}, "Readiness assessment contract matches")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
    require(len(manifest) == 9 and [row["relative_path"] for row in manifest] == sorted(IMMUTABLE_FILES), "Manifest has nine sorted immutable rows")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Manifest path is portable: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")
        require(bool(row["role"].strip()), f"Manifest role is present: {row['relative_path']}")

    inventory_header, inventory = read_csv(root / "data/source-table-inventory.csv")
    require(inventory_header == ["table_name", "archive_path", "source_bytes", "source_rows", "source_columns", "source_sha256"], "Source inventory header matches")
    require(tuple(row["table_name"] for row in inventory) == EXPECTED_TABLES, "Source inventory has 16 ordered tables")
    require(sum(int(row["source_rows"]) for row in inventory) == 471836, "Source inventory totals 471836 rows")
    require(sum(int(row["source_bytes"]) for row in inventory) == 82293440, "Source inventory totals 82293440 bytes")
    inventory_by_table = {row["table_name"]: row for row in inventory}
    require(inventory_by_table["patients"]["source_rows"] == "1171" and inventory_by_table["encounters"]["source_rows"] == "53346", "Patient and encounter counts match")
    require(inventory_by_table["organizations"]["source_rows"] == "1119" and inventory_by_table["observations"]["source_rows"] == "299697", "Organization and observation counts match")
    require(inventory_by_table["medications"]["source_rows"] == "42989" and inventory_by_table["procedures"]["source_rows"] == "34981", "Medication and procedure counts match")
    require(all(re.fullmatch(r"[0-9a-f]{64}", row["source_sha256"]) for row in inventory), "Every source table has a SHA-256")

    feasibility_header, feasibility = read_csv(root / "data/source-feasibility.csv")
    require(feasibility_header == ["metric_id", "metric", "value", "unit", "rule", "decision_use"], "Feasibility header matches")
    require([row["metric_id"] for row in feasibility] == [f"F{index:02d}" for index in range(1, 13)], "Feasibility has twelve ordered facts")
    values = {row["metric_id"]: row["value"] for row in feasibility}
    require(values == EXPECTED_FEASIBILITY, "Feasibility values match the pinned full source")
    require(int(values["F02"]) - int(values["F03"]) - int(values["F04"]) - int(values["F05"]) == int(values["F06"]), "Initial and landmark cohort counts reconcile")
    require(int(values["F09"]) + int(values["F10"]) == int(values["F08"]), "Later outcome counts reconcile")
    require(values["F11"] == "64" and values["F12"] == "not ready", "Raw site comparison remains not ready")

    for relative in RECORD_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}")

    path_header, pathway = read_csv(root / "pathway-map.csv")
    require(path_header == ["state_id", "sequence", "state", "entry_rule", "exit_rule", "time_relation", "source_evidence", "owner", "failure_or_ambiguity", "downstream_use"], "Pathway header matches")
    require([row["state_id"] for row in pathway] == [f"P{index:02d}" for index in range(1, 9)] and [int(row["sequence"]) for row in pathway] == list(range(1, 9)), "Pathway has eight ordered states")
    outcome_header, outcomes = read_csv(root / "outcome-set.csv")
    require(outcome_header == ["outcome_id", "role", "outcome_concept", "timing", "numerator_or_event", "denominator_or_risk_set", "source_status", "decision_use", "claim_limit"], "Outcome-set header matches")
    require([row["outcome_id"] for row in outcomes] == [f"O{index:02d}" for index in range(1, 7)] and [row["role"] for row in outcomes] == ["primary", "process", "balancing", "safety", "access", "patient-important"], "Outcome set has six required roles")
    evidence_header, evidence = read_csv(root / "evidence-standard.csv")
    require(evidence_header == ["stage_id", "decision_stage", "minimum_evidence", "automatic_stop", "owner"] and [row["stage_id"] for row in evidence] == ["E01", "E02", "E03"], "Evidence standard has three stages")
    stakeholder_header, stakeholders = read_csv(root / "stakeholder-map.csv")
    require(stakeholder_header == ["stakeholder_id", "role", "decision_need", "affected_or_accountable", "power_or_burden", "engagement_point", "owner", "unresolved_question"] and [row["stakeholder_id"] for row in stakeholders] == [f"S{index:02d}" for index in range(1, 8)], "Stakeholder map has seven roles")
    option_header, options = read_csv(root / "improvement-options.csv")
    require(option_header == ["option_id", "option", "targeted_pathway_gap", "required_workflow", "measure", "balancing_measure", "equity_or_access_risk", "evidence_needed", "disposition"] and [row["option_id"] for row in options] == ["I01", "I02", "I03"], "Improvement table has three options")
    if not starter:
        for rows, header, label in ((pathway, path_header, "pathway"), (outcomes, outcome_header, "outcome"), (evidence, evidence_header, "evidence"), (stakeholders, stakeholder_header, "stakeholder"), (options, option_header, "improvement")):
            require(all(all(row[column].strip() for column in header) for row in rows), f"Every {label} row is complete")

    charter = (root / "care-pathway-decision-charter.md").read_text(encoding="utf-8")
    charter_fields = (
        "Decision owner", "Decision", "Proposed next action", "Target population", "Pathway entry",
        "Discharge origin", "Exposure", "Comparator", "Exposure window", "Landmark",
        "Landmark exclusions", "Primary outcome", "Outcome window", "Analysis aim",
        "Evidence standard", "Feasibility conclusion", "Raw site comparison",
        "Patient-important evidence gap", "Claim boundary", "Stop or referral trigger",
    )
    require(all(field(charter, label) is not None for label in charter_fields), "Decision charter has every required field")
    if not starter:
        lower = charter.lower()
        for phrase in ("day 30", "after day 30", "day 365", "synthetic", "not ready", "64", "not efficacy", "does not authorize implementation"):
            require(phrase in lower, f"Decision charter includes: {phrase}")

    interpretation = (root / "source-feasibility-interpretation.md").read_text(encoding="utf-8").lower()
    require(all(f"f{index:02d}" in interpretation for index in range(1, 13)), "Feasibility interpretation covers F01 through F12")
    if not starter:
        for phrase in ("518", "nine", "eight", "twenty-five", "476", "129", "87", "64", "immortal-time", "do not estimate"):
            require(phrase in interpretation, f"Feasibility interpretation includes: {phrase}")

    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(field(ai_use, label) is not None for label in ai_fields), "AI-use record has every required field")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    if not starter:
        score_value = field(progression, "Readiness score")
        score_match = re.fullmatch(r"(\d+(?:\.\d+)?) of 20\.00", score_value or "")
        require(score_match is not None and Decimal(score_match.group(1)) >= Decimal("16") and Decimal(score_match.group(1)) <= Decimal("20"), "Readiness score is between 16 and 20")
        require(field(progression, "Gate result") is not None and "no failed gate" in field(progression, "Gate result").lower(), "No final readiness gate failed")
        progression_value = field(progression, "Progression")
        require(progression_value in ALLOWED_PROGRESSION, "Progression value is allowed")
        permitted = field(progression, "Module 02 permission")
        require((progression_value in {"continue", "continue with conditions"}) == (permitted == "permitted for curriculum construction"), "Module 02 permission matches progression")
        condition_rows = [line for line in progression.splitlines() if re.match(r"^\| C\d{2} \|", line)]
        require(len(condition_rows) >= 6 and all("| open |" in line or "| closed |" in line for line in condition_rows), "Progression records at least six owned conditions")

    report = {
        "status": "pass", "mode": "starter" if starter else "complete",
        "checks_passed": len(checks), "manifest_rows": 9,
        "assembled_files": 19, "readiness_points": 20,
    }
    print(f"APP-1 Module 01 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app1-module01-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, starter = base / "reference", base / "starter"
        build_workspace.assemble(reference, reference=True)
        complete_report = validate(reference)
        build_workspace.assemble(starter)
        starter_report = validate(starter, starter=True)
        try:
            validate(starter)
        except ValidationError as error:
            assert "Record is complete" in str(error), str(error)
        else:
            raise AssertionError("Validator accepted an incomplete starter")

        cases: list[tuple[Path, str]] = []
        broken_source = base / "broken-source"
        shutil.copytree(reference, broken_source)
        path = broken_source / "data/source-feasibility.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("F06,day-30 landmark eligible,476", "F06,day-30 landmark eligible,477"), encoding="utf-8", newline="\n")
        cases.append((broken_source, "Manifest SHA-256 matches"))
        missing_path = base / "missing-path"
        shutil.copytree(reference, missing_path)
        path = missing_path / "pathway-map.csv"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8", newline="\n")
        cases.append((missing_path, "Pathway has eight ordered states"))
        bad_score = base / "bad-score"
        shutil.copytree(reference, bad_score)
        path = bad_score / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("20.00 of 20.00", "21.00 of 20.00"), encoding="utf-8", newline="\n")
        cases.append((bad_score, "Readiness score is between 16 and 20"))
        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        path = bad_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Progression: `continue with conditions`", "Progression: `deploy`"), encoding="utf-8", newline="\n")
        cases.append((bad_progression, "Progression value is allowed"))
        for workspace, expected in cases:
            try:
                validate(workspace)
            except ValidationError as error:
                assert expected in str(error), str(error)
            else:
                raise AssertionError(f"Validator accepted invalid workspace: {workspace.name}")
    print(f"APP-1 Module 01 validator self-check passed: {complete_report['checks_passed']} complete checks and {starter_report['checks_passed']} starter checks; incomplete and broken workspaces rejected.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.workspace:
            parser.error("workspace is required unless --self-check is used")
        validate(args.workspace.resolve(), starter=args.starter)
    except (OSError, ValueError, KeyError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
