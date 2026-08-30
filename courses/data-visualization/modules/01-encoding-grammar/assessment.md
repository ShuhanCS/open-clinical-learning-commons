# Module 01 assessment

## Task

Prepare one reproducible comparison for a Massachusetts hospital patient-experience director. The director needs to choose two results for deeper qualitative review, not declare winners and losers.

Use the committed HCAHPS teaching extract. You may use the worked 15-hospital view or define another transparent subset of at least 10 reported hospitals. If you change the subset, state the rule before viewing the results and keep every source field needed to reproduce it.

## Exact submission package

Submit these six files in a folder named `module-01`:

```text
module-01/
  encoding-map.md
  analysis.R
  figure.png
  source-record.yml
  alt-text.md
  decision-note.md
```

Do not submit only a screenshot or a link to a proprietary workspace.

## File contracts

### `encoding-map.md`

Include one row for every variable or reference statistic visible in the figure.

| Required field | What to write |
|---|---|
| Variable or statistic | The exact field or derived value. |
| Data role | Nominal, ordered, quantitative, temporal, annotation, or provenance. |
| Mark or layer | Point, line, bar, text, reference line, caption, or another exact choice. |
| Channel | X position, y position, length, color, shape, size, text, or not encoded. |
| Reason | How the mapping serves the director's comparison. |

End with a short grammar trace that names the data, mapping, marks, scale, coordinates, labels, and layers.

### `analysis.R`

The script must:

1. read `hcahps_ma_recommend_2026.csv` from a relative path;
2. preserve facility ID as a nominal identifier;
3. apply the stated subset rule;
4. stop with a useful error if required fields are missing;
5. build the submitted chart;
6. save `figure.png`; and
7. run without manual editing after the files are placed in the documented layout.

### `figure.png`

The figure must show:

- the hospital comparison on an aligned position or common-baseline length scale;
- the exact measure and percent unit;
- readable facility labels;
- the CMS source, release date, and measurement period;
- any subset or reference rule the reader needs; and
- a title that states the comparison rather than a generic chart type.

Color may support the display, but it cannot be the only carrier of an ordered result or a required category.

### `source-record.yml`

Copy the module source record and add:

- your subset rule;
- row count used in the figure;
- any recoding, sorting, derived statistic, or exclusion;
- the SHA-256 checksum of the exact input file; and
- the date you ran the analysis.

Do not remove the publisher, full URLs, release, period, rights, missingness, or interpretation limits.

### `alt-text.md`

Write 80 to 150 words that state:

1. the chart type and population;
2. the measure and period;
3. the main comparison pattern;
4. the highest and lowest displayed results or another decision-relevant range;
5. the meaning of any reference mark; and
6. the limit that the chart does not establish causes or overall quality.

Do not list all labels if the visible table or surrounding text already provides them.

### `decision-note.md`

Use these headings:

```markdown
# Decision note

## Audience and decision
## Two results for follow-up
## Why these encodings fit
## What the display cannot establish
## Reproducibility check
## AI assistance disclosure
```

The note must name two results for deeper review and one follow-up question for each. A low or high plotted value alone is not an explanation.

## Assessment items by difficulty

### Foundation

1. Classify `facility_name`, `recommend_percent`, `completed_surveys`, and `period_end` by data role.
2. Identify the mark and every visible channel in your figure.
3. Point to one element that is annotation or provenance rather than a data encoding.

### Applied

4. Explain why aligned position or length is preferable to unordered hue for the percentage comparison.
5. Explain what would happen if completed survey count controlled point area.
6. State whether the 15-hospital selection creates a valid peer group and defend the answer.

### Transfer

7. Describe how the encoding map would change if the decision shifted from comparing hospitals to monitoring one hospital over eight quarters.
8. Name one new variable you would need before making a stronger comparison claim.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Source and provenance | 15 | Exact CMS source, release, period, checksum, subset, transformations, missingness, and limits are retained. |
| Encoding map | 20 | Every visible variable and reference is classified and mapped correctly; the grammar trace is complete. |
| Reproducible analysis | 20 | Relative paths, input checks, deterministic subset, and figure export run without manual repair. |
| Figure | 20 | The chart supports the named comparison with aligned position or length, readable labels, units, context, and no misleading channel. |
| Decision note | 15 | Two follow-up results and questions are named; the claim stays within what the aggregate survey data support. |
| Accessibility and text alternative | 10 | Meaning is not color-dependent; text is readable; the alternative states the pattern, range, reference, and limit. |
| **Total** | **100** | |

## Pass conditions

A passing submission earns at least 75 points and meets all four non-negotiable conditions:

1. `analysis.R` runs and produces `figure.png`;
2. the main quantitative comparison uses aligned position or a common-baseline length;
3. the source, release, period, measure, and subset are accurately disclosed; and
4. the note does not claim that the chart proves causation, statistical difference, or overall hospital quality.

A submission that misses one non-negotiable condition is returned for correction even if its numerical score is 75 or higher.

## AI policy

AI assistance is allowed for syntax, debugging, critique, and alternative generation. Disclosure and verification are required. You are accountable for every submitted source claim, transformation, mapping, and conclusion.
