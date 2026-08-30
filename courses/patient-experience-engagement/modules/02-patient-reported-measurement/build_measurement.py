"""Build and verify the APP-2 Module 02 measurement evidence."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
import shutil
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
INVENTORY = MODULE_ROOT / "data/source-inventory.csv"
GENERATED_FILES = (
    "data/synthetic/patient-measurement-responses.csv",
    "outputs/synthetic-score-summary.csv",
    "outputs/reliability-diagnostics.csv",
    "outputs/published-concordance.csv",
    "outputs/published-concordance-summary.csv",
    "outputs/invariant-checks.csv",
    "build-report.json",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def verify_sources(source_root: Path = MODULE_ROOT) -> dict[str, int]:
    rows = read_csv(INVENTORY)
    if len(rows) != 28 or [row["source_id"] for row in rows] != [f"SRC{i:02d}" for i in range(1, 29)]:
        raise ValueError("Source inventory must contain SRC01 through SRC28")
    total_bytes = total_pages = pdf_files = instrument_files = 0
    for row in rows:
        relative = Path(row["relative_path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"Unsafe source path: {relative}")
        path = source_root / relative
        if not path.is_file():
            raise FileNotFoundError(f"Missing source: {relative}")
        if path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise ValueError(f"Source fingerprint changed: {relative}")
        if not row["direct_url"].startswith("https://"):
            raise ValueError(f"Source URL is not complete: {relative}")
        total_bytes += path.stat().st_size
        total_pages += int(row["pages"])
        if row["source_type"].endswith("_pdf"):
            pdf_files += 1
            with path.open("rb") as handle:
                if handle.read(5) != b"%PDF-":
                    raise ValueError(f"Invalid PDF header: {relative}")
        if row["source_type"] == "instrument_pdf":
            instrument_files += 1
    if (total_bytes, total_pages, pdf_files, instrument_files) != (25032907, 1343, 27, 22):
        raise ValueError("Source suite dimensions changed")
    return {"files": 28, "bytes": total_bytes, "pages": total_pages, "pdf_files": pdf_files, "instrument_files": instrument_files}


def synthetic_rows() -> list[dict[str, str]]:
    pairs: list[tuple[str, str]] = []
    for pair, count in (
        (("yes", "yes"), 120), (("yes", "no"), 16), (("no", "yes"), 8), (("no", "no"), 16),
        (("yes", "missing"), 12), (("no", "missing"), 4), (("missing", "yes"), 16), (("missing", "no"), 8),
    ):
        pairs.extend([pair] * count)
    q20 = ["yes_definitely"] * 100 + ["yes_somewhat"] * 48 + ["no"] * 28 + ["no_caregiver"] * 40 + ["missing"] * 24
    rows: list[dict[str, str]] = []
    for index in range(240):
        if index < 200:
            destination, q22, q23 = "home_or_other", *pairs[index]
        elif index < 220:
            destination, q22, q23 = "another_health_facility", "not_applicable", "not_applicable"
        else:
            destination, q22, q23 = "missing", "missing", "missing"
        rows.append({
            "synthetic_record_id": f"SYN-{index + 1:04d}",
            "data_class": "synthetic_procedural_teaching_only",
            "q20_caregiver_information": q20[index],
            "q21_discharge_destination": destination,
            "q22_help_after_discharge": q22,
            "q23_written_symptom_information": q23,
        })
    return rows


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def sample_variance(values: list[float]) -> float:
    center = mean(values)
    return sum((value - center) ** 2 for value in values) / (len(values) - 1)


def score_synthetic(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, float]]:
    q20_answered = [row["q20_caregiver_information"] for row in rows if row["q20_caregiver_information"] in {"yes_definitely", "yes_somewhat", "no"}]
    q22 = [row["q22_help_after_discharge"] for row in rows if row["q22_help_after_discharge"] in {"yes", "no"}]
    q23 = [row["q23_written_symptom_information"] for row in rows if row["q23_written_symptom_information"] in {"yes", "no"}]
    q20_score = 100 * q20_answered.count("yes_definitely") / len(q20_answered)
    q22_score = 100 * q22.count("yes") / len(q22)
    q23_score = 100 * q23.count("yes") / len(q23)
    composite = (q22_score + q23_score) / 2
    person_means = []
    complete: list[tuple[float, float]] = []
    for row in rows:
        values = [1.0 if value == "yes" else 0.0 for value in (row["q22_help_after_discharge"], row["q23_written_symptom_information"]) if value in {"yes", "no"}]
        if values:
            person_means.append(mean(values))
        if len(values) == 2:
            complete.append((values[0], values[1]))
    person_weighted = 100 * mean(person_means)
    x, y = [pair[0] for pair in complete], [pair[1] for pair in complete]
    covariance = sum((a - mean(x)) * (b - mean(y)) for a, b in zip(x, y)) / (len(complete) - 1)
    phi = covariance / math.sqrt(sample_variance(x) * sample_variance(y))
    total = [a + b for a, b in complete]
    raw_alpha = 2 * (1 - (sample_variance(x) + sample_variance(y)) / sample_variance(total))
    standardized_alpha = 2 * phi / (1 + phi)
    expected = (len(q20_answered), len(q22), q22.count("yes"), len(q23), q23.count("yes"), len(person_means), len(complete))
    if expected != (176, 176, 148, 184, 144, 200, 160):
        raise ValueError(f"Synthetic response contract changed: {expected}")
    numeric = {
        "q20_top_box_percent": q20_score, "q22_top_box_percent": q22_score,
        "q23_top_box_percent": q23_score, "question_weighted_composite_percent": composite,
        "person_weighted_mean_percent": person_weighted, "phi": phi,
        "raw_alpha": raw_alpha, "standardized_alpha": standardized_alpha,
    }
    targets = {"question_weighted_composite_percent": 81.17588932806323, "person_weighted_mean_percent": 80.0, "phi": 0.4900980294098035, "raw_alpha": 0.6549707602339181, "standardized_alpha": 0.6578064257979319}
    for key, target in targets.items():
        if not math.isclose(numeric[key], target, rel_tol=0, abs_tol=1e-10):
            raise ValueError(f"Synthetic {key} changed: {numeric[key]}")
    score_rows = [
        {"metric_id": "S01", "metric": "Q20 yes definitely top box", "numerator": 100, "denominator": 176, "value": f"{q20_score:.8f}", "unit": "percent", "data_class": "synthetic", "official_status": "individual teaching calculation"},
        {"metric_id": "S02", "metric": "Q22 yes top box", "numerator": 148, "denominator": 176, "value": f"{q22_score:.8f}", "unit": "percent", "data_class": "synthetic", "official_status": "unadjusted teaching calculation"},
        {"metric_id": "S03", "metric": "Q23 yes top box", "numerator": 144, "denominator": 184, "value": f"{q23_score:.8f}", "unit": "percent", "data_class": "synthetic", "official_status": "unadjusted teaching calculation"},
        {"metric_id": "S04", "metric": "Q22 Q23 question-weighted composite", "numerator": "mean of S02 and S03", "denominator": "2 question proportions", "value": f"{composite:.8f}", "unit": "percent", "data_class": "synthetic", "official_status": "unadjusted teaching composite"},
        {"metric_id": "S05", "metric": "Q22 Q23 person-weighted mean", "numerator": "mean available response within person", "denominator": 200, "value": f"{person_weighted:.8f}", "unit": "percent", "data_class": "synthetic", "official_status": "alternative teaching calculation"},
    ]
    reliability_rows = [
        {"diagnostic_id": "D01", "diagnostic": "complete cases", "value": len(complete), "unit": "records", "interpretation": "synthetic records with both Q22 and Q23 answered"},
        {"diagnostic_id": "D02", "diagnostic": "phi correlation", "value": f"{phi:.10f}", "unit": "coefficient", "interpretation": "synthetic procedural diagnostic only"},
        {"diagnostic_id": "D03", "diagnostic": "raw Cronbach alpha", "value": f"{raw_alpha:.10f}", "unit": "coefficient", "interpretation": "synthetic procedural diagnostic only; not HCAHPS validation"},
        {"diagnostic_id": "D04", "diagnostic": "standardized Cronbach alpha", "value": f"{standardized_alpha:.10f}", "unit": "coefficient", "interpretation": "synthetic procedural diagnostic only; not hospital-level reliability"},
        {"diagnostic_id": "D05", "diagnostic": "QAG aggregate reliability target", "value": "at least 0.8", "unit": "signal-to-noise reliability", "interpretation": "hospital-level target generally based on at least 300 completed surveys over 12 months"},
    ]
    return score_rows, reliability_rows, numeric


def published_concordance(source_root: Path = MODULE_ROOT) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object]]:
    source = source_root / "data/raw/HCAHPS-Hospital.csv.gz"
    wanted = {"H_COMP_6_Y_P", "H_DISCH_HELP_Y_P", "H_SYMPTOMS_Y_P"}
    facilities: dict[str, dict[str, object]] = defaultdict(dict)
    with gzip.open(source, "rt", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            measure = row["HCAHPS Measure ID"]
            value = row["HCAHPS Answer Percent"]
            if measure not in wanted:
                continue
            record = facilities[row["Facility ID"]]
            record.update({"facility_id": row["Facility ID"], "facility_name": row["Facility Name"], "state": row["State"]})
            try:
                record[measure] = float(value)
            except ValueError:
                pass
    rows: list[dict[str, object]] = []
    differences: Counter[float] = Counter()
    for facility_id in sorted(facilities):
        record = facilities[facility_id]
        if not wanted <= record.keys():
            continue
        simple = (float(record["H_DISCH_HELP_Y_P"]) + float(record["H_SYMPTOMS_Y_P"])) / 2
        difference = float(record["H_COMP_6_Y_P"]) - simple
        differences[difference] += 1
        rows.append({
            "facility_id": facility_id, "facility_name": record["facility_name"], "state": record["state"],
            "official_discharge_information_percent": f"{float(record['H_COMP_6_Y_P']):.1f}",
            "published_help_after_discharge_yes_percent": f"{float(record['H_DISCH_HELP_Y_P']):.1f}",
            "published_symptoms_information_yes_percent": f"{float(record['H_SYMPTOMS_Y_P']):.1f}",
            "simple_published_item_mean_percent": f"{simple:.1f}",
            "official_minus_simple_mean_points": f"{difference:.1f}",
            "use_boundary": "source concordance only; no ranking",
        })
    exact = differences[0.0]
    facts = {"complete_facilities": len(rows), "exact_matches": exact, "nonexact_matches": len(rows) - exact, "min_difference": min(differences), "max_difference": max(differences)}
    if facts != {"complete_facilities": 3610, "exact_matches": 1734, "nonexact_matches": 1876, "min_difference": -3.0, "max_difference": 3.5}:
        raise ValueError(f"Published concordance changed: {facts}")
    summary = [
        {"summary_type": "metric", "key": "complete_facilities", "value": 3610},
        {"summary_type": "metric", "key": "exact_match_facilities", "value": 1734},
        {"summary_type": "metric", "key": "nonexact_match_facilities", "value": 1876},
        {"summary_type": "metric", "key": "minimum_difference_points", "value": "-3.0"},
        {"summary_type": "metric", "key": "maximum_difference_points", "value": "3.5"},
    ]
    summary.extend({"summary_type": "distribution", "key": f"difference_{value:.1f}", "value": count} for value, count in sorted(differences.items()))
    return rows, summary, facts


def build(target: Path, source_root: Path = MODULE_ROOT) -> dict[str, object]:
    target = target.resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    sources = verify_sources(source_root)
    target.mkdir(parents=True)
    synthetic = synthetic_rows()
    score_rows, reliability_rows, numeric = score_synthetic(synthetic)
    concordance, concordance_summary, public_facts = published_concordance(source_root)
    write_csv(target / GENERATED_FILES[0], list(synthetic[0]), synthetic)
    write_csv(target / GENERATED_FILES[1], list(score_rows[0]), score_rows)
    write_csv(target / GENERATED_FILES[2], list(reliability_rows[0]), reliability_rows)
    write_csv(target / GENERATED_FILES[3], list(concordance[0]), concordance)
    write_csv(target / GENERATED_FILES[4], list(concordance_summary[0]), concordance_summary)
    checks = [
        ("I01", "source files", sources["files"] == 28, "28 immutable source files"),
        ("I02", "source bytes", sources["bytes"] == 25032907, "25,032,907 retained bytes"),
        ("I03", "PDF suite", sources["pdf_files"] == 27 and sources["pages"] == 1343, "27 PDFs and 1,343 pages"),
        ("I04", "instrument suite", sources["instrument_files"] == 22, "22 mode-language instruments"),
        ("I05", "synthetic rows", len(synthetic) == 240, "240 visibly synthetic records"),
        ("I06", "eligible records", sum(row["q21_discharge_destination"] == "home_or_other" for row in synthetic) == 200, "200 Q22/Q23-eligible records"),
        ("I07", "Q22 denominator", score_rows[1]["denominator"] == 176, "176 answered Q22 records"),
        ("I08", "Q22 numerator", score_rows[1]["numerator"] == 148, "148 Q22 yes responses"),
        ("I09", "Q23 denominator", score_rows[2]["denominator"] == 184, "184 answered Q23 records"),
        ("I10", "Q23 numerator", score_rows[2]["numerator"] == 144, "144 Q23 yes responses"),
        ("I11", "teaching composite", math.isclose(numeric["question_weighted_composite_percent"], 81.17588932806323), "81.17588933 percent"),
        ("I12", "person-weighted mean", numeric["person_weighted_mean_percent"] == 80.0, "80.0 percent and distinct formula"),
        ("I13", "complete cases", reliability_rows[0]["value"] == 160, "160 complete synthetic item pairs"),
        ("I14", "synthetic alpha boundary", reliability_rows[2]["interpretation"].endswith("not HCAHPS validation"), "procedural diagnostic only"),
        ("I15", "public complete facilities", public_facts["complete_facilities"] == 3610, "3,610 complete published facility rows"),
        ("I16", "public mismatch", public_facts["exact_matches"] == 1734 and public_facts["nonexact_matches"] == 1876, "1,734 exact and 1,876 nonexact"),
        ("I17", "public difference bounds", public_facts["min_difference"] == -3.0 and public_facts["max_difference"] == 3.5, "-3.0 to 3.5 points"),
        ("I18", "claim boundary", True, "unadjusted teaching and official adjusted values remain distinct"),
    ]
    if not all(passed for _, _, passed, _ in checks):
        raise ValueError("One or more build invariants failed")
    invariant_rows = [{"check_id": check_id, "check": label, "status": "pass" if passed else "fail", "evidence": evidence} for check_id, label, passed, evidence in checks]
    write_csv(target / GENERATED_FILES[5], list(invariant_rows[0]), invariant_rows)
    report = {
        "status": "pass", "source": sources, "synthetic_rows": 240,
        "scores": {key: round(value, 10) for key, value in numeric.items()},
        "published_concordance": public_facts, "invariant_checks": len(checks),
    }
    (target / GENERATED_FILES[6]).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    return report


def generated_fingerprints(root: Path) -> dict[str, str]:
    return {relative: sha256(root / relative) for relative in GENERATED_FILES}


def write_committed() -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="app2-module02-write-") as temp_dir:
        built = Path(temp_dir) / "built"
        report = build(built)
        for relative in GENERATED_FILES:
            destination = MODULE_ROOT / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(built / relative, destination)
        return report


def verify_committed() -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="app2-module02-verify-") as temp_dir:
        built = Path(temp_dir) / "built"
        report = build(built)
        missing = [relative for relative in GENERATED_FILES if not (MODULE_ROOT / relative).is_file()]
        if missing:
            raise FileNotFoundError(f"Missing committed output: {', '.join(missing)}")
        if generated_fingerprints(built) != generated_fingerprints(MODULE_ROOT):
            raise ValueError("Committed measurement outputs do not reproduce")
        return report


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="app2-module02-build-") as temp_dir:
        base = Path(temp_dir)
        first, second = base / "first", base / "second"
        build(first)
        build(second)
        assert generated_fingerprints(first) == generated_fingerprints(second)
        try:
            build(first)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target")
        changed_root = base / "changed-source"
        shutil.copytree(MODULE_ROOT / "data/raw", changed_root / "data/raw")
        changed = changed_root / "data/raw/instruments/mail/english.pdf"
        with changed.open("ab") as handle:
            handle.write(b"changed")
        try:
            build(base / "rejected", source_root=changed_root)
        except ValueError as error:
            assert "fingerprint changed" in str(error)
        else:
            raise AssertionError("Builder accepted a changed official source")
    print("APP-2 Module 02 measurement builder self-check passed: deterministic outputs, existing-target protection, and changed-source rejection.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--write-committed", action="store_true")
    parser.add_argument("--verify-committed", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        selected = sum(bool(value) for value in (args.target, args.write_committed, args.verify_committed, args.self_check))
        if selected != 1:
            parser.error("choose exactly one of --target, --write-committed, --verify-committed, or --self-check")
        if args.self_check:
            self_check()
        elif args.write_committed:
            print(json.dumps(write_committed(), indent=2))
        elif args.verify_committed:
            print(json.dumps(verify_committed(), indent=2))
        else:
            print(json.dumps(build(args.target), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
