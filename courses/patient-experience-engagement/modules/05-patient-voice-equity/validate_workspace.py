"""Validate an APP-2 Module 05 learner or reference workspace."""

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

import build_workspace


IMMUTABLE_FILES = build_workspace.IMMUTABLE_FILES
RECORD_FILES = build_workspace.RECORD_FILES
PLACEHOLDER = re.compile(r"\bREPLACE\b")
PERSONAL_PATH = re.compile(r"(?im)[A-Z]:\\Users\\")
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise and resubmit", "stop or refer"}


class ValidationError(ValueError):
    """Raised when a workspace violates the release contract."""


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

    required = set(IMMUTABLE_FILES) | set(RECORD_FILES) | {"release-manifest.csv"}
    require(root.is_dir(), "Workspace directory exists")
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    require(actual == required and len(actual) == 49, "Workspace has exactly 49 expected files")
    header, manifest = read_csv(root / "release-manifest.csv")
    require(header == ["relative_path", "bytes", "sha256", "role"], "Release manifest header matches")
    require(len(manifest) == 33 and [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Release manifest has 33 sorted immutable rows")
    require({row["relative_path"] for row in manifest} == set(IMMUTABLE_FILES), "Release manifest covers every immutable file")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Immutable file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Immutable bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Immutable SHA-256 matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    contract = json.loads((root / "voice-equity-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app2-05", "version": "0.1.0", "commons_release": "0.60.0", "week": 5, "hours": 16.0, "course_points": 20}, "Module identity and points match")
    require(contract["upstream"]["module04_manifest_sha256"] == "bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8" and contract["upstream"]["permission"] == "permitted for patient-voice and equity analysis", "Module 04 identity and permission match")
    require(contract["synthetic_comments"] == {"seed": "oclc-app2-05-v1", "opportunities": 782, "received_comments": 420, "double_coded_comments": 120, "themes": 8, "real_patient_text": False}, "Synthetic comment contract matches")
    require(contract["permissions"]["machine_learning"] == "reserved for Module 06" and contract["permissions"]["clinical_action"] == "prohibited", "ML and clinical permissions remain bounded")

    upstream_header, upstream = read_csv(root / "data/upstream-inventory.csv")
    require(upstream_header == ["source_id", "title", "relative_path", "bytes", "sha256", "role"], "Upstream inventory header matches")
    require(len(upstream) == 5 and sum(int(row["bytes"]) for row in upstream) == 5297691, "Upstream inventory has five files and 5,297,691 bytes")
    for row in upstream:
        path = root / row["relative_path"]
        require(path.is_file() and path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"Upstream fingerprint matches: {row['relative_path']}")
    release = json.loads((root / "data/upstream/module04-release.json").read_text(encoding="utf-8"))
    require(release["module"]["id"] == "oclc-app2-04" and release["module"]["version"] == "0.1.0" and release["package"]["manifest_sha256"] == "bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8", "Accepted Module 04 release identity matches")
    require(release["progression"]["module05_permission"] == "permitted for patient-voice and equity analysis", "Accepted release permits Module 05")

    person_header, people = read_csv(root / "data/upstream/module04-linked-persons.csv")
    event_header, events = read_csv(root / "data/upstream/module04-linked-events.csv")
    require(len(people) == 1255 and len(events) == 28455, "Accepted teaching tables have 1,255 people and 28,455 events")
    require("DUPERSID" not in person_header and "DUPERSID" not in event_header and "EVNTIDX" not in event_header, "Direct public-use person and event identifiers are absent")
    require(sum(row["response_status"] == "respondent" for row in people) == 782, "Accepted synthetic respondent count is 782")
    source_header, sources = read_csv(root / "data/upstream/module04-source-inventory.csv")
    require(len(sources) == 25 and all(row["url"].startswith("https://meps.ahrq.gov/") for row in sources), "Accepted inventory points to 25 official MEPS files with complete URLs")
    denominator_header, denominators = read_csv(root / "data/upstream/module04-denominator-registry.csv")
    require(len(denominators) == 14 and any(row["denominator_id"] == "D022" and row["unweighted_n"] == "0" for row in denominators), "Accepted denominators retain the zero-record portal evidence gap")

    opportunity_header, opportunities = read_csv(root / "data/synthetic/comment-opportunities.csv")
    comment_header, comments = read_csv(root / "data/synthetic/synthetic-comments.csv")
    sample_header, sample = read_csv(root / "data/synthetic/double-coding-sample.csv")
    require(len(opportunities) == 782 and len(comments) == 420 and len(sample) == 120, "Synthetic opportunity, comment, and coding-sample rows match")
    require(len({row["opportunity_id"] for row in opportunities}) == 782 and len({row["comment_id"] for row in comments}) == 420, "Synthetic opportunity and comment IDs are unique")
    require(sum(row["comment_returned"] == "yes" for row in opportunities) == 420, "Exactly 420 synthetic opportunities return a comment")
    require({row["comment_id"] for row in comments} == {row["comment_id"] for row in opportunities if row["comment_returned"] == "yes"}, "Received comment IDs match returned opportunities")
    require(all(row["data_class"] == "fully_synthetic_comment_linked_to_public_derived_meps" and row["comment_language"] == "synthetic English" and row["comment_text"].strip() for row in comments), "Every comment is nonempty and explicitly synthetic")
    require(all(row["coder_a_theme"] == row["coder_b_theme"] == row["adjudicated_theme"] == "" for row in sample), "Learner coding sample contains no hidden completed labels")
    require({row["comment_id"] for row in sample} <= {row["comment_id"] for row in comments}, "Every coding-sample record maps to a synthetic comment")

    profile_header, profile = read_csv(root / "outputs/source-profile.csv")
    require(profile_header == ["metric", "value", "unit", "evidence"] and len(profile) == 14, "Source profile has fourteen metrics")
    profile_map = {row["metric"]: row["value"] for row in profile}
    require(profile_map["synthetic_comment_opportunities"] == "782" and profile_map["synthetic_comments_received"] == "420" and profile_map["portal_preference_denominator"] == "0", "Source profile preserves comment counts and portal gap")
    codebook_header, codebook = read_csv(root / "outputs/comment-codebook.csv")
    require(len(codebook) == 8 and {row["theme"] for row in codebook} == {"communication_clarity", "medication_help", "warning_signs", "access_after_hours", "cost_barrier", "digital_channel", "respect_involvement", "other_or_unclear"}, "Codebook has eight fixed themes")
    require(all(row["include"] and row["exclude"] and row["anchor_language"] and "one primary theme" in row["coding_rule"] for row in codebook), "Every codebook theme has inclusion exclusion anchor and ambiguity rules")
    flow_header, flow = read_csv(root / "outputs/comment-flow.csv")
    require(len(flow) == 9 and flow[0]["opportunities"] == "782" and flow[0]["comments_received"] == "420" and flow[0]["return_percent"] == "53.70843990", "Comment flow has nine rows and exact total")
    require(all("not a real response rate" in row["claim_limit"] for row in flow), "Every comment-flow row rejects real response and preference claims")
    agreement_header, agreement = read_csv(root / "outputs/agreement-summary.csv")
    require(len(agreement) == 9 and agreement[0]["records"] == "120" and agreement[0]["agreements"] == "96" and agreement[0]["percent_agreement"] == "80.00000000" and agreement[0]["cohens_kappa"] == "0.77142857", "Agreement summary has exact audit facts")
    assisted_header, assisted = read_csv(root / "outputs/assisted-classification-audit.csv")
    require(len(assisted) == 9 and assisted[0]["benchmark_n"] == "120" and assisted[0]["accuracy"] == "0.78333333" and assisted[0]["recall"] == "0.78333333", "Assisted audit has exact benchmark accuracy and macro recall")
    require(all("human" in row["human_review_rule"] for row in assisted), "Every assisted-audit row keeps human review")
    theme_header, themes = read_csv(root / "outputs/theme-summary.csv")
    require(len(themes) == 8 and sum(int(row["received_comments"]) for row in themes) == 420 and all("not prevalence" in row["claim_limit"] for row in themes), "Theme summary has eight themes and rejects prevalence")
    example_header, examples = read_csv(root / "outputs/comment-examples.csv")
    require(len(examples) == 16 and all("generated teaching text" in row["example_status"] for row in examples), "Comment examples have two generated records per theme")

    support_header, support = read_csv(root / "outputs/group-support.csv")
    require(len(support) == 13 and {row["dimension"] for row in support} == {"other_language_at_home", "income_group", "insurance_coverage", "race_ethnicity"}, "Group support has thirteen rows across four dimensions")
    estimates_header, estimates = read_csv(root / "outputs/group-estimates.csv")
    require(len(estimates) == 52 and sum(row["support_status"] == "supported" for row in estimates) == 35, "Group estimates have 52 rows and 35 supported estimates")
    require(all((row["weighted_percent"] and row["survey_se_pp"] and row["ci95_low_percent"] and row["ci95_high_percent"]) if row["support_status"] == "supported" else (not row["weighted_percent"] and not row["survey_se_pp"] and not row["ci95_low_percent"] and not row["ci95_high_percent"]) for row in estimates), "Supported estimates are complete and suppressed estimates stay blank")
    estimate_map = {(row["dimension"], row["group"], row["measure"]): row for row in estimates}
    require(estimate_map[("income_group", "lower income", "delayed_for_cost")]["weighted_percent"] == "10.20205820" and estimate_map[("income_group", "middle or high income", "delayed_for_cost")]["weighted_percent"] == "6.18067839", "Lower and reference income delayed-cost estimates match")
    require(estimate_map[("insurance_coverage", "uninsured", "any_telehealth_event")]["support_status"] == "suppressed" and estimate_map[("race_ethnicity", "non-Hispanic Asian only", "delayed_for_cost")]["support_status"] == "suppressed", "Sparse insurance and race estimates remain suppressed")
    contrasts_header, contrasts = read_csv(root / "outputs/group-contrasts.csv")
    require(len(contrasts) == 36 and sum(row["support_status"] == "supported" for row in contrasts) == 19, "Group contrasts have 36 rows and 19 supported contrasts")
    require(all((row["difference_pp"] and row["survey_se_pp"] and row["ci95_low_pp"] and row["ci95_high_pp"]) if row["support_status"] == "supported" else (not row["difference_pp"] and not row["survey_se_pp"] and not row["ci95_low_pp"] and not row["ci95_high_pp"]) for row in contrasts), "Supported contrasts are complete and suppressed contrasts stay blank")
    contrast_map = {(row["dimension"], row["group"], row["measure"]): row for row in contrasts}
    require(contrast_map[("income_group", "lower income", "delayed_for_cost")]["difference_pp"] == "4.02137981" and contrast_map[("income_group", "lower income", "delayed_for_cost")]["ci95_low_pp"] == "0.59188925", "Primary delayed-cost contrast matches")
    require(contrast_map[("race_ethnicity", "non-Hispanic Black only", "delayed_for_cost")]["support_status"] == "suppressed", "Sparse positive-count contrast remains suppressed")
    exclusion_header, exclusion = read_csv(root / "outputs/channel-exclusion-audit.csv")
    require(len(exclusion) == 13 and all("synthetic procedural" in row["data_class"] and "not observed" in row["claim_limit"] for row in exclusion), "Channel-exclusion audit has thirteen bounded synthetic rows")
    invariant_header, invariants = read_csv(root / "outputs/invariant-checks.csv")
    require(len(invariants) == 28 and [row["check_id"] for row in invariants] == [f"I{number:02d}" for number in range(1, 29)] and all(row["status"] == "pass" for row in invariants), "All 28 evidence invariants pass in order")
    report = json.loads((root / "build-report.json").read_text(encoding="utf-8"))
    require(report["status"] == "pass" and report["synthetic_comments"]["received"] == 420 and report["synthetic_comments"]["real_patient_text_rows"] == 0, "Build report preserves synthetic comment identity")
    require(report["group_review"]["estimate_rows"] == 52 and report["group_review"]["supported_estimates"] == 35 and report["group_review"]["supported_contrasts"] == 19, "Build report preserves group support counts")

    for name in RECORD_FILES:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if learner:
            require(bool(PLACEHOLDER.search(text)), f"Learner prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Reference record is complete: {name}")
    if learner:
        result = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 49}
        print(f"APP-2 Module 05 learner validation passed: {len(checks)} checks.")
        return result

    provenance = (root / "comment-provenance.md").read_text(encoding="utf-8")
    require(all(value in provenance for value in ("782 synthetic opportunities", "420 fully synthetic", "Real patient text rows: `0`", "not patient prevalence")) or all(value in provenance for value in ("782 synthetic opportunities", "420 fully synthetic", "Real patient text rows: `0`", "theme prevalence")), "Comment provenance has exact counts and real-text boundary")
    codebook_decision_header, codebook_decisions = read_csv(root / "codebook-decisions.csv")
    require(len(codebook_decisions) == 8 and all(row["decision"] == "retain" for row in codebook_decisions), "Completed codebook decisions cover and retain eight themes")
    coding_header, coding_review = read_csv(root / "double-coding-review.csv")
    require(len(coding_review) == 9 and coding_review[0]["records"] == "120" and coding_review[0]["agreements"] == "96" and coding_review[0]["cohens_kappa"] == "0.77142857", "Completed double-coding review matches agreement evidence")
    agreement_text = (root / "agreement-interpretation.md").read_text(encoding="utf-8")
    require(all(value in agreement_text for value in ("120 comments", "80.00000000", "0.77142857", "does not validate")), "Agreement interpretation contains sample arithmetic and limit")
    assisted_text = (root / "assisted-classification-review.md").read_text(encoding="utf-8")
    require(all(value in assisted_text for value in ("0.78333333", "0.40000000", "0.60000000", "all 420", "Module 06")), "Assisted review contains accuracy failure human review and ML boundary")
    group_plan = (root / "group-analysis-plan.md").read_text(encoding="utf-8")
    require(all(value in group_plan for value in ("PERWT24F", "VARSTR", "VARPSU", "50 valid", "10 positive", "10 negative", "joint linearized")), "Group plan has complete design support and contrast rules")
    support_decision_header, support_decisions = read_csv(root / "group-support-decisions.csv")
    require(len(support_decisions) == 13 and any(row["group"] == "uninsured" and row["decision"] == "suppress all estimates" for row in support_decisions), "Completed group-support decisions retain all groups and sparse suppression")
    group_text = (root / "group-difference-interpretation.md").read_text(encoding="utf-8")
    require(all(value in group_text for value in ("4.02137981", "0.59188925", "7.45087037", "uninsured", "does not prove inequity")), "Group interpretation has exact contrast suppression and claim limit")
    channel_text = (root / "channel-exclusion-review.md").read_text(encoding="utf-8")
    require(all(value in channel_text for value in ("782", "420", "53.70843990", "160 of 301", "162 of 277", "98 of 204", "cannot establish real")), "Channel review has exact flow and synthetic limit")
    memo = (root / "equity-patient-voice-memo.md").read_text(encoding="utf-8")
    require(all(value in memo for value in ("4.02137981", "6.88053616", "generated examples", "patient partners", "does not measure discrimination", "may not train on comment text")), "Equity memo separates evidence unknowns patient question and Module 06 limit")
    claims = (root / "responsible-claims.md").read_text(encoding="utf-8").lower()
    require(all(value in claims for value in ("prevalence", "patient testimony", "proof of inequity", "causal", "portal preference", "patient targeting", "human owner")), "Responsible claims cover every required boundary")
    reproduction = (root / "reproducibility-check.md").read_text(encoding="utf-8")
    require(all(value in reproduction for value in ("five of five", "5,297,691", "byte for byte", "28 of 28", "not overwritten")), "Reproducibility record has exact checks and overwrite protection")
    gate_header, gates = read_csv(root / "gate-results.csv")
    require(len(gates) == 22 and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 23)] and all(row["status"] == "pass" for row in gates), "All 22 patient-voice and equity gates pass in order")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    labels = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in labels), "AI-use record has every accountable field")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Module 05 score") == "20.00 of 20.00, carried into the Week 6 checkpoint exactly once", "Module score is exact and carried once")
    require(markdown_field(progression, "Patient-voice and equity gates") == "22 of 22 pass" and markdown_field(progression, "Failed gates") == "none", "Progression records all gates")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 06 permission")
    require(disposition in ALLOWED_PROGRESSION and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for partnered improvement and embedded ML")), "Module 06 permission matches progression")
    require(markdown_field(progression, "Comment-text machine learning") == "prohibited" and markdown_field(progression, "Proof of inequity") == "prohibited" and markdown_field(progression, "Clinical action") == "prohibited" and markdown_field(progression, "Patient targeting") == "prohibited", "Downstream prohibitions remain explicit")
    result = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 49}
    print(f"APP-2 Module 05 reference validation passed: {len(checks)} checks.")
    return result


