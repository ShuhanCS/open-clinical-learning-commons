# DA-730 Module 02 specification: Perception and visual accuracy

- Specification version: 0.1.0
- Commons release: 0.13.0
- Status: runnable release candidate
- Last updated: 2026-08-29
- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module package: `courses/data-visualization/modules/02-perception-accuracy/`
- Prerequisite package: `courses/data-visualization/modules/01-encoding-grammar/`

## 1. Module identity and place in the course

| Field | Contract |
|---|---|
| Module ID | `oclc-da730-02` |
| Title | Perception and visual accuracy |
| Course position | Second of 13 modules |
| Learner time | 8 hours |
| Prerequisite | Module 01, including its encoding map and CMS HCAHPS extract |
| Primary concept | Readers decode marks through perceptual judgments that differ in accuracy and effort |
| Primary software path | R and ggplot2 |
| Primary case | Hospital HCAHPS recommendation-result comparisons |
| Decision owner | Health-system quality committee |
| Next module | Module 03, Chart selection in practice |

Module 01 established what is encoded. Module 02 establishes why the chosen channel affects how accurately and quickly an audience can recover the comparison. Module 03 will combine that evidence with question and data structure to select a display.

## 2. Healthcare decision and audience

### Primary decision

A health-system quality committee must compare published HCAHPS recommendation results across hospitals and decide which display to use in its briefing packet. The committee needs to:

- find a named hospital;
- place hospitals in approximate order;
- distinguish close percentages;
- retrieve an exact value when needed;
- avoid overreading small visible differences; and
- recognize that the display does not establish statistical distinction or cause.

The module decision is which display creates the least avoidable reading error for that task, not which chart looks most modern.

### Audience characteristics

The committee is mixed:

- clinical and operational leaders may have little visualization training;
- analysts may need exact values and provenance;
- some readers use grayscale print, small screens, zoom, or assistive technology;
- meeting time is limited; and
- the committee may act on the apparent order even when differences are close.

The selected display must support overview and lookup without making familiarity the only design argument.

### Approved alternate cases

The tool-independent core may be instantiated with:

1. CMS timely-care results for an operations committee;
2. CDC PLACES county estimates for a population-health team; or
3. ClinicalTrials.gov enrollment values for a research portfolio group.

An alternate needs at least 10 comparable units, close quantitative pairs, exact answers, one named decision owner, a source record, task generator, scorer, and interpretation limits.

## 3. Foundation skill revisited or extended

The module assumes learners can:

- run and modify an R script;
- read a CSV;
- classify variables by analytical role;
- identify marks, channels, scales, labels, and layers; and
- produce the Module 01 encoding map.

It extends these skills by reversing the encoding process. The learner asks how a reader decodes the mark and measures that decoding through:

- higher-value correctness;
- absolute percentage-point estimation error;
- elapsed time as one imperfect effort signal; and
- a short interpretation-error note.

The module does not reteach Module 01's grammar vocabulary. It uses that vocabulary to explain observed errors.

## 4. Assessable learning outcomes

### Competency statement

Compare plausible encodings using evidence about perceptual accuracy and select the one the audience can read with the least avoidable error.

### Outcomes

| ID | Outcome | Direct evidence |
|---|---|---|
| M02.1 | Distinguish detection, identification, ordering, estimation, comparison, and exact lookup tasks. | Reader-task statement and assessment items |
| M02.2 | Explain the evidence-based preference for aligned position over angle, area, volume, or color intensity for close quantitative comparison. | `decision-note.md` and critique responses |
| M02.3 | Record and score correctness, absolute gap error, time, and confusion in a controlled classroom exercise. | `perception-test.md` and scoring outputs |
| M02.4 | Separate published graphical-perception evidence from a learner's small practice sample. | Limitations section and decision note |
| M02.5 | Diagnose a close-value pie comparison and an exaggerated-radius bubble display. | Critique and repair items |
| M02.6 | Produce a reproducible, accessible quality-committee display whose channel fits the reader task. | `analysis.R`, `selected-display.png`, and `alt-text.md` |

