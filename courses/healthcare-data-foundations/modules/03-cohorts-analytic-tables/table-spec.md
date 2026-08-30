# Analytic-table specification

## Grain and keys

`outputs/analytic-table.csv` has exactly one row per included synthetic patient and selected index encounter. `patient_id` and `index_encounter_id` are each unique and non-null.

## Field groups

- Source fields: birth date, death date, gender, race, and ethnicity.
- Index fields: age, selected encounter identifiers, timestamps, class, code, description, and optional reason.
- Pre-index fields: four separately aggregated 365-day counts.
- Post-index fields: first 30-day state and 90-day return, death, and endpoint fields.
- Metadata: source release and cohort-definition version.

The post-index fields are outcomes or follow-up descriptions. They must not be used as baseline predictors without a new analysis contract.

## Null rules

- Death date can be null.
- Index reason code and description can be null.
- Next-encounter ID, timestamp, and elapsed days are null exactly when `next_30d_state` is `No encounter recorded`.
- Keys, index timestamps, counts, flags, state, endpoint, and version fields cannot be null.

## Measured release facts

- Rows: 374.
- Fields: 29.
- Index class: 314 emergency and 60 inpatient.
- Next state: 263 no encounter recorded, 92 scheduled care, 4 urgent care, and 15 acute return.
- Acute return within 90 days: 36.
- Death within 90 days: 8.
- Endpoint: 8 death, 36 acute return, and 330 no acute return recorded.
- Complete 90-day source coverage: 374.

## History-count release facts

| Field | Minimum | Maximum | Sum |
|---|---:|---:|---:|
| prior_365d_encounter_count | 0 | 187 | 2,138 |
| prior_365d_acute_count | 0 | 13 | 113 |
| prior_365d_condition_count | 0 | 5 | 468 |
| prior_365d_medication_count | 0 | 185 | 1,007 |

These are row counts in the synthetic source, not counts of clinically unique problems or therapies.
