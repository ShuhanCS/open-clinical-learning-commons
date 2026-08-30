"""Validate an APP-3 Module 01 decision-framing workspace."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "assessment.md", "data-spec.md", "decision-contract.json",
    "profile_sources.py", "source-record.yml", "validate_workspace.py",
    "data/capacity-source-profile.csv", "data/measure-family-anchors.csv",
    "data/source-inventory.csv", "data/raw/Complications_and_Deaths-Hospital.csv.gz",
    "data/raw/HHS-Capacity-Massachusetts.csv.gz",
    "data/raw/Timely_and_Effective_Care-Hospital.csv.gz",
)
RECORD_FILES = (
    "clinical-performance-charter.md", "synthetic-service-declaration.md", "unit-of-flow.csv",
    "process-boundary.csv", "measure-family.csv", "source-feasibility-interpretation.md",
    "stakeholder-accountability-map.csv", "claim-boundary.csv", "ai-use.md",
    "progression-decision.md",
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
    import profile_sources

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
    require(contract["module"]["id"] == "oclc-app3-01" and contract["module"]["commons_release"] == "0.66.0", "Module identity matches")
    require(contract["module"]["hours"] == 15.5 and contract["package"] == {"immutable_manifest_rows": 14, "editable_records": 10, "assembled_files": 25}, "Workload and package contract match")
    require(contract["service"]["id"] == "CGH-ED-01" and contract["service"]["public_hospital_linkage"] == "prohibited", "Fictional service boundary matches")
    require(contract["assessment"] == {"course_points_awarded_here": 0, "week3_measure_component_points": 20, "week3_performance_diagnostic_points": 20, "noncompensable_gates": 12}, "Assessment handoff matches")
    require(contract["sources"]["timely"]["rows"] == 138084 and contract["sources"]["complications"]["rows"] == 95800 and contract["sources"]["capacity"]["rows"] == 1045406, "Complete-source dimensions match")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
    require(len(manifest) == 14 and [row["relative_path"] for row in manifest] == sorted(IMMUTABLE_FILES), "Manifest has 14 sorted immutable rows")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Manifest path is portable: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")
        require(bool(row["role"].strip()), f"Manifest role is present: {row['relative_path']}")

    source_summary = profile_sources.verify_committed(root)
    require(source_summary["timely_rows"] == 138084 and source_summary["complications_rows"] == 95800, "Complete CMS sources reproduce")
    require(source_summary["capacity_rows"] == 1045406 and source_summary["capacity_extract_rows"] == 15179, "HHS full profile and state extract reproduce")
    require(source_summary["capacity_extract_raw_sha256"] == "7689038ce3dd013fe26daf3e6433b15f419a10360e19d3a063789ce5ae2c1068", "HHS state extract identity reproduces")

    inventory_header, inventory = read_csv(root / "data/source-inventory.csv")
    require(inventory_header == ["source_id", "title", "publisher", "grain", "rows", "columns", "raw_bytes", "raw_sha256", "repository_artifact", "teaching_role", "claim_limit"], "Source-inventory header matches")
    require([row["source_id"] for row in inventory] == ["CMS-TIMELY-2026-08-13", "CMS-COMPLICATIONS-2026-08-13", "HHS-CAPACITY-2024-05-03", "CGH-ED-01-DECLARATION"], "Source inventory has four ordered evidence layers")
    require(inventory[-1]["rows"] == "0" and "no public hospital linkage" in inventory[-1]["claim_limit"], "Synthetic declaration contains no public rows or linkage")

    anchors_header, anchors = read_csv(root / "data/measure-family-anchors.csv")
    require(anchors_header == ["anchor_id", "source_id", "field_or_measure_id", "concept", "evidence_role", "source_rows", "reported_rows", "unavailable_rows", "period_or_range", "decision_use", "claim_limit"], "Measure-anchor header matches")
    require([row["anchor_id"] for row in anchors] == [f"A{index:02d}" for index in range(1, 11)], "Measure anchors have ten ordered facts")
    by_field = {row["field_or_measure_id"]: row for row in anchors}
    require(by_field["OP_18b"]["reported_rows"] == "4081" and by_field["PSI_90"]["reported_rows"] == "2908", "Timeliness and safety support matches")
    require(by_field["previous_day_total_ED_visits_7_day_sum"]["reported_rows"] == "10909", "Historical demand support matches")
    require(all("does not describe CGH-ED-01" in row["claim_limit"] for row in anchors), "Every public anchor preserves the local claim boundary")

    profile_header, profile = read_csv(root / "data/capacity-source-profile.csv")
    require(profile_header == ["metric_id", "metric", "value", "unit", "method", "decision_use"], "Capacity-profile header matches")
    require([row["metric_id"] for row in profile] == [f"CP{index:02d}" for index in range(1, 21)], "Capacity profile has 20 ordered facts")
    values = {row["metric_id"]: row["value"] for row in profile}
    require(values["CP01"] == "1045406" and values["CP02"] == "128" and values["CP05"] == "5172" and values["CP06"] == "226", "Complete HHS dimensions match")
    require(values["CP11"] == "15179" and values["CP12"] == "74" and values["CP13"] == "24", "HHS extract dimensions match")
    require(values["CP16"] == "15057" and values["CP17"] == "14807" and values["CP18"] == "13877" and values["CP19"] == "10909", "HHS field support matches")
    require(values["CP20"] == "0", "Public sources contain no patient-level rows")

    for relative in RECORD_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}")

    csv_contracts = (
        ("unit-of-flow.csv", ["state_id", "sequence", "state", "clock_status", "required_fields", "decision_use", "failure_branch", "owner"], "U", 6),
        ("process-boundary.csv", ["boundary_id", "boundary_type", "element", "included", "rule", "rationale", "owner", "next_module"], "B", 8),
        ("measure-family.csv", ["family_id", "family", "role", "unit", "denominator_or_base", "public_anchor", "future_local_source", "decision_use", "claim_limit", "owner"], "M", 7),
        ("stakeholder-accountability-map.csv", ["stakeholder_id", "role", "decision_right", "evidence_need", "burden_or_power", "engagement_point", "owner", "unresolved_question"], "S", 8),
        ("claim-boundary.csv", ["claim_id", "claim", "disposition", "reason", "evidence_needed", "owner"], "C", 8),
    )
    records: dict[str, list[dict[str, str]]] = {}
    for filename, expected_header, prefix, count in csv_contracts:
        header, rows = read_csv(root / filename)
        records[filename] = rows
        require(header == expected_header, f"{filename} header matches")
        id_field = header[0]
        require([row[id_field] for row in rows] == [f"{prefix}{index:02d}" for index in range(1, count + 1)], f"{filename} has {count} ordered rows")
        if not starter:
            require(all(all(row[column].strip() for column in header) for row in rows), f"Every {filename} row is complete")

    require([int(row["sequence"]) for row in records["unit-of-flow.csv"]] == list(range(1, 7)), "Unit of flow has six ordered states")
    if not starter:
        roles = {row["role"] for row in records["measure-family.csv"]}
        require({"outcome", "balancing", "process", "safety", "explanatory", "equity"}.issubset(roles), "Measure families include all required decision roles")
        require(all(row["disposition"] in {"allowed", "conditional", "prohibited"} for row in records["claim-boundary.csv"]), "Every claim has an allowed disposition")
        require(sum(row["disposition"] == "prohibited" for row in records["claim-boundary.csv"]) >= 5, "Prohibited operational claims remain explicit")

    charter = (root / "clinical-performance-charter.md").read_text(encoding="utf-8")
    charter_fields = (
        "Decision owner", "Decision", "Proposed next action", "Service", "Service status",
        "Unit of flow", "Entry", "Exit", "Problem statement", "Target population",
        "Public source role", "Future local evidence", "Measure families", "Evidence standard",
        "Accountability", "Claim boundary", "Stop or referral trigger", "Operational diagnosis",
        "Staffing change", "Clinical action", "Implementation status", "Module 02 handoff",
    )
    require(all(field(charter, label) is not None for label in charter_fields), "Decision charter has every required field")
    declaration = (root / "synthetic-service-declaration.md").read_text(encoding="utf-8")
    declaration_fields = ("Service ID", "Status", "Care setting", "Population", "Unit of flow", "Public source relationship", "Operational tables begin", "Public hospital attribution", "Real patient records", "Operational diagnosis status", "Staffing recommendation status", "Implementation status")
    require(all(field(declaration, label) is not None for label in declaration_fields), "Synthetic declaration has every required field")
    if not starter:
        lower = (charter + declaration).lower()
        for phrase in ("cgh-ed-01", "fictional", "one synthetic adult emergency encounter", "no public hospital linkage", "prohibited in module 01", "not authorized"):
            require(phrase in lower, f"Decision records include: {phrase}")

    interpretation = (root / "source-feasibility-interpretation.md").read_text(encoding="utf-8").lower()
    if not starter:
        for phrase in ("138,084", "95,800", "1,045,406", "481,497,539", "15,179", "4,658", "4,790", "5,172", "-999999", "does not describe current capacity", "no public source supports hospital ranking"):
            require(phrase in interpretation, f"Source interpretation includes: {phrase}")

    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(field(ai_use, label) is not None for label in ai_fields), "AI-use record has every required field")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    gate_rows = [line for line in progression.splitlines() if re.match(r"^\| G\d{2} \|", line)]
    condition_rows = [line for line in progression.splitlines() if re.match(r"^\| O\d{2} \|", line)]
    require(len(gate_rows) == 12, "Progression records 12 gates")
    require(len(condition_rows) == 7, "Progression records seven owned conditions")
    if not starter:
        require(all("| pass |" in row for row in gate_rows), "All reference gates pass")
        require(all("| open |" in row for row in condition_rows), "Seven owned conditions remain open")
        progression_value = field(progression, "Progression")
        permission = field(progression, "Module 02 permission")
        require(progression_value in ALLOWED_PROGRESSION, "Progression value is allowed")
        require((progression_value in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction"), "Module 02 permission matches progression")
        for label in ("Operational diagnosis", "Staffing change", "Clinical action", "Hospital ranking", "Public-to-synthetic linkage"):
            require(field(progression, label) == "prohibited", f"{label} remains prohibited")

    report = {"status": "pass", "mode": "starter" if starter else "complete", "checks_passed": len(checks), "manifest_rows": 14, "assembled_files": 25, "course_points_awarded_here": 0}
    print(f"APP-3 Module 01 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app3-module01-validate-") as temp_dir:
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
        source_path = changed_source / "data/raw/HHS-Capacity-Massachusetts.csv.gz"
        raw = gzip.decompress(source_path.read_bytes()).replace(b"hospital_pk", b"hospital_xx", 1)
        with source_path.open("wb") as handle:
            with gzip.GzipFile(filename="", mode="wb", fileobj=handle, mtime=0) as zipped:
                zipped.write(raw)
        missing_record = base / "missing-record"
        shutil.copytree(reference, missing_record)
        (missing_record / "measure-family.csv").unlink()
        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        path = bad_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Progression: `continue with conditions`", "Progression: `deploy`"), encoding="utf-8", newline="\n")
        bad_claim = base / "bad-claim"
        shutil.copytree(reference, bad_claim)
        path = bad_claim / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Staffing change: `prohibited`", "Staffing change: `recommended`"), encoding="utf-8", newline="\n")
        cases = (
            (changed_source, "Manifest SHA-256 matches"),
            (missing_record, "Workspace has exactly 25 expected files"),
            (bad_progression, "Progression value is allowed"),
            (bad_claim, "Staffing change remains prohibited"),
        )
        for workspace, expected in cases:
            try:
                validate(workspace)
            except ValidationError as error:
                assert expected in str(error), str(error)
            else:
                raise AssertionError(f"Validator accepted invalid workspace: {workspace.name}")
    print(f"APP-3 Module 01 validator self-check passed: {complete_report['checks_passed']} complete checks and {starter_report['checks_passed']} starter checks; incomplete and broken workspaces rejected.")


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
