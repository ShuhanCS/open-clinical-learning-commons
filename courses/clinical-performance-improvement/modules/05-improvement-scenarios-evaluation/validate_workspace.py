"""Validate an APP-3 Module 05 learner or reference workspace."""

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
    r"(?i)(simulation proves|implementation authority:\s*`?authorized|"
    r"selected option:\s*`?S0[1-3]|safety outcome:\s*`?(?:improved|safe)|"
    r"return within 72 hours:\s*`?(?:improved|reduced))"
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
    import build_scenarios
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
    expected_files = 56 if starter else 68
    expected_manifest = 41 if starter else 53
    require(root.is_dir(), "Workspace directory exists")
    require(actual == expected and len(actual) == expected_files, f"Workspace has exactly {expected_files} expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "scenario-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app3-05", "version": "0.1.0", "commons_release": "0.71.0", "hours": 16.0, "course_points": 25}, "Module identity and workload match")
    require(contract["upstream"]["point_arrivals"] == 876.924084 and contract["upstream"]["accepted_encounters"] == 43628, "Accepted forecast and population match")
    simulation = contract["simulation"]
    require(simulation["warmup_days"] == 7 and simulation["measurement_days"] == 7 and simulation["replications_per_scenario_condition"] == 200, "Time and replication contract match")
    require(simulation["base_clinician_slots"] == {"night": 2, "day": 6, "evening": 4}, "Guided-model capacity matches")
    require(simulation["effective_service_fraction"] == 0.20 and simulation["queue_trigger_patients"] == 4 and simulation["queue_trigger_persistence_minutes"] == 15, "Service and trigger assumptions match")
    require(contract["scenarios"] == ["S00", "S01", "S02", "S03"] and contract["conditions"] == ["C01", "C02", "C03", "C04", "C05"], "Scenario and condition registers match")
    require(contract["assessment"] == {"course_points": 25, "noncompensable_gates": 20, "next_module": "oclc-app3-06"}, "Assessment and handoff match")

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
    require(handoff == {"files": 29, "module04_version": "0.1.0", "accepted_encounters": 43628, "scenarios": 4, "forecast_arrivals": 876.924084}, "Module 04 handoff reproduces")

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
        require(not any(path.startswith("outputs/") for path in actual), "Starter contains no accepted scenario outputs")
    else:
        require(UNSAFE_CLAIM.search(record_text) is None, "Learner records contain no selected-option, safety, causal, or implementation overclaim")

        assumption_header, assumptions = read_csv(root / "scenario-assumption-register.csv")
        require(assumption_header == ["assumption_id", "domain", "assumption", "accepted_value", "source", "status", "claim_limit"], "Assumption register header matches")
        require([row["assumption_id"] for row in assumptions] == [f"A{index:02d}" for index in range(1, 19)] and all(row["status"] == "accepted" for row in assumptions), "All 18 assumptions are accepted and ordered")

        validation = (root / "scenario-validation.md").read_text(encoding="utf-8")
        for phrase in ("24 of 24 passed", "4,000", "60.035963", "11.914912%", "45.084398", "70.473589"):
            require(phrase in validation, f"Scenario validation includes: {phrase}")
        comparison = (root / "scenario-comparison.md").read_text(encoding="utf-8")
        require(field(comparison, "Decision") == "none qualifies for feasibility review", "No option is forced through the decision rule")
        for phrase in ("1.958703", "21.244986", "2.518000", "5.803341", "41.617987", "6.611140", "0.316383", "14.547388"):
            require(phrase in comparison, f"Scenario comparison includes: {phrase}")
        sensitivity = (root / "sensitivity-interpretation.md").read_text(encoding="utf-8")
        require(field(sensitivity, "Null or failed comparisons retained") == "6" and "86.671644 minutes worse" in sensitivity, "Failed sensitivity evidence remains visible")
        access = (root / "access-workforce-safety-review.md").read_text(encoding="utf-8")
        require(field(access, "Safety outcome") == "not simulated; prospective measurement required" and field(access, "Return within 72 hours") == "not simulated; prospective measurement required", "Safety and return boundaries match")
        require("40.000000" in access and "25.220413" in access and "not staffing recommendations" in access, "Workforce consequences and limit remain visible")

        threat_header, threat_rows = read_csv(root / "evaluation-threat-audit.csv")
        require(threat_header == ["threat_id", "threat", "detection", "response", "status"] and [row["threat_id"] for row in threat_rows] == [f"T{index:02d}" for index in range(1, 9)], "Eight evaluation threats are complete")
        _, scores = read_csv(root / "week6-score.csv")
        require(len(scores) == 7 and scores[-1] == {"criterion_id": "TOTAL", "criterion": "Week 6 Module 05 score", "points_available": "25", "points_awarded": "25", "evidence": "counted once"}, "Week 6 score is exactly 25 points once")
        _, gates = read_csv(root / "gate-results.csv")
        require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 21)] and all(row["status"] == "pass" for row in gates), "All 20 noncompensable gates pass")
        handoff_text = (root / "module06-handoff.md").read_text(encoding="utf-8")
        require(field(handoff_text, "Option for feasibility review") == "none" and field(handoff_text, "Implementation authority") == "not authorized", "Module 06 receives no selected option or implementation authority")
        progression = (root / "progression-decision.md").read_text(encoding="utf-8")
        require(field(progression, "Decision") in ALLOWED_PROGRESSION and field(progression, "Decision") == "continue with conditions", "Progression decision is allowed and supported")
        require(field(progression, "Module 05 score") == "25 of 25" and field(progression, "Gates passed") == "20 of 20", "Progression carries exact score and gates")

        output_shapes = {
            "input-profile.csv": 45, "condition-register.csv": 5,
            "validation-checks.csv": 24, "replication-results.csv": 4000,
            "scenario-summary.csv": 20, "paired-effects.csv": 15,
            "sensitivity-review.csv": 15, "evaluation-measures.csv": 12,
            "evaluation-threats.csv": 8,
        }
        for filename, count in output_shapes.items():
            _, rows = read_csv(root / f"outputs/{filename}")
            require(len(rows) == count, f"{filename} has {count} rows")
        findings = json.loads((root / "outputs/scenario-findings.json").read_text(encoding="utf-8"))
        require(findings["selection"]["selected_option"] == "none" and findings["sensitivity"]["null_or_failed_rows"] == 6, "Selection and failed sensitivities match")
        require(findings["point_demand"]["S00"]["median_wait_minutes"] == 60.035963 and findings["point_demand"]["S00"]["left_before_seen_percent"] == 11.914912, "No-change point-demand result matches")
        require(findings["point_paired_effects"]["S01"]["p90_wait_improvement_minutes"] == 21.244986 and findings["point_paired_effects"]["S02"]["median_wait_improvement_minutes"] == -5.803341, "Paired scenario effects match")
        require(findings["evaluation"]["causal_status"] == "not established by simulation" and findings["module06_handoff"]["authority"].endswith("no implementation authority"), "Causal and implementation boundaries match")
        for filename in ("point-demand-tradeoffs.svg", "sensitivity-wait-effects.svg"):
            svg = (root / f"outputs/{filename}").read_text(encoding="utf-8")
            require('role="img"' in svg and "<title" in svg and "<desc" in svg, f"{filename} has accessible SVG structure")
            require("\u2013" not in svg and "\u2014" not in svg, f"{filename} uses plain ASCII dashes")

        with tempfile.TemporaryDirectory(prefix="app3-module05-validate-") as temp_dir:
            regenerated = Path(temp_dir) / "outputs"
            report = build_scenarios.generate(regenerated)
            require(report == {"outputs": 12, "replication_rows": 4000, "summary_rows": 20, "paired_effect_rows": 15, "selected_option": "none", "null_or_failed_sensitivities": 6}, "Scenario build report matches")
            for relative in build_workspace.OUTPUT_FILES:
                name = Path(relative).name
                require((regenerated / name).read_bytes() == (root / relative).read_bytes(), f"Regenerated output matches: {name}")

    report = {
        "status": "pass",
        "mode": "starter" if starter else "complete",
        "checks_passed": len(checks),
        "assembled_files": expected_files,
        "manifest_rows": expected_manifest,
        "module05_points": 0 if starter else 25,
        "gates_passed": 0 if starter else 20,
    }
    print(f"APP-3 Module 05 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path) -> None:
    try:
        validate(root)
    except (OSError, ValueError, KeyError, RuntimeError):
        return
    raise AssertionError("Validator accepted an invalid workspace")


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app3-module05-validator-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)

        names = (
            "upstream-change", "wrong-score", "failed-gate", "forced-option",
            "safety-claim", "causal-claim", "implementation-claim",
            "hidden-failure", "missing-record", "changed-output",
            "placeholder", "wrong-progression",
        )
        cases = {}
        for name in names:
            target = base / name
            shutil.copytree(reference, target)
            cases[name] = target
        path = cases["upstream-change"] / "upstream/week53-forecast.csv"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
        path = cases["wrong-score"] / "week6-score.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("TOTAL,Week 6 Module 05 score,25,25,counted once", "TOTAL,Week 6 Module 05 score,25,24,counted once"), encoding="utf-8")
        path = cases["failed-gate"] / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass\n", ",fail\n", 1), encoding="utf-8")
        path = cases["forced-option"] / "scenario-comparison.md"
        path.write_text(path.read_text(encoding="utf-8").replace("none qualifies for feasibility review", "S01", 1), encoding="utf-8")
        with (cases["safety-claim"] / "access-workforce-safety-review.md").open("a", encoding="utf-8") as handle:
            handle.write("\n- Safety outcome: `improved`\n")
        with (cases["causal-claim"] / "evaluation-design.md").open("a", encoding="utf-8") as handle:
            handle.write("\nSimulation proves the effect.\n")
        with (cases["implementation-claim"] / "module06-handoff.md").open("a", encoding="utf-8") as handle:
            handle.write("\n- Implementation authority: `authorized`\n")
        path = cases["hidden-failure"] / "sensitivity-interpretation.md"
        path.write_text(path.read_text(encoding="utf-8").replace("- Null or failed comparisons retained: `6`", "- Null or failed comparisons retained: `0`"), encoding="utf-8")
        (cases["missing-record"] / "scenario-validation.md").unlink()
        path = cases["changed-output"] / "outputs/scenario-findings.json"
        path.write_text(path.read_text(encoding="utf-8").replace('"selected_option": "none"', '"selected_option": "S01"', 1), encoding="utf-8")
        with (cases["placeholder"] / "progression-decision.md").open("a", encoding="utf-8") as handle:
            handle.write("\nREPLACE\n")
        path = cases["wrong-progression"] / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("continue with conditions", "advance anyway", 1), encoding="utf-8")
        for target in cases.values():
            expect_failure(target)
        assert complete_report["module05_points"] == 25 and complete_report["gates_passed"] == 20
        assert starter_report["module05_points"] == 0 and starter_report["gates_passed"] == 0
    print("APP-3 Module 05 validator self-check passed: reference, starter, and twelve failure routes checked.")


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
