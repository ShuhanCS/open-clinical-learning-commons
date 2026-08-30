# DA-730 Module 04 specification: Distributions versus summaries

- Specification version: 0.4.0
- Commons release: 0.15.0
- Status: runnable release candidate
- Last updated: 2026-08-29
- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module package: `courses/data-visualization/modules/04-distributions-vs-summaries/`
- Original build record: `docs/specs/2026-08-15-ali-goff-module-04-build-spec.md`

## 1. Module identity and place in the course

| Field | Contract |
|---|---|
| Module ID | `oclc-da730-04` |
| Title | Distributions versus summaries |
| Course position | Fourth of 13 modules |
| Learner time | 8 hours |
| Prerequisites | Modules 01 through 03 and basic summary statistics |
| Primary concept | A correct summary can hide a decision-relevant tail, subgroup, or second process |
| Primary software path | R and ggplot2 |
| Primary case | Synthetic emergency-department length of stay anchored to a public CMS hospital-level median |
| Decision owner | Emergency-department operations leader and hospital patient-flow team |
| Next module | Module 05, Rates, denominators, and adjustment |

Module 03 selected a plausible form from the question and available structure. Module 04 asks whether that structure has been summarized too aggressively. The learner must decide when a center is sufficient, when a distribution is necessary, which group or care process is hidden, and what decision changes when the hidden structure becomes visible.

The portable outcome is not a preferred chart. It is the ability to test whether a summary preserves the patient groups, time pattern, tail, and operational process needed for a decision.

## 2. Healthcare decision and audience

### Primary decision

An emergency department has a synthetic fast-track pathway. Department-wide mean length of stay changes little across 2026, while the typical discharged visit improves and the longest admitted stays worsen as boarding becomes more common.

The emergency-department operations leader must decide whether to:

- expand fast track;
- change staffing;
- investigate inpatient boarding and bed capacity;
- revise the monitoring display;
- maintain current operations; or
- request better evidence before acting.

The learner determines what the mean, median, 90th percentile, threshold share, pooled histogram, and group-specific distribution each reveal or conceal.

### Decision owners

The primary audience is deliberately cross-functional:

- emergency-department clinical and operational leadership protects patient flow within the department;
- the chief operating officer allocates hospital capacity and attention;
- the patient-flow and bed-management team owns the inpatient bottleneck;
- analysts maintain definitions, source records, and reproducible metrics; and
- patients experience the waits represented by the distribution.

A useful recommendation names which team should act and which process it should investigate. "The distribution is skewed" is an analytic observation, not yet a decision.

### Decision boundary

The module supports a decision inside a synthetic case. It may not:

- claim that a real hospital improved or deteriorated;
- claim that fast track or boarding caused an outcome;
- claim patient harm from the simulated length-of-stay values;
- use the public CMS hospital median as a patient-level distribution or benchmark;
- interpret synthetic acuity or age patterns clinically; or
- recommend staffing or capacity levels for a real institution.

## 3. Foundation skill revisited or extended

The module assumes learners can:

- identify quantitative, categorical, and time variables;
- state what one row represents;
- calculate or interpret mean, median, proportion, and percentile;
- distinguish comparison, distribution, time, and lookup tasks;
- run a supplied R script;
- interpret an axis and legend; and
- record source, transformation, and decision context.

It extends those skills through a distribution audit:

1. **Center:** What does the mean or median summarize?
2. **Shape:** Is the distribution symmetric, skewed, multimodal, bounded, censored, or truncated?
3. **Tail:** Which threshold or high percentile represents a consequential experience?
4. **Groups:** Does pooling hide a patient group, service, disposition, or care process?
5. **Time:** Do opposing changes cancel in a pooled annual or monthly summary?
6. **Denominator:** How many observations support each group and period?
7. **Decision:** What action changes when the structure is revealed?
8. **Failure:** Is the available grain sufficient to answer the distribution question?

The learner should not replace one automatic rule with another. Skew does not make the median universally correct, and a full distribution is not always the clearest display.

## 4. Assessable learning outcomes

