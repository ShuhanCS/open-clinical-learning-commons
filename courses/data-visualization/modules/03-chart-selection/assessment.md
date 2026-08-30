# Module 03 assessment

## Task

Complete all 10 question-to-display decisions, build the two HCAHPS chart cases, and defend why the exact lookup case is a table. Then prepare one executive recommendation that includes the necessary companion and a no-display gate.

## Exact submission package

```text
module-03/
  selection-matrix.md
  analysis.R
  figures/
    comparison.png
    relationship.png
    exact-lookup.csv
  source-record.yml
  alt-text.md
  decision-note.md
```

## File contracts

### `selection-matrix.md`

Include all 10 cases and these fields:

| Field | Required content |
|---|---|
| Decision and owner | Who acts and what choice is informed. |
| Reader task | Detect, identify, order, estimate, compare, lookup, follow, locate, or another precise task. |
| Data grain and shape | What one row represents and what structure is available. |
| Precision and context | Exactness plus denominator, uncertainty, period, missingness, or definition needs. |
| Candidate display | First plausible form. |
| Required companion | Table, note, second view, or none with reason. |
| Rejected alternative | One plausible choice and a concrete reason to reject it. |
| No-display trigger | Evidence failure that stops publication. |
| Final choice | Chart, table, coordinated pair, or no display. |
| Justification | Two to four decision-specific sentences. |

### `analysis.R`

The script must:

1. read the Module 01 HCAHPS extract through a relative path;
2. check required fields;
3. define the reported and 15-hospital subsets;
4. build the comparison and relationship figures;
5. export the exact-lookup table;
6. use source release and period in outputs; and
7. write the exact filenames under `figures/`.

### `figures/comparison.png`

Use aligned position or common-baseline length, direct or accessible exact values, readable hospital labels, and the required source context. The companion lookup table must carry response rate and completed surveys.

### `figures/relationship.png`

Use paired quantitative position for recommendation percent and response rate. If area carries completed surveys, label it and do not make it the primary comparison. State that association does not establish cause.

### `figures/exact-lookup.csv`

Include facility ID, hospital name, recommendation percent, response-rate percent, and completed surveys for the declared subset. This is the selected display for the exact lookup case.

### `source-record.yml`

Retain the module record and add analysis date, exact subset rule, row counts, transformations, output paths, and checksums. Do not remove public source URLs, release, period, rights, or limits.

### `alt-text.md`

Provide separate 80 to 150 word alternatives for `comparison.png` and `relationship.png`. For the CSV, provide a two-sentence introduction that names the columns and selection rule.

### `decision-note.md`

Use:

```markdown
# Decision note

## Executive team and decision
## Reader task
## Selected primary display
## Required companion
## Rejected alternative
## Failure and no-display test
## What the evidence cannot establish
## Reproducibility check
## AI assistance disclosure
```

## Assessment items

### Foundation

1. Explain why one quantitative field does not determine one chart type.
2. Distinguish a comparison task from exact lookup.
3. State the minimum evidence needed before drawing a time trend.

### Applied

4. Defend the table for C02.
5. Diagnose the one-form dashboard and name the fabricated relationship field.
6. Explain when two coordinated views are necessary rather than decorative.

### Transfer

7. A leader asks for a county map of raw admissions. Name the decision, missing denominator, companion, and no-display trigger.
8. A distribution question arrives with only a mean. State the correct next action and why no chart repair can recover the missing structure.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Ten-case selection matrix | 25 | Complete decision, task, grain, precision, context, candidate, companion, rejected alternative, failure gate, and choice. |
| Reproducible analysis | 20 | Relative paths, field checks, deterministic subsets, two PNGs, and exact CSV export. |
| Display-task fit | 20 | Comparison, relationship, and lookup forms each fit their distinct reader task. |
| Decision note | 15 | Executive recommendation, companion, rejected alternative, failure test, and bounded claim. |
| Source and provenance | 10 | Exact sources, release, period, transformations, outputs, rights, and checksums. |
| Accessibility and alternatives | 10 | Readable non-color-dependent figures, two complete alternatives, and accessible lookup file. |
| **Total** | **100** | |

## Pass conditions

A passing submission earns at least 75 points and meets all five conditions:

1. all 10 cases have a final choice and no-display trigger;
2. `analysis.R` creates the two figures and CSV;
3. the exact lookup case remains a table unless the reader task is explicitly changed;
4. the no-evidence case remains no display until its named gap is resolved; and
5. source, release, period, subset, and limits are accurate.

## AI policy

AI may suggest candidates and critiques. It may not invent missing data, denominators, periods, or evidence. The learner verifies every selection against the case, source, and output.
