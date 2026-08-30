# DA-730 Module 01 specification: Encoding and the grammar of graphics

- Specification version: 0.1.0
- Commons release: 0.12.0
- Status: runnable release candidate
- Last updated: 2026-08-29
- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module package: `courses/data-visualization/modules/01-encoding-grammar/`
- Source brief: `docs/curriculum/courses/DA-730/course-spec.md`

## 1. Module identity and place in the course

| Field | Contract |
|---|---|
| Module ID | `oclc-da730-01` |
| Title | Encoding and the grammar of graphics |
| Course position | First of 13 modules |
| Learner time | 7 hours |
| Prerequisite | Week-zero R bridge or equivalent ability to run a script, read a CSV, and find generated files |
| Primary concept | A visualization is a mapping from variables to marks and visual channels, assembled through scales, coordinates, labels, and layers |
| Primary software path | R and ggplot2 |
| Software rule | The competency is tool-independent; an approved alternative must preserve editable source, explicit mappings, and reproducibility |
| Primary case | CMS HCAHPS hospital recommendation results |
| Decision owner | Massachusetts hospital patient-experience director |
| Next module | Module 02, Perception and visual accuracy |

This module establishes the vocabulary used in every later DA-730 module. Learners must be able to describe a chart as a set of choices before they judge perceptual accuracy, choose a chart family, or build a narrative.

## 2. Healthcare decision and audience

### Primary decision

A hospital patient-experience director needs a readable comparison of published Massachusetts HCAHPS recommendation results. The immediate decision is which two results should receive deeper qualitative review. The chart is not used to award a rank, declare a quality failure, or select an intervention.

### Audience needs

The director needs to:

- find a named hospital quickly;
- compare a bounded percentage across several hospitals;
- see the exact result without estimating it from color or area;
- understand which hospitals are included;
- retain source release and measurement-period context; and
- know that the display identifies follow-up questions rather than causes.

### Primary domain instantiation

CMS HCAHPS measure `H_RECMND_DY`, filtered to Massachusetts, provides one nominal facility field, one quantitative percentage, survey-count and response-rate context, reporting dates, source metadata, and explicit unavailable values.

### Approved alternate instantiations

An instructor may swap the primary case without changing the concept core if the alternative satisfies the dataset contract.

1. **Hospital process comparison:** CMS Timely and Effective Care, one consistently defined hospital-level time or percentage measure across a named geographic set. Decision owner: clinical operations director.
2. **County prevention comparison:** CDC PLACES, one current county estimate within a state. Decision owner: population-health director.
3. **Trial portfolio comparison:** ClinicalTrials.gov, one transparent quantitative attribute across a deliberately defined study set. Decision owner: research program director.

Every alternate must publish its own source record, extract, build steps, validation, answer key, expected findings, and interpretation limits. An instructor cannot simply point the current lab at a new file.

## 3. Foundation skill revisited or extended

This course is separate from Foundations 1 and 2, but it assumes those straight-through technical courses or a transition bridge. Module 01 reuses only the technical ability needed to work with a table and script.

It extends that foundation by teaching learners to:

- treat stored data type and analytical role as related but distinct;
- connect a decision question to a variable role;
- connect a variable role to a visual channel; and
- represent the mapping in code and documentation.

The module does not reteach importing data, file paths, data-frame indexing, numeric conversion, or basic R execution. The week-zero bridge supports learners who have not completed the future foundation sequence.

## 4. Assessable learning outcomes

### Competency statement

Given a healthcare question and tabular data, map variables to suitable visual channels and explain why the resulting display has its form.

### Outcomes

By the end of the module, a learner can:

| ID | Outcome | Direct evidence |
|---|---|---|
| M01.1 | Classify variables as nominal, ordered, quantitative, or temporal for a named decision. | `encoding-map.md` and foundation items |
| M01.2 | Identify data, mappings, marks, scales, coordinates, labels, and layers in an existing chart. | Grammar trace and critique response |
| M01.3 | Use aligned position or common-baseline length for a precise quantitative comparison. | `figure.png` and `analysis.R` |
| M01.4 | Separate data encodings from selection rules, annotations, references, and provenance. | Encoding map and source record |
| M01.5 | Diagnose an ordered value encoded only by unordered hue and a precise value encoded only by area. | Critique responses |
| M01.6 | Produce a reproducible, accessible comparison with source context and a bounded decision claim. | Six-file submission package |

## 5. Concept ownership and boundaries

### This module owns

