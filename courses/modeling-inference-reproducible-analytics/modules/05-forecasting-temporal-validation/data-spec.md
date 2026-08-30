# Data specification

## Public source releases

| Input | Rows | Fields | SHA-256 |
|---|---:|---:|---|
| CDC NHSN all-jurisdiction release | 6,208 | 14 | `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1` |
| Massachusetts teaching series | 94 | 21 | `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616` |

The source is CDC's Weekly Hospital Respiratory Data, HRD Metrics by Jurisdiction, dataset `rhwp-grxi`: https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi

Rows are public jurisdiction-week aggregates across reporting hospitals, not patient or single-hospital records. The period is 2024-11-09 through 2026-08-22.

## Forecast series

Every Massachusetts date is unique and exactly seven days after the prior row. `week_index` runs from 1 through 94. The target `total_respiratory_new_admissions` equals the row sum of `covid_new_admissions`, `flu_new_admissions`, and `rsv_new_admissions`.

Context fields include the number and percentage of hospitals reporting occupancy and `reporting_gap_pct`. Those fields are not denominators or correction weights for admissions.

## Folds

Five expanding windows end at weeks 74, 78, 82, 86, and 90. Each predicts the next four weeks. Test blocks are non-overlapping and together cover weeks 75 through 94. A fit may use only source rows at or before its origin.

## Models

- `LAST`: repeat the final training target.
- `SNAIVE52`: use the target 52 weeks earlier.
- `HOLT_DAMPED`: refit additive level and damped trend inside each fold.
- `ARIMA111`: supplied recognition example at the final origin; ineligible for selection.

## Interpretation limits

- The aggregate can change when contributing hospitals change.
- Counts are not population rates or a complete burden estimate.
- Reported seasonal patterns do not prove causes.
- Backtest accuracy does not establish operational utility.
- MAPE is unstable at small actual counts.
- Supplied intervals are illustrative, not calibrated.
- Source values and forecast misses must never be edited to improve results.
