# Module 02: Perception and visual accuracy

- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module ID: `oclc-da730-02`
- Learner time: 8 hours
- Prerequisite: Module 01
- Release status: runnable release candidate
- Module version: 0.1.0

## The decision

A health-system quality committee needs to compare hospital patient-experience results. Several displays are technically correct, but they do not demand the same effort or support the same accuracy.

Your job is to choose the display the committee can read with the least avoidable error. Preference is not enough. You will connect published perception evidence, your own controlled practice trials, and the committee's task.

## Competency

Compare plausible encodings using evidence about perceptual accuracy and select the one the audience can read with the least avoidable error.

By the end of the module, you can:

1. distinguish visual detection, ordering, lookup, and quantitative estimation tasks;
2. explain why aligned position usually supports more accurate quantitative comparison than angle, area, volume, or color intensity;
3. measure response correctness, absolute estimation error, and completion time in a small classroom test;
4. diagnose clutter, search effort, and a misleading size transformation;
5. choose a display for a named audience and comparison task; and
6. state why your classroom observations are practice evidence rather than a generalizable experiment.

## Twenty-minute concept core

### 1. A reader must decode the chart

Encoding turns a value into position, length, angle, area, color, or another visible property. Perception is the reverse operation. A reader looks at the mark and estimates the value, order, difference, or pattern.

The chart is successful only if that decoding is accurate enough and fast enough for the decision.

### 2. Use an evidence-based starting order

For elementary quantitative judgments, a useful starting order is:

1. position on a common aligned scale;
2. position on nonaligned scales;
3. length;
4. angle or slope;
5. area;
6. volume; and
7. color intensity or saturation.

This is a design starting point, not a law. Exact results depend on the task, scale, number of marks, labels, device, audience, and interaction. A bar endpoint also has a position, a table can outperform a chart for exact lookup, and direct labels can change the task entirely.

### 3. Separate the reader's tasks

| Reader task | Example | Usually helpful |
|---|---|---|
| Detect | Find the one hospital with an alert state. | One salient, redundant feature with a clear legend or label. |
| Identify | Find a named hospital. | Readable labels, stable order, search structure. |
| Order | Put hospitals from low to high. | Aligned position or common-baseline length. |
| Estimate | Approximate a percentage or gap. | Aligned scale, useful ticks, direct values when exactness matters. |
| Compare | Judge which value is higher and by how much. | Shared position scale and low clutter. |
| Look up | Retrieve one exact value. | A table or direct label may be faster and more accurate than a chart. |

Do not ask which chart is best without naming the reader's task.

### 4. Preattentive does not mean effortless truth

A single distinct feature, such as one different hue or orientation, can stand out quickly in a simple field. That can help a reader find a mark. It does not make the encoded number accurate, explain why the mark matters, or replace accessible labeling.

Several simultaneous differences, crowded marks, weak contrast, and color-vision variation can remove the advantage. Use salient features sparingly and redundantly.

### 5. Audience effort is part of the design

Every legend lookup, scale change, distant label, decorative mark, and unnecessary category adds work. Some effort is justified when the structure is complex. Avoidable effort competes with the decision.

For the quality committee, the relevant question is not whether a pie chart is familiar. It is whether committee members can compare close hospital percentages accurately and explain the result without reconstruction.

## The classroom perception test

The package creates 10 trials from the pinned Module 01 HCAHPS extract:

| Display | Primary perceptual task | Trials |
|---|---|---:|
| Dot plot | Aligned position | 2 |
| Bar chart | Common-baseline length and endpoint position | 2 |
| Table | Exact lookup and subtraction | 2 |
| Two pies | Angle and area across separate baselines | 2 |
| Bubble comparison | Area | 2 |

Each trial asks:

1. Is Hospital A or Hospital B higher?
2. What is the estimated difference in percentage points?
3. How many seconds did the response take?
4. What caused confusion, if anything?

