"""Validate APP-1 Module 05 clinical-variation workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "source-record.yml", "variation-contract.json", "environment.yml",
    "assessment.md", "measure-contract.csv", "build_variation.py", "validate_variation.py",
)
WORK_FILES = (
    "README.md", "variation-memo.md", "measure-interpretation.md", "support-suppression-review.md",
    "claim-audit.csv", "handoff-to-module06.md", "reproducibility-check.md", "ai-use.md",
    "progression-decision.md",
)
OUTPUTS = {
    "analysis-checks.csv": (16, 4, 660, "3dabac9212c8a09a4a9c1386739a3f07ab3a776c7628f924e553c1c5a9842753"),
    "build-report.json": (None, None, 1914, "86d76bb049a3b54f83ba692f1c0e514035e5a76d2cd874080a0d9b45d0ed6f62"),
    "care-patterns.csv": (476, 26, 99475, "c5d372e777ff3b190859e7c418b87c4f165776b84fb86346db700fa39f516a6e"),
    "clinical-subgroup-variation.csv": (6, 18, 1660, "1d98c4ea0e9ad29b149dd6a841971343aa2608c499cbde1f3003b83f5185ec10"),
    "exposure-variation.csv": (6, 18, 1788, "1a34057e6632da0c98a04abb774eb9266d55e170429539d55030c733edf74a8d"),
    "measure-summary.csv": (8, 7, 1423, "dfbd2be741cbf92b99bd5b6a29acb1a80589449e2edf4cb44c027cabe33f673e"),
    "record-mix.csv": (30, 7, 5302, "4354f65e4b077e94547dd7434831486cb0ef0de0ec704e8a93b8381318034841"),
    "site-summary.csv": (6, 15, 1642, "f22c4cee9689ccfed38b8cab83f98c65a0785b1b75caf8b88f53535d7991c8bf"),
    "site-variation.csv": (36, 12, 8081, "85c43edd00e0e9094c2197ce441a8b8bc187d48b80b5a58d32c2aa025e3e4f6b"),
    "time-variation.csv": (6, 13, 1361, "d6f2e4f816b90dfab2b7afd0add77f7c6939b9595ffb27fd953143ec05acbf6a"),
    "variation-figure.svg": (None, None, 57545, "c937a8f6bc942e501eab036c64ad4ab63c0fd3c775e78bdf6ad6a385ed9597eb"),
}
SITE_ORDER = ["SITE-A", "SITE-B", "SITE-C", "SITE-D", "SITE-E", "SITE-F"]
SITE_MEASURES = ["M01", "M02", "M04", "M05", "M06", "M10"]
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


def validate(root: Path, starter: bool = False, submission: bool = False) -> dict[str, object]:
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
        expected_files = required | {"workspace-manifest.csv"}
        if not starter:
            expected_files |= {f"outputs/{name}" for name in OUTPUTS}
        actual_files = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
        require(actual_files == expected_files, f"Workspace has exactly {19 if starter else 30} expected files")
        header, manifest = read_csv(root / "workspace-manifest.csv")
        require(header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
        require(len(manifest) == 9 and [row["relative_path"] for row in manifest] == sorted(IMMUTABLE_FILES), "Manifest has nine sorted immutable rows")
        for row in manifest:
            path = root / row["relative_path"]
            require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
            require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {row['relative_path']}")
            require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    source = (root / "source-record.yml").read_text(encoding="utf-8")
    source_values = (
        "commons_release: 0.53.0", "rows: 476", "known_direct_site_effect: zero",
        "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5",
        "e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e",
        "1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a",
    )
    require(all(value in source for value in source_values), "Source identities and synthetic-site provenance match")
    contract = json.loads((root / "variation-contract.json").read_text(encoding="utf-8"))
    require(contract["analysis_id"] == "app1-clinical-variation-v1" and contract["landmark_day"] == 30 and contract["end_day"] == 365, "Analysis identity and timing match")
    require(contract["site_order"] == SITE_ORDER and contract["known_direct_site_effect"] == 0, "Site order and known effect match")
    require(contract["support"] == {"minimum_people": 50, "minimum_numerator": 10, "minimum_complement": 10}, "Support contract matches")
    require(contract["statistics"]["pairwise_site_tests"] == "prohibited" and contract["randomness"] == "none", "Statistical and randomness boundaries match")
    environment = (root / "environment.yml").read_text(encoding="utf-8")
    require(all(value in environment for value in ("python=3.12", "matplotlib=3.10.9", "numpy=2.0.2", "pandas=3.0.3", "scipy=1.17.1")), "Environment versions match")
    assessment = (root / "assessment.md").read_text(encoding="utf-8")
    require("Total | 20.00" in assessment and len(re.findall(r"(?m)^\d+\. ", assessment)) == 18, "Assessment has 20 points and 18 gates")

    measure_header, measures = read_csv(root / "measure-contract.csv")
    require(measure_header == ["measure_id", "label", "role", "source_table", "record_rule", "time_window", "numerator", "denominator", "operational_threshold", "permitted_use", "claim_limit"], "Measure-contract header matches")
    require(len(measures) == 11 and [row["measure_id"] for row in measures] == [f"M{i:02d}" for i in range(1, 12)], "Eleven measures are fixed and ordered")
    measure_by_id = {row["measure_id"]: row for row in measures}
    require(measure_by_id["M04"]["role"] == "treatment_record" and "not dispensing possession ingestion adherence" in measure_by_id["M04"]["claim_limit"], "Medication record cannot become adherence")
    require(measure_by_id["M05"]["record_rule"] == "description equals Medication Reconciliation (procedure)" and measure_by_id["M10"]["operational_threshold"] == "0.05", "Procedure and outcome contracts match")

    text_files = [name for name in required if Path(name).suffix.lower() in {".md", ".json", ".yml", ".csv"}]
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
        print(f"APP-1 Module 05 starter validation passed: {len(checks)} checks.")
        return report

    output_root = root / "outputs"
    require(all((output_root / name).is_file() for name in OUTPUTS), "All eleven outputs are present")
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
    people = tables["care-patterns.csv"]
    require(len({row["patient_id"] for row in people}) == 476 and sum(int(row["event_indicator"]) for row in people) == 87, "Person output conserves 476 people and 87 events")
    require(sum(int(row["landmark_exposure"]) for row in people) == 129 and {row["teaching_site_id"] for row in people} == set(SITE_ORDER), "Exposure and six sites are conserved")
    require(abs(sum(float(row["expected_probability"]) for row in people) - 86.99999984) < 0.00000001, "Rounded expected probabilities reconcile")
    require(all(row["post_landmark_person_days"] == "335" and "not adherence" in row["claim_boundary"] for row in people), "Every person has common time and claim boundary")

    summary = {row["measure_id"]: row for row in tables["measure-summary.csv"]}
    expected_summary = {
        "M01": ("129", "476", "0.27100840"), "M02": ("260", "476", "0.54621849"),
        "M03": ("433", "476", "0.90966387"), "M04": ("279", "476", "0.58613445"),
        "M05": ("143", "476", "0.30042017"), "M06": ("297", "476", "0.62394958"),
        "M10": ("87", "476", "0.18277311"), "M11": ("17", "129", "0.13178295"),
    }
    require(all((summary[key]["numerator"], summary[key]["denominator"], summary[key]["proportion"]) == value for key, value in expected_summary.items()), "Eight measure summaries preserve exact denominators")
    require("not dispensing possession ingestion adherence" in summary["M04"]["claim_limit"] and "not a validated reconciliation rate" in summary["M11"]["claim_limit"], "Treatment and reconciliation limits remain visible")

    exposure = {row["measure_id"]: row for row in tables["exposure-variation.csv"]}
    require(exposure["M03"]["absolute_difference"] == "-0.13129147" and exposure["M03"]["fisher_two_sided_p"] == "0.00003899" and exposure["M03"]["threshold_met"] == "yes", "Later scheduled-care exposure difference matches")
    require(exposure["M04"]["absolute_difference"] == "-0.01713469" and exposure["M04"]["threshold_met"] == "no", "Medication-record exposure difference matches")
    require(exposure["M06"]["absolute_difference"] == "-0.18597949" and exposure["M10"]["interval_excludes_zero"] == "no", "Procedure and outcome exposure evidence matches")
    subgroup = {row["measure_id"]: row for row in tables["clinical-subgroup-variation.csv"]}
    require(subgroup["M10"]["group_one"] == "inpatient" and subgroup["M10"]["absolute_difference"] == "0.32197657" and subgroup["M10"]["lower95"] == "0.18927501", "Clinical-subgroup outcome evidence matches")

    site_rows = tables["site-variation.csv"]
    require([row["measure_id"] for row in site_rows[::6]] == SITE_MEASURES, "Six site measures remain ordered")
    for measure_id in SITE_MEASURES:
        rows = [row for row in site_rows if row["measure_id"] == measure_id]
        require([row["teaching_site_id"] for row in rows] == SITE_ORDER, f"Fixed site order: {measure_id}")
        require(all(row["support_status"] == "report with caution" and row["known_direct_site_effect"] == "0" and row["site_field_class"] == "synthetic_extension" for row in rows), f"Supported synthetic provenance: {measure_id}")
    site_summary = {row["measure_id"]: row for row in tables["site-summary.csv"]}
    site_followup = site_summary["M01"]
    require(site_followup["minimum_site"] == "SITE-E" and site_followup["minimum_proportion"] == "0.22988506" and site_followup["maximum_site"] == "SITE-F" and site_followup["maximum_proportion"] == "0.37804878", "Site follow-up endpoints match")
    require(site_followup["absolute_range"] == "0.14816372" and site_followup["global_p_value"] == "0.27993975" and site_followup["threshold_met"] == "yes", "Site operational and statistical evidence remain separate")

    time_rows = tables["time-variation.csv"]
    require(sum(int(row["person_days"]) for row in time_rows) == 476 * 335, "Time windows conserve all post-landmark person-days")
    time_map = {(row["exposure_group"], row["window"]): row for row in time_rows}
    require(time_map[("scheduled_followup", "days_31_90")]["scheduled_records_per_1000_person_days"] == "19.12144703", "Exposed early scheduled-record rate matches")
    require(time_map[("no_recorded_followup", "days_31_90")]["scheduled_records_per_1000_person_days"] == "14.74543708", "Comparator early scheduled-record rate matches")
    mix = tables["record-mix.csv"]
    descriptions = {row["description"] for row in mix}
    require({"Auscultation of the fetal heart", "Evaluation of uterine fundal height", "Medication Reconciliation (procedure)", "24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet"}.issubset(descriptions), "Record mix keeps heterogeneous clinical pathways visible")

    svg = (output_root / "variation-figure.svg").read_text(encoding="utf-8")
    svg_values = ("SITE-A", "SITE-F", "Synthetic teaching site in fixed order", "not rankings", "global chi-square p = 0.27993975", "site-variation.csv")
    require(all(value in svg for value in svg_values), "Figure has site labels, fixed order, statistical evidence, and exact-table route")
    report_json = json.loads((output_root / "build-report.json").read_text(encoding="utf-8"))
    require(report_json["module"] == "oclc-app1-05" and report_json["commons_release"] == "0.53.0", "Build report identity matches")
    require(report_json["sources"]["database_access"] == "read-only" and report_json["reference_findings"]["known_direct_site_effect"] == 0, "Build report preserves read-only source and zero effect")

    memo = (root / "variation-memo.md").read_text(encoding="utf-8").lower()
    memo_values = ("0.14816372", "0.27993975", "known direct effect is zero", "-0.13129147", "not evidence that early follow-up", "not a validated medication-reconciliation")
    require(all(value in memo for value in memo_values), "Memo has exact evidence and bounded claims")
    interpretation = (root / "measure-interpretation.md").read_text(encoding="utf-8").lower()
    require(all(value in interpretation for value in ("19.12144703", "14.74543708", "not adherence", "1,832", "does not refit")), "Measure interpretation preserves rates, record meaning, and model handoff")
    support = (root / "support-suppression-review.md").read_text(encoding="utf-8").lower()
    require(all(value in support for value in ("site-a through site-f", "report with caution", "four sites", "every site has fewer than 10", "structured alternative", "not a ranking")), "Support review includes suppression and accessible routes")

    claim_header, claims = read_csv(root / "claim-audit.csv")
    require(claim_header == ["claim_id", "draft_claim", "evidence", "decision", "corrected_claim", "reason", "human_owner"] and len(claims) == 6, "Claim audit has six complete rows")
    require([row["claim_id"] for row in claims] == [f"C{i:02d}" for i in range(1, 7)] and sum(row["decision"] == "reject" for row in claims) == 5 and claims[-1]["decision"] == "keep with boundary", "Claim audit decisions match")
    require(all(row["human_owner"] for row in claims), "Every audited claim has a human owner")

    handoff = (root / "handoff-to-module06.md").read_text(encoding="utf-8")
    handoff_fields = ("Bounded variation finding", "Equity question", "Improvement lever", "Simpler analytic benchmark")
    require(all(markdown_field(handoff, label) for label in handoff_fields), "Module 06 handoff has exactly four required decisions")
    require(handoff.count("- Bounded variation finding:") == 1 and handoff.count("- Equity question:") == 1 and handoff.count("- Improvement lever:") == 1 and handoff.count("- Simpler analytic benchmark:") == 1, "Handoff has one of each required item")
    require(markdown_field(handoff, "Module 05 equity conclusion") == "not assessed" and markdown_field(handoff, "Module 05 implementation authorization") == "not authorized", "Module 05 does not preempt equity or authorize implementation")

    reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require(all(value in reproducibility for value in ("two complete builds match byte for byte", "read-only", "changed-database result", "rejected", "randomness: `none`")), "Reproduction and mutation results are complete")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in ai_fields), "AI-use record has every accountable field")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Clinical variation score") == "20.00 of 20.00" and markdown_field(progression, "Gate result") == "18 of 18 pass", "Reference score and gates match")
    require(markdown_field(progression, "Progression") in ALLOWED_PROGRESSION and markdown_field(progression, "Clinical use") == "prohibited", "Progression is allowed and clinical use prohibited")

    mode = "submission" if submission else "complete"
    report = {"status": "pass", "mode": mode, "checks_passed": len(checks), "assembled_files": 30 if not is_source_package else None}
    print(f"APP-1 Module 05 {mode} validation passed: {len(checks)} checks.")
    return report


def rejected(action, expected_message: str) -> None:
    try:
        action()
    except ValidationError as error:
        if expected_message.lower() not in str(error).lower():
            raise AssertionError(f"Expected rejection containing {expected_message!r}, got {error!r}") from error
    else:
        raise AssertionError(f"Expected validation rejection: {expected_message}")


def self_check() -> None:
    from build_workspace import assemble

    with tempfile.TemporaryDirectory(prefix="app1-module05-validator-") as temp_dir:
        root = Path(temp_dir)
        reference, starter = root / "reference", root / "starter"
        assemble(reference, reference=True)
        assemble(starter)
        validate(reference)
        validate(starter, starter=True)

        changed_output = root / "changed-output"
        shutil.copytree(reference, changed_output)
        with (changed_output / "outputs" / "measure-summary.csv").open("a", encoding="utf-8") as handle:
            handle.write("changed\n")
        rejected(lambda: validate(changed_output), "Output bytes match")

        changed_immutable = root / "changed-immutable"
        shutil.copytree(reference, changed_immutable)
        with (changed_immutable / "measure-contract.csv").open("a", encoding="utf-8") as handle:
            handle.write("changed\n")
        rejected(lambda: validate(changed_immutable), "Manifest bytes match")

        incomplete = root / "incomplete"
        shutil.copytree(reference, incomplete)
        (incomplete / "variation-memo.md").write_text("REPLACE\n", encoding="utf-8")
        rejected(lambda: validate(incomplete), "Work file is complete")

        bad_score = root / "bad-score"
        shutil.copytree(reference, bad_score)
        score = (bad_score / "progression-decision.md").read_text(encoding="utf-8").replace("20.00 of 20.00", "19.00 of 20.00")
        (bad_score / "progression-decision.md").write_text(score, encoding="utf-8", newline="\n")
        rejected(lambda: validate(bad_score), "Reference score and gates match")

        bad_progression = root / "bad-progression"
        shutil.copytree(reference, bad_progression)
        text = (bad_progression / "progression-decision.md").read_text(encoding="utf-8").replace("continue with conditions", "deploy")
        (bad_progression / "progression-decision.md").write_text(text, encoding="utf-8", newline="\n")
        rejected(lambda: validate(bad_progression), "Progression is allowed")
    print("APP-1 Module 05 validator self-check passed: complete, starter, output, immutable, placeholder, score, and progression paths tested.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=MODULE_ROOT)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--submission", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.starter and args.submission:
        parser.error("--starter and --submission cannot be combined")
    try:
        if args.self_check:
            self_check()
        else:
            validate(args.root, starter=args.starter, submission=args.submission)
    except (OSError, ValueError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
