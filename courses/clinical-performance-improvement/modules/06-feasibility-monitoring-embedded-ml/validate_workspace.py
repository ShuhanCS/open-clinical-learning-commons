"""Validate an APP-3 Module 06 learner or reference workspace."""

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
UNSAFE_CLAIM = re.compile(
    r"(?i)(implementation authority:\s*`?authorized|option ready for implementation:\s*`?S0[1-3]|"
    r"safety (?:is|was) established|feature importance proves|model decision:\s*`?(?:accept|deploy) gradient|"
    r"clinical routing authority:\s*`?authorized)"
)
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


def validate(root: Path, starter: bool = False, regenerate: bool = True) -> dict[str, object]:
    import build_evidence
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
    expected_files = 63 if starter else 82
    expected_manifest = 45 if starter else 64
    require(root.is_dir(), "Workspace directory exists")
    require(actual == expected and len(actual) == expected_files, f"Workspace has exactly {expected_files} expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "ml-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {
        "id": "oclc-app3-06", "version": "0.1.0", "commons_release": "0.72.0",
        "hours": 16.0, "application_hours": 8.0, "machine_learning_hours": 8.0,
        "course_points_added": 0, "week6_points": 25,
    }, "Module identity, hours, and point accounting match")
    require(contract["upstream"] == {
        "forecast_module": "oclc-app3-04@0.1.0+commons.0.70.0",
        "scenario_module": "oclc-app3-05@0.1.0+commons.0.71.0",
        "selected_option": "none", "implementation_authorized": False,
    }, "Upstream decision and authority match")
    require(contract["comparison"]["target"] == "accepted arrivals per eight-hour shift" and contract["comparison"]["folds"] == 28 and contract["comparison"]["evaluation_rows"] == 588, "Target, folds, and common rows match")
    require(contract["features"]["complete_week_means_only"] is True and contract["features"]["training_fold_preprocessing_only"] is True and "synthetic_special_event_flag" in contract["features"]["excluded"], "Feature and preprocessing boundaries match")
    require(contract["model"] == {
        "loss": "squared_error", "n_estimators": 100, "learning_rate": 0.05,
        "max_depth": 2, "min_samples_leaf": 15, "max_features": None,
        "random_state": 7300600, "nonnegative_floor": 0, "tuning": "prohibited",
    }, "Fixed untuned challenger matches")
    require(contract["assessment"] == {
        "noncompensable_gates": 22, "course_points_awarded_here": 0,
        "week6_points_counted_once": 25, "next_module": "oclc-app3-07",
    }, "Assessment and Module 07 handoff match")

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
    require(handoff == {
        "files": 33, "forecast_rows": 588, "shift_rows": 1092,
        "monitoring_measures": 12, "module05_points": 25, "selected_option": "none",
    }, "Module 04 and 05 handoff reproduces")

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
        require(not any(path.startswith("outputs/") for path in actual), "Starter contains no accepted Module 06 outputs")
    else:
        require(UNSAFE_CLAIM.search(record_text) is None, "Learner records contain no unsupported option, safety, ML, clinical, or implementation claim")

        feasibility_text = (root / "feasibility-review.md").read_text(encoding="utf-8")
        require(field(feasibility_text, "Option ready for implementation") == "none" and field(feasibility_text, "Implementation authority") == "not authorized", "No option or implementation is forced through")
        require(field(feasibility_text, "S00 disposition") == "retain as monitoring baseline" and field(feasibility_text, "S01 disposition") == "revise before reconsideration" and field(feasibility_text, "S02 disposition") == "stop in current form" and field(feasibility_text, "S03 disposition") == "revise before reconsideration", "All four dispositions match")
        require("40.000000" in feasibility_text and "25.220413" in feasibility_text and "new scenario contract" in feasibility_text, "Resource evidence and return condition remain visible")

        safety = (root / "quality-safety-review.md").read_text(encoding="utf-8")
        require(field(safety, "Safety outcome status") == "not simulated; prospective measurement required" and field(safety, "Return within 72 hours status") == "not simulated; prospective measurement required", "Safety and return outcomes remain prospective")
        require(field(safety, "Clinical routing authority") == "not authorized" and "60.084398" in safety, "Clinical authority and high-acuity rule match")
        access = (root / "access-equity-review.md").read_text(encoding="utf-8")
        require("0.000000" in access and "0.241085" in access and "5.000000" in access and field(access, "Equity effect") == "not established", "Access evidence and limit match")
        workforce = (root / "workforce-review.md").read_text(encoding="utf-8")
        require("7.923167" in workforce and "8.715484" in workforce and "40.000000" in workforce and "25.220413" in workforce, "Workforce planning values match")
        require(field(workforce, "Staffing recommendation") == "not established" and "not treated as zero burden" in workforce, "Staffing and missing-burden limits match")

        dashboard_review = (root / "dashboard-review.md").read_text(encoding="utf-8")
        require(field(dashboard_review, "Measures displayed") == "12" and field(dashboard_review, "Prospectively unavailable values") == "3" and field(dashboard_review, "Automatic alerting") == "none", "Dashboard count and authority match")
        escalation_review = (root / "escalation-fallback-review.md").read_text(encoding="utf-8")
        require(field(escalation_review, "Escalation rules") == "10" and field(escalation_review, "Automatic actions") == "0" and field(escalation_review, "Fallback state") == "continue no-change monitoring", "Escalation and fallback match")
        stewardship = (root / "monitoring-stewardship.md").read_text(encoding="utf-8")
        require(field(stewardship, "Measure owners assigned") == "12 of 12" and "do not impute" in stewardship, "Monitoring ownership and unavailable rule match")

        account_header, accounts = read_csv(root / "accountability-map.csv")
        require(account_header == ["accountability_id", "decision_or_measure", "responsible", "accountable", "consulted", "informed", "authority_limit"], "Accountability header matches")
        require([row["accountability_id"] for row in accounts] == [f"A{index:02d}" for index in range(1, 11)] and accounts[-1]["responsible"] == "Joe Joseph MD", "Ten accountability rows include Module 07 clinician leadership")
        require(all(row["responsible"] and row["accountable"] and row["authority_limit"] for row in accounts), "Every accountability row has ownership and a limit")

        ml_review = (root / "ml-contract-review.md").read_text(encoding="utf-8")
        for phrase in ("accepted arrivals per eight-hour shift", "21 shifts", "28", "588", "GradientBoostingRegressor", "7300600", "prohibited", "12 of 12 passed"):
            require(phrase in ml_review, f"ML contract includes: {phrase}")
        comparison = (root / "model-comparison.md").read_text(encoding="utf-8")
        require(field(comparison, "Model decision") == "retain transparent forecast" and field(comparison, "Decision rules passed") == "7 of 8", "ML near-miss decision is retained")
        for phrase in ("5.937283", "5.205494", "0.731788", "0.750000", "7.307180", "6.554934", "9.403087", "0.018212"):
            require(phrase in comparison, f"Model comparison includes: {phrase}")
        failure = (root / "failure-review.md").read_text(encoding="utf-8")
        require(field(failure, "Difficult folds passing the no-worse rule") == "4 of 4" and field(failure, "Largest ML errors retained") == "10" and "860.277096" in failure, "Failure, difficult-fold, and Week 53 evidence match")
        require(field(failure, "Feature-importance meaning") == "model split allocation only; not causal", "Feature importance limit matches")

        score_header, scores = read_csv(root / "week6-score.csv")
        require(score_header == ["criterion_id", "criterion", "points_available", "points_awarded", "evidence"] and len(scores) == 5, "Week 6 score shape matches")
        require(scores[:4] == [
            {"criterion_id": "W6-01", "criterion": "Module 04 forecast gate", "points_available": "0", "points_awarded": "0", "evidence": "accepted zero-point gate"},
            {"criterion_id": "W6-02", "criterion": "Module 05 scenario and evaluation", "points_available": "25", "points_awarded": "25", "evidence": "accepted score carried once"},
            {"criterion_id": "W6-03", "criterion": "Module 06 feasibility and monitoring gates", "points_available": "0", "points_awarded": "0", "evidence": "required zero-point gates"},
            {"criterion_id": "W6-04", "criterion": "Module 06 embedded ML gates", "points_available": "0", "points_awarded": "0", "evidence": "required zero-point gates"},
        ], "Module 04 and 06 remain zero-point gates and Module 05 is counted once")
        require(scores[-1] == {"criterion_id": "TOTAL", "criterion": "Cumulative Week 6 package", "points_available": "25", "points_awarded": "25", "evidence": "counted once"}, "Week 6 score is exactly 25 points once")
        _, gates = read_csv(root / "gate-results.csv")
        require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 23)] and all(row["status"] == "pass" for row in gates), "All 22 Module 06 gates pass")
        handoff_text = (root / "module07-handoff.md").read_text(encoding="utf-8")
        require(field(handoff_text, "Module 05 option") == "none" and field(handoff_text, "ML decision") == "retain transparent forecast" and field(handoff_text, "Implementation authority") == "not authorized", "Module 07 receives bounded scenario and forecast decisions")
        require(field(handoff_text, "Week 6 score") == "25 of 25, counted once" and field(handoff_text, "Module 06 gates") == "22 of 22", "Module 07 receives exact score and gates")
        ai = (root / "ai-use.md").read_text(encoding="utf-8")
        require(field(ai, "Invented unavailable outcomes") == "none" and field(ai, "Threshold changes after fitting") == "none" and field(ai, "Model tuning") == "none", "Responsible AI boundaries match")
        progression = (root / "progression-decision.md").read_text(encoding="utf-8")
        require(field(progression, "Decision") in ALLOWED_PROGRESSION and field(progression, "Decision") == "continue with conditions", "Progression decision is allowed and supported")
        require(field(progression, "Forecast decision") == "retain transparent forecast" and field(progression, "Implementation authority") == "not authorized", "Progression preserves model and authority decisions")
        reproducibility = (root / "reproducibility-check.md").read_text(encoding="utf-8")
        require("19 of 19" in reproducibility and "1,176" in reproducibility and "12 of 12 passed" in reproducibility and field(reproducibility, "Result") == "reproduced", "Reproducibility record is complete")

        output_shapes = {
            "upstream-inventory.csv": 33, "feasibility-screen.csv": 28,
            "monitoring-measures.csv": 12, "escalation-fallback.csv": 10,
            "dashboard-data.csv": 12, "ml-split-registry.csv": 28,
            "ml-predictions.csv": 1176, "model-performance.csv": 2,
            "fold-comparison.csv": 28, "model-error-slices.csv": 38,
            "feature-importance.csv": 30, "failure-cases.csv": 10,
            "leakage-tests.csv": 12, "week53-model-comparison.csv": 22,
            "decision-change.csv": 9, "invariant-checks.csv": 20,
        }
        for filename, count in output_shapes.items():
            _, rows = read_csv(root / f"outputs/{filename}")
            require(len(rows) == count, f"{filename} has {count} rows")

        _, feasibility_rows = read_csv(root / "outputs/feasibility-screen.csv")
        require({row["scenario_id"] for row in feasibility_rows} == {"S00", "S01", "S02", "S03"} and all(row["implementation_authorized"] == "0" for row in feasibility_rows), "Feasibility output preserves scenarios and no authority")
        _, measure_rows = read_csv(root / "outputs/monitoring-measures.csv")
        require([row["measure_id"] for row in measure_rows] == [f"M{index:02d}" for index in range(1, 13)] and sum(row["value"] == "unavailable" for row in measure_rows) == 3, "Twelve ordered measures retain three unavailable states")
        _, escalation_rows = read_csv(root / "outputs/escalation-fallback.csv")
        require(all(row["automatic_action"] == "0" and row["fallback_state"] == "continue no-change monitoring" for row in escalation_rows), "Escalation output has human review and fallback only")
        _, split_rows = read_csv(root / "outputs/ml-split-registry.csv")
        require([row["fold_id"] for row in split_rows] == [f"F{index:02d}" for index in range(1, 29)] and all(row["test_rows"] == "21" for row in split_rows), "All 28 temporal folds contain 21 target rows")
        _, prediction_rows = read_csv(root / "outputs/ml-predictions.csv")
        method_rows = {method: [row for row in prediction_rows if row["method"] == method] for method in ("seasonal_exponential_smoothing", "gradient_boosted")}
        require(all(len(rows) == 588 for rows in method_rows.values()), "Both methods have 588 rows")
        require({(row["fold_id"], row["target_shift_id"]) for row in method_rows["seasonal_exponential_smoothing"]} == {(row["fold_id"], row["target_shift_id"]) for row in method_rows["gradient_boosted"]}, "Methods use exact common target rows")
        _, performance = read_csv(root / "outputs/model-performance.csv")
        require(performance[0]["mae_arrivals"] == "5.937283" and performance[1]["mae_arrivals"] == "5.205494" and performance[0]["selected_flag"] == "1" and performance[1]["selected_flag"] == "0", "Performance and selected method match")
        _, fold_rows = read_csv(root / "outputs/fold-comparison.csv")
        difficult = [row for row in fold_rows if row["difficult_fold"] == "1"]
        require([row["fold_id"] for row in difficult] == ["F03", "F09", "F15", "F16"] and all(row["difficult_fold_rule_status"] == "pass" for row in difficult), "Four difficult folds pass their no-worse rule")
        _, leak_rows = read_csv(root / "outputs/leakage-tests.csv")
        require([row["test_id"] for row in leak_rows] == [f"L{index:02d}" for index in range(1, 13)] and all(row["status"] == "pass" for row in leak_rows), "All 12 leakage and environment tests pass")
        _, decision_rows = read_csv(root / "outputs/decision-change.csv")
        require(decision_rows[0]["rule_id"] == "R01" and decision_rows[0]["observed"] == "0.731788" and decision_rows[0]["status"] == "fail", "MAE near-miss remains failed")
        require(sum(row["status"] == "pass" for row in decision_rows[:-1]) == 7 and decision_rows[-1]["decision_effect"] == "retain transparent forecast", "Seven of eight rules retain the transparent forecast")
        _, invariant_rows = read_csv(root / "outputs/invariant-checks.csv")
        require(all(row["status"] == "pass" for row in invariant_rows), "All 20 release invariants pass")
        report = json.loads((root / "outputs/build-report.json").read_text(encoding="utf-8"))
        require(report["outputs"] == 19 and report["prediction_rows"] == 1176 and report["decision_rules_passed"] == 7 and report["ml_decision"] == "retain transparent forecast", "Build report shape and decision match")
        require(report["mae_improvement_arrivals"] == 0.731788 and report["week53_ml_arrivals"] == 860.277096 and report["implementation_authorized"] is False, "Build report near miss, Week 53, and authority match")

        svg = (root / "outputs/forecast-comparison.svg").read_text(encoding="utf-8")
        require('role="img"' in svg and "<title" in svg and "<desc" in svg and "retain transparent forecast" in svg, "Forecast SVG is accessible and states the decision")
        require("\u2013" not in svg and "\u2014" not in svg, "Forecast SVG uses plain ASCII dashes")
        dashboard = (root / "outputs/monitoring-dashboard.html").read_text(encoding="utf-8")
        require(dashboard.count("<h1>") == 1 and dashboard.count('<article class="measure') == 12 and "Exact measure table" in dashboard, "Dashboard has semantic heading and 12 exact measure cards")
        require("Planning evidence only" in dashboard and "No clinical action" in dashboard and "No live connection" in dashboard, "Dashboard displays planning and authority limits")
        require("<script" not in dashboard.lower() and "http://" not in dashboard and "https://" not in dashboard and "@media (max-width: 420px)" in dashboard, "Dashboard is self-contained and supports narrow screens")

        if regenerate:
            with tempfile.TemporaryDirectory(prefix="app3-module06-validate-") as temp_dir:
                regenerated = Path(temp_dir) / "outputs"
                regenerated_report = build_evidence.generate(regenerated)
                require(regenerated_report["ml_decision"] == "retain transparent forecast" and regenerated_report["outputs"] == 19, "Evidence build report reproduces")
                for relative in build_workspace.OUTPUT_FILES:
                    name = Path(relative).name
                    require((regenerated / name).read_bytes() == (root / relative).read_bytes(), f"Regenerated output matches: {name}")

    report = {
        "status": "pass",
        "mode": "starter" if starter else "complete",
        "checks_passed": len(checks),
        "assembled_files": expected_files,
        "manifest_rows": expected_manifest,
        "week6_points": 0 if starter else 25,
        "module06_gates_passed": 0 if starter else 22,
    }
    print(f"APP-3 Module 06 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path) -> None:
    try:
        validate(root, regenerate=False)
    except (OSError, ValueError, KeyError, RuntimeError):
        return
    raise AssertionError("Validator accepted an invalid workspace")


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app3-module06-validator-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)

        names = (
            "upstream-change", "forced-option", "implementation-claim", "missing-feasibility",
            "safety-claim", "access-threshold", "hidden-workforce", "dashboard-boundary",
            "wrong-rows", "changed-parameter", "leakage-failure", "dropped-difficult-fold",
            "changed-threshold", "accepted-ml", "duplicate-points", "failed-gate",
            "placeholder", "wrong-progression",
        )
        cases = {}
        for name in names:
            target = base / name
            shutil.copytree(reference, target)
            cases[name] = target
        path = cases["upstream-change"] / "upstream/module05-release.json"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8", newline="\n")
        path = cases["forced-option"] / "feasibility-review.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Option ready for implementation: `none`", "Option ready for implementation: `S01`"), encoding="utf-8")
        with (cases["implementation-claim"] / "module07-handoff.md").open("a", encoding="utf-8") as handle:
            handle.write("\n- Implementation authority: `authorized`\n")
        (cases["missing-feasibility"] / "feasibility-review.md").unlink()
        with (cases["safety-claim"] / "quality-safety-review.md").open("a", encoding="utf-8") as handle:
            handle.write("\nSafety is established.\n")
        path = cases["access-threshold"] / "access-equity-review.md"
        path.write_text(path.read_text(encoding="utf-8").replace("5.000000", "50.000000"), encoding="utf-8")
        path = cases["hidden-workforce"] / "workforce-review.md"
        path.write_text(path.read_text(encoding="utf-8").replace("40.000000", "0.000000"), encoding="utf-8")
        path = cases["dashboard-boundary"] / "outputs/monitoring-dashboard.html"
        path.write_text(path.read_text(encoding="utf-8").replace("Planning evidence only", "Operational dashboard"), encoding="utf-8")
        path = cases["wrong-rows"] / "outputs/ml-predictions.csv"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8", newline="\n")
        path = cases["changed-parameter"] / "ml-contract.json"
        path.write_text(path.read_text(encoding="utf-8").replace('"n_estimators": 100', '"n_estimators": 200'), encoding="utf-8")
        path = cases["leakage-failure"] / "outputs/leakage-tests.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8")
        path = cases["dropped-difficult-fold"] / "outputs/fold-comparison.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("F03,21", "F30,21", 1), encoding="utf-8")
        path = cases["changed-threshold"] / "outputs/decision-change.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("0.750000", "0.700000", 1), encoding="utf-8")
        path = cases["accepted-ml"] / "model-comparison.md"
        path.write_text(path.read_text(encoding="utf-8").replace("retain transparent forecast", "accept gradient boosted forecast", 1), encoding="utf-8")
        path = cases["duplicate-points"] / "week6-score.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("W6-03,Module 06 feasibility and monitoring gates,0,0", "W6-03,Module 06 feasibility and monitoring gates,25,25"), encoding="utf-8")
        path = cases["failed-gate"] / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8")
        with (cases["placeholder"] / "progression-decision.md").open("a", encoding="utf-8") as handle:
            handle.write("\nREPLACE\n")
        path = cases["wrong-progression"] / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("continue with conditions", "advance anyway", 1), encoding="utf-8")
        for target in cases.values():
            expect_failure(target)
        assert complete_report["week6_points"] == 25 and complete_report["module06_gates_passed"] == 22
        assert starter_report["week6_points"] == 0 and starter_report["module06_gates_passed"] == 0
    print("APP-3 Module 06 validator self-check passed: reference, starter, and eighteen failure routes checked.")


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
    except (OSError, ValueError, KeyError, ImportError, ValidationError) as error:
        parser.exit(1, f"Workspace validation failed: {error}\n")


if __name__ == "__main__":
    main()
