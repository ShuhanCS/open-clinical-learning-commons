# Cohort specification

## Decision and grain

Build one row for each included synthetic adult patient at the first qualifying acute encounter. The senior clinical data analyst decides whether the cohort is technically ready for Module 04.

## Source population

All 1,171 patients in the accepted Module 02 database.

## Qualifying event

An event qualifies when all of these rules hold:

1. `encounterclass` is `emergency` or `inpatient`.
2. Encounter start is on or after `2015-01-01T00:00:00Z` and before `2020-01-01T00:00:00Z`.
3. The patient is at least 18 completed years old at encounter start.

Completed age uses the difference in years minus one when the event month and day precede the birth month and day.

## Index event and time zero

Within each patient, order adult eligible events by encounter start ascending and encounter ID ascending. Select rank 1. The encounter ID is the deterministic tie-breaker.

Index start is time zero for pre-index history. Index stop begins post-index follow-up.

## Exclusion order and conservation

| Step | Starting | Excluded | Remaining | Rule |
|---:|---:|---:|---:|---|
| 1 | 1,171 | 0 | 1,171 | All source patients. |
| 2 | 1,171 | 690 | 481 | Has emergency or inpatient encounter in the index period. |
| 3 | 481 | 107 | 374 | Has at least one qualifying event at age 18 or older. |
| 4 | 374 | 0 | 374 | Select first eligible event per patient. |

The final conservation equation is `690 + 107 + 374 = 1,171`.

## Lookback

The 365-day window begins 365 elapsed days before index start and ends immediately before index start. Count all encounters, acute encounters, condition rows, and medication rows separately. Separate aggregation prevents join multiplication. The index event and all later events are excluded.

## Follow-up

The 30-day next state is the first different encounter that starts after index stop and at most 30 elapsed days later. Ties use encounter ID.

| Encounter class | State |
|---|---|
| ambulatory, outpatient, wellness | Scheduled care |
| urgentcare | Urgent care |
| emergency, inpatient | Acute return |
| no qualifying record | No encounter recorded |

The 90-day acute-return flag detects any emergency or inpatient encounter starting after index stop and at most 90 days later. The death flag uses the synthetic death date in the same open-left, closed-right window. `endpoint_90d` gives death precedence, then acute return, then no acute return recorded.

## Interpretation boundary

The released SQL reproducibly selects 374 adults from this synthetic archive. It does not estimate utilization, death, quality, access, or treatment effects in a real population.