- variable roles for visualization;
- marks and visual channels;
- the terms geometry, aesthetic, scale, coordinates, labels, and layers;
- a grammar trace from data to display;
- the difference between an encoding and an annotation;
- the first use of aligned position for quantitative comparison;
- a complete variable-to-channel justification; and
- reproducible chart source as part of the evidence.

### This module introduces but does not own

- a qualitative accuracy distinction among position, length, angle, area, and color;
- direct labeling and non-color redundancy;
- missing public-reporting values;
- survey-count and response-rate context;
- cautious hospital comparison language; and
- basic source records and checksums.

### Explicitly out of scope

- experimental evidence about graphical perception, owned by Module 02;
- general chart-selection rules, owned by Module 03;
- distributional shape and aggregation, owned by Module 04;
- rates, denominators, patient-mix adjustment, and fairness of comparisons, owned by Module 05;
- confidence intervals, reliability, small numbers, and statistical distinction, owned by Module 06;
- color theory and full accessibility design, owned by Module 07;
- time-series inference, owned by Module 08;
- formal small-multiple design, owned by Module 09;
- map, flow, hierarchy, dashboard, and narrative composition, owned by Modules 10 through 13; and
- HCAHPS instrument or adjustment-method instruction.

An instructor may name these future questions but should not absorb their teaching time into Module 01.

## 6. Lesson sequence and learner time

The module totals 7 hours, or 420 minutes.

| Sequence | Learner time | Activity | Required evidence |
|---|---:|---|---|
| Source and decision opening | 30 min | Inspect CMS rows, identify the grain, review unavailable values, and name the director's decision. | Unit-of-observation statement |
| Tool-independent concept core | 30 min | Learn variable roles, marks, channels, grammar components, and the encoding versus annotation distinction. | Annotated familiar chart |
| Worked HCAHPS example | 60 min | Rebuild a comparison table as a layered chart and trace every choice. | Reference encoding map |
| Tier 1 and Tier 2 guided lab | 90 min | Run the package, identify layers, change marks and channels, and record what becomes easier or harder. | Saved outputs and modification notes |
| Critique studio | 60 min | Diagnose the unordered-color and area-only displays; propose the smallest repair. | Two critique responses |
| Independent exercise | 120 min | Build and document an accessible director-facing comparison. | Six-file package |
| Peer reproducibility and accessibility check | 30 min | Run another learner's script and test the figure, source context, text alternative, and claim boundary. | Verification note and corrections |
| **Total** | **420 min** | | **7 hours** |

### Time-flex rule

If only 5.5 hours are available synchronously, move source inspection and the first script run to required prework. Do not remove the independent exercise, source record, text alternative, or reproducibility check.

## 7. Readings and authoritative sources

### Required before class

1. CMS, Patient survey (HCAHPS) - Hospital dataset page:
   https://data.cms.gov/provider-data/dataset/dgck-syfz
2. Module learner lesson:
   `courses/data-visualization/modules/01-encoding-grammar/README.md`
3. Module data specification:
   `courses/data-visualization/modules/01-encoding-grammar/data-spec.md`

### Required during the module

1. CMS hospital data dictionary:
   https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf
2. ggplot2 book, layers chapter:
   https://ggplot2-book.org/layers
3. W3C Web Accessibility Initiative, complex images tutorial:
   https://www.w3.org/WAI/tutorials/images/complex/

### Instructor reference

1. CMS Provider Data Catalog API documentation:
   https://data.cms.gov/provider-data/docs
2. CMS hospitals measures and current data collection periods:
   https://data.cms.gov/provider-data/topics/hospitals/measures-and-current-data-collection-periods

If any URL changes, the module cannot advance beyond release candidate until the source record and learner links are repaired.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Primary dataset

| Field | Value |
|---|---|
| Publisher | Centers for Medicare & Medicaid Services |
| Dataset | Patient survey (HCAHPS) - Hospital |
| Dataset ID | `dgck-syfz` |
| CMS release | 2026-08-13 |
| CMS modified | 2026-07-22 |
| Coverage | 2024-10-01 through 2025-09-30 |
| Filter | Massachusetts and `H_RECMND_DY` |
| Extract rows | 65 |
| Reported rows | 56 |
| Unavailable rows | 9 |
| Extract checksum | `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74` |
| Original CMS file | `HCAHPS-Hospital.csv`, 105,461,119 bytes, SHA-256 `b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc` |
| Rights | U.S. government public-reporting data in the public domain; CMS attribution requested; no implied federal endorsement |
| Patient records | None |

### Teaching purpose

