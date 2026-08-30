# FND-2 Module 01 data specification

## Immutable input

| Property | Contract |
|---|---|
| Upstream owner | FND-1 Module 04 |
| File | `resolved-analytic-table.csv` |
| Rows | 374 |
| Source fields | 29 |
| Grain | one selected synthetic adult and one index encounter per row |
| Bytes | 121787 |
| SHA-256 | `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a` |
| Source release | `synthea-csv-apr2020` |
| Cohort definition | 0.1.0 |
| Real patients | none |

The input is verified and copied. It is never edited in place. Any change to its bytes, fields, row count, patient grain, index grain, source release, or cohort version stops the build.

## Modeling unit and target

One modeling row represents one selected synthetic adult at the stop of one index emergency or inpatient encounter. The target is `acute_return_90d`: whether a different emergency or inpatient encounter appears within 90 days after index stop.

Prediction time is `index_stop`. The outcome horizon is 90 days. The source is fully observed for the registered synthetic follow-up contract, but that does not make the cohort representative of real patients.

## Derived modeling cohort

`modeling-cohort.csv` preserves all 29 source fields and appends:

| Field | Meaning | Model use |
|---|---|---|
| `model_row_id` | stable row-tracking ID assigned after temporal ordering | tracking only |
| `prediction_time` | exact copy of `index_stop` | metadata only |
| `outcome_horizon_days` | fixed value 90 | metadata only |
| `split` | frozen train, validation, or test assignment | never a predictor |
| `split_order` | one-based order by `index_start` then `patient_id` | never a predictor |

The derived file has 374 rows and 34 fields. It changes order only: source values remain byte-for-value equivalent within each row.

## Feature boundary

Nine default predictors are allowed: age at index, source gender, source race, source ethnicity, index class, and the four prior-365-day counts.

Patient and encounter IDs are tracking keys. Birth date is excluded from the default model because age is already supplied and direct dates increase disclosure and overfitting risk. Index codes, descriptions, and optional reasons remain excluded until a separate high-cardinality and missingness plan is approved.

All next-30-day fields, all future or outcome-derived 90-day fields, follow-up completion, split labels, split order, metrics, and reviewer decisions are prohibited predictors.

## Temporal split

Rows are sorted once by `index_start` and then `patient_id`.

| Positions | Split | Rows | Positives | Negatives | First date | Last date |
|---|---|---:|---:|---:|---|---|
| 1-224 | train | 224 | 25 | 199 | 2015-01-01 | 2017-04-02 |
| 225-299 | validation | 75 | 7 | 68 | 2017-04-05 | 2018-04-03 |
| 300-374 | test | 75 | 4 | 71 | 2018-04-18 | 2019-12-28 |

The split cannot be regenerated with a new random seed, stratified to look more balanced, or changed after observing performance. A changed row or date requires a new upstream and module version decision.

## Baseline

`baseline-metrics.csv` records one pre-model comparison: the training outcome prevalence applied as a constant probability.

```text
25 / 224 = 0.111607142857
```

No validation or test performance metric is calculated in Module 01. Module 03 owns model comparison and the single final evaluation on untouched test data.

## Output files

| Output | Rows | Role |
|---|---:|---|
| `modeling-cohort.csv` | 374 | exact source plus registered derivation fields |
| `split-registry.csv` | 374 | row identity, time, split, order, and label reconciliation |
| `baseline-metrics.csv` | 1 | frozen training-prevalence baseline definition |
| `modeling-checks.csv` | 24 | executable release invariants |
| `build-report.json` | 1 object | fingerprints, split facts, baseline, and disposition |

All CSV files use UTF-8 and LF line endings. Generated files are never hand-edited.
