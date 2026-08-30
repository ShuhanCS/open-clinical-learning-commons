# Module 12 data specification

## Purpose

This release supports a dashboard-design lesson with complete public source preservation, explicit measure windows, exact peer context, named scenario triggers, and action ownership.

The source is historical public reporting. The dashboard is intentionally a review dashboard, not a simulated real-time operations product.

## Data lineage

```text
CMS Timely and Effective Care - Hospital
  -> validate all 138,084 rows and the complete-source checksum
  -> select MA and EDV, OP_18b, OP_22
  -> preserve 186 source rows across 62 hospitals
  -> derive status, peer medians, unfavorable ranks, triggers, lag, and actions
  -> create a three-row measure dictionary
  -> render five decision views, exact table, and text alternative
```

## Complete source

- Dataset ID: `yv7e-xc69`.
- Release: 2026-08-13.
- Rows: 138,084.
- Columns: 16.
- Bytes: 34,150,899.
- SHA-256: `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516`.
- Landing page: https://data.cms.gov/provider-data/dataset/yv7e-xc69
- Pinned CSV: https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv

## Source selection

Filters:

```text
State == MA
and
Measure ID in {EDV, OP_18b, OP_22}
```

The selection contains 186 rows: 62 hospitals by 3 required measure rows. Unavailable values and footnotes remain.

### Source fields

| Field | Meaning |
|---|---|
| `facility_id` | CMS Certification Number used as the hospital key. |
| `facility_name` | Public hospital name. |
| `city`, `state`, `county` | Public location context. |
| `condition` | CMS condition grouping, Emergency Department. |
| `measure_id`, `measure_name` | Public measure identity and source label. |
| `score` | Public category, number, or unavailable label. |
| `sample` | Public source sample or denominator field when provided. |
| `footnote` | Public footnote code when provided. |
| `period_start`, `period_end` | Reporting window. |
| `cms_release_date` | Release date added from the source record. |
| `source_url` | Dataset landing page. |

Street address, ZIP code, and telephone number are omitted because the teaching decision does not need them.

## Measures

### EDV

- Display: Emergency department volume category.
- Unit: CMS category.
- Role: context only.
- Selected hospital value: low.
- Period: 2024-01-01 through 2024-12-31.
- Source lag at release: 590 days.
- No performance trigger.

### OP_18b

- Display: Median ED time before departure.
- Unit: minutes.
- Direction: lower is better.
- Source name excludes transferred patients and psychiatric or mental-health patients.
- Selected hospital value: 188 minutes.
- Selected sample: 422.
- Massachusetts reported hospitals: 54.
- Massachusetts median: 211.5 minutes.
- Range: 113 to 336 minutes.
- Period: 2024-10-01 through 2025-09-30.
- Source lag at release: 317 days.
- Mock trigger: at or above 240 minutes.

### OP_22

- Display: Patients leaving before being seen.
- Unit: percent.
- Direction: lower is better.
- Selected hospital value: 23 percent.
- Selected denominator: 19,211.
- Massachusetts reported hospitals: 53.
- Massachusetts median: 3 percent.
- Range: 0 to 23 percent.
- Period: 2024-01-01 through 2024-12-31.
- Source lag at release: 590 days.
- Mock trigger: at or above 10 percent.

## Teaching table

Grain: one hospital, one measure, one reporting period.

| Field group | Fields | Purpose |
|---|---|---|
| Identity | facility, city, state, county, measure | Join and display. |
| Definition | label, unit, direction | Prevent mixed-unit interpretation. |
| Source value | raw score, numeric score, status, sample, footnote | Preserve exact reporting. |
| Time | start, end, release | Expose reporting windows. |
| Peer context | reported n, median, min, max, unfavorable rank | Descriptive comparison. |
| Scenario | selected hospital, threshold, operator, crossed, origin | Declare mock review logic. |
| Action | lag, monitoring use, action, boundary | Connect display to a defensible response. |