## 5. Concept ownership and boundaries

### This module owns

- visualization as perceptual decoding;
- elementary judgments of common-scale position, nonaligned position, length, angle, area, volume, and color intensity;
- reader-task distinctions;
- correctness, absolute estimation error, time, and confusion as observation fields;
- preattentive feature claims stated with task and context limits;
- clutter and avoidable audience effort;
- classroom perception-test protocol and scoring; and
- the difference between published evidence and a local practice sample.

### This module introduces but does not own

- tables as a valid display choice for exact lookup;
- ordering and small multiples;
- redundant accessibility cues;
- reference lines and direct labels as task-changing design choices;
- experimental-design limits; and
- the ethics of recording learner response data.

### Explicitly out of scope

- full chart-selection workflow, owned by Module 03;
- distributional summaries, owned by Module 04;
- denominators and adjustment, owned by Module 05;
- confidence intervals and statistical uncertainty, owned by Module 06;
- complete color and accessibility instruction, owned by Module 07;
- time, comparison, map, structure, dashboard, and narrative design, owned by Modules 08 through 13;
- a publishable human-subjects experiment;
- inferential statistics for perception results; and
- grading learners by response speed.

## 6. Lesson sequence and learner time

The module totals 8 hours, or 480 minutes.

| Sequence | Time | Activity | Required evidence |
|---|---:|---|---|
| Decision and reader-task opening | 30 min | Identify what the committee must detect, identify, order, estimate, compare, and look up. | Reader-task statement |
| Evidence-based concept core | 45 min | Study graphical decoding, the accuracy starting order, task dependence, salient features, and clutter. | Annotated evidence note |
| Test prediction and setup | 45 min | Predict condition patterns, assign counterbalanced order, and record timing accommodation. | Prediction and protocol |
| Ten-trial perception lab | 90 min | Complete and record all trials with a partner. | Completed response CSV |
| Scoring and interpretation | 60 min | Run the scorer and distinguish observed self-data from general evidence. | Scored trials and five-row summary |
| Critique and repair studio | 60 min | Diagnose close pies and exaggerated bubble radii. | Two repair responses |
| Independent assessment | 120 min | Build and justify a committee display. | Six-file package |
| Peer reproducibility and access check | 30 min | Run code, inspect source context and text alternative, and audit the claim. | Verification note and corrections |
| **Total** | **480 min** | | **8 hours** |

### Accommodation rule

Timing is a descriptive field, not a performance requirement. A learner may use an untimed, extended-time, keyboard, zoom, screen-reader, or partner-assisted path. The protocol records the mode so observations are interpreted honestly. Competency credit depends on measurement logic and design judgment, not speed.

## 7. Authoritative readings and public clinical sources

### Required evidence

1. Cleveland, W. S., and McGill, R. (1984). Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods.
   https://doi.org/10.1080/01621459.1984.10478080
2. Heer, J., and Bostock, M. (2010). Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design.
   https://idl.uw.edu/papers/crowdsourcing-graphical-perception
3. Treisman, A. M., and Gelade, G. (1980). A Feature-Integration Theory of Attention.
   https://pubmed.ncbi.nlm.nih.gov/7351125/

### Required clinical source

CMS, Patient survey (HCAHPS) - Hospital:

https://data.cms.gov/provider-data/dataset/dgck-syfz

### Required module materials

- `courses/data-visualization/modules/02-perception-accuracy/README.md`
- `courses/data-visualization/modules/02-perception-accuracy/data-spec.md`
- Module 01 encoding map and source record

### Reading standard

Learners do not need to reproduce the original experiments. They must identify the task, dependent measure, evidence-supported design implication, and one limit on transferring the result to the committee setting.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Upstream HCAHPS release

