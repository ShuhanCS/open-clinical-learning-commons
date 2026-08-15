# Ali Goff DataVis Module 04: build specification

- Status: implementation-ready draft for faculty and clinical review
- Date: 2026-08-15
- Course: DA-730, Analyzing, Visualizing, and Storytelling with Data
- Course designer and content owner: Ali Goff
- Commons sponsor: Shuhan He
- Module: Distributions versus summaries
- Current module version: `0.1.0`
- Target runnable module version: `0.2.0`
- Primary source: [Ali Goff's DA-730 redesign](../source/ali-goff-da-730-course-redesign.md#module-04-distributions-versus-summaries)
- Content record: [Module 04](../../courses/data-visualization/modules/04-distributions-vs-summaries/README.md)

## Decision

Build Module 04 as the first complete Open Clinical Learning Commons teaching release.

The release will pair a synthetic emergency department encounter dataset with a reproducible R lab, critique exercises, assessments, an instructor key, validation checks, and a release record. Another instructor must be able to teach it without Ali's original Word document and without access to patient data.

The first build makes these choices:

- R and ggplot2 are the graded environment. The concept core remains independent of software.
- A small, transparent R simulation creates the data. The module does not need a generative AI model.
- The learner dataset includes the `boarded` field for the transition cohort.
- The main `real` dataset is committed. The `null` and `trivial` assessment variants are generated on demand.
- The module uses synthetic data only. No MGB, MIMIC, partner, or other patient-level data enter the repository.

## What success looks like

A learner can inspect emergency department length-of-stay data, find the process hidden by a stable summary, select a display that fits the operational decision, and explain what leadership should do differently.

An instructor can clone the repository, run four documented commands, teach the module, and grade the work with the supplied rubric. A reviewer can reproduce the data and confirm that it meets the teaching contract.

## Audience

### Learner

The first learner is an MSDA student or IDEA fellow who understands mean, median, quantiles, and histograms but may still need working R code to modify.

### Instructor

The instructor may know health analytics without having designed the dataset or the emergency department case. The package must explain prerequisites, timing, likely misconceptions, grading, and what to cut.

### Reviewer

The review team covers four roles:

1. Ali Goff approves the visualization competency and teaching sequence.
2. An emergency department operations reviewer approves the case language and operational interpretation.
3. A data or statistical reviewer checks generation, validation, and reproducibility.
4. An instructor who did not build the module completes a dry run.

One person may fill more than one role. The release record names the people who completed each review.

## Competency and evidence

The competency is:

> Given a dataset and a comparison question, determine whether a summary statistic faithfully represents the underlying distribution, select a display that reveals the features relevant to the decision, and state what decision changes because of the fuller view.

The learner must demonstrate three behaviors:

| Code | Behavior | Acceptable evidence |
|---|---|---|
| C4.1 | Diagnose | Identifies skew, multiple modes, unequal group sizes, or a consequential tail that the original summary hides. |
| C4.2 | Select and justify | Chooses a display or summary and explains why it is better than at least one reasonable alternative. |
| C4.3 | Connect to consequence | States which operational decision changes and why. |

A polished chart cannot pass by itself. The learner must meet C4.3.

## Scope

The build includes:

- the domain-independent concept core already recorded in the module README;
- the emergency department length-of-stay case;
- a reproducible synthetic data release;
- one lab with run, modify, and author support levels;
- three flawed displays and repair prompts;
- recognition, application, and judgment assessments;
- an instructor key and rubric;
- release metadata and review evidence.

The build does not include the other ten DA-730 modules, a Python mirror, a learning management system, a credential, a full synthetic hospital, live clinical decision support, or an OMOP implementation.

## Package contract

The completed module contains only the files needed to generate, inspect, teach, assess, and release it:

```text
courses/data-visualization/modules/04-distributions-vs-summaries/
  README.md
  data-spec.md
  generate_ed_los.R
  validate_ed_los.R
  data/
    ed_los_2026.csv
  lab.R
  critique_charts.R
  assessment.md
  instructor-notes.md
  release.json
```

The README remains the concept and case record. `data-spec.md` holds the dictionary, generation assumptions, and check definitions. The instructor notes include the answer key and rubric so the first build does not split material across more files than instructors need.

Generated figures go to an untracked `outputs/` directory. Assessment variant CSV files are not committed.

## Runnable interface

The module must work from its own directory with these commands:

```powershell
Rscript generate_ed_los.R real 730 data/ed_los_2026.csv
Rscript validate_ed_los.R data/ed_los_2026.csv real
Rscript lab.R data/ed_los_2026.csv
Rscript critique_charts.R data/ed_los_2026.csv
```

`generate_ed_los.R` accepts three positional arguments: variant, seed, and output path. With no arguments it uses `real`, `730`, and `data/ed_los_2026.csv`.

The generator and validator use base R. The lab and critique scripts may use only `ggplot2`, `dplyr`, and `readr`. If a package is missing, the script stops with the exact installation command. Each script fails with a nonzero exit code and a plain explanation when its input is invalid.

## Data release

### Provenance

Every row is synthetic. The first release is generated from the teaching requirements in Ali Goff's course design. It is not fitted to, sampled from, or derived from an MGB or MIMIC patient record.

The release documentation must distinguish three things:

- pedagogical targets from Ali's design;
- assumptions introduced by the Commons implementation;
- results measured from the generated file.

If a later release is calibrated with an open aggregate source, its source URL, retrieval date, license, transformation, and affected parameters must be recorded. That change requires a new data version.

### Schema

The committed CSV has 8,392 rows and these seven columns in this order:

| Column | Type | Allowed values and rule |
|---|---|---|
| `encounter_id` | character | Unique synthetic identifier. No identifier has meaning outside this file. |
| `arrival_date` | date | A valid date from 2026-01-01 through 2026-12-31. |
| `esi` | integer | 1, 2, 3, 4, or 5. ESI 1 is the deliberately small group. |
| `age_group` | character | `18-39`, `40-64`, `65-79`, or `80+`. |
| `disposition` | character | `admitted` or `discharged`. |
| `boarded` | integer | 0 or 1. A boarded encounter must also be admitted. |
| `los_min` | integer | Positive arrival-to-departure length of stay in minutes. |

The reference release uses 6,462 discharged encounters, 1,930 admitted encounters, and 66 ESI 1 encounters. Missing values are not allowed in the first release.

### Generation model

The generator must make the teaching mechanism understandable in code:

1. Allocate 8,392 encounters across the 2026 calendar year.
2. Assign disposition, acuity, and age group from documented categorical probabilities or exact counts.
3. Improve the discharged length-of-stay distribution over the year to represent the fast-track pathway.
4. Increase boarding among admitted encounters from about 10 percent in January to about 46 percent in December.
5. Generate admitted non-boarded and boarded stays from separate right-skewed distributions, with boarded stays forming the longer-stay mode.
6. Combine the pathways, round to positive whole minutes, shuffle rows, and assign encounter identifiers.

The code must name its parameters near the top and explain each in clinical language. It must not tune hidden constants after writing the CSV. The validator decides whether a generated file is releasable.

### Teaching checks for the `real` variant

All six checks must pass:

| Check | Required result |
|---|---|
| Skew | Overall mean divided by overall median is at least 1.20. |
| Unequal groups | The larger disposition group is at least 2.5 times the smaller group. |
| Hidden second process | The admitted distribution has a longer-stay mode associated with boarding, while the pooled distribution makes it much less prominent. |
| Opposing trends | January-to-December mean change is less than 6 percent in absolute value and the 90th percentile rises by more than 40 percent. |
| Small subgroup | At least one meaningful subgroup has fewer than 100 rows. The reference release uses 66 ESI 1 encounters. |
| Average of averages | The unweighted average of admitted and discharged means differs from the pooled mean by at least 30 minutes. |

The hidden-process check uses two forms of evidence. An automated proxy confirms that boarded admitted encounters have a median at least 300 minutes above non-boarded admitted encounters and that boarding prevalence rises by at least 25 percentage points from January to December. A reviewer then confirms that the admitted density has a visible second mode that is weak when all encounters are pooled. The release record stores both results.

The source realization provides reference values, not equality tests:

- overall mean divided by median: 1.41;
- admitted modes near 252 and 782 minutes;
- annual mean change: +4.5 percent;
- 90th-percentile change: +104.1 percent;
- difference between the unweighted average of group means and pooled mean: 71 minutes.

### Variant contract

All variants keep the same schema, row count, seed behavior, and realistic right-skewed distributions. The variant name does not appear in the CSV.

| Variant | Teaching purpose | Required pattern |
|---|---|---|
| `real` | Find a consequential process hidden by the pooled summary. | Passes the six teaching checks above. |
| `null` | Report honestly that the expected deterioration is absent. | January-to-December changes in mean, median, and 90th percentile are each within 5 percent; the over-eight-hour share changes by less than 1 percentage point. |
| `trivial` | Separate statistical detection from operational importance. | January and December differ at `p < 0.05` using a two-sided Wilcoxon rank-sum test, while median changes by no more than 10 minutes, the 90th percentile changes by no more than 10 percent, and the over-eight-hour share changes by no more than 2 percentage points. |

The validator runs the Wilcoxon test with `stats::wilcox.test(..., exact = FALSE)` and reports the effect measures beside the p-value. The trivial thresholds are teaching choices, not universal clinical thresholds. The case prompt tells learners what operational difference would justify action.

### Determinism

For a given variant and seed, two generator runs must produce byte-identical CSV files. A different seed must preserve the variant contract without producing the same file.

The release process calculates a SHA-256 checksum for the committed CSV and records it in `release.json`.

## Lab specification

### Standard session

The standard teaching profile is 90 minutes:

| Segment | Time |
|---|---:|
| Concept core and first prediction | 20 minutes |
| Run and observe | 20 minutes |
| Modify and compare | 25 minutes |
| Author or critique task | 15 minutes |
| Decision debrief | 10 minutes |

The existing 60-minute and 35-minute cuts remain available in the instructor notes. The empirical cumulative distribution function is an extension if the class cannot complete it inside the standard session.

### Tier 1: run and observe

`lab.R` produces four labelled views:

1. monthly mean length of stay;
2. the pooled length-of-stay distribution;
3. distributions separated by disposition;
4. monthly mean, median, 90th percentile, and share over eight hours.

Learners answer what each view reveals, what it hides, and whether the leadership conclusion changes.

### Tier 2: modify

The learner starts from working code and completes the six modifications listed in the module content record. The required transition-cohort tasks are the box-plot comparison, disposition split, boarding split, and 90th-to-95th-percentile change. The logarithmic scale and empirical cumulative distribution function may be cut for time.

### Tier 3: author

The learner produces:

- one reproducible R script;
- one chart for the chief operating officer;
- a two-sentence board note stating the finding and recommended decision;
- a short justification that compares the chosen display with one alternative.

No single chart type is required. A simple summary can earn full credit in the null or trivial variant when the learner justifies it and reports the result honestly.

### Chart requirements

Every submitted chart must identify the measure and unit, use an honest scale, label the relevant groups, and avoid using color as the only way to distinguish a finding. The learner supplies one or two sentences of alt text with the exported chart.

## Critique set

`critique_charts.R` reproducibly creates:

1. a mean length-of-stay chart with standard error bars that hides group size and distribution;
2. a monthly mean chart with a vertical axis from 180 to 210 minutes;
3. an unweighted average of admitted and discharged group means presented as the overall mean.

Each critique asks what is concealed, who could be affected, and what should replace the display or calculation. The answer key must explain why repairing the visual style alone does not repair the analytic choice.

## Assessment and rubric

`assessment.md` contains the nine items already defined in the module record and marks each with C4.1, C4.2, or C4.3. It also provides an instructor-facing map from each item to the expected evidence.

The Tier 3 submission uses a 100-point rubric:

| Criterion | Points |
|---|---:|
| Diagnoses the hidden or absent distributional pattern | 25 |
| Selects an appropriate statistic and display | 20 |
| Justifies the choice against a reasonable alternative | 15 |
| Connects the evidence to a defensible operational decision | 30 |
| Produces reproducible, readable, and accessible work | 10 |

A passing submission needs at least 70 points and at least 18 of the 30 decision points. This prevents chart polish from compensating for a missing or unsupported recommendation.

## Instructor notes

`instructor-notes.md` must let an instructor teach without consulting the source document. It includes:

- the answer key for the lab, critique set, and assessments;
- the misconception notes already recorded in the module README;
- the 90-, 60-, and 35-minute teaching profiles;
- guidance on when to reveal or use `boarded`;
- the expected operational interpretation and acceptable alternatives;
- a warning that the data are synthetic design data, not evidence about any hospital;
- handoffs to rates, uncertainty, time, quality improvement, and ethics;
- a short post-session defect log for timing, unclear prompts, software failures, and unexpected learner interpretations.

## Release record

`release.json` contains:

- module identifier and version;
- data identifier and version;
- generator seed and variant;
- row count and column list;
- CSV SHA-256 checksum;
- R and package versions used for the release;
- documentation, code, and data licenses;
- authors and their roles;
- reviewers and completed review roles;
- source document and source date;
- validation results;
- known issues;
- release date.

The runnable release bumps the module from `0.1.0` to `0.2.0`. A changed dataset, answer key, or graded requirement requires a new module patch or minor version according to impact. A released CSV is never silently replaced under the same data version.

## Maturity path

| Stage | Evidence required |
|---|---|
| Pre-alpha | Content record and build specification exist. This is the current stage. |
| Alpha | A clean clone can generate and validate the data, run the lab, create the critique charts, and grade the worked answer. All four review roles are recorded. |
| Beta | The module has been taught once to the target cohort. Timing, defects, learner work, and instructor revisions are recorded without student identifiers. |
| Stable | A second instructor or program has taught the module successfully, no release-blocking defect remains, and adoption instructions have been tested outside the build team. |

This follows the useful lesson-lifecycle pattern used by The Carpentries while keeping OCLC governance small: https://carpentries.github.io/lesson-development-training/instructor/operations.html

## Acceptance tests

The module is ready for an alpha release only when all of these statements are true:

- [ ] A clean clone runs the four documented commands successfully.
- [ ] Two `real` runs with seed 730 produce byte-identical files.
- [ ] The committed CSV has the schema, counts, and values defined in this spec.
- [ ] The `real`, `null`, and `trivial` variants pass their own validation rules.
- [ ] The six `real` teaching checks pass, including the recorded visual review of the hidden second mode.
- [ ] `lab.R` runs from top to bottom without manual repair and produces the four required views.
- [ ] `critique_charts.R` reproduces all three flawed displays.
- [ ] The assessment items and rubric map to C4.1, C4.2, and C4.3.
- [ ] The answer key reproduces the measured results from the committed CSV.
- [ ] Chart examples meet the module's accessibility requirements.
- [ ] No file contains patient data, restricted data, or an undocumented imported source.
- [ ] All module links resolve, the release record is complete, and the checksum matches.
- [ ] An instructor who did not write the code completes a dry run.

## Build order

1. Implement the generator, validator, committed `real` CSV, data specification, and release record.
2. Implement the Tier 1 and Tier 2 lab and confirm every prompt against generated output.
3. Generate the critique set and write repairs in the instructor key.
4. Assemble assessment variants, scoring guidance, and the Tier 3 worked answer.
5. Run data, clinical, content, and independent-instructor reviews.
6. Tag the alpha release, teach the pilot, and record defects for beta.

## Faculty decisions that remain

Two decisions do not block implementation:

1. Name the emergency department operations reviewer and independent dry-run instructor.
2. Decide whether the final course wrapper needs a non-US wording of the emergency department measure example.

The implementation defaults remain R with ggplot2, a visible `boarded` field, and a 90-minute standard teaching profile unless Ali changes them during content review.

## Design precedents

The module combines established patterns without copying a full platform:

- Health Gym for validated synthetic clinical teaching data: https://github.com/NicKuo-ResearchStuff/Health_Gym_AI
- PhysioNet for versioned, reviewed data publication: https://physionet.org/about/
- The Carpentries for open lesson maturity and independent teaching: https://carpentries.org/lesson-development/community-lessons/
- MIT Critical Data for multidisciplinary clinical-data learning: https://criticaldata.mit.edu/

OHDSI and OMOP compatibility can be added when a later module needs longitudinal or multi-table clinical data. Module 04 needs only the seven-column encounter table defined here.
