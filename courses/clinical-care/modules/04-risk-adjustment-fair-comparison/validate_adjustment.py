"""Validate APP-1 Module 04 risk-adjustment workspaces."""

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


MODULE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "source-record.yml", "adjustment-contract.json", "environment.yml",
    "assessment.md", "field-role-contract.csv", "build_adjustment.py", "validate_adjustment.py",
    "paired-risk-adjustment.R",
)
WORK_FILES = (
    "README.md", "risk-adjustment-memo.md", "model-assessment.md", "support-suppression-review.md",
    "fair-comparison-interpretation.md", "reproducibility-check.md", "ai-use.md", "progression-decision.md",
)
OUTPUTS = {
    "adjusted-association.csv": (1, 12, 397, "ba45d38cf65bc19de33708827cf1b0fe27ef981d8ffd95d78fa861c758098f20"),
    "analysis-checks.csv": (16, 4, 552, "1bac4ea6f83e2799deb440b23da948beae70b1c382bdccc112012072aaa5d3b3"),
    "bootstrap-stability.csv": (5, 9, 946, "07cdfbe77b35bd869960127ea34c65d753f65a416a03b8532b86ec4608a3938c"),
    "build-report.json": (None, None, 13873, "c5466c3f6778f8d689151ac6f32203b422b63b81c29868e6539f3e33f2010f43"),
    "calibration-quintiles.csv": (5, 8, 495, "01a0bcd82ba15acb556298e029057dc039bffd1971e1324eeb797508da6ce4db"),
    "comparison-figure.svg": (None, None, 51255, "99221affece300425e43c8e0a25721082ad0690be3e55dffd9860e30f0e78eb9"),
    "expected-outcomes.csv": (476, 12, 54320, "e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e"),
    "exposure-comparison.csv": (2, 13, 591, "32c800fd3dc3099054c8ba5745c3b3bb0a4f1060f6b8fe036b6643b90713a565"),
    "field-role-summary.csv": (22, 4, 1480, "d83f11a72b612dca0dd621b4e67c995ab40a09755b3dd0c14026c59a733849fc"),
    "model-coefficients.csv": (5, 10, 1230, "032c8aec1b419f0f0efb6761b585dd2cdab1a53d0f48d969cb505a50a128b082"),
    "model-performance.csv": (10, 3, 587, "7b2b6d8e97c93a3f74f8f4888b52097e8867808b3e4278a4a429f5a525e763a3"),
    "site-case-mix.csv": (6, 11, 575, "5cc00cc5d79a66fac0729d4aa8044b8bc05e02621720f3326b26856a9e134775"),
    "site-comparison.csv": (6, 20, 1908, "a0a97799817e22bbe4252b3d296ae4150c0120eb182078fcd37b44c5e5610329"),
}
SITE_ORDER = ["SITE-A", "SITE-B", "SITE-C", "SITE-D", "SITE-E", "SITE-F"]
PREDICTORS = {"index_encounter_class", "age_at_index", "prior_365d_acute_count", "prior_365d_condition_count"}
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


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    required = set(IMMUTABLE_FILES) | set(WORK_FILES)
    is_source_package = root == MODULE_ROOT.resolve() and (root / "template").is_dir()
    require(root.is_dir(), "Workspace directory exists")
    require(all((root / name).is_file() for name in required), "All fixed and work files are present")
    if not is_source_package:
        expected = required | {"workspace-manifest.csv"}
        if not starter:
            expected |= {f"outputs/{name}" for name in OUTPUTS}
        actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
        require(actual == expected, f"Workspace has exactly {19 if starter else 32} expected files")
        header, manifest = read_csv(root / "workspace-manifest.csv")
        require(header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
        require(len(manifest) == 10 and [row["relative_path"] for row in manifest] == sorted(IMMUTABLE_FILES), "Manifest has ten sorted immutable rows")
        for row in manifest:
            path = root / row["relative_path"]
            require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
            require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
            require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    source = (root / "source-record.yml").read_text(encoding="utf-8")
    require(all(value in source for value in ("commons_release: 0.52.0", "people: 476", "events: 87", "ph_screen_result: fail")), "Source identity counts and PH handoff match")
    require("558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5" in source, "Upstream cohort fingerprint matches")
    require("ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860" in source, "Checkpoint fingerprint matches")
    contract = json.loads((root / "adjustment-contract.json").read_text(encoding="utf-8"))
    require(contract["analysis_id"] == "app1-risk-adjustment-v1" and contract["fixed_horizon_days"] == 335, "Adjustment identity and horizon match")
    require([row["model_field"] for row in contract["predictors"]] == ["age_decade_from_40", "any_prior_acute", "prior_365d_condition_count", "index_inpatient"], "Four predictors and order match")
    require(contract["bootstrap"] == {"samples": 300, "seed": 20260830, "unit": "person"}, "Bootstrap contract matches")
    require(contract["site_order"] == SITE_ORDER and contract["suppression"]["minimum_observed_events"] == 10, "Site order and suppression contract match")
    environment = (root / "environment.yml").read_text(encoding="utf-8")
    require(all(value in environment for value in ("matplotlib=3.10.9", "numpy=2.0.2", "pandas=3.0.3", "scipy=1.17.1", "statsmodels=0.14.6", "r-stats")), "Environment versions and R route match")
    assessment = (root / "assessment.md").read_text(encoding="utf-8")
    require("Total | 25.00" in assessment and len(re.findall(r"(?m)^\d+\. ", assessment)) == 18, "Assessment has 25 points and 18 gates")

    role_header, roles = read_csv(root / "field-role-contract.csv")
    require(role_header == ["field_id", "field", "provenance", "timing", "role", "transformation", "permitted_use", "prohibited_use"], "Field-role header matches")
    require(len(roles) == 49 and [row["field_id"] for row in roles] == [f"F{i:03d}" for i in range(1, 50)], "All 49 field roles are ordered")
    require({row["field"] for row in roles if row["role"] == "baseline_predictor"} == PREDICTORS, "Only four prespecified fields are baseline predictors")
    role_by_field = {row["field"]: row["role"] for row in roles}
    require(role_by_field["landmark_exposure"] == "exposure" and role_by_field["event_indicator"] == "outcome" and role_by_field["teaching_site_id"] == "comparison_group", "Exposure outcome and site cannot leak into expected outcomes")
    require({role_by_field[name] for name in ("gender", "race", "ethnicity")} == {"equity_audit_only"}, "Demographic fields remain audit-only")

    text_files = [name for name in required if Path(name).suffix.lower() in {".md", ".json", ".yml", ".r"}]
    for name in text_files:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if starter and name in WORK_FILES:
            require(bool(PLACEHOLDER.search(text)), f"Starter prompt is present: {name}")
        if not starter and name in WORK_FILES:
            require(not PLACEHOLDER.search(text), f"Work file is complete: {name}")
    if starter:
        require(not (root / "outputs").exists(), "Starter has no prebuilt outputs")
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "assembled_files": 19}
        print(f"APP-1 Module 04 starter validation passed: {len(checks)} checks.")
        return report

    output_root = root / "outputs"
    require(all((output_root / name).is_file() for name in OUTPUTS), "All thirteen outputs are present")
    tables: dict[str, list[dict[str, str]]] = {}
    for name, (expected_rows, expected_fields, expected_bytes, expected_hash) in OUTPUTS.items():
        path = output_root / name
        require(path.stat().st_size == expected_bytes, f"Output bytes match: {name}")
        require(sha256(path) == expected_hash, f"Output SHA-256 matches: {name}")
        if path.suffix == ".csv":
            header, rows = read_csv(path)
            require(len(rows) == expected_rows and len(header) == expected_fields, f"Output shape matches: {name}")
            tables[name] = rows

    require(all(row["status"] == "pass" for row in tables["analysis-checks.csv"]), "All 16 analysis checks pass")
    people = tables["expected-outcomes.csv"]
    require(len({row["patient_id"] for row in people}) == 476 and sum(int(row["event_indicator"]) for row in people) == 87, "Person output conserves 476 people and 87 events")
    require(abs(sum(float(row["expected_probability"]) for row in people) - 87) < 0.000001, "Person expected events reconcile to 87")
    require(sum(int(row["landmark_exposure"]) for row in people) == 129 and {row["teaching_site_id"] for row in people} == set(SITE_ORDER), "Exposure and site support are conserved")

    performance = {row["metric"]: row["value"] for row in tables["model-performance.csv"]}
    require(performance["brier_score"] == "0.13490621" and performance["roc_auc"] == "0.66585409" and performance["sum_expected_events"] == "87.00000000", "Apparent performance matches")
    coefficients = {row["term"]: row for row in tables["model-coefficients.csv"]}
    require(coefficients["any_prior_acute"]["coefficient"] == "1.86449649" and coefficients["index_inpatient"]["odds_ratio"] == "4.09130751", "Expected-model coefficients match")
    bootstrap = {row["term"]: row for row in tables["bootstrap-stability.csv"]}
    require(all(row["successful_fits"] == "300" and row["failed_fits"] == "0" for row in bootstrap.values()), "All 300 bootstrap fits are accounted for")
    require(bootstrap["any_prior_acute"]["bootstrap_upper97_5"] == "22.56297423" and bootstrap["age_decade_from_40"]["same_sign_share"] == "0.58666667", "Sparse and sign instability remain visible")

    calibration = tables["calibration-quintiles.csv"]
    require([row["quintile"] for row in calibration] == ["1", "2", "3", "4", "5"] and sum(int(row["observed_events"]) for row in calibration) == 87, "Five calibration groups conserve events")
    require(calibration[-1]["observed_events"] == "37" and calibration[-1]["expected_events"] == "33.61772427", "Highest calibration group matches")

    exposure = {row["group"]: row for row in tables["exposure-comparison.csv"]}
    require(exposure["scheduled_followup"]["standardized_event_rate"] == "0.19819116" and exposure["no_recorded_followup"]["standardized_event_rate"] == "0.17721417", "Exposure standardized rates match")
    association = tables["adjusted-association.csv"][0]
    require(association["adjusted_odds_ratio"] == "1.16353250" and association["lower95"] == "0.67665877" and association["upper95"] == "2.00072462" and association["p_value"] == "0.58392672", "Secondary adjusted association matches")
    require("not risk ratio hazard ratio or causal effect" in association["boundary"], "Adjusted-association quantity boundary is explicit")

    sites = tables["site-comparison.csv"]
    require([row["teaching_site_id"] for row in sites] == SITE_ORDER, "Six sites remain in fixed order")
    require(sum(int(row["people"]) for row in sites) == 476 and sum(int(row["observed_events"]) for row in sites) == 87, "Site comparison conserves people and events")
    require(all(row["suppression_status"] == "report with caution" and row["known_direct_site_effect"] == "0" and row["field_class"] == "synthetic_extension" for row in sites), "Every site is reportable with synthetic zero-effect provenance")
    require(all(int(row["people"]) >= 50 and int(row["observed_events"]) >= 10 and float(row["expected_events"]) >= 10 for row in sites), "Every site meets numerical support thresholds")
    require(sites[0]["standardized_event_rate"] == "0.27308240" and sites[1]["observed_events"] == "10" and sites[2]["expected_events"] == "10.90777066", "Site reference evidence matches")
    require(all(0 <= float(row["standardized_lower95"]) <= float(row["standardized_event_rate"]) <= float(row["standardized_upper95"]) for row in sites), "Every site interval is ordered")

    svg = (output_root / "comparison-figure.svg").read_text(encoding="utf-8")
    require(all(value in svg for value in ("SITE-A", "SITE-F", "Indirectly standardized event rate", "fixed order and not rankings", "cohort event rate", "expected events as fixed")), "Figure labels and interpretation boundary are present")
    report_json = json.loads((output_root / "build-report.json").read_text(encoding="utf-8"))
    require(report_json["module"] == "oclc-app1-04" and report_json["commons_release"] == "0.52.0", "Build report identity matches")
    require(report_json["source"]["sha256"] == "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5" and report_json["model"]["bootstrap"]["successful"] == 300, "Build report source and bootstrap match")

    memo = (root / "risk-adjustment-memo.md").read_text(encoding="utf-8").lower()
    require(all(value in memo for value in ("87.00000000", "1.16353250", "0.58392672", "not a risk ratio", "does not repair", "0.00636020")), "Memo has exact evidence and quantity boundaries")
    model = (root / "model-assessment.md").read_text(encoding="utf-8").lower()
    require(all(value in model for value in ("apparent", "0.13490621", "0.66585409", "300 person bootstrap fits succeeded", "22.56297423")), "Model assessment reports performance and instability")
    support = (root / "support-suppression-review.md").read_text(encoding="utf-8").lower()
    require(all(value in support for value in ("site-a", "site-f", "structured alternative", "fixed", "report with caution")), "Support review includes fixed visual and structured routes")
    fair = (root / "fair-comparison-interpretation.md").read_text(encoding="utf-8").lower()
    require(all(value in fair for value in ("known direct effect", "zero", "not a risk ratio", "residual confounding", "does not certify fairness", "league table")), "Fair-comparison boundaries are explicit")
    reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require(all(value in reproducibility for value in ("two complete builds match byte for byte", "changed-field-role result", "execution awaits")), "Reproduction and R status are honest")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in ai_fields), "AI-use record has every accountable field")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Cumulative component score") == "25.00 of 25.00", "Cumulative score is exact")
    require(markdown_field(progression, "Risk-adjustment gate result") == "18 of 18 pass", "All risk-adjustment gates pass")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 05 permission")
    require(disposition in ALLOWED_PROGRESSION, "Progression value is allowed")
    require((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction"), "Module 05 permission matches progression")
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) >= 10, "Progression has at least ten owned conditions")

    report = {"status": "pass", "mode": "complete", "checks_passed": len(checks), "assembled_files": 32}
    print(f"APP-1 Module 04 complete validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app1-module04-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, starter = base / "reference", base / "starter"
        build_workspace.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_adjustment.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_workspace.assemble(starter)
        learner = validate(starter, starter=True)
        try:
            validate(starter)
        except ValidationError as error:
            assert "exactly 32 expected files" in str(error)
        else:
            raise AssertionError("Validator accepted an incomplete starter")

        mutations = (
            ("broken-output", "outputs/model-performance.csv", "0.13490621", "0.93490621", "Output SHA-256 matches"),
            ("bad-score", "progression-decision.md", "25.00 of 25.00", "24.00 of 25.00", "Cumulative score is exact"),
            ("bad-progression", "progression-decision.md", "continue with conditions", "deploy", "Progression value is allowed"),
            ("bad-field-role", "field-role-contract.csv", "F029,landmark_exposure", "F029,landmark_outcomex", "Manifest SHA-256 matches"),
        )
        for folder, relative, old, new, expected_error in mutations:
            bad = base / folder
            shutil.copytree(reference, bad)
            path = bad / relative
            path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8", newline="\n")
            try:
                validate(bad)
            except ValidationError as error:
                assert expected_error in str(error), error
            else:
                raise AssertionError(f"Validator accepted mutation: {folder}")
    print(f"APP-1 Module 04 validator self-check passed: {complete['checks_passed']} complete checks and {learner['checks_passed']} starter checks; copied, incomplete, output, score, progression, and field-role routes verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
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
        validate(args.workspace, starter=args.starter)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
