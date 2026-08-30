# Module 02 instructor notes and answer key

## Teaching purpose

Module 01 taught learners to name a mapping. Module 02 gives them an empirical reason to care which mapping they choose. The central move is from taste language, such as clean or engaging, to reader-task language, such as lower estimation error, faster lookup, or less legend search.

The 10-trial test is an instrumented exercise, not a study. Model that distinction every time results are discussed.

## Verified setup

From the module directory:

```powershell
Rscript build_perception_tasks.R
Rscript validate_perception_tasks.R
Rscript lab.R
Rscript critique_charts.R
```

Reference environment:

- R 4.6.1
- ggplot2 4.0.3
- Windows

Expected technical results:

- 12 of 12 task-design checks pass;
- 10 stimuli render;
- two response templates and one instructor key are created;
- the scoring self-check returns 100% higher-value accuracy and zero absolute gap error for a perfect response file; and
- two critique charts render.

## Eight-hour teaching sequence

| Segment | Time | Instructor action | Learner evidence |
|---|---:|---|---|
| Decision and task opening | 30 min | Ask what the quality committee must detect, identify, order, estimate, compare, or look up. | Named reader task |
| Evidence-based concept core | 45 min | Teach graphical decoding, the accuracy starting order, task dependence, preattentive features, and clutter. | Annotated channel ranking with caveat |
| Test prediction and setup | 45 min | Form pairs, assign A or B order, check timing accommodation, and collect predictions. | Prediction and protocol record |
| Ten-trial perception lab | 90 min | One partner presents and times; then roles may switch with the other order. | Completed response template |
| Scoring and interpretation | 60 min | Run the scorer and separate observation from general evidence. | Scored trials and five-row summary |
| Critique and repair studio | 60 min | Diagnose close pies and exaggerated bubble radii. | Two repair proposals |
| Independent assessment | 120 min | Coach the reader task and evidence chain. | Six-file package |
| Peer run and revision | 30 min | Test code, text alternative, source record, and claim limits. | Corrected package |
| **Total** | **480 min** | | **8 hours** |

## Trial answer key

| Trial | Display | A | B | Higher | Gap |
|---|---|---:|---:|---|---:|
| T01 | Dot | 71% | 75% | B, Mount Auburn Hospital | 4 points |
| T02 | Dot | 72% | 66% | A, UMass Memorial Medical Center/University Campus | 6 points |
| T03 | Bar | 68% | 73% | B, Boston Medical Center | 5 points |
| T04 | Bar | 79% | 75% | A, Beth Israel Deaconess Medical Center | 4 points |
| T05 | Table | 79% | 86% | B, New England Baptist Hospital | 7 points |
| T06 | Table | 68% | 62% | A, South Shore Hospital | 6 points |
| T07 | Pie | 66% | 72% | B, Southcoast Hospitals Group | 6 points |
| T08 | Pie | 62% | 52% | A, Baystate Medical Center | 10 points |
| T09 | Bubble | 66% | 72% | B, Lahey Hospital & Medical Center, Burlington | 6 points |
| T10 | Bubble | 75% | 73% | A, Winchester Hospital | 2 points |

Do not reveal hospital identities until after scoring. The A and B aliases control label length and familiarity during the task.

## Published-evidence answer key

### Graphical perception

Cleveland and McGill define graphical perception as visual decoding and connect elementary judgments to quantitative accuracy. Their work supports a design preference for position on common scales over less accurate angle and area judgments for elementary comparison tasks.

Heer and Bostock replicated earlier graphical-perception work through crowdsourcing and extended it to additional design questions. The teaching point is that visualization recommendations can be tested rather than treated only as taste.

### Attention and salient features

Treisman and Gelade's feature-integration work supports a careful distinction between detecting a simple distinctive feature and integrating several features into an identified object. In visualization teaching, do not reduce this to a list of colors that always pop out. Salience depends on contrast, surrounding marks, the task, and the viewer.

### Required caveat

The common encoding order is a starting model. It is not a promise about every reader or chart. Labels, gridlines, scale, interaction, density, task, and prior knowledge can change performance.

## Classroom-test interpretation key

There is no required empirical winner in an individual learner's 10 trials. Full credit depends on accurate scoring and bounded interpretation.

Strong observations include:

