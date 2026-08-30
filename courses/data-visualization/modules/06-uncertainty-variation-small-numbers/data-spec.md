# Module 06 data specification

## Purpose

The release supports one question: does a point-only ranking of Massachusetts heart failure readmission estimates justify a focused quality review?

The files preserve CMS estimates, source intervals, denominators, comparison categories, dates, and footnotes. Derived fields only support display and reconciliation. They do not replace the CMS model.

## Raw sources

### Unplanned Hospital Visits - Hospital

- Landing page: https://data.cms.gov/provider-data/dataset/632h-zaca
- Exact CSV: https://data.cms.gov/provider-data/sites/default/files/resources/30edc1d0417a34b58affcc2495a02b0a_1785189969/Unplanned_Hospital_Visits-Hospital.csv
- Rows: 67,060
- Columns: 20
- Bytes: 19,048,784
- SHA-256: `a3e64029ea6daea1f7de163e5b5054b918d0c8be986fccfc47c7a8d5b29a6d1d`

The build selects all 4,790 rows where `Measure ID` equals `READM_30_HF`.

### Unplanned Hospital Visits - National

- Landing page: https://data.cms.gov/provider-data/dataset/cvcs-xecj
- Exact CSV: https://data.cms.gov/provider-data/sites/default/files/resources/d30b0557f1d06bee1d5646d2eaede709_1785189969/Unplanned_Hospital_Visits-National.csv
- Rows: 14
- Bytes: 2,814
- SHA-256: `44e39aedc296f00fa8477a3485a66012cbfcdefb173435199a0b03343c9402c3`

All 14 rows remain in the committed output. The selected row publishes a national rate of 21.3 for 2023-07-01 through 2025-06-30.

### Footnote Crosswalk

- Landing page: https://data.cms.gov/provider-data/dataset/y9us-9xdf
- Exact CSV: https://data.cms.gov/provider-data/sites/default/files/resources/f29bb7c812e242f6edfef0a4b7d0eaca_1760630713/Footnote_Crosswalk.csv
- Rows: 32
- Bytes: 3,456
- SHA-256: `5214e1468fb04c5cdeac8920f2c446cccaa65e2f6f929424cd228042a52d963e`

The full crosswalk remains in the committed output. Each selected hospital footnote joins by its source code.

## Released files

| File | Rows | Role | SHA-256 |
|---|---:|---|---|
| `cms_hf_readmission_hospitals_2026.csv` | 4,790 | All national hospital rows for the selected measure | `e69fcee79711ef8496cb32205b492e6e3a788c4e63009bc1330a84216b0edeba` |
| `cms_unplanned_national_2026.csv` | 14 | Complete national summary release | `408c2d3f27a93c9294f9399e6a0deabfe70076685a5e06f285daf857e92161f9` |
| `cms_footnote_crosswalk_2026.csv` | 32 | Complete official footnote lookup | `94d22120d0efcb0d6f98f3470bce8a7cffb3cf657eb95179556198c4ebae84e7` |
| `ma_hf_readmission_uncertainty_2026.csv` | 65 | Massachusetts decision table with transparent derived fields | `33e6284a1064bb12600903526e4e65c009f875d9e6f6a3f25783d3a9a4b00727` |

## Selected hospital fields

| Field | Type | Source or derivation | Missing-value rule |
|---|---|---|---|
| `facility_id` | text | Facility ID | Preserve text and letter suffixes. |
| `facility_name` | text | Facility Name | Preserve source value. |
| `city` | text | City/Town | Preserve source value. |
| `state` | text | State | Massachusetts is `MA`. |
| `county` | text | County/Parish | Context only. |
| `measure_id` | text | Measure ID | Always `READM_30_HF`. |
| `measure_name` | text | Measure Name | Preserve source value. |
| `compared_to_national` | text | Compared to National | Preserve source category. |
| `denominator` | integer | Denominator | Blank for Not Available or Not Applicable. |
| `score` | decimal | Score | Blank for Not Available. |
| `lower_estimate` | decimal | Lower Estimate | Blank for Not Available. |
| `higher_estimate` | decimal | Higher Estimate | Blank for Not Available. |
| `number_of_patients` | integer | Number of Patients | Blank for Not Available or Not Applicable. |
| `number_of_patients_returned` | integer | Number of Patients Returned | Same rule. |
| `footnote_code` | text | Footnote | Blank when absent. |
| `footnote_text` | text | Joined crosswalk | Blank when no code exists. |
| `start_date` | ISO date | Start Date | Convert only format. |
| `end_date` | ISO date | End Date | Convert only format. |
| `estimate_status` | text | Source score, category, and footnote | `reported`, `too_few`, or `not_available`. |
| `source_release` | ISO date text | Catalog metadata | `2026-08-13`. |

## Massachusetts derived fields

| Field | Rule |
|---|---|
| `reported_rank_worst_first` | Sort reported scores descending, then facility name ascending. |
| `interval_width` | `higher_estimate - lower_estimate`, rounded to one decimal. |
| `contains_national_rate` | 1 when 21.3 falls inside the source interval. |
| `source_comparison_group` | Short label derived from the exact CMS comparison category. |
| `denominator_display_group` | Under 100, 100 to 499, 500 or more, or unavailable. |
| `top_ten_point_rank` | 1 for reported ranks 1 through 10. |

The denominator group is descriptive. It is not a CMS suppression rule.

## Status logic

```text
if Score is reported:
  estimate_status = reported
else if Compared to National is Number of Cases Too Small or Footnote is 1:
  estimate_status = too_few
else:
  estimate_status = not_available
```

Source text never becomes zero.

## Integrity conditions

- The selected measure has one row per facility ID.
- Every reported point lies between its lower and higher source estimates.
- Every unavailable point and interval field is blank in the release.
- Every used footnote code resolves to the official crosswalk.
- All selected rows use one measure and one reporting period.
- Massachusetts has 65 rows and 53 reported estimates.
- The Massachusetts reporting statuses reconcile to 53 reported, 2 too few, and 10 not available.

## Interpretation limits

- CMS publishes a risk-standardized estimate, not a raw observed proportion.
- The denominator cannot recreate the model or its source interval.
- Lower and higher estimates remain source labels unless a CMS method document establishes a confidence level.
- CMS comparison categories use the national rate, not every hospital pair.
- Visual interval overlap is descriptive and does not test equivalence or pairwise difference.
- Public hospital estimates do not establish patient-level experience or causal quality differences.
