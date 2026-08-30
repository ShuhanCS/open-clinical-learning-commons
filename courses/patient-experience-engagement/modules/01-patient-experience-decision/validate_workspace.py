"""Validate an APP-2 Module 01 decision-framing workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes", "README.md", "VERSION", "assessment.md", "build_workspace.py",
    "data-spec.md", "decision-contract.json", "instructor-notes.md", "profile_source.py",
    "source-record.yml", "validate_workspace.py", "data/raw/HCAHPS-Hospital.csv.gz",
    "data/source-profile.csv", "data/measure-inventory.csv", "data/discharge-measure-profile.csv",
)
RECORD_FILES = (
    "patient-experience-decision-charter.md", "construct-map.csv", "patient-journey-map.csv",
    "evidence-needs.csv", "stakeholder-partnership-map.csv", "claim-boundary.csv",
    "source-feasibility-interpretation.md", "ai-use.md", "progression-decision.md",
)
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
    import profile_source

    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    expected_files = set(IMMUTABLE_FILES) | set(RECORD_FILES) | {"release-manifest.csv"}
    require(root.is_dir(), "Workspace directory exists")
    actual_files = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    require(actual_files == expected_files and len(actual_files) == 25, "Workspace has exactly 25 expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "decision-contract.json").read_text(encoding="utf-8"))
    require(contract["module"]["id"] == "oclc-app2-01" and contract["module"]["commons_release"] == "0.56.0", "Module identity matches")
    require(contract["module"]["hours"] == 15.5 and contract["package"] == {"immutable_manifest_rows": 15, "editable_records": 9, "assembled_files": 25}, "Workload and package contract match")
    require(contract["assessment"] == {"course_points_awarded_here": 0, "week3_measurement_component_points": 20, "noncompensable_gates": 12}, "Assessment handoff matches")
    require(contract["source"]["rows"] == 325720 and contract["source"]["facilities"] == 4790 and contract["source"]["measure_ids"] == 68, "Source dimensions match")
    require(contract["source"]["patient_level_rows"] == 0, "Source remains hospital level")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
    require(len(manifest) == 15 and [row["relative_path"] for row in manifest] == sorted(IMMUTABLE_FILES), "Manifest has 15 sorted immutable rows")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Manifest path is portable: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")
        require(bool(row["role"].strip()), f"Manifest role is present: {row['relative_path']}")

    summary = profile_source.verify_committed(root / "data/raw/HCAHPS-Hospital.csv.gz", root / "data")
    require(summary == {"rows": 325720, "facilities": 4790, "measures": 68, "states": 56, "response_rate_facilities": 3949, "completed_surveys_sum": 2411406}, "Full-source profile reproduces")

    profile_header, profile = read_csv(root / "data/source-profile.csv")
    require(profile_header == ["metric_id", "metric", "value", "unit", "method", "decision_use"], "Source-profile header matches")
    require([row["metric_id"] for row in profile] == [f"SP{index:02d}" for index in range(1, 21)], "Source profile has 20 ordered facts")
    profile_values = {row["metric_id"]: row["value"] for row in profile}
    require(profile_values["SP01"] == "325720" and profile_values["SP03"] == "4790" and profile_values["SP04"] == "68", "Source profile dimensions match")
    require(profile_values["SP13"] == "3949" and profile_values["SP14"] == "841", "Response support matches")
    require(profile_values["SP15"] == "18" and profile_values["SP16"] == "22" and profile_values["SP17"] == "28", "Response-rate quartiles match")
    require(profile_values["SP18"] == "2411406" and profile_values["SP19"] == "0", "Completed-survey scale and patient-level boundary match")

    inventory_header, inventory = read_csv(root / "data/measure-inventory.csv")
    require(inventory_header == ["measure_id", "question", "answer_description", "reported_value_field", "facility_rows", "reported_value_rows", "unavailable_value_rows", "teaching_role"], "Measure-inventory header matches")
    require(len(inventory) == 68 and [row["measure_id"] for row in inventory] == sorted(row["measure_id"] for row in inventory), "Measure inventory has 68 sorted IDs")
    require(all(row["facility_rows"] == "4790" for row in inventory), "Every measure has one row per facility")
    inventory_by_id = {row["measure_id"]: row for row in inventory}
    require(inventory_by_id["H_COMP_6_Y_P"]["reported_value_rows"] == "3949", "Primary discharge anchor support matches")
    require(inventory_by_id["H_SYMPTOMS_Y_P"]["reported_value_rows"] == "3610", "Warning-sign item support matches")

    discharge_header, discharge = read_csv(root / "data/discharge-measure-profile.csv")
    require(discharge_header == ["measure_id", "role", "facility_rows", "reported_percent_rows", "unavailable_percent_rows", "min_percent", "q1_percent", "median_percent", "q3_percent", "max_percent"], "Discharge-profile header matches")
    require([row["measure_id"] for row in discharge] == ["H_COMP_6_Y_P", "H_COMP_6_N_P", "H_DISCH_HELP_Y_P", "H_SYMPTOMS_Y_P"], "Discharge profile has four ordered anchors")
    discharge_by_id = {row["measure_id"]: row for row in discharge}
    require(discharge_by_id["H_COMP_6_Y_P"]["median_percent"] == "87" and discharge_by_id["H_COMP_6_Y_P"]["unavailable_percent_rows"] == "841", "Primary discharge profile matches")
    require(discharge_by_id["H_DISCH_HELP_Y_P"]["median_percent"] == "86" and discharge_by_id["H_DISCH_HELP_Y_P"]["unavailable_percent_rows"] == "1180", "Help-after-discharge profile matches")

    for relative in RECORD_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}")

    construct_header, constructs = read_csv(root / "construct-map.csv")
    require(construct_header == ["construct_id", "concept", "working_definition", "role_in_decision", "measure_status", "patient_partner_question", "claim_limit"], "Construct-map header matches")
    require([row["construct_id"] for row in constructs] == [f"C{index:02d}" for index in range(1, 8)], "Construct map has seven concepts")

    journey_header, journey = read_csv(root / "patient-journey-map.csv")
    require(journey_header == ["stage_id", "sequence", "stage", "patient_question", "measurement_opportunity", "access_or_burden_risk", "partner_role", "owner", "unresolved_evidence"], "Journey-map header matches")
    require([row["stage_id"] for row in journey] == [f"J{index:02d}" for index in range(1, 8)] and [int(row["sequence"]) for row in journey] == list(range(1, 8)), "Patient journey has seven ordered stages")

    evidence_header, evidence = read_csv(root / "evidence-needs.csv")
    require(evidence_header == ["need_id", "evidence_needed", "available_in_public_hcahps", "local_collection_required", "patient_partner_role", "decision_if_missing", "owner", "next_module"], "Evidence-needs header matches")
    require([row["need_id"] for row in evidence] == [f"E{index:02d}" for index in range(1, 9)], "Evidence-needs record has eight rows")

    stakeholder_header, stakeholders = read_csv(root / "stakeholder-partnership-map.csv")
    require(stakeholder_header == ["stakeholder_id", "role", "decision_right", "evidence_need", "burden_or_power", "engagement_point", "owner", "unresolved_question"], "Stakeholder-map header matches")
    require([row["stakeholder_id"] for row in stakeholders] == [f"S{index:02d}" for index in range(1, 8)], "Stakeholder map has seven roles")

    boundary_header, boundaries = read_csv(root / "claim-boundary.csv")
    require(boundary_header == ["boundary_id", "claim", "disposition", "reason", "evidence_needed", "owner"], "Claim-boundary header matches")
    require([row["boundary_id"] for row in boundaries] == [f"B{index:02d}" for index in range(1, 9)], "Claim boundary has eight rows")
    require(all(row["disposition"] in {"allowed", "conditional", "prohibited"} for row in boundaries), "Every claim has an allowed disposition")

    if not starter:
        require(any("patient" in row["role"].lower() and "co-own" in row["decision_right"].lower() for row in stakeholders), "Patient partner co-ownership is explicit")
        for rows, header, label in (
            (constructs, construct_header, "construct"), (journey, journey_header, "journey"),
            (evidence, evidence_header, "evidence"), (stakeholders, stakeholder_header, "stakeholder"),
            (boundaries, boundary_header, "claim-boundary"),
        ):
            require(all(all(row[column].strip() for column in header) for row in rows), f"Every {label} row is complete")

    charter = (root / "patient-experience-decision-charter.md").read_text(encoding="utf-8")
    charter_fields = (
        "Decision owner", "Patient-partner authority", "Decision", "Proposed next action",
        "Target population", "Care setting", "Primary construct", "Supporting constructs",
        "Measure type", "Public source role", "Local evidence gap", "Language and access rule",
        "Proxy rule", "Burden rule", "Evidence standard", "Claim boundary",
        "Stop or referral trigger", "Module 02 handoff", "Implementation status",
        "Hospital-ranking status",
    )
    require(all(field(charter, label) is not None for label in charter_fields), "Decision charter has every required field")
    if not starter:
        lower = charter.lower()
        for phrase in (
            "recovery at home", "patient/caregiver", "multilingual", "hospital level",
            "not patient level", "instrument selection", "implementation is prohibited",
            "hospital ranking is prohibited",
        ):
            require(phrase in lower, f"Decision charter includes: {phrase}")

    interpretation = (root / "source-feasibility-interpretation.md").read_text(encoding="utf-8").lower()
    require(all(f"sp{index:02d}" in interpretation for index in range(1, 21)), "Source interpretation covers SP01 through SP20")
    if not starter:
        for phrase in (
            "325,720", "4,790", "68", "56", "3,949", "841", "22 percent",
            "2,411,406", "not patient-level", "does not support hospital ranking",
        ):
            require(phrase in interpretation, f"Source interpretation includes: {phrase}")

    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = (
        "Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared",
        "Files affected", "Output used, modified, or rejected", "Material claim",
        "Independent verification", "Correction or retained action", "Human owner",
        "Accountability statement",
    )
    require(all(field(ai_use, label) is not None for label in ai_fields), "AI-use record has every required field")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    gate_rows = [line for line in progression.splitlines() if re.match(r"^\| G\d{2} \|", line)]
    require(len(gate_rows) == 12, "Progression records 12 gates")
    if not starter:
        require(all("| pass |" in row for row in gate_rows), "All reference gates pass")
        require(field(progression, "Gate result") == "no failed gate", "No readiness gate failed")
        progression_value = field(progression, "Progression")
        require(progression_value in ALLOWED_PROGRESSION, "Progression value is allowed")
        permission = field(progression, "Module 02 permission")
        require((progression_value in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction"), "Module 02 permission matches progression")
        require(field(progression, "Clinical action") == "prohibited", "Clinical action remains prohibited")
        condition_rows = [line for line in progression.splitlines() if re.match(r"^\| O\d{2} \|", line)]
        require(len(condition_rows) == 7 and all("| open |" in row for row in condition_rows), "Seven owned conditions remain open")

    report = {
        "status": "pass", "mode": "starter" if starter else "complete",
        "checks_passed": len(checks), "manifest_rows": 15,
        "assembled_files": 25, "course_points_awarded_here": 0,
    }
    print(f"APP-2 Module 01 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app2-module01-validate-") as temp_dir:
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

        changed_source = base / "changed-source"
        shutil.copytree(reference, changed_source)
        path = changed_source / "data/source-profile.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("SP01,source rows,325720", "SP01,source rows,325721"), encoding="utf-8", newline="\n")
        missing_journey = base / "missing-journey"
        shutil.copytree(reference, missing_journey)
        path = missing_journey / "patient-journey-map.csv"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8", newline="\n")
        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        path = bad_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Progression: `continue with conditions`", "Progression: `deploy`"), encoding="utf-8", newline="\n")
        bad_claim = base / "bad-claim"
        shutil.copytree(reference, bad_claim)
        path = bad_claim / "patient-experience-decision-charter.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Hospital-ranking status: `hospital ranking is prohibited`", "Hospital-ranking status: `hospital ranking is allowed`"), encoding="utf-8", newline="\n")

        cases = (
            (changed_source, "Manifest SHA-256 matches"),
            (missing_journey, "Patient journey has seven ordered stages"),
            (bad_progression, "Progression value is allowed"),
            (bad_claim, "Decision charter includes: hospital ranking is prohibited"),
        )
        for workspace, expected in cases:
            try:
                validate(workspace)
            except ValidationError as error:
                assert expected in str(error), str(error)
            else:
                raise AssertionError(f"Validator accepted invalid workspace: {workspace.name}")
    print(f"APP-2 Module 01 validator self-check passed: {complete_report['checks_passed']} complete checks and {starter_report['checks_passed']} starter checks; incomplete and broken workspaces rejected.")


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
