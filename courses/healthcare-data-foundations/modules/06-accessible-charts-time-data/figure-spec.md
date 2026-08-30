# Figure contract

All figures use a 7 by 4 inch canvas, PNG at 300 DPI, SVG, sans-serif text of at least 8 points, sentence-case labels, explicit units, and the Okabe-Ito blue `#0072B2`, orange `#E69F00`, and black `#000000`. Bars begin at zero. Each figure has an exact CSV and structured text alternative. No figure uses 3D, gradients, shadows, decorative marks, or color alone.

## F01: Quality and missingness

- Question: Which fields have accepted structural missingness or seeded missingness that required restoration?
- Table: `tables/quality-missingness.csv`.
- Files: `figures/quality-missingness.png`, `.svg`, and `alt-text/quality-missingness.md`.
- Mark: grouped horizontal bars from zero.
- Cue: blue diagonal hatch for 374 accepted rows; orange cross hatch for the 379-row defective teaching layer; direct percent labels.
- Fields: death date, gender, index encounter ID, index reason code, index reason description, and three next-encounter companion fields.
- Uncertainty: none supported.
- Caption boundary: defective counts are deterministic teaching defects; accepted optional missingness is not automatically error.

## F02: Descriptive rates

- Question: What selected 30-day and 90-day events are recorded for the synthetic cohort?
- Table: `tables/descriptive-rates.csv`.
- Files: `figures/descriptive-rates.png`, `.svg`, and `alt-text/descriptive-rates.md`.
- Mark: horizontal points and intervals on a zero-based percent scale.
- Cue: a common blue line and circle plus direct numerator/denominator labels.
- Uncertainty: the exact Module 05 Wilson 95-percent interval; no significance mark or real-population claim.
- Caption boundary: RT01 contains RT02 through RT04, and rows across windows are not all mutually exclusive.

## F03: Quarterly selected index counts

- Question: How are the 374 selected index encounters distributed across calendar quarters in the pinned synthetic cohort?
- Table: `tables/quarterly-index-counts.csv`.
- Files: `figures/quarterly-index-counts.png`, `.svg`, and `alt-text/quarterly-index-counts.md`.
- Mark: three lines on a zero-based count axis from 2015 Q1 through 2019 Q4.
- Cue: total uses black solid circles, emergency uses blue dashed squares, and inpatient uses orange dotted triangles.
- Uncertainty: none supported.
- Caption boundary: one index per person means these are not hospital volumes, rates, forecasts, causes, process limits, or evidence of demand change.

## Text alternative order

Each alternative states purpose, structure, axes and units, series and redundant cues, exact high and low values, main pattern, uncertainty meaning when present, source and period, exact-table path, and the material interpretation limit.
