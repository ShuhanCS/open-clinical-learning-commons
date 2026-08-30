"""Validate an APP-3 Module 03 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


PLACEHOLDER = re.compile(r"\b(?:REPLACE|TODO|TBD)\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
URL = re.compile(r"https?://")
UNSAFE_CLAIM = re.compile(r"(?i)(signal proves cause|recommend (?:adding|hiring|increasing) staff|staffing should|implement now|(?:language|mobility) group proves inequity)")
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


def field(text: str, label: str) -> str | None:
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    import build_diagnostic
    import build_workspace
    import freeze_upstream

    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    immutable = build_workspace.CONTROL_FILES + build_workspace.UPSTREAM_FILES
    if not starter:
        immutable += build_workspace.OUTPUT_FILES
    expected = set(immutable) | set(build_workspace.RECORD_FILES) | {"release-manifest.csv"}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    expected_files = 41 if starter else 54
    expected_manifest = 27 if starter else 40
    require(root.is_dir(), "Workspace directory exists")
    require(actual == expected and len(actual) == expected_files, f"Workspace has exactly {expected_files} expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "diagnostic-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app3-03", "version": "0.1.0", "commons_release": "0.68.0", "hours": 16.5, "course_points": 20}, "Module identity and workload match")
    require(contract["upstream"] == {"module_id": "oclc-app3-02", "module_version": "0.1.0", "commons_release": "0.67.0", "files": 14, "accepted_encounters": 43628, "query_checks": 30}, "Module 02 handoff contract matches")
    require(contract["phases"] == {"baseline_weeks": [1, 24], "evaluation_weeks": [25, 52], "target_weeks": [35, 44], "target_shift": "evening", "recovery_weeks": [45, 52]}, "Diagnostic phases match")
    require(contract["diagnostic"] == {"charts": 4, "signal_rules": 3, "signal_records": 9, "outputs": 13, "stage": "roomed_to_clinician", "target_stage_median_minutes": 66.0, "root_cause_status": "not established"}, "Diagnostic contract matches")

    header, manifest = read_csv(root / "release-manifest.csv")
    require(header == ["relative_path", "bytes", "sha256", "role"], "Manifest header matches")
    require(len(manifest) == expected_manifest and [row["relative_path"] for row in manifest] == sorted(immutable), f"Manifest has {expected_manifest} sorted rows")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Manifest path is portable: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"Manifest identity matches: {row['relative_path']}")

    handoff = freeze_upstream.verify(root)
    require(handoff == {"files": 14, "module02_version": "0.1.0", "accepted_encounters": 43628, "query_checks": 30}, "Module 02 handoff reproduces")

    record_text = ""
    for relative in build_workspace.RECORD_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        record_text += "\n" + text
        if not starter:
            require(not PLACEHOLDER.search(text), f"Submission record is complete: {relative}")
    if starter:
        require(PLACEHOLDER.search(record_text) is not None, "Starter contains explicit learner placeholders")
        require(not any(path.startswith("outputs/") for path in actual), "Starter contains no accepted diagnostic outputs")
    else:
        require(URL.search(record_text) is None, "Learner records contain no public-to-synthetic link")
        require(UNSAFE_CLAIM.search(record_text) is None, "Learner records contain no unsafe causal, staffing, equity, or implementation claim")

    csv_contracts = (
        ("process-map.csv", ["step_id", "sequence", "state", "owner", "handoff_from", "handoff_to", "clock_role", "rework_capture_status", "failure_branch", "diagnostic_use"], "P", 6),
        ("chart-selection.csv", ["chart_id", "measure", "chart_family", "unit", "denominator_or_exposure", "baseline", "limit_method", "signal_rules", "selection_reason", "known_limit", "owner"], "C", 4),
        ("signal-rules.csv", ["rule_id", "rule", "eligible_charts", "signal_point", "review_action", "causal_status", "automation_status"], "R", 3),
        ("week3-score.csv", ["criterion_id", "criterion", "points_available", "points_awarded", "evidence"], "R", 6),
        ("gate-results.csv", ["gate_id", "gate", "status", "evidence", "owner"], "G", 18),
    )
    records: dict[str, list[dict[str, str]]] = {}
    for filename, expected_header, prefix, count in csv_contracts:
        current_header, rows = read_csv(root / filename)
        records[filename] = rows
        require(current_header == expected_header, f"{filename} header matches")
        expected_ids = [f"{prefix}{index:02d}" for index in range(1, count + 1)]
        if filename == "week3-score.csv":
            expected_ids = ["R01", "R02", "R03", "R04", "R05", "TOTAL"]
        elif filename == "signal-rules.csv":
            expected_ids = ["R1", "R2", "R3"]
        require([row[current_header[0]] for row in rows] == expected_ids, f"{filename} has {count} ordered rows")
        if not starter:
            require(all(all(row[column].strip() for column in current_header) for row in rows), f"Every {filename} field is complete")

    require([int(row["sequence"]) for row in records["process-map.csv"]] == list(range(1, 7)), "Process map has six ordered states")
    if not starter:
        chart_families = {row["chart_id"]: row["chart_family"] for row in records["chart-selection.csv"]}
        require(chart_families == {"C01": "p-chart", "C02": "XmR", "C03": "exact Poisson u-chart", "C04": "run chart"}, "Chart families match the predeclared contract")
        require([row["baseline"] for row in records["chart-selection.csv"]] == ["Weeks 1-24", "Weeks 1-24", "Weeks 1-24", "Weeks 1-24 median"], "Every chart uses the declared baseline")
        require("exact 0.00135 and 0.99865 Poisson count quantiles" in records["chart-selection.csv"][2]["limit_method"], "Low-count u-chart rule is exact")
        require([row["rule_id"] for row in records["signal-rules.csv"]] == ["R1", "R2", "R3"], "Three signal rules are predeclared")
        require(all(row["causal_status"] == "does not prove cause" and row["automation_status"] == "no automated action" for row in records["signal-rules.csv"]), "Signals do not prove cause or automate action")
        score = records["week3-score.csv"]
        require(sum(int(row["points_awarded"]) for row in score[:5]) == 20 and score[-1]["points_awarded"] == "20", "Reference score is 20 of 20")
        require(all(row["status"] == "pass" for row in records["gate-results.csv"]), "All 18 noncompensable gates pass")

        diagnostic = (root / "performance-diagnostic.md").read_text(encoding="utf-8")
        require(field(diagnostic, "Baseline") == "Weeks 1 through 24" and field(diagnostic, "Evaluation") == "Weeks 25 through 52", "Diagnostic phases are exact")
        require(field(diagnostic, "Stage") == "roomed-to-clinician" and field(diagnostic, "Scope") == "evening shifts in Weeks 35 through 44", "Bounded diagnosis scope is exact")
        require(field(diagnostic, "Root cause") == "not established" and field(diagnostic, "Staffing change") == "not authorized", "Root cause and staffing remain unestablished")
        for phrase in ("97.636958", "90.485606", "104.788311", "Weeks 4 through 11", "49 minutes", "66 minutes"):
            require(phrase in diagnostic, f"Performance diagnostic includes: {phrase}")

        safety = (root / "safety-interpretation.md").read_text(encoding="utf-8")
        for phrase in ("39,975", "894", "673", "358", "379", "75.2796", "40.0447", "99.0302", "Weeks 33 through 42"):
            require(phrase in safety, f"Safety interpretation includes: {phrase}")
        subgroup = (root / "subgroup-support-interpretation.md").read_text(encoding="utf-8")
        require("401, not supported" in subgroup and "242, not supported" in subgroup and "2,308, supported" in subgroup, "Target-window subgroup support is exact")
        escalation = (root / "escalation-rule.md").read_text(encoding="utf-8")
        require(field(escalation, "Reference trigger point") == "Week 44" and field(escalation, "Action") == "open human clinical, flow, access, and safety review within one business day", "Human escalation rule is exact")
        for label in ("Automated staffing", "Automated scheduling or routing", "Clinical action", "Implementation"):
            require(field(escalation, label) == "prohibited", f"{label} remains prohibited")

        progression = (root / "progression-decision.md").read_text(encoding="utf-8")
        value = field(progression, "Progression")
        permission = field(progression, "Week 3 checkpoint permission")
        require(value in ALLOWED_PROGRESSION, "Progression value is allowed")
        require((value in {"continue", "continue with conditions"}) == (permission == "permitted for curriculum construction"), "Week 3 checkpoint permission matches progression")
        require(field(progression, "Module 04 permission") == "not yet; Week 3 checkpoint must accept the frozen package first", "Module 04 waits for checkpoint acceptance")
        require(len([line for line in progression.splitlines() if re.match(r"^\| O\d{2} \|", line)]) == 8, "Eight checkpoint conditions have owners")

        findings = json.loads((root / "outputs/diagnostic-findings.json").read_text(encoding="utf-8"))
        require(findings["control_charts"] == {"arrival_run_median": 853.0, "incident_u_center_per_1000": 9.895751, "p_chart_center_percent": 8.13767, "signal_records": 9, "xmr_center_minutes": 97.636958, "xmr_lower_minutes": 90.485606, "xmr_moving_range_mean": 2.688478, "xmr_upper_minutes": 104.788311}, "Control-chart findings match")
        require(all(findings["expected_signal_recovery"].values()), "Expected evaluation and caution signals recover")
        require(findings["bounded_diagnosis"]["baseline_median_minutes"] == 49.0 and findings["bounded_diagnosis"]["target_median_minutes"] == 66.0 and findings["bounded_diagnosis"]["recovery_median_minutes"] == 49.0, "Stage diagnosis and recovery match")
        require(findings["safety"] == {"incident_capture_percent": 40.0447, "incident_true_positives": 358, "known_true_events": 894, "temporal_incident_signal_status": "no exact Poisson limit breach", "trigger_false_positives": 379, "trigger_sensitivity_percent": 75.2796, "trigger_specificity_percent": 99.0302, "trigger_true_positives": 673}, "Safety findings match")
        require(findings["subgroup"] == {"full_release_supported_groups": 3, "target_window_claim_status": "not supported", "target_window_supported_groups": 1}, "Subgroup support findings match")

        output_shapes = {
            "variation-series.csv": 208, "control-limits.csv": 4, "signal-audit.csv": 9,
            "weekly-safety.csv": 52, "safety-surveillance.csv": 6,
            "process-stage-comparison.csv": 20, "bottleneck-reconciliation.csv": 8,
            "subgroup-window-support.csv": 6,
        }
        for filename, count in output_shapes.items():
            _, rows = read_csv(root / f"outputs/{filename}")
            require(len(rows) == count, f"{filename} has {count} rows")
        for filename in ("weekly-arrival-to-clinician-xmr.svg", "weekly-left-before-seen-p-chart.svg", "weekly-incident-report-u-chart.svg", "process-stage-comparison.svg"):
            svg = (root / f"outputs/{filename}").read_text(encoding="utf-8")
            require('role="img"' in svg and "<title" in svg and "<desc" in svg, f"{filename} has accessible SVG structure")
            require("\u2013" not in svg and "\u2014" not in svg, f"{filename} uses plain ASCII dashes")
        require("S = predeclared signal" in (root / "outputs/weekly-arrival-to-clinician-xmr.svg").read_text(encoding="utf-8"), "Signal chart does not rely on color alone")
        r_code = (root / "verify_control_charts.R").read_text(encoding="utf-8")
        require("stopifnot" in r_code and "97.63695833333333" in r_code and "104.78831050724637" in r_code, "Base-R cross-check records exact expectations")

        committed = build_diagnostic.verify_committed(root)
        require(committed == {"outputs": 13, "signal_records": 9, "target_stage_median": 66.0}, "Committed diagnostic outputs match")
        with tempfile.TemporaryDirectory(prefix="app3-module03-validate-") as temp_dir:
            regenerated = Path(temp_dir) / "outputs"
            build_diagnostic.build(root, regenerated)
            for relative in build_workspace.OUTPUT_FILES:
                name = Path(relative).name
                require((regenerated / name).read_bytes() == (root / relative).read_bytes(), f"Regenerated output matches: {name}")

    report = {
        "status": "pass", "mode": "starter" if starter else "complete",
        "checks_passed": len(checks), "assembled_files": expected_files,
        "manifest_rows": expected_manifest, "module03_points": 0 if starter else 20,
        "week3_points": 0 if starter else 40,
    }
    print(f"APP-3 Module 03 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path, starter: bool = False) -> None:
    try:
        validate(root, starter=starter)
    except (OSError, ValueError, KeyError, RuntimeError):
        return
    raise AssertionError("Validator accepted an invalid workspace")


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app3-module03-validator-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)

        names = (
            "upstream-change", "missing-upstream", "changed-baseline", "wrong-chart",
            "changed-limit", "missing-low-count", "signal-cause", "staffing-claim",
            "unsupported-subgroup", "changed-diagnosis", "wrong-score", "failed-gate",
            "bad-progression", "missing-record",
        )
        cases = {}
        for name in names:
            target = base / name
            shutil.copytree(reference, target)
            cases[name] = target
        path = cases["upstream-change"] / "upstream/weekly-metrics.csv"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
        (cases["missing-upstream"] / "upstream/safety-events.csv.gz").unlink()
        path = cases["changed-baseline"] / "chart-selection.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("Weeks 1-24", "Weeks 2-24", 1), encoding="utf-8")
        path = cases["wrong-chart"] / "chart-selection.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("C01,weekly left before seen,p-chart", "C01,weekly left before seen,XmR", 1), encoding="utf-8")
        path = cases["changed-limit"] / "outputs/control-limits.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("97.636958", "97.000000", 1), encoding="utf-8")
        path = cases["missing-low-count"] / "chart-selection.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("exact 0.00135 and 0.99865 Poisson count quantiles", "normal limits", 1), encoding="utf-8")
        for name, phrase in (("signal-cause", "The signal proves cause."), ("staffing-claim", "We recommend adding staff."), ("unsupported-subgroup", "The language group proves inequity.")):
            with (cases[name] / "performance-diagnostic.md").open("a", encoding="utf-8") as handle:
                handle.write(f"\n{phrase}\n")
        path = cases["changed-diagnosis"] / "performance-diagnostic.md"
        path.write_text(path.read_text(encoding="utf-8").replace("- Stage: `roomed-to-clinician`", "- Stage: `triage-to-roomed`", 1), encoding="utf-8")
        path = cases["wrong-score"] / "week3-score.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("R01,Chart selection and exact limits,4,4,", "R01,Chart selection and exact limits,4,3,"), encoding="utf-8")
        path = cases["failed-gate"] / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8")
        path = cases["bad-progression"] / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("continue with conditions", "advance anyway", 1), encoding="utf-8")
        (cases["missing-record"] / "process-map.csv").unlink()
        for target in cases.values():
            expect_failure(target)
        expect_failure(starter)
        assert complete_report["module03_points"] == 20 and complete_report["week3_points"] == 40
        assert starter_report["module03_points"] == 0
    print("APP-3 Module 03 validator self-check passed: reference, starter, and fifteen failure routes checked.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            print(json.dumps(validate(args.workspace.resolve(), starter=args.starter), indent=2))
        else:
            parser.error("workspace is required")
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