### Competency statement

Determine whether a summary statistic faithfully represents a distribution, choose a display that exposes consequential structure, and state what healthcare decision changes.

### Outcomes

| ID | Outcome | Direct evidence |
|---|---|---|
| M04.1 | Explain why every summary is a lossy compression and name what a specific summary discards. | Distribution audit A1 to A3 |
| M04.2 | Diagnose skew, a consequential tail, unequal groups, multiple modes, and opposing time trends. | Audit, lab, and critique |
| M04.3 | Select mean, median, quantile, or threshold share based on the decision rather than habit. | Matrix and decision note |
| M04.4 | Choose and interpret a histogram, density, box plot, violin, ECDF, or coordinated time summary. | Tier 2 work and final figures |
| M04.5 | Disaggregate a pooled view by disposition and boarding to identify a care-process mechanism. | `analysis.R` and `distribution.png` |
| M04.6 | Distinguish patient-level variation from precision of an estimated mean. | C1 critique |
| M04.7 | Correct an average of averages using counts or separate groups. | C3 critique and audit |
| M04.8 | Report a null or trivial pattern without manufacturing an operational effect. | A4, A7, and variant analysis |
| M04.9 | Separate the public CMS hospital-level anchor from synthetic encounter assumptions. | `source-record.yml` and decision note |
| M04.10 | Make a bounded operational recommendation for a named owner. | `decision-note.md` |

## 5. Concept ownership and boundaries

### This module owns

- summaries as lossy compression;
- mean and median as decision-dependent centers;
- quantiles and decision-relevant threshold shares;
- skew and consequential tails;
- multimodality and hidden processes;
- unequal group sizes and pooled summaries;
- average-of-averages errors;
- disaggregation by patient group or care process;
- histograms, density views, box plots, violin plots, and empirical cumulative distribution functions as distribution forms;
- the difference between patient-level variation and standard error; and
- honest null and trivial-effect reporting.

### This module introduces but does not own

- denominator stability and crude versus adjusted rates;
- confidence intervals and small-number uncertainty;
- accessibility through color plus line type;
- time-series signal interpretation;
- small multiples;
- dashboard metric selection; and
- executive narrative.

These ideas are used only enough to support the distribution decision. Modules 05 through 13 deepen them.

### Explicitly out of scope

- causal evaluation of fast track or boarding;
- real emergency-department performance benchmarking;
- patient-level calibration from the CMS source;
- staffing or capacity estimation;
- inferential modeling of length of stay;
- censoring, competing events, or survival methods;
- formal process-control rules;
- acuity-based clinical inference from the synthetic file;
- missing-data modeling; and
- a universal preference for means, medians, box plots, or full distributions.

## 6. Lesson sequence and learner time

The module totals 8 hours, or 480 minutes.

| Sequence | Time | Activity | Required evidence |
|---|---:|---|---|
| Operational decision opening | 30 min | Predict what one monthly mean would imply for the chief operating officer. | Initial decision and failure statement |
| Distribution concept core | 60 min | Study center, shape, tail, groups, time, and denominator. | Annotated distribution audit |
| Public source and synthetic boundary | 45 min | Inspect the full OP_18b extract and trace the 148-minute anchor into the generator. | Provenance note |
| Guided runnable lab | 90 min | Build the mean, histogram, disposition density, and four-metric view. | Four figures and monthly table |
| Tier 2 modification | 60 min | Compare box plot, group split, boarding split, log scale, ECDF, and percentile choices. | Six modification notes |
| Critique studio | 45 min | Repair standard-error bars, a truncated mean, and an average of averages. | Three critique responses |
| Independent assessment | 120 min | Complete the seven-part submission across recognition, application, and transfer. | Assessment package |
| Peer run and revision | 30 min | Reproduce figures, audit the source boundary, and inspect accessibility. | Verification note and corrections |
| **Total** | **480 min** | | **8 hours** |

### Short-time path

