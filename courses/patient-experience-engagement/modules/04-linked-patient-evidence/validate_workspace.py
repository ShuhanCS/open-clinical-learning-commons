"""Validate an APP-2 Module 04 learner or reference workspace."""

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

from build_workspace import IMMUTABLE_FILES, RECORD_FILES


PLACEHOLDER = re.compile(r"\bREPLACE\b|\bTODO\b|\bTBD\b", re.IGNORECASE)
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
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

    required = set(IMMUTABLE_FILES) | set(RECORD_FILES) | {"release-manifest.csv"}
    require(root.is_dir(), "Workspace directory exists")
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
    require(actual == required and len(actual) == 65, "Workspace has exactly 65 expected files")
    header, manifest = read_csv(root / "release-manifest.csv")
    require(header == ["relative_path", "bytes", "sha256", "role"], "Release manifest header matches")
    require(len(manifest) == 52 and [row["relative_path"] for row in manifest] == sorted(row["relative_path"] for row in manifest), "Release manifest has 52 sorted immutable rows")
    require({row["relative_path"] for row in manifest} == set(IMMUTABLE_FILES), "Release manifest covers every immutable file")
    for row in manifest:
        path = root / row["relative_path"]
        require(path.is_file(), f"Immutable file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]), f"Immutable bytes match: {row['relative_path']}")
        require(sha256(path) == row["sha256"], f"Immutable SHA-256 matches: {row['relative_path']}")

    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version matches")
    contract = json.loads((root / "linkage-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app2-04", "version": "0.1.0", "commons_release": "0.59.0", "week": 4, "hours": 16.5, "course_points": 25}, "Module identity and points match")
    require(contract["upstream"]["candidate_manifest_sha256"] == "5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903", "Week 3 checkpoint identity matches")
    require(contract["source"]["official_files"] == 25 and contract["source"]["official_bytes"] == 18206634 and contract["source"]["official_pdf_pages"] == 1101, "Official source contract matches")
    require(contract["target"]["people"] == 1255 and contract["target"]["linked_events"] == 28455 and contract["target"]["related_emergency_inpatient_pairs"] == 855, "Target linkage contract matches")
    require(contract["permissions"]["machine_learning"] == "reserved for Module 06" and contract["permissions"]["clinical_action"] == "prohibited", "ML and clinical permissions remain bounded")

    source_header, sources = read_csv(root / "data/source-inventory.csv")
    require(source_header == ["source_id", "title", "relative_path", "url", "media_type", "bytes", "sha256", "pages", "role"], "Source inventory header matches")
    require(len(sources) == 25 and sum(int(row["bytes"]) for row in sources) == 18206634 and sum(int(row["pages"] or 0) for row in sources) == 1101, "Official source inventory has 25 files, 18,206,634 bytes, and 1,101 pages")
    require(all(row["url"].startswith("https://meps.ahrq.gov/") for row in sources), "Every official source URL is complete")
    upstream_header, upstream = read_csv(root / "data/upstream-inventory.csv")
    require(upstream_header == ["source_id", "title", "relative_path", "bytes", "sha256", "role"] and len(upstream) == 3 and sum(int(row["bytes"]) for row in upstream) == 570340, "Upstream inventory has three accepted files and 570,340 bytes")

    person_header, people = read_csv(root / "data/public/linked-persons.csv")
    event_header, events = read_csv(root / "data/public/linked-events.csv")
    require(len(people) == 1255 and len(events) == 28455, "Released teaching tables have 1,255 people and 28,455 events")
    require("DUPERSID" not in person_header and "EVNTIDX" not in event_header and "DUPERSID" not in event_header, "Released tables omit direct public-use person and event IDs")
    require(len({row["link_person_id"] for row in people}) == 1255 and len({row["linked_event_id"] for row in events}) == 28455, "Released person and event IDs are unique")
    require({row["link_person_id"] for row in events} <= {row["link_person_id"] for row in people}, "Every released event links to a released person")
    require(abs(sum(float(row["base_person_weight"]) for row in people) - 18879474.284615) < 0.000001, "Target base-weighted population matches")
    require(sum(row["response_status"] == "respondent" for row in people) == 782, "Accepted synthetic response count matches")
    require(all(row["data_class"] == "public_derived_meps_with_synthetic_response_handoff" for row in people) and all(row["data_class"] == "public_derived_meps_event" for row in events), "Public-derived and synthetic handoff data classes remain explicit")
    event_counts = {setting: sum(row["event_setting"] == setting for row in events) for setting in ("inpatient", "emergency", "outpatient", "office_based")}
    require(event_counts == {"inpatient": 1692, "emergency": 1601, "outpatient": 4651, "office_based": 20511}, "Target event setting counts match")
    require(sum(row["event_setting"] == "inpatient" and row["event_year"] == "2023" for row in events) == 12, "Twelve inpatient carry-in starts remain visible")
    event_ids = {row["linked_event_id"] for row in events}
    related = [row for row in events if row["related_event_id"]]
    require(len(related) == 1710 and all(row["related_event_id"] in event_ids for row in related), "Eight hundred fifty-five reciprocal emergency-inpatient pairs remain linked")
    require(all(row["inpatient_discharges_reported"] == row["inpatient_events_linked"] and row["emergency_visits_reported"] == row["emergency_events_linked"] and row["outpatient_visits_reported"] == row["outpatient_events_linked"] and row["office_visits_reported"] == row["office_events_linked"] for row in people), "Every person-level service total reconciles to event rows")

    profile_header, profile = read_csv(root / "outputs/source-profile.csv")
    require(profile_header == ["metric", "value", "unit", "evidence"] and len(profile) == 13, "Source profile has thirteen metrics")
    profile_map = {row["metric"]: row["value"] for row in profile}
    require(profile_map["person_source_rows"] == "19140" and profile_map["event_source_rows"] == "174231" and profile_map["target_linked_event_rows"] == "28455" and profile_map["target_inpatient_carry_in_starts"] == "12", "Source profile counts and carry-in rule match")
    reconciliation_header, reconciliation = read_csv(root / "outputs/linkage-reconciliation.csv")
    require(len(reconciliation) == 5 and all(row["status"] == "pass" and row["difference"] == "0" for row in reconciliation), "All four event settings and related pairs reconcile")
    denominator_header, denominators = read_csv(root / "outputs/denominator-registry.csv")
    require(len(denominators) == 14 and denominators[0]["unweighted_n"] == "1255", "Denominator registry has fourteen aligned entries")
    require(any(row["denominator_id"] == "D022" and row["unweighted_n"] == "0" and row["data_class"] == "not_available" for row in denominators), "Portal evidence gap remains explicit")
    access_header, access = read_csv(root / "outputs/access-communication-estimates.csv")
    require(len(access) == 10 and {row["measure"] for row in access} == {"usual_source", "regular_phone_difficult", "evening_weekend_hours", "after_hours_difficult", "asked_other_treatments", "involved_usually_always", "options_explained", "provider_language_match", "delayed_for_cost", "unable_to_afford"}, "Access table has ten prespecified measures")
    access_map = {row["measure"]: row for row in access}
    require(access_map["usual_source"]["weighted_percent"] == "80.78856833" and access_map["after_hours_difficult"]["weighted_percent"] == "52.44065366", "Primary access estimates match")
    require(access_map["provider_language_match"]["eligible_persons"] == "45" and access_map["provider_language_match"]["support_flag"] == "limited_support" and access_map["provider_language_match"]["survey_se_pp"] == "3.56420303", "Provider-language estimate retains limited support and domain variance")
    service_header, services = read_csv(root / "outputs/service-use-estimates.csv")
    require(len(services) == 8 and {row["setting"] for row in services} == {"inpatient", "emergency", "outpatient", "office_based"}, "Service-use table covers four settings and two statistics")
    service_map = {(row["setting"], row["statistic"]): row for row in services}
    require(service_map[("emergency", "any_use")]["weighted_estimate"] == "70.89748576" and service_map[("office_based", "mean_events")]["weighted_estimate"] == "16.71995519", "Service-use estimates match")
    digital_header, digital = read_csv(root / "outputs/digital-engagement.csv")
    require(len(digital) == 7 and digital[2]["denominator_n"] == "25162" and digital[2]["numerator_n"] == "1813" and digital[2]["weighted_percent"] == "7.37866394", "Digital-service event distribution matches")
    require(digital[-1]["setting"] == "portal_preference" and digital[-1]["denominator_n"] == "0", "Portal preference remains not available")
    pattern_header, patterns = read_csv(root / "outputs/linked-evidence-patterns.csv")
    require(len(patterns) == 14 and {row["synthetic_experience_group"] for row in patterns} == {"both_discharge_items_yes", "one_or_both_discharge_items_no"}, "Linked teaching patterns have two synthetic groups and fourteen rows")
    pattern_map = {(row["synthetic_experience_group"], row["linked_measure"]): row for row in patterns}
    require(pattern_map[("both_discharge_items_yes", "delayed_for_cost")]["weighted_estimate"] == "5.15284197" and pattern_map[("one_or_both_discharge_items_no", "delayed_for_cost")]["weighted_estimate"] == "12.69288290", "Linked teaching comparison matches")
    invariant_header, invariants = read_csv(root / "outputs/invariant-checks.csv")
    require(len(invariants) == 25 and [row["check_id"] for row in invariants] == [f"I{number:02d}" for number in range(1, 26)] and all(row["status"] == "pass" for row in invariants), "All 25 evidence invariants pass in order")
    report = json.loads((root / "build-report.json").read_text(encoding="utf-8"))
    require(report["status"] == "pass" and report["source"]["bytes"] == 18206634 and report["target"]["linked_events"] == 28455 and report["related_emergency_inpatient_pairs"] == 855, "Build report identity and counts match")

    for name in RECORD_FILES:
        text = (root / name).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {name}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {name}")
        if learner:
            require(bool(PLACEHOLDER.search(text)), f"Learner prompt is present: {name}")
        else:
            require(not PLACEHOLDER.search(text), f"Reference record is complete: {name}")
    if learner:
        result = {"status": "pass", "mode": "learner", "checks_passed": len(checks), "assembled_files": 65}
        print(f"APP-2 Module 04 learner validation passed: {len(checks)} checks.")
        return result

    plan_text = (root / "linkage-plan.md").read_text(encoding="utf-8")
    require(all(value in plan_text for value in ("DUPERSID", "855", "12", "PERWT24F", "VARSTR", "VARPSU")), "Completed linkage plan contains keys, relationships, period, and design")
    audit_header, audit = read_csv(root / "linkage-audit.csv")
    require(len(audit) == 8 and all(row["status"] == "pass" for row in audit), "Completed linkage audit has eight passing rows")
    decision_header, decisions = read_csv(root / "denominator-decisions.csv")
    require(len(decisions) == 8 and any(row["denominator_id"] == "D022" and row["eligible_n"] == "0" for row in decisions), "Completed denominator decisions retain the portal evidence gap")
    access_text = (root / "access-communication-interpretation.md").read_text(encoding="utf-8")
    require(all(value in access_text for value in ("80.78856833", "52.44065366", "7.61893012", "45", "limited_support")), "Completed access interpretation contains exact estimates and limited support")
    service_text = (root / "service-use-interpretation.md").read_text(encoding="utf-8")
    require(all(value in service_text for value in ("28,455", "855", "Twelve", "70.89748576", "92.74535872", "noncausal")), "Completed service-use interpretation contains exact reconciliation and claim limit")
    digital_text = (root / "digital-engagement-interpretation.md").read_text(encoding="utf-8")
    require(all(value in digital_text for value in ("25,162", "1,813", "7.37866394", "no portal-preference", "must not")), "Completed digital interpretation rejects portal and preference inference")
    linked_text = (root / "linked-evidence-analysis.md").read_text(encoding="utf-8")
    require(all(value in linked_text for value in ("538", "5.15284197", "12.69288290", "15.32762989", "16.96290478", "synthetic", "cannot establish")), "Completed linked analysis contains exact procedural comparison and limit")
    claim_text = (root / "responsible-claims.md").read_text(encoding="utf-8").lower()
    require(all(value in claim_text for value in ("causal", "ranking", "patient targeting", "portal preference", "synthetic", "human owner")), "Responsible claims record covers every prohibited interpretation and owner")
    reproduction_text = (root / "reproducibility-check.md").read_text(encoding="utf-8").lower()
    require("two independent evidence builds match byte for byte" in reproduction_text and "25 of 25 pass" in reproduction_text and "none" in reproduction_text, "Reproducibility record is complete")
    gate_header, gates = read_csv(root / "gate-results.csv")
    require(len(gates) == 20 and [row["gate_id"] for row in gates] == [f"G{number:02d}" for number in range(1, 21)] and all(row["status"] == "pass" for row in gates), "All 20 linkage gates pass in order")
    ai = (root / "ai-use.md").read_text(encoding="utf-8")
    labels = ("Tool and model", "Date", "Purpose", "Prompt or task", "Data classes shared", "Files affected", "Output used, modified, or rejected", "Material claim", "Independent verification", "Correction or retained action", "Human owner", "Accountability statement")
    require(all(markdown_field(ai, label) for label in labels), "AI-use record has every accountable field")
    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(markdown_field(progression, "Module 04 score") == "25.00 of 25.00, carried into the Week 6 checkpoint exactly once", "Module score is exact and carried once")
    require(markdown_field(progression, "Linkage gates") == "20 of 20 pass" and markdown_field(progression, "Failed gates") == "none", "Progression records all linkage gates")
    disposition = markdown_field(progression, "Progression")
    permission = markdown_field(progression, "Module 05 permission")
    require(disposition in ALLOWED_PROGRESSION and ((disposition in {"continue", "continue with conditions"}) == (permission == "permitted for patient-voice and equity analysis")), "Module 05 permission matches progression")
    require(markdown_field(progression, "Clinical action") == "prohibited" and markdown_field(progression, "Hospital ranking") == "prohibited" and markdown_field(progression, "Patient targeting") == "prohibited" and markdown_field(progression, "Causal claim") == "prohibited" and markdown_field(progression, "Machine learning") == "reserved for Module 06", "Downstream prohibitions remain explicit")
    result = {"status": "pass", "mode": "reference", "checks_passed": len(checks), "assembled_files": 65}
    print(f"APP-2 Module 04 reference validation passed: {len(checks)} checks.")
    return result


def self_check() -> None:
    import build_linked_evidence
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app2-module04-validate-") as temp_dir:
        base = Path(temp_dir)
        reference, learner, reproduction = base / "reference", base / "learner", base / "reproduction"
        build_workspace.assemble(reference, reference=True)
        complete = validate(reference)
        copied = subprocess.run([sys.executable, str(reference / "validate_workspace.py"), str(reference)], capture_output=True, text=True, check=False)
        assert copied.returncode == 0 and f"{complete['checks_passed']} checks" in copied.stdout, copied.stderr
        build_workspace.assemble(learner)
        starter = validate(learner, learner=True)
        rebuilt = build_linked_evidence.build(reproduction)
        for relative, digest in rebuilt["generated_sha256"].items():
            assert sha256(reference / relative) == digest

        broken = base / "broken-event"
        shutil.copytree(reference, broken)
        path = broken / "data/public/linked-events.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",inpatient,", ",emergency,", 1), encoding="utf-8", newline="\n")
        try:
            validate(broken)
        except ValidationError as error:
            assert "Immutable bytes match" in str(error) or "Immutable SHA-256 matches" in str(error)
        else:
            raise AssertionError("Validator accepted a changed event setting")

        bad_gate = base / "bad-gate"
        shutil.copytree(reference, bad_gate)
        path = bad_gate / "gate-results.csv"
        path.write_text(path.read_text(encoding="utf-8").replace(",pass,", ",fail,", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_gate)
        except ValidationError as error:
            assert "20 linkage gates" in str(error)
        else:
            raise AssertionError("Validator accepted a failed linkage gate")

        bad_progression = base / "bad-progression"
        shutil.copytree(reference, bad_progression)
        path = bad_progression / "progression-decision.md"
        path.write_text(path.read_text(encoding="utf-8").replace("permitted for patient-voice and equity analysis", "prohibited", 1), encoding="utf-8", newline="\n")
        try:
            validate(bad_progression)
        except ValidationError as error:
            assert "permission matches progression" in str(error)
        else:
            raise AssertionError("Validator accepted invalid Module 05 permission")
    print(f"APP-2 Module 04 validator self-check passed: {complete['checks_passed']} reference checks and {starter['checks_passed']} learner checks; copied, reproduction, and mutation routes verified.")


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
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
