"""Validate APP-5 Module 01 learner and reference workspaces."""

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
    "population-denominator-contract.csv": (["contract_id", "measure_or_role", "numerator", "denominator", "population", "source", "period", "geography", "module01_status", "later_owner", "claim_limit"], 10),
    "geography-time-contract.csv": (["contract_id", "element", "accepted_value", "status", "source_or_owner", "later_use", "limit"], 8),
    "public-data-role-map.csv": (["role_id", "source_or_layer", "accepted_role", "module01_evidence", "later_use", "not_supported", "status", "owner"], 9),
    "equity-language-contract.csv": (["language_id", "term_or_phrase", "definition_or_problem", "permitted_use", "required_evidence", "prohibited_shortcut", "owner"], 9),
    "community-accountability-map.csv": (["stakeholder_id", "role", "decision_right", "module01_evidence_owned", "can_require_revision", "can_stop", "open_condition"], 12),
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
    require(actual == {path.replace("\\", "/") for path in expected}, "Workspace file set does not match the 27-file contract")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Manifest header mismatch")
    require(len(manifest) == 16, "Manifest must contain 16 immutable rows")
    require([row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Manifest is not sorted")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Missing immutable file: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Immutable byte count changed: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Immutable hash changed: {row['relative_path']}")

    contract = json.loads((root / "decision-contract.json").read_text(encoding="utf-8"))
    require(contract["module"]["id"] == "oclc-app5-01", "Module ID mismatch")
    require(contract["module"]["version"] == "0.1.0", "Module version mismatch")
    require(contract["module"]["commons_release"] == "0.87.0", "Commons release mismatch")
    require(contract["module"]["hours"] == 15.5, "Module hours mismatch")
    require(contract["assessment"]["course_points_awarded_here"] == 0, "Module 01 cannot award course points")
    require(contract["assessment"]["noncompensable_gates"] == 12, "Gate count mismatch")
    require(contract["package"] == {"immutable_manifest_rows": 16, "editable_records": 10, "assembled_files": 27}, "Package contract mismatch")
    require(all(value == "prohibited" for value in contract["authority"].values()), "Every early or real-world authority must remain prohibited")

    places_header, places = read_csv(root / "data/places-diabetes-ma-tract-2025.csv")
    acs_header, acs = read_csv(root / "data/acs-b01001-ma-tract-2024.csv")
    svi_header, svi = read_csv(root / "data/svi2022-ma-tract.csv")
    source_header, sources = read_csv(root / "data/source-inventory.csv")
    field_header, fields = read_csv(root / "data/field-inventory.csv")
    join_header, joins = read_csv(root / "data/join-feasibility.csv")
    reading_header, readings = read_csv(root / "data/reading-inventory.csv")

    require(len(places_header) == 24 and len(places) == 1597, "PLACES release shape mismatch")
    require(len(acs_header) == 100 and len(acs) == 1620, "ACS release shape mismatch")
    require(len(svi_header) == 158 and len(svi) == 1613, "SVI release shape mismatch")
    require(len(sources) == 3 and len(fields) == 282 and len(joins) == 3 and len(readings) == 9, "Source profile row counts mismatch")
    require(source_header[0:6] == ["source_id", "publisher", "title", "release", "upstream_url", "retrieved"], "Source inventory header mismatch")
    require(field_header == ["source_id", "field_order", "field_name", "source_or_derived", "rows", "nonmissing", "missing", "distinct_nonmissing", "negative_sentinel_like", "teaching_role"], "Field inventory header mismatch")
    require(join_header == ["comparison", "left_source", "left_tracts", "right_source", "right_tracts", "intersection", "left_only", "right_only", "interpretation"], "Join profile header mismatch")
    require(reading_header == ["source_id", "title", "version_or_release", "url", "teaching_role", "claim_limit"], "Reading inventory header mismatch")

    places_ids = [row["locationid"] for row in places]
    acs_ids = [row["tract_fips"] for row in acs]
    svi_ids = [row["FIPS"] for row in svi]
    require(len(places_ids) == len(set(places_ids)), "PLACES contains duplicate tracts")
    require(len(acs_ids) == len(set(acs_ids)), "ACS contains duplicate tracts")
    require(len(svi_ids) == len(set(svi_ids)), "SVI contains duplicate tracts")
    require(all(len(value) == 11 and value.startswith("25") for value in places_ids + acs_ids + svi_ids), "A tract FIPS is invalid")
    require(all(row["stateabbr"] == "MA" and row["measureid"] == "DIABETES" and row["year"] == "2023" and row["datavaluetypeid"] == "CrdPrv" for row in places), "PLACES filter contract changed")
    require(all(row["ST"] == "25" and row["ST_ABBR"] == "MA" for row in svi), "SVI state filter changed")
    require(len(set(places_ids) & set(acs_ids) & set(svi_ids)) == 1597, "Three-source tract intersection changed")
    require(len(set(places_ids) | set(acs_ids) | set(svi_ids)) == 1620, "Three-source tract union changed")
    require([(int(row["intersection"]), int(row["left_only"]), int(row["right_only"])) for row in joins] == [(1597, 0, 16), (1597, 0, 23), (1613, 0, 7)], "Join feasibility facts changed")
    require(all(row["data_value"] and row["low_confidence_limit"] and row["high_confidence_limit"] and row["totalpop18plus"] for row in places), "PLACES value, interval, or adult population is missing")

    public = contract["public_release"]
    require(sha256(root / "data/places-diabetes-ma-tract-2025.csv") == public["places_sha256"], "PLACES identity mismatch")
    require(sha256(root / "data/acs-b01001-ma-tract-2024.csv") == public["acs_sha256"], "ACS identity mismatch")
    require(sha256(root / "data/svi2022-ma-tract.csv") == public["svi_sha256"], "SVI identity mismatch")
    require(sha256(root / "data/source-inventory.csv") == public["source_inventory_sha256"], "Source inventory identity mismatch")
    require(sha256(root / "data/field-inventory.csv") == public["field_inventory_sha256"], "Field inventory identity mismatch")
    require(sha256(root / "data/join-feasibility.csv") == public["join_feasibility_sha256"], "Join feasibility identity mismatch")
    require(sha256(root / "data/reading-inventory.csv") == public["reading_inventory_sha256"], "Reading inventory identity mismatch")

    csv_records: dict[str, list[dict[str, str]]] = {}
    for filename, (header, count) in CSV_CONTRACTS.items():
        actual_header, rows = read_csv(root / filename)
        require(actual_header == header, f"{filename} header mismatch")
        require(len(rows) == count, f"{filename} must contain {count} rows")
        csv_records[filename] = rows

    record_text = "\n".join((root / relative).read_text(encoding="utf-8") for relative in RECORD_FILES)
    require(not PERSONAL_PATH.search(record_text), "Submission contains a personal local path")
    if starter:
        require(PLACEHOLDER.search(record_text) is not None, "Starter submission must retain assessed placeholders")
        return {"status": "pass", "mode": "starter", "checks": 112, "manifest_rows": 16, "source_files": 3, "gates": 12}

    require(PLACEHOLDER.search(record_text) is None, "Complete submission contains a placeholder")
    charter = (root / "population-decision-charter.md").read_text(encoding="utf-8")
    source_interpretation = (root / "source-feasibility-interpretation.md").read_text(encoding="utf-8")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    require("FMA-DP-01" in charter and "explicitly fictional" in charter, "Fictional case boundary is missing")
    require("adults age 18 and older" in charter and "Massachusetts census tract" in charter, "Population or geography is missing")
    require("PLACES adult population travels with the modeled PLACES estimate" in charter, "PLACES denominator role is missing")
    require("question the framing, add local knowledge, contest interpretations and burdens, require revision, and stop" in charter, "Community decision rights are incomplete")
    require("no rate, disparity, map, tract rank, target, allocation, model, intervention effect" in charter, "Early-analysis boundary is incomplete")
    require("200,356,282 raw bytes" in source_interpretation and "616,690 rows" in source_interpretation, "Complete ACS source identity is missing")
    require("three-source intersection is 1,597 tracts" in source_interpretation, "Three-source intersection interpretation is missing")
    require("does not supply observed diagnoses" in source_interpretation, "Observed-case limit is missing")
    require("not sufficient to identify a tract for funding or outreach" in source_interpretation, "Targeting boundary is missing")

    require(markdown_field(progression, "Decision") in ALLOWED_PROGRESSION, "Progression decision is invalid")
    require(markdown_field(progression, "Decision") == "continue with conditions", "Reference progression decision mismatch")
    for label in (
        "Rate calculation in Module 01", "Standardization in Module 01", "Disparity claim in Module 01",
        "Mapping in Module 01", "Tract ranking", "Targeting or allocation", "Model fitting",
        "Intervention-effect estimation", "Real community action", "Implementation", "Deployment",
    ):
        require(markdown_field(progression, label) == "prohibited", f"{label} must remain prohibited")
    require(markdown_field(progression, "Module 02 curriculum construction") == "permitted", "Module 02 permission mismatch")
    require("Protected or identifiable data shared: `none`" in ai_use, "Protected-data disclosure mismatch")
    require("Agent authority: `none over the population, denominator, equity language, community role, progression, targeting, allocation, intervention, or final decision`" in ai_use, "Agent authority boundary is missing")

    denominators = {row["contract_id"]: row for row in csv_records["population-denominator-contract.csv"]}
    require(denominators["PD-07"]["module01_status"] == "accepted as context only", "SVI denominator boundary changed")
    require(denominators["PD-09"]["numerator"] == "prohibited" and denominators["PD-09"]["denominator"] == "prohibited", "Individual denominator must remain prohibited")
    community = {row["stakeholder_id"]: row for row in csv_records["community-accountability-map.csv"]}
    require(community["CA-01"]["can_require_revision"] == "yes" and community["CA-01"]["can_stop"] == "yes for progression to real community action", "Resident rights are incomplete")
    require(community["CA-02"]["can_require_revision"] == "yes" and community["CA-02"]["can_stop"] == "yes for progression to real community action", "Community-organization rights are incomplete")
    claims = {row["claim_id"]: row for row in csv_records["claim-boundary.csv"]}
    for claim_id in ("CB-03", "CB-05", "CB-06", "CB-08", "CB-09", "CB-10", "CB-11", "CB-12", "CB-13"):
        require(claims[claim_id]["status"] == "prohibited", f"{claim_id} must remain prohibited")
    equity = {row["language_id"]: row for row in csv_records["equity-language-contract.csv"]}
    require("unfair or unjust" in equity["EL-03"]["definition_or_problem"], "Inequity definition is incomplete")
    require("individual" in equity["EL-08"]["prohibited_shortcut"], "Ecological language boundary is incomplete")
    return {"status": "pass", "mode": "complete", "checks": 176, "manifest_rows": 16, "source_files": 3, "gates": 12}


def expect_failure(path: Path, starter: bool = False) -> None:
    try:
        validate(path, starter=starter)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError):
        return
    raise AssertionError(f"Validator accepted a broken workspace: {path}")


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module01-validate-") as temp_dir:
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
        source = source_mutation / "data/places-diabetes-ma-tract-2025.csv"
        changed = bytearray(source.read_bytes())
        changed[-2] ^= 1
        source.write_bytes(changed)
        expect_failure(source_mutation)

        placeholder = base / "placeholder"
        shutil.copytree(reference, placeholder)
        with (placeholder / "population-decision-charter.md").open("a", encoding="utf-8") as handle:
            handle.write("\nREPLACE\n")
        expect_failure(placeholder)

        authority = base / "authority"
        shutil.copytree(reference, authority)
        path = authority / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("- Targeting or allocation: `prohibited`.", "- Targeting or allocation: `permitted`."), encoding="utf-8")
        expect_failure(authority)

        community = base / "community"
        shutil.copytree(reference, community)
        path = community / "community-accountability-map.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("yes for progression to real community action", "no", 1), encoding="utf-8")
        expect_failure(community)

        claim = base / "observed-claim"
        shutil.copytree(reference, claim)
        path = claim / "source-feasibility-interpretation.md"
        path.write_text(path.read_text(encoding="utf-8").replace("does not supply observed diagnoses", "supplies observed diagnoses"), encoding="utf-8")
        expect_failure(claim)

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

    print(f"APP-5 Module 01 complete validation passed: {complete_report['checks']} checks.")
    print(f"APP-5 Module 01 starter validation passed: {starter_report['checks']} checks.")
    print("APP-5 Module 01 validator self-check passed: missing, source, placeholder, authority, community-right, observed-claim, copied-answer, and personal-path routes rejected.")


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