For a 90-minute synchronous session, keep the decision opening, four Tier 1 outputs, boarding split, box-plot comparison, and decision rewrite. The remaining work stays asynchronous. A 35-minute version is a demonstration and does not by itself provide enough practice for competency credit.

## 7. Authoritative readings and public clinical sources

### Required readings

1. Weissgerber, T. L., Milic, N. M., Winham, S. J., and Garovic, V. D. (2015). Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm.
   https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128
2. Streit, M., and Gehlenborg, N. (2014). Bar charts and box plots.
   https://doi.org/10.1038/nmeth.2807
3. NIST/SEMATECH e-Handbook of Statistical Methods, Histogram.
   https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm

### Optional extension

Rousselet, G. A., Pernet, C. R., and Wilcox, R. R. (2017). Beyond differences in means.

Open-access manuscript: https://eprints.gla.ac.uk/141172/

DOI: https://doi.org/10.1111/ejn.13610

### Required public clinical source

CMS, Timely and Effective Care - Hospital:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

CMS metadata endpoint:

https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items/yv7e-xc69

CMS hospital data dictionary:

https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf

### Reading standard

Learners identify what the source observed, what display problem it addresses, one defensible implication, and one limit. They do not turn a paper example into a universal prohibition. They also distinguish the CMS hospital-level median from the synthetic patient-level teaching distribution.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Original public CMS file

| Field | Value |
|---|---|
| Publisher | Centers for Medicare & Medicaid Services |
| Dataset | Timely and Effective Care - Hospital |
| Dataset ID | `yv7e-xc69` |
| Release | 2026-08-13 |
| Modified | 2026-07-22 |
| Full rows | 138,084 |
| Full columns | 16 |
| Full file bytes | 34,150,899 |
| Full file SHA-256 | `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516` |
| Access | Public U.S. government provider-reporting data |

The build script pins the exact full CSV distribution URL and refuses to rebuild if the dataset release or modified date changes.

### Complete national OP_18b extract

| Field | Value |
|---|---|
| Path | `data/cms_ed_op18b_2026.csv` |
| Measure | `OP_18b` |
| Grain | One hospital result row |
| Coverage | 2024-10-01 through 2025-09-30 |
| Total rows | 4,658 |
| Reported rows | 4,081 |
| Unavailable rows | 577 |
| Reported median | 148 minutes |
| Reported range | 42 to 413 minutes |
| Checksum | `c9603109d4ea251b8096a655c27ad42cd6313bdb1309999bee3eb37ce79ec67d` |

Every national OP_18b row is retained, including unavailable results, samples, and footnotes. The extract is not a selected convenience sample.

### Synthetic encounter release

| Field | Value |
|---|---|
| Path | `data/ed_los_2026.csv` |
| Data ID | `oclc-ed-los-2026` |
| Data version | 0.2.0 |
| Grain | One synthetic emergency-department encounter |
| Rows | 8,392 |
| Variant | `real` |
| Seed | 730 |
| Checksum | `27c1c0feed8beb4ab0ac6dc77eaa3d1ed95c07b89f52f4881c25954ba43fbc55` |

### Calibration boundary

The median of 4,081 reported OP_18b hospital results is 148 minutes. The generator centers the synthetic discharged pathway on that value. In the real variant, the discharged median moves symmetrically from 179 minutes in January to 117 minutes in December.

CMS does not provide the patient-level distributions used here. The following are synthetic teaching assumptions:

- monthly discharged change;
- admission counts and disposition mix;
- non-boarded and boarded medians and spreads;
- boarding prevalence;
- patient-level tails and modes;
- arrival dates;
- acuity and age composition; and
- the relationship among all those fields.

### Rights and teaching use

The CMS data are public government reporting data. The original instructional metadata and synthetic release use the repository's stated documentation and data terms. Attribution must not imply federal endorsement. The full source record is `source-record.yml`.

## 9. Data dictionary and expected analytic structure

### CMS calibration fields