def self_check() -> None:
    import build_patient_voice

    with tempfile.TemporaryDirectory(prefix="app2-module05-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner, reproduction = base / "reference", base / "learner", base / "reproduction"
        build_workspace.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_workspace.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_workspace.assemble(learner)
        starter = validate(learner, learner=True)
        rebuilt = build_patient_voice.build(reproduction)
        for relative, digest in rebuilt["generated_sha256"].items():
            if relative.startswith("instructor/"):
                continue
            assert sha256(reference / relative) == digest

        broken = base / "broken-comment"
        shutil.copytree(reference, broken)
        path = broken / "data/synthetic/synthetic-comments.csv"
        path.write_text(path.read_text(encoding="utf-8").replace("fully_synthetic_comment", "observed_patient_comment", 1), encoding="utf-8", newline="\n")
        try:
            validate(broken)
        except ValidationError as error:
            assert "Immutable bytes match" in str(error) or "Immutable SHA-256 matches" in str(error)
        else:
            raise AssertionError("Validator accepted a changed comment data class")

        bad_gate = base / "bad-gate"
        shutil.copytree(reference, bad_gate)
        path = bad_gate / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_gate)
        except ValidationError as error:
            assert "22 patient-voice and equity gates" in str(error)
        else:
            raise AssertionError("Validator accepted a failed gate")

        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        path = bad_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("permitted for partnered improvement and embedded ML", "prohibited", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_progression)
        except ValidationError as error:
            assert "permission matches progression" in str(error)
        else:
            raise AssertionError("Validator accepted invalid Module 06 permission")
    print(f"APP-2 Module 05 validator self-check passed: {complete['checks_passed']} reference checks and {starter['checks_passed']} learner checks; copied, reproduction, and mutation routes verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path)
    parser.add_argument("--learner", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.workspace:
            validate(args.workspace, learner=args.learner)
        else:
            parser.error("workspace is required unless --self-check is used")
    except (OSError, ValueError, KeyError, json.JSONDecodeError, csv.Error, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
