"""Validate the APP-3 cumulative Week 3 checkpoint."""

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
    "README.md", "evidence-index.csv", "measures-variation-readiness-review.md",
    "checkpoint-gates.csv", "checkpoint-defense.md", "reproducibility-check.md",
    "ai-use.md", "progression-decision.md",
)
MODULES = {
    "module-01": {
        "id": "oclc-app3-01", "version": "0.1.0", "commons_release": "0.66.0",
        "files": 25, "immutable_rows": 14, "manifest_bytes": 1741,
        "manifest_sha256": "ecd8400c5e972e7070d64770086d752a89fd8bc659a1c5c1345c612d0236605d",
    },
    "module-02": {
        "id": "oclc-app3-02", "version": "0.1.0", "commons_release": "0.67.0",
        "files": 58, "immutable_rows": 43, "manifest_bytes": 5266,
        "manifest_sha256": "868f87c365de83e052c3acee6c7742586a8007dd75d9976343b2f06dfbf622e4",
    },
    "module-03": {
        "id": "oclc-app3-03", "version": "0.1.0", "commons_release": "0.68.0",
        "files": 54, "immutable_rows": 40, "manifest_bytes": 5115,
        "manifest_sha256": "6528e85f2324fd4b2068788598417be96f6c3a699a587a6ef5eb63f176b0242f",
    },
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


def validate(root: Path, learner: bool = False) -> dict[str, object]:
    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    required = set(IMMUTABLE_FILES) | set(WORK_FILES) | {"candidate-manifest.csv"}
    require(root.is_dir(), "Checkpoint directory exists")
    header, manifest = read_csv(root / "candidate-manifest.csv")
    require(
        header == ["relative_path", "bytes", "sha256", "source_module", "source_version", "role"],
        "Candidate manifest header matches",
    )
    require(
        len(manifest) == 137
        and [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest),
        "Candidate manifest has 137 sorted rows",
    )
    expected = required | {row["relative_path"] for row in manifest}
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts
    }
    require(actual == expected and len(actual) == 153, "Checkpoint has exactly 153 expected files")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        directory = row["relative_path"].split("/")[1]
        require(
            row["source_module"] == MODULES[directory]["id"]
            and row["source_version"] == MODULES[directory]["version"],
            f"Candidate source identity matches: {row['relative_path']}",
        )

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version matches")
    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(
        contract["checkpoint_id"] == "oclc-app3-cp01"
        and contract["version"] == "0.1.0"
        and contract["commons_release"] == "0.69.0",
        "Checkpoint identity matches",
    )
    require(
        contract["course_points"] == 40
        and contract["point_source"] == "oclc-app3-02 20 points once plus oclc-app3-03 20 points once",
        "Checkpoint point contract matches",
    )
    require(
        contract["accepted_component_files"] == 137 and len(contract["accepted_modules"]) == 3,
        "Contract accepts 137 files from three modules",
    )
    require(
        [module["points"] for module in contract["accepted_modules"]] == [0, 20, 20]
        and sum(module["points"] for module in contract["accepted_modules"]) == 40,
        "Contract assigns Module 01 zero points and Modules 02 and 03 20 points once",
    )
    require(
        contract["required_gates"] == {
            "module01_decision": 12, "module02_measurement": 15,
            "module03_diagnostic": 18, "checkpoint_integrity": 18,
        },
        "Contract carries all inherited and checkpoint gate totals",
    )

    for directory, details in MODULES.items():
        module_root = root / "candidate" / directory
        files = [
            path for path in module_root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        ]
        require(len(files) == details["files"], f"{directory} file count matches")
        require(
            (module_root / "VERSION").read_text(encoding="utf-8").strip() == details["version"],
            f"{directory} version matches",
        )
        if (module_root / "release.json").is_file():
            release = json.loads((module_root / "release.json").read_text(encoding="utf-8"))
            identity = (release["module_id"], release["module_version"], release["commons_release"])
        else:
            decision = json.loads((module_root / "decision-contract.json").read_text(encoding="utf-8"))["module"]
            identity = (decision["id"], decision["version"], decision["commons_release"])
        require(
            identity == (details["id"], details["version"], details["commons_release"]),
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
            require(
                path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"],
                f"{directory} nested artifact matches: {row['relative_path']}",
            )

    for name in WORK_FILES:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if learner:
            require(bool(PLACEHOLDER.search(text)), f"Learner prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Reference record is complete: {name}")
    if learner:
        report = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 153}
        print(f"APP-3 Checkpoint 1 learner validation passed: {len(checks)} checks.")
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
    require(
        len(index_rows) == 3
        and [row["module_id"] for row in index_rows] == ["oclc-app3-01", "oclc-app3-02", "oclc-app3-03"],
        "Evidence index has three ordered modules",
    )
    require(
        [row["checkpoint_points"] for row in index_rows] == ["0", "20", "20"]
        and sum(Decimal(row["checkpoint_points"]) for row in index_rows) == Decimal("40"),
        "Evidence index assigns Module 01 zero points and Modules 02 and 03 20 points exactly once",
    )
    for row, details in zip(index_rows, MODULES.values(), strict=True):
        require(
            row["version"] == details["version"] and row["commons_release"] == details["commons_release"],
            f"Evidence index version matches: {row['module_id']}",
        )
        require(
            int(row["assembled_files"]) == details["files"]
            and int(row["manifest_rows"]) == details["immutable_rows"]
            and int(row["manifest_bytes"]) == details["manifest_bytes"]
            and row["manifest_sha256"] == details["manifest_sha256"],
            f"Evidence index manifest matches: {row['module_id']}",
        )
    require(
        [row["gates"] for row in index_rows] == ["12 of 12 pass", "15 of 15 pass", "18 of 18 pass"],
        "Evidence index carries all inherited passing gates",
    )

    review = (root / "measures-variation-readiness-review.md").read_text(encoding="utf-8")
    required_values = (
        "138,084", "95,800", "1,045,406", "318,732", "43,628", "39,975", "3,653",
        "1,092", "52 weeks", "Seventeen measure", "12 declared repairs", "30 query checks",
        "Weeks 1 through 24", "four declared chart", "Three predeclared rules", "nine signal records",
        "8.13767", "97.636958", "90.485606", "104.788311", "9.895751", "853",
        "894", "673", "358", "379", "75.2796", "40.0447", "99.0302",
        "49 minutes", "66 minutes", "44 minutes", "401", "242", "40 of 40",
    )
    require(all(value in review for value in required_values), "Cumulative review contains exact accepted evidence")
    review_lower = review.lower()
    require(
        "a signal opens review and does not prove cause" in review_lower
        and "root cause remains not established" in review_lower,
        "Cumulative review preserves signal and root-cause limits",
    )
    require(
        "those cross-group comparisons are not supported" in review_lower
        and "full-release support cannot be borrowed" in review_lower,
        "Cumulative review preserves target-window subgroup limits",
    )
    require(
        "does not automate staffing" in review_lower
        and "staffing change, clinical action, automated action, and implementation remain prohibited" in review_lower,
        "Cumulative review preserves human escalation and action limits",
    )
    require(
        not re.search(r"(?i)signal proves cause|recommend adding staff|automates staffing|authorizes implementation", review),
        "Cumulative review contains no prohibited cause, staffing, automation, or implementation claim",
    )

    gates_header, gates = read_csv(root / "checkpoint-gates.csv")
    require(gates_header == ["gate_id", "gate", "status", "evidence", "owner"], "Checkpoint gate header matches")
    require(
        len(gates) == 18
        and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 19)]
        and all(row["status"] == "pass" for row in gates),
        "All 18 checkpoint integrity gates pass",
    )

    module01 = root / "candidate/module-01"
    module01_progression = (module01 / "progression-decision.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\| G\d{2} \|", module01_progression)) == 12, "Accepted Module 01 has 12 gates")
    require(
        markdown_field(module01_progression, "Module 02 permission") == "permitted for curriculum construction",
        "Accepted Module 01 permits measure construction",
    )
    decision_contract = json.loads((module01 / "decision-contract.json").read_text(encoding="utf-8"))
    require(
        decision_contract["service"]["id"] == "CGH-ED-01"
        and decision_contract["service"]["unit_of_flow"] == "one synthetic adult emergency encounter"
        and decision_contract["service"]["public_hospital_linkage"] == "prohibited",
        "Accepted Module 01 service and linkage boundary match",
    )

    module02 = root / "candidate/module-02"
    _, measure_score = read_csv(module02 / "measure-score.csv")
    measure_criteria = [row for row in measure_score if row["criterion_id"] != "TOTAL"]
    measure_total = next(row for row in measure_score if row["criterion_id"] == "TOTAL")
    require(
        len(measure_criteria) == 5
        and sum(Decimal(row["points_awarded"]) for row in measure_criteria) == Decimal("20")
        and measure_total["points_awarded"] == "20",
        "Accepted Module 02 score totals 20 once",
    )
    _, module02_gates = read_csv(module02 / "gate-results.csv")
    require(len(module02_gates) == 15 and all(row["status"] == "pass" for row in module02_gates), "Accepted Module 02 has 15 passing gates")
    build_report = json.loads((module02 / "outputs/build-report.json").read_text(encoding="utf-8"))
    require(
        build_report["findings"]["accepted_encounters"] == 43628
        and build_report["findings"]["query_checks"] == 30
        and build_report["findings"]["failed_query_checks"] == 0,
        "Accepted Module 02 population and query checks match",
    )

    module03 = root / "candidate/module-03"
    _, diagnostic_score = read_csv(module03 / "week3-score.csv")
    diagnostic_criteria = [row for row in diagnostic_score if row["criterion_id"] != "TOTAL"]
    diagnostic_total = next(row for row in diagnostic_score if row["criterion_id"] == "TOTAL")
    require(
        len(diagnostic_criteria) == 5
        and sum(Decimal(row["points_awarded"]) for row in diagnostic_criteria) == Decimal("20")
        and diagnostic_total["points_awarded"] == "20",
        "Accepted Module 03 score totals 20 once",
    )
    _, module03_gates = read_csv(module03 / "gate-results.csv")
    require(len(module03_gates) == 18 and all(row["status"] == "pass" for row in module03_gates), "Accepted Module 03 has 18 passing gates")
    _, signals = read_csv(module03 / "outputs/signal-audit.csv")
    require(len(signals) == 9, "Accepted Module 03 has nine signal records")
    _, safety = read_csv(module03 / "outputs/safety-surveillance.csv")
    overall = next(row for row in safety if row["event_class"] == "overall")
    require(
        [overall[key] for key in (
            "known_true_events", "trigger_true_positives", "incident_true_positives", "trigger_false_positives",
            "trigger_sensitivity_percent", "incident_capture_percent", "trigger_specificity_percent",
        )] == ["894", "673", "358", "379", "75.2796", "40.0447", "99.0302"],
        "Accepted Module 03 safety undercapture evidence matches",
    )
    _, stages = read_csv(module03 / "outputs/process-stage-comparison.csv")
    target_stage = next(
        row for row in stages
        if row["context_id"] == "target_evening" and row["stage_id"] == "roomed_to_clinician"
    )
    require(target_stage["median_minutes"] == "66.0", "Accepted Module 03 target stage median matches")
    _, subgroups = read_csv(module03 / "outputs/subgroup-window-support.csv")
    target_support = {
        row["access_support_group"]: row for row in subgroups if row["window_id"] == "target_evening"
    }
    require(
        target_support["language_support"]["eligible_encounters"] == "401"
        and target_support["language_support"]["support_status"] == "not supported"
        and target_support["mobility_support"]["eligible_encounters"] == "242"
        and target_support["mobility_support"]["support_status"] == "not supported",
        "Accepted Module 03 target-window subgroup support matches",
    )
    escalation = (module03 / "escalation-rule.md").read_text(encoding="utf-8").lower()
    require(
        "human clinical" in escalation and "one business day" in escalation
        and "automated staffing: `prohibited`" in escalation
        and "automated scheduling or routing: `prohibited`" in escalation,
        "Accepted Module 03 E01 remains human-only",
    )

    defense = (root / "checkpoint-defense.md").read_text(encoding="utf-8")
    require(
        re.findall(r"(?m)^## Q(\d{2})\.", defense) == [f"{number:02d}" for number in range(1, 13)],
        "Checkpoint defense has 12 ordered questions",
    )
    require(
        len(re.findall(r"(?m)^Answer:", defense)) == 12
        and len(re.findall(r"(?m)^Evidence:", defense)) == 12
        and len(re.findall(r"(?m)^Limit:", defense)) == 12,
        "Checkpoint defense answers every question with evidence and a limit",
    )

    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    reproduction_terms = (
        "137", "module 01 has 0 points", "sum is 40", "two independent reference builds match byte for byte",
        "- candidate mutation: `rejected`", "- missing-candidate mutation: `rejected`",
        "- duplicate-point mutation: `rejected`", "- failed-gate mutation: `rejected`",
        "- changed-signal mutation: `rejected`", "- signal-as-cause mutation: `rejected`",
        "- staffing-claim mutation: `rejected`", "- unsupported-subgroup mutation: `rejected`",
        "- automated-escalation mutation: `rejected`", "- incomplete-defense mutation: `rejected`",
        "- invalid-progression mutation: `rejected`", "base-r control-chart check", "pending before alpha",
    )
    require(all(term in reproduction for term in reproduction_terms), "Reproducibility record covers assembly, limits, and mutation routes")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(
        markdown_field(progression, "Checkpoint score") == "40 of 40"
        and markdown_field(progression, "Point source") == "Module 02 20 points once plus Module 03 20 points once",
        "Checkpoint score and point source are exact",
    )
    require(
        markdown_field(progression, "Module 01 decision gates") == "12 of 12 pass"
        and markdown_field(progression, "Module 02 measurement gates") == "15 of 15 pass"
        and markdown_field(progression, "Module 03 diagnostic gates") == "18 of 18 pass"
        and markdown_field(progression, "Checkpoint integrity gates") == "18 of 18 pass",
        "All inherited and checkpoint gate totals pass",
    )
    require(markdown_field(progression, "Failed gates") == "none", "No failed gate is hidden")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 04 permission")
    require(
        disposition in ALLOWED_PROGRESSION
        and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for demand forecasting and capacity analysis")),
        "Module 04 permission matches progression",
    )
    require(markdown_field(progression, "Root cause") == "not established", "Root cause remains unestablished")
    require(
        all(markdown_field(progression, label) == "prohibited" for label in (
            "Staffing change", "Clinical action", "Automated action", "Implementation",
        )),
        "Staffing, clinical, automated, and implementation action remain prohibited",
    )
    require(markdown_field(progression, "Machine learning") == "reserved for Module 06", "Machine learning remains owned by Module 06")
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) == 8, "Progression has eight owned conditions")

    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    labels = (
        "Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected",
        "Output used, modified, or rejected", "Material claim", "Independent verification",
        "Correction or retained action", "Human owner", "Accountability statement",
    )
    require(all(markdown_field(ai, label) for label in labels), "AI-use record has every accountable field")

    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 153}
    print(f"APP-3 Checkpoint 1 reference validation passed: {len(checks)} checks.")
    return report


