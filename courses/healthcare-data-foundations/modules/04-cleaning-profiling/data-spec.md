# Data specification

## Layer contract

The module preserves three distinct layers:

| Layer | Rows | Fields | Grain | Permitted change |
|---|---:|---:|---|---|
| accepted analytic table | 374 | 29 | one row per synthetic patient | none |
| defective analytic table | 379 | 29 | intentionally violates person grain | deterministic manifest only |
| resolved analytic table | 374 | 29 | one row per synthetic patient | rebuild from accepted source |

The accepted and resolved files must share SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.

## Defect contract

`defect-manifest.csv` records 68 changes across 56 issue cases and 20 defect families. It names the affected synthetic patient, field, operation, accepted value, and defective value. Five D01 cases append exact duplicate rows. Multi-field D13 and D14 cases generate three manifest changes each.

`quality-rules.csv` registers 28 rules: D01 through D20 are seeded problems; N01 through N08 are accepted source characteristics. A rule count is calculated independently by `profile_quality.py`, not copied from the manifest.

## Missingness contract

Blank values are structurally allowed only for death date, index description, index reason fields, and the three next-encounter companion fields. Their meaning depends on the field and state. Required-field blanks seeded by D02 or D11 are defects and must be restored from the accepted source.

## Resolution contract

The learner may correct a seeded value only when the accepted source and manifest establish the restoration. The learner may not overwrite the accepted file, impute optional values, drop inconvenient rows, normalize unsupported categories silently, or recompute the cohort. The reference resolution is a clean rebuild from the accepted release.

## SQLite contract

`fnd1-quality-defects.sqlite` contains the accepted table, defective table, manifest, rules, and release metadata. It exists for relational inspection; the CSV files remain the submission and fingerprint contract.