The file supports nominal-to-position, quantitative-to-position, direct-label, reference-line, and provenance decisions in a healthcare comparison. Completed surveys provide a deterministic readability rule and a reason to distinguish contextual variables from visually encoded measures. Unavailable rows keep source handling visible without making missing-data methods the lesson.

### Dataset substitution contract

A substitute dataset must contain:

- one nominal identity field with at least 10 readable groups;
- one consistently defined quantitative measure suitable for comparison;
- one contextual field that could be encoded but does not need to be;
- provenance and measurement-period fields;
- at least one source limitation that affects the claim;
- enough spread to make channel choice visible;
- a lawful public or synthetic release path; and
- no patient-level identifiers or protected health information.

The preferred assessed view has 10 to 30 marks. Larger source files are allowed, but the learner view must have a transparent selection or grouping rule.

## 9. Data dictionary and analytic structure

The canonical field-level dictionary is in `data-spec.md`. The required analytic structure is:

| Property | Contract |
|---|---|
| Unit of observation | One hospital-measure result |
| Grain | Facility by measure by measurement period |
| Key | `facility_id` within this one-measure state extract |
| Main category | `facility_name` |
| Main quantitative result | `recommend_percent` |
| Context | `completed_surveys`, `response_rate_percent` |
| Missingness signal | `value_status` and three retained CMS footnote fields |
| Provenance | `measure_id`, `period_start`, `period_end`, `cms_release_date` |
| Patient-level inference | Not permitted |

### Reference view

The worked view includes the 15 reported hospitals with the largest completed survey counts. Ties use ascending facility ID. The chart sorts these 15 hospitals by recommendation percentage for reading. Selection and display order are separate transformations and must be documented separately.

## 10. Worked example and instructor walkthrough

### Worked question

How can a patient-experience director see the spread in recommendation results among the 15 Massachusetts hospitals with the most completed surveys in this CMS release?

### Walkthrough sequence

1. **Open the source table.** Name the unit of observation and identify why facility ID is nominal even when it looks numeric.
2. **State the decision.** Choose results for deeper review, not declare hospital quality.
3. **Classify the fields.** Hospital is nominal; recommendation percent is quantitative; completed surveys are quantitative context; dates are temporal provenance.
4. **Choose the primary channel.** Place recommendation percent on a common x scale because the task requires comparison.
5. **Choose the category channel.** Place hospital labels on aligned y rows for lookup.
6. **Choose the mark.** Use a point for each hospital result.
7. **Add a reference layer.** Use the unweighted median across all 56 reported Massachusetts hospitals as orientation, not as a target.
8. **Add a segment layer.** Connect the reference to each point so direction and distance are visible.
9. **Add a text layer.** Repeat exact percentages without requiring position estimates.
10. **Add provenance labels.** Name CMS, release date, measure period, and selection rule.
11. **Write the grammar trace.** Make every visible element accountable to the decision.
12. **Bound the claim.** State what follow-up the display supports and what it cannot establish.

### Expected findings

The pinned data produce:

- 56 reported and 9 unavailable Massachusetts results;
- a reported statewide range from 42% to 93%;
- an unweighted median of 70.5% across reported hospitals;
- a 15-hospital worked view selected by completed survey count; and
- a 52% to 86% range within the worked view.

These are descriptive facts about the published release. They are not adjusted comparisons performed by the learner and do not establish causes or statistical difference.

## 11. Guided practice

### Tier 1: Run and observe

Learners run `lab.R`, then:

1. match every row of `encoding-map.csv` to the chart;
2. circle the mark that represents one hospital;
3. identify which direction carries category and which carries quantity;
4. identify the reference, segment, point, text, and caption layers; and
5. explain why the CMS release date belongs in a caption rather than mark color.

### Tier 2: Modify and explain

Learners work in a copy of `lab.R` and change only one decision at a time:

1. replace the point with a common-baseline bar;
2. remove direct labels;
3. map completed surveys to point size; and
4. restore the reference design after comparing the alternatives.

For every change, learners answer:

- Which mark or channel changed?
- Which task became easier?
- Which task became harder?
- Did the claim or audience change?
- Would you keep the change for the director?

### Guided-practice completion rule

Learners do not need to prefer the reference chart. They must identify the changed grammar component and defend their decision using the audience's task.

## 12. Independent exercise

Each learner creates one comparison for the named patient-experience director using at least 10 reported hospitals.

The learner may:

- use the worked 15-hospital view;
- define another Massachusetts subset with a rule stated before interpreting the results; or
- use all 56 reported rows if the figure remains readable.

