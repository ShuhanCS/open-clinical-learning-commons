"""Validate APP-5 Module 03 learner and reference workspaces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


PLACEHOLDER = re.compile(r"\b(?:REPLACE|TODO|TBD)\b")
PERSONAL_PATH = re.compile(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)")
REAL_CLAIM = re.compile(r"(?im)^(?:This is an observed Massachusetts disparity|Real Massachusetts groups have|This shows a real community deficit)\b")
INTERSECTIONAL_CLAIM = re.compile(r"(?i)(the joint race.*language.*disability|intersectional disparity is established)")
ALLOWED_PROGRESSION = {"continue", "continue with conditions", "revise", "refer"}
SPEC_HEADER = [
    "measure_id", "name", "type", "numerator_or_summary", "denominator_or_standard",
    "age_groups", "multiplier", "interval_or_uncertainty", "availability_rule",
    "reference_rule", "interpretation_limit",
]
SENSITIVITY_HEADER = [
    "dimension_id", "primary_reference", "alternative_reference",
    "primary_summary_absolute_difference", "primary_summary_ratio",
    "alternative_summary_absolute_difference", "alternative_summary_ratio",
    "interpretation", "status",
]


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
    match = re.search(rf"(?im)^- {re.escape(label)}:\s*`?([^`\r\n]+)`?\.\s*$", text)
    return match.group(1).strip() if match else None


def validate(root: Path, starter: bool = False) -> dict[str, object]:
    import build_disparities
    import build_workspace
    import freeze_upstream
    import generate_equity_layer

    root = root.resolve()
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationError(message)
        checks.append(message)

    immutable = build_workspace.CONTROL_FILES + build_workspace.DATA_FILES + build_workspace.UPSTREAM_FILES
    if not starter:
        immutable += build_workspace.OUTPUT_FILES
    expected = set(immutable) | set(build_workspace.SQL_FILES) | set(build_workspace.RECORD_FILES) | {"release-manifest.csv"}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    expected_count = 108 if starter else 120
    require(root.is_dir(), "Workspace directory exists")
    require(actual == expected and len(actual) == expected_count, f"Workspace has exactly {expected_count} expected files")
    require((root / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0", "Module version is 0.1.0")

    contract = json.loads((root / "disparity-contract.json").read_text(encoding="utf-8"))
    require(contract["module"] == {"id": "oclc-app5-03", "version": "0.1.0", "commons_release": "0.89.0", "hours": 16.5, "course_points": 20}, "Module identity and workload match")
    require(contract["upstream"]["handoff_manifest_sha256"] == "f5e84b251143edeb65b68d816a57492755083d8bc57c73e6bdaede381b933ef1", "Frozen handoff identity matches")
    require(contract["source"] == {"release": "fma-dp-01-equity-v1", "generator_version": "0.1.0", "seed": 73053, "period": "2024", "dimensions": 3, "groups": 19, "margin_rows": 151715, "completeness_rows": 7985, "adult_denominator_per_dimension": 5679768, "synthetic_events_per_dimension": 283614, "manifest_sha256": "c3f7549f6fcc25e0bfd5f074a7f936e519a0bd7f9459452da903c653aee28384"}, "Synthetic source contract matches")
    require(contract["analysis"] == {"rate_multiplier": 100000, "age_bands": 5, "sql_files": 4, "accepted_output_tables": 11, "query_checks": 36, "source_reconciliation_checks": 12, "group_age_rates": 110, "standardized_group_rates": 22, "reported_comparison_groups": 16, "disparity_comparisons": 32, "summary_disparities": 6, "missingness_fields": 5, "representation_rows": 19, "bias_register_rows": 8}, "Disparity analysis contract matches")
    require(contract["suppression"] == {"minimum_event_count": 16, "minimum_denominator": 100, "published_tract_group_rows": 30343, "primary_suppressed_cells": 19742, "complementary_suppressed_cells": 1488, "publishable_cells": 9113, "audit_rows": 4791, "failed_audits": 0, "suppressed_values_are_zero": False, "tract_totals_published": False}, "Suppression contract matches")
    require(contract["assessment"] == {"criteria": 5, "points": 20, "pass_score": 16, "noncompensable_gates": 18, "week3_total_after_checkpoint": 40}, "Assessment contract matches")
    require(contract["workspace"] == {"learner_files": 108, "learner_manifest_rows": 92, "reference_files": 120, "reference_manifest_rows": 104, "editable_records": 11, "editable_sql_files": 4}, "Workspace contract matches")
    require(all(value == "prohibited" for value in contract["authority"].values()), "All real-world and premature analytical authority remains prohibited")
    release = json.loads((root / "release.json").read_text(encoding="utf-8"))
    require(release["module_id"] == "oclc-app5-03" and release["module_version"] == "0.1.0" and release["commons_release"] == "0.89.0" and release["validation"]["complete_checks"] == 431 and release["validation"]["starter_checks"] == 332 and release["validation"]["protected_failure_routes"] == 17, "Release identity and validation counts match")

    manifest_header, manifest = read_csv(root / "release-manifest.csv")
    require(manifest_header == ["relative_path", "bytes", "sha256", "role"], "Release manifest header matches")
    expected_manifest = 92 if starter else 104
    require(len(manifest) == expected_manifest and [row["relative_path"] for row in manifest] == sorted(immutable), f"Release manifest has {expected_manifest} sorted rows")
    for row in manifest:
        relative = Path(row["relative_path"])
        require(not relative.is_absolute() and ".." not in relative.parts, f"Manifest path is portable: {row['relative_path']}")
        path = root / relative
        require(path.is_file(), f"Manifest file exists: {row['relative_path']}")
        require(path.stat().st_size == int(row["bytes"]) and sha256(path) == row["sha256"], f"Manifest identity matches: {row['relative_path']}")

    handoff = freeze_upstream.verify(root)
    require(handoff["upstream_files"] == 74 and handoff["reference_files"] == 72 and handoff["nested_manifest_rows"] == 57, "Complete Module 02 handoff reproduces")
    source = generate_equity_layer.verify(root)
    require(source["margin_rows"] == 151715 and source["completeness_rows"] == 7985 and source["adult_denominator_per_dimension"] == 5679768 and source["synthetic_events_per_dimension"] == 283614, "Synthetic equity source reproduces")

    record_text = ""
    for relative in build_workspace.RECORD_FILES + build_workspace.SQL_FILES:
        text = (root / relative).read_text(encoding="utf-8")
        require("\u2013" not in text and "\u2014" not in text, f"Plain ASCII dashes: {relative}")
        require(not PERSONAL_PATH.search(text), f"No personal absolute path: {relative}")
        record_text += "\n" + text
        if not starter:
            require(not PLACEHOLDER.search(text), f"Submission file is complete: {relative}")

    spec_header, specifications = read_csv(root / "disparity-measure-specifications.csv")
    require(spec_header == SPEC_HEADER, "Disparity measure specification header matches")
    require([row["measure_id"] for row in specifications] == [f"DM{index:02d}" for index in range(1, 10)], "Disparity measure specification has nine ordered rows")
    sensitivity_header, sensitivity = read_csv(root / "reference-group-sensitivity.csv")
    require(sensitivity_header == SENSITIVITY_HEADER, "Reference-sensitivity header matches")
    require([row["dimension_id"] for row in sensitivity] == ["disability_status", "primary_language", "race_ethnicity"], "Reference sensitivity has three ordered dimensions")
    score_header, score = read_csv(root / "week3-component-score.csv")
    require(score_header == ["criterion_id", "criterion", "points_available", "points_awarded", "evidence"], "Score header matches")
    require([row["criterion_id"] for row in score] == ["R01", "R02", "R03", "R04", "R05", "TOTAL"], "Score has five criteria and total")
    gate_header, gates = read_csv(root / "gate-results.csv")
    require(gate_header == ["gate_id", "gate", "status", "evidence", "owner"], "Gate header matches")
    require([row["gate_id"] for row in gates] == [f"G{index:02d}" for index in range(1, 19)], "Gate file has 18 ordered rows")

    if starter:
        require(PLACEHOLDER.search(record_text) is not None, "Starter contains explicit learner placeholders")
        require(not any(path.startswith("outputs/") for path in actual), "Starter contains no accepted outputs")
        report = {"status": "pass", "mode": "starter", "checks": len(checks), "files": expected_count, "manifest_rows": expected_manifest, "course_points": 0}
        print(f"APP-5 Module 03 starter validation passed: {len(checks)} checks.")
        return report

    require(not REAL_CLAIM.search(record_text), "Submission makes no real Massachusetts disparity or community-deficit claim")
    require(not INTERSECTIONAL_CLAIM.search(record_text), "Submission makes no unsupported intersectional claim")
    require(all(all(row[column].strip() for column in spec_header) for row in specifications), "Every disparity measure specification field is complete")
    require("Wilson 95 percent interval" in specifications[0]["interval_or_uncertainty"] and "normal approximation" in specifications[1]["interval_or_uncertainty"], "Rate interval methods are explicit")
    require(sum(int(row["points_awarded"]) for row in score[:5]) == 20 and score[-1]["points_awarded"] == "20", "Reference score is 20 of 20")
    require(all(row["status"] == "pass" and row["evidence"] and row["owner"] for row in gates), "All 18 noncompensable gates pass with evidence and owners")

    expected_sensitivity = {
        "disability_status": ("no_reported_disability", 2172.8508009662, 1.4717380179, 1086.4254004831, 1.220960203),
        "primary_language": ("english", 778.3285287899, 1.1628981428, 584.3473603512, 1.1189871509),
        "race_ethnicity": ("white", 974.8180920556, 1.2129238385, 718.9414708135, 1.1478378374),
    }
    for row in sensitivity:
        reference, primary_difference, primary_ratio, alternative_difference, alternative_ratio = expected_sensitivity[row["dimension_id"]]
        require(row["primary_reference"] == reference and row["alternative_reference"] == "overall_reported", f"Reference choices match: {row['dimension_id']}")
        require(abs(float(row["primary_summary_absolute_difference"]) - primary_difference) < 0.000001 and abs(float(row["primary_summary_ratio"]) - primary_ratio) < 0.000001, f"Primary summary matches: {row['dimension_id']}")
        require(abs(float(row["alternative_summary_absolute_difference"]) - alternative_difference) < 0.000001 and abs(float(row["alternative_summary_ratio"]) - alternative_ratio) < 0.000001 and row["status"] == "pass", f"Alternative summary matches: {row['dimension_id']}")

    missingness = (root / "missingness-and-representation-audit.md").read_text(encoding="utf-8")
    require(all(value in missingness for value in ("6,000", "7,578", "5,314", "8,376", "zero missing geography cannot establish complete capture")), "Missingness and conditioned geography findings are complete")
    require("cannot describe intersectional identities" in missingness, "Separate-margin representation limit is explicit")
    bias = (root / "selection-linkage-measurement-bias.md").read_text(encoding="utf-8")
    require("Twenty-three ACS tracts" in bias and "correct join cannot repair selection" in bias and "cannot be crossed" in bias, "Selection linkage and measurement bias analysis is complete")
    suppression = (root / "suppression-policy.md").read_text(encoding="utf-8")
    require(all(value in suppression for value in ("`16`", "`100`", "`19,742`", "`1,488`", "`9,113`", "`4,791`", "A blank is unavailable, not zero", "contains no tract-dimension total")), "Suppression and non-reconstruction policy is complete")
    claim = (root / "responsible-disparity-claim.md").read_text(encoding="utf-8")
    require(all(value in claim for value in ("6,778.90", "4,606.05", "2,172.85", "1.4717", "generator result", "does not support a biological explanation")), "Responsible synthetic disparity claim is complete")

    progression = (root / "progression-decision.md").read_text(encoding="utf-8")
    require(field(progression, "Progression") in ALLOWED_PROGRESSION and field(progression, "Progression") == "continue with conditions", "Progression value is allowed and conditioned")
    require(field(progression, "Week 3 checkpoint curriculum construction") == "permitted", "Week 3 checkpoint construction is permitted")
    require(field(progression, "Module 04 curriculum construction") == "not yet; Week 3 checkpoint must accept the frozen package first", "Module 04 waits for checkpoint acceptance")
    require(field(progression, "Synthetic disparity statement") == "supported with conditions for the fictional release", "Synthetic statement boundary is explicit")
    for label in ("Real disparity claim", "Intersectional claim", "Mapping", "Tract ranking", "Targeting or allocation", "Model fitting", "Intervention-effect estimation", "Real community action", "Implementation", "Deployment"):
        require(field(progression, label) == "prohibited", f"{label} remains prohibited")
    require(len([line for line in progression.splitlines() if re.match(r"^\| O\d{2} \|", line)]) == 10, "Ten checkpoint and alpha conditions have owners")
    ai_use = (root / "ai-use.md").read_text(encoding="utf-8")
    require("Protected or identifiable data shared: `none`" in ai_use and "Agent authority: `none over" in ai_use, "AI-use boundary is complete")

    committed = build_disparities.verify_committed(root)
    require(committed == {"outputs": 11, "margin_rows": 151715, "group_age_rates": 110, "disparity_comparisons": 32, "published_tract_group_rows": 30343, "primary_suppressed_cells": 19742, "complementary_suppressed_cells": 1488, "query_checks": 36}, "Committed disparity outputs match")
    with tempfile.TemporaryDirectory(prefix="app5-module03-validate-") as temp_dir:
        regenerated = Path(temp_dir) / "outputs"
        report = build_disparities.build(root, root / "sql", regenerated)
        require(report["findings"]["failed_query_checks"] == 0 and report["findings"]["failed_source_reconciliation_checks"] == 0, "All 36 query and 12 reconciliation checks pass")
        for relative in build_workspace.OUTPUT_FILES:
            name = Path(relative).name
            require((regenerated / name).read_bytes() == (root / relative).read_bytes(), f"Regenerated output matches: {name}")

    report = {"status": "pass", "mode": "complete", "checks": len(checks), "files": expected_count, "manifest_rows": expected_manifest, "course_points": 20}
    print(f"APP-5 Module 03 complete validation passed: {len(checks)} checks.")
    return report


def expect_failure(root: Path, starter: bool = False) -> None:
    try:
        validate(root, starter=starter)
    except (OSError, ValueError, KeyError, RuntimeError, json.JSONDecodeError):
        return
    raise AssertionError(f"Validator accepted an invalid workspace: {root}")


def self_check() -> None:
    import build_workspace

    with tempfile.TemporaryDirectory(prefix="app5-module03-validator-") as temp_dir:
        base = Path(temp_dir)
        reference = base / "reference"
        starter = base / "starter"
        build_workspace.assemble(reference, reference=True)
        build_workspace.assemble(starter)
        complete_report = validate(reference)
        starter_report = validate(starter, starter=True)

        names = (
            "upstream-mutation", "source-mutation", "missing-file", "placeholder",
            "changed-sql", "bad-score", "failed-gate", "bad-reference",
            "missing-interval", "hidden-missingness", "zero-suppression",
            "reconstructable-suppression", "intersectional-claim", "real-claim",
            "ranking-authority", "implementation-authority", "personal-path",
        )
        cases = []
        for name in names:
            target = base / name
            shutil.copytree(reference, target)
            cases.append((name, target))
        upstream_path = cases[0][1] / "upstream/module02-reference/outputs/standard-population.csv"
        upstream_path.write_bytes(upstream_path.read_bytes() + b"x")
        source_path = cases[1][1] / "data/raw/synthetic-equity-margins.csv.gz"
        source_path.write_bytes(source_path.read_bytes() + b"x")
        (cases[2][1] / "disparity-measure-specifications.csv").unlink()
        with (cases[3][1] / "responsible-disparity-claim.md").open("a", encoding="utf-8") as handle:
            handle.write("\nREPLACE\n")
        sql_path = cases[4][1] / "sql/04-audit-missingness-bias-and-suppression.sql"
        sql_path.write_text(sql_path.read_text(encoding="utf-8").replace("30343", "30342", 1), encoding="utf-8")
        score_path = cases[5][1] / "week3-component-score.csv"
        score_path.write_text(score_path.read_text(encoding="utf-8").replace('R01,"Group rates support intervals and standardization",4,4,', 'R01,"Group rates support intervals and standardization",4,3,'), encoding="utf-8")
        gate_path = cases[6][1] / "gate-results.csv"
        gate_path.write_text(gate_path.read_text(encoding="utf-8").replace("G18,Claim and authority boundary,pass", "G18,Claim and authority boundary,fail"), encoding="utf-8")
        sensitivity_path = cases[7][1] / "reference-group-sensitivity.csv"
        sensitivity_path.write_text(sensitivity_path.read_text(encoding="utf-8").replace("2172.8508009662", "2172.0000000000", 1), encoding="utf-8")
        spec_path = cases[8][1] / "disparity-measure-specifications.csv"
        spec_path.write_text(spec_path.read_text(encoding="utf-8").replace("Wilson 95 percent interval", "none", 1), encoding="utf-8")
        missing_path = cases[9][1] / "missingness-and-representation-audit.md"
        missing_path.write_text(missing_path.read_text(encoding="utf-8").replace("zero missing geography cannot establish complete capture", "zero missing geography proves complete capture"), encoding="utf-8")
        suppression_zero = cases[10][1] / "suppression-policy.md"
        suppression_zero.write_text(suppression_zero.read_text(encoding="utf-8").replace("A blank is unavailable, not zero", "A blank is zero"), encoding="utf-8")
        suppression_total = cases[11][1] / "suppression-policy.md"
        suppression_total.write_text(suppression_total.read_text(encoding="utf-8").replace("contains no tract-dimension total", "contains a tract-dimension total"), encoding="utf-8")
        with (cases[12][1] / "responsible-disparity-claim.md").open("a", encoding="utf-8") as handle:
            handle.write("\nThe joint race language and disability table establishes an intersectional disparity.\n")
        with (cases[13][1] / "responsible-disparity-claim.md").open("a", encoding="utf-8") as handle:
            handle.write("\nThis is an observed Massachusetts disparity.\n")
        ranking_path = cases[14][1] / "progression-decision.md"
        ranking_path.write_text(ranking_path.read_text(encoding="utf-8").replace("- Tract ranking: `prohibited`.", "- Tract ranking: `permitted`."), encoding="utf-8")
        implementation_path = cases[15][1] / "progression-decision.md"
        implementation_path.write_text(implementation_path.read_text(encoding="utf-8").replace("- Implementation: `prohibited`.", "- Implementation: `permitted`."), encoding="utf-8")
        with (cases[16][1] / "ai-use.md").open("a", encoding="utf-8") as handle:
            handle.write("\nC:\\Users\\Example\\private.csv\n")
        for _, target in cases:
            expect_failure(target)

        copied = base / "copied-starter"
        shutil.copytree(starter, copied)
        for relative in build_workspace.RECORD_FILES + build_workspace.SQL_FILES:
            shutil.copy2(reference / relative, copied / relative)
        expect_failure(copied, starter=True)
        expect_failure(starter)
        assert complete_report["course_points"] == 20 and starter_report["course_points"] == 0
    print("APP-5 Module 03 validator self-check passed: reference, starter, copied-answer, complete-mode starter, and 17 protected failure routes rejected.")


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
            print(json.dumps(validate(args.workspace, starter=args.starter), indent=2))
        else:
            parser.error("workspace is required")
    except (OSError, ValueError, KeyError, RuntimeError, json.JSONDecodeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