| Field | Value |
|---|---|
| Publisher | Centers for Medicare & Medicaid Services |
| Dataset | Patient survey (HCAHPS) - Hospital |
| Dataset ID | `dgck-syfz` |
| Release | 2026-08-13 |
| Coverage | 2024-10-01 through 2025-09-30 |
| Shared extract | `../01-encoding-grammar/data/hcahps_ma_recommend_2026.csv` |
| Shared extract rows | 65 |
| Shared extract checksum | `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74` |
| Rights | U.S. government public-reporting data in the public domain; attribution requested; no implied endorsement |

### Derived perception-task release

| Field | Value |
|---|---|
| Path | `data/perception_tasks_2026.csv` |
| Rows | 10 |
| Columns | 13 |
| Displays | Two each for dot, bar, table, pie, and bubble |
| Gap range | 2 to 10 percentage points |
| Correct aliases | Five A and five B |
| Checksum | `b792637411a00c67baa30d70688e5a9b8353cee8a2758251419e84c0c4c1cbe6` |

### Teaching purpose

The task table produces exact-answer stimuli and supports scoring without duplicating the CMS extract. Actual hospital identities are retained for provenance and post-test debrief, while the timed stimuli use Hospital A and Hospital B to control label length and familiarity.

### Learner-response governance

Completed response files may contain timing, errors, confusion, and accommodation information. Treat them as educational records. Do not commit identified learner response files to the public repository. Do not pool or publish them as research without appropriate consent, privacy review, and institutional approval.

## 9. Data dictionary and expected analytic structure

The canonical task dictionary is in `data-spec.md`.

### Task grain

| Property | Contract |
|---|---|
| Unit | One paired-hospital perception trial |
| Task key | `trial_id` |
| Condition | `display` |
| Stimulus values | `facility_a_percent` and `facility_b_percent` |
| Direction answer | `correct_alias` |
| Magnitude answer | `correct_gap_points` |
| Provenance | Both facility IDs and names plus `cms_release_date` |

### Response grain

| Property | Contract |
|---|---|
| Unit | One learner response to one trial |
| Join key | `trial_id` |
| Direction response | `higher_response` |
| Magnitude response | `estimated_gap_points` |
| Effort proxy | `seconds` |
| Qualitative error | `confusion_note` |

### Derived scoring fields

- `is_correct`: response alias equals the task's correct alias;
- `absolute_gap_error`: absolute value of estimated gap minus correct gap;
- `higher_accuracy_percent`: mean correctness times 100 within a display;
- `mean_absolute_gap_error`: mean absolute error within a display; and
- `median_seconds`: median recorded time within a display.

With only two trials per display, these summaries are descriptive prompts rather than stable estimates.

## 10. Worked example and instructor walkthrough

### Worked question

For close HCAHPS percentages, which display helps the committee identify the higher hospital and estimate the percentage-point gap with the least avoidable error?

### Walkthrough sequence

1. **Name the two tasks.** Direction asks A or B. Magnitude asks the gap.
2. **Predict before testing.** Learners predict correctness, error, and time patterns.
3. **Inspect T01 only after prediction.** T01 uses aligned point position for 71% and 75%.
4. **Separate mark from answer.** The point has no direct label; the reader estimates from the scale.
5. **Record without correction.** A partner records B, estimated gap, seconds, and confusion before revealing the key.
6. **Calculate error.** A 6-point estimate for the true 4-point gap has absolute error 2.
7. **Compare with T05.** T05 is a table with exact 79% and 86% values. Direction and gap can be exact, but subtraction may add time.
8. **Compare with T07.** Separate pie angles make a 6-point difference harder to estimate precisely.
9. **Score all trials.** Use the script, not manual transcribing, for derived fields.
10. **Interpret narrowly.** State what happened in the learner's trials and what the published literature supports more generally.
11. **Return to the committee.** Choose a display based on order, gap, lookup, and meeting effort.

