"""Validate an APP-3 Module 04 learner or reference workspace."""

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
    r"(?i)(equilibrium (?:is )?established|demand (?:is )?guaranteed|"
    r"recommend (?:adding|hiring|increasing|reducing) staff|staffing should|implement now)"
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


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    import build_forecast
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
    expected_files = 49 if starter else 59
    expected_manifest = 36 if starter else 46
    require(root.is_dir(), "Workspace directory exists")
    require(actual == expected and len(actual) == expected_files, f"Workspace has exactly {expected_files} expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "forecast-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app3-04", "version": "0.1.0", "commons_release": "0.70.0", "hours": 16.5, "course_points": 0}, "Module identity and workload match")
    require(contract["upstream"] == {"checkpoint_id": "oclc-app3-cp01", "version": "0.1.0", "commons_release": "0.69.0", "candidate_files": 137, "candidate_manifest_sha256": "9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656", "frozen_files": 23, "shift_rows": 1092, "weeks": 52}, "Checkpoint handoff contract matches")
    forecast = contract["forecast"]
    require(forecast["target"] == "accepted arrivals per eight-hour shift" and forecast["issue_time"] == "end of the final shift in each completed week", "Forecast target and issue time match")
    require(forecast["horizon_shifts"] == 21 and forecast["seasonal_period_shifts"] == 21, "Horizon and seasonal lag are 21 shifts")
    require(forecast["initial_training_weeks"] == [1, 24] and forecast["evaluation_weeks"] == [25, 52] and forecast["rolling_folds"] == 28, "Rolling-origin windows match")
    require(forecast["methods"] == ["last_value", "seasonal_naive", "seasonal_exponential_smoothing"], "Three transparent methods match")
    require(forecast["alpha"] == 0.3 and forecast["gamma"] == 0.2 and forecast["trend"] == "none", "Smoothing parameters are fixed")
    require(contract["capacity"]["staffing_recommendation"] == "prohibited" and contract["assessment"] == {"noncompensable_gates": 18, "course_points_awarded_here": 0, "next_module": "oclc-app3-05"}, "Capacity and assessment boundaries match")

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
    require(handoff == {"files": 23, "checkpoint_version": "0.1.0", "candidate_files": 137, "shift_rows": 1092, "weeks": 52, "accepted_encounters": 43628}, "Checkpoint handoff reproduces")

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
        require(not any(path.startswith("outputs/") for path in actual), "Starter contains no accepted forecast outputs")
    else:
        require(UNSAFE_CLAIM.search(record_text) is None, "Learner records contain no guaranteed-demand, equilibrium, staffing, or implementation claim")

    fold_header, folds = read_csv(root / "fold-audit.csv")
    require(fold_header == ["fold_id", "issue_date", "train_end_week", "test_week", "horizon_shifts", "special_event_shifts", "actual_arrivals", "forecast_arrivals", "forecast_error", "fold_mae_arrivals", "eligibility_status"], "Fold audit header matches")
    gate_header, gates = read_csv(root / "gate-results.csv")
    require(gate_header == ["gate_id", "gate", "required_status", "evidence", "status"], "Gate result header matches")
    if starter:
        require(len(folds) >= 1 and len(gates) == 18, "Starter provides fold and gate structures")
    else:
        require([row["fold_id"] for row in folds] == [f"F{index:02d}" for index in range(1, 29)], "Fold audit has 28 ordered origins")
        require(all(row["horizon_shifts"] == "21" and row["eligibility_status"] == "eligible" for row in folds), "Every fold has 21 eligible target shifts")
        require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 19)] and all(row["status"] == "pass" for row in gates), "All 18 noncompensable gates pass")

        forecast_plan = (root / "forecast-plan.md").read_text(encoding="utf-8")
        require(field(forecast_plan, "Target") == "accepted arrivals per eight-hour shift", "Learner target matches")
        require(field(forecast_plan, "Cutoff") == "the issue shift; no later observation is eligible", "Cutoff excludes future observations")
        require(field(forecast_plan, "Horizon") == "21 consecutive shifts over 7 days", "One-week horizon is explicit")
        require("28 expanding rolling-origin folds" in forecast_plan and "0.25 arrivals" in forecast_plan, "Fold and tie rules are explicit")

        model = (root / "model-comparison.md").read_text(encoding="utf-8")
        for phrase in ("10.775510", "7.095238", "5.937283", "7.307180", "0.008215", "15.141268%", "1743.145982", "1747.976153"):
            require(phrase in model, f"Model comparison includes: {phrase}")
        require(field(model, "Selected method") == "seasonal_exponential_smoothing", "Selected method matches")
        require("under- and over-forecasts" in model and "64.68 arrivals per week" in model, "Operational error consequences remain visible")

        failure = (root / "failure-period-review.md").read_text(encoding="utf-8")
        require(field(failure, "Highest-MAE fold") == "F09" and field(failure, "Test week") == "33", "Highest-error fold is identified")
        require("F03" in failure and "F15" in failure and "F16" in failure and "holiday, 9 rows" in failure, "Failure and unsupported periods remain visible")

        capacity = (root / "capacity-interpretation.md").read_text(encoding="utf-8")
        for phrase in ("876.924084", "805.136639 to 970.733035", "0.960000", "841.847121", "772.931174", "931.903714", "64.678197", "62.091069"):
            require(phrase in capacity, f"Capacity interpretation includes: {phrase}")
        require(field(capacity, "Staffing recommendation") == "not authorized", "Capacity interpretation does not authorize staffing")

        little = (root / "littles-law-interpretation.md").read_text(encoding="utf-8")
        require(field(little, "Equilibrium status") == "not established" and field(little, "Permitted use") == "bounded consistency check only", "Little's Law use is bounded")
        require("median arrival-to-clinician elapsed time" in little and "mean queue-end snapshot" in little, "Little's Law field mismatch is explicit")

        accessible = (root / "accessible-output-review.md").read_text(encoding="utf-8")
        require(accessible.count("`pass`") == 8 and "805 to 971" in accessible, "Accessible output review is complete")
        handoff_text = (root / "module05-handoff.md").read_text(encoding="utf-8")
        require(field(handoff_text, "Module 05 permission") == "permitted for improvement scenario and evaluation construction", "Module 05 handoff permission matches")
        require(field(handoff_text, "Staffing decision") == "not authorized" and "F03, F09, F15, and F16" in handoff_text, "Module 05 retains action and failure boundaries")
        progression = (root / "progression-decision.md").read_text(encoding="utf-8")
        decision = field(progression, "Decision")
        require(decision in ALLOWED_PROGRESSION and decision == "continue with conditions", "Progression decision is allowed and supported")
        require(field(progression, "Gates passed") == "18 of 18" and field(progression, "Course points awarded here") == "0", "Progression preserves zero-point gate rule")
        require(field(progression, "Implementation authority") == "not authorized", "Progression does not authorize implementation")

        output_shapes = {
            "folds.csv": 28, "forecast-predictions.csv": 1764, "error-summary.csv": 3,
            "error-slices.csv": 17, "week53-forecast.csv": 21,
            "capacity-implication.csv": 13, "littles-law-check.csv": 4,
        }
        for filename, count in output_shapes.items():
            _, rows = read_csv(root / f"outputs/{filename}")
            require(len(rows) == count, f"{filename} has {count} rows")
        findings = json.loads((root / "outputs/forecast-findings.json").read_text(encoding="utf-8"))
        require(findings["selected_method"] == "seasonal_exponential_smoothing" and findings["contract"]["folds"] == 28, "Forecast findings identify selection and folds")
        require(findings["method_metrics"]["seasonal_exponential_smoothing"] == {"bias": 0.008215, "mae": 5.937283, "over": 1747.976153, "rmse": 7.30718, "under": 1743.145982, "wape": 15.141268}, "Selected-model metrics match")
        require(findings["week53"] == {"empirical_actual_equivalent_lower": 805.136639, "empirical_actual_equivalent_upper": 970.733035, "end_date": "2025-01-05", "raw_forecast_arrivals": 876.924084, "rounded_shift_total_arrivals": 878, "start_date": "2024-12-30"}, "Week 53 findings match")
        require(findings["capacity"]["staffing_recommendation"] == "not authorized" and findings["littles_law"]["equilibrium_status"] == "not established", "Output claim boundaries match")

        for filename in ("forecast-error-comparison.svg", "week53-demand-forecast.svg"):
            svg = (root / f"outputs/{filename}").read_text(encoding="utf-8")
            require('role="img"' in svg and "<title" in svg and "<desc" in svg, f"{filename} has accessible SVG structure")
            require("\u2013" not in svg and "\u2014" not in svg, f"{filename} uses plain ASCII dashes")
        require("Last&#160;value" in (root / "outputs/forecast-error-comparison.svg").read_text(encoding="utf-8"), "Method chart does not rely on color alone")
        r_code = (root / "verify_forecast.R").read_text(encoding="utf-8")
        require("stopifnot" in r_code and "876.9240843532087" in r_code and "5.937282542565626" in r_code, "Base-R cross-check records exact expectations")

        with tempfile.TemporaryDirectory(prefix="app3-module04-validate-") as temp_dir:
            regenerated = Path(temp_dir) / "outputs"
            report = build_forecast.generate(regenerated)
            require(report == {"outputs": 10, "folds": 28, "prediction_rows": 1764, "selected_method": "seasonal_exponential_smoothing", "week53_raw_forecast": 876.924084}, "Forecast build report matches")
            for relative in build_workspace.OUTPUT_FILES:
                name = Path(relative).name
                require((regenerated / name).read_bytes() == (root / relative).read_bytes(), f"Regenerated output matches: {name}")

    report = {
        "status": "pass",
        "mode": "starter" if starter else "complete",
        "checks_passed": len(checks),
        "assembled_files": expected_files,
        "manifest_rows": expected_manifest,
        "module04_points": 0,
        "gates_passed": 0 if starter else 18,
    }
    print(f"APP-3 Module 04 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path, starter: bool = False) -> None:
    try:
        validate(root, starter=starter)
    except (OSError, ValueError, KeyError, RuntimeError):
        return
    raise AssertionError("Validator accepted an invalid workspace")


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app3-module04-validator-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)

        names = (
            "upstream-change", "missing-upstream", "wrong-target", "missing-fold",
            "future-leakage", "wrong-method", "wrong-mae", "hidden-error",
            "failed-gate", "missing-record", "staffing-claim", "equilibrium-claim",
            "holiday-overclaim", "changed-capacity", "missing-law-limit",
            "bad-progression", "handoff-staffing", "changed-output", "placeholder",
        )
        cases = {}
        for name in names:
            target = base / name
            shutil.copytree(reference, target)
            cases[name] = target
        path = cases["upstream-change"] / "upstream/shift-metrics.csv"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
        (cases["missing-upstream"] / "upstream/checkpoint-release.json").unlink()
        path = cases["wrong-target"] / "forecast-plan.md"
        path.write_text(path.read_text(encoding="utf-8").replace("accepted arrivals per eight-hour shift", "daily visits", 1), encoding="utf-8")
        lines = (cases["missing-fold"] / "fold-audit.csv").read_text(encoding="utf-8").splitlines()
        (cases["missing-fold"] / "fold-audit.csv").write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
        path = cases["future-leakage"] / "forecast-plan.md"
        path.write_text(path.read_text(encoding="utf-8").replace("the issue shift; no later observation is eligible", "later observations may enter", 1), encoding="utf-8")
        path = cases["wrong-method"] / "model-comparison.md"
        path.write_text(path.read_text(encoding="utf-8").replace("- Selected method: `seasonal_exponential_smoothing`", "- Selected method: `seasonal_naive`", 1), encoding="utf-8")
        path = cases["wrong-mae"] / "model-comparison.md"
        path.write_text(path.read_text(encoding="utf-8").replace("5.937283", "4.000000", 1), encoding="utf-8")
        path = cases["hidden-error"] / "model-comparison.md"
        path.write_text(path.read_text(encoding="utf-8").replace("under- and over-forecasts", "total errors", 1), encoding="utf-8")
        path = cases["failed-gate"] / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass\n", ",fail\n", 1), encoding="utf-8")
        (cases["missing-record"] / "failure-period-review.md").unlink()
        for name, phrase in (("staffing-claim", "We recommend adding staff."), ("equilibrium-claim", "Equilibrium is established.")):
            with (cases[name] / "capacity-interpretation.md").open("a", encoding="utf-8") as handle:
                handle.write(f"\n{phrase}\n")
        path = cases["holiday-overclaim"] / "failure-period-review.md"
        path.write_text(path.read_text(encoding="utf-8").replace("holiday, 9 rows", "holiday, stable estimate", 1), encoding="utf-8")
        path = cases["changed-capacity"] / "capacity-interpretation.md"
        path.write_text(path.read_text(encoding="utf-8").replace("841.847121", "900.000000", 1), encoding="utf-8")
        path = cases["missing-law-limit"] / "littles-law-interpretation.md"
        path.write_text(path.read_text(encoding="utf-8").replace("bounded consistency check only", "staffing calculation", 1), encoding="utf-8")
        path = cases["bad-progression"] / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("continue with conditions", "advance anyway", 1), encoding="utf-8")
        path = cases["handoff-staffing"] / "module05-handoff.md"
        path.write_text(path.read_text(encoding="utf-8").replace("- Staffing decision: `not authorized`", "- Staffing decision: `authorized`", 1), encoding="utf-8")
        path = cases["changed-output"] / "outputs/error-summary.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("5.937283", "4.937283", 1), encoding="utf-8")
        with (cases["placeholder"] / "progression-decision.md").open("a", encoding="utf-8") as handle:
            handle.write("\nREPLACE\n")
        for target in cases.values():
            expect_failure(target)
        expect_failure(starter)
        assert complete_report["gates_passed"] == 18 and complete_report["module04_points"] == 0
        assert starter_report["gates_passed"] == 0
    print("APP-3 Module 04 validator self-check passed: reference, starter, and nineteen failure routes checked.")


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
