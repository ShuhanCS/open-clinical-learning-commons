"""Validate an APP-2 Module 03 learner or reference workspace."""

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
from pathlib import Path

from build_workspace import IMMUTABLE_FILES, RECORD_FILES


PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
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


def validate(root: Path, learner: bool = False) -> dict[str, object]:
    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    required = set(IMMUTABLE_FILES) | set(RECORD_FILES) | {"release-manifest.csv"}
    require(root.is_dir(), "Workspace directory exists")
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    require(actual == required and len(actual) == 44, "Workspace has exactly 44 expected files")
    header, manifest = read_csv(root / "release-manifest.csv")
    require(header == ["relative_path", "bytes", "sha256", "role"], "Release manifest header matches")
    require(len(manifest) == 31 and [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Release manifest has 31 sorted immutable rows")
    require({row["relative_path"] for row in manifest} == set(IMMUTABLE_FILES), "Release manifest covers every immutable file")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Immutable file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Immutable bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Immutable SHA-256 matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    contract = json.loads((root / "response-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app2-03", "version": "0.1.0", "commons_release": "0.58.0", "week": 3, "hours": 16.5}, "Module identity matches")
    require(contract["upstream"]["manifest_sha256"] == "c261307b45be842c00c9ded66614a3770f379d41a1d7efecb68032f9c090a870", "Accepted Module 02 fingerprint matches")
    require(contract["target"]["target_rows"] == 1255 and contract["target"]["frame_coverage_percent"] == 100.0, "Target and constructed coverage contract match")
    require(contract["weighting"]["upper_bound"] == 3.0 and contract["expected_reference"]["response_cells"] == 13, "Weighting cells and bound match")

    source_header, sources = read_csv(root / "data/source-inventory.csv")
    require(source_header == ["source_id", "title", "relative_path", "url", "media_type", "bytes", "sha256", "pages", "role"], "Source inventory header matches")
    require(len(sources) == 5 and sum(int(row["bytes"]) for row in sources) == 12353779 and sum(int(row["pages"] or 0) for row in sources) == 869, "Official source suite has five files, 12,353,779 bytes, and 869 PDF pages")
    require(all(row["url"].startswith("https://meps.ahrq.gov/") for row in sources), "Every source URL is official and complete")
    field_header, field_rows = read_csv(root / "data/field-map.csv")
    require(field_header == ["source_name", "start", "end", "kind", "derived_use"] and len(field_rows) == 17, "Fixed-width field map has 17 fields")
    require(field_rows[-3]["source_name"] == "PERWT24F" and field_rows[-2]["source_name"] == "VARSTR" and field_rows[-1]["source_name"] == "VARPSU", "Weight and design fields remain explicit")

    public_header, public = read_csv(root / "data/public/adult-inpatient-frame.csv")
    synthetic_header, synthetic = read_csv(root / "data/synthetic/response-study.csv")
    require(len(public) == len(synthetic) == 1255, "Public frame and synthetic overlay each have 1,255 rows")
    require("DUPERSID" not in public_header and "exact_age" not in public_header and all(not name.startswith("_") for name in public_header), "Derived public frame omits direct source ID, exact age, and private builder fields")
    ids = [row["frame_record_id"] for row in public]
    require(ids == [row["frame_record_id"] for row in synthetic] and len(ids) == len(set(ids)), "Frame identity is unique and aligned")
    require(all(float(row["base_person_weight"]) > 0 and int(row["inpatient_discharges"]) >= 1 for row in public), "Every frame row has positive base weight and an inpatient discharge")
    require(abs(sum(float(row["base_person_weight"]) for row in public) - 18879474.284615) < 0.000001, "Target base-weighted population matches")
    respondents = [row for row in synthetic if row["response_status"] == "respondent"]
    nonrespondents = [row for row in synthetic if row["response_status"] == "nonrespondent"]
    require(len(respondents) == 782 and len(nonrespondents) == 473 and all(row["invited"] == "yes" for row in synthetic), "Every frame member is invited and response counts match")
    require(sum(row["q21_truth"] == "home_or_other" for row in synthetic) == 1006, "Full-frame Q21 home truth count matches")
    require(sum(row["response_status"] == "respondent" and row["q21_truth"] == "home_or_other" for row in synthetic) == 642, "Respondent Q21 home count matches")
    require(all(row["q21_observed"] == row["q22_observed"] == row["q23_observed"] == "not_observed_total_nonresponse" for row in nonrespondents), "Nonrespondents have no observed Q21, Q22, or Q23 value")
    require(all(row["q22_truth"] == row["q23_truth"] == "not_applicable" for row in synthetic if row["q21_truth"] == "another_health_facility"), "Q21 another-health-facility truth preserves Q22 and Q23 not applicable")
    require(all(row["analysis_weight"] == "" for row in nonrespondents) and all(float(row["analysis_weight"]) > 0 for row in respondents), "Only respondents receive a positive analysis weight")
    require(max(float(row["bounded_response_factor"]) for row in synthetic) <= 3.0, "No bounded response factor exceeds 3.0")
    require(sum(row["q22_observed"] in ("yes", "no") for row in synthetic) == 585 and sum(row["q23_observed"] in ("yes", "no") for row in synthetic) == 589, "Q22 and Q23 answered counts match")

    profile_header, profile = read_csv(root / "outputs/source-profile.csv")
    require(profile_header == ["metric", "value", "unit", "evidence"] and len(profile) == 10, "Source profile has ten metrics")
    profile_map = {row["metric"]: row["value"] for row in profile}
    require(profile_map["source_rows"] == "19140" and profile_map["positive_person_weight_rows"] == "18683" and profile_map["target_rows"] == "1255", "Source profile counts match")
    saq_header, saq = read_csv(root / "outputs/public-saq-response.csv")
    require(len(saq) == 1 and saq[0]["eligible_n"] == "1251" and saq[0]["has_saq_data_n"] == "993", "Public MEPS SAQ example counts match")
    require(saq[0]["unweighted_has_data_percent"] == "79.37649880" and saq[0]["base_weighted_has_data_percent"] == "79.58699393", "Public MEPS SAQ rates match")
    flow_header, flow = read_csv(root / "outputs/response-flow.csv")
    require(len(flow) == 7 and [row["count"] for row in flow] == ["1255", "1255", "1255", "782", "642", "585", "589"], "Immutable response flow conserves every set")
    subgroup_header, subgroup = read_csv(root / "outputs/subgroup-response.csv")
    require(len(subgroup) == 40 and {row["dimension"] for row in subgroup} == {"age_band", "sex", "race_ethnicity", "other_language_at_home", "poverty_category", "health_status", "proxy_status", "interview_language", "insurance_coverage", "region", "assigned_mode"}, "Subgroup response table covers 11 dimensions")
    require(any(row["support_flag"] == "limited_support" for row in subgroup), "Limited subgroup support remains visible")
    item_header, items = read_csv(root / "outputs/item-missingness.csv")
    require(len(items) == 20 and {row["item"] for row in items} == {"Q22", "Q23"}, "Item-missingness table has 20 Q22 and Q23 rows")
    item_total = {(row["item"], row["dimension"]): row for row in items if row["dimension"] == "total"}
    require(item_total[("Q22", "total")]["missing_n"] == "57" and item_total[("Q23", "total")]["missing_n"] == "53", "Item-specific missing counts match")
    cell_header, cells = read_csv(root / "outputs/weight-cells.csv")
    require(len(cells) == 13 and sum(row["bound_hit"] == "yes" for row in cells) == 1, "Thirteen observed response cells and one bound hit remain visible")
    require(all(float(row["bounded_response_factor"]) <= 3 for row in cells) and any(row["frame_n"] == "1" and row["support_flag"] == "limited_support" for row in cells), "Weight bound and one-record missing-language support flag match")
    diagnostic_header, diagnostics = read_csv(root / "outputs/weight-diagnostics.csv")
    require(len(diagnostics) == 2 and diagnostics[0]["kish_effective_n"] == "548.95483815" and diagnostics[1]["kish_effective_n"] == "527.00399458", "Weight diagnostics retain both Kish effective sample sizes")
    estimate_header, estimates = read_csv(root / "outputs/estimate-comparison.csv")
    require(len(estimates) == 12 and {row["measure"] for row in estimates} == {"Q22", "Q23", "teaching_composite"}, "Estimate comparison has three measures and four estimators")
    estimate_map = {(row["measure"], row["estimator"]): row for row in estimates}
    expected_adjusted = {"Q22": "75.23813405", "Q23": "74.64013037", "teaching_composite": "74.93913221"}
    require(all(estimate_map[(measure, "respondent_response_adjusted")]["estimate_percent"] == value for measure, value in expected_adjusted.items()), "Response-adjusted estimates match")
    require(all(float(estimate_map[(measure, "respondent_response_adjusted")]["absolute_bias_pp"]) < float(estimate_map[(measure, "respondent_base_weighted")]["absolute_bias_pp"]) for measure in expected_adjusted), "Bounded adjustment improves both items and the composite")
    require(all(float(estimate_map[(measure, "respondent_response_adjusted")]["absolute_bias_pp"]) > 0 for measure in expected_adjusted), "Known-truth residual bias remains visible")
    invariant_header, invariants = read_csv(root / "outputs/invariant-checks.csv")
    require(len(invariants) == 23 and all(row["status"] == "pass" for row in invariants), "All 23 immutable evidence invariants pass")
    report = json.loads((root / "build-report.json").read_text(encoding="utf-8"))
    require(report["status"] == "pass" and report["source"]["bytes"] == 12353779 and report["synthetic_response"]["respondents"] == 782, "Build report identity and counts match")

    for name in RECORD_FILES:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if learner:
            require(bool(PLACEHOLDER.search(text)), f"Learner prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Reference record is complete: {name}")
    if learner:
        report = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 44}
        print(f"APP-2 Module 03 learner validation passed: {len(checks)} checks.")
        return report

    response_header, response_record = read_csv(root / "response-flow.csv")
    require(len(response_record) == 6 and response_record[0]["value"] == "62.31075697 percent", "Completed response-flow record matches")
    subgroup_record_header, subgroup_record = read_csv(root / "subgroup-representation.csv")
    require(len(subgroup_record) == 5 and any(row["frame_support"] == "1" and "missing" in row["dimension"] for row in subgroup_record), "Completed subgroup record retains the one-record missing-language cell")
    missing_record_header, missing_record = read_csv(root / "item-missingness.csv")
    require(len(missing_record) == 2 and [row["missing_n"] for row in missing_record] == ["57", "53"], "Completed item-missingness record matches")
    bias_header, bias_record = read_csv(root / "bias-recovery.csv")
    require(len(bias_record) == 3 and bias_record[-1]["adjusted_absolute_bias_pp"] == "4.20274444", "Completed bias-recovery record matches")
    gate_header, gates = read_csv(root / "gate-results.csv")
    require(len(gates) == 19 and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 20)] and all(row["status"] == "pass" for row in gates), "All 19 response gates pass in order")
    target_text = (root / "target-frame.md").read_text(encoding="utf-8")
    require(all(value in target_text for value in ("19,140", "18,683", "1,255", "18,879,474.284615", "100 percent")), "Target-frame record contains exact population evidence")
    weighting_text = (root / "weighting-decision.md").read_text(encoding="utf-8")
    require(all(value in weighting_text for value in ("PERWT24F", "13", "3.0", "one", "548.95483815", "527.00399458", "0.77492695")), "Weighting decision contains exact factor and stability evidence")
    mode_text = (root / "mode-coverage-interpretation.md").read_text(encoding="utf-8").lower()
    require("not evidence" in mode_text and "100 percent teaching coverage" in mode_text, "Mode and coverage interpretation rejects real causal and coverage claims")
    privacy_text = (root / "privacy-consent.md").read_text(encoding="utf-8")
    require(markdown_field(privacy_text, "Current fielding status") == "prohibited", "Real fielding remains prohibited")
    reproduction_text = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require("two independent evidence builds match byte for byte" in reproduction_text and "23 of 23 pass" in reproduction_text and "none" in reproduction_text, "Reproducibility record is complete")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Carried checkpoint score") == "20.00 of 20.00 from Module 02 exactly once", "Carried score is exact and not duplicated")
    require(markdown_field(progression, "Module 03 response gates") == "19 of 19 pass" and markdown_field(progression, "Failed gates") == "none", "Progression records all response gates")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 04 permission")
    require(disposition in ALLOWED_PROGRESSION and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for linked analysis")), "Module 04 permission matches progression")
    require(markdown_field(progression, "Clinical action") == "prohibited" and markdown_field(progression, "Hospital ranking") == "prohibited" and markdown_field(progression, "Real fielding") == "prohibited", "Clinical, ranking, and fielding prohibitions remain explicit")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    labels = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in labels), "AI-use record has every accountable field")
    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 44}
    print(f"APP-2 Module 03 reference validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_response_evidence
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app2-module03-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner, reproduction = base / "reference", base / "learner", base / "reproduction"
        build_workspace.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_workspace.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_workspace.assemble(learner)
        starter = validate(learner, learner=True)
        rebuilt = build_response_evidence.build(reproduction)
        for relative, digest in rebuilt["generated_sha256"].items():
            assert sha256(reference / relative) == digest

        broken = base / "broken-response"
        shutil.copytree(reference, broken)
        path = broken / "data/synthetic/response-study.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",respondent,", ",nonrespondent,", 1), encoding="utf-8", newline="\n")
        try:
            validate(broken)
        except ValidationError as error:
            assert "Immutable bytes match" in str(error) or "Immutable SHA-256 matches" in str(error)
        else:
            raise AssertionError("Validator accepted a changed response state")

        bad_gate = base / "bad-gate"
        shutil.copytree(reference, bad_gate)
        path = bad_gate / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_gate)
        except ValidationError as error:
            assert "19 response gates" in str(error)
        else:
            raise AssertionError("Validator accepted a failed response gate")

        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        path = bad_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("permitted for linked analysis", "prohibited", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_progression)
        except ValidationError as error:
            assert "permission matches progression" in str(error)
        else:
            raise AssertionError("Validator accepted invalid Module 04 permission")
    print(f"APP-2 Module 03 validator self-check passed: {complete['checks_passed']} reference checks and {starter['checks_passed']} learner checks; copied, reproduction, and mutation routes verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--learner", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            validate(args.workspace, learner=args.learner)
        else:
            parser.error("workspace is required unless --self-check is used")
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
