# Module 11 data specification

## Purpose

The release lets learners build and audit a conserved patient flow without using protected health information. It preserves every source row needed to reproduce the case while removing unused synthetic identifier-like fields.

## Data lineage

```text
Pinned Synthea CSV archive
  -> all 1,171 patient rows, 6 selected fields
  -> all 53,346 encounter rows, 9 selected fields
  -> 374-person adult acute index cohort
  -> 15 aggregate edges and 7 decision paths
  -> alluvial flow, matrix, composition, exact table, and text alternative
```

## Source archive

- URL: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- Archive size: 8,982,431 bytes.
- Archive SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`.
- Retrieved: 2026-08-30.
- Required members: `csv/patients.csv` and `csv/encounters.csv`.

## Source selection 1: patients

Grain: one synthetic patient.

| Field | Type | Meaning |
|---|---|---|
| `patient_id` | UUID text | Synthetic patient key. |
| `birth_date` | date | Synthetic birth date used only for age eligibility. |
| `death_date` | date or blank | Synthetic death date used for the mutually exclusive endpoint. |
| `sex` | categorical text | Source gender field, retained as `M` or `F` in this archive. |
| `race` | categorical text | Synthea race value. |
| `ethnicity` | categorical text | Synthea ethnicity value. |

The released table has 1,171 rows and 6 columns.

## Source selection 2: encounters

Grain: one synthetic encounter.

| Field | Type | Meaning |
|---|---|---|
| `encounter_id` | UUID text | Unique synthetic encounter key. |
| `start` | UTC timestamp | Encounter start. |
| `stop` | UTC timestamp | Encounter end. |
| `patient_id` | UUID text | Foreign key to the patient selection. |
| `encounter_class` | categorical text | Ambulatory, emergency, inpatient, outpatient, urgent care, or wellness. |
| `code` | text | Source encounter code. |
| `description` | text | Source encounter description. |
| `reason_code` | text or blank | Optional source reason code. |
| `reason_description` | text or blank | Optional source reason description. |

The released table has 53,346 rows and 9 columns. Every encounter patient joins to exactly one released patient.

## Teaching cohort

Grain: one adult synthetic patient with one qualifying index event.

### Eligibility

1. The patient has an emergency or inpatient encounter between 2015-01-01 and 2019-12-31 inclusive.
2. The patient is at least 18 years old at that encounter.
3. The first eligible encounter becomes the single index event.

Patients without a qualifying event and patients younger than 18 at the candidate event do not enter the cohort. The cohort contains 374 patients.

### Thirty-day state

The first different encounter starting after index stop and within 30 days is grouped as:

| Source class | Teaching state |
|---|---|
| `ambulatory`, `outpatient`, `wellness` | Scheduled care |
| `urgentcare` | Urgent care |
| `emergency`, `inpatient` | Acute return |
| no qualifying encounter | No encounter recorded |

This grouping is a teaching definition. Scheduled care does not prove planned transitional follow-up.

### Ninety-day endpoint

The endpoint is mutually exclusive:

1. `Death within 90 days` if the synthetic death date is after index stop and no more than 90 days later.
2. Otherwise `Acute return within 90 days` if an emergency or inpatient encounter starts after index stop and no more than 90 days later.
3. Otherwise `No acute return within 90 days`.

Death takes precedence so each person has one terminal state. The separate `acute_return_90d` field remains available to audit whether an acute encounter occurred before death.

## Cohort field dictionary

| Field | Meaning |
|---|---|
| `patient_id` through `ethnicity` | Patient source fields. |
| `age_at_index` | Completed years at index start. |
| `index_encounter_id` | Selected first qualifying encounter. |
| `index_start`, `index_stop` | UTC index timestamps. |
| `index_class` | Emergency or Inpatient. |
| `next_30d_state` | Mutually exclusive first next-state group. |
| `next_30d_encounter_id` | Source encounter ID or blank. |
| `next_30d_start` | Source start timestamp or blank. |
| `next_30d_days_after_index_stop` | Elapsed days to three decimals or blank. |
| `acute_return_90d` | Yes if any acute encounter occurs in the 90-day window. |
| `death_90d` | Yes if the synthetic death date occurs in the window. |
| `endpoint_90d` | Mutually exclusive endpoint. |
| `transition_path` | Index class and 30-day state joined with ` -> `. |
| `path_count` | Number of cohort patients on that path. |
| `path_denominator` | Same path count, made explicit for the path rate. |
| `path_acute_return_count` | Patients on the path with an acute return within 90 days. |
| `path_acute_return_pct` | Path acute-return count divided by path denominator. |
| `cohort_acute_return_pct` | All cohort acute returns divided by 374. |
| `priority_screen` | Yes when path count is at least 20 and path percentage exceeds cohort percentage. |

## Edge table

Grain: one aggregate directed edge between adjacent stages.

| Field | Meaning |
|---|---|
| `stage_from`, `node_from` | Origin stage and state. |
| `stage_to`, `node_to` | Destination stage and state. |
| `patient_count` | Conserved patient count on the edge. |
| `cohort_denominator`, `cohort_pct` | Count relative to all 374 patients. |
| `node_from_denominator`, `node_from_pct` | Count relative to the origin node. |

Each stage sums to 374. All outgoing edges from one node sum to that node's denominator.

## Measured facts

| Result | Value |
|---|---:|
| Cohort patients | 374 |
| Emergency index | 314 |
| Inpatient index | 60 |
| No encounter recorded within 30 days | 263 |
| Scheduled care within 30 days | 92 |
| Urgent care within 30 days | 4 |
| Acute return as first 30-day state | 15 |
| Any acute return within 90 days | 36 |
| Death within 90 days | 8 |
| Overall acute-return percentage | 9.6% |
| Reference audit path | Inpatient -> No encounter recorded |
| Reference audit path denominator | 38 |
| Reference audit path acute-return percentage | 15.8% |

## Priority screen

The reference screen is:

```text
path_count >= 20
and
path_acute_return_pct > cohort_acute_return_pct
```

It identifies a manageable teaching path with more synthetic acute returns than the cohort percentage. It is not an official quality screen, statistical test, benchmark, risk-adjusted measure, or allocation rule.

## Conservation rules

- Each patient has one index class.
- Each patient has one 30-day state.
- Each patient has one 90-day endpoint.
- Stage totals must equal 374.
- A missing follow-up row remains an explicit state rather than disappearing.
- Rates never travel as ribbon widths. Counts travel; rates belong in the table, matrix, or composition view.

## Missingness and absence

Blank death dates mean the synthetic record does not contain a death date. Blank next encounter fields mean no qualifying encounter is present during the 30-day window. Neither blank supports a claim about real-world care.

## Rights and minimization

Synthea is open-source under Apache 2.0, and its official site describes the generated records as free of privacy and security restrictions. The Commons still applies minimization as a teaching habit. Synthetic direct identifier-like fields and unused financial or organizational identifiers are not redistributed.

## Interpretation limits

- The data are simulated.
- The sample is not representative of a current real population.
- Encounter classes are generator outputs, not adjudicated claims or local EHR definitions.
- No encounter recorded is not the same as no care.
- The module does not risk-adjust outcomes.
- The module does not infer causality.
- Small path counts make rates unstable.
- The reference screen only chooses a definition-audit target.

## Refresh contract

A source refresh requires a new source date, archive checksum, row and column counts, measured facts, module version, Commons version, validator expectations, visual inspection, and human review. A changed upstream archive must not silently overwrite this release.