The learner must choose two results for follow-up and write a distinct question for each. The note may recommend more analysis. It may not infer a cause from the plotted percentage.

### Transfer prompt

After submitting the primary display, the learner explains how the encoding map would change if the decision became monitoring one hospital over eight quarters. This response prepares the temporal work in Module 08 without teaching time-series methods early.

## 13. Visualization and communication requirements

The assessed figure must:

- use aligned position or common-baseline length for `recommend_percent`;
- preserve hospital identity as readable text;
- display the percent unit;
- name the exact HCAHPS construct;
- disclose the subset or row-selection rule;
- identify the CMS source, release date, and measurement period;
- distinguish any reference from a formal target;
- remain interpretable without color;
- fit an ordinary document or learning-management-system page; and
- have an 80 to 150 word text alternative.

The figure may use color, shape, size, facets, or annotation when each addition has a named purpose. Decoration does not satisfy the mapping requirement.

## 14. Exact submission package

The assessed folder is:

```text
module-01/
  encoding-map.md
  analysis.R
  figure.png
  source-record.yml
  alt-text.md
  decision-note.md
```

File contracts are defined in `assessment.md`. Filenames are exact so peer and instructor checks can run without searching or renaming.

### Reproducibility layout

The learner may place the source CSV beside `analysis.R` or in a documented relative `data/` folder. Absolute user paths are not allowed. The script must stop with a useful message when the input is missing or structurally wrong.

## 15. Rubric and pass conditions

| Criterion | Points |
|---|---:|
| Source and provenance | 15 |
| Encoding map | 20 |
| Reproducible analysis | 20 |
| Figure | 20 |
| Decision note | 15 |
| Accessibility and text alternative | 10 |
| **Total** | **100** |

The pass mark is 75 points. These conditions are also mandatory:

1. code runs and creates the submitted figure;
2. the quantitative comparison uses aligned position or common-baseline length;
3. source, release, period, measure, and subset are accurate; and
4. the decision note does not claim causation, statistical difference, or complete hospital quality.

If a mandatory condition fails, the package is returned for correction regardless of total points.

### Checkpoint contribution

The Module 01 figure, encoding map, source record, and decision note may be revised for the week-3 visual reasoning checkpoint. Module 03 will add formal chart-selection justification, and Modules 05 and 06 will later add measure and uncertainty judgment.

## 16. Common errors, failure modes, and interventions

| Failure | Likely misconception | Intervention |
|---|---|---|
| Facility ID is averaged or placed on a numeric scale | Storage type is confused with analytical role. | Ask what arithmetic on two facility IDs would mean. |
| Percent is encoded only by qualitative hue | Ordered data are disconnected from channel semantics. | Remove the legend and ask learners to order three marks. |
| Percent is encoded only by circle area | Visual prominence is confused with comparison accuracy. | Estimate two close values, then align them on a shared axis. |
| Completed surveys are called the number of patients served | The field name is being overinterpreted. | Restore the exact CMS definition and distinguish respondents from the hospital population. |
| Unavailable rows are dropped without a count | Filtering is treated as invisible. | Require 65 source, 56 reported, and 9 unavailable in the source record. |
| The 15 hospitals are called peers | A readability selection is mistaken for comparability. | Separate selection rule, display order, and analytic peer definition. |
| The median is labeled a benchmark or target | A descriptive statistic is mistaken for an external standard. | Ask who set the target and where it appears in the source. |
| A polished figure has no grammar trace | Aesthetic judgment is substituting for accountable reasoning. | Grade `encoding-map.md` before figure style. |
| Code works only on the learner's computer | The output is not reproducible. | Require relative paths and a peer clean run. |
| AI-written text adds unsupported survey claims | Fluency is mistaken for verification. | Require claim-by-claim source checking and disclosure. |

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Required information cannot depend on color alone.
- Text must remain readable at ordinary document size.
- Direct values or a companion table must make exact results recoverable.
- The text alternative must state the chart structure, measure, period, pattern, range, reference, and decision limit.
- The title and labels must use plain healthcare language rather than grammar jargon.

### Equity

The primary file does not contain race, ethnicity, language, disability, payer, or other patient subgroup fields. Learners must not claim that the comparison demonstrates equitable or inequitable experience. They may identify the absence of subgroup evidence as a follow-up need.

Hospital omission is also visible. Nine Massachusetts facilities have unavailable results in this release. They remain in the teaching extract and source count even though they cannot appear in the quantitative chart.

### Privacy

