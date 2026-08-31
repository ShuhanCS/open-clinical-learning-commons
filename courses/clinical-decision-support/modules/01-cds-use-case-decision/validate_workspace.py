"""Validate APP-4 Module 01 learner and reference workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path

from build_workspace import IMMUTABLE_FILES, RECORD_FILES, assemble


PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}
CSV_CONTRACTS = {
    "user-workflow-action-map.csv": (["step_id", "workflow_state", "required_information", "primary_actor", "permitted_system_behavior", "human_action_or_nonaction", "failure_or_burden_question", "owner"], 8),
    "intended-use-boundary.csv": (["boundary_id", "element", "status", "module01_decision", "later_owner", "reason"], 12),
    "public-synthetic-data-role-map.csv": (["role_id", "evidence_question", "public_nhanes_role", "synthetic_cgh_gim_01_role", "status", "claim_limit"], 12),
    "input-availability-inventory.csv": (["input_id", "candidate_concept", "public_field_route", "synthetic_route", "decision_time_requirement", "module01_status", "later_owner", "claim_limit"], 8),
    "stakeholder-accountability-map.csv": (["stakeholder_id", "role", "decision_right", "module01_evidence_owned", "can_require_revision", "can_stop", "open_condition"], 13),
    "claim-boundary.csv": (["claim_id", "claim", "status", "evidence_required", "owner"], 14),
}


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
    match = re.search(rf"(?m)^- {re.escape(label)}: `([^`]+)`\.$", text)
    return match.group(1) if match else None


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    root = root.resolve()
    require(root.is_dir(), f"Workspace does not exist: {root}")
    expected = set(IMMUTABLE_FILES) | set(RECORD_FILES) | {"release-manifest.csv"}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    require(actual == set(path.replace("\\", "/") for path in expected), "Workspace file set does not match the 41-file contract")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Manifest header mismatch")
    require(len(manifest) == 29, "Manifest must contain 29 immutable rows")
    require([row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Manifest is not sorted")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Missing immutable file: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Immutable byte count changed: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Immutable hash changed: {row['relative_path']}")

    contract = json.loads((root / "decision-contract.json").read_text(encoding="utf-8"))
    require(contract["module"]["id"] == "oclc-app4-01", "Module ID mismatch")
    require(contract["module"]["version"] == "0.1.0", "Module version mismatch")
    require(contract["module"]["commons_release"] == "0.77.0", "Commons release mismatch")
    require(contract["module"]["hours"] == 15.5, "Module hours mismatch")
    require(contract["assessment"]["course_points_awarded_here"] == 0, "Module 01 cannot award course points")
    require(contract["assessment"]["noncompensable_gates"] == 12, "Gate count mismatch")
    require(contract["package"] == {"immutable_manifest_rows": 29, "editable_records": 11, "assembled_files": 41}, "Package contract mismatch")
    require(all(value == "prohibited" for value in contract["authority"].values()), "Every live-use authority must remain prohibited")

    inventory_header, inventory = read_csv(root / "data/source-inventory.csv")
    fields_header, fields = read_csv(root / "data/field-inventory.csv")
    joins_header, joins = read_csv(root / "data/cycle-join-profile.csv")
    standards_header, standards = read_csv(root / "data/standards-inventory.csv")
    require(len(inventory) == 16 and len(fields) == 442 and len(joins) == 4 and len(standards) == 5, "Source profile row counts mismatch")
    require(sum(int(row["raw_bytes"]) for row in inventory) == 34221200, "Raw source byte total mismatch")
    require(sum(int(row["gzip_bytes"]) for row in inventory) == 3149043, "Gzip source byte total mismatch")
    require(sum(int(row["rows"]) for row in inventory) == 145563, "Source row total mismatch")
    require(sum(int(row["seqn_duplicates"]) for row in inventory) == 0, "A source contains duplicate SEQN values")
    require({row["cycle"] for row in inventory} == {"2013-2014", "2015-2016", "2017-2018", "2021-2023"}, "Cycle set mismatch")
    require({row["component"] for row in inventory} == {"DEMO", "BMX", "DIQ", "GHB"}, "Component set mismatch")
    require(all(row["seqn_unique"] == row["rows"] for row in inventory), "SEQN is not unique in every source")
    require([int(row["all_four_joined"]) for row in joins] == [6979, 6744, 6401, 7199], "Cycle join counts mismatch")
    require(all(row["survey_design_present"] == "true" for row in joins), "Survey design fields are incomplete")
    require(inventory_header[0:4] == ["source_id", "cycle", "component", "suffix"], "Source inventory header mismatch")
    require(fields_header[0:5] == ["source_id", "cycle", "component", "field_order", "field_name"], "Field inventory header mismatch")
    require(joins_header[0:5] == ["cycle", "demo_rows", "bmx_rows", "diq_rows", "ghb_rows"], "Join profile header mismatch")
    require(standards_header == ["source_id", "title", "version", "url", "teaching_role", "claim_limit"], "Standards inventory header mismatch")
    require(sha256(root / "data/source-inventory.csv") == contract["public_release"]["source_inventory_sha256"], "Source inventory identity mismatch")
    require(sha256(root / "data/field-inventory.csv") == contract["public_release"]["field_inventory_sha256"], "Field inventory identity mismatch")
    require(sha256(root / "data/cycle-join-profile.csv") == contract["public_release"]["cycle_join_profile_sha256"], "Cycle join profile identity mismatch")
    require(sha256(root / "data/standards-inventory.csv") == contract["public_release"]["standards_inventory_sha256"], "Standards inventory identity mismatch")

    for filename, (header, count) in CSV_CONTRACTS.items():
        actual_header, rows = read_csv(root / filename)
        require(actual_header == header, f"{filename} header mismatch")
        require(len(rows) == count, f"{filename} must contain {count} rows")

    record_text = "\n".join((root / relative).read_text(encoding="utf-8") for relative in RECORD_FILES)
    require(not PERSONAL_PATH.search(record_text), "Submission contains a personal local path")
    if starter:
        require(PLACEHOLDER.search(record_text) is not None, "Starter submission must retain assessed placeholders")
        return {"status": "pass", "mode": "starter", "checks": 121, "manifest_rows": 29, "source_files": 16, "gates": 12}

    require(PLACEHOLDER.search(record_text) is None, "Complete submission contains a placeholder")
    charter = (root / "cds-use-case-charter.md").read_text(encoding="utf-8")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    source_interpretation = (root / "source-feasibility-interpretation.md").read_text(encoding="utf-8")
    synthetic_contract = (root / "synthetic-generation-contract.md").read_text(encoding="utf-8")
    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    require("CGH-GIM-01" in charter and "explicitly fictional" in charter, "Fictional service boundary is missing")
    require("clinician responsible for the current adult encounter" in charter, "Primary user is missing")
    require("confirmatory HbA1c testing" in charter, "Intended support is missing")
    require("diagnosis, automatic order" in charter, "Prohibited action is incomplete")
    require("No model or threshold is accepted" in charter, "Early model and threshold boundary is missing")
    require("34,221,200 raw bytes" in source_interpretation and "145,563 component rows" in source_interpretation, "Source interpretation scale is wrong")
    require("cannot establish local `CGH-GIM-01`" in source_interpretation, "Local-validation limit is missing")
    require("Module 01 generated clinical rows: `0`" in synthetic_contract, "Module 01 generated rows must be zero")
    require("Public NHANES participants, identifiers, rows, or values cannot be copied" in synthetic_contract, "Public-to-synthetic separation is missing")
    require(markdown_field(progression, "Decision") in ALLOWED_PROGRESSION, "Progression decision is invalid")
    require(markdown_field(progression, "Decision") == "continue with conditions", "Reference progression decision mismatch")
    for label in ("Model fitting", "Final target selection", "Predictor acceptance", "Threshold selection", "Alert firing", "Real-patient scoring", "Clinical action", "Implementation", "Deployment"):
        require(markdown_field(progression, label) == "prohibited", f"{label} must remain prohibited")
    require(markdown_field(progression, "Module 02 curriculum construction") == "permitted", "Module 02 permission mismatch")
    require("Protected or identifiable data shared: `none`" in ai_use, "Protected-data disclosure mismatch")
    require("Agent authority: `none" in ai_use, "Agent authority boundary is missing")
    return {"status": "pass", "mode": "complete", "checks": 177, "manifest_rows": 29, "source_files": 16, "gates": 12}


def expect_failure(path: Path, starter: bool = False) -> None:
    try:
        validate(path, starter=starter)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError):
        return
    raise AssertionError(f"Validator accepted a broken workspace: {path}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app4-module01-validate-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        assemble(reference, reference=True)
        assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)

        missing = base / "missing"
        shutil.copytree(reference, missing)
        (missing / "claim-boundary.csv").unlink()
        expect_failure(missing)

        source_mutation = base / "source-mutation"
        shutil.copytree(reference, source_mutation)
        raw = source_mutation / "data/raw/DEMO_H.xpt.gz"
        changed = bytearray(raw.read_bytes())
        changed[-1] ^= 1
        raw.write_bytes(changed)
        expect_failure(source_mutation)

        placeholder = base / "placeholder"
        shutil.copytree(reference, placeholder)
        with (placeholder / "cds-use-case-charter.md").open("a", encoding="utf-8") as handle:
            handle.write("\nREPLACE\n")
        expect_failure(placeholder)

        authority = base / "authority"
        shutil.copytree(reference, authority)
        path = authority / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("- Deployment: `prohibited`.", "- Deployment: `permitted`."), encoding="utf-8")
        expect_failure(authority)

        copied = base / "copied"
        shutil.copytree(starter, copied)
        for relative in RECORD_FILES:
            shutil.copy2(reference / relative, copied / relative)
        expect_failure(copied, starter=True)

        personal = base / "personal"
        shutil.copytree(reference, personal)
        with (personal / "ai-use.md").open("a", encoding="utf-8") as handle:
            handle.write("\nC:\\Users\\Example\\private.csv\n")
        expect_failure(personal)

    print(f"APP-4 Module 01 complete validation passed: {complete_report['checks']} checks.")
    print(f"APP-4 Module 01 starter validation passed: {starter_report['checks']} checks.")
    print("APP-4 Module 01 validator self-check passed: missing, source, placeholder, authority, copied-answer, and personal-path routes rejected.")


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
            parser.error("workspace is required")
        print(json.dumps(validate(args.workspace, starter=args.starter), indent=2))
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