def expect_rejection(
    reference: Path,
    base: Path,
    name: str,
    mutate: Callable[[Path], None],
    message_fragment: str,
) -> None:
    broken = base / name
    shutil.copytree(reference, broken)
    mutate(broken)
    try:
        validate(broken)
    except (OSError, ValidationError) as error:
        if message_fragment not in str(error):
            raise AssertionError(f"{name} failed for the wrong reason: {error}") from error
    else:
        raise AssertionError(f"Validator accepted {name}")


def replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"Mutation source not found in {path}: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def self_check() -> None:
    import build_checkpoint

    with tempfile.TemporaryDirectory(prefix="app3-cp01-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner = base / "reference", base / "learner"
        build_checkpoint.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run(
            [sys.executable, str(reference / "validate_checkpoint.py"), str(reference)],
            capture_output=True, text=True, check=False,
        )
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_checkpoint.assemble(learner)
        starter = validate(learner, learner=True)

        expect_rejection(
            reference, base, "changed-candidate",
            lambda root: replace(root / "candidate/module-03/outputs/signal-audit.csv", "S009", "S099"),
            "Candidate SHA-256 matches",
        )
        expect_rejection(
            reference, base, "missing-candidate",
            lambda root: (root / "candidate/module-03/outputs/signal-audit.csv").unlink(),
            "Checkpoint has exactly 153 expected files",
        )
        expect_rejection(
            reference, base, "changed-module01-points",
            lambda root: replace(root / "evidence-index.csv", ",0,12 of 12 pass", ",1,12 of 12 pass"),
            "points exactly once",
        )
        expect_rejection(
            reference, base, "duplicate-module02-points",
            lambda root: replace(root / "evidence-index.csv", ",20,15 of 15 pass", ",40,15 of 15 pass"),
            "points exactly once",
        )
        expect_rejection(
            reference, base, "duplicate-module03-points",
            lambda root: replace(root / "evidence-index.csv", ",20,18 of 18 pass", ",40,18 of 18 pass"),
            "points exactly once",
        )
        expect_rejection(
            reference, base, "wrong-total",
            lambda root: replace(root / "evidence-index.csv", ",20,15 of 15 pass", ",19,15 of 15 pass"),
            "points exactly once",
        )
        expect_rejection(
            reference, base, "failed-inherited-gate",
            lambda root: replace(root / "evidence-index.csv", "15 of 15 pass", "14 of 15 pass"),
            "inherited passing gates",
        )
        expect_rejection(
            reference, base, "failed-checkpoint-gate",
            lambda root: replace(root / "checkpoint-gates.csv", ",pass,", ",fail,"),
            "18 checkpoint integrity gates pass",
        )
        expect_rejection(
            reference, base, "changed-signal-count",
            lambda root: replace(root / "measures-variation-readiness-review.md", "nine signal records", "eight signal records"),
            "exact accepted evidence",
        )
        expect_rejection(
            reference, base, "signal-as-cause",
            lambda root: replace(root / "measures-variation-readiness-review.md", "A signal opens review and does not prove cause.", "The signal proves cause."),
            "signal and root-cause limits",
        )
        expect_rejection(
            reference, base, "staffing-claim",
            lambda root: replace(root / "measures-variation-readiness-review.md", "Root cause remains not established.", "Root cause remains not established. We recommend adding staff."),
            "no prohibited cause, staffing, automation, or implementation claim",
        )
        expect_rejection(
            reference, base, "unsupported-subgroup",
            lambda root: replace(root / "measures-variation-readiness-review.md", "Those cross-group comparisons are not supported.", "Those cross-group comparisons are supported."),
            "target-window subgroup limits",
        )
        expect_rejection(
            reference, base, "automated-escalation",
            lambda root: replace(root / "measures-variation-readiness-review.md", "It does not automate staffing", "It automates staffing"),
            "human escalation and action limits",
        )
        expect_rejection(
            reference, base, "incomplete-defense",
            lambda root: replace(root / "checkpoint-defense.md", "Answer: Module 04 may begin", "Response: Module 04 may begin"),
            "answers every question",
        )
        expect_rejection(
            reference, base, "invalid-progression",
            lambda root: replace(root / "progression-decision.md", "permitted for demand forecasting and capacity analysis", "not permitted"),
            "permission matches progression",
        )
        expect_rejection(
            reference, base, "missing-ai-field",
            lambda root: replace(root / "ai-use.md", "- Human owner: `Shuhan He and the named APP-3 faculty owner`", "- Human owner: ``"),
            "every accountable field",
        )
        expect_rejection(
            reference, base, "missing-reproduction-route",
            lambda root: replace(root / "reproducibility-check.md", "- Candidate mutation: `rejected`\n", ""),
            "mutation routes",
        )
        try:
            validate(learner)
        except ValidationError as error:
            assert "Reference record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted starter records as complete")

    print(
        f"APP-3 Checkpoint 1 validator self-check passed: {complete['checks_passed']} reference checks "
        f"and {starter['checks_passed']} learner checks; copied validation and eighteen failure routes verified."
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
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
