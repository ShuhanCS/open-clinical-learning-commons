# Module 07 instructor notes

## Teaching purpose

This module separates accessibility from taste. Learners work on one fixed clinical and statistical case. A successful repair changes the access path, not the source values or conclusion.

## Preparation

Before class:

1. run `python validate_accessibility_case.py`;
2. run `Rscript lab.R`;
3. run `Rscript critique_charts.R`;
4. open every PNG at 100 percent zoom;
5. print or export the first two figures in grayscale;
6. inspect the CSV with a table reader;
7. read the short and long text alternatives aloud;
8. confirm that the full URLs in `source-record.yml` still resolve.

Do not present the reference palette as a universal clinical palette. It is one tested encoding on a white background for this case.

## Reproducible answer facts

| Quantity | Answer |
|---|---:|
| Rows | 65 |
| Columns | 27 |
| Reported | 53 |
| No different from national | 52 |
| Worse than national | 1 |
| Too few | 2 |
| Not available | 10 |
| National rate | 21.3 |
| Reported score range | 19.7 to 25.2 |
| Reported denominator range | 30 to 2,088 |
| Minimum defined contrast on white | 5.54:1 |
| Maximum defined contrast on white | 18.88:1 |
| Validation checks | 66 |
| Release SHA-256 | `b58168d9002a3e489213b0fafde1eca76f5b1a426c71ea3d61551671d76a49c2` |

## Concept key

### Use of color

Color may reinforce a distinction. It may not be the only means of identifying comparison status. In the reference figure, the one worse row is both a red triangle and a row that can be identified by its direct status cue. The no-different rows are blue circles. The grayscale version adds a W or N prefix.

Changing red to a color-blind-safe red is not enough if every status still uses the same shape and the legend is the only decoder.

### Contrast

Expected thresholds from WCAG 2.2 for this lesson:

- 4.5:1 for normal text and images of normal text;
- 3:1 for large text;
- 3:1 for required graphical objects against adjacent colors.

The module defines five foreground colors with at least 5.54:1 contrast on white. Learners still need to test the exported chart. Thin lines, transparency, adjacent colored regions, gray backgrounds, antialiasing, and printing can make a numerically acceptable palette hard to read.

### Short and long descriptions

Short text identifies the image and the main finding. It should not narrate every mark.

The long description provides the structure and essential information a reader needs to reach the same interpretation. For this chart, that includes:

- 65 total hospital rows;
- 53 reported scores and source intervals;
- a 21.3 national reference;
- 52 no-different and 1 worse classifications;
- 2 too-few and 10 not-available rows;
- the 19.7 to 25.2 reported range;
- the source and period;
- the pairwise-test and causal boundaries;
- a path to the exact-value table.

The long description should not turn 65 rows into one unstructured paragraph. Use headings and a table when structure matters.

### Alternate version

The CSV is a downloadable data alternative. In a web or document setting, learners also need a semantic table or another accessible presentation. A download link alone may not meet the immediate reading task.

## Lab walkthrough

### Figure 1: color plus shape

Ask learners to cover the legend. Can they still identify the exceptional row? Then remove color or view the image in grayscale. The triangle still differs, but the distinction becomes much easier when direct text or the W cue is available.

### Figure 2: grayscale redundant encoding

The claim remains unchanged. The worse row is a triangle with a W prefix. The no-different rows are circles with N prefixes. The national reference and intervals remain visible.

### Figure 3: reporting status

The bar chart uses one dark gray. Direct labels and counts carry the meaning. It shows why unavailable rows need a visible access path even when they have no position on the score axis.

### Figure 4: cue key

The key includes better, no different, worse, too few, and not available. The Massachusetts data contain no better row. Including the reusable cue does not create a better observation in the case.

## Critique key

### C1: red and green color only

Expected defects:

- color alone carries status;
- red and green are difficult for some readers to distinguish;
- every point has the same shape;
- the legend requires repeated eye travel;
- the chart hides the interval and benchmark;
- hospital status is not available in text.

Acceptable repairs include shape plus color, a W or N prefix, direct labels, faceting by status, or a status column in the adjacent table. The source categories must not change.

### C2: low-contrast heatmap

Expected defects:

- pale tiles have weak contrast;
- color alone carries value;
- three measures are separately normalized without explaining the scales;
- exact values and units are absent;
- the low and high directions differ across measures;
- the chart suggests a common quantity that does not exist.

The best repair may be deletion. A labeled table or aligned plots can make score, interval width, and denominator easier to compare without pretending they share one scale.

## Submission review order

Review in this order:

1. source fidelity;
2. non-color status cue;
3. grayscale output;
4. contrast record;
5. exact table and missingness;
6. short and long text;
7. decision note;
8. reproducibility;
9. AI-use record.

Stop and return the package if source values changed. Accessibility cannot compensate for a false result.

## Acceptable decision language

An acceptable conclusion is:

> The accessible display preserves one CMS worse-than-national classification and 52 no-different classifications among the 53 reported Massachusetts rows. The committee should review the source-classified worse row and keep the other hospitals in routine monitoring while treating the 12 unavailable or too-few rows as missing evidence, not zero performance.

Other conclusions may pass when they preserve the comparison and causal boundaries.

## Claims that do not pass

- "The red hospital is the worst hospital."
- "Every overlapping interval proves the hospitals are the same."
- "The accessible palette proves WCAG compliance."
- "Too few cases means a rate of zero."
- "A green symbol means better care."
- "The chart proves which hospital caused more readmissions."

## Accessibility review

Technical checks cannot certify the finished submission. A named accessibility reviewer should inspect:

- screen and grayscale exports;
- projected and printed legibility;
- final contrast and adjacent colors;
- direct labels and legend dependence;
- short alt text;
- structured long description;
- table headers, caption, and reading order;
- the smaller viewing context;
- the learner's recorded test evidence.

## Handoff to Module 08

Accessibility becomes a standing requirement. Module 08 adds time and process variation. Learners must carry forward contrast, redundant encoding, text alternatives, exact values, and unavailable-status handling while deciding whether a time pattern is signal or ordinary variation.

## Human release gates

The module still needs named reviews for:

- accessibility and assistive-technology use;
- clinical quality interpretation;
- statistical and CMS source fidelity;
- visualization teaching quality;
- independent teachability on a clean system.