| Field | Meaning |
|---|---|
| `facility_id` | CMS hospital identifier |
| `facility_name` | Published facility name |
| `city`, `state` | Published location fields |
| `measure_id`, `measure_name` | `OP_18b` and its full definition |
| `score_min` | Reported hospital median in minutes; blank if unavailable |
| `value_status` | `reported` or `not_available` |
| `sample`, `footnote` | CMS source context retained as text |
| `period_start`, `period_end` | ISO coverage dates |
| `cms_release_date` | Pinned source release |
| `source_url` | Full landing-page URL |

### Synthetic encounter fields

| Field | Type | Contract |
|---|---|---|
| `encounter_id` | string | Unique synthetic ID `ED26-00001` format |
| `arrival_date` | date | Date in calendar year 2026 |
| `esi` | integer | Synthetic Emergency Severity Index 1 through 5 |
| `age_group` | category | `18-39`, `40-64`, `65-79`, or `80+` |
| `disposition` | category | `admitted` or `discharged` |
| `boarded` | integer | 0 or 1; boarded encounters are admitted |
| `los_min` | integer | Positive synthetic arrival-to-departure length of stay in minutes |

### Reference composition

- 6,462 discharged encounters;
- 1,930 admitted encounters;
- 540 boarded admitted encounters;
- 66 ESI 1 encounters; and
- no missing encounter fields.

### Derived monthly metrics

For each arrival month:

- `mean_min`;
- `median_min`;
- `p90_min`; and
- `over_8h_pct`, the percentage with `los_min > 480`.

### Variant contract

| Variant | Pattern | Learner responsibility |
|---|---|---|
| `real` | Stable pooled mean, improving discharged pathway, worsening upper tail, and growing boarding | Find the consequential hidden process |
| `null` | January and December summaries stay inside null thresholds | Report absence without searching for a favorable result |
| `trivial` | A small detectable shift remains inside operational thresholds | Separate statistical detection from importance |

The variant name does not appear inside the generated CSV. The instructor records variant and seed separately.

## 10. Worked example and instructor walkthrough

### Opening view

Show only the monthly mean. It moves from 217.9 minutes in January to 212.5 minutes in December, a 2.5 percent decrease. Ask the learner what decision this supports and what the mean cannot show.

### Add the pooled distribution

The pooled histogram shows strong right skew. The overall mean is 215.2 minutes, the median is 169 minutes, and their ratio is 1.273. The distribution reveals long waits but does not clearly identify the care process producing them.

### Disaggregate by disposition

The disposition density separates a shorter discharged process from the admitted process. Admitted encounters contain a second mode near the 782-minute boarded median. Pooling weakens that mode because discharged encounters outnumber admitted encounters by 3.348 to 1.

### Compare monthly summaries

| Measure | January | December | Change |
|---|---:|---:|---:|
| Mean | 217.9 min | 212.5 min | -2.5% |
| Median | 200.0 min | 134.0 min | -33.0% |
| 90th percentile | 306.1 min | 536.8 min | +75.4% |
| Share over 8 hours | 2.4% | 10.5% | +8.0 percentage points |

The mean and median emphasize the majority discharged pathway. The 90th percentile and threshold share reveal worsening long waits.

### Trace the process

- discharged mean falls from 190.3 to 124.4 minutes;
- admitted mean rises from 310.3 to 508.8 minutes;
- boarded admitted median is 782 minutes;
- non-boarded admitted median is 252 minutes; and
- boarding prevalence rises by 36.3 percentage points.

### Rewrite the decision

The supported synthetic-case recommendation is to protect fast-track gains while assigning a separate boarding and inpatient-capacity investigation. The display must not call the year an overall success based only on center statistics.

### Source walkthrough

End by showing that the 148-minute anchor came from all reported hospital OP_18b values, while every patient-level shape and process was generated. This distinction is part of the assessed competency.

## 11. Guided practice

### Tier 1: Run and observe

Learners run `lab.R` and answer:

1. What does the monthly mean suggest?
2. What patient experience appears in the pooled histogram?
3. What care process remains hard to identify when pooled?
4. What changes after separating disposition?
5. Which monthly measures describe center and which describe the tail?
6. What operational decision changes?

