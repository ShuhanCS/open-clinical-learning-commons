# CMS HCAHPS teaching extract specification

## Purpose

This extract supports one lesson: translate healthcare variables into explicit marks and visual channels. It contains every Massachusetts hospital row for the CMS HCAHPS measure `H_RECMND_DY` in the 2026-08-13 release.

The lab uses a 15-row view selected by completed survey count so hospital labels remain legible. The full 65-row state extract stays available for source inspection, missing-value review, and later exercises.

## Rebuild and validate

From this module directory:

```powershell
Rscript build_hcahps.R
Rscript validate_hcahps.R
```

`build_hcahps.R` uses only base R. It checks the live CMS metadata before fetching data. If CMS no longer reports release `2026-08-13` and modified date `2026-07-22`, the script stops instead of silently replacing the teaching release.

The committed extract remains usable after a later CMS update. Updating it requires a new source review, checksum, module release, and expected-results check.

## Source selection

- Publisher: Centers for Medicare & Medicaid Services
- Dataset: Patient survey (HCAHPS) - Hospital
- Dataset identifier: `dgck-syfz`
- Measure identifier: `H_RECMND_DY`
- Measure: Patients who reported YES, they would definitely recommend the hospital
- Geography filter: `state = MA`
- CMS release: 2026-08-13
- CMS modified date: 2026-07-22
- Measurement period: 2024-10-01 through 2025-09-30
- Retrieved: 2026-08-29
- Source rows after filters: 65
- Reported results: 56
- Not available results: 9

Full URLs are recorded in `source-record.yml`.

## Teaching-extract schema

| Column | Type | Rule and use |
|---|---|---|
| `facility_id` | character | CMS facility identifier. Unique in this one-measure state extract. Treat as nominal. |
| `facility_name` | character | CMS facility name. Used as a nominal category label. |
| `city` | character | CMS city or town. Context only in this module. |
| `state` | character | Always `MA` in this release. |
| `measure_id` | character | Always `H_RECMND_DY`. |
| `measure` | character | Human-readable CMS question. |
| `recommend_percent` | numeric | Published HCAHPS answer percent. Blank when CMS reports the value as unavailable. |
| `completed_surveys` | numeric | Published number of completed surveys. Blank when CMS reports it as unavailable. |
| `response_rate_percent` | numeric | Published survey response rate percent. Blank when unavailable. |
| `value_status` | character | `reported` or `not_available`. Derived from the CMS answer-percent field. |
| `value_footnote` | character | CMS footnote code for the answer percent. Blank when no footnote is supplied. |
| `completed_surveys_footnote` | character | CMS footnote code for completed surveys. |
| `response_rate_footnote` | character | CMS footnote code for response rate. |
| `period_start` | date text | ISO date. Always `2024-10-01`. |
| `period_end` | date text | ISO date. Always `2025-09-30`. |
| `cms_release_date` | date text | ISO date. Always `2026-08-13`. |

## Transformations

The build script performs only these changes:

1. requests rows where `hcahps_measure_id = H_RECMND_DY` and `state = MA`;
2. keeps source identity, measure, result, survey-count, response-rate, footnote, and period fields;
3. renames columns to stable snake-case names;
4. converts reported percentages and counts to numeric values;
5. represents CMS `Not Available` results as blank numeric cells plus `value_status = not_available`;
6. converts dates from `MM/DD/YYYY` to `YYYY-MM-DD`;
7. adds the verified CMS release date; and
8. sorts rows by facility ID.

There is no imputation, aggregation, weighting, ranking, joining, or patient-level transformation.

## Lab peer-set rule

The worked display uses the 15 reported hospitals with the largest `completed_surveys` values. Ties are resolved by ascending facility ID. The rule is deterministic and produces a 34-percentage-point spread in the pinned release.

The rule is for label readability and a useful encoding exercise. It does not define comparable hospitals. Learners must retain completed survey counts in the exported table and describe the selection in their decision note.

## Expected analytic structure

- Unit of observation: one hospital-measure result.
- Grain: facility by measure by measurement period.
- Key in this extract: `facility_id`.
- Outcome used in the chart: `recommend_percent`.
- Context used for the teaching view: `completed_surveys`.
- Missingness: nine hospitals have no published result and carry CMS footnote codes.
- Patient-level interpretation: prohibited because no patient rows are present.

## Validation contract

`validate_hcahps.R` checks:

1. exact schema and column order;
2. 65 rows and 65 unique facility IDs;
3. Massachusetts and `H_RECMND_DY` filters;
4. 56 reported and 9 unavailable values;
5. bounded reported percentages and positive completed-survey counts;
6. agreement between missing numeric values and availability status;
7. retained footnotes for unavailable values;
8. the exact measurement period and CMS release;
9. the 15-row peer-set rule; and
10. enough comparison spread for the planned critique.

## Provenance and checksum

- Original CMS filename: `HCAHPS-Hospital.csv`
- Original CMS file size: 105,461,119 bytes
- Original CMS file SHA-256: `b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc`
- Extract path: `data/hcahps_ma_recommend_2026.csv`
- Rows: 65
- Columns: 16
- SHA-256: `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74`
- Build script: `build_hcahps.R`
- Validator: `validate_hcahps.R`

## Rights and attribution

The CMS hospital data dictionary states that these U.S. government public-reporting data are in the public domain and may be reused. CMS attribution is appreciated. Reuse must not imply federal endorsement of a provider, product, or service.

Data dictionary:

https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf

## Interpretation limits

- HCAHPS reflects surveyed inpatient experiences during the stated period.
- A hospital-level result does not describe every patient or encounter.
- This module does not teach the survey instrument, adjustment method, response bias, reliability, confidence intervals, or statistical comparison.
- Completed survey count does not by itself define precision or comparability.
- A visible difference is not automatically an important, statistically distinguishable, or actionable difference.
- The display supports question formation and follow-up, not causal attribution or a complete judgment of hospital quality.