- higher-value identification and gap estimation can diverge;
- a table can provide zero estimation error but still require slower subtraction;
- two pie angles can support a broad higher/lower judgment while making a close gap hard to estimate;
- area judgments can make small differences hard to order;
- gridlines and axis range affect estimation; and
- direct labels change the task from estimation toward lookup.

Required limitations include at least three of:

- only two trials per display;
- one learner or a small class;
- different values across conditions;
- different dot and bar scales;
- order, practice, and memory effects;
- device and rendering effects;
- partner timing error;
- motor, visual, language, or assistive-technology effects; and
- a simplified task unlike a live committee decision.

## Critique answer key

### Close values as separate pies

Problems:

- the committee must compare angles across separate circles;
- the values are close, so the wedge differences are difficult to estimate;
- there is no aligned quantitative scale;
- ordering four hospitals requires repeated visual memory; and
- familiarity with pies does not solve the quantitative task.

Smallest repair: use aligned points or common-baseline bars. Add direct values if the committee needs exact lookup.

### Exaggerated bubbles

Problems:

- the code subtracts 60 and maps the remainder to radius;
- circle area therefore changes with the square of that transformed radius;
- a small percentage difference becomes a much larger visible area ratio;
- no scale explains the transformation; and
- the display implies magnitude rather than supporting an accurate gap estimate.

Smallest repair: map the original percentage to aligned x position. If area must encode a second quantity, use an area-correct scale, label it, and keep the percentage on position.

## Strong decision-note pattern

> The quality committee's primary task is to order hospitals and identify where close recommendation results differ, not retrieve one isolated exact value. I recommend an aligned dot plot with direct percentage labels. Published graphical-perception evidence favors common-scale position for quantitative comparison. In my classroom trials, the dot tasks produced [learner result], while the table produced [learner result]. Those 10 trials are practice observations, not a general estimate. The selected display reduces angle and area estimation, keeps exact values available, and uses a caption for the CMS release and measurement period. It does not show statistical distinction, reasons for a gap, or total hospital quality.

## Common errors and interventions

| Error | What it reveals | Intervention |
|---|---|---|
| Learner says position is always best | Ranking is treated as a law without a reader task. | Give an exact one-cell lookup and ask whether a table is clearer. |
| Learner calls the 10 trials an experiment proving superiority | Classroom instrumentation is confused with research design. | Ask what was randomized, controlled, replicated, and sampled. |
| Response time is graded as speed | Effort measure is confused with learner worth. | Grade recording and interpretation, never fast performance. |
| A preattentive color is used without a label | Detection is confused with identification and access. | Remove color and ask how the state can still be recovered. |
| Bar and dot results are compared without noting scale | A confound is ignored. | Put both on 0% to 100% and predict the change. |
| Bubble size uses radius without area correction | Geometry is confused with the encoded quantity. | Calculate how doubling radius changes area. |
| Table is dismissed as not a visualization | Chart preference replaces task fit. | Ask whether exact lookup or overview is the decision task. |
| AI invents a plausible result narrative | Fluency replaces observed data. | Compare prose against `scored-trials.csv` line by line. |

## Grading guidance

For the 20 perception-test points:

- 5 points: prediction, order, timing mode, and complete trial record;
- 5 points: correct use of scoring outputs;
- 5 points: correctness, error, time, and confusion observations; and
- 5 points: at least three material limitations and one next design test.

For the 15 evidence points:

- 5 points: accurate common-scale position argument;
- 5 points: reader-task qualification, including table lookup; and
- 5 points: careful use of attention or salience without universal claims.

## Accessibility and accommodation

- Offer an untimed path when timing would measure disability or access rather than the intended comparison task.
- Allow keyboard or assistive-technology presentation.
- Do not compare named learner speed publicly.
- Check all stimuli at ordinary display size before class.
- Use the response notes to identify access barriers separately from perceptual confusion.
- Grade reasoning and complete evidence, not speed.

## If time is short

Keep the evidence core, prediction, one trial per display, scoring, one critique, and the final display recommendation. Cut the second trial per display and the role swap. Preserve the limitation discussion because fewer trials make it more important.

## Human review still required

Before alpha release, record:

- DA-730 visualization-faculty review;
- health-system quality or clinical-content review;
- accessibility review, including the timed-task accommodation; and
- independent-instructor clean-run review.
