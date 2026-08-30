# Accessible schema description

## Database purpose

[REPLACE: explain the database decision and synthetic-data limit.]

## Table grains

| Table | One row represents | Primary or surrogate key | Main parent tables |
|---|---|---|---|
| patients | [REPLACE] | [REPLACE] | [REPLACE] |
| encounters | [REPLACE] | [REPLACE] | [REPLACE] |
| observations | [REPLACE] | [REPLACE] | [REPLACE] |
| [REPLACE: add all remaining source tables] | [REPLACE] | [REPLACE] | [REPLACE] |

## Relationship reading

[REPLACE: describe every relationship in `data-model.mmd` as text, including cardinality and optionality. State why some source tables use `source_row_number`.]

## Minimized views

[REPLACE: explain `v_patients_minimal`, `v_encounters_core`, and `v_observations_core`, including which identity-like or cost fields they avoid and why the full synthetic source tables remain available.]

## Known structural limits

[REPLACE: record source age, synthetic status, absent or optional encounter references, empty supplies table, code-system interpretation limits, and what Module 03 must define before cohort work.]
