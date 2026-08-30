"""Validate the APP-2 cumulative Week 3 checkpoint."""

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


CHECKPOINT_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
IMMUTABLE_FILES = (".gitattributes", "VERSION", "checkpoint-contract.json", "assessment.md", "instructor-notes.md", "build_checkpoint.py", "validate_checkpoint.py")
WORK_FILES = ("README.md", "evidence-index.csv", "measurement-representation-review.md", "reproducibility-check.md", "ai-use.md", "progression-decision.md")
MODULES = {
    "module-01": {"id": "oclc-app2-01", "version": "0.1.0", "commons_release": "0.56.0", "files": 25, "immutable_rows": 15, "manifest_bytes": 1787, "manifest_sha256": "c693e04592994f6f7bef14459b83669a5c824d0bf0b027a0624bab12a3cb4862"},
    "module-02": {"id": "oclc-app2-02", "version": "0.1.0", "commons_release": "0.57.0", "files": 66, "immutable_rows": 52, "manifest_bytes": 6890, "manifest_sha256": "c261307b45be842c00c9ded66614a3770f379d41a1d7efecb68032f9c090a870"},
    "module-03": {"id": "oclc-app2-03", "version": "0.1.0", "commons_release": "0.58.0", "files": 44, "immutable_rows": 31, "manifest_bytes": 4045, "manifest_sha256": "3d7787a975335518cf4a4f50b5561a323707e2acea6bd1724b1c92a565f64a30"},
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
    require(header == ["relative_path", "bytes", "sha256", "source_module", "source_version", "role"], "Candidate manifest header matches")
    require(len(manifest) == 135 and [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Candidate manifest has 135 sorted rows")
    expected = required | {row["relative_path"] for row in manifest}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    require(actual == expected and len(actual) == 149, "Checkpoint has exactly 149 expected files")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Candidate file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Candidate bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Candidate SHA-256 matches: {row['relative_path']}")
        directory = row["relative_path"].split("/")[1]
        require(row["source_module"] == MODULES[directory]["id"] and row["source_version"] == MODULES[directory]["version"], f"Candidate source identity matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version matches")
    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(contract["checkpoint_id"] == "oclc-app2-cp01" and contract["version"] == "0.1.0" and contract["commons_release"] == "0.58.0", "Checkpoint identity matches")
    require(contract["course_points"] == 20 and contract["point_source"] == "oclc-app2-02 exactly once", "Checkpoint point contract matches")
    require(contract["accepted_component_files"] == 135 and len(contract["accepted_modules"]) == 3, "Contract accepts 135 files from three modules")
    require(sum(module["points"] for module in contract["accepted_modules"]) == 20 and [module["points"] for module in contract["accepted_modules"]] == [0, 20, 0], "Contract assigns 20 points to Module 02 only")

    for directory, details in MODULES.items():
        module_root = root / "candidate" / directory
        files = [path for path in module_root.rglob("*") if path.is_file() and "__pycache__" not in path.parts]
        require(len(files) == details["files"], f"{directory} file count matches")
        require((module_root / "VERSION").read_text(encoding="utf-8").strip() == details["version"], f"{directory} version matches")
        nested = module_root / "release-manifest.csv"
        require(nested.stat().st_size == details["manifest_bytes"], f"{directory} nested manifest bytes match")
        require(sha256(nested) == details["manifest_sha256"], f"{directory} nested manifest SHA-256 matches")
        nested_header, nested_rows = read_csv(nested)
        require(nested_header == ["relative_path", "bytes", "sha256", "role"], f"{directory} nested manifest header matches")
        require(len(nested_rows) == details["immutable_rows"], f"{directory} nested immutable row count matches")
        for row in nested_rows:
            path = module_root / row["relative_path"]
            require(path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"{directory} nested artifact matches: {row['relative_path']}")

    for name in WORK_FILES:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if learner:
            require(bool(PLACEHOLDER.search(text)), f"Learner prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Reference record is complete: {name}")
    if learner:
        report = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 149}
        print(f"APP-2 Checkpoint 1 learner validation passed: {len(checks)} checks.")
        return report

    index_header, index_rows = read_csv(root / "evidence-index.csv")
    require(index_header == ["module_id", "title", "version", "commons_release", "assembled_files", "manifest_bytes", "manifest_sha256", "checkpoint_points", "gates", "progression", "accepted_decision", "role"], "Evidence index header matches")
    require(len(index_rows) == 3 and [row["module_id"] for row in index_rows] == ["oclc-app2-01", "oclc-app2-02", "oclc-app2-03"], "Evidence index has three ordered modules")
    require(sum(Decimal(row["checkpoint_points"]) for row in index_rows) == Decimal("20.00") and [row["checkpoint_points"] for row in index_rows] == ["0.00", "20.00", "0.00"], "Evidence index assigns 20 points exactly once")
    for row, details in zip(index_rows, MODULES.values(), strict=True):
        require(row["version"] == details["version"] and row["commons_release"] == details["commons_release"], f"Evidence index version matches: {row['module_id']}")
        require(int(row["assembled_files"]) == details["files"] and int(row["manifest_bytes"]) == details["manifest_bytes"] and row["manifest_sha256"] == details["manifest_sha256"], f"Evidence index manifest matches: {row['module_id']}")
    require(index_rows[1]["gates"] == "18 of 18 pass" and index_rows[2]["gates"] == "19 of 19 pass", "Evidence index carries measurement and response gates")

    review = (root / "measurement-representation-review.md").read_text(encoding="utf-8")
    required_values = ("20.00 of 20.00", "19,140", "18,683", "1,255", "18,879,474.284615", "782", "62.31075697", "642", "585", "589", "13 observed", "3.13328156", "3.0 bound", "548.95483815", "527.00399458", "3.14500108", "5.26048779", "4.20274444")
    require(all(value in review for value in required_values), "Integrated review contains exact measurement and response evidence")
    review_lower = review.lower()
    require("does not remove bias" in review_lower and "not an official meps or hcahps weight" in review_lower and "100 percent only by construction" in review_lower, "Integrated review contains weight, bias, and coverage boundaries")
    require("does not establish a real patient" in review_lower and "real fielding" in review_lower, "Integrated review contains data-class and fielding boundaries")

    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require("135" in reproduction and "two independent reference builds match byte for byte" in reproduction and "20.00 points appear on module 02 once" in reproduction, "Reproducibility record covers assembly and point integrity")
    require("candidate mutation" in reproduction and "duplicate-point mutation" in reproduction and "failed-gate mutation" in reproduction, "Reproducibility record covers mutation routes")

    module02 = root / "candidate/module-02"
    score_header, score = read_csv(module02 / "measurement-score.csv")
    require(len(score) == 5 and sum(Decimal(row["points_awarded"]) for row in score) == Decimal("20"), "Accepted Module 02 score totals 20")
    m02_gate_header, m02_gates = read_csv(module02 / "gate-results.csv")
    require(len(m02_gates) == 18 and all(row["status"] == "pass" for row in m02_gates), "Accepted Module 02 has 18 passing measurement gates")
    m02_progression = (module02 / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(m02_progression, "Module 03 permission") == "permitted for response and representation study", "Accepted Module 02 permits the response study")

    module03 = root / "candidate/module-03"
    flow_header, flow = read_csv(module03 / "outputs/response-flow.csv")
    require([row["count"] for row in flow] == ["1255", "1255", "1255", "782", "642", "585", "589"], "Accepted Module 03 response flow matches")
    cell_header, cells = read_csv(module03 / "outputs/weight-cells.csv")
    require(len(cells) == 13 and sum(row["bound_hit"] == "yes" for row in cells) == 1 and max(float(row["bounded_response_factor"]) for row in cells) == 3.0, "Accepted Module 03 response cells and bound match")
    diagnostic_header, diagnostics = read_csv(module03 / "outputs/weight-diagnostics.csv")
    require([row["kish_effective_n"] for row in diagnostics] == ["548.95483815", "527.00399458"], "Accepted Module 03 effective sample sizes match")
    estimate_header, estimates = read_csv(module03 / "outputs/estimate-comparison.csv")
    adjusted = {row["measure"]: row for row in estimates if row["estimator"] == "respondent_response_adjusted"}
    require([adjusted[name]["absolute_bias_pp"] for name in ("Q22", "Q23", "teaching_composite")] == ["3.14500108", "5.26048779", "4.20274444"], "Accepted Module 03 residual bias matches")
    m03_gate_header, m03_gates = read_csv(module03 / "gate-results.csv")
    require(len(m03_gates) == 19 and all(row["status"] == "pass" for row in m03_gates), "Accepted Module 03 has 19 passing response gates")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Checkpoint score") == "20.00 of 20.00" and markdown_field(progression, "Point source") == "Module 02 exactly once", "Checkpoint score and point source are exact")
    require(markdown_field(progression, "Module 02 measurement gates") == "18 of 18 pass" and markdown_field(progression, "Module 03 response gates") == "19 of 19 pass" and markdown_field(progression, "Checkpoint integrity gates") == "15 of 15 pass", "All gate totals pass")
    require(markdown_field(progression, "Failed gates") == "none", "No failed gate is hidden")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 04 permission")
    require(disposition in ALLOWED_PROGRESSION and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for linked analysis")), "Module 04 permission matches progression")
    require(all(markdown_field(progression, label) == "prohibited" for label in ("Clinical action", "Hospital ranking", "Real fielding", "Patient targeting")), "Clinical, ranking, fielding, and targeting remain prohibited")
    require(markdown_field(progression, "Machine learning") == "reserved for Module 06", "Machine learning remains owned by Module 06")
    require(len(re.findall(r"(?m)^\| C\d{2} \|", progression)) == 8, "Progression has eight owned conditions")

    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    labels = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in labels), "AI-use record has every accountable field")
    report = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 149}
    print(f"APP-2 Checkpoint 1 reference validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import build_checkpoint

    with tempfile.TemporaryDirectory(prefix="app2-cp01-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner = base / "reference", base / "learner"
        build_checkpoint.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_checkpoint.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_checkpoint.assemble(learner)
        starter = validate(learner, learner=True)

        broken = base / "broken-candidate"
        shutil.copytree(reference, broken)
        path = broken / "candidate/module-03/outputs/response-flow.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",782,", ",781,", 1), encoding="utf-8", newline="\n")
        try:
            validate(broken)
        except ValidationError as error:
            assert "Candidate SHA-256 matches" in str(error) or "Candidate bytes match" in str(error)
        else:
            raise AssertionError("Validator accepted a candidate mutation")

        duplicate = base / "duplicate-points"
        shutil.copytree(reference, duplicate)
        path = duplicate / "evidence-index.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",0.00,12 of 12 pass", ",20.00,12 of 12 pass", 1), encoding="utf-8", newline="\n")
        try:
            validate(duplicate)
        except ValidationError as error:
            assert "20 points exactly once" in str(error)
        else:
            raise AssertionError("Validator accepted duplicate checkpoint points")

        bad_gate = base / "bad-gate"
        shutil.copytree(reference, bad_gate)
        path = bad_gate / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("19 of 19 pass", "18 of 19 pass", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_gate)
        except ValidationError as error:
            assert "All gate totals pass" in str(error)
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
    print(f"APP-2 Checkpoint 1 validator self-check passed: {complete['checks_passed']} reference checks and {starter['checks_passed']} learner checks; copied and mutation routes verified.")


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
