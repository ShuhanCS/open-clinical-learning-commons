"""Validate the FND-1 cumulative Week 6 checkpoint."""

from __future__ import annotations

import argparse
import csv
import json
import re
import struct
import tempfile
import xml.etree.ElementTree as ET
from decimal import Decimal
from pathlib import Path

import assemble_checkpoint


PACKAGE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\[REPLACE:[^\]\r\n]*\]|\b(?:TODO|TBD|REPLACE(?:_ME)?)\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
CONTRACT_FIELDS = ["artifact_id", "source_module", "source_path", "target_path", "row_count", "byte_count", "sha256", "role"]
MANIFEST_FIELDS = CONTRACT_FIELDS + ["assembled_byte_count", "assembled_sha256", "status"]
SUMMARY_FIELDS = ["source_module", "module_id", "version", "role", "accepted_decision", "artifact_count", "progression_condition"]
SCORE_FIELDS = ["criterion_id", "criterion", "course_points", "score", "evidence", "status"]
TEXT_RECORDS = (
    "README.md", "component-score.csv", "quality-decision.md", "interpretation-memo.md",
    "accessibility-synthesis.md", "source-record.yml", "transformation-record.md",
    "reproducibility-check.md", "ai-use.md", "review-disposition.md",
)
BASE_FILES = (".gitattributes", *TEXT_RECORDS, "VERSION", "artifact-contract.csv", "release-manifest.csv", "checkpoint-summary.csv")
ISSUES = [f"D{value:02d}" for value in range(1, 21)] + [f"N{value:02d}" for value in range(1, 9)]


class ValidationError(RuntimeError):
    pass


def require(condition: bool, label: str, checks: list[str]) -> None:
    if not condition:
        raise ValidationError(label)
    checks.append(label)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def csv_rows(root: Path, relative: str, expected: int, checks: list[str]) -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = read_csv(root / relative)
    require(len(rows) == expected, f"Expected row count {expected}: {relative}", checks)
    return fields, rows


def check_png(path: Path, checks: list[str]) -> None:
    data = path.read_bytes()
    require(data[:8] == b"\x89PNG\r\n\x1a\n", f"PNG signature: {path.name}", checks)
    position, width, height, pixels_per_meter, unit = 8, None, None, None, None
    while position + 12 <= len(data):
        length = struct.unpack(">I", data[position:position + 4])[0]
        kind = data[position + 4:position + 8]
        payload = data[position + 8:position + 8 + length]
        if kind == b"IHDR":
            width, height = struct.unpack(">II", payload[:8])
        elif kind == b"pHYs":
            horizontal, vertical, unit = struct.unpack(">IIB", payload)
            require(horizontal == vertical, f"PNG square pixels: {path.name}", checks)
            pixels_per_meter = horizontal
        if kind == b"IEND":
            break
        position += length + 12
    require((width, height) == (2100, 1200), f"PNG is 2100 by 1200: {path.name}", checks)
    require(unit == 1 and pixels_per_meter is not None and 299.5 <= pixels_per_meter * 0.0254 <= 300.5, f"PNG is 300 DPI: {path.name}", checks)


def check_svg(path: Path, checks: list[str]) -> None:
    root = ET.parse(path).getroot()
    require(root.tag.endswith("svg"), f"SVG root: {path.name}", checks)
    require(root.attrib.get("width") == "504pt" and root.attrib.get("height") == "288pt", f"SVG physical size: {path.name}", checks)
    require(root.attrib.get("viewBox") == "0 0 504 288", f"SVG viewBox: {path.name}", checks)


