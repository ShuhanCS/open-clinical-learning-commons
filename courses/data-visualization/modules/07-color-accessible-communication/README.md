# Module 07: Color and accessible visual communication

This module asks a clinical quality analyst to make the Module 06 heart failure readmission display usable on screen, in print, in grayscale, and with assistive technology. The statistical claim stays fixed. Learners change how readers reach it.

## Decision

Can every committee member identify the CMS comparison status, exact values, unavailable rows, and main finding without relying on color alone?

The case contains the same 65 Massachusetts hospital rows used in Module 06. Fifty-three have reported estimates. CMS classifies 52 as no different from the national rate and one as worse. Two rows have too few cases and ten are not available.

## Learning outcomes

After this module, a learner can:

- choose sequential, diverging, and qualitative color only when the data structure calls for it;
- calculate and interpret contrast against the final background;
- pair color with shape, text, line type, position, or direct labels;
- test a display in color, grayscale, print, and a smaller viewing context;
- write short alt text and a structured long description for a complex chart;
- provide an exact-value table and CSV download;
- keep source uncertainty and unavailable values intact during an accessibility repair.

## Standards and source case

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Understanding use of color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
- Understanding contrast minimum: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum
- Understanding non-text contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
- W3C complex images tutorial: https://www.w3.org/WAI/tutorials/images/complex/
- CDC COVE Section 508 accessibility: https://www.cdc.gov/cove/about/section-508-accessibility.html
- CMS hospital source: https://data.cms.gov/provider-data/dataset/632h-zaca

WCAG requires color not to be the only visual means of carrying information. Normal text needs at least 4.5:1 contrast, large text at least 3:1, and required graphical objects at least 3:1 against adjacent colors. This module's five foreground cue colors use a stricter 4.5:1 floor on white, then add text and shape.

## Files

```text
07-color-accessible-communication/
  README.md
  assessment.md
  build_accessibility_case.py
  critique_charts.R
  data-spec.md
  instructor-notes.md
  lab.R
  release.json
  source-record.yml
  validate_accessibility_case.py
  data/
    accessibility_hf_readmission_2026.csv
```

## Build the teaching table

Python's standard library is enough:

```powershell
python build_accessibility_case.py
```

The build reads the pinned Module 06 Massachusetts table, verifies its SHA-256 checksum, preserves every source value, adds redundant display cues, calculates contrast, and writes a deterministic 65-row release.

## Validate the data

```powershell
python validate_accessibility_case.py
```

The validator checks 66 source-preservation, status, order, missingness, contrast, encoding, and text-alternative conditions.

## Run the lab

Requirements:

- R 4.x
- ggplot2

```powershell
Rscript lab.R
```

Optional paths:

```powershell
Rscript lab.R --data data/accessibility_hf_readmission_2026.csv --output output
```

The lab creates:

```text
output/
  01-color-plus-shape.png
  02-grayscale-redundant.png
  03-reporting-status-with-counts.png
  04-contrast-and-cue-key.png
  accessible_hf_readmission_table.csv
  alt-text-reference.md
```

## Run the critique set

```powershell
Rscript critique_charts.R
```

The critique set creates two deliberately inaccessible figures:

```text
critique-output/
  C1-red-green-color-only.png
  C2-low-contrast-heatmap.png
```

The first uses red and green as the only status cue. The second uses pale color alone for three separately scaled quantities while hiding values and units. Learners repair both before completing the independent submission.

## Measured teaching facts

| Quantity | Result |
|---|---:|
| Total hospital rows | 65 |
| Reported estimates | 53 |
| No different from national | 52 |
| Worse than national | 1 |
| Too few cases | 2 |
| Not available | 10 |
| Foreground cue colors defined | 5 |
| Lowest cue contrast on white | 5.54:1 |
| Highest cue contrast on white | 18.88:1 |
| Data validation checks | 66 |

The palette includes a better-than-national cue even though the Massachusetts case has no row in that category. The cue supports reuse without inventing a better result in this dataset.

## Learner submission

```text
module-07/
  accessibility-audit.md
  analysis.R
  figure.png
  data-table.csv
  alt-text.md
  decision-note.md
  ai-use.md
```

See [assessment.md](assessment.md) for the exact prompt and rubric. See [instructor-notes.md](instructor-notes.md) for the answer key and facilitation notes.

## Interpretation boundary

Accessibility does not change the source measure. Keep the CMS point estimates, lower and higher estimates, national rate, reporting period, comparison categories, denominators, and unavailable status. Do not replace the source intervals, turn interval overlap into a pairwise test, or call a hospital better or worse because of a palette choice.

## Status

This package is a runnable release candidate. Technical checks are complete when `release.json` says so. Accessibility, clinical quality, statistical interpretation, visualization, and independent-teachability reviews remain human gates.