The pairs have correct gaps from 2 to 10 percentage points. Five answers are A and five are B. Two counterbalanced trial orders reduce one simple order effect.

This design is for learning. Ten trials from one learner do not estimate a population effect. The displays also differ in scale and task mechanics, so the results cannot isolate one perceptual channel as a formal experiment would.

## Run the package

From this module directory:

```powershell
Rscript build_perception_tasks.R
Rscript validate_perception_tasks.R
Rscript lab.R
Rscript critique_charts.R
```

The lab creates:

- 10 PNG stimuli in `outputs/lab/stimuli/`;
- `outputs/lab/response-template-a.csv`;
- `outputs/lab/response-template-b.csv`; and
- `outputs/lab/instructor-key.csv`.

### Run the test with a partner

1. Choose template A or B.
2. The partner opens one named stimulus at a time and does not show the next filename early.
3. Start timing when the full image is visible.
4. Record A or B, estimated percentage-point gap, elapsed seconds, and confusion.
5. Complete all 10 trials before opening the instructor key or source table.
6. Save the completed response CSV under a new filename.

Score it with:

```powershell
Rscript score_perception_test.R path/to/completed-responses.csv
```

The scoring script writes:

- `outputs/scored/scored-trials.csv`; and
- `outputs/scored/perception-summary.csv`.

The summary reports higher-value accuracy, mean absolute gap error, and median seconds by display.

## Three scaffold tiers

### Tier 1: Run and interpret

Use the prepared stimuli, one counterbalanced order, and the scoring script. Explain one error or delay using the mark and channel, not just the chart name.

### Tier 2: Modify and compare

Change one feature in a copy of `lab.R`:

- use the same 0% to 100% axis for dots and bars;
- add direct percentage labels;
- remove gridlines;
- increase or decrease the number of ticks; or
- highlight one hospital with both shape and a text label.

Predict the effect before rerunning a small set. State whether the modification changes detection, lookup, ordering, estimation, or all four.

### Tier 3: Author and justify

Build the quality committee's selected display using the HCAHPS extract. Submit the exact six-file package in `assessment.md`. The final display may be a chart or table if it best fits the named task.

## Interpretation rules

Your own test can support statements such as:

- I made fewer higher-value errors in the aligned-position trials.
- My exact table lookups were accurate but took longer because I had to subtract.
- I underestimated the gap in both bubble trials.
- Direct labels would change the task from visual estimation to lookup.

It cannot support statements such as:

- dot plots are always 25% more accurate than bar charts;
- clinicians cannot read pie charts;
- the observed time difference will occur in every audience; or
- one chart is universally best.

Use the published studies for general evidence and the classroom test to practice measurement and self-observation.

## Accessibility requirements

- Every stimulus and final display needs readable text and adequate contrast.
- The selected display cannot require color vision to recover the answer.
- A text alternative must name the chart structure, population, measure, main comparison, and material limit.
- Timing is not used to penalize disability, language background, motor differences, or assistive-technology use.
- Learners may request an untimed or keyboard-compatible path without losing competency credit.

## AI use

AI assistance is allowed for syntax, debugging, alternative generation, and prose editing. It cannot serve as the timed test participant or replace your recorded observations. Disclose the tool, purpose, adopted change, and verification in `decision-note.md`. If you did not use AI, write `No AI assistance used.`

## Required evidence readings

William S. Cleveland and Robert McGill, Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods:

https://doi.org/10.1080/01621459.1984.10478080

Jeffrey Heer and Michael Bostock, Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design:

https://idl.uw.edu/papers/crowdsourcing-graphical-perception

Anne M. Treisman and Garry Gelade, A Feature-Integration Theory of Attention:

https://pubmed.ncbi.nlm.nih.gov/7351125/

## Handoff

Module 01 made the mapping explicit. Module 02 adds evidence about how readers decode it. Module 03 turns the decision, data roles, reader task, and perception evidence into a repeatable chart-selection method.