### Tier 2: Modify and compare

Learners make six changes:

1. Replace the density with a box plot and identify the missing mode information.
2. Split monthly mean by disposition and explain the cancellation.
3. Split admitted encounters by boarding and identify the second process.
4. Use a log scale and explain the changed reading task.
5. Build an ECDF and calculate the share above 480 minutes.
6. Replace the 90th with the 95th percentile and explain why the metric should be chosen before inspecting the result.

For each change, the learner records the question, gained information, lost information, audience effect, and decision consequence.

### Tier 3: Author and defend

The learner builds one distribution figure and one coordinated monthly summary without starter plotting code. Multiple forms can earn full credit. The learner must justify the chosen statistic and form against a plausible alternative.

### Guided source task

Learners inspect the calibration extract and report:

- total, reported, and unavailable rows;
- measure definition and unit;
- coverage and release;
- median and range among reported hospital values;
- why the median of hospital medians is not a national patient median; and
- which generator parameters are and are not calibrated.

## 12. Independent exercise

### Prompt

Prepare an emergency-department distribution brief for the chief operating officer. The instructor assigns the real, null, or trivial variant without placing the label in the data file.

The learner must:

1. inspect the source and synthetic boundary;
2. verify grain, dates, groups, and length-of-stay values;
3. calculate center, tail, threshold, and group metrics;
4. decide whether the expected hidden process is present;
5. build a distribution view;
6. build a coordinated monthly-metrics view;
7. compare one reasonable alternative;
8. write accessible alternatives;
9. make a bounded recommendation; and
10. record reproducibility and AI assistance.

### Recognition and application questions

The exact A1 through A9 prompts are in `assessment.md`. They cover:

- same mean with stable or opposing processes;
- box plots and hidden modes;
- facts omitted by mean bars;
- trivial but detectable change;
- large multi-group distributions;
- similar medians with different tails;
- honest null reporting;
- better medians with more long-wait complaints; and
- a board decision brief.

### Failure conditions

The learner must pause the distribution claim when:

- only an aggregate center is available;
- row grain mixes patients, visits, periods, or facilities;
- a subgroup cannot be reconstructed;
- censoring or truncation is material but undocumented;
- measurement definitions change across periods; or
- the public aggregate is being treated as patient-level data.

## 13. Visualization and communication requirements

### Required `distribution.png`

The figure must:

- show distributional shape or cumulative probability;
- identify the relevant group or care process;
- use length-of-stay minutes;
- make the long tail or second mode available;
- disclose any axis limit or log transformation;
- report group counts directly or through a companion;
- avoid calling long waits removable outliers without process review;
- remain interpretable without color; and
- state that the encounters are synthetic.

### Required `monthly-metrics.png`

The figure must:

- compare center and tail-sensitive measures across ordered months;
- identify which panels use minutes and which use percent;
- use honest scales;
- preserve the 480-minute threshold definition;
- make January and December values retrievable;
- avoid claiming a process-control signal; and
- name the operational question.

### Statistic-selection rules

- Use the mean for total burden, staffing hours, capacity, or cost when its assumptions fit.
- Use the median for a typical experience when the center answers the decision.
- Use a high percentile when the service decision concerns most encounters.
- Use a threshold share when a named limit has operational or patient meaning.
- Use the full or group-specific distribution when shape, tail, or multiple processes change the decision.

### Accessibility

Line type or direct text repeats color distinctions. Exact metrics remain available in a table. Alt text states the finding, group, time direction, and decision consequence rather than listing decorative properties.

## 14. Exact submission package and filenames

```text
module-04/
  distribution-audit.md
  analysis.R
  figures/
    distribution.png
    monthly-metrics.png
  source-record.yml
  alt-text.md
  decision-note.md
```

### `distribution-audit.md`

Include:

- answers A1 through A8;
- row grain and source boundary;
- center, shape, tail, group, time, denominator, decision, and failure analysis;
- assigned variant and seed;
- chosen statistic and form;
- rejected alternative; and
- no-claim conditions.

### `analysis.R`

The script must:

