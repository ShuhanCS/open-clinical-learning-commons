"""Validate an assembled FND-2 Checkpoint 1 release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from decimal import Decimal
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
EDITABLE_RECORDS = (
    "README.md", "cumulative-interpretation.md", "technical-defense.md",
    "component-score.csv", "gate-results.csv", "reviewer-record.md",
    "reproduction-record.md", "accessibility-review.md", "ai-use.md",
    "progression-decision.md",
)
ROOT_FILES = (
    ".gitattributes", ".gitignore", "VERSION", "checkpoint-contract.json",
    "assessment.md", "validate_checkpoint.py", "release-manifest.csv",
) + EDITABLE_RECORDS
KEY_HASHES = {
    "modules/01-aims-reproducible-workspace/outputs/modeling-cohort.csv": "6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332",
    "modules/01-aims-reproducible-workspace/outputs/split-registry.csv": "05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1",
    "modules/02-regression-interpretation/formula-registry.csv": "fc69d6146eec729969b571b535c13027e9b875d34dd99637f0dc0d9b934239a6",
    "modules/03-prediction-evaluation/outputs/test-predictions.csv": "531c00d310292aeeaea476d1c94e128f5c81c34c2fc60e014d2c157e152b7438",
}
CRITERIA = ("A01", "A02", "A03", "A04", "R01", "R02", "P01", "P02", "P03", "H01")
AVAILABLE = tuple(Decimal(value) for value in ("4.00", "4.00", "3.00", "4.00", "4.50", "5.50", "4.50", "4.50", "3.50", "2.50"))
GATES = tuple(f"G{index:02d}" for index in range(1, 24))


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


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    require(root.is_dir(), "Checkpoint directory exists")
    for relative in ROOT_FILES:
        require((root / relative).is_file(), f"Required root file exists: {relative}")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Checkpoint version is 0.1.0")

    contract = json.loads((root / "checkpoint-contract.json").read_text(encoding="utf-8"))
    require(contract["checkpoint"]["id"] == "oclc-fnd2-cp1", "Checkpoint ID matches")
    require(contract["checkpoint"]["commons_release"] == "0.42.0", "Commons release matches")
    require(contract["package"] == {"upstream_artifacts": 72, "checkpoint_control_artifacts": 6, "manifest_rows": 78, "editable_records": 10, "assembled_files": 89}, "Package contract matches")
    require(contract["assessment"]["required_gates"] == 23, "Gate contract matches")
    require(contract["assessment"]["defense_questions"] == 12, "Defense contract matches")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "source_unit", "source_version", "bytes", "sha256"], "Manifest header matches")
    require(len(manifest) == 78, "Manifest has 78 rows")
    paths = [row["relative_path"] for row in manifest]
    require(paths == sorted(paths), "Manifest paths are sorted")
    require(len(paths) == len(set(paths)), "Manifest paths are unique")
    for row in manifest:
        relative = row["relative_path"]
        candidate = Path(relative)
        require(not candidate.is_absolute() and ".." not in candidate.parts, f"Manifest path is safe: {relative}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {relative}")
        require(path.stat().st_size == int(row["bytes"]), f"Manifest bytes match: {relative}")
        require(sha256(path) == row["sha256"], f"Manifest SHA-256 matches: {relative}")
        require(row["source_version"] == "0.1.0", f"Manifest source version matches: {relative}")
    require(sum(path.is_file() for path in root.rglob("*")) == 89, "Assembled package has 89 files")

    for relative, digest in KEY_HASHES.items():
        require(sha256(root / relative) == digest, f"Key fingerprint matches: {relative}")
    for module in ("01-aims-reproducible-workspace", "02-regression-interpretation", "03-prediction-evaluation"):
        require((root / "modules" / module / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", f"Module version matches: {module}")

    m1 = json.loads((root / "modules/01-aims-reproducible-workspace/outputs/build-report.json").read_text(encoding="utf-8"))
    require(m1["source"]["rows"] == 374 and m1["source"]["fields"] == 29, "Accepted FND-1 source shape matches")
    require([m1["split"][name]["rows"] for name in ("train", "validation", "test")] == [224, 75, 75], "Split rows match")
    require([m1["split"][name]["positives"] for name in ("train", "validation", "test")] == [25, 7, 4], "Split outcomes match")
    require(m1["baseline"]["constant_probability"] == "0.111607142857", "Baseline probability matches")

    m2 = json.loads((root / "modules/02-regression-interpretation/outputs/build-report.json").read_text(encoding="utf-8"))
    require(m2["linear_case"] == {"all_recorded_rows": 111, "training_rows": 69, "structural_blanks": 263}, "Linear case matches")
    require(m2["logistic_case"]["training_rows"] == 224 and m2["logistic_case"]["positives"] == 25, "Logistic case matches")
    _, regression_checks = read_csv(root / "modules/02-regression-interpretation/outputs/regression-checks.csv")
    require(len(regression_checks) == 24 and all(row["status"] == "pass" for row in regression_checks), "All 24 regression checks pass")

    m3 = json.loads((root / "modules/03-prediction-evaluation/outputs/build-report.json").read_text(encoding="utf-8"))
    require(m3["selection"] == {"model_id": "ML01", "locked_threshold": "0.08513264", "test_opened_after_lock": True}, "Selection and threshold match")
    require(m3["test_confusion"] == {"true_negative": 48, "false_positive": 23, "false_negative": 2, "true_positive": 2}, "Test confusion matches")
    _, prediction_checks = read_csv(root / "modules/03-prediction-evaluation/outputs/prediction-checks.csv")
    require(len(prediction_checks) == 22 and all(row["status"] == "pass" for row in prediction_checks), "All 22 prediction checks pass")
    _, leak = read_csv(root / "modules/03-prediction-evaluation/outputs/leaked-model-failure.csv")
    require(leak[0]["selection_eligibility"] == "never eligible", "Leaked model remains ineligible")
    _, subgroups = read_csv(root / "modules/03-prediction-evaluation/outputs/subgroup-metrics.csv")
    require(len(subgroups) == 10 and sum(row["suppressed"] == "yes" for row in subgroups) == 5, "Subgroup suppression matches")

    for relative in EDITABLE_RECORDS:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        if not starter:
            require(not PLACEHOLDER.search(text), f"Record is complete: {relative}")

    score_header, scores = read_csv(root / "component-score.csv")
    require(score_header == ["criterion_id", "component", "course_points_available", "points_earned", "status", "evidence"], "Score header matches")
    require(tuple(row["criterion_id"] for row in scores) == CRITERIA, "Score criteria match")
    require(tuple(Decimal(row["course_points_available"]) for row in scores) == AVAILABLE, "Available points match")
    require(sum(AVAILABLE) == Decimal("40.00"), "Available points total 40.00")
    if not starter:
        earned = tuple(Decimal(row["points_earned"]) for row in scores)
        require(all(Decimal("0") <= value <= available for value, available in zip(earned, AVAILABLE, strict=True)), "Earned points are in range")
        require(sum(earned) >= Decimal("32.00"), "Earned points meet 32.00 minimum")
        require(all(row["status"] in {"pass", "pass with conditions"} for row in scores), "All score rows pass")
        require(all(row["evidence"].strip() for row in scores), "Every score row cites evidence")

    gate_header, gates = read_csv(root / "gate-results.csv")
    require(gate_header == ["gate_id", "gate", "status", "evidence", "reviewer_note"], "Gate header matches")
    require(tuple(row["gate_id"] for row in gates) == GATES, "Gate IDs match")
    if not starter:
        require(all(row["status"] == "pass" for row in gates), "All 23 gates pass")
        require(all(row["evidence"].strip() and row["reviewer_note"].strip() for row in gates), "Every gate has evidence and a note")

    defense = (root / "technical-defense.md").read_text(encoding="utf-8")
    require(len(re.findall(r"(?m)^\d+\.", defense)) == 12, "Defense has 12 numbered answers")
    if not starter:
        require(re.search(r"(?im)^- Status:\s*`?adequate`?\s*$", defense) is not None, "Defense is adequate")

    cumulative = (root / "cumulative-interpretation.md").read_text(encoding="utf-8").lower()
    if not starter:
        for phrase in ("374", "224", "75", "25", "0.111607142857", "263", "2.20423495", "ml01", "leak01", "0.08513264", "48 true negatives", "23 false positives", "four outcomes", "deployment"):
            require(phrase in cumulative, f"Cumulative interpretation includes: {phrase}")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8").lower()
    if not starter:
        disposition_match = re.search(r"(?m)^- disposition:\s*`?(accept with conditions|accept|revise|refer)`?\s*$", progression)
        require(disposition_match is not None, "Progression disposition is allowed")
        permission_match = re.search(r"(?m)^- module 04 permission:\s*`?(permitted|not permitted)`?\s*$", progression)
        require(permission_match is not None, "Module 04 permission is explicit")
        allowed = disposition_match.group(1) in {"accept", "accept with conditions"}
        require((permission_match.group(1) == "permitted") == allowed, "Permission matches disposition")
        require("48" in progression and "23" in progression and "2" in progression, "Progression preserves exact test counts")

    report = {"status": "pass", "mode": "starter" if starter else "complete", "checks_passed": len(checks), "manifest_rows": len(manifest), "course_points": "40.00"}
    print(f"FND-2 Checkpoint 1 {report['mode']} validation passed: {len(checks)} checks.")
    return report


def self_check() -> None:
    import assemble_checkpoint

    with tempfile.TemporaryDirectory(prefix="fnd2-checkpoint1-validate-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        assemble_checkpoint.assemble(reference, assemble_checkpoint.REFERENCE_MODULES, reference=True)
        complete_report = validate(reference)
        assemble_checkpoint.assemble(starter, assemble_checkpoint.REFERENCE_MODULES, reference=False)
        starter_report = validate(starter, starter=True)
        try:
            validate(starter)
        except ValidationError as error:
            assert "Record is complete" in str(error)
        else:
            raise AssertionError("Validator accepted prompted starter as complete")

        broken = base / "broken"
        shutil.copytree(reference, broken)
        (broken / "modules/03-prediction-evaluation/outputs/test-predictions.csv").unlink()
        try:
            validate(broken)
        except ValidationError as error:
            assert "Manifest file exists" in str(error)
        else:
            raise AssertionError("Validator accepted missing immutable evidence")

        bad_score = base / "bad-score"
        shutil.copytree(reference, bad_score)
        score = (bad_score / "component-score.csv").read_text(encoding="utf-8").replace("A01,Module 01,4.00,4.00", "A01,Module 01,4.00,5.00")
        (bad_score / "component-score.csv").write_text(score, encoding="utf-8", newline="")
        try:
            validate(bad_score)
        except ValidationError as error:
            assert "Earned points are in range" in str(error)
        else:
            raise AssertionError("Validator accepted out-of-range score")

        failed_gate = base / "failed-gate"
        shutil.copytree(reference, failed_gate)
        gates = (failed_gate / "gate-results.csv").read_text(encoding="utf-8").replace(",pass,", ",revise,", 1)
        (failed_gate / "gate-results.csv").write_text(gates, encoding="utf-8", newline="")
        try:
            validate(failed_gate)
        except ValidationError as error:
            assert "All 23 gates pass" in str(error)
        else:
            raise AssertionError("Validator accepted a failed gate")
    print(f"FND-2 Checkpoint 1 validator self-check passed: {complete_report['checks_passed']} complete checks and {starter_report['checks_passed']} starter checks; incomplete and broken packages rejected.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", nargs="?", type=Path, default=PACKAGE_ROOT)
    parser.add_argument("--starter", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        validate(args.checkpoint.resolve(), starter=args.starter)
    except (OSError, ValueError, KeyError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
