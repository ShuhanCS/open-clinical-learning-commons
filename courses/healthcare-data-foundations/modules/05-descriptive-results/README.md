# FND-1 Module 05: Descriptive results

This module turns the accepted 374-person synthetic analytic table into exact descriptive evidence with a denominator contract. A clinical analytics reviewer decides whether Module 06 can use the results without changing their meaning.

## Released evidence

- 17 registered one-variable summaries.
- Two complete cross-tabs with 12 cells and row percentages.
- Six rates with numerators, denominators, time windows, and Wilson 95-percent intervals.
- Two unadjusted index-class stratum rows.
- 27 denominator records carrying Module 04 conditions N01 through N08.
- 18 passing machine-readable checks.

The reference disposition is `accept with conditions`. Results describe this synthetic teaching cohort only.

## Build

The builder uses only the Python standard library and refuses an existing target.

```powershell
python build_descriptive.py --source data/resolved-analytic-table.csv --quality-results data/quality-rule-results.csv --target <new-output-directory>
```

## Notebook

Open `notebooks/05-descriptive-results.ipynb` from this module folder. It verifies source grain, selected summaries, cross-tab conservation, rates, conditions, and the Module 06 handoff. The builder is the accessible non-notebook route.

## Validate

```powershell
python validate_descriptive.py .
python validate_descriptive.py <module-05-submission> --submission
```

## Learning route

1. Verify source and quality-results fingerprints.
2. Read `data-spec.md` and the denominator registry before interpreting output.
3. Compare mean and median for skewed count fields.
4. Reconcile every cross-tab row.
5. Trace each rate from event definition to denominator and time window.
6. Treat the stratum table as unadjusted description.
7. Cite result IDs in the interpretation memo.
8. Record reproduction, AI use, and the final disposition.

## Boundaries

- Do not recalculate the cohort or clean the accepted source.
- Do not fill structurally missing values with zero.
- Do not omit supported extremes or small internal cells.
- Do not add p-values, causal language, risk adjustment, or real-population inference.
- Module 06 must use the released CSV tables rather than retyped prose values.

Module version: 0.1.0. Commons release: 0.33.0.