The CMS file contains aggregate hospital public-reporting data and no patient-level records. Learners may not join it to private records for this public module. No protected health information may be added to the submission.

### Responsible claims

Allowed:

- describe the published percentages;
- identify displayed high and low results;
- describe the selection rule;
- propose questions for deeper review; and
- note missing information.

Not allowed:

- claim that the chart proves one hospital provides better overall care;
- infer the cause of a difference;
- call a visible gap statistically significant;
- treat completed surveys as the number of patients represented by the hospital; or
- treat the unweighted statewide median as a CMS target.

## 18. AI and agent policy

AI assistance is allowed for:

- explaining unfamiliar R syntax;
- debugging an error;
- proposing alternative encodings;
- checking whether code and the encoding map agree; and
- editing a draft text alternative for clarity.

AI assistance cannot replace:

- inspection of the CMS source record;
- verification of fields, release, period, and row counts;
- the learner's mapping decisions;
- execution of the submitted code;
- accessibility inspection; or
- accountability for claims.

`decision-note.md` must disclose the tool, purpose, adopted change, and verification. `No AI assistance used.` is a complete disclosure when true. Fabricated citations, unrun code, or invented HCAHPS methods trigger correction and academic-policy handling under the official course rules.

## 19. Answer key and instructor materials

The instructor key is `courses/data-visualization/modules/01-encoding-grammar/instructor-notes.md`.

It contains:

- verified environment and expected results;
- the seven-hour facilitation sequence;
- the reference grammar trace;
- answers for both critique charts;
- a defensible decision-note example;
- a text-alternative example;
- common misconceptions and interventions;
- point-level grading guidance;
- accessibility checks;
- a short-time adaptation; and
- the required human review roles.

The learner README contains the 20-minute concept core, runnable steps, tiered lab directions, interpretation boundaries, accessibility requirements, and AI policy.

## 20. Runnable acceptance checks

### Data build

From the module directory:

```powershell
Rscript build_hcahps.R
```

Pass condition: the script verifies CMS metadata release `2026-08-13` and modified date `2026-07-22`, receives 65 filtered rows, and recreates the committed extract.

### Data validation

```powershell
Rscript validate_hcahps.R
```

Pass condition: 15 of 15 checks pass.

### Lab execution

```powershell
Rscript lab.R
```

Pass condition: the peer table, encoding map, and layered comparison are created without manual edits.

### Critique execution

```powershell
Rscript critique_charts.R
```

Pass condition: both intentionally flawed critique charts are created.

### Visual inspection

An instructor confirms that:

- the reference line and all 15 points render;
- labels do not overlap enough to block identification;
- direct percentages are readable;
- the subtitle identifies the selection and reference;
- the caption shows source, release, and period; and
- both critique charts visibly express the intended failure.

### Repository checks

Before release:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
git diff --check
```

### Clean-run review

Before alpha, an independent instructor runs the four scripts from a clean checkout, follows the learner README without private guidance, and records any missing instruction or environment assumption in `release.json`.

## 21. Release status, reviewers, version, and known issues

### Release identity

| Item | Value |
|---|---|
| Module version | 0.1.0 |
| Commons release | 0.12.0 |
| Status | Runnable release candidate |
| Release date | 2026-08-29 |
| Technical validation | Complete |
| Human review | Pending |

### Maturity gate

The module is a runnable release candidate because the source is pinned, the data pipeline recreates the extract, the validator passes, the lab and critiques run, the assessed package is exact, and instructor answers exist.

It becomes alpha only after all four human roles sign off:

1. visualization faculty and source fidelity;
2. clinical or patient-experience content;
3. accessibility; and
4. independent teachability from a clean checkout.

It becomes beta only after a taught pilot and documented revision. It becomes stable only after successful reuse by a second instructor or program under the course-level maturity rules.

### Known issues

- Human reviews are pending.
- The 15-hospital selection is a readability rule, not a peer-group definition.
- The live CMS API will eventually move to a later release. The build intentionally stops until that change is reviewed and versioned.
- HCAHPS methodology, adjustment, response bias, reliability, and inference remain outside Module 01.
- The reference environment is Windows. The R scripts use portable paths, but macOS and Linux execution still need an independent clean-run record.

## Handoff to Module 02

Module 01 ends with a defensible mapping, not proof that every mapping is equally easy to read. Module 02 begins with the same HCAHPS comparison and asks learners to predict and test which channels support more accurate judgments. The explicit encoding map becomes the input to that perceptual audit.

The next build unit is:

`docs/curriculum/courses/DA-730/modules/02-perception-accuracy-spec.md`