def check_notebook(path: Path, checks: list[str]) -> None:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    require(notebook.get("nbformat") == 4, f"Notebook format 4: {path.name}", checks)
    outputs = [output for cell in notebook.get("cells", []) for output in cell.get("outputs", [])]
    require(not any(output.get("output_type") == "error" for output in outputs), f"Notebook has no error output: {path.name}", checks)


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    checks: list[str] = []
    require(root.is_dir(), "Checkpoint directory exists", checks)
    contract = assemble_checkpoint.read_contract()
    required = BASE_FILES + tuple(row["target_path"] for row in contract)
    require(len(required) == 50 and len(set(required)) == 50, "Package contract contains 50 unique files", checks)
    for relative in required:
        require((root / relative).is_file(), f"Required file exists: {relative}", checks)
    require(not any(root.rglob("*.jpg")) and not any(root.rglob("*.jpeg")), "No JPEG substitutes", checks)
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version is 0.1.0", checks)

    for relative in TEXT_RECORDS:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII punctuation: {relative}", checks)
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}", checks)
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}", checks)

    package_contract = root / "artifact-contract.csv"
    require(package_contract.read_bytes() == (PACKAGE_ROOT / "artifact-contract.csv").read_bytes(), "Artifact contract matches the released contract", checks)
    contract_fields, package_rows = read_csv(package_contract)
    require(contract_fields == CONTRACT_FIELDS and package_rows == contract, "Artifact contract schema and rows match", checks)

    manifest_fields, manifest = csv_rows(root, "release-manifest.csv", 35, checks)
    require(manifest_fields == MANIFEST_FIELDS, "Release manifest header matches", checks)
    require([row["artifact_id"] for row in manifest] == [row["artifact_id"] for row in contract], "Manifest artifact order matches contract", checks)
    for expected, row in zip(contract, manifest, strict=True):
        require(all(row[field] == expected[field] for field in CONTRACT_FIELDS), f"Manifest contract fields match: {row['artifact_id']}", checks)
        relative = row["target_path"]
        path = root / relative
        require(row["status"] == "verified", f"Manifest status verified: {relative}", checks)
        require(int(row["assembled_byte_count"]) == path.stat().st_size == int(row["byte_count"]), f"Manifest bytes match: {relative}", checks)
        require(row["assembled_sha256"] == assemble_checkpoint.sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {relative}", checks)
        if row["row_count"]:
            _, rows = read_csv(path)
            require(len(rows) == int(row["row_count"]), f"Manifest row count matches: {relative}", checks)

    summary_fields, summary = csv_rows(root, "checkpoint-summary.csv", 3, checks)
    require(summary_fields == SUMMARY_FIELDS, "Checkpoint summary header matches", checks)
    require([row["source_module"] for row in summary] == ["M04", "M05", "M06"], "Checkpoint summary module order matches", checks)
    require([int(row["artifact_count"]) for row in summary] == [11, 9, 15], "Checkpoint summary artifact counts match", checks)
    require([row["accepted_decision"] for row in summary] == ["proceed with conditions", "accept with conditions", "accept with conditions"], "Checkpoint summary decisions match", checks)

    analytic_fields, analytic = csv_rows(root, "data/analytic-table.csv", 374, checks)
    require(len(analytic_fields) == 29, "Analytic table has 29 fields", checks)
    require(len({row["patient_id"] for row in analytic}) == 374, "Analytic table has one row per patient", checks)
    require(len({row["index_encounter_id"] for row in analytic}) == 374, "Analytic table has one unique index encounter per row", checks)
    require(assemble_checkpoint.sha256(root / "data/analytic-table.csv") == "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a", "Accepted analytic fingerprint matches", checks)

    dictionary_fields, dictionary = csv_rows(root, "data/data-dictionary.csv", 29, checks)
    require(dictionary_fields == ["position", "field_name", "timing", "data_type", "nullable", "allowed_values_or_rule", "description"], "Data dictionary header matches", checks)
    require([int(row["position"]) for row in dictionary] == list(range(1, 30)), "Data dictionary positions are complete", checks)
    require([row["field_name"] for row in dictionary] == analytic_fields, "Data dictionary field order matches analytic table", checks)

    _, defects = csv_rows(root, "quality/defect-manifest.csv", 68, checks)
    require(set(row["issue_id"] for row in defects) == set(ISSUES[:20]), "Defect manifest covers D01 through D20", checks)
    _, quality = csv_rows(root, "quality/quality-profile.csv", 29, checks)
    _, missingness = csv_rows(root, "quality/missingness-profile.csv", 29, checks)
    require([row["field_name"] for row in quality] == analytic_fields == [row["field_name"] for row in missingness], "Quality profiles follow analytic field order", checks)

    _, rules = csv_rows(root, "quality/quality-rule-results.csv", 28, checks)
    require([row["issue_id"] for row in rules] == ISSUES, "Quality rules cover D01-D20 and N01-N08", checks)
    require(all(row["detection_status"] == "pass" for row in rules), "Every quality detection passes", checks)
    _, risks = csv_rows(root, "quality/quality-risk-log.csv", 28, checks)
    require([row["issue_id"] for row in risks] == ISSUES, "Risk log covers D01-D20 and N01-N08", checks)
    _, resolutions = csv_rows(root, "quality/resolution-log.csv", 28, checks)
    require([row["issue_id"] for row in resolutions] == ISSUES, "Resolution log covers D01-D20 and N01-N08", checks)
    require(all(row["status"] == "resolved" for row in resolutions[:20]), "D01 through D20 are resolved", checks)
    require(all(row["status"] == "retained condition" for row in resolutions[20:]), "N01 through N08 remain conditions", checks)
    if not starter:
        quality_decision = (root / "quality-decision.md").read_text(encoding="utf-8").lower()
        require(
            "proceed with conditions" in quality_decision
            and "d01 through d20" in quality_decision
            and all(issue.lower() in quality_decision for issue in ISSUES[20:]),
            "Quality decision preserves all issues and progression condition",
            checks,
        )

    _, profiles = csv_rows(root, "evidence-tables/variable-profile.csv", 17, checks)
    require(all(int(row["available_n"]) + int(row["missing_n"]) == 374 for row in profiles), "Variable-profile availability reconciles", checks)
    _, cross_tabs = csv_rows(root, "evidence-tables/cross-tabs.csv", 12, checks)
    for result_id in ("CT01", "CT02"):
        rows = [row for row in cross_tabs if row["result_id"] == result_id]
        require(sum(int(row["n"]) for row in rows) == 374, f"Cross-tab {result_id} conserves the cohort", checks)
        require(all(abs(float(row["row_percent"]) - 100 * int(row["n"]) / int(row["row_denominator"])) < 0.000001 for row in rows), f"Cross-tab {result_id} row percentages reconcile", checks)

    _, rates = csv_rows(root, "evidence-tables/rates.csv", 6, checks)
    require([row["result_id"] for row in rates] == [f"RT{value:02d}" for value in range(1, 7)], "Rates are RT01 through RT06", checks)
    require([int(row["numerator"]) for row in rates] == [111, 92, 4, 15, 36, 8], "Rate numerators match", checks)
    require(all(int(row["denominator"]) == 374 for row in rates), "Rate denominators match 374", checks)
    require(all(float(row["wilson_95_lower_percent"]) <= float(row["percent"]) <= float(row["wilson_95_upper_percent"]) for row in rates), "Rate estimates fall within Wilson intervals", checks)
    _, strata = csv_rows(root, "evidence-tables/stratified-table.csv", 2, checks)
    require(sum(int(row["n"]) for row in strata) == 374, "Strata conserve the cohort", checks)
    _, denominators = csv_rows(root, "evidence-tables/denominator-registry.csv", 27, checks)
    denominator_text = " ".join(value for row in denominators for value in row.values())
    require(all(issue in denominator_text for issue in ISSUES[20:]), "Denominator registry links N01 through N08", checks)
    _, descriptive_checks = csv_rows(root, "evidence-tables/descriptive-checks.csv", 18, checks)
    require(all(row["status"] == "pass" for row in descriptive_checks), "All descriptive invariants pass", checks)

    _, visual_missingness = csv_rows(root, "tables/quality-missingness.csv", 8, checks)
    _, visual_rates = csv_rows(root, "tables/descriptive-rates.csv", 6, checks)
    require(visual_rates == rates, "F02 exact table matches the accepted rates", checks)
    _, quarterly = csv_rows(root, "tables/quarterly-index-counts.csv", 20, checks)
    require(sum(int(row["total_index_n"]) for row in quarterly) == 374, "F03 totals sum to 374", checks)
    require(sum(int(row["emergency_index_n"]) for row in quarterly) == 314, "F03 emergency total is 314", checks)
    require(sum(int(row["inpatient_index_n"]) for row in quarterly) == 60, "F03 inpatient total is 60", checks)
    require(all(int(row["accepted_denominator"]) == 374 and int(row["defective_denominator"]) == 379 for row in visual_missingness), "F01 layer denominators match", checks)

    registry_fields, registry = csv_rows(root, "figure-registry.csv", 3, checks)
    require(len(registry_fields) == 25 and [row["figure_id"] for row in registry] == ["F01", "F02", "F03"], "Figure registry has 25 fields and F01-F03", checks)
    for row in registry:
        for path_field, hash_field in (("table_path", "table_sha256"), ("png_path", "png_sha256"), ("svg_path", "svg_sha256"), ("alt_text_path", "alt_text_sha256")):
            relative = row[path_field]
            path = root / relative
            require(path.is_file(), f"Figure registry path exists: {relative}", checks)
            require(assemble_checkpoint.sha256(path) == row[hash_field], f"Figure registry fingerprint matches: {relative}", checks)
        require(row["width_pixels"] == "2100" and row["height_pixels"] == "1200" and row["dpi"] == "300.00", f"Figure registry output size matches: {row['figure_id']}", checks)
        require(row["redundant_cue"] and row["claim_limit"], f"Figure registry access and claim limits exist: {row['figure_id']}", checks)
        check_png(root / row["png_path"], checks)
        check_svg(root / row["svg_path"], checks)

    alternatives = "\n".join((root / row["alt_text_path"]).read_text(encoding="utf-8") for row in registry).lower()
    for phrase in ("purpose:", "structure:", "main values:", "finding and limit:", "343 of 374", "111 of 374", "314", "60"):
        require(phrase in alternatives, f"Structured alternatives include: {phrase}", checks)
    if not starter:
        access = (root / "accessibility-synthesis.md").read_text(encoding="utf-8").lower()
        for phrase in ("grayscale", "50-percent-width", "200-percent-zoom", "reading-order", "structured-alternative"):
            require(phrase in access, f"Accessibility synthesis includes: {phrase}", checks)

    for relative in ("notebooks/data-quality.ipynb", "notebooks/descriptive-results.ipynb"):
        check_notebook(root / relative, checks)
    if not starter:
        source_record = (root / "source-record.yml").read_text(encoding="utf-8").lower()
        require("synthetic: true" in source_record and "contains_real_patients: false" in source_record and "rights_boundary:" in source_record, "Source record preserves synthetic and rights boundaries", checks)
        transformation = (root / "transformation-record.md").read_text(encoding="utf-8").lower()
        require("does not clean, impute, calculate, round, redraw, recode, suppress, or edit" in transformation, "Transformation record prohibits checkpoint mutation", checks)
        reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
        require("module 04 validation: pass" in reproducibility and "module 05 validation: pass" in reproducibility and "module 06 validation: pass" in reproducibility, "Reproducibility record covers three module validations", checks)
        ai_use = (root / "ai-use.md").read_text(encoding="utf-8").lower()
        require("material output verified:" in ai_use and "verification method and result:" in ai_use and "human decision:" in ai_use, "AI-use record contains verification and human decision", checks)

    score_fields, scores = csv_rows(root, "component-score.csv", 8, checks)
    require(score_fields == SCORE_FIELDS, "Component-score header matches", checks)
    available = [Decimal(row["course_points"]) for row in scores]
    require(sum(available) == Decimal("25.00"), "Checkpoint points total 25", checks)
    require(sum(available[:3]) == Decimal("13.75") and sum(available[3:5]) == Decimal("6.25") and sum(available[5:]) == Decimal("5.00"), "Quality, descriptive, and access shares match", checks)

    if not starter:
        earned = [Decimal(row["score"]) for row in scores]
        require(all(Decimal("0") <= value <= limit for value, limit in zip(earned, available, strict=True)), "Earned points are in range", checks)
        require(sum(earned) >= Decimal("20.00"), "Passing score is at least 20 of 25", checks)
        require(all(row["status"] in {"pass", "pass with conditions"} for row in scores), "All scored criteria pass", checks)
        review = (root / "review-disposition.md").read_text(encoding="utf-8").lower()
        match = re.search(r"(?m)^disposition:\s*(accept with conditions|accept|revise|refer)\s*$", review)
        require(bool(match), "Review has an allowed disposition", checks)
        require(match.group(1) in {"accept", "accept with conditions"}, "Disposition permits Module 07", checks)
        require(bool(re.search(r"(?m)^module 07 progression:\s*allowed(?: with conditions)?\s*$", review)), "Module 07 progression is explicit", checks)

    for relative in ("artifact-contract.csv", "release-manifest.csv", "checkpoint-summary.csv"):
        require(b"\r\n" not in (root / relative).read_bytes(), f"Generated contract uses LF: {relative}", checks)

    report = {
        "status": "pass",
        "mode": "starter" if starter else "complete",
        "checks_passed": len(checks),
        "checks": checks,
        "artifact_rows": len(manifest),
        "course_points": 25,
    }
    print(f"FND-1 Checkpoint 2 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-checkpoint2-validate-") as temp_dir:
        temp = Path(temp_dir)
        reference = temp / "reference"
        learner = temp / "learner"
        assemble_checkpoint.assemble(assemble_checkpoint.CANONICAL_ROOTS, reference, reference=True)
        assemble_checkpoint.assemble(assemble_checkpoint.CANONICAL_ROOTS, learner)
        validate(reference)
        validate(learner, starter=True)
        try:
            validate(learner)
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted unfinished cumulative records.")
        (reference / "figures" / "quality-missingness.png").unlink()
        try:
            validate(reference)
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted a missing immutable artifact.")
    print("FND-1 Checkpoint 2 validator self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.checkpoint:
            parser.error("provide a checkpoint folder or --self-check")
        validate(args.checkpoint.resolve(), args.starter)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ET.ParseError, ValidationError) as exc:
        parser.exit(1, f"Validation failed: {exc}\n")


if __name__ == "__main__":
    main()
