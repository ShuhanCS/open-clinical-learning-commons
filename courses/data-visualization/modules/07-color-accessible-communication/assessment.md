# Module 07 assessment

## Decision prompt

You are preparing the Massachusetts heart failure readmission display for a clinical quality committee. Committee members will use a projected screen, printed packet, grayscale office printer, and assistive technology. Some will read the display quickly during a meeting. Others will review exact values later.

Revise the Module 06 display so every reader can recover the same source-supported finding without relying on color alone.

## Source boundary

Use `data/accessibility_hf_readmission_2026.csv` or rebuild it from the pinned Module 06 table. Do not import patient records, reconstruct missing CMS values, replace the source intervals, or create a new performance category.

The final display must preserve:

- all 65 hospital rows across the figure and table;
- all 53 reported scores and source intervals;
- the 21.3 national reference;
- the 52 no-different and 1 worse source categories;
- the 2 too-few and 10 not-available rows;
- the measure ID, reporting period, source release, and attribution;
- the boundary that pairwise hospital difference is not tested.

## Part 1: standards reading

Read the assigned W3C and CDC pages. In `accessibility-audit.md`, answer:

1. Which information in the draft is carried by hue?
2. What non-color cue will carry the same meaning?
3. Which text and graphical objects need contrast checks in the final delivery context?
4. What belongs in short alt text, the long description, and the exact-value table?
5. Which user tasks still require a compliant alternate version even if the chart is visually legible?

Do not write that a chart is "WCAG certified." Name the checks you performed and their scope.

## Part 2: run the reference lab

Run:

```powershell
Rscript lab.R
```

Inspect the four reference figures, CSV, and text alternative. Record:

- which status cues survive grayscale;
- which exact values are available only in the table;
- how unavailable rows remain visible;
- whether the short text identifies the chart and main finding;
- whether the long description preserves structure, values, uncertainty, and limits.

## Part 3: critique and repair

Run:

```powershell
Rscript critique_charts.R
```

For each flawed display, submit:

1. the expected reader task;
2. the accessibility barrier;
3. the likely interpretation error;
4. the repair;
5. the evidence that the repair worked;
6. one remaining limit.

### C1: red and green carry status alone

Identify why hue, identical point shapes, and an indirect legend make the status fragile. Repair the chart with at least two redundant cues. Keep the source comparison categories unchanged.

### C2: pale heatmap

Identify why low contrast, separately normalized columns, missing values, and missing units block comparison. Decide whether the repair should be a labeled heatmap, a small table, separate aligned plots, or no heatmap.

## Part 4: independent accessible display

Create one final static figure for the committee. The figure may adapt the reference caterpillar plot or use another defensible form.

`figure.png` must:

- show reported point estimates and CMS lower and higher estimates;
- label the 21.3 national reference directly;
- preserve the CMS comparison category;
- use color only with shape, text, line type, direct labels, or another non-color cue;
- use foreground and background combinations that pass the recorded contrast test;
- remain understandable in grayscale;
- name the measure and reporting period;
- state that the endpoints come from CMS and pairwise hospital difference is not tested;
- point to the exact-value table and long description;
- avoid a title that calls every high point a poor performer.

The final figure does not have to place all 65 facility names on one page if that harms reading. If labels move to the table, the figure and table need a stable shared identifier and a clear reading path.

## Part 5: exact-value alternative

`data-table.csv` must include one row for every hospital and these columns:

```text
reading_order
facility_id
facility_name
score
lower_estimate
higher_estimate
denominator
display_label
display_symbol
start_date
end_date
footnote_text
short_alt_row
```

Blank source values remain blank. The CSV is the downloadable data alternative. In a website or document submission, also present it as a semantic table with a caption, column headers, and a predictable reading order.

## Part 6: text alternative

`alt-text.md` contains:

```markdown
# Text alternative

## Short alternative

## Long description

### Purpose and structure

### Main finding

### Values and uncertainty

### Missing and unavailable results

### Decision boundary

### Exact-value table
```

The short alternative identifies the chart and main finding in one or two sentences. It points to the long description when the image location allows it.

The long description explains the chart structure, national reference, reported range, comparison counts, missing statuses, source intervals, and decision boundary. It does not recite decorative details or all 65 rows. Link or point to `data-table.csv` for exact values.

## Part 7: accessibility audit

`accessibility-audit.md` contains:

```markdown
# Accessibility audit

## Audience, context, and user tasks

## Information carried by color

## Contrast calculations

## Redundant cues

## Color, grayscale, print, and small-view checks

## Text alternative and table

## Repairs made

## Remaining risks and human review
```

For each contrast calculation, record foreground, background, ratio, object or text use, threshold, and result. A palette name or color-blind simulator screenshot does not replace the calculation.

For each viewing check, record the tool or method, output or screenshot location, defect found, repair, and final result.

## Part 8: decision note

`decision-note.md` contains:

```markdown
# Decision note

## Reader

## Finding

## Action

## Access path

## Uncertainty

## Evidence needed next
```

The action should support focused review or monitoring. It may not call for punishment, causal attribution, or a pairwise hospital conclusion.

## Exact submission

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

An approved alternative tool may replace `analysis.R` with an editable source file that regenerates the figure and table. Manual edits made only to the exported PNG do not meet the requirement.

## Rubric

| Criterion | Weight | Full-credit evidence |
|---|---:|---|
| Source fidelity and interpretation | 15% | The figure and table preserve all source values, statuses, dates, benchmark, and claim boundaries. |
| Color and contrast | 15% | The audit records correct ratios and tests the final background, marks, text, and delivery context. |
| Redundant encoding and grayscale | 15% | Status survives without hue through clear shape, text, line, position, or direct-label cues. |
| Figure design and time-pressured reading | 15% | A clinical reader can find the benchmark, status, uncertainty, and next step quickly. |
| Text alternative and exact table | 15% | Short text identifies the purpose and finding; the structured long description and complete table preserve equivalent information. |
| Critique and repair | 10% | Both flawed displays are diagnosed as reader problems and repaired without changing the evidence. |
| Reproducibility | 10% | The editable analysis regenerates the final figure and table from the released data. |
| Decision note and AI accountability | 5% | The action fits the evidence, and AI use or non-use is recorded with human verification. |

Passing requires at least 80 percent overall and every pass condition below.

## Noncompensable pass conditions

- Color is not the only status cue.
- Required text and graphical objects meet their recorded contrast thresholds in the final context.
- The grayscale check preserves status and the main finding.
- Every hospital remains in the figure, exact table, or linked alternate path.
- The table contains 65 rows and keeps unavailable scores blank.
- The short alternative, long description, and exact table are all present.
- Source scores, intervals, national rate, statuses, dates, and footnotes are not changed.
- The recommendation does not claim pairwise significance, equivalence, or causation.
- The analysis is editable and reproducible.
- No restricted patient or partner data are included.
- `ai-use.md` is complete, including when no AI was used.
