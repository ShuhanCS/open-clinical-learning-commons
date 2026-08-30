"""Build the exact FND-2 Module 01 modeling-workspace release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from collections import Counter
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
SOURCE_BYTES = 121_787
SOURCE_SHA256 = "3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a"
SOURCE_ROWS = 374
SOURCE_FIELDS = (
    "patient_id", "birth_date", "death_date", "age_at_index", "gender", "race",
    "ethnicity", "index_encounter_id", "index_start", "index_stop", "index_class",
    "index_code", "index_description", "index_reason_code", "index_reason_description",
    "prior_365d_encounter_count", "prior_365d_acute_count",
    "prior_365d_condition_count", "prior_365d_medication_count", "next_30d_state",
    "next_30d_encounter_id", "next_30d_start", "next_30d_days_after_index_stop",
    "acute_return_90d", "death_90d", "endpoint_90d", "followup_90d_complete",
    "source_release", "cohort_definition_version",
)
DERIVED_FIELDS = (
    "model_row_id", "prediction_time", "outcome_horizon_days", "split", "split_order",
)
SPLIT_SPECS = {
    "train": {"start": 1, "stop": 224, "rows": 224, "positives": 25, "first": "2015-01-01", "last": "2017-04-02"},
    "validation": {"start": 225, "stop": 299, "rows": 75, "positives": 7, "first": "2017-04-05", "last": "2018-04-03"},
    "test": {"start": 300, "stop": 374, "rows": 75, "positives": 4, "first": "2018-04-18", "last": "2019-12-28"},
}
ALLOWED_PREDICTORS = {
    "age_at_index", "gender", "race", "ethnicity", "index_class",
    "prior_365d_encounter_count", "prior_365d_acute_count",
    "prior_365d_condition_count", "prior_365d_medication_count",
}
PROHIBITED_PREDICTORS = {
    "next_30d_state", "next_30d_encounter_id", "next_30d_start",
    "next_30d_days_after_index_stop", "acute_return_90d", "death_90d", "endpoint_90d",
    "followup_90d_complete", "split", "split_order",
}
PORTABLE_FILES = (
    "requirements.txt", "data-spec.md", "source-record.yml", "assessment.md",
    "aim-classification-exercises.csv",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def default_source() -> Path:
    local = MODULE_ROOT / "data" / "resolved-analytic-table.csv"
    if local.is_file():
        return local
    return MODULE_ROOT.parents[2] / "healthcare-data-foundations" / "modules" / "04-cleaning-profiling" / "outputs" / "resolved-analytic-table.csv"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: tuple[str, ...] | None = None) -> None:
    if not rows and not fieldnames:
        raise ValueError(f"Cannot infer columns for empty CSV: {path}")
    columns = list(fieldnames or rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def verify_source(source_path: Path) -> list[dict[str, str]]:
    if not source_path.is_file():
        raise FileNotFoundError(f"Accepted FND-1 source not found: {source_path}")
    if source_path.stat().st_size != SOURCE_BYTES or sha256(source_path) != SOURCE_SHA256:
        raise ValueError("Accepted FND-1 source fingerprint changed.")
    fields, rows = read_csv(source_path)
    if tuple(fields) != SOURCE_FIELDS:
        raise ValueError("Accepted FND-1 source fields or field order changed.")
    if len(rows) != SOURCE_ROWS:
        raise ValueError("Accepted FND-1 source row count changed.")
    if len({row["patient_id"] for row in rows}) != SOURCE_ROWS:
        raise ValueError("Accepted FND-1 patient grain changed.")
    if len({row["index_encounter_id"] for row in rows}) != SOURCE_ROWS:
        raise ValueError("Accepted FND-1 index-encounter grain changed.")
    if any(row["acute_return_90d"] not in {"0", "1"} for row in rows):
        raise ValueError("The binary acute-return label changed.")
    return rows


def derive_rows(source_rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    ordered = sorted(source_rows, key=lambda row: (row["index_start"], row["patient_id"]))
    cohort: list[dict[str, object]] = []
    registry: list[dict[str, object]] = []
    for position, row in enumerate(ordered, start=1):
        split = "train" if position <= 224 else "validation" if position <= 299 else "test"
        model_row_id = f"FND2-{position:04d}"
        derived = {
            **row,
            "model_row_id": model_row_id,
            "prediction_time": row["index_stop"],
            "outcome_horizon_days": 90,
            "split": split,
            "split_order": position,
        }
        cohort.append(derived)
        registry.append({
            "model_row_id": model_row_id,
            "patient_id": row["patient_id"],
            "index_encounter_id": row["index_encounter_id"],
            "index_start": row["index_start"],
            "prediction_time": row["index_stop"],
            "split_order": position,
            "split": split,
            "acute_return_90d": row["acute_return_90d"],
        })
    return cohort, registry


def baseline_rows(registry: list[dict[str, object]]) -> list[dict[str, object]]:
    train = [row for row in registry if row["split"] == "train"]
    positives = sum(row["acute_return_90d"] == "1" for row in train)
    probability = positives / len(train)
    return [{
        "baseline_id": "BL01",
        "fit_split": "train",
        "application_scope": "all later prediction comparisons",
        "n": len(train),
        "positives": positives,
        "negatives": len(train) - positives,
        "constant_probability": f"{probability:.12f}",
        "threshold": "0.500000",
        "classification_rule": "predict positive when probability is at least threshold",
        "selection_status": "frozen before candidate-model comparison",
    }]


def check_rows(cohort: list[dict[str, object]], registry: list[dict[str, object]], baseline: list[dict[str, object]]) -> list[dict[str, object]]:
    counts = Counter(str(row["split"]) for row in registry)
    positives = Counter(str(row["split"]) for row in registry if row["acute_return_90d"] == "1")
    date_ranges = {
        split: (
            min(str(row["index_start"]) for row in rows)[:10],
            max(str(row["index_start"]) for row in rows)[:10],
        )
        for split in SPLIT_SPECS
        for rows in [[row for row in registry if row["split"] == split]]
        if rows
    }
    checks: list[tuple[str, str, object, object]] = [
        ("CHK01", "modeling cohort rows", len(cohort), 374),
        ("CHK02", "modeling cohort fields", len(cohort[0]), 34),
        ("CHK03", "unique model row IDs", len({row["model_row_id"] for row in cohort}), 374),
        ("CHK04", "unique patients", len({row["patient_id"] for row in cohort}), 374),
        ("CHK05", "unique index encounters", len({row["index_encounter_id"] for row in cohort}), 374),
        ("CHK06", "acute-return positives", sum(row["acute_return_90d"] == "1" for row in cohort), 36),
        ("CHK07", "acute-return negatives", sum(row["acute_return_90d"] == "0" for row in cohort), 338),
        ("CHK08", "prediction time equals index stop", sum(row["prediction_time"] == row["index_stop"] for row in cohort), 374),
        ("CHK09", "90-day horizon rows", sum(str(row["outcome_horizon_days"]) == "90" for row in cohort), 374),
        ("CHK10", "split order sequence", [int(row["split_order"]) for row in cohort], list(range(1, 375))),
        ("CHK11", "train rows", counts["train"], 224),
        ("CHK12", "validation rows", counts["validation"], 75),
        ("CHK13", "test rows", counts["test"], 75),
        ("CHK14", "train positives", positives["train"], 25),
        ("CHK15", "validation positives", positives["validation"], 7),
        ("CHK16", "test positives", positives["test"], 4),
        ("CHK17", "train date range", "|".join(date_ranges["train"]), "2015-01-01|2017-04-02"),
        ("CHK18", "validation date range", "|".join(date_ranges["validation"]), "2017-04-05|2018-04-03"),
        ("CHK19", "test date range", "|".join(date_ranges["test"]), "2018-04-18|2019-12-28"),
        ("CHK20", "training baseline probability", baseline[0]["constant_probability"], "0.111607142857"),
        ("CHK21", "allowed predictor count", len(ALLOWED_PREDICTORS), 9),
        ("CHK22", "prohibited predictor count", len(PROHIBITED_PREDICTORS), 10),
        ("CHK23", "source release rows", sum(row["source_release"] == "synthea-csv-apr2020" for row in cohort), 374),
        ("CHK24", "cohort version rows", sum(row["cohort_definition_version"] == "0.1.0" for row in cohort), 374),
    ]
    return [{
        "check_id": check_id,
        "check": label,
        "observed": json.dumps(observed, separators=(",", ":")) if isinstance(observed, list) else observed,
        "expected": json.dumps(expected, separators=(",", ":")) if isinstance(expected, list) else expected,
        "status": "pass" if observed == expected else "fail",
    } for check_id, label, observed, expected in checks]


def build_outputs(source_path: Path, target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    source_rows = verify_source(source_path)
    cohort, registry = derive_rows(source_rows)
    baseline = baseline_rows(registry)
    checks = check_rows(cohort, registry, baseline)
    if any(row["status"] != "pass" for row in checks):
        raise ValueError("One or more modeling-workspace release checks failed.")
    target.mkdir(parents=True)
    outputs: dict[str, tuple[list[dict[str, object]], tuple[str, ...] | None]] = {
        "modeling-cohort.csv": (cohort, SOURCE_FIELDS + DERIVED_FIELDS),
        "split-registry.csv": (registry, None),
        "baseline-metrics.csv": (baseline, None),
        "modeling-checks.csv": (checks, None),
    }
    report: dict[str, object] = {
        "status": "pass",
        "version": "0.1.0",
        "source": {"rows": 374, "fields": 29, "bytes": source_path.stat().st_size, "sha256": sha256(source_path)},
        "outputs": {},
        "split": {
            split: {"rows": spec["rows"], "positives": spec["positives"], "negatives": spec["rows"] - spec["positives"], "first_index_date": spec["first"], "last_index_date": spec["last"]}
            for split, spec in SPLIT_SPECS.items()
        },
        "baseline": {"fit_split": "train", "constant_probability": baseline[0]["constant_probability"]},
        "decision": {"reference_disposition": "accept with conditions", "module_02_progression": "allowed"},
    }
    for name, (rows, fields) in outputs.items():
        path = target / name
        write_csv(path, rows, fields)
        report["outputs"][name] = {
            "rows": len(rows), "fields": len(fields or rows[0]),
            "bytes": path.stat().st_size, "sha256": sha256(path),
        }
    report_path = target / "build-report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="")
    return report


def build_workspace(source_path: Path, target: Path) -> dict[str, object]:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    verify_source(source_path)
    shutil.copytree(MODULE_ROOT / "learner-template", target)
    for name in PORTABLE_FILES:
        shutil.copy2(MODULE_ROOT / name, target / name)
    shutil.copy2(__file__, target / Path(__file__).name)
    shutil.copy2(MODULE_ROOT / "validate_modeling_workspace.py", target / "validate_modeling_workspace.py")
    data_dir = target / "data"
    data_dir.mkdir()
    shutil.copy2(source_path, data_dir / "resolved-analytic-table.csv")
    return build_outputs(data_dir / "resolved-analytic-table.csv", target / "outputs")


def self_check() -> None:
    source = default_source()
    with tempfile.TemporaryDirectory(prefix="fnd2-module01-build-") as temp_dir:
        root = Path(temp_dir)
        output = root / "outputs"
        report = build_outputs(source, output)
        assert report["split"]["train"]["rows"] == 224
        assert report["split"]["test"]["positives"] == 4
        try:
            build_outputs(source, output)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not refuse an existing output target.")
        workspace = root / "learner-workspace"
        workspace_report = build_workspace(source, workspace)
        assert workspace_report["baseline"]["constant_probability"] == "0.111607142857"
        assert (workspace / "data" / "resolved-analytic-table.csv").stat().st_size == SOURCE_BYTES
        reproduced = workspace / "reproduced-outputs"
        reproduced_report = build_outputs(workspace / "data" / "resolved-analytic-table.csv", reproduced)
        assert reproduced_report["outputs"] == workspace_report["outputs"]
    print("FND-2 Module 01 builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path)
    parser.add_argument("--source", type=Path, default=default_source())
    parser.add_argument("--build-reference", action="store_true")
    parser.add_argument("--outputs-only", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if args.build_reference:
        report = build_outputs(args.source.resolve(), MODULE_ROOT / "outputs")
        print(json.dumps(report, indent=2))
        return
    if args.outputs_only:
        if args.target is None:
            parser.error("target is required with --outputs-only")
        report = build_outputs(args.source.resolve(), args.target.resolve())
        print(json.dumps(report, indent=2))
        return
    if args.target is None:
        parser.error("target is required unless --self-check or --build-reference is used")
    report = build_workspace(args.source.resolve(), args.target.resolve())
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
