"""Validate the APP-3 cumulative Week 6 checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal
from pathlib import Path
from typing import Callable


CHECKPOINT_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (
    ".gitattributes", "VERSION", "checkpoint-contract.json", "assessment.md",
    "instructor-notes.md", "build_checkpoint.py", "validate_checkpoint.py",
)
WORK_FILES = (
    "README.md", "evidence-index.csv", "forecast-scenario-monitoring-review.md",
    "checkpoint-gates.csv", "checkpoint-defense.md", "reproducibility-check.md",
    "ai-use.md", "progression-decision.md", "module07-handoff.md",
)
MODULES = {
    "module-04": {
        "id": "oclc-app3-04", "version": "0.1.0", "commons_release": "0.70.0",
        "files": 59, "immutable_rows": 46, "manifest_bytes": 5946,
        "manifest_sha256": "e462b470ba6aefa83c50bfdbcc21f8ca3be11dcf8e47ef9c377b820b42571f12",
    },
    "module-05": {
        "id": "oclc-app3-05", "version": "0.1.0", "commons_release": "0.71.0",
        "files": 68, "immutable_rows": 53, "manifest_bytes": 6773,
        "manifest_sha256": "2c6cddb2d59ba3e5d3eb67023c68756f9c2cd50144ba7e699fcf1cde8bfc4104",
    },
    "module-06": {
        "id": "oclc-app3-06", "version": "0.1.0", "commons_release": "0.72.0",
        "files": 82, "immutable_rows": 64, "manifest_bytes": 8672,
        "manifest_sha256": "7f81c00961f783c81e3f2b9d77b3a82b7e2d422860efb19e27ae55eb50b9ef85",
    },
}
MANIFEST_BYTES = 36654
MANIFEST_SHA256 = "4f2a303bc5626ea58139aa935da157f524db1d25b5a158a927ef5daec197958a"
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

    required = set(IMMUTABLE_FILES) | set(WORK_FILES) | {"candidate-manifest.csv"}
    require(root.is_dir(), "Checkpoint directory exists")
    manifest_path = root / "candidate-manifest.csv"
    require(manifest_path.is_file(), "Candidate manifest exists")
    require(manifest_path.stat().st_size == MANIFEST_BYTES, "Candidate manifest bytes match")
    require(sha256(manifest_path) == MANIFEST_SHA256, "Candidate manifest SHA-256 matches")
    header, manifest = read_csv(manifest_path)
    require(
        header == ["relative_path", "bytes", "sha256", "source_module", "source_version", "role"],
        "Candidate manifest header matches",
    )
    paths = [row["relative_path"] for row in manifest]
    require(len(manifest) == 209 and paths == sorted(paths) and len(set(paths)) == 209, "Candidate manifest has 209 unique sorted rows")
    require(
        all(path.startswith("candidate/module-0") and "\\" not in path and ".." not in Path(path).parts for path in paths),
        "Candidate paths are portable and bounded",
    )
    expected = required | set(paths)
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == expected and len(actual) == 226, "Checkpoint has exactly 226 expected files")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        directory = row["relative_path"].split("/")[1]
        require(
            directory in MODULES
            and row["source_module"] == MODULES[directory]["id"]
            and row["source_version"] == MODULES[directory]["version"]
            and row["role"] == "accepted reference workspace artifact",
            f"Candidate source identity matches: {row['relative_path']}",
        )

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version matches")
    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(
        contract["checkpoint_id"] == "oclc-app3-cp02"
        and contract["version"] == "0.1.0"
        and contract["commons_release"] == "0.73.0"
        and contract["course_points"] == 25,
        "Checkpoint identity and score match",
    )
    require(
        contract["accepted_component_files"] == 209
        and [module["points"] for module in contract["accepted_modules"]] == [0, 25, 0]
        and sum(module["points"] for module in contract["accepted_modules"]) == 25,
        "Contract carries the 0, 25, 0 point map once",
    )
    require(
        contract["required_gates"] == {
            "module04_forecast": 18, "module05_scenario_evaluation": 20,
            "module06_feasibility_monitoring_ml": 22, "checkpoint_integrity": 20,
        },
        "Contract carries all inherited and checkpoint gates",
    )
    require(
        contract["accepted_decisions"] == {
            "scenario": "none qualifies",
            "scenario_dispositions": {"S00": "retain", "S01": "revise", "S02": "stop", "S03": "revise"},
            "forecast": "seasonal_exponential_smoothing",
            "ml": "retain transparent forecast",
            "progression": "continue with conditions",
        },
        "Contract carries the accepted decisions",
    )
    require(all(value == "prohibited" for value in contract["boundaries"].values()), "Contract preserves all action boundaries")

    for directory, details in MODULES.items():
        module_root = root / "candidate" / directory
        files = [path for path in module_root.rglob("*") if path.is_file() and "__pycache__" not in path.parts]
        require(len(files) == details["files"], f"{directory} file count matches")
        require((module_root / "VERSION").read_text(encoding="utf-8").strip() == details["version"], f"{directory} version matches")
        release = json.loads((module_root / "release.json").read_text(encoding="utf-8"))
        require(
            (release["module_id"], release["module_version"], release["commons_release"])
            == (details["id"], details["version"], details["commons_release"]),
            f"{directory} release identity matches",
        )
        nested = module_root / "release-manifest.csv"
        require(nested.stat().st_size == details["manifest_bytes"], f"{directory} nested manifest bytes match")
        require(sha256(nested) == details["manifest_sha256"], f"{directory} nested manifest SHA-256 matches")
        nested_header, nested_rows = read_csv(nested)
        require(nested_header == ["relative_path", "bytes", "sha256", "role"], f"{directory} nested manifest header matches")
        require(len(nested_rows) == details["immutable_rows"], f"{directory} nested immutable row count matches")
        for row in nested_rows:
            path = module_root / row["relative_path"]
            require(path.is_file() and path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"{directory} nested artifact matches: {row['relative_path']}")

    for name in WORK_FILES:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if learner:
            require(bool(PLACEHOLDER.search(text)), f"Learner prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Reference record is complete: {name}")
    if learner:
        report = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 226}
        print(f"APP-3 Checkpoint 2 learner validation passed: {len(checks)} checks.")
        return report

    index_header, index_rows = read_csv(root / "evidence-index.csv")
    require(
        index_header == [
            "module_id", "title", "version", "commons_release", "assembled_files", "manifest_rows",
            "manifest_bytes", "manifest_sha256", "checkpoint_points", "gates", "progression",
            "accepted_decision", "role",
        ],
        "Evidence index header matches",
    )
    require(len(index_rows) == 3 and [row["module_id"] for row in index_rows] == ["oclc-app3-04", "oclc-app3-05", "oclc-app3-06"], "Evidence index has three ordered modules")
    require([row["checkpoint_points"] for row in index_rows] == ["0", "25", "0"] and sum(Decimal(row["checkpoint_points"]) for row in index_rows) == Decimal("25"), "Evidence index carries 25 points once")
    require([row["gates"] for row in index_rows] == ["18 of 18 pass", "20 of 20 pass", "22 of 22 pass"], "Evidence index carries all inherited passing gates")
    for row, details in zip(index_rows, MODULES.values(), strict=True):
        require(
            row["version"] == details["version"]
            and row["commons_release"] == details["commons_release"]
            and int(row["assembled_files"]) == details["files"]
            and int(row["manifest_rows"]) == details["immutable_rows"]
            and int(row["manifest_bytes"]) == details["manifest_bytes"]
            and row["manifest_sha256"] == details["manifest_sha256"],
            f"Evidence index identity matches: {row['module_id']}",
        )
        require(f"209 rows 36654 bytes SHA-256 {MANIFEST_SHA256}" in row["role"], f"Evidence index carries checkpoint manifest identity: {row['module_id']}")

    review = (root / "forecast-scenario-monitoring-review.md").read_text(encoding="utf-8")
    review_terms = (
        "accepted arrivals per eight-hour shift", "end of the final shift in each completed week", "21 shifts", "Weeks 1 through 24",
        "F01 through F28", "588 exact target rows", "Seasonal exponential smoothing", "5.937283", "7.307180", "0.008215", "15.141268",
        "876.924084", "The empirical actual-equivalent planning range is 805.136639 to 970.733035", "Little's Law equilibrium is not established", "Staffing recommendation is not authorized",
        "S00 through S03", "C01 through C05", "4,000 paired runs", "Six comparisons are null or failed", "No option qualified",
        "21.244986", "1.958703", "5.803341", "41.617987", "86.671644", "0.316383", "14.547388",
        "12 measures and eight threats", "Safety and return within 72 hours were not simulated", "does not establish a causal effect",
        "28 scenario-domain rows", "five supported, 18 require local evidence, and five are not supported",
        "S00 is retained", "S01 must be revised", "S02 is stopped", "S03 must be revised",
        "12 owned measures", "three are prospectively unavailable", "Ten escalation and fallback rules", "zero automatic actions",
        "Continued no-change monitoring", "static accessible planning artifact", "no script", "no live connection",
        "GradientBoostingRegressor", "seed 7300600", "All 12 leakage", "same 28 folds and 588 target rows",
        "5.205494", "6.554934", "-0.513059", "13.275060", "4742.085347", "5234.268116", "9.403087", "860.277096",
        "0.750000", "0.731788", "Seven rules pass and R01 fails", "retain transparent forecast", "Feature importance describes model allocation, not cause",
        "25 points once", "18 Module 04, 20 Module 05, 22 Module 06, and 20 checkpoint gates pass", "continue with conditions",
    )
    require(all(term in review for term in review_terms), "Cumulative review contains exact accepted evidence")
    require(
        not re.search(r"(?i)option selected|safety was simulated|causal effect established|automatic alerting enabled|challenger accepted|staffing recommendation authorized|implementation authorized", review),
        "Cumulative review contains no prohibited decision or authority",
    )

    gates_header, gates = read_csv(root / "checkpoint-gates.csv")
    require(gates_header == ["gate_id", "gate", "status", "evidence", "owner"], "Checkpoint gate header matches")
    require(len(gates) == 20 and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 21)] and all(row["status"] == "pass" for row in gates), "All 20 checkpoint integrity gates pass")

    module04 = root / "candidate/module-04"
    _, module04_gates = read_csv(module04 / "gate-results.csv")
    require(len(module04_gates) == 18 and all(row["status"] == "pass" for row in module04_gates), "Accepted Module 04 has 18 passing gates")
    _, errors = read_csv(module04 / "outputs/error-summary.csv")
    selected = next(row for row in errors if row["selected_flag"] == "1")
    require(
        [selected[key] for key in ("method", "evaluation_rows", "mae_arrivals", "rmse_arrivals", "bias_arrivals", "wape_percent")]
        == ["seasonal_exponential_smoothing", "588", "5.937283", "7.307180", "0.008215", "15.141268"],
        "Accepted Module 04 method and errors match",
    )
    findings04 = json.loads((module04 / "outputs/forecast-findings.json").read_text(encoding="utf-8"))
    require(findings04["week53"]["raw_forecast_arrivals"] == 876.924084, "Accepted Module 04 Week 53 point matches")
    _, little = read_csv(module04 / "outputs/littles-law-check.csv")
    require(len(little) == 4 and all(row["equilibrium_status"] == "not established" for row in little), "Accepted Module 04 Little's Law limit matches")

    module05 = root / "candidate/module-05"
    _, score05 = read_csv(module05 / "week6-score.csv")
    criteria05 = [row for row in score05 if row["criterion_id"] != "TOTAL"]
    total05 = next(row for row in score05 if row["criterion_id"] == "TOTAL")
    require(len(criteria05) == 6 and sum(Decimal(row["points_awarded"]) for row in criteria05) == Decimal("25") and total05["points_awarded"] == "25", "Accepted Module 05 score totals 25 once")
    _, module05_gates = read_csv(module05 / "gate-results.csv")
    require(len(module05_gates) == 20 and all(row["status"] == "pass" for row in module05_gates), "Accepted Module 05 has 20 passing gates")
    findings05 = json.loads((module05 / "outputs/scenario-findings.json").read_text(encoding="utf-8"))
    require(
        findings05["selection"]["selected_option"] == "none"
        and findings05["simulation_contract"]["scenario_runs"] == 4000
        and findings05["sensitivity"]["null_or_failed_rows"] == 6
        and findings05["evaluation"]["measures"] == 12
        and findings05["evaluation"]["threats"] == 8,
        "Accepted Module 05 no-selection and evaluation evidence match",
    )

    module06 = root / "candidate/module-06"
    _, score06 = read_csv(module06 / "week6-score.csv")
    require(
        [row["points_awarded"] for row in score06 if row["criterion_id"] != "TOTAL"] == ["0", "25", "0", "0"]
        and next(row for row in score06 if row["criterion_id"] == "TOTAL")["points_awarded"] == "25",
        "Accepted Module 06 carries the Week 6 score without adding points",
    )
    _, module06_gates = read_csv(module06 / "gate-results.csv")
    require(len(module06_gates) == 22 and all(row["status"] == "pass" for row in module06_gates), "Accepted Module 06 has 22 passing gates")
    _, feasibility = read_csv(module06 / "outputs/feasibility-screen.csv")
    status_counts = {status: sum(row["status"] == status for row in feasibility) for status in {row["status"] for row in feasibility}}
    dispositions = {row["scenario_id"]: row["scenario_disposition"] for row in feasibility}
    require(len(feasibility) == 28 and status_counts == {"supported": 5, "requires local evidence": 18, "not supported": 5}, "Accepted Module 06 feasibility evidence matches")
    require(
        dispositions == {"S00": "retain as monitoring baseline", "S01": "revise before reconsideration", "S02": "stop in current form", "S03": "revise before reconsideration"},
        "Accepted Module 06 scenario dispositions match",
    )
    _, measures = read_csv(module06 / "outputs/monitoring-measures.csv")
    require(len(measures) == 12 and sum(row["value"] == "unavailable" for row in measures) == 3, "Accepted Module 06 has 12 measures and three unavailable values")
    _, escalation = read_csv(module06 / "outputs/escalation-fallback.csv")
    require(len(escalation) == 10 and all(row["automatic_action"] == "0" and row["fallback_state"] == "continue no-change monitoring" for row in escalation), "Accepted Module 06 has ten human-owned rules and no automatic action")
    dashboard = (module06 / "outputs/monitoring-dashboard.html").read_text(encoding="utf-8").lower()
    require("<script" not in dashboard and "cgh-ed-01" in dashboard and "planning" in dashboard and "<table" in dashboard, "Accepted Module 06 dashboard remains static and bounded")
    _, leakage = read_csv(module06 / "outputs/leakage-tests.csv")
    require(len(leakage) == 12 and all(row["status"] == "pass" for row in leakage), "Accepted Module 06 has 12 passing leakage checks")
    _, decision = read_csv(module06 / "outputs/decision-change.csv")
    require(
        len(decision) == 9 and decision[0]["rule_id"] == "R01" and decision[0]["threshold"] == "at least 0.750000 arrivals per shift"
        and decision[0]["observed"] == "0.731788" and decision[0]["status"] == "fail"
        and decision[-1]["decision_effect"] == "retain transparent forecast",
        "Accepted Module 06 retains failed R01 and the transparent forecast",
    )
    report06 = json.loads((module06 / "outputs/build-report.json").read_text(encoding="utf-8"))
    require(report06["common_evaluation_rows"] == 588 and report06["decision_rules_passed"] == 7 and report06["implementation_authorized"] is False, "Accepted Module 06 ML and authority facts match")

    defense = (root / "checkpoint-defense.md").read_text(encoding="utf-8")
    require(re.findall(r"(?m)^## Q(\d{2})\.", defense) == [f"{number:02d}" for number in range(1, 15)], "Checkpoint defense has 14 ordered questions")
    require(
        len(re.findall(r"(?m)^Answer:", defense)) == 14
        and len(re.findall(r"(?m)^Evidence:", defense)) == 14
        and len(re.findall(r"(?m)^Decision consequence:", defense)) == 14
        and len(re.findall(r"(?m)^Limit:", defense)) == 14,
        "Checkpoint defense answers every question with evidence consequence and limit",
    )

    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    reproduction_terms = (
        "209", "36654", MANIFEST_SHA256, "module 04 has 0 points", "module 05 has 25 once", "sum is 25",
        "two independent reference builds match byte for byte", "copied validator", "candidate mutation", "nested-manifest mutation",
        "missing-candidate mutation", "duplicate-point mutation", "wrong-component-point mutation", "module-04-gate mutation",
        "module-05-gate mutation", "module-06-gate mutation", "forecast-method mutation", "forecast-row mutation",
        "forecast-range mutation", "forced-scenario-selection mutation", "hidden-scenario-failure mutation", "invented-safety mutation",
        "changed-disposition mutation", "unavailable-as-zero mutation", "dashboard-boundary mutation", "ml-row mutation",
        "leakage-failure mutation", "moved-r01 mutation", "accepted-challenger mutation", "incomplete-defense mutation",
        "unauthorized-implementation mutation", "placeholder-reference mutation", "invalid-progression mutation", "pending before alpha",
    )
    require(all(term in reproduction for term in reproduction_terms), "Reproducibility record covers assembly and all failure routes")

    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    ai_fields = (
        "Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected",
        "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action",
        "Human owner", "Accountability statement",
    )
    require(all(markdown_field(ai, field) for field in ai_fields), "Responsible agent-use record has every accountable field")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Checkpoint score") == "25 of 25" and markdown_field(progression, "Point source") == "Module 05 25 points once", "Progression score and point source are exact")
    require(
        markdown_field(progression, "Module 04 forecast gates") == "18 of 18 pass"
        and markdown_field(progression, "Module 05 scenario and evaluation gates") == "20 of 20 pass"
        and markdown_field(progression, "Module 06 feasibility monitoring and ML gates") == "22 of 22 pass"
        and markdown_field(progression, "Checkpoint integrity gates") == "20 of 20 pass"
        and markdown_field(progression, "Failed gates") == "none",
        "Progression carries every passing gate total",
    )
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 07 permission")
    require(
        disposition in ALLOWED_PROGRESSION
        and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for clinician leadership, recommendation, and defense")),
        "Module 07 permission matches progression",
    )
    require(
        markdown_field(progression, "Selected scenario") == "none"
        and markdown_field(progression, "Accepted forecast") == "seasonal exponential smoothing"
        and markdown_field(progression, "ML decision") == "retain transparent forecast",
        "Progression carries the accepted analytic decisions",
    )
    prohibited_fields = ("Clinical action", "Staffing change", "Schedule change", "Automated action", "Test start", "Implementation", "Production scoring", "Model deployment")
    require(all(markdown_field(progression, field) == "prohibited" for field in prohibited_fields), "Progression preserves all action boundaries")

    handoff = (root / "module07-handoff.md").read_text(encoding="utf-8")
    handoff_terms = (
        "oclc-app3-cp02", "0.73.0", "209", MANIFEST_SHA256, "25 of 25 from Module 05 once",
        "Joe Joseph, MD", "Selected scenario: `none`", "seasonal exponential smoothing", "S00 retain, S01 revise, S02 stop, S03 revise",
        "12 measures, three prospectively unavailable, and ten human-owned escalation rules", "Automatic actions: `zero`",
        "0.731788 versus required 0.750000", "retain transparent forecast", "may not select an option",
    )
    require(all(term in handoff for term in handoff_terms), "Module 07 handoff carries exact evidence decisions and limits")

    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 226}
    print(f"APP-3 Checkpoint 2 reference validation passed: {len(checks)} checks.")
    return report


def load_builder():
    spec = importlib.util.spec_from_file_location("app3_cp02_builder", CHECKPOINT_ROOT / "build_checkpoint.py")
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load checkpoint builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def self_check() -> None:
    builder = load_builder()

    def replace(path: Path, old: str, new: str) -> None:
        text = path.read_text(encoding="utf-8")
        if old not in text:
            raise AssertionError(f"Mutation source not found in {path.name}: {old}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")

    def append(path: Path) -> None:
        with path.open("ab") as handle:
            handle.write(b"\nmutation")

    def remove(path: Path) -> None:
        path.unlink()

    with tempfile.TemporaryDirectory(prefix="app3-cp02-validator-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        learner = base / "learner"
        first = builder.assemble(reference, reference=True)
        second_path = base / "reference-2"
        second = builder.assemble(second_path, reference=True)
        builder.assemble(learner)
        assert first == second
        complete = validate(reference)
        starter = validate(learner, learner=True)
        copied = subprocess.run(
            [sys.executable, "validate_checkpoint.py", "."], cwd=reference,
            capture_output=True, text=True, check=False,
        )
        assert copied.returncode == 0, copied.stdout + copied.stderr

        routes: list[tuple[str, Callable[[Path], None]]] = [
            ("candidate", lambda root: append(root / "candidate/module-04/outputs/error-summary.csv")),
            ("nested-manifest", lambda root: append(root / "candidate/module-05/release-manifest.csv")),
            ("missing-candidate", lambda root: remove(root / "candidate/module-06/outputs/build-report.json")),
            ("duplicate-point", lambda root: replace(root / "evidence-index.csv", "oclc-app3-06,Feasibility", "oclc-app3-05,Feasibility")),
            ("wrong-component-point", lambda root: replace(root / "evidence-index.csv", ",25,20 of 20", ",24,20 of 20")),
            ("module-04-gate", lambda root: replace(root / "candidate/module-04/gate-results.csv", ",pass\nG18", ",fail\nG18")),
            ("module-05-gate", lambda root: replace(root / "candidate/module-05/gate-results.csv", ",pass\nG20", ",fail\nG20")),
            ("module-06-gate", lambda root: replace(root / "candidate/module-06/gate-results.csv", "G22,reproducibility and responsible AI complete,pass", "G22,reproducibility and responsible AI complete,fail")),
            ("forecast-method", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "Seasonal exponential smoothing remains accepted", "Last value remains accepted")),
            ("forecast-row", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "588 exact target rows", "587 exact target rows")),
            ("forecast-range", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "805.136639 to 970.733035", "800 to 975")),
            ("forced-scenario-selection", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "No option qualified", "S01 qualified")),
            ("hidden-scenario-failure", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "Six comparisons are null or failed", "All comparisons pass")),
            ("invented-safety", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "Safety and return within 72 hours were not simulated", "Safety and return within 72 hours were simulated")),
            ("changed-disposition", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "S02 is stopped", "S02 is retained")),
            ("unavailable-as-zero", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "three are prospectively unavailable", "three are zero")),
            ("dashboard-boundary", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "no live connection", "a live connection")),
            ("ml-row", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "same 28 folds and 588 target rows", "same 28 folds and 600 target rows")),
            ("leakage-failure", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "All 12 leakage", "Eleven of 12 leakage")),
            ("moved-r01", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "0.750000", "0.700000")),
            ("accepted-challenger", lambda root: replace(root / "forecast-scenario-monitoring-review.md", "retain transparent forecast", "accept challenger")),
            ("incomplete-defense", lambda root: replace(root / "checkpoint-defense.md", "Decision consequence: Module 07 must discuss", "Consequence: Module 07 must discuss")),
            ("unauthorized-implementation", lambda root: replace(root / "progression-decision.md", "- Implementation: `prohibited`", "- Implementation: `authorized`")),
            ("placeholder-reference", lambda root: replace(root / "ai-use.md", "- Human owner: `Shuhan He and the named APP-3 faculty owner`", "- Human owner: `REPLACE`")),
            ("invalid-progression", lambda root: replace(root / "progression-decision.md", "permitted for clinician leadership, recommendation, and defense", "not permitted")),
        ]
        for name, mutate in routes:
            target = base / f"mutation-{name}"
            shutil.copytree(reference, target)
            mutate(target)
            try:
                validate(target)
            except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError):
                pass
            else:
                raise AssertionError(f"Validator accepted {name} mutation")
        try:
            validate(learner)
        except ValidationError as error:
            assert "Reference record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted learner prompts as a reference")

    print(
        f"APP-3 Checkpoint 2 validator self-check passed: {complete['checks_passed']} reference checks "
        f"and {starter['checks_passed']} learner checks; copied validation and {len(routes)} failure routes verified."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path)
    parser.add_argument("--learner", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.checkpoint:
            validate(args.checkpoint, learner=args.learner)
        else:
            parser.error("checkpoint is required unless --self-check is used")
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ImportError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
