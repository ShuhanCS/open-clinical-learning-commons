# Module 01 instructor notes and answer key

## Teaching purpose

This module replaces software-menu thinking with a durable model: variables are represented by marks whose properties vary through visual channels. Learners should leave able to explain why a chart has its form, even when they have never used the authoring tool in front of them.

Do not turn the session into a survey-method lecture or a ggplot2 syntax tour. The HCAHPS case makes the decision real. The assessed knowledge is the mapping and its justification.

## Verified setup

From the module directory:

```powershell
Rscript validate_hcahps.R
Rscript lab.R
Rscript critique_charts.R
```

Technical reference environment:

- R 4.6.1
- ggplot2 4.0.3
- Windows

Expected validator result: 15 of 15 checks pass.

Expected release facts:

- 65 Massachusetts hospital rows
- 56 reported recommendation percentages
- 9 unavailable results with footnotes
- reported range of 42% to 93%
- measurement period 2024-10-01 through 2025-09-30
- CMS release date 2026-08-13
- worked peer set of 15 hospitals
- peer-set spread of 34 percentage points
- all-reported-hospital unweighted median of 70.5%

## Seven-hour teaching sequence

| Segment | Time | Instructor action | Learner evidence |
|---|---:|---|---|
| Source and decision opening | 30 min | Show the CMS row structure, unavailable values, and named director's question. | Learner states the unit of observation and decision. |
| Concept core | 30 min | Teach data roles, marks, channels, scales, coordinates, labels, and layers. | Learner annotates one familiar chart. |
| Worked HCAHPS build | 60 min | Move from a comparison table to the layered dot plot one choice at a time. | Learner completes the reference encoding map. |
| Tier 1 and Tier 2 lab | 90 min | Run, inspect, and modify the chart. Ask what changed after each edit. | Learner saves comparisons and short explanations. |
| Critique studio | 60 min | Use the two flawed charts without revealing their filenames first. | Learner diagnoses channel failure and proposes a repair. |
| Independent assessment | 120 min | Coach the question and source record, not the visual style. | Six-file submission package. |
| Peer check and revision | 30 min | Pair learners to test code, text alternatives, and decision limits. | Corrected package and verification note. |
| **Total** | **420 min** | | **7 hours** |

## Worked example answer key

### Correct grammar trace

- Data: one row per Massachusetts hospital for `H_RECMND_DY`, restricted to reported values and then to the 15 largest completed-survey counts.
- Mapping: hospital name to y position; recommendation percentage to x position; the percentage also to a direct text label.
- Marks: points for hospital results, segments from the reference to each result, one vertical reference line, and text labels.
- Scale: a bounded percentage axis displayed from 45% to 92% for the selected data. Values remain percentages; the caption and labels disclose the unit.
- Coordinates: Cartesian coordinates with a shared horizontal scale.
- Labels: decision-oriented title, subset and reference subtitle, named x axis, direct values, source, release, and measurement period.
- Layers: reference line first, comparison segments second, data points third, direct labels fourth.

### Why completed surveys are not point size in the reference

Completed surveys are important context, but sizing the point creates a second task and makes the recommendation percentage look like a weighted quantity. In Module 01, completed surveys define the transparent 15-row teaching view and remain in the table. A later module can decide whether volume, response rate, or uncertainty belongs in the display.

### Why the statewide median is a reference, not a target

The unweighted median helps readers orient themselves. It is not a CMS performance threshold, an expected value, or evidence of statistical difference. Learners should not call hospitals above it successful or hospitals below it failing.

## Critique answer key

### Chart 1: unordered color

Diagnosis:

- `recommend_percent` is ordered quantitative data.
- The chart maps it only to a set of qualitative hues.
- Hue does not provide a natural numerical order.
- Readers must repeatedly search the legend to recover exact values.
- Similar hues may also become indistinguishable for some readers or in grayscale.

Smallest repair: map the percentage to aligned x position. Keep color constant or reserve it for one small, meaningful nominal grouping. Direct labels may repeat exact values.

### Chart 2: area for precision

Diagnosis:

- The percentage controls circle area.
- Readers must compare two-dimensional areas to answer a close numerical question.
- The circles share a center line but do not place the result itself on an aligned quantitative position.
- Differences in the observed range appear smaller and are difficult to estimate.

Smallest repair: map the percentage to x position or common-baseline length. Use point size only if a second quantity is necessary and clearly labeled.

## Strong decision-note example

> For this first review, examine New England Baptist Hospital's 86% result and St Vincent Hospital's 52% result. The chart shows that they sit at opposite ends of the 15-hospital teaching view selected by completed survey count. It does not explain the gap. For New England Baptist, ask which patient-experience practices patients identify as most helpful and whether the pattern holds across services. For St Vincent, review item-level results, survey administration, response patterns, patient mix, and recent operational changes before choosing an intervention.

Accept other hospital choices when the learner uses the display accurately and asks a defensible follow-up question.

## Text-alternative example

> Layered dot plot comparing the percentage of patients who would definitely recommend the 15 Massachusetts hospitals with the most completed surveys in the CMS HCAHPS release dated August 13, 2026. Results cover October 2024 through September 2025. Values range from 52% at St Vincent Hospital to 86% at New England Baptist Hospital. A dashed vertical line marks the unweighted median of 70.5% across all 56 Massachusetts hospitals with reported values. Nine other hospitals have unavailable results and are not plotted. The display identifies results for follow-up but does not establish causes, statistical differences, or overall hospital quality.

## Common errors and interventions

| Error | What it reveals | Instructor response |
|---|---|---|
| Facility ID is treated as numeric | Storage type is confused with analytical role. | Ask what addition or averaging of two facility IDs would mean. |
| Percent is mapped only to hue | Data type was named but not connected to channel accuracy. | Ask learners to order three marks without the legend. |
| Point area carries the precise value | Visual prominence is confused with numerical readability. | Ask learners to estimate the 72% and 75% circles, then compare aligned points. |
| Completed surveys are described as patients represented | Survey completions are treated as the hospital population. | Restore the exact field name and discuss what is and is not counted. |
| Missing hospitals disappear without comment | Filtering is treated as neutral. | Require the 65, 56, and 9 counts in the source record or note. |
| The chart is called a hospital-quality ranking | The measure is stretched beyond its construct. | Return to the exact HCAHPS question and the named follow-up decision. |
| The statewide median is called a benchmark | A descriptive reference is treated as an external target. | Ask who set the target and where that rule appears in the source. |
| The chart is polished but the encoding map is incomplete | Style is substituting for reasoning. | Grade the map before visual aesthetics. |

## Grading guidance

Grade the reasoning before the styling. A plain bar or point display can earn full credit. A sophisticated chart fails if the learner cannot state the mapping or if the source claim is wrong.

For the 20 figure points:

- 8 points: quantitative result on aligned position or common-baseline length;
- 4 points: readable identity labels and percent unit;
- 4 points: source, release, period, subset, and reference context;
- 4 points: accessible and decision-oriented presentation.

For the 20 analysis points:

- 5 points: relative-path input and useful missing-column check;
- 5 points: deterministic, disclosed subset;
- 5 points: chart code matches the encoding map;
- 5 points: script writes the submitted PNG from a clean run.

## Accessibility check

At ordinary document size, verify:

1. hospital labels and values remain readable;
2. the main comparison survives grayscale;
3. no required meaning depends on color alone;
4. the title, unit, source, period, and subset are visible;
5. the text alternative states the main pattern and decision limit; and
6. the PNG is not used as the only place where source data can be recovered.

## If time is short

Keep the concept core, worked mapping, one critique chart, and independent six-file submission. Cut the second Tier 2 modification and shorten peer discussion. Do not cut source provenance, text alternatives, or the claim-boundary check.

## Optional extension

Ask learners to create a second encoding map for monitoring one hospital over eight quarters. They should identify time as the x variable, recommendation percentage as y position, and the hospital identity as context rather than a repeated category. Do not require time-series inference in this module.

## Review still required

Before alpha release, record review by:

- DA-730 visualization faculty;
- a clinician or patient-experience subject-matter reviewer;
- an accessibility reviewer; and
- an independent instructor who runs the package from a clean checkout.
