# Perception-task data specification

## Purpose

This module reuses the exact CMS HCAHPS teaching extract released with Module 01 and adds a 10-row task-design table. The task table creates repeatable classroom stimuli for aligned position, length, table lookup, angle, and area judgments.

No CMS data are copied into this module. The shared course package reads:

`../01-encoding-grammar/data/hcahps_ma_recommend_2026.csv`

That file remains the single teaching-extract source of truth.

## Build and validate

From the Module 02 directory:

```powershell
Rscript build_perception_tasks.R
Rscript validate_perception_tasks.R
```

The build script selects explicit facility pairs from the Module 01 extract. The validator checks all trial values and answers against that source.

## Upstream source

- Publisher: Centers for Medicare & Medicaid Services
- Dataset: Patient survey (HCAHPS) - Hospital
- Dataset identifier: `dgck-syfz`
- CMS release: 2026-08-13
- Measurement period: 2024-10-01 through 2025-09-30
- Module 01 extract rows: 65
- Module 01 extract SHA-256: `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74`
- Module 01 source record: `../01-encoding-grammar/source-record.yml`
- Landing page: https://data.cms.gov/provider-data/dataset/dgck-syfz

## Derived task file

- Path: `data/perception_tasks_2026.csv`
- Rows: 10
- Columns: 13
- SHA-256: `b792637411a00c67baa30d70688e5a9b8353cee8a2758251419e84c0c4c1cbe6`
- Builder: `build_perception_tasks.R`
- Validator: `validate_perception_tasks.R`

## Schema

| Column | Type | Rule |
|---|---|---|
| `trial_id` | character | Unique `T01` through `T10`. |
| `display` | character | `dot`, `bar`, `table`, `pie`, or `bubble`; exactly two of each. |
| `facility_a_id` | character | CMS facility ID assigned the masked alias Hospital A. |
| `facility_a_name` | character | CMS name retained for instructor debrief. |
| `facility_a_percent` | numeric | Reported recommendation percentage from Module 01. |
| `facility_b_id` | character | CMS facility ID assigned the masked alias Hospital B. |
| `facility_b_name` | character | CMS name retained for instructor debrief. |
| `facility_b_percent` | numeric | Reported recommendation percentage from Module 01. |
| `correct_alias` | character | `A` or `B`, derived from the two values. |
| `correct_hospital_id` | character | CMS ID of the higher value. |
| `correct_hospital_name` | character | CMS name of the higher value. |
| `correct_gap_points` | numeric | Absolute difference in percentage points. |
| `cms_release_date` | date text | Always `2026-08-13`. |

## Task design

| Trial | Display | A | B | Correct | Gap |
|---|---|---:|---:|---|---:|
| T01 | Dot | 71% | 75% | B | 4 points |
| T02 | Dot | 72% | 66% | A | 6 points |
| T03 | Bar | 68% | 73% | B | 5 points |
| T04 | Bar | 79% | 75% | A | 4 points |
| T05 | Table | 79% | 86% | B | 7 points |
| T06 | Table | 68% | 62% | A | 6 points |
| T07 | Pie | 66% | 72% | B | 6 points |
| T08 | Pie | 62% | 52% | A | 10 points |
| T09 | Bubble | 66% | 72% | B | 6 points |
| T10 | Bubble | 75% | 73% | A | 2 points |

The correct alias is balanced at five A and five B responses. Gaps range from 2 to 10 percentage points. Values are not identical across display conditions, so learners must not interpret between-display differences as isolated causal effects of the channel.

## Stimulus contract

`lab.R` creates:

- two dot plots with a 40% to 90% aligned scale;
- two horizontal bar charts with a 0% to 100% common baseline;
- two tables with exact values;
- two paired pie displays in which each hospital's result and other responses sum to 100%;
- two bubble displays with area proportional to the percentage;
- two reversed trial orders; and
- one instructor answer key.

Hospital names are masked as A and B during testing to reduce name-length and familiarity effects. The source identities remain in the task table for instructor debrief and provenance.

## Response schema

The response templates contain:

| Column | Rule |
|---|---|
| `order` | Presentation order from 1 through 10. |
| `trial_id` | Links the response to the task key. |
| `display` | Display condition copied for convenience. |
| `higher_response` | Learner enters `A` or `B`. |
| `estimated_gap_points` | Non-negative numeric estimate. |
| `seconds` | Positive elapsed seconds. |
| `confusion_note` | Optional short description. |

`score_perception_test.R` adds correctness, correct gap, and absolute gap error. It summarizes higher-value accuracy, mean absolute gap error, and median seconds by display.

## Validation contract

The validator checks:

1. exact task schema;
2. 10 ordered unique trial IDs;
3. two trials for every display;
4. five A and five B answers;
5. gaps from 2 to 10 points;
6. the pinned CMS release;
7. both facility values against the Module 01 extract;
8. derived answer aliases;
9. derived gaps; and
10. derived correct facility IDs.

The current release passes 12 reported checks because several contracts are checked separately for clearer failures.

## Rights and privacy

The upstream CMS public-reporting data are U.S. government works in the public domain. Attribution is appreciated and reuse must not imply federal endorsement. The task table contains no patient records, personal responses, or protected health information.

Learner response times and errors are educational records. Do not publish named results or use them for research without the appropriate consent, privacy, and institutional review process.

## Known limits

- Ten trials provide practice, not a stable estimate of an individual's perception.
- Display conditions use different value pairs and, for dots and bars, different axis ranges.
- Timing includes device, rendering, motor, language, and partner effects.
- Repeated exposure can create learning and memory effects.
- Tables change the operation from visual estimation to exact lookup and subtraction.
- The task does not represent the complexity, interruptions, or accessibility needs of a real quality-committee meeting.