## Value status

- `reported`: numeric score parses successfully.
- `reported_category`: EDV is low, medium, high, or very high.
- `not_available`: score is neither numeric nor a released EDV category.

No unavailable value is imputed.

## Peer calculations

For each numeric measure:

```text
ma_reported_n = count of Massachusetts hospitals with numeric scores
ma_median = ordinary median of those hospital scores
ma_min = minimum reported score
ma_max = maximum reported score
ma_rank_unfavorable = 1 + count of reported scores greater than this score
```

Both numeric measures are lower-is-better. Ties receive the same competition rank.

The median and rank are descriptive. They are not CMS classifications, formal benchmarks, uncertainty-adjusted comparisons, or statistical tests.

## Scenario triggers

The mock quality-improvement charter defines:

```text
OP_18b alert when score >= 240 minutes
OP_22 alert when score >= 10 percent
```

The trigger owner is the fictional course scenario. The thresholds are not CMS benchmarks and must not be transferred to a real hospital without governance and clinical approval.

For Anna Jaques Hospital:

- OP_18b: 188, trigger not crossed.
- OP_22: 23, trigger crossed.
- EDV: context only.

## Source lag

```text
source_lag_days_at_release = cms_release_date - period_end
```

- OP_18b: 317 days.
- OP_22 and EDV: 590 days.

All three rows are labeled `historical_public_reporting_review_only` because the lag exceeds 180 days.

The 180-day label is a teaching classification for use mode. It is not a CMS timeliness rule.

## Action contract

When OP_22 crosses the mock trigger:

1. Validate CMS-to-local numerator, denominator, exclusions, and source completeness.
2. Pull current local monthly OP-22 and ED-time data.
3. If the current local signal persists, review arrival, triage, staffing, and capacity.
4. Record the owner, chosen action, and next review date.

The public value alone does not authorize a staffing or care change.

## Measure dictionary

The three-row dictionary preserves:

- source and display names;
- unit and direction;
- grain;
- numerator or summary;
- denominator or included population;
- sample meaning;
- reporting window;
- release date;
- scenario trigger and result;
- action;
- refresh cadence;
- decision owner;
- interpretation limit; and
- source URL.

## Dashboard view contract

### View 1: alert

Shows the selected OP-22 value, state median, mock trigger, and immediate validation action.

### View 2: freshness

Shows each reporting window and lag at release. It prevents the public values from being read as current.

### View 3: OP-22 peer position

Shows all reported Massachusetts hospitals on a percent scale, the selected hospital, median, and mock trigger.

### View 4: OP-18b peer position

Shows all reported hospitals on a minutes scale. It remains separate from OP-22 because the unit and window differ.

### View 5: action sequence

Shows one owner and four ordered actions. It converts an alert into a review workflow.

## Missingness

| Measure | Reported | Unavailable |
|---|---:|---:|
| EDV | 53 categories | 9 |
| OP_18b | 54 numeric | 8 |
| OP_22 | 53 numeric | 9 |

Unavailable rows remain in source and teaching releases. The dashboard peer plots use only numeric reported rows and state the reported count.

## Rights

CMS Provider Data Catalog data are public U.S. government reporting data. Attribution is preserved and reuse must not imply federal endorsement.

The package links to AHRQ display guidance. It does not reproduce the third-party copyrighted dashboard PDF linked on the AHRQ page.

## Interpretation limits

- Public aggregate reporting is historical.
- Different measures use different windows.
- The dashboard is not real-time.
- The public score is not a local operational series.
- Peer medians are descriptive.
- Scenario triggers are fictional assumptions.
- No causal conclusion is supported.
- No intervention effect is supported.
- Current local data and clinical governance are required before operational action.

## Refresh contract

A source refresh requires new source and selected checksums, row and column counts, reporting windows, medians, ranges, selected-hospital facts, lag calculations, scenario-trigger results, module version, Commons version, validator expectations, visual inspection, and human review.