### Expected answer for the worked calculation

If the learner identifies B correctly in T01 and estimates 6 percentage points:

- direction correctness: true;
- correct gap: 4 points;
- estimated gap: 6 points; and
- absolute gap error: 2 points.

## 11. Guided practice

### Tier 1: Run and interpret

Learners:

1. generate all 10 stimuli;
2. complete one counterbalanced order with a partner;
3. score the response file;
4. compare direction correctness, gap error, and time; and
5. explain at least one trial using position, length, angle, area, or lookup.

### Tier 2: Modify and compare

Each learner changes one feature in a copied lab script:

- commonize the dot and bar axis range;
- add direct labels;
- remove or change gridlines;
- alter tick density; or
- add a redundant shape and text alert.

Before rerunning two matched trials, the learner records:

- the changed grammar component;
- the reader task expected to change;
- the predicted direction of correctness, error, or time; and
- the access effect.

Afterward, the learner states whether the observation matched the prediction without generalizing from two trials.

### Tier 3: Author and justify

The learner creates the committee's final display and six-file assessed package. A table may be selected if the stated task is exact lookup. A dot plot or bar chart may be selected for ordering and comparison. The argument must name the task and avoid a universal chart claim.

## 12. Independent exercise

### Prompt

Prepare a quality-committee display and recommendation using at least 10 reported Massachusetts hospitals from the Module 01 HCAHPS extract.

The committee's primary task must be one of:

- order hospitals and inspect close gaps;
- find two named hospitals and compare exact values; or
- detect one explicitly defined follow-up state while preserving all labels.

The learner chooses the task before the display.

### Required evidence chain

1. State the reader task.
2. Name the primary perceptual judgment.
3. Cite the published evidence that informs the design.
4. Report what the learner's classroom test added.
5. Name one relevant test confound.
6. Build the selected display.
7. State the error or effort avoided.
8. Bound the clinical and statistical claim.

### Transfer prompt

The committee now has 50 hospitals and needs to detect one alert state. The learner explains how detection, identification, and comparison separate, which salient feature could help, and why a label or shape must preserve access.

## 13. Visualization and communication requirements

The final display must:

- match the chosen reader task;
- use aligned position or common-baseline length for close quantitative comparison unless the chosen task is exact table lookup;
- avoid angle or area as the only evidence for a close gap;
- show percent units;
- identify the HCAHPS construct;
- disclose hospital subset, CMS release, and measurement period;
- use readable hospital labels;
- remain interpretable without color;
- avoid an undisclosed radius, area, truncation, or transformation; and
- state that the result is not total hospital quality.

### Direct labels

Direct values are allowed. The learner must explain that they shift part of the task from visual estimation to lookup. This is often a benefit, not a violation.

### Axis rule

A nonzero axis may be used for a point comparison when the visible range and measure are clear. Common-baseline bars must start at zero unless a defensible exception is explicitly marked and justified. The module does not teach deceptive truncation as a way to make small gaps look important.

## 14. Exact submission package and filenames

```text
module-02/
  perception-test.md
  analysis.R
  selected-display.png
  source-record.yml
  alt-text.md
  decision-note.md
```

`perception-test.md` contains prediction, protocol, results, patterns, interpretation errors, limitations, and next design test. Full file contracts are in `assessment.md`.

### Reproducibility rule

`analysis.R` uses relative paths, checks required fields, applies a deterministic subset, and writes the PNG. A saved R workspace, screenshot-only chart, or proprietary published link without editable source is incomplete.

## 15. Rubric and pass conditions

| Criterion | Points |
|---|---:|
| Perception-test record | 20 |
| Published evidence and reasoning | 15 |
| Reproducible analysis | 20 |
| Selected display | 20 |
| Decision note and claim boundary | 15 |
| Accessibility and text alternative | 10 |
| **Total** | **100** |

The pass mark is 75. Five conditions are mandatory:

