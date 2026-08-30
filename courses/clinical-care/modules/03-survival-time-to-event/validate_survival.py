"""Validate APP-1 Module 03 survival workspaces."""

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
    ".gitattributes", "VERSION", "source-record.yml", "analysis-contract.json", "environment.yml",
    "assessment.md", "build_survival.py", "validate_survival.py", "paired-survival.R",
)
WORK_FILES = (
    "README.md", "survival-interpretation.md", "ph-assessment.md", "competing-events-note.md",
    "accessibility-review.md", "reproducibility-check.md", "ai-use.md", "progression-decision.md",
)
OUTPUTS = {
    "analysis-checks.csv": (15, 4, 508, "a297438fe7aa70a70b1ad86f0c86c1f1a3df7fad8fa5925545986afcea83d64c"),
    "build-report.json": (None, None, 5788, "b5ba4b8dcb522f2fe814e22a1c1a2357849e121a91ae1c7a52a905b2b302cfaa"),
    "cohort-summary.csv": (3, 7, 207, "ce12ebae8ca15b413b9431e7092e0fb8cea161609f2848e685de2becc318586f"),
    "cox-model.csv": (1, 13, 326, "b0aa566c805ffc88d6c615fe22e17a11b0d9f7df632dfb94b88b3f9a2a8f79c7"),
    "death-audit.csv": (3, 7, 494, "811cf9c23306632b4df345a6623ea77c2c4b23e6fab3a478b2b905806b61b0f1"),
    "fixed-time-comparison.csv": (6, 10, 1219, "14b82733b12644151bc5030e02426bda62acc4bb091b03622cf47c741d5a7c23"),
    "km-curve.svg": (None, None, 50390, "88d4948a44ae548f518196965480e457253505891f23c1c7ea1271ad6862f904"),
    "km-event-table.csv": (84, 12, 9356, "a67cade7a9fb2d364a0c2061dbcc6865bcb055ee64813428a295a7ebda2ef5b7"),
    "km-risk-table.csv": (12, 12, 1297, "e79bef64e8ca9be0d0c3c5015aee5b9d4e08e8edf5b60994cd6e6e5faec4297c"),
    "logrank.csv": (1, 10, 282, "2cfd217834c35af550a579a0423596520c36d7211a8f73e01bf3295e4d04994f"),
    "ph-check.csv": (1, 8, 337, "419acb2d8e7107f7d36e749618cee7e9dc7cc26afe336eb58e439c1fcfc9465e"),
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
        require(actual == expected, f"Workspace has exactly {18 if starter else 29} expected files")
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
    require("commons_release: 0.51.0" in source and "people: 476" in source and "events: 87" in source, "Source identity and counts match")
    require("558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5" in source, "Upstream cohort fingerprint matches")
    contract = json.loads((root / "analysis-contract.json").read_text(encoding="utf-8"))
    require(contract["analysis_id"] == "app1-survival-v1" and contract["fixed_times_days"] == [0, 30, 90, 180, 270, 335], "Analysis contract and fixed times match")
    require(contract["cox_model"] == {"predictors": ["landmark_exposure"], "ties": "efron", "adjusted": False}, "Cox contract is exposure-only and unadjusted")
    environment = (root / "environment.yml").read_text(encoding="utf-8")
    require(all(value in environment for value in ("matplotlib=3.10.9", "numpy=2.0.2", "pandas=3.0.3", "scipy=1.17.1", "statsmodels=0.14.6", "r-survival")), "Environment versions and R route match")
    assessment = (root / "assessment.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\d+\. ", assessment)) == 16, "Assessment has 16 gates")

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
        report = {"status": "pass", "mode": "starter", "checks_passed": len(checks), "assembled_files": 18}
        print(f"APP-1 Module 03 starter validation passed: {len(checks)} checks.")
        return report

    output_root = root / "outputs"
    require(all((output_root / name).is_file() for name in OUTPUTS), "All eleven outputs are present")
    tables = {}
    for name, (expected_rows, expected_fields, expected_bytes, expected_hash) in OUTPUTS.items():
        path = output_root / name
        require(path.stat().st_size == expected_bytes, f"Output bytes match: {name}")
        require(sha256(path) == expected_hash, f"Output SHA-256 matches: {name}")
        if path.suffix == ".csv":
            header, rows = read_csv(path)
            require(len(rows) == expected_rows and len(header) == expected_fields, f"Output shape matches: {name}")
            tables[name] = rows
    require(all(row["status"] == "pass" for row in tables["analysis-checks.csv"]), "All 15 cohort checks pass")
    summary = {row["group"]: row for row in tables["cohort-summary.csv"]}
    require((summary["scheduled_followup"]["people"], summary["scheduled_followup"]["events"]) == ("129", "25"), "Scheduled-follow-up support is 129 people and 25 events")
    require((summary["no_recorded_followup"]["people"], summary["no_recorded_followup"]["events"]) == ("347", "62"), "No-follow-up support is 347 people and 62 events")
    events = tables["km-event-table.csv"]
    require(sum(int(row["events_at_time"]) for row in events) == 87 and sum(int(row["censored_at_time"]) for row in events) == 389, "Event-time table conserves 87 events and 389 censors")
    require(all(0 <= float(row["lower95"]) <= float(row["km_event_free_probability"]) <= float(row["upper95"]) <= 1 for row in events), "Every Kaplan-Meier interval is ordered and bounded")
    risks = tables["km-risk-table.csv"]
    require({int(row["time_days"]) for row in risks} == {0, 30, 90, 180, 270, 335} and len(risks) == 12, "Risk table has both groups at all six times")
    require(all(int(row["at_risk_before"]) >= int(row["cumulative_events"]) for row in risks), "Risk-table counts are nonnegative and coherent")
    fixed = {row["time_days"]: row for row in tables["fixed-time-comparison.csv"]}
    require(fixed["30"]["event_free_difference_exposed_minus_unexposed"] == "0.01242097" and fixed["180"]["event_free_difference_exposed_minus_unexposed"] == "-0.03469383" and fixed["335"]["event_free_difference_exposed_minus_unexposed"] == "-0.01512410", "Fixed-time differences match")
    logrank = tables["logrank.csv"][0]
    require(logrank["chi_square"] == "0.17859356" and logrank["p_value"] == "0.67258471", "Log-rank result matches")
    cox = tables["cox-model.csv"][0]
    require(cox["hazard_ratio"] == "1.10542457" and cox["lower95"] == "0.69479700" and cox["upper95"] == "1.75873453", "Cox result matches")
    ph = tables["ph-check.csv"][0]
    require(ph["correlation"] == "0.29040504" and ph["p_value"] == "0.00636020" and ph["screen_result"] == "fail", "PH screen fails with exact evidence")
    deaths = tables["death-audit.csv"]
    require(len(deaths) == 3 and all(row["later_death_before_event_flag"] == "0" and row["relation"] == "death_after_first_later_acute_return" for row in deaths), "All three later deaths occur after event")
    svg = (output_root / "km-curve.svg").read_text(encoding="utf-8")
    require("Event-free probability" in svg and "Synthetic teaching cohort" in svg, "SVG labels and source note are present")
    report_json = json.loads((output_root / "build-report.json").read_text(encoding="utf-8"))
    require(report_json["module"] == "oclc-app1-03" and report_json["commons_release"] == "0.51.0", "Build report identity matches")
    require(report_json["source"]["sha256"] == "558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5", "Build report source matches")

    interpretation = (root / "survival-interpretation.md").read_text(encoding="utf-8").lower()
    require(all(value in interpretation for value in ("0.67258471", "1.10542457", "0.00636020", "not a probability", "not a causal effect")), "Interpretation contains exact evidence and quantity boundaries")
    ph_text = (root / "ph-assessment.md").read_text(encoding="utf-8").lower()
    require("result: `fail`" in ph_text and "not the main" in ph_text and "module 04" in ph_text, "PH response is explicit")
    death_text = (root / "competing-events-note.md").read_text(encoding="utf-8").lower()
    require("three" in death_text and "does not prove independent censoring" in death_text, "Death and censoring boundary is explicit")
    access = (root / "accessibility-review.md").read_text(encoding="utf-8").lower()
    require("line style" in access and "structured alternative" in access and "km-risk-table.csv" in access, "Accessibility review names visual and structured routes")
    reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require("two complete builds match byte for byte" in reproducibility and "execution awaits" in reproducibility, "Reproduction and R status are honest")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Carried Week 3 score") == "20.00 of 20.00", "Carried score is exact")
    require(markdown_field(progression, "Survival gate result") == "16 of 16 pass", "All survival gates pass")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 04 permission")
    require(disposition in ALLOWED_PROGRESSION, "Progression value is allowed")
    require((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction"), "Module 04 permission matches progression")
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) >= 8, "Progression has eight owned conditions")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in ai_fields), "AI-use record has every accountable field")
    report = {"status": "pass", "mode": "complete", "checks_passed": len(checks), "assembled_files": 29}
    print(f"APP-1 Module 03 complete validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app1-module03-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, starter = base / "reference", base / "starter"
        build_workspace.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_survival.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_workspace.assemble(starter)
        learner = validate(starter, starter=True)
        try:
            validate(starter)
        except ValidationError as error:
            assert "exactly 29 expected files" in str(error)
        else:
            raise AssertionError("Validator accepted an incomplete starter")
        broken = base / "broken"
        shutil.copytree(reference, broken)
        path = broken / "outputs/ph-check.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("0.00636020", "0.60000000", 1), encoding="utf-8", newline="\n")
        try:
            validate(broken)
        except ValidationError as error:
            assert "Output SHA-256 matches" in str(error)
        else:
            raise AssertionError("Validator accepted a changed output")
        bad = base / "bad-progression"
        shutil.copytree(reference, bad)
        path = bad / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("continue with conditions", "deploy", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad)
        except ValidationError as error:
            assert "Progression value is allowed" in str(error)
        else:
            raise AssertionError("Validator accepted an invalid progression")
    print(f"APP-1 Module 03 validator self-check passed: {complete['checks_passed']} complete checks and {learner['checks_passed']} starter checks; copied, incomplete, and broken routes verified.")


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