1. use relative paths;
2. check required fields and positive length of stay;
3. parse dates;
4. report counts by disposition, boarding, acuity, and month;
5. calculate mean, median, 90th percentile, 95th percentile, and over-eight-hour share;
6. compare January with December;
7. produce both exact PNG filenames; and
8. print a reproducibility summary.

### `source-record.yml`

Copy the module source record and add assigned file, variant, seed, analysis date, transformations, output paths, row counts, and checksums. Keep the public calibration and synthetic assumptions separate.

### `alt-text.md`

Provide a separate 80 to 150 word alternative for each PNG. Include the direction and approximate magnitude of the key difference, relevant group, and operational implication.

### `decision-note.md`

Use:

```markdown
# Decision note

## Decision owner and choice
## Center, tail, and hidden process
## Selected statistic and displays
## Rejected alternative
## Patient or process consequence
## Source and synthetic boundary
## What the evidence cannot establish
## Reproducibility check
## AI assistance disclosure
```

## 15. Rubric and pass conditions

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Distribution audit | 25 | Center, shape, tail, groups, time, denominator, hidden or absent process, and decision consequence |
| Reproducible analysis | 20 | Relative paths, checks, declared variant and seed, exact summaries, and two figures |
| Display and statistical fit | 20 | Statistic and display match the decision and are compared with a reasonable alternative |
| Decision note and claim boundary | 15 | Named owner, supported action, process consequence, and explicit limit |
| Source and provenance | 10 | CMS anchor, synthetic assumptions, transformations, rights, and checksums are accurate |
| Accessibility and alternatives | 10 | Honest scales, units, non-color cues, readable labels, and complete alt text |
| **Total** | **100** | |

The pass mark is 75. All five conditions are mandatory:

1. code runs and writes both figures;
2. the learner reports the assigned pattern without assuming a result;
3. the statistic and display expose or honestly dismiss the decision-relevant structure;
4. the source record separates public hospital-level calibration from synthetic encounter assumptions; and
5. the decision note avoids real-hospital, patient-harm, benchmark, and causal claims.

### Week-3 checkpoint contribution

The Module 04 distribution audit can enter the week-3 visualization judgment dossier as evidence of disaggregation and summary selection. Module 06 formally closes the checkpoint after denominators and uncertainty are added.

## 16. Common errors, failure modes, and interventions

| Failure | Likely misconception | Intervention |
|---|---|---|
| Median is always called better for skewed data | Statistic is chosen by shape alone. | Ask a capacity question where total burden requires the mean. |
| Every final chart shows every point | Completeness is confused with usability. | Give 50,000 rows and require a decision-sized form. |
| Box plot is treated as full distribution | Quartiles are confused with density shape. | Compare the admitted box plot with boarding-specific densities. |
| Tail is called outliers and deleted | A distinct care process is mistaken for error. | Trace boarded encounters before any exclusion. |
| Pooled mean is called stable care | Opposing processes are ignored. | Split by disposition and time. |
| Standard-error bars describe patient experience | Estimate precision is confused with variation. | Compare standard deviation, standard error, and raw distribution. |
| Two group means are averaged equally | Group sizes are ignored. | Recalculate a count-weighted mean and retain group views. |
| Highest percentile is selected after plotting | Result-driven metric choice occurs. | Name the operational threshold before seeing the result. |
| Null variant receives a deterioration story | Expected narrative replaces evidence. | Grade honest absence and a monitoring plan. |
| Small p-value triggers a major action | Detection is confused with importance. | Compare absolute minutes, percentile change, and threshold share. |
| CMS anchor is described as patient data | Aggregate and individual grain are conflated. | Trace one CMS row and one synthetic row side by side. |
| Synthetic pattern is called a benchmark | Plausible scale is confused with representative performance. | Restate exactly which single parameter is calibrated. |
| AI invents a clinical mechanism | Fluent explanation outruns generated fields. | Require a row, transformation, or named unresolved hypothesis. |

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Color is paired with line type, direct text, grouping, or separate panels.
- Axis units and any transformed scale are explicit.
- Figure titles state the reader task or finding in plain language.
- Exact values remain available through the monthly metrics CSV or a companion table.
- Two complete text alternatives are required.
- Small groups are labeled with counts.
- Output remains readable at ordinary document size and with zoom.

