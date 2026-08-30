# Module 13 data and invariant specification

## Purpose

Module 13 reuses one stable public evidence chain to teach audience adaptation. It does not create a new source release.

The technical and executive outputs must remain numerically, definitionally, temporally, and ethically consistent.

## Lineage

```text
CMS Timely and Effective Care - Hospital, release 2026-08-13
  -> Module 12 Massachusetts EDV, OP_18b, and OP_22 source selection
  -> Module 12 186-row teaching table and three-row measure dictionary
  -> Module 13 three-row selected-facility exact table
  -> technical quality-director story
  -> executive quality-committee story
  -> cross-audience invariant audit
```

## Complete CMS source

- Dataset ID: `yv7e-xc69`.
- Release date: 2026-08-13.
- Rows: 138,084.
- Columns: 16.
- Bytes: 34,150,899.
- SHA-256: `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516`.
- Landing page: https://data.cms.gov/provider-data/dataset/yv7e-xc69
- Pinned CSV: https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv

## Reused Module 12 releases

| File | Rows | Columns | SHA-256 |
|---|---:|---:|---|
| `cms_ma_ed_dashboard_source_2026.csv` | 186 | 15 | `f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b` |
| `ma_ed_public_reporting_dashboard_2026.csv` | 186 | 31 | `fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd` |
| `ed_dashboard_measure_dictionary_2026.csv` | 3 | 18 | `2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412` |

The Module 13 lab reads the upstream teaching table directly. Duplication would create an unnecessary synchronization risk.

## Selected exact-table grain

One selected facility, one measure, one reporting period.

The exact table contains three rows:

- EDV;
- OP_18b; and
- OP_22.

## Exact table fields

| Field | Meaning |
|---|---|
| `measure_id` | Stable CMS measure identity. |
| `display_label` | Audience-ready label tied to the source definition. |
| `score_raw` | Exact released source representation. |
| `score_numeric` | Numeric value when applicable. |
| `unit` | Category, minutes, or percent. |
| `sample` | Released source sample field when provided. |
| `value_status` | Reported numeric, reported category, or unavailable. |
| `footnote` | Released source footnote when provided. |
| `period_start`, `period_end` | Reporting window. |
| `cms_release_date` | Pinned CMS release date. |
| `source_lag_days_at_release` | Days from period end to release. |
| `ma_reported_n` | Numeric Massachusetts peer count when applicable. |
| `ma_median` | Descriptive Massachusetts median. |
| `ma_rank_unfavorable` | Descriptive lower-is-better rank. |
| `scenario_threshold` | Mock course review trigger. |
| `threshold_crossed` | Scenario result. |
| `threshold_origin` | Explicit course, non-CMS origin. |
| `monitoring_use` | Historical public-reporting use label. |
| `action_if_crossed` | Validation-first action boundary. |

## Stable values

### EDV

- Value: low.
- Unit: CMS volume category.
- Role: context only.
- Period: 2024-01-01 through 2024-12-31.
- Lag: 590 days.
- Trigger: not applicable.

### OP_18b

- Value: 188 minutes.
- Sample: 422.
- Peer count: 54.
- Massachusetts median: 211.5 minutes.
- Unfavorable rank: 45.
- Mock trigger: 240 minutes.
- Trigger result: not crossed.
- Period: 2024-10-01 through 2025-09-30.
- Lag: 317 days.

### OP_22

- Value: 23 percent.
- Source sample: 19,211.
- Peer count: 53.
- Massachusetts median: 3 percent.
- Unfavorable rank: 1.
- Mock trigger: 10 percent.
- Trigger result: crossed.
- Period: 2024-01-01 through 2024-12-31.
- Lag: 590 days.

## Invariant classes

### Source invariants

- publisher;
- dataset ID;
- landing page;
- source file URL;
- release date;
- checksums;
- selected filter; and
- source rights.

### Definition invariants

- measure IDs;
- display definitions;
- units;
- directions;
- population or summary meaning;
- sample-field meaning;
- reporting windows; and
- interpretation limits.

### Numeric invariants

- selected values;
- samples;
- peer counts;
- medians;
- ranks;
- trigger values;
- trigger results; and
- lag.

### Decision invariants

- finding;
- historical-use label;
- trigger origin;
- supported action;
- action owner;
- current-local-data requirement;
- material limitation; and
- unsupported conclusions.

## Adaptable classes

- title length;
- annotation density;
- evidence sequence;
- peer-detail depth;
- terminology explanation;
- footnote placement;
- figure aspect ratio;
- decision-brief length; and
- presentation time.

Adaptable elements cannot change an invariant.

## Technical figure contract

The peer distribution uses only reported numeric OP-22 values. Unavailable values remain in the upstream release and are accounted for by the reported count.

The selected facility uses a diamond and direct label. The median and mock trigger use different line patterns and direct labels.

The y position orders hospitals by public value and does not encode another clinical variable.

## Executive figure contract

The three cards represent:

1. source-supported signal;
2. time boundary; and
3. decision request.

They are not three independent KPIs.

The executive figure must retain the threshold boundary, owner, return evidence, and unsupported conclusion.

## Cross-version audit

Before release, compare:

- every number;
- every unit;
- every date;
- peer-language meaning;
- threshold value and origin;
- trigger result;
- action wording;
- action owner;
- freshness boundary;
- causal language;
- current-performance language;
- subgroup language; and
- source line.

Any unexplained difference fails the release.

## Rights

CMS Provider Data Catalog records are public U.S. government reporting data. Attribution is retained and reuse does not imply endorsement.

The module reuses no third-party image or copyrighted narrative asset.

## Interpretation limits

- Historical public aggregate data.
- Different measure windows.
- Descriptive peer context.
- Mock course triggers.
- No subgroup evidence.
- No real-time operations.
- No causal design.
- No intervention-effect evidence.
- No authority to change care.

## Refresh contract

A source refresh is a new release. It requires new checksums, rows, columns, periods, selected values, peer context, trigger results, lag, validator expectations, figures, exact table, alternatives, adaptation record, decision brief, version, visual inspection, and human review.
