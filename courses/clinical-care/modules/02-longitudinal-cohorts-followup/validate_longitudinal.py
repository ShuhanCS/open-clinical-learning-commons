"""Validate APP-1 Module 02 longitudinal cohort workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "source-record.yml", "extension-contract.json",
    "data-dictionary.csv", "assessment.md", "build_longitudinal.py", "validate_longitudinal.py",
)
WORK_FILES = (
    "README.md", "phenotype-spec.md", "transformation-record.md", "validation-notes.md",
    "reproducibility-check.md", "ai-use.md", "progression-decision.md",
    "sql/01-index-cohort.sql", "sql/02-event-audit.sql",
    "sql/03-longitudinal-cohort.sql", "sql/04-validation.sql",
)
OUTPUTS = {
    "analysis-cohort.csv": (476, 49, 200699, "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5"),
    "build-report.json": (1, None, 2926, "8829cb8c99e175abc4d9212ff0d3a1ccf6b1b73318ad28e5a5b9c8dd65ceb02f"),
    "censoring-summary.csv": (6, 6, 372, "46dba77dca430105431b40a1dccb478de0043496193d55ffbc42205435910f95"),
    "cohort-flow.csv": (5, 6, 446, "bb9c0828260a5e613a56c97b8fc701d5a9043e72cc2b205cd9df3bddc0635aed"),
    "event-audit.csv": (1018, 11, 210154, "8491e4c02d33771a904bcc095982cccd6265c3d301c10fc79ac259ceede6fe9c"),
    "index-cohort.csv": (518, 15, 101751, "f6f4311cfb617c55c31bb97afac38d328d161bd8e7ec17bb558735abeadf0107"),
    "longitudinal-cohort.csv": (518, 40, 166746, "ff684f8dce203c73a4f83e4ee781fe5eff15c0bc3c89652ded9acae906c2f1db"),
    "query-checks.csv": (26, 2, 640, "aecd10a6e122dcc34990fac08069cb3cf2339d61ed3eb0cce02beb899861988f"),
    "site-assignment.csv": (476, 10, 64967, "8cfbd4137e5f9ab8688a2fc88082f283443a913cba1167510e397f09e138964b"),
    "site-support.csv": (6, 15, 641, "b76f1ad7f77752e96060ade82d023695afa40d3a24128d2cd191ed0e53cf9088"),
}
REFERENCE_CHECKS = {
    "source people": 1171, "source encounters": 53346, "initial cohort": 518,
    "unique initial patients": 518, "index emergency": 451, "index inpatient": 67,
    "index deaths": 9, "early deaths": 8, "early acute returns": 25,
    "branch overlaps": 0, "landmark eligible": 476, "scheduled followup": 129,
    "no scheduled followup": 347, "later acute returns": 87,
    "exposed later acute returns": 25, "unexposed later acute returns": 62,
    "administrative censored": 389, "competing death censored": 0,
    "later deaths recognized": 3, "source organizations": 64,
    "invalid index order": 0, "invalid followup time": 0,
    "invalid early acute time": 0, "invalid later acute time": 0,
    "landmark conservation": 518, "outcome conservation": 476,
}
EVENT_ROLES = {
    "early_acute_return": (27, 25, 25),
    "early_death": (8, 8, 8),
    "index_death": (9, 9, 9),
    "index_encounter": (518, 518, 518),
    "later_acute_return": (241, 99, 99),
    "later_death": (3, 3, 3),
    "scheduled_followup": (212, 138, 138),
}
SITE_SUPPORT = {
    "SITE-A": (76, 19, 21, 39, 22, 15),
    "SITE-B": (75, 19, 10, 35, 22, 18),
    "SITE-C": (68, 19, 10, 21, 26, 21),
    "SITE-D": (88, 21, 13, 26, 32, 30),
    "SITE-E": (87, 20, 18, 25, 36, 26),
    "SITE-F": (82, 31, 15, 13, 21, 48),
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


def markdown_field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, starter: bool = False, database: Path | None = None) -> dict[str, object]:
    import build_longitudinal

    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    is_module_root = root == MODULE_ROOT.resolve() and (root / "template").is_dir()
    required = set(IMMUTABLE_FILES) | set(WORK_FILES)
    require(root.is_dir(), "Workspace directory exists")
    require(all((root / relative).is_file() for relative in required), "All fixed and work files are present")
    manifest_path = root / "workspace-manifest.csv"
    if not is_module_root:
        expected = required | {"workspace-manifest.csv"}
        if not starter:
            expected |= {f"outputs/{name}" for name in OUTPUTS}
        actual = {
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        require(actual == expected, f"Workspace has exactly {20 if starter else 30} expected files")
        manifest_header, manifest = read_csv(manifest_path)
        require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Workspace manifest header matches")
        require(len(manifest) == 8 and [row["relative_path"] for row in manifest] == sorted(IMMUTABLE_FILES), "Workspace manifest has eight sorted immutable rows")
        for row in manifest:
            path = root / row["relative_path"]
            require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
            require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
            require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")
    source = (root / "source-record.yml").read_text(encoding="utf-8")
    require("commons_release: 0.50.0" in source and "corrected_landmark_denominator: 476" in source, "Source record has corrected module identity")
    require("1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a" in source, "Source database fingerprint matches")
    contract = json.loads((root / "extension-contract.json").read_text(encoding="utf-8"))
    require(contract["extension_id"] == "app1-six-site-v1" and contract["seed"] == "app1-six-site-v1", "Extension identity and seed match")
    require(contract["known_direct_site_effect"].startswith("zero") and contract["field_class"] == "synthetic_extension", "Extension zero-effect and field class match")
    for tier, probabilities in contract["probabilities"].items():
        require(sum(Decimal(value) for value in probabilities) == Decimal("1.00"), f"{tier} site probabilities sum to 1.00")

    dictionary_header, dictionary = read_csv(root / "data-dictionary.csv")
    require(dictionary_header == ["field_id", "file", "field", "data_type", "grain", "field_class", "source_or_derivation", "timing_availability", "missing_meaning", "allowed_use", "prohibited_interpretation"], "Data dictionary header matches")
    require(len(dictionary) == 87 and [row["field_id"] for row in dictionary] == [f"D{index:03d}" for index in range(1, 88)], "Data dictionary has 87 ordered rows")
    require(all(all(value.strip() for value in row.values()) for row in dictionary), "Every data dictionary row is complete")

    text_files = [relative for relative in required if Path(relative).suffix.lower() in {".md", ".csv", ".sql", ".yml", ".json"}]
    for relative in text_files:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        if starter and relative in WORK_FILES:
            require(bool(PLACEHOLDER.search(text)), f"Starter prompt is present: {relative}")
        if not starter and relative in WORK_FILES:
            require(not PLACEHOLDER.search(text), f"Work file is complete: {relative}")

    if starter:
        require(not (root / "outputs").exists(), "Starter has no prebuilt outputs")
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "assembled_files": 20}
        print(f"APP-1 Module 02 starter validation passed: {len(checks)} checks.")
        return report

    for relative in WORK_FILES[-4:]:
        require(build_longitudinal.read_query(root / relative).endswith(";"), f"Read-only SQL passes: {relative}")

    output_root = root / "outputs"
    require(all((output_root / name).is_file() for name in OUTPUTS), "All ten reference outputs are present")
    output_headers: set[str] = set()
    for name, (expected_rows, expected_fields, expected_bytes, expected_hash) in OUTPUTS.items():
        path = output_root / name
        require(path.stat().st_size == expected_bytes, f"Output bytes match: {name}")
        require(sha256(path) == expected_hash, f"Output SHA-256 matches: {name}")
        if path.suffix == ".csv":
            header, rows = read_csv(path)
            output_headers.update(header)
            require(len(rows) == expected_rows and len(header) == expected_fields, f"Output shape matches: {name}")
    require({row["field"] for row in dictionary} == output_headers, "Data dictionary covers every released CSV field")

    report_json = json.loads((output_root / "build-report.json").read_text(encoding="utf-8"))
    require(report_json["module"] == "oclc-app1-02" and report_json["commons_release"] == "0.50.0", "Build report identity matches")
    require(report_json["source_database"] == {"bytes": 141234176, "sha256": "1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a"}, "Build report source identity matches")
    require(report_json["checks"] == REFERENCE_CHECKS, "Build report contains all 26 exact checks")

    index_header, index_rows = read_csv(output_root / "index-cohort.csv")
    require(len({row["patient_id"] for row in index_rows}) == 518, "Index cohort has 518 unique people")
    require(sum(row["index_encounter_class"] == "emergency" for row in index_rows) == 451 and sum(row["index_encounter_class"] == "inpatient" for row in index_rows) == 67, "Index class split is 451/67")
    require(all(int(row["age_at_index"]) >= 18 for row in index_rows), "Every index person is an adult")
    require(len(index_header) == 15, "Index cohort has 15 fields")

    _, longitudinal = read_csv(output_root / "longitudinal-cohort.csv")
    require(len({row["patient_id"] for row in longitudinal}) == 518, "Longitudinal cohort has one row per initial person")
    require(sum(int(row["index_death_flag"]) for row in longitudinal) == 9, "Nine index deaths remain visible")
    require(sum(int(row["early_death_flag"]) for row in longitudinal) == 8, "Eight early deaths remain visible")
    require(sum(int(row["early_acute_return_flag"]) for row in longitudinal) == 25, "Twenty-five early acute returns remain visible")
    eligible = [row for row in longitudinal if row["landmark_eligible_flag"] == "1"]
    require(len(eligible) == 476, "Corrected landmark cohort has 476 people")
    require(sum(row["landmark_exposure"] == "1" for row in eligible) == 129, "Landmark exposure count is 129")
    require(sum(row["event_indicator"] == "1" for row in eligible) == 87, "Later event count is 87")
    require(sum(row["landmark_exposure"] == "1" and row["event_indicator"] == "1" for row in eligible) == 25, "Exposed event count is 25")
    require(sum(row["landmark_exposure"] == "0" and row["event_indicator"] == "1" for row in eligible) == 62, "Unexposed event count is 62")
    require(sum(row["censor_reason"] == "administrative_end" for row in eligible) == 389 and sum(row["censor_reason"] == "competing_death" for row in eligible) == 0, "Censoring is 389 administrative and 0 competing death")
    require(sum(int(row["later_death_flag"]) for row in eligible) == 3, "Three later deaths remain visible")
    require(all(Decimal(row["observed_time_days"]) > 0 and Decimal(row["observed_time_days"]) <= 335 for row in eligible), "Every eligible observed time is positive and bounded")

    _, event_rows = read_csv(output_root / "event-audit.csv")
    for role, (row_count, selected_count, people_count) in EVENT_ROLES.items():
        group = [row for row in event_rows if row["event_role"] == role]
        require(len(group) == row_count, f"Event audit row count matches: {role}")
        require(sum(row["selected_for_analysis"] == "1" for row in group) == selected_count, f"Event audit selected count matches: {role}")
        require(len({row["patient_id"] for row in group}) == people_count, f"Event audit person count matches: {role}")

    _, flow = read_csv(output_root / "cohort-flow.csv")
    require([int(row["remaining"]) for row in flow] == [518, 509, 501, 476, 476], "Cohort flow conserves the corrected risk set")
    _, censoring = read_csv(output_root / "censoring-summary.csv")
    censor_counts = {(row["landmark_exposure"], row["disposition"]): int(row["people"]) for row in censoring}
    require(censor_counts == {("1", "event"): 25, ("1", "competing_death"): 0, ("1", "administrative_end"): 104, ("0", "event"): 62, ("0", "competing_death"): 0, ("0", "administrative_end"): 285}, "Censoring summary reconciles exposure and disposition")

    assignment_header, assignments = read_csv(output_root / "site-assignment.csv")
    require(len({row["patient_id"] for row in assignments}) == 476 and len(assignment_header) == 10, "Site assignment has one row per eligible person")
    require({row["teaching_site_id"] for row in assignments} == set(SITE_SUPPORT), "All six teaching sites are present")
    require(all(row["extension_seed"] == "app1-six-site-v1" and row["extension_version"] == "0.1.0" and row["field_class"] == "synthetic_extension" for row in assignments), "Every site assignment has exact provenance")
    regenerated = build_longitudinal.assign_sites(longitudinal, contract)
    require(assignments == [{key: str(value) for key, value in row.items()} for row in regenerated], "Every site assignment reproduces from the fixed algorithm")

    _, analysis = read_csv(output_root / "analysis-cohort.csv")
    require(len({row["patient_id"] for row in analysis}) == 476, "Analysis cohort has one row per eligible person")
    longitudinal_by_patient = {row["patient_id"]: row for row in eligible}
    assignment_by_patient = {row["patient_id"]: row for row in assignments}
    for row in analysis:
        upstream = longitudinal_by_patient[row["patient_id"]]
        extension = assignment_by_patient[row["patient_id"]]
        require(all(row[field] == upstream[field] for field in ("scheduled_followup_flag", "later_acute_return_flag", "event_indicator", "observed_time_days")), f"Source outcomes are unchanged: {row['patient_id']}")
        require(row["teaching_site_id"] == extension["teaching_site_id"] and row["baseline_risk_tier"] == extension["baseline_risk_tier"], f"Extension merge matches: {row['patient_id']}")

    _, site_rows = read_csv(output_root / "site-support.csv")
    for row in site_rows:
        expected = SITE_SUPPORT[row["teaching_site_id"]]
        observed = tuple(int(row[field]) for field in ("people", "exposed", "later_events", "low_risk", "medium_risk", "high_risk"))
        require(observed == expected, f"Site support matches: {row['teaching_site_id']}")
        require(int(row["unexposed"]) > 0 and int(row["exposed"]) > 0 and int(row["later_events"]) >= 10, f"Site exposure and event support is present: {row['teaching_site_id']}")
        require(int(row["known_direct_site_effect"]) == 0, f"Known direct site effect is zero: {row['teaching_site_id']}")

    _, query_rows = read_csv(output_root / "query-checks.csv")
    require({row["check_name"]: int(row["observed_value"]) for row in query_rows} == REFERENCE_CHECKS, "All 26 SQL checks match")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    score = markdown_field(progression, "Phenotype and cohort score")
    score_match = re.fullmatch(r"(\d+(?:\.\d+)?) of 20\.00", score or "")
    require(score_match is not None and Decimal("16") <= Decimal(score_match.group(1)) <= Decimal("20"), "Score is between 16 and 20")
    require("no failed gate" in (markdown_field(progression, "Gate result") or "").lower(), "No progression gate failed")
    progression_value = markdown_field(progression, "Progression")
    require(progression_value in ALLOWED_PROGRESSION, "Progression value is allowed")
    permission = markdown_field(progression, "Module 03 permission")
    require((progression_value in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction"), "Module 03 permission matches progression")
    condition_rows = [line for line in progression.splitlines() if re.match(r"^\| C\d{2} \|", line)]
    require(len(condition_rows) >= 8 and all("| open |" in line or "| closed |" in line for line in condition_rows), "Progression has at least eight owned conditions")

    ai_text = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai_text, label) for label in ai_fields), "AI-use record has every accountable field")

    if database:
        with tempfile.TemporaryDirectory(prefix="app1-module02-reproduce-") as temp_dir:
            reproduced = Path(temp_dir) / "outputs"
            build_longitudinal.build(database.resolve(), reproduced, root / "sql")
            for name in OUTPUTS:
                require(sha256(reproduced / name) == sha256(output_root / name), f"Database reproduction matches: {name}")

    report = {"status": "pass", "mode": "complete", "checks_passed": len(checks), "assembled_files": 30}
    print(f"APP-1 Module 02 complete validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app1-module02-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, starter = base / "reference", base / "starter"
        build_workspace.assemble(reference, reference=True)
        complete_report = validate(reference)
        copied_validator = subprocess.run(
            [sys.executable, str(reference / "validate_longitudinal.py"), str(reference)],
            capture_output=True, text=True, check=False,
        )
        assert copied_validator.returncode == 0 and "1140 checks" in copied_validator.stdout, copied_validator.stderr
        build_workspace.assemble(starter)
        starter_report = validate(starter, starter=True)
        try:
            validate(starter)
        except ValidationError as error:
            assert "Workspace has exactly 30 expected files" in str(error), str(error)
        else:
            raise AssertionError("Validator accepted incomplete starter")

        broken_output = base / "broken-output"
        shutil.copytree(reference, broken_output)
        path = broken_output / "outputs/analysis-cohort.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("SITE-B", "SITE-Z", 1), encoding="utf-8", newline="\n")
        bad_score = base / "bad-score"
        shutil.copytree(reference, bad_score)
        path = bad_score / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("20.00 of 20.00", "21.00 of 20.00"), encoding="utf-8", newline="\n")
        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        path = bad_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Progression: `continue with conditions`", "Progression: `deploy`"), encoding="utf-8", newline="\n")
        for workspace, expected in ((broken_output, "Output SHA-256 matches"), (bad_score, "Score is between 16 and 20"), (bad_progression, "Progression value is allowed")):
            try:
                validate(workspace)
            except ValidationError as error:
                assert expected in str(error), str(error)
            else:
                raise AssertionError(f"Validator accepted invalid workspace: {workspace.name}")
    print(f"APP-1 Module 02 validator self-check passed: {complete_report['checks_passed']} complete checks and {starter_report['checks_passed']} starter checks; incomplete and broken workspaces rejected.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--database", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--submission", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.workspace:
            parser.error("workspace is required unless --self-check is used")
        validate(args.workspace, starter=args.starter, database=args.database)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