### Equity

The synthetic age and acuity fields are not clinically calibrated. Learners must not infer that a real age or acuity group waits longer. The module still teaches an equity-relevant habit: a majority summary can hide a smaller group that experiences a different process.

An alternate real aggregate source must preserve subgroup definitions, missingness, suppression, sampling, and denominator context. A disparity claim requires appropriate population and uncertainty evidence beyond this module.

### Privacy

Both committed datasets are public aggregate data or synthetic encounter data. No real patient record enters the repository. A local substitution using patient-level data requires separate authorization, minimization, secure storage, privacy review, and release control. It must not be committed to the public repository.

### Responsible claims

Allowed:

- describe the CMS OP_18b hospital-result distribution;
- state the 148-minute hospital-level anchor;
- describe the generated encounter pattern;
- compare synthetic groups and months;
- recommend an action inside the synthetic scenario; and
- report no meaningful pattern in null or trivial variants.

Not allowed:

- call 148 minutes a national patient median or quality target;
- claim the synthetic hospital is representative;
- claim fast track or boarding caused a real outcome;
- claim the synthetic tail proves patient harm;
- interpret synthetic acuity or age differences clinically; or
- set real staffing, capacity, or policy from this case.

## 18. AI and agent policy

AI may assist with:

- debugging the builder, generator, validator, or plotting code;
- comparing summary and display candidates;
- checking whether calculated values match output;
- proposing a critique repair;
- editing the source record, decision note, or alt text; and
- checking consistency across files.

AI may not:

- invent observations, unavailable CMS scores, denominators, or footnotes;
- describe the CMS source as patient-level data;
- label an unlabeled assessment variant without analysis;
- manufacture a hidden effect in the null variant;
- upgrade a trivial effect into an operational recommendation;
- claim that a synthetic result occurred in a real hospital;
- replace visual inspection or a reproducibility run; or
- conceal a generated assumption behind clinical-sounding prose.

The decision note records tool, purpose, adopted change, and learner verification. `No AI assistance used.` is complete when true.

## 19. Answer key and instructor notes

The instructor key is:

`courses/data-visualization/modules/04-distributions-vs-summaries/instructor-notes.md`

It contains:

- source and calibration boundaries;
- verified setup and results;
- 90-, 60-, and 35-minute session plans;
- Tier 1 answers;
- Tier 2 modification guidance;
- all three critique repairs;
- A1 through A9 answer guidance;
- the 100-point rubric;
- a worked board brief;
- common misconceptions;
- timing of the boarding-field reveal;
- handoffs to later modules;
- human review roles; and
- a post-session defect log.

### Reference interpretation

The real variant contains opposing processes. A strong answer protects the synthetic fast-track gain but directs a separate investigation toward boarding and inpatient flow. A strong null answer reports that the expected deterioration is absent. A strong trivial answer distinguishes a small statistical detection from a decision-changing effect.

### Alternate answers

A histogram, density, violin, ECDF, or coordinated view can earn full credit when it reveals the necessary shape, tail, group, and time information. A simpler summary can earn full credit for a null or center-focused decision when the learner proves that omitted structure does not change the choice.

## 20. Runnable acceptance checks

Run from `courses/data-visualization/modules/04-distributions-vs-summaries/`.

### Rebuild the public calibration

```powershell
Rscript build_cms_ed_calibration.R data/cms_ed_op18b_2026.csv
```

Pass: all 4,658 national OP_18b rows are written, including 4,081 reported and 577 unavailable values, and the reported median is 148 minutes.

### Rebuild and validate the real variant

```powershell
Rscript generate_ed_los.R real 730 data/ed_los_2026.csv
Rscript validate_ed_los.R data/ed_los_2026.csv real
```

Pass: the committed checksum is reproduced and 26 of 26 checks pass.

