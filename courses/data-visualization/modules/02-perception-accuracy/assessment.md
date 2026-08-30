# Module 02 assessment

## Task

Recommend one display for a health-system quality committee comparing hospital HCAHPS recommendation results. Your recommendation must combine published graphical-perception evidence, your recorded classroom test, and the committee's exact reader task.

The final display may be a chart or a table. You must explain the error and effort it avoids.

## Exact submission package

Submit these six files in a folder named `module-02`:

```text
module-02/
  perception-test.md
  analysis.R
  selected-display.png
  source-record.yml
  alt-text.md
  decision-note.md
```

## File contracts

### `perception-test.md`

Use these headings:

```markdown
# Perception test

## Prediction
## Protocol and trial order
## Results
## Error and effort patterns
## Interpretation errors
## Limits of this classroom test
## Design change I would test next
```

Include:

- which response template you used;
- whether timing was standard or accommodated;
- a table with all 10 trial results;
- the five-row display summary from `perception-summary.csv`;
- one observation about correctness;
- one observation about absolute gap error;
- one observation about time or effort;
- one confusion that affected interpretation; and
- at least three reasons the results cannot establish a general population ranking.

### `analysis.R`

The script must:

1. read the shared Module 01 HCAHPS extract with a relative path;
2. check for the required fields;
3. define and disclose the hospital subset;
4. create the recommended display;
5. use channels that fit the committee's reader task;
6. save `selected-display.png`; and
7. run without manual repair from the documented layout.

You may include your scoring code or call `score_perception_test.R`, but the submitted display must regenerate independently of a saved workspace.

### `selected-display.png`

The display must:

- support the committee's named comparison or lookup task;
- make close quantitative differences readable without area or angle as the only evidence;
- state the HCAHPS measure and percentage-point unit;
- show the subset, CMS release, and measurement period;
- preserve readable hospital identity;
- remain interpretable without color; and
- avoid presenting the result as complete hospital quality.

### `source-record.yml`

Retain the module source record and add:

- the exact subset used in the final display;
- row count;
- transformations, ordering, reference values, and exclusions;
- Module 01 extract checksum;
- analysis date; and
- any learner response file used, labeled as an educational record that is not published.

### `alt-text.md`

Write 80 to 150 words that state:

1. the display type and hospital set;
2. the measure and period;
3. the main ordering or comparison;
4. the important range or gap;
5. how a reference or annotation should be read; and
6. the material claim limit.

### `decision-note.md`

Use these headings:

```markdown
# Decision note

## Committee and reader task
## Recommended display
## Published perception evidence
## What my classroom test added
## Error and effort avoided
## What the display cannot establish
## Reproducibility check
## AI assistance disclosure
```

Do not write that your 10 trials proved a universal chart ranking. Connect the published evidence and your observation without treating them as equivalent.

## Assessment items by difficulty

### Foundation

1. Name the elementary judgment used by each of the five display types.
2. Explain the difference between detecting the higher hospital and estimating the gap.
3. Calculate absolute gap error for a response of 8 points when the correct gap is 5.

### Applied

4. Explain why the table may be best for exact lookup even when aligned position is best for seeing an ordered pattern.
5. Diagnose the close-value pie critique and propose the smallest repair.
6. Explain why mapping `percent - 60` to circle radius exaggerates small differences.

### Transfer

7. The committee now needs to find one hospital in an alert state among 50 facilities. How does the reader task change, and what feature could support detection without replacing labels?
8. Name the minimum design changes required before this classroom exercise could support a stronger comparative claim about display performance.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Perception-test record | 20 | Complete 10-trial protocol, scored results, correctness, error, time, confusion, and limits. |
| Published evidence and reasoning | 15 | Accurate use of graphical-perception and attention evidence without turning the ranking into a universal law. |
| Reproducible analysis | 20 | Relative paths, input checks, transparent subset, matching code and output, clean figure export. |
| Selected display | 20 | Fits the committee's task, reduces avoidable error, preserves source context, and stays readable without color. |
| Decision note and claim boundary | 15 | Recommendation connects audience, evidence, observation, effort, and limits. |
| Accessibility and text alternative | 10 | Readable, non-color-dependent display and complete 80 to 150 word alternative. |
| **Total** | **100** | |

## Pass conditions

A passing submission earns at least 75 points and meets all five conditions:

1. all 10 trials are recorded or an approved accessibility accommodation is documented;
2. `analysis.R` runs and creates `selected-display.png`;
3. the selected display fits a named reader task;
4. source, measure, release, period, and subset are accurate; and
5. the note does not present the classroom test as generalizable research.

A missing condition requires correction regardless of numerical score.

## AI policy

AI assistance may help with code, critique, alternative designs, and prose. An AI system may not act as your test participant or invent timing, errors, confusion, or evidence. Disclose and verify all assistance.