1. all 10 trials are recorded or an approved access path is documented;
2. code runs and writes the selected display;
3. the display fits a named reader task;
4. source, measure, release, period, and subset are accurate; and
5. classroom observations are not presented as generalizable research.

### Week-3 checkpoint contribution

The Module 02 test record, evidence note, final display, source record, and decision note feed the week-3 visualization judgment dossier. Module 03 will require the learner to compare this choice with at least one alternative through a repeatable selection matrix.

## 16. Common errors, failure modes, and interventions

| Failure | Likely misconception | Intervention |
|---|---|---|
| Position is called universally best | The evidence order is detached from the task. | Give a one-value exact lookup and compare a table. |
| The 10 trials are called a proving experiment | Instrumented practice is confused with research. | Ask what was randomized, sampled, controlled, and replicated. |
| Fast responses earn higher marks | Time is treated as learner ability rather than one noisy effort signal. | Grade protocol and reasoning, never speed. |
| Higher-value correctness is the only metric | Direction and magnitude tasks are collapsed. | Score absolute gap error separately. |
| Direct labels are called cheating | Lookup is treated as inferior to estimation. | Ask what the committee actually needs. |
| Pie familiarity is the only defense | Familiarity is substituted for task performance. | Ask readers to estimate a close gap without values. |
| Bubble radius carries a transformed percent | Radius and area are confused. | Calculate how radius changes area and restore position. |
| Dot and bar times are compared as if scale were controlled | A visible design difference is ignored. | Rerun with common axes and label it a new test. |
| Preattentive color carries the alert alone | Detection is confused with access and identification. | Add text and shape; test grayscale. |
| Named learner speed is published | Educational data governance is ignored. | De-identify or keep the responses private. |
| AI writes a plausible result not present in the CSV | Narrative fluency replaces evidence. | Trace every claim to a scored row or citation. |

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Timing accommodations do not reduce competency credit.
- Stimuli and final display must support zoom and ordinary-size reading.
- Required meaning cannot depend on color alone.
- Every final display needs a text alternative.
- A table or direct label remains available for exact-value access.
- Response notes distinguish perceptual confusion from an access barrier where possible.

### Equity

Do not compare named learner speed or accuracy publicly. Visual ability, color perception, language, prior chart exposure, disability, device, and testing conditions all affect performance. A committee design should support the range of intended readers rather than an imagined average reader only.

The HCAHPS source also lacks patient subgroup variables in this extract. The selected hospital comparison cannot establish equitable experience across race, ethnicity, language, disability, payer, or other populations.

### Privacy

CMS inputs are aggregate public data. Learner response files are educational records and stay outside the public repository when identifiable. A future research study requires consent, a protocol, secure storage, appropriate institutional review, and a separate release decision.

### Responsible claims

Allowed:

- describe a learner's own accuracy, error, and time;
- report a small class in aggregate when course policy permits;
- connect a display decision to published perception evidence;
- state a task-specific recommendation; and
- identify test limitations.

Not allowed:

- claim a universal effect size from these trials;
- diagnose a learner's perceptual ability;
- penalize slower accessible use;
- claim the HCAHPS chart proves quality or cause; or
- present a transformed bubble radius as the original percentage.

## 18. AI and agent policy

AI may assist with:

- explaining a paper or term;
- debugging build, scoring, or chart code;
- proposing a display alternative;
- checking whether the code matches the claimed channel; and
- editing the decision note or text alternative.

AI may not:

- act as the timed participant;
- invent responses, elapsed times, or confusion notes;
- claim to have visually inspected output it did not inspect;
- fabricate a paper finding;
- replace the learner's verification run; or
- turn the classroom exercise into a general claim.

The decision note records tool, purpose, adopted change, and verification. `No AI assistance used.` is complete when true.

## 19. Answer key and instructor notes

The instructor key is:

`courses/data-visualization/modules/02-perception-accuracy/instructor-notes.md`

It contains:

- verified technical results;
- the eight-hour sequence;
- all 10 trial answers and hospital identities;
- published-evidence teaching notes;
- accepted and prohibited classroom-test interpretations;
- critique diagnoses and repairs;
- a strong decision-note pattern;
- common-error interventions;
- point-level grading guidance;
- accessibility and timing accommodations;
- a short-time path; and
- human review requirements.

The machine-readable answer key is generated as `outputs/lab/instructor-key.csv`. Instructors should not distribute it until testing is complete.

## 20. Runnable acceptance checks

### Build the task release

```powershell
Rscript build_perception_tasks.R
```

Pass: 10 deterministic tasks are recreated from the Module 01 extract.

### Validate the task release

```powershell
Rscript validate_perception_tasks.R
```

Pass: 12 of 12 checks succeed.

### Generate stimuli

```powershell
Rscript lab.R
```

Pass: 10 stimulus PNGs, two response templates, and one instructor key are created.

### Score a response file

```powershell
Rscript score_perception_test.R path/to/completed-responses.csv
```

Pass: the script writes scored trials and a five-row display summary. A perfect-response self-check must produce 100% direction accuracy, zero mean absolute gap error, and the supplied positive time for each display.

### Generate critiques

```powershell
Rscript critique_charts.R
```

Pass: the close-pie and exaggerated-bubble PNGs are created.

### Visual inspection

Confirm:

- all trial images show A and B without actual hospital names;
- dot and bar axes are visible and labeled;
- table values render fully;
- both pie facets and the legend render;
- bubble areas and size legend render;
- source release captions are visible; and
- critique titles make the intended question clear without giving the repair.

### Link check

Confirm browser resolution for the Cleveland and McGill DOI and HTTP responses for the CMS dataset, Heer and Bostock page, Treisman and Gelade PubMed record, CMS data dictionary, documentation license, and code license. The Taylor & Francis publisher currently returns 403 to automated HEAD requests after the DOI resolves, so a scripted HEAD failure alone does not invalidate the citation.

### Repository checks

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
git diff --check
```

### Clean-run gate

Before alpha, an independent instructor follows only the learner README from a clean checkout, completes an accommodated or standard response path, scores it, builds the final display, and records any hidden assumption.

## 21. Release status, reviewers, version, and known issues

### Release identity

| Item | Value |
|---|---|
| Module version | 0.1.0 |
| Commons release | 0.13.0 |
| Status | Runnable release candidate |
| Release date | 2026-08-29 |
| Technical validation | Complete |
| Human review | Pending |

### Maturity gate

The module is a runnable release candidate because the task table is reproducible, answers are validated against the pinned HCAHPS source, stimuli render, scoring has a perfect-response self-check, critiques render, the six-file assessment is exact, and the instructor key is complete.

Alpha requires sign-off from:

1. visualization faculty and evidence fidelity;
2. health-system quality or clinical content;
3. accessibility, including timed-task accommodation; and
4. independent teachability from a clean checkout.

Beta requires a taught pilot and revision. Stable requires successful reuse by a second instructor or program.

### Known issues

- Human reviews are pending.
- Ten trials are too few for a generalizable perception claim.
- Values differ across conditions.
- Dot and bar scales differ.
- Partner timing, device, motor, language, visual, and rendering effects are not controlled.
- Repeated viewing can create practice and memory effects.
- macOS and Linux clean-run verification is pending.

## Handoff to Module 03

Module 02 ends with a task-specific perception argument. Module 03 will require learners to combine:

- the decision and audience;
- variable roles from Module 01;
- the reader task and perceptual evidence from Module 02;
- the number of measures and groups;
- uncertainty and context needs; and
- the option to choose a chart, table, multiple views, or no display.

The next build unit is:

`docs/curriculum/courses/DA-730/modules/03-chart-selection-spec.md`
