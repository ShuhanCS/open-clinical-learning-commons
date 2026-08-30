# FND-1 Module 06: Accessible charts and time-indexed data

This module turns the accepted Module 04 and 05 evidence into three accessible figures without changing a value, denominator, interval, or claim boundary. A data-quality review panel decides whether the figures are ready for the cumulative Week 6 checkpoint.

## Released evidence

- F01 compares accepted and deliberately defective missingness for eight fields.
- F02 shows six synthetic-cohort rates with the exact Module 05 Wilson intervals.
- F03 shows 374 selected indexes across 20 quarters without treating them as service volume or a tested trend.
- Every figure has a 300-DPI PNG, SVG, exact CSV, structured text alternative, and registry record.
- Color is reinforced by hatches, markers, line styles, direct labels, or an exact table.

The reference disposition is `accept with conditions`. The conditions are exact-table linkage, equivalent text, N01 through N08, unadjusted descriptive language, selected-cohort time wording, and synthetic-data scope.

## Render

The renderer requires Matplotlib 3.10.9 and Pillow 11.1.0. It verifies all four input fingerprints and refuses an existing target.

```powershell
python render_figures.py --target <new-output-directory>
```

## Validate

```powershell
python validate_figures.py .
python validate_figures.py <module-06-submission> --submission
```

## Learning route

1. Verify all four upstream fingerprints and read `figure-spec.md`.
2. Trace every displayed mark to an exact table field.
3. Check zero baselines, units, labels, and the Module 05 interval definition.
4. Test all figures in grayscale, at 50-percent width, and at 200-percent zoom.
5. Read each text alternative without viewing its figure.
6. Reconcile F03 totals to 374 selected indexes.
7. Record reproduction, accessibility, AI use, and an allowed disposition.
8. Hand the exact package to the Week 6 checkpoint without retyping values.

## Boundaries

- Do not treat accepted structural missingness as error.
- Do not sum overlapping rate rows or add significance marks.
- Do not add uncertainty to F01 or F03.
- Do not call the quarter sequence hospital volume, a trend, a forecast, or a cause.
- Do not substitute workplace or patient data.
- Do not use color as the only carrier of meaning.

Module version: 0.1.0. Commons release: 0.34.0.
