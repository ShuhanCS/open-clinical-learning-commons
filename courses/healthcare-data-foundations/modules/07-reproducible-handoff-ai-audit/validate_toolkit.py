"""Validate an FND-1 Module 07 reproducible toolkit candidate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import math
import re
import tempfile
from collections import Counter
from decimal import Decimal
from pathlib import Path


SCRIPT_ROOT = Path(__file__).resolve().parent
PIPELINE_FIELDS = ["artifact_id", "source_unit", "source_module_dir", "source_path", "target_path", "byte_count", "sha256", "role"]
MANIFEST_FIELDS = ["relative_path", "source_unit", "source_version", "bytes", "sha256", "role"]
SCORE_FIELDS = ["criterion_id", "criterion", "course_points", "score", "evidence", "status"]
PROMPT_FIELDS = [
    "entry_id", "date", "tool_model", "purpose", "data_class_shared", "request_summary",
    "response_summary", "affected_artifact", "risk_if_wrong", "verification_method",
    "evidence", "result", "human_action_owner", "disclosure_status",
]
PLACEHOLDER = re.compile(r"\[REPLACE:[^\]\r\n]*\]|\b(?:TODO|TBD|REPLACE(?:_ME)?)\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
RECORD_FILES = (
    ".gitattributes", "README.md", "CHANGELOG.md", "release-notes.md",
    "component-score.csv", "release-checklist.md", "reproducibility-check.md",
    "review-disposition.md", "documentation/data-brief.md", "documentation/limitations.md",
    "documentation/ai-audit.md", "audit/prompt-log.csv", "defense/handoff-brief.md",
    "defense/questions-and-responses.md", "VERSION",
)
TEXT_RECORDS = tuple(path for path in RECORD_FILES if path not in {".gitattributes", "VERSION"})
ISSUES = [f"D{value:02d}" for value in range(1, 21)] + [f"N{value:02d}" for value in range(1, 9)]
PIPELINE_CONTRACT_SHA256 = "d61f208046663b80f8a591be66cc4f22fecbf0c5be7803786f75fd74cdd1d783"
ANALYTIC_SHA256 = "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"


class ValidationError(RuntimeError):
    pass


def require(condition: bool, label: str, checks: list[str]) -> None:
    if not condition:
        raise ValidationError(label)
    checks.append(label)


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


def csv_rows(root: Path, relative: str, expected: int, checks: list[str]) -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = read_csv(root / relative)
    require(len(rows) == expected, f"Expected row count {expected}: {relative}", checks)
    return fields, rows


def wilson(numerator: int, denominator: int) -> tuple[float, float]:
    z = 1.959963984540054
    proportion = numerator / denominator
    denominator_term = 1 + z * z / denominator
    center = (proportion + z * z / (2 * denominator)) / denominator_term
    spread = z * math.sqrt((proportion * (1 - proportion) + z * z / (4 * denominator)) / denominator) / denominator_term
    return 100 * (center - spread), 100 * (center + spread)


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    checks: list[str] = []
    require(root.is_dir(), "Toolkit directory exists", checks)
    manifest_fields, manifest = csv_rows(root, "release-manifest.csv", 74, checks)
    require(manifest_fields == MANIFEST_FIELDS, "Release manifest header matches", checks)
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths), "Release manifest paths are sorted", checks)
    require(len(set(paths)) == 74, "Release manifest paths are unique", checks)
    required = set(paths) | set(RECORD_FILES) | {"release-manifest.csv"}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    require(len(required) == 90 and actual == required, "Toolkit has the exact 90-file tree", checks)
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Toolkit version is 0.1.0", checks)

    for relative in TEXT_RECORDS:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII punctuation: {relative}", checks)
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}", checks)
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}", checks)

    blocked_suffixes = {".sqlite", ".db", ".zip", ".pyc", ".pem", ".key"}
    require(not any(path.suffix.lower() in blocked_suffixes for path in root.rglob("*") if path.is_file()), "No database, archive, cache, key, or certificate file", checks)
    require(not any(part in {".venv", "__pycache__", "source-cache"} for path in root.rglob("*") for part in path.parts), "No environment, cache, or source-cache directory", checks)

    expected_sources = Counter({
        "CP2-M04": 11, "CP2-M05": 9, "CP2-M06": 15, "CP2": 14,
        "M01": 1, "M02": 13, "M03": 5, "M04": 2, "M05": 1, "M06": 1, "M07": 2,
    })
    require(Counter(row["source_unit"] for row in manifest) == expected_sources, "Manifest source allocation matches", checks)
    for row in manifest:
        relative = row["relative_path"]
        path = Path(relative)
        require(not path.is_absolute() and ".." not in path.parts, f"Manifest path is portable: {relative}", checks)
        file_path = root / path
        require(file_path.is_file(), f"Manifest file exists: {relative}", checks)
        require(file_path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {relative}", checks)
        require(sha256(file_path) == row["sha256"], f"Manifest SHA-256 matches: {relative}", checks)
        require(row["source_version"] == "0.1.0" and bool(row["role"]), f"Manifest version and role match: {relative}", checks)

    pipeline_path = root / "pipeline-contract.csv"
    pipeline_fields, pipeline = csv_rows(root, "pipeline-contract.csv", 23, checks)
    require(pipeline_fields == PIPELINE_FIELDS, "Pipeline contract header matches", checks)
    require(sha256(pipeline_path) == PIPELINE_CONTRACT_SHA256 and pipeline_path.stat().st_size == 4478, "Pipeline contract fingerprint matches", checks)
    require(len({row["artifact_id"] for row in pipeline}) == 23 and len({row["target_path"] for row in pipeline}) == 23, "Pipeline IDs and targets are unique", checks)
    require(Counter(row["source_unit"] for row in pipeline) == Counter({"M01": 1, "M02": 13, "M03": 5, "M04": 2, "M05": 1, "M06": 1}), "Pipeline source allocation matches", checks)
    manifest_by_path = {row["relative_path"]: row for row in manifest}
    for row in pipeline:
        target = row["target_path"]
        require(target in manifest_by_path, f"Pipeline target is manifested: {target}", checks)
        require((root / target).stat().st_size == int(row["byte_count"]), f"Pipeline bytes match: {target}", checks)
        require(sha256(root / target) == row["sha256"], f"Pipeline SHA-256 matches: {target}", checks)

    require(sha256(root / "provenance/checkpoint2-artifact-contract.csv") == "ec031d23a50628b07ce15091c90a76f03241e3f4c4a17927211b74b854754a6b", "Checkpoint 2 artifact contract fingerprint matches", checks)
    require(sha256(root / "provenance/checkpoint2-release-manifest.csv") == "d7bb0e561309f4b61353f4485fe1d647d8a15c47e064f93acd816a77e512489d", "Checkpoint 2 manifest fingerprint matches", checks)
    _, checkpoint_contract = csv_rows(root, "provenance/checkpoint2-artifact-contract.csv", 35, checks)
    _, checkpoint_manifest = csv_rows(root, "provenance/checkpoint2-release-manifest.csv", 35, checks)
    _, checkpoint_summary = csv_rows(root, "provenance/checkpoint2-summary.csv", 3, checks)
    require((root / "provenance/checkpoint2-VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint 2 version matches", checks)
    require([row["artifact_id"] for row in checkpoint_contract] == [row["artifact_id"] for row in checkpoint_manifest], "Checkpoint 2 contract and manifest IDs agree", checks)
    require([row["source_module"] for row in checkpoint_summary] == ["M04", "M05", "M06"], "Checkpoint 2 summary modules agree", checks)
    require([row["accepted_decision"] for row in checkpoint_summary] == ["proceed with conditions", "accept with conditions", "accept with conditions"], "Checkpoint 2 accepted decisions agree", checks)

    checkpoint_record_names = (
        "README.md", "component-score.csv", "quality-decision.md", "interpretation-memo.md",
        "accessibility-synthesis.md", "source-record.yml", "transformation-record.md",
        "reproducibility-check.md", "ai-use.md", "review-disposition.md",
    )
    for name in checkpoint_record_names:
        require((root / "documentation" / "checkpoint2" / name).is_file(), f"Checkpoint 2 record exists: {name}", checks)
    upstream_review = (root / "documentation/checkpoint2/review-disposition.md").read_text(encoding="utf-8").lower()
    require("disposition: accept with conditions" in upstream_review and "module 07 progression: allowed with conditions" in upstream_review, "Checkpoint 2 permits conditional Module 07 progression", checks)

    analytic_fields, analytic = csv_rows(root, "data/analytic-table.csv", 374, checks)
    require(len(analytic_fields) == 29, "Analytic table has 29 fields", checks)
    require(len({row["patient_id"] for row in analytic}) == 374, "Analytic table has 374 unique patients", checks)
    require(len({row["index_encounter_id"] for row in analytic}) == 374, "Analytic table has 374 unique index encounters", checks)
    require(sha256(root / "data/analytic-table.csv") == ANALYTIC_SHA256, "Analytic table fingerprint matches", checks)
    no_next = [row for row in analytic if row["next_30d_state"] == "No encounter recorded"]
    require(len(no_next) == 263, "No-next-encounter rows total 263", checks)
    require(all(not row[field] for row in no_next for field in ("next_30d_encounter_id", "next_30d_start", "next_30d_days_after_index_stop")), "No-next-encounter companion fields remain blank", checks)

    dictionary_fields, dictionary = csv_rows(root, "data/data-dictionary.csv", 29, checks)
    require([int(row["position"]) for row in dictionary] == list(range(1, 30)), "Data dictionary positions are complete", checks)
    require([row["field_name"] for row in dictionary] == analytic_fields and "timing" in dictionary_fields, "Data dictionary matches analytic fields and timing", checks)

    _, defects = csv_rows(root, "quality/defect-manifest.csv", 68, checks)
    require(set(row["issue_id"] for row in defects) == set(ISSUES[:20]), "Defect manifest covers D01 through D20", checks)
    _, rules = csv_rows(root, "quality/quality-rule-results.csv", 28, checks)
    require([row["issue_id"] for row in rules] == ISSUES and all(row["detection_status"] == "pass" for row in rules), "Quality rules cover D01-D20 and N01-N08 and pass", checks)
    _, resolutions = csv_rows(root, "quality/resolution-log.csv", 28, checks)
    require(all(row["status"] == "resolved" for row in resolutions[:20]), "D01 through D20 are resolved", checks)
    require(all(row["status"] == "retained condition" for row in resolutions[20:]), "N01 through N08 remain conditions", checks)
    csv_rows(root, "quality/quality-profile.csv", 29, checks)
    csv_rows(root, "quality/missingness-profile.csv", 29, checks)
    csv_rows(root, "quality/quality-risk-log.csv", 28, checks)

    _, profiles = csv_rows(root, "evidence-tables/variable-profile.csv", 17, checks)
    require(all(int(row["available_n"]) + int(row["missing_n"]) == 374 for row in profiles), "Profile availability reconciles", checks)
    _, cross_tabs = csv_rows(root, "evidence-tables/cross-tabs.csv", 12, checks)
    require(all(sum(int(row["n"]) for row in cross_tabs if row["result_id"] == result) == 374 for result in ("CT01", "CT02")), "Cross-tabs conserve the cohort", checks)
    _, rates = csv_rows(root, "evidence-tables/rates.csv", 6, checks)
    require([int(row["numerator"]) for row in rates] == [111, 92, 4, 15, 36, 8], "Rate numerators match", checks)
    require(all(int(row["denominator"]) == 374 for row in rates), "Rate denominators match 374", checks)
    for row in rates:
        lower, upper = wilson(int(row["numerator"]), int(row["denominator"]))
        require(round(lower, 6) == round(float(row["wilson_95_lower_percent"]), 6) and round(upper, 6) == round(float(row["wilson_95_upper_percent"]), 6), f"Wilson interval matches: {row['result_id']}", checks)
    _, strata = csv_rows(root, "evidence-tables/stratified-table.csv", 2, checks)
    require(sum(int(row["n"]) for row in strata) == 374, "Strata conserve the cohort", checks)
    _, denominators = csv_rows(root, "evidence-tables/denominator-registry.csv", 27, checks)
    denominator_text = " ".join(value for row in denominators for value in row.values())
    require(all(issue in denominator_text for issue in ISSUES[20:]), "Denominator registry preserves N01 through N08", checks)
    _, descriptive_checks = csv_rows(root, "evidence-tables/descriptive-checks.csv", 18, checks)
    require(all(row["status"] == "pass" for row in descriptive_checks), "Descriptive checks pass", checks)

    csv_rows(root, "tables/quality-missingness.csv", 8, checks)
    _, visual_rates = csv_rows(root, "tables/descriptive-rates.csv", 6, checks)
    require(visual_rates == rates, "F02 table matches accepted rates", checks)
    _, quarters = csv_rows(root, "tables/quarterly-index-counts.csv", 20, checks)
    require(sum(int(row["total_index_n"]) for row in quarters) == 374, "F03 total is 374", checks)
    require(sum(int(row["emergency_index_n"]) for row in quarters) == 314, "F03 emergency total is 314", checks)
    require(sum(int(row["inpatient_index_n"]) for row in quarters) == 60, "F03 inpatient total is 60", checks)
    registry_fields, registry = csv_rows(root, "figure-registry.csv", 3, checks)
    require(len(registry_fields) == 25 and [row["figure_id"] for row in registry] == ["F01", "F02", "F03"], "Figure registry contains F01-F03 and 25 fields", checks)
    for row in registry:
        for path_field, hash_field in (("table_path", "table_sha256"), ("png_path", "png_sha256"), ("svg_path", "svg_sha256"), ("alt_text_path", "alt_text_sha256")):
            relative = row[path_field]
            require((root / relative).is_file() and sha256(root / relative) == row[hash_field], f"Figure registry target matches: {relative}", checks)
        require(row["redundant_cue"] and row["zero_baseline"] == "yes" and row["claim_limit"], f"Figure access and claim fields match: {row['figure_id']}", checks)

    requirements = (root / "requirements.txt").read_text(encoding="utf-8").splitlines()
    require(requirements == ["jupyterlab==4.6.3", "nbclient==0.10.2", "pandas==3.0.5"], "Python requirement pins match", checks)
    _, source_manifest = csv_rows(root, "source-code/module02/source-manifest.csv", 16, checks)
    require(sum(int(row["source_rows"]) for row in source_manifest) == 471836, "Module 02 source manifest rows total 471836", checks)
    schema = (root / "source-code/module02/schema.sql").read_text(encoding="utf-8").lower()
    require(all(f"create table {name}" in schema for name in ("patients", "encounters", "conditions", "medications", "observations", "supplies")), "Module 02 schema includes core tables", checks)
    for name in ("01-eligible-events.sql", "02-index-cohort.sql", "03-analytic-table.sql", "04-validation.sql"):
        sql = (root / "source-code/module03/sql" / name).read_text(encoding="utf-8").lower()
        require("with " in sql and not re.search(r"\b(insert|update|delete|drop|alter|attach)\b", sql), f"Read-only cohort SQL: {name}", checks)
    for relative, phrase in (
        ("source-code/module02/build_database.py", "EXPECTED_ARCHIVE_SHA256"),
        ("source-code/module03/build_cohort.py", "QUERIES"),
        ("source-code/module04/build_defect_release.py", "D20"),
        ("source-code/module04/profile_quality.py", "retained condition"),
        ("source-code/module05/build_descriptive.py", "wilson"),
        ("source-code/module06/render_figures.py", "redundant_cue"),
    ):
        require(phrase.lower() in (root / relative).read_text(encoding="utf-8").lower(), f"Pipeline source is substantive: {relative}", checks)

    score_fields, scores = csv_rows(root, "component-score.csv", 8, checks)
    require(score_fields == SCORE_FIELDS, "Component-score header matches", checks)
    available = [Decimal(row["course_points"]) for row in scores]
    require(sum(available) == Decimal("35.00"), "Component score totals 35", checks)

    prompt_fields, prompts = read_csv(root / "audit/prompt-log.csv")
    require(prompt_fields == PROMPT_FIELDS, "Prompt-log header matches", checks)
    if not starter:
        require(len(prompts) >= 1, "Prompt log contains a material entry", checks)
        require(all(row["result"] in {"pass", "fail", "partial support"} and row["disclosure_status"] == "disclosed" for row in prompts), "Prompt-log results and disclosure are complete", checks)
        require(all(not re.search(r"(?i)\b(restricted|phi|secret|credential|workplace)\b", row["data_class_shared"]) for row in prompts), "Prompt log contains no prohibited data class", checks)

        readme = (root / "README.md").read_text(encoding="utf-8").lower()
        require("https://github.com/shuhancs/open-clinical-learning-commons" in readme and "fnd1-handoff-v0.1.0" in readme and "90 files" in readme and "74 immutable" in readme, "README records release identity and package counts", checks)
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8").lower()
        require("## [0.1.0]" in changelog and "### added" in changelog and "### preserved" in changelog and "### known conditions" in changelog, "Change log is complete", checks)
        release_notes = (root / "release-notes.md").read_text(encoding="utf-8").lower()
        require("compatible" in release_notes and "conditions" in release_notes and "synthetic" in release_notes and "new version decision" in release_notes, "Release notes cover compatibility and conditions", checks)
        data_brief = (root / "documentation/data-brief.md").read_text(encoding="utf-8").lower()
        for phrase in ("synthea", "4194b18", "374 rows", "29 fields", "d01 through d20", "n01 through n08", "wilson", "f01", "permitted", "prohibited", "reproduction"):
            require(phrase in data_brief, f"Data brief includes: {phrase}", checks)
        limitations = (root / "documentation/limitations.md").read_text(encoding="utf-8").lower()
        for phrase in ("synthetic", "selected", "structural missingness", "small", "unadjusted", "wilson", "20-quarter", "accessibility", "macos", "human review", "revision or referral"):
            require(phrase in limitations, f"Limitations include: {phrase}", checks)
        reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
        for phrase in ("python", "sqlite", "source archive", "checkpoint 2 complete validation: pass", "second clean assembly", "toolkit complete validation: pass", "independent reproducer"):
            require(phrase in reproduction, f"Reproduction record includes: {phrase}", checks)
        audit = (root / "documentation/ai-audit.md").read_text(encoding="utf-8").lower()
        for phrase in ("claim and consequence", "independent method and evidence", "result and action", "263", "blank", "human owner", "not source"):
            require(phrase in audit, f"AI audit includes: {phrase}", checks)
        checklist = (root / "release-checklist.md").read_text(encoding="utf-8")
        require(checklist.count("- [x]") == 20 and "- [ ]" not in checklist, "All 20 release checklist items pass", checks)

        earned = [Decimal(row["score"]) for row in scores]
        require(all(Decimal("0") <= score <= limit for score, limit in zip(earned, available, strict=True)), "Earned points are in range", checks)
        require(sum(earned) >= Decimal("28.00"), "Passing score is at least 28 of 35", checks)
        require(all(row["status"] in {"pass", "pass with conditions"} for row in scores), "All score criteria pass", checks)
        defense = (root / "defense/handoff-brief.md").read_text(encoding="utf-8").lower()
        for phrase in ("source and permitted use", "schema and grain", "cohort and denominator", "analytic-table construction", "quality issue", "descriptive evidence", "accessibility path", "reproduction and validation", "ai-assisted step", "recommended disposition"):
            require(phrase in defense, f"Handoff brief includes: {phrase}", checks)
        responses = (root / "defense/questions-and-responses.md").read_text(encoding="utf-8")
        require(all(re.search(rf"(?m)^{number}\.\s+\S", responses) for number in range(1, 11)), "All ten defense responses exist", checks)
        review = (root / "review-disposition.md").read_text(encoding="utf-8").lower()
        disposition = re.search(r"(?m)^disposition:\s*(accept with conditions|accept|revise|refer)\s*$", review)
        require(bool(disposition) and disposition.group(1) in {"accept", "accept with conditions"}, "Disposition permits final checkpoint", checks)
        require(bool(re.search(r"(?m)^final checkpoint progression:\s*allowed(?: with conditions)?\s*$", review)), "Final checkpoint progression is explicit", checks)

    for relative in ("pipeline-contract.csv", "release-manifest.csv", "audit/prompt-log.csv", "component-score.csv"):
        require(b"\r\n" not in (root / relative).read_bytes(), f"Generated contract uses LF: {relative}", checks)

    report = {
        "status": "pass",
        "mode": "starter" if starter else "complete",
        "checks_passed": len(checks),
        "checks": checks,
        "manifest_rows": len(manifest),
        "course_points": 35,
    }
    print(f"FND-1 Module 07 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def load_assembler():
    path = SCRIPT_ROOT / "assemble_toolkit.py"
    if not path.is_file():
        raise ValidationError("Self-check requires assemble_toolkit.py beside the module validator.")
    spec = importlib.util.spec_from_file_location("fnd1_module07_assembler", path)
    if spec is None or spec.loader is None:
        raise ValidationError("Could not load the Module 07 assembler.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def self_check() -> None:
    assembler = load_assembler()
    with tempfile.TemporaryDirectory(prefix="fnd1-module07-validate-") as temp_dir:
        temp = Path(temp_dir)
        checkpoint = temp / "checkpoint2"
        reference = temp / "reference"
        learner = temp / "learner"
        assembler.assemble_reference_checkpoint(checkpoint)
        assembler.assemble(checkpoint, assembler.COURSE_ROOT, reference, reference=True)
        assembler.assemble(checkpoint, assembler.COURSE_ROOT, learner)
        validate(reference)
        validate(learner, starter=True)
        try:
            validate(learner)
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted unfinished release records.")
        (reference / "evidence-tables" / "rates.csv").unlink()
        try:
            validate(reference)
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted a missing immutable artifact.")
    print("FND-1 Module 07 validator self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("toolkit", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if not args.toolkit:
            parser.error("provide a toolkit folder or --self-check")
        validate(args.toolkit.resolve(), args.starter)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as exc:
        parser.exit(1, f"Validation failed: {exc}\n")


if __name__ == "__main__":
    main()