### Validate assessment variants

```powershell
Rscript generate_ed_los.R null 730 outputs/assessment-null.csv
Rscript validate_ed_los.R outputs/assessment-null.csv null
Rscript generate_ed_los.R trivial 730 outputs/assessment-trivial.csv
Rscript validate_ed_los.R outputs/assessment-trivial.csv trivial
```

Pass: each variant passes 23 of 23 checks.

### Generate learner outputs

```powershell
Rscript lab.R data/ed_los_2026.csv
```

Pass: four PNGs and `monthly_metrics.csv` are created.

### Generate critique outputs

```powershell
Rscript critique_charts.R data/ed_los_2026.csv
```

Pass: three intentionally flawed PNGs are created.

### Determinism and checksum checks

Rebuild the calibration and real encounter file into a temporary directory. Confirm:

- calibration SHA-256 `c9603109d4ea251b8096a655c27ad42cd6313bdb1309999bee3eb37ce79ec67d`;
- encounter SHA-256 `27c1c0feed8beb4ab0ac6dc77eaa3d1ed95c07b89f52f4881c25954ba43fbc55`; and
- a different seed produces a different encounter file that still passes the real contract.

### Visual inspection

Confirm:

- the monthly mean does not visually manufacture a large change;
- the pooled histogram shows right skew and discloses its 99.5th-percentile view limit;
- disposition densities remain distinguishable without color alone;
- the admitted second process is visible;
- all four monthly-metric panels render with correct units;
- the three critique charts visibly contain their intended defect; and
- titles do not claim a real hospital result.

### Link check

Confirm browser resolution for the CMS landing page, metadata endpoint, data dictionary, PLOS article, Nature DOI, NIST page, and optional Rousselet DOI. Record any publisher automation barrier without substituting an unofficial source.

### Repository checks

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
node --check curriculum-data.js
git diff --check
```

### Clean-run gate

Before alpha, an independent instructor follows only the README from a clean checkout, rebuilds or verifies both data releases, runs all three variants, creates all lab and critique outputs, and records any hidden assumption.

## 21. Release status, reviewers, version, and known issues

### Release identity

| Item | Value |
|---|---|
| Module version | 0.4.0 |
| Commons release | 0.15.0 |
| Synthetic data version | 0.2.0 |
| Calibration version | 0.1.0 |
| Status | Runnable release candidate |
| Release date | 2026-08-29 |
| Technical validation | Complete |
| Human review | Pending |

### Maturity gate

The module is a runnable release candidate because the complete national OP_18b calibration is pinned and reproducible, all three synthetic variants meet their contracts, the lab and critique outputs render, the exact assessment package is defined, and the instructor key contains measured answers.

Alpha requires sign-off from:

1. visualization faculty for distribution and source fidelity;
2. an emergency-department clinician or operations leader for decision realism;
3. accessibility review for figures, tables, and text alternatives; and
4. independent teachability from a clean checkout.

Beta requires a taught pilot and revision. Stable requires successful reuse by a second instructor or program.

### Known issues

- Human reviews are pending.
- CMS OP_18b is a hospital-level median and does not provide a patient-level distribution.
- Only the discharged median center is calibrated to the public source.
- Acuity and age group are independent of length of stay and cannot support clinical inference.
- Staffing, occupancy, seasonality, transfers, censoring, return visits, diagnoses, and other real processes are omitted.
- The hidden second mode has technical and build-team visual confirmation but still needs independent human review.
- macOS and Linux clean-run verification is pending.

## Handoff to Module 05

Module 04 ends with a distribution and group comparison that reveals a smaller care process. Module 05 asks whether the rates and denominators used to compare that process are stable and comparable.

The learner carries forward:

- decision owner and action;
- row grain and group definitions;
- chosen center, percentile, and threshold;
- subgroup counts;
- missingness and unavailable-value status;
- public-versus-synthetic source boundary;
- reproducible figures; and
- a bounded operational claim.

The next build unit is Module 05, Rates, denominators, and adjustment.
