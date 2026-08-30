# Descriptive data specification

## Inputs

`resolved-analytic-table.csv` is the immutable Module 04 release: 374 synthetic people, 29 fields, one row per person, SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.

`quality-rule-results.csv` contributes eight retained conditions. Every registered output that touches optionality, supported extremes, or small cells names the applicable N-rule.

## Calculation contract

- Counts are integers.
- Percentages and numeric summaries use six decimal places.
- Standard deviations are sample standard deviations.
- Q1 and Q3 use inclusive linear interpolation.
- Category values are retained and ordered deterministically.
- Cross-tab percentages use the named row denominator.
- Wilson intervals use z = 1.959963984540054.
- Calculations use unrounded values.
- No blank is changed to zero or a clinical state.

## Output grain

| File | Rows | Grain |
|---|---:|---|
| variable-profile.csv | 17 | one registered field |
| cross-tabs.csv | 12 | one row-category by endpoint cell |
| rates.csv | 6 | one registered proportion |
| stratified-table.csv | 2 | one index-class stratum |
| denominator-registry.csv | 27 | one result family |
| descriptive-checks.csv | 18 | one release invariant |

`denominator-registry.csv` is the meaning contract. A result is incomplete without its numerator definition, denominator definition and count, missing-value rule, time window, unit, interpretation limit, and retained conditions.

## Handoff

Module 06 may select and display released rows. It may not silently recalculate a number, change a label, omit the exact table, or weaken the interpretation limit.
