"""Validate an APP-5 Module 06 learner or reference workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import tempfile
from pathlib import Path

import build_workspace


ROOT = Path(__file__).resolve().parent
MODULE_ID = "oclc-app5-06"
MODULE_VERSION = "0.1.0"
COMMONS_RELEASE = "0.93.0"

CSV_ROWS = {
    "theory-of-change.csv": 7,
    "delivery-pathway.csv": 10,
    "implementation-measure-registry.csv": 8,
    "monitoring-plan.csv": 20,
    "readiness-capacity-review.csv": 6,
    "benefit-harm-balancing-register.csv": 8,
    "incident-escalation-register.csv": 4,
    "responsible-claims-audit.csv": 15,
    "week6-gate-results.csv": 34,
}


class ValidationError(RuntimeError):
    pass


class Audit:
    def __init__(self) -> None:
        self.checks = 0
        self.errors: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def finish(self) -> None:
        if self.errors:
            raise ValidationError("; ".join(self.errors[:20]))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def all_files(root: Path) -> set[str]:
    return {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}


def validate_manifest(root: Path, mode: str, audit: Audit) -> None:
    manifest_path = root / "release-manifest.csv"
    audit.check(manifest_path.is_file(), "Release manifest missing")
    if not manifest_path.is_file():
        return
    rows = read_csv(manifest_path)
    expected_rows = build_workspace.EXPECTED_REFERENCE_MANIFEST_ROWS if mode == "complete" else build_workspace.EXPECTED_LEARNER_MANIFEST_ROWS
    audit.check(len(rows) == expected_rows, "Release manifest row count changed")
    expected_paths = {row["relative_path"] for row in rows}
    editable = set(build_workspace.RECORD_FILES) | set(build_workspace.SQL_FILES)
    expected_files = expected_paths | editable | {"release-manifest.csv"}
    audit.check(all_files(root) == expected_files, "Workspace file set changed")
    for row in rows:
        path = root / row["relative_path"]
        audit.check(path.is_file(), f"Manifest file missing: {row['relative_path']}")
        if path.is_file():
            audit.check(path.stat().st_size == int(row["bytes"]), f"Manifest byte count changed: {row['relative_path']}")
            audit.check(sha256(path) == row["sha256"], f"Manifest SHA-256 changed: {row['relative_path']}")


def validate_structure(root: Path, mode: str, audit: Audit) -> list[Path]:
    editable = [root / name for name in build_workspace.RECORD_FILES + build_workspace.SQL_FILES]
    for path in editable:
        audit.check(path.is_file(), f"Editable record missing: {path.relative_to(root).as_posix()}")
    if any(not path.is_file() for path in editable):
        return editable
    texts = {path: path.read_text(encoding="utf-8") for path in editable}
    if mode == "learner":
        for path, text in texts.items():
            audit.check("REPLACE" in text, f"Learner prompt missing or reference answer copied: {path.relative_to(root).as_posix()}")
        audit.check(not (root / "outputs").exists(), "Learner workspace contains reference outputs")
    else:
        for path, text in texts.items():
            audit.check("REPLACE" not in text, f"Complete workspace contains a starter prompt: {path.relative_to(root).as_posix()}")
            audit.check("—" not in text and "–" not in text, f"Authored record contains an em or en dash: {path.relative_to(root).as_posix()}")
    return editable


def validate_complete(root: Path, audit: Audit) -> None:
    release = json.loads((root / "release.json").read_text(encoding="utf-8"))
    audit.check((root / "VERSION").read_text(encoding="utf-8").strip() == MODULE_VERSION, "Module version changed")
    audit.check(release["module_id"] == MODULE_ID and release["module_version"] == MODULE_VERSION, "Release identity changed")
    audit.check(release["commons_release"] == COMMONS_RELEASE, "Commons release changed")
    audit.check(release["course_points"] == 0 and release["week6_checkpoint_points_after_acceptance"] == 25, "Point carry changed")
    audit.check(release["challenger_release"]["stable_for_bounded_questions"] is False, "Failed challenger was accepted")

    report_path = root / "outputs/build-report.json"
    audit.check(report_path.is_file(), "Build report missing")
    if report_path.is_file():
        report = json.loads(report_path.read_text(encoding="utf-8"))
        audit.check(sha256(report_path) == "f53dc9a5b3274ee33917a3f78d1b0152f1dcaca232bc07de3b39045e5246f6f7", "Build report identity changed")
        audit.check(report["findings"]["monitoring_triggers"] == 6, "Monitoring trigger count changed")
        audit.check(report["findings"]["challenger_stable_for_bounded_questions"] is False, "Build accepted challenger")
        audit.check(report["findings"]["failed_query_checks"] == 0, "Build query checks failed")

    for name, count in CSV_ROWS.items():
        rows = read_csv(root / name)
        audit.check(len(rows) == count, f"Record row count changed: {name}")
        audit.check(all(all(value.strip() for value in row.values()) for row in rows), f"Complete record has blank values: {name}")

    theory = read_csv(root / "theory-of-change.csv")
    audit.check([row["step"] for row in theory] == [f"T{index:02d}" for index in range(1, 8)], "Theory steps changed")
    delivery = read_csv(root / "delivery-pathway.csv")
    audit.check([row["step_id"] for row in delivery] == [f"D{index:02d}" for index in range(1, 11)], "Delivery steps changed")

    monitoring = read_csv(root / "monitoring-plan.csv")
    audit.check([row["measure_id"] for row in monitoring] == [f"M{index:02d}" for index in range(1, 21)], "Monitoring measure IDs changed")
    audit.check(sum(row["result"] == "triggered" for row in monitoring) == 6, "Six declared monitoring triggers not preserved")
    audit.check(all(row["automatic_action"] == "no" for row in monitoring), "Monitoring creates automatic action")
    audit.check(sum(int(row["denominator"]) > 0 for row in monitoring) == 20, "Monitoring denominator unavailable or hidden")

    implementation = read_csv(root / "implementation-measure-registry.csv")
    audit.check(all(row["automatic_action"] == "no" for row in implementation), "Implementation registry creates automatic action")
    readiness = {row["condition"]: row for row in read_csv(root / "readiness-capacity-review.csv")}
    audit.check(readiness["staff_not_ready"]["affected_tracts"] == "5", "Staff concern count changed")
    audit.check(readiness["high_travel"]["affected_tracts"] == "12", "Travel concern count changed")
    audit.check(readiness["high_burden"]["affected_tracts"] == "1", "Burden concern count changed")

    incidents = read_csv(root / "incident-escalation-register.csv")
    audit.check(sum(int(row["records"]) for row in incidents) == 280, "Incident register does not reconcile")
    audit.check(sum(int(row["records"]) for row in incidents if row["incident_state"] != "none") == 23, "Incident test count changed")
    audit.check(all(row["automatic_action"] == "no" for row in incidents), "Incident register creates automatic action")

    gates = read_csv(root / "week6-gate-results.csv")
    audit.check([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 35)], "Gate IDs changed")
    audit.check(all(row["noncompensable"] == "yes" and row["status"] == "pass" for row in gates), "A noncompensable gate failed")

    claims = {row["claim_id"]: row for row in read_csv(root / "responsible-claims-audit.csv")}
    audit.check(claims["C06"]["status"] == "prohibited", "Effect claim allowed")
    audit.check(claims["C10"]["status"] == "prohibited", "Failed challenger called useful")
    audit.check(claims["C15"]["status"] == "prohibited", "Implementation or deployment claim allowed")

    model_card = (root / "cluster-model-card.md").read_text(encoding="utf-8")
    audit.check("The challenger fails and is not useful" in model_card, "Challenger failure not preserved")
    audit.check("nine fixed features" in model_card and "seed 73056" in model_card, "Fixed model contract changed")
    stability = (root / "cluster-stability-support-review.md").read_text(encoding="utf-8")
    audit.check("0.120" in stability and "only two" in stability and "rejected" in stability, "Stability failure changed")
    tailoring = (root / "tailoring-questions.md").read_text(encoding="utf-8")
    audit.check("supplies no accepted tailoring questions" in tailoring, "Failed cluster used for tailoring")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    audit.check("Continue with conditions" in progression and "adds zero points" in progression, "Progression or point carry changed")
    audit.check("unready for real implementation" in progression or "not ready for real implementation" in progression, "Intervention readiness overstated")
    evaluation = (root / "evaluation-proposal.md").read_text(encoding="utf-8")
    audit.check("provides no effect estimate" in evaluation and "APP-6 owns" in evaluation, "Effect boundary changed")
    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8")
    audit.check("f53dc9a5b3274ee33917a3f78d1b0152f1dcaca232bc07de3b39045e5246f6f7" in reproduction, "Reproduction identity changed")
    ai_record = (root / "ai-use.md").read_text(encoding="utf-8").lower()
    audit.check("no post-result tuning" in ai_record or "without post-result tuning" in ai_record, "AI record omits tuning accountability")

    for relative in build_workspace.SQL_FILES:
        sql = (root / relative).read_text(encoding="utf-8")
        audit.check("REPLACE" not in sql and "SELECT" in sql.upper(), f"Reference SQL incomplete: {relative}")


def validate(root: Path, mode: str = "complete") -> dict[str, object]:
    root = root.resolve()
    audit = Audit()
    audit.check(root.is_dir(), "Workspace directory missing")
    validate_manifest(root, mode, audit)
    validate_structure(root, mode, audit)
    if mode == "complete" and not audit.errors:
        validate_complete(root, audit)
    audit.finish()
    return {"status": "pass", "mode": mode, "checks": audit.checks}


def expect_rejected(root: Path, mode: str, label: str) -> None:
    try:
        validate(root, mode)
    except ValidationError:
        return
    raise AssertionError(f"Validator accepted protected failure: {label}")


def mutate_and_reject(root: Path, relative: str, transform, label: str) -> None:
    path = root / relative
    original = path.read_bytes()
    try:
        path.write_bytes(transform(original))
        expect_rejected(root, "complete", label)
    finally:
        path.write_bytes(original)


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app5-module06-validator-") as temporary:
        base = Path(temporary)
        reference = base / "reference"
        learner = base / "learner"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(learner, reference=False)
        complete = validate(reference, "complete")
        starter = validate(learner, "learner")
        expect_rejected(learner, "complete", "starter in complete mode")
        expect_rejected(reference, "learner", "copied reference answer in learner mode")

        mutate_and_reject(reference, "VERSION", lambda raw: b"0.1.1\n", "immutable version mutation")
        mutate_and_reject(reference, "cluster-model-card.md", lambda raw: raw + b"\nREPLACE\n", "starter marker in complete work")
        mutate_and_reject(reference, "cluster-model-card.md", lambda raw: raw.replace(b"fails and is not useful", b"passes and is useful"), "failed challenger accepted")
        mutate_and_reject(reference, "monitoring-plan.csv", lambda raw: raw.replace(b",no\n", b",yes\n", 1), "automatic monitoring action")
        mutate_and_reject(reference, "week6-gate-results.csv", lambda raw: raw.replace(b"G34,", b"G34,").replace(b",pass,progression-decision.md", b",fail,progression-decision.md"), "gate failure hidden")
        mutate_and_reject(reference, "progression-decision.md", lambda raw: raw.replace(b"adds zero points", b"adds five points"), "point carry changed")
        mutate_and_reject(reference, "evaluation-proposal.md", lambda raw: raw.replace(b"provides no effect estimate", b"provides an effect estimate"), "effect claim added")
        mutate_and_reject(reference, "incident-escalation-register.csv", lambda raw: raw.replace(b"access owner and program steward", b""), "incident owner removed")
        mutate_and_reject(reference, "reproducibility-check.md", lambda raw: raw.replace(b"f53dc9a5b3274ee33917a3f78d1b0152f1dcaca232bc07de3b39045e5246f6f7", b"0000000000000000000000000000000000000000000000000000000000000000"), "reproduction identity changed")
        mutate_and_reject(reference, "responsible-claims-audit.csv", lambda raw: raw.replace(b"C10,The challenger is useful,prohibited", b"C10,The challenger is useful,permitted"), "model claim allowed")
        mutate_and_reject(reference, "sql/04-audit-gates-points-and-authority.sql", lambda raw: raw + b"\n-- REPLACE\n", "incomplete SQL")
        mutate_and_reject(reference, "tailoring-questions.md", lambda raw: raw + "\nAn em dash — is prohibited.\n".encode("utf-8"), "authored em dash")

    print(json.dumps({"status": "pass", "complete_checks": complete["checks"], "starter_checks": starter["checks"], "protected_failure_routes": 14}, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path, default=ROOT)
    parser.add_argument("--mode", choices=("complete", "learner"), default="complete")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        else:
            print(json.dumps(validate(args.workspace, args.mode), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, ValidationError) as error:
        parser.exit(1, f"Workspace validation failed: {error}\n")


if __name__ == "__main__":
    main()
