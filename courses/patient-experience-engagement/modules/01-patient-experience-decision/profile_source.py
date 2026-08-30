"""Profile and verify the complete CMS HCAHPS hospital source."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import shutil
import tempfile
from collections import Counter
from decimal import Decimal
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = MODULE_ROOT / "data" / "raw" / "HCAHPS-Hospital.csv.gz"
DEFAULT_OUTPUT = MODULE_ROOT / "data"
EXPECTED_GZIP_BYTES = 2_195_547
EXPECTED_GZIP_SHA256 = "56c6c11f1d61820f367417a00b1e2abaaf02d0b7104d7a5429031e750332503c"
EXPECTED_RAW_BYTES = 105_461_119
EXPECTED_RAW_SHA256 = "b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc"
EXPECTED_HEADER = [
    "Facility ID", "Facility Name", "Address", "City/Town", "State", "ZIP Code",
    "County/Parish", "Telephone Number", "HCAHPS Measure ID", "HCAHPS Question",
    "HCAHPS Answer Description", "Patient Survey Star Rating",
    "Patient Survey Star Rating Footnote", "HCAHPS Answer Percent",
    "HCAHPS Answer Percent Footnote", "HCAHPS Linear Mean Value",
    "Number of Completed Surveys", "Number of Completed Surveys Footnote",
    "Survey Response Rate Percent", "Survey Response Rate Percent Footnote",
    "Start Date", "End Date",
]
DISCHARGE_ROLES = {
    "H_COMP_6_Y_P": "primary recovery-at-home decision anchor",
    "H_COMP_6_N_P": "complementary recovery-at-home response",
    "H_DISCH_HELP_Y_P": "support-after-discharge item",
    "H_SYMPTOMS_Y_P": "warning-sign information item",
}
PROFILE_FIELDS = ["metric_id", "metric", "value", "unit", "method", "decision_use"]
INVENTORY_FIELDS = [
    "measure_id", "question", "answer_description", "reported_value_field",
    "facility_rows", "reported_value_rows", "unavailable_value_rows", "teaching_role",
]
DISCHARGE_FIELDS = [
    "measure_id", "role", "facility_rows", "reported_percent_rows",
    "unavailable_percent_rows", "min_percent", "q1_percent", "median_percent",
    "q3_percent", "max_percent",
]


class SourceError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def raw_fingerprint(path: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0
    with gzip.open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            size += len(block)
            digest.update(block)
    return size, digest.hexdigest()


def numeric(value: str) -> Decimal | None:
    try:
        return Decimal(value)
    except Exception:
        return None


def value_field(measure_id: str) -> str:
    if measure_id.endswith("STAR_RATING") or measure_id == "H_STAR_RATING":
        return "Patient Survey Star Rating"
    if "LINEAR_SCORE" in measure_id:
        return "HCAHPS Linear Mean Value"
    return "HCAHPS Answer Percent"


def quantile(values: list[Decimal], fraction: Decimal) -> Decimal:
    ordered = sorted(values)
    position = Decimal(len(ordered) - 1) * fraction
    lower = int(position)
    upper = lower if position == lower else lower + 1
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * weight


def display(value: Decimal) -> str:
    return format(value.normalize(), "f")


def scan(path: Path) -> dict[str, object]:
    if path.stat().st_size != EXPECTED_GZIP_BYTES or sha256(path) != EXPECTED_GZIP_SHA256:
        raise SourceError("Compressed source fingerprint changed")
    raw_bytes, raw_sha = raw_fingerprint(path)
    if raw_bytes != EXPECTED_RAW_BYTES or raw_sha != EXPECTED_RAW_SHA256:
        raise SourceError("Decompressed source fingerprint changed")

    rows = 0
    facilities: dict[str, tuple[str, str, str]] = {}
    measures: dict[str, dict[str, object]] = {}
    states: set[str] = set()
    periods: set[tuple[str, str]] = set()
    discharge: dict[str, list[Decimal]] = {key: [] for key in DISCHARGE_ROLES}
    discharge_unavailable = Counter()

    with gzip.open(path, "rb") as binary:
        with io.TextIOWrapper(binary, encoding="utf-8-sig", newline="") as text:
            reader = csv.DictReader(text)
            if list(reader.fieldnames or []) != EXPECTED_HEADER:
                raise SourceError("Source header changed")
            for row in reader:
                rows += 1
                facility_id = row["Facility ID"]
                facility_fact = (
                    row["State"], row["Survey Response Rate Percent"],
                    row["Number of Completed Surveys"],
                )
                prior = facilities.setdefault(facility_id, facility_fact)
                if prior != facility_fact:
                    raise SourceError(f"Facility-level survey facts changed within {facility_id}")
                states.add(row["State"])
                periods.add((row["Start Date"], row["End Date"]))

                measure_id = row["HCAHPS Measure ID"]
                measure = measures.setdefault(measure_id, {
                    "question": row["HCAHPS Question"],
                    "answer_description": row["HCAHPS Answer Description"],
                    "facility_rows": 0,
                    "reported_value_rows": 0,
                })
                if (
                    measure["question"] != row["HCAHPS Question"] or
                    measure["answer_description"] != row["HCAHPS Answer Description"]
                ):
                    raise SourceError(f"Measure wording changed within {measure_id}")
                measure["facility_rows"] = int(measure["facility_rows"]) + 1
                if numeric(row[value_field(measure_id)]) is not None:
                    measure["reported_value_rows"] = int(measure["reported_value_rows"]) + 1

                if measure_id in discharge:
                    percent = numeric(row["HCAHPS Answer Percent"])
                    if percent is None:
                        discharge_unavailable[measure_id] += 1
                    else:
                        discharge[measure_id].append(percent)

    if rows != 325_720 or len(facilities) != 4_790 or len(measures) != 68 or len(states) != 56:
        raise SourceError("Source dimensions changed")
    if periods != {("10/01/2024", "09/30/2025")}:
        raise SourceError("Reporting period changed")
    if {int(item["facility_rows"]) for item in measures.values()} != {4_790}:
        raise SourceError("A measure no longer has one row per facility")

    response_rates = [numeric(value[1]) for value in facilities.values()]
    response_rates = [value for value in response_rates if value is not None]
    completed = [numeric(value[2]) for value in facilities.values()]
    completed = [value for value in completed if value is not None]
    if len(response_rates) != 3_949 or len(completed) != 3_949:
        raise SourceError("Facility response or completed-survey support changed")

    profile_values = [
        ("SP01", "source rows", rows, "row", "streamed CSV count", "full-source scope"),
        ("SP02", "source columns", len(EXPECTED_HEADER), "field", "exact header", "source structure"),
        ("SP03", "public facilities", len(facilities), "facility", "distinct Facility ID", "facility-level grain"),
        ("SP04", "HCAHPS measure IDs", len(measures), "measure", "distinct measure ID", "measurement inventory"),
        ("SP05", "state or territory codes", len(states), "code", "distinct State", "geographic coverage only"),
        ("SP06", "rows per measure", 4790, "row", "all measure counts agree", "one row per facility and measure"),
        ("SP07", "reporting period start", "2024-10-01", "date", "source Start Date", "time boundary"),
        ("SP08", "reporting period end", "2025-09-30", "date", "source End Date", "time boundary"),
        ("SP09", "decompressed source bytes", raw_bytes, "byte", "gzip stream count", "source fingerprint"),
        ("SP10", "decompressed source SHA-256", raw_sha, "hash", "SHA-256", "source fingerprint"),
        ("SP11", "stored gzip bytes", path.stat().st_size, "byte", "file size", "portable full source"),
        ("SP12", "stored gzip SHA-256", sha256(path), "hash", "SHA-256", "portable full source"),
        ("SP13", "facilities with numeric response rate", len(response_rates), "facility", "distinct facility value", "response support"),
        ("SP14", "facilities without numeric response rate", len(facilities) - len(response_rates), "facility", "distinct facility value", "public-value gap"),
        ("SP15", "response rate first quartile", display(quantile(response_rates, Decimal("0.25"))), "percent", "facility distribution", "response context"),
        ("SP16", "response rate median", display(quantile(response_rates, Decimal("0.50"))), "percent", "facility distribution", "response context"),
        ("SP17", "response rate third quartile", display(quantile(response_rates, Decimal("0.75"))), "percent", "facility distribution", "response context"),
        ("SP18", "sum of reported completed survey counts", display(sum(completed)), "reported survey count", "sum across supported facilities", "scale, not distinct-patient proof"),
        ("SP19", "patient-level response rows", 0, "row", "source grain review", "patient-level inference prohibited"),
        ("SP20", "public facility identities", len(facilities), "facility", "distinct Facility ID", "ranking prohibited"),
    ]
    source_profile = [dict(zip(PROFILE_FIELDS, map(str, item))) for item in profile_values]

    inventory = []
    for measure_id in sorted(measures):
        measure = measures[measure_id]
        reported = int(measure["reported_value_rows"])
        inventory.append({
            "measure_id": measure_id,
            "question": str(measure["question"]),
            "answer_description": str(measure["answer_description"]),
            "reported_value_field": value_field(measure_id),
            "facility_rows": str(measure["facility_rows"]),
            "reported_value_rows": str(reported),
            "unavailable_value_rows": str(4790 - reported),
            "teaching_role": DISCHARGE_ROLES.get(measure_id, "source inventory"),
        })

    discharge_profile = []
    for measure_id, role in DISCHARGE_ROLES.items():
        values = discharge[measure_id]
        discharge_profile.append({
            "measure_id": measure_id,
            "role": role,
            "facility_rows": "4790",
            "reported_percent_rows": str(len(values)),
            "unavailable_percent_rows": str(discharge_unavailable[measure_id]),
            "min_percent": display(min(values)),
            "q1_percent": display(quantile(values, Decimal("0.25"))),
            "median_percent": display(quantile(values, Decimal("0.50"))),
            "q3_percent": display(quantile(values, Decimal("0.75"))),
            "max_percent": display(max(values)),
        })

    return {
        "summary": {
            "rows": rows, "facilities": len(facilities), "measures": len(measures),
            "states": len(states), "response_rate_facilities": len(response_rates),
            "completed_surveys_sum": int(sum(completed)),
        },
        "source-profile.csv": (PROFILE_FIELDS, source_profile),
        "measure-inventory.csv": (INVENTORY_FIELDS, inventory),
        "discharge-measure-profile.csv": (DISCHARGE_FIELDS, discharge_profile),
    }


def render_csv(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def write_profiles(source: Path, output_dir: Path, overwrite: bool = False) -> dict[str, object]:
    result = scan(source)
    output_dir.mkdir(parents=True, exist_ok=True)
    for name in ("source-profile.csv", "measure-inventory.csv", "discharge-measure-profile.csv"):
        path = output_dir / name
        if path.exists() and not overwrite:
            raise FileExistsError(f"Refusing to overwrite existing profile: {path}")
        fields, rows = result[name]
        path.write_bytes(render_csv(fields, rows))
    return result["summary"]


def verify_committed(source: Path = DEFAULT_SOURCE, output_dir: Path = DEFAULT_OUTPUT) -> dict[str, object]:
    result = scan(source)
    for name in ("source-profile.csv", "measure-inventory.csv", "discharge-measure-profile.csv"):
        fields, rows = result[name]
        expected = render_csv(fields, rows)
        path = output_dir / name
        if not path.is_file() or path.read_bytes() != expected:
            raise SourceError(f"Committed profile changed: {name}")
    return result["summary"]


def self_check() -> None:
    summary = verify_committed()
    with tempfile.TemporaryDirectory(prefix="app2-module01-profile-") as temp_dir:
        base = Path(temp_dir)
        first, second = base / "first", base / "second"
        write_profiles(DEFAULT_SOURCE, first)
        write_profiles(DEFAULT_SOURCE, second)
        for name in ("source-profile.csv", "measure-inventory.csv", "discharge-measure-profile.csv"):
            assert (first / name).read_bytes() == (second / name).read_bytes()
        changed = base / "changed.csv.gz"
        shutil.copy2(DEFAULT_SOURCE, changed)
        content = bytearray(changed.read_bytes())
        content[-1] ^= 1
        changed.write_bytes(content)
        try:
            scan(changed)
        except SourceError as error:
            assert "fingerprint changed" in str(error)
        else:
            raise AssertionError("Profiler accepted a changed source")
    assert summary == {
        "rows": 325720, "facilities": 4790, "measures": 68, "states": 56,
        "response_rate_facilities": 3949, "completed_surveys_sum": 2411406,
    }
    print("APP-2 Module 01 source profiler self-check passed: full source, deterministic profiles, and changed-source rejection.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--verify-committed", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
        elif args.write:
            print(json.dumps(write_profiles(args.source, args.output_dir, args.force), indent=2))
        elif args.verify_committed:
            print(json.dumps(verify_committed(args.source, args.output_dir), indent=2))
        else:
            print(json.dumps(scan(args.source)["summary"], indent=2))
    except (OSError, ValueError, SourceError) as error:
        parser.exit(1, f"Source profiling failed: {error}\n")


if __name__ == "__main__":
    main()
