# Module 08 data specification

## Purpose

The release supports one decision: should a weekly Massachusetts hospital metric trigger investigation, remain under routine monitoring, or be treated as insufficient because reporting or process assumptions are unstable?

## Authoritative source

- Publisher: Centers for Disease Control and Prevention
- System: National Healthcare Safety Network
- Dataset: Weekly Hospital Respiratory Data, HRD Metrics by Jurisdiction
- Dataset ID: `rhwp-grxi`
- Landing page: https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi
- Metadata API: https://data.cdc.gov/api/views/rhwp-grxi
- Pinned period: 2024-11-09 through 2026-08-22
- Retrieval date: 2026-08-29
- Raw selected-query rows: 6,208
- Raw selected-query bytes: 790,364
- Raw selected-query SHA-256: `d261cbc441069a41ef1b14347af90dfd6c59e402d7854a5e86288a4f0e9d4dc6`

The exact query URL is recorded in `source-record.yml` and `release.json`. It selects 14 fields, orders by week and jurisdiction, excludes later rows, and requests no more than 10,000 records.

## Released files

| File | Rows | Columns | SHA-256 |
|---|---:|---:|---|
| `data/nhsn_hospital_capacity_jurisdiction_2024_2026.csv` | 6,208 | 14 | `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1` |
| `data/ma_hospital_capacity_time_2024_2026.csv` | 94 | 21 | `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616` |

## All-jurisdiction fields

| Field | Type | Definition and rule |
|---|---|---|
| `week_end` | ISO date | Source week-ending date, reduced to `YYYY-MM-DD`. |
| `jurisdiction` | text | Source jurisdiction abbreviation or national grouping. |
| `respiratory_season` | text or blank | Source respiratory-season label. Blank remains blank. |
| `inpatient_beds` | integer or blank | Total inpatient beds reported for the jurisdiction-week. |
| `inpatient_beds_occupied` | integer or blank | Occupied inpatient beds reported for the jurisdiction-week. |
| `inpatient_occupancy_pct` | decimal or blank | Published occupied inpatient bed percentage. |
| `icu_beds` | integer or blank | Total ICU beds reported for the jurisdiction-week. |
| `icu_beds_occupied` | integer or blank | Occupied ICU beds reported for the jurisdiction-week. |
| `icu_occupancy_pct` | decimal or blank | Published occupied ICU bed percentage. |
| `covid_new_admissions` | integer or blank | Confirmed COVID-19 new hospital admissions. |
| `flu_new_admissions` | integer or blank | Confirmed influenza new hospital admissions. |
| `rsv_new_admissions` | integer or blank | Confirmed RSV new hospital admissions. |
| `hospitals_reporting_occupancy` | integer | Number of hospitals in the occupancy reporting measure. |
| `hospitals_reporting_occupancy_pct` | decimal | Published percent of hospitals reporting occupancy. |

## Massachusetts teaching fields

The Massachusetts release preserves all 14 fields above and adds:

| Field | Type | Derivation and use |
|---|---|---|
| `week_index` | integer | Chronological row number from 1 through 94. |
| `calendar_year` | integer | Calendar year derived from `week_end`. |
| `iso_week` | integer | ISO week number derived from `week_end`. |
| `source_season_status` | text | `source reported` or `source field unavailable`. |
| `days_since_prior` | integer or blank | Seven for every row after the first. |
| `total_respiratory_new_admissions` | integer | Sum of COVID-19, influenza, and RSV new admissions when all three are reported. |
| `reporting_gap_pct` | decimal | `100 - hospitals_reporting_occupancy_pct`; context only, not a correction weight. |

## Completeness and published anomalies

The all-jurisdiction release deliberately preserves source behavior:

- 6,088 jurisdiction-weeks have complete core capacity, occupancy, and admission fields.
- 120 jurisdiction-weeks have all nine core numeric fields blank.
- Three Guam rows report inpatient occupancy counts greater than reported inpatient beds.
- Three Guam or Northern Mariana Islands rows report occupied ICU beds greater than reported ICU beds.
- One Wisconsin row, dated 2026-07-25, reports 100.68 percent coverage.
- The respiratory-season field is unavailable in the Massachusetts source for 61 of 94 weeks and reported for 33.

These records remain intact. The teaching package identifies them as official-source anomalies. It does not silently cap percentages, swap fields, drop rows, or impute values.

## Massachusetts analytic structure

- One row is one jurisdiction-week.
- Dates are unique and increase in seven-day steps.
- All 94 Massachusetts rows have complete core metrics.
- The series is an aggregate of reporting hospitals. It is not a fixed hospital cohort.
- Occupancy percentages are published source values, not recalculated weights.
- Reporting coverage is displayed beside occupancy as context.
- Respiratory admission counts are sums across reporting hospitals, not population rates.

## Baseline and process-chart contract

The reference lab uses the first 26 weeks, 2024-11-09 through 2025-05-03, as a declared teaching baseline for an exploratory individuals chart.

```text
center = mean(baseline occupancy)
moving range = absolute difference between adjacent baseline values
sigma estimate = mean moving range / 1.128
lower limit = center - 3 * sigma estimate
upper limit = center + 3 * sigma estimate
```

The resulting center is 85.23 percent, the lower limit is 80.72 percent, and the upper limit is 89.75 percent. The limits are exploratory. Seasonality, reporting coverage, the aggregate jurisdiction mix, and the absence of a stable internal process definition weaken a formal statistical process-control interpretation.

## Missingness contract

- Blank source values remain blank.
- Missing values do not become zero.
- The source season label is never backfilled from the calendar.
- The first `days_since_prior` value remains blank because no earlier released week exists.
- The first three four-week trailing means remain unavailable by definition.
- A reporting gap does not trigger deletion, weighting, or imputation.

## Build and validation

`build_nhsn_time_series.py` uses Python's standard library. It downloads or reads the pinned query response, verifies its SHA-256 checksum, checks the schema and row counts, normalizes types, builds the Massachusetts release, and writes deterministic CSV files.

`validate_nhsn_time_series.py` runs 47 checks across checksums, field order, row identity, date range, weekly continuity, completeness, published anomalies, source reconciliation, derived fields, and measured facts.

## Interpretation limits

- A jurisdiction aggregate cannot establish one facility's internal process behavior.
- Reporting coverage is context, not a correction weight.
- A seasonal pattern does not by itself establish the cause of an occupancy change.
- A line outside exploratory limits does not establish special cause when process assumptions are weak.
- A smoothed series cannot replace the raw series when weekly operational changes matter.
- Temporal association does not establish an intervention effect.
