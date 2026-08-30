# Chart-selection case specification

## Purpose

The module combines a 10-row curricular case table with the pinned Module 01 HCAHPS extract. The case table is not clinical observation data. It is a versioned set of healthcare decisions, evidence requirements, reference choices, companions, and failure gates.

## Build and validate

```powershell
Rscript build_selection_cases.R
Rscript validate_selection_cases.R
```

## Curricular case release

- Path: `data/selection_cases_2026.csv`
- Rows: 10
- Columns: 13
- SHA-256: `0f295bd9bf94e9f5800e4fdaebea303d8cc0b28ccd3afcb01603d8e1c0a2eff8`
- Builder: `build_selection_cases.R`
- Validator: `validate_selection_cases.R`
- Documentation license: CC BY 4.0

## Schema

| Column | Type | Rule |
|---|---|---|
| `case_id` | character | Unique `C01` through `C10`. |
| `case_title` | character | Plain-language question label. |
| `decision_owner` | character | Named healthcare role or group. |
| `decision` | character | Choice the evidence informs. |
| `reader_task` | character | Compare, lookup, relationship, distribution, time, composition, flow, geography, monitor, or verify evidence. |
| `data_shape` | character | Grain and structural requirement. |
| `precision_need` | character | Pattern, exactness, range, or other required judgment. |
| `context_required` | character | Denominator, uncertainty, period, missingness, or other material context. |
| `source_url` | character | Complete public source URL. |
| `reference_choice` | character | Defensible starting selection, including one no-display case. |
| `required_companion` | character | Table, note, second view, or other necessary support. |
| `no_display_trigger` | character | Evidence failure that blocks the display. |
| `build_mode` | character | Two `build`, one `table`, and seven `decision-only` cases. |

## Case inventory

| ID | Reader task | Reference choice | Source |
|---|---|---|---|
| C01 | Compare | Aligned dot plot | CMS HCAHPS |
| C02 | Lookup | Table | CMS HCAHPS |
| C03 | Relationship | Scatterplot | CMS HCAHPS |
| C04 | Distribution | Distribution view with subgroup comparison | Synthea or approved encounter release |
| C05 | Time | Line or run chart with process context | CMS timely care |
| C06 | Composition | Ordered composition view with counts | CDC WONDER |
| C07 | Flow | Flow view plus transition table | Synthea |
| C08 | Geography | Map plus aligned comparison | CDC PLACES and later context sources |
| C09 | Monitor | Coordinated comparison and table | CMS hospitals |
| C10 | Verify evidence | No display; request adequate evidence | CMS HCAHPS evidence-gap scenario |

## Shared HCAHPS source

- Path: `../01-encoding-grammar/data/hcahps_ma_recommend_2026.csv`
- CMS release: 2026-08-13
- Coverage: 2024-10-01 through 2025-09-30
- Rows: 65
- Reported rows: 56
- SHA-256: `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74`
- Source record: `../01-encoding-grammar/source-record.yml`

Module 03 uses `recommend_percent`, `response_rate_percent`, `completed_surveys`, facility identity, value status, period, and release.

## Worked-view rules

### Comparison

Use the 15 reported hospitals with the most completed surveys. Break ties by facility ID. Sort the display by recommendation percentage. Show recommendation percentage through aligned position and direct labels. Preserve response rate and completed surveys in the companion table.

### Relationship

Use all 56 reported hospitals with finite recommendation, response-rate, and completed-survey values. Map response rate to x position, recommendation percent to y position, and completed surveys to area. Label the area legend and state that association does not establish cause.

### Lookup

Use the same 15-hospital set and export facility ID, name, recommendation percent, response rate, and completed surveys as a CSV table. Exact lookup does not require a chart.

## Validation contract

The validator checks:

1. exact schema;
2. 10 cases and ordered IDs;
3. unique case titles;
4. full reader-task coverage;
5. no blank fields;
6. complete HTTPS source URLs;
7. two build, one table, and seven decision-only cases;
8. exactly one no-display choice;
9. a material no-display trigger for every case;
10. the pinned HCAHPS release;
11. 56 reported HCAHPS rows; and
12. at least 50 complete relationship rows.

The current script reports 13 checks because structural elements are separated for useful failure messages.

## Limits

- Reference choices are starting decisions, not a universal chart taxonomy.
- Several cases specify data requirements but do not ship their future module extracts here.
- The HCAHPS worked views do not establish statistical difference, fairness, or causation.
- The 15-hospital set is selected for readability, not clinical comparability.
- C10 is intentionally under-supported and must remain a no-display case until its evidence gap is resolved.
