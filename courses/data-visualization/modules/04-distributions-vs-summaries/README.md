# Module 04: Distributions versus summaries

- Thread: visualization
- Level: healthcare essential
- Status: runnable release candidate; required human reviews pending
- Module version: `0.4.0`
- Slot cost: one teaching slot
- Concept core: about 22 minutes
- Lab: 60 to 90 minutes, depending on scaffold level
- First lab environment: R and ggplot2
- Source: [Ali Goff's DA-730 redesign](../../../../docs/source/ali-goff-da-730-course-redesign.md#module-04-distributions-versus-summaries)
- Current specification: [21-section module contract](../../../../docs/curriculum/courses/DA-730/modules/04-distributions-summaries-spec.md)
- Original build specification: [implementation record](../../../../docs/specs/2026-08-15-ali-goff-module-04-build-spec.md)

## Why this module exists

A correct summary can still hide the part of a distribution that matters for a healthcare decision. This module teaches learners to ask whether a mean, median, or other summary preserves the information needed to act.

The primary case uses emergency department length of stay. Median performance improves after a fast-track pathway launches, while the longest stays become much worse as inpatient boarding grows. Both findings are correct. The learner must find the hidden change and redirect the decision.

## Quick start

Install R and the `ggplot2` package, open this module directory, then run:

```powershell
Rscript validate_ed_los.R data/ed_los_2026.csv real
Rscript lab.R data/ed_los_2026.csv
Rscript critique_charts.R data/ed_los_2026.csv
```

To reproduce the committed data first, run:

```powershell
Rscript build_cms_ed_calibration.R data/cms_ed_op18b_2026.csv
Rscript generate_ed_los.R real 730 data/ed_los_2026.csv
```

### Beginner RStudio path

1. Download `lab.R` and `ed_los_2026.csv` into the same folder.
2. Open `lab.R` in RStudio.
3. Choose **Session > Set Working Directory > To Source File Location**.
4. In the Console, run `install.packages("ggplot2")` once.
5. Click **Source**. The script creates four charts and `monthly_metrics.csv` in `outputs/lab/`.

The final reference visualization is `outputs/lab/04-monthly-metrics.png`. It compares the mean, median, 90th percentile, and share of visits over eight hours across 2026.

See the [data specification](data-spec.md), [learner assessment](assessment.md), [instructor notes](instructor-notes.md), and [release record](release.json).

## 1. Competency statement

Given a healthcare dataset and a clinical or operational comparison question, the learner determines whether a summary statistic represents the patient groups and care processes needed for the decision. The learner selects a display that reveals any consequential part of the distribution and explains what a healthcare leader should do differently.

The assessment uses three observable behaviors:

- C4.1, diagnose: identify when a summary conceals skew, multiple modes, unequal group sizes, or a consequential tail.
- C4.2, select and justify: choose a display and defend it against at least one alternative. A well-defended decision to use a summary can earn full credit.
- C4.3, connect to consequence: state what decision changes when the distribution is revealed.

A technically polished chart does not meet the competency if the learner cannot explain what someone should do differently.

## 2. Prerequisites

Within the visualization course:

- Module 01: encoding and the grammar of graphics;
- Module 02: perception and the accuracy ranking;
- Module 03: chart selection in practice.

From the foundation curriculum:

- mean, median, standard deviation, and quantiles;
- basic interpretation of histograms;
- ability to run and modify supplied R code.

The transition cohort may enter with no R authoring experience. The first two scaffold levels provide all required code.

## 3. Concept core

### Every summary is a lossy compression

A summary statistic replaces many values with a few. The question is not whether the summary is mathematically correct. The question is:

> Does what this summary discards matter for the decision being made?

Anscombe's quartet or the Datasaurus Dozen may introduce the idea, but the healthcare decision remains the center of the module.

### Healthcare interpretation rule

For every display, learners name the patient group, care process, healthcare audience, and decision. In the emergency-department case, "the median improved" is not a complete interpretation. Learners must ask whether the metric describes discharged patients, admitted patients, or people waiting for an inpatient bed, then state whether the evidence supports a fast-track, staffing, bed-flow, or monitoring decision.

### What a bar of means discards

A bar that represents one mean per group hides:

- shape, including skew and multiple modes;
- spread;
- the number of observations;
- the individual patient experience.

Adding a standard error bar only describes the precision of the estimated mean. It does not show the spread of patient experience.

### Four hiding mechanisms

| Mechanism | What the mean does | Healthcare example |
|---|---|---|
| Skew | Moves toward the tail and may describe nobody typical. | Cost, wait time, and length of stay. |
| Multiple modes | Falls between real groups and describes neither. | Two care pathways pooled into one metric. |
| Unequal group sizes | Tracks the largest group. | Discharged patients overwhelm admitted patients in a pooled summary. |
| Consequential tail | Treats extreme values as noise. | The longest waits are the patients at greatest risk of harm. |

### The disaggregation reflex

When a summary looks stable, split it by the variable most likely to separate care pathways. If the subgroups resemble the whole, the summary earned confidence. If they do not, the split reveals the decision-relevant structure.

A flat pooled mean can describe an unchanged system or two large opposing changes.

### Display ladder

Use the least complex display that supports the decision.

| Display | Reveals | Important blind spot |
|---|---|---|
| Bar of means | Central tendency | Shape, spread, sample size, and individuals. |
| Mean with error bar | Precision of the estimated mean | Shape and spread of the data. |
| Box plot | Median, quartiles, and extremes | Multiple modes. |
| Box or violin with points | Shape, sample size, and individuals | Clutter with large datasets. |
| Histogram or density plot | Full shape | Group comparison unless separated. |
| Faceted density or ridgeline plot | Shape across groups | Precise values. |
| Empirical cumulative distribution function | All percentiles and threshold exceedance | Unfamiliarity for many audiences. |

The box plot receives special attention because learners may treat it as the universally responsible choice. It cannot reveal multiple modes.

### Match the statistic to the decision

| Decision | Useful statistic |
|---|---|
| Total burden, capacity, or cost | Mean, because it multiplies by the number of cases. |
| Typical patient experience | Median. |
| Staffing so most patients are served | A high percentile such as the 90th. |
| Preventing prolonged waits or harm | Share above a decision-relevant threshold. |
| Regulatory reporting | The statistic named by the measure specification. |

### When a summary is enough

The module does not teach learners to show every distribution. A summary may be enough when the data are roughly symmetric and unimodal, sample size is large and stable, the decision depends on the center, and the audience cannot use a more detailed display.

### Required readings

- Weissgerber TL, Milic NM, Winham SJ, Garovic VD. Beyond bar and line graphs: time for a new data presentation paradigm. *PLOS Biology*. 2015;13(4):e1002128. https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128
- Streit M, Gehlenborg N. Bar charts and box plots. *Nature Methods*. 2014;11(2):117. https://doi.org/10.1038/nmeth.2807
- NIST/SEMATECH e-Handbook of Statistical Methods, Histogram. https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm
- CMS, Timely and Effective Care - Hospital. https://data.cms.gov/provider-data/dataset/yv7e-xc69
- Optional: Rousselet GA, Pernet CR, Wilcox RR. Beyond differences in means. *European Journal of Neuroscience*. 2017;46(2):1738-1748. Open-access manuscript: https://eprints.gla.ac.uk/141172/ DOI: https://doi.org/10.1111/ejn.13610

Use the linked publisher or government record. Distinguish an article's result from a universal rule and the CMS hospital median from a patient-level distribution.

## 4. Healthcare case

### Emergency department length of stay

An emergency department launches a synthetic fast-track pathway in January 2026. Twelve months later, the median length of stay has fallen from 200 to 134 minutes. Leadership calls the change a success and asks for a chart to support expansion.

The recalibrated reference release measures:

| Metric | January 2026 | December 2026 | Change |
|---|---:|---:|---:|
| Mean length of stay | 217.9 minutes | 212.5 minutes | -2.5% |
| Median length of stay | 200.0 minutes | 134.0 minutes | -33.0% |
| 90th percentile | 306.1 minutes | 536.8 minutes | +75.4% |
| Share over eight hours | 2.4% | 10.5% | +8.0 percentage points |

The fast-track pathway works for discharged patients. At the same time, inpatient boarding grows from 10% to 46% of admitted patients. Discharged encounters make up most of the dataset, so the median reports the improvement. The upper tail reports the deterioration among boarded patients.

Expanding fast track would address the already improved pathway. The distribution redirects attention toward inpatient capacity and boarding.

### Alternate settings

The same competency and data contract can use other clinical settings:

| Setting | Outcome | Groups | Hidden second process |
|---|---|---|---|
| Oncology | Infusion chair time | Regimen | Pharmacy turnaround delays. |
| Ambulatory care | Clinic wait time | Visit type | Double-booked appointments. |
| Revenue cycle | Cost per admission | Diagnosis-related group | Complication-driven outliers. |
| Perioperative care | Case duration | Service line | Add-on emergency cases. |

## 5. Dataset specification

The portable artifact is the data contract, not one CSV. A new clinical case must satisfy the same teaching conditions.

### Required conditions

| Condition | Threshold | What it teaches |
|---|---:|---|
| Right-skewed primary outcome | Mean divided by median is at least 1.20. | The mean may not represent a typical case. |
| Unequal group sizes | Largest group is at least 2.5 times the comparison group. | A pooled summary follows the majority group. |
| Hidden second mode | The minority group has a clear second mode that becomes a weak shoulder when pooled. | Disaggregation reveals structure. |
| Opposing time trends | Mean changes by less than 6%; 90th percentile rises by more than 40%. | Stability does not prove that nothing changed. |
| Small subgroup | At least one meaningful group has fewer than 100 observations. | Small denominators produce unstable estimates. |
| Misleading average of averages | Unweighted group means differ from the pooled mean by at least 30 minutes. | Group means must be weighted or reported separately. |

### Measured reference release

The source values guided the teaching design. The committed variant `real`, seed `730`, measures:

- 8,392 synthetic encounters in calendar year 2026;
- generator seed `730`;
- mean divided by median of `1.273`;
- 6,462 discharged and 1,930 admitted encounters, a ratio of `3.35:1`;
- admitted modes near 252 and 782 minutes, with the second mode weak when data are pooled;
- January-to-December mean change of `-2.5%` and 90th-percentile change of `+75.4%`;
- 66 encounters in the rarest acuity group;
- 67.9-minute difference between the unweighted average of group means and the pooled mean.

All defined teaching thresholds pass. Exact measured results and the CSV checksum are recorded in [release.json](release.json).

### Source status

The public calibration file contains every national CMS OP_18b hospital row from the 2026-08-13 Timely and Effective Care release: 4,658 rows, including 4,081 reported values and 577 unavailable results. The reported hospital median is 148 minutes. The generator uses that value only as the center of the discharged pathway.

The 8,392 encounter rows remain deterministic synthetic teaching data. The monthly improvement, admission process, boarding process, tails, acuity, age, and dates are not CMS estimates and were not fitted to patient records. See [source-record.yml](source-record.yml) for URLs, rights, transformations, checksums, and limits.

### Columns

| Column | Type | Purpose |
|---|---|---|
| `encounter_id` | character | Synthetic encounter identifier. |
| `arrival_date` | date | Date within calendar year 2026. |
| `esi` | integer | Emergency Severity Index from 1 to 5, with level 1 deliberately rare. |
| `age_group` | character | 18-39, 40-64, 65-79, or 80+. |
| `disposition` | character | Admitted or discharged. |
| `boarded` | integer | Boarding indicator and the mechanism behind the second mode. |
| `los_min` | integer | Arrival-to-departure length of stay in minutes. |

### Effect variants

The generator must support three unlabelled variants:

- `real`: deterioration is concealed by the summary;
- `null`: nothing meaningful changed;
- `trivial`: a detectable change is too small to justify action.

Use the real variant for the lab. Use null and trivial variants in assessment so learners cannot assume a hidden finding exists.

## 6. Lab

One lab has three scaffold levels. Learners at different coding levels still answer the same visualization question.

### Tier 1: run and observe

The supplied R script should produce four views and ask learners to interpret them:

1. Monthly mean length of stay. Does the department appear improved, worse, or stable?
2. A histogram of all length-of-stay values. Is the distribution symmetric, and is there evidence of a second process?
3. Density plots separated by disposition. How many modes appear, and what might they represent?
4. Monthly mean, median, 90th percentile, and share over eight hours. Which measures improve and which worsen?
5. What leadership decision changes when the fourth view replaces the first?

### Tier 2: modify

Learners receive working code and make six changes:

1. Replace the density display with a box plot and identify what disappears.
2. Separate the monthly mean chart by disposition and explain which group drives the pooled trend.
3. Separate by boarding status and explain the second mode.
4. Add a logarithmic horizontal scale and discuss what becomes easier and harder to read.
5. Build an empirical cumulative distribution function and estimate the share above eight hours.
6. Replace the 90th percentile with the 95th and discuss why the measure should be chosen before inspecting the result.

### Tier 3: author

Learners receive the following task without starter code:

> The chief operating officer has five minutes at the board meeting. Produce one chart and two sentences that accurately represent emergency department performance in 2026. Justify the chart against one alternative and state what decision it supports that the current mean-based chart does not.

Multiple displays may earn full credit. The justification and decision consequence are graded, not a preferred chart type.

## 7. Critique set

### C1. Mean with standard error bars

Mean length of stay by acuity level hides sample size and the distribution of patient experience. The repair should reveal observations or distributions and label the group size.

### C2. Truncated axis

A monthly mean chart uses a vertical axis from 212 to 219 minutes. It exaggerates a small mean change while continuing to hide the upper-tail deterioration. Repairing the axis alone does not repair the analytic choice.

### C3. Average of averages

A table reports the unweighted mean of the discharged and admitted group means as the overall mean. The repair weights by group size or reports the groups separately.

Every critique asks:

- What is concealed?
- Who could be harmed by the concealment?
- What display or summary should replace it?

## 8. Assessment items

### Recognition

1. Explain how an emergency department's annual mean length of stay could remain unchanged when care is stable, and how the same mean could result from discharged patients improving while admitted patients wait longer.
2. Identify what a box plot can hide when discharged and boarded admitted patients follow different length-of-stay patterns.
3. Name three facts a bar of mean length of stay by acuity does not provide and explain how each omission could change an emergency-department decision.

### Application

4. Given the trivial-effect variant, choose a display and justify it against one alternative. A well-defended summary can earn full credit.
5. Choose a display for 4,000 encounters across six hospital service lines and explain how it supports a system operations director without hiding group size or unusual waits.
6. Read an empirical cumulative distribution function for two clinics and explain why their medians are misleading.

### Judgment and transfer

7. Given the null variant and a director who expects deterioration, report the absence of a meaningful effect rather than manufacturing one.
8. Explain how median door-to-clinician time can improve while complaints about long waits rise, then specify what to add to the dashboard.
9. Given a new dataset and operational decision, choose a statistic, build a display, and write a recommendation. Half of the score comes from explaining what decision changes.

## 9. Instructor notes

### Common misconceptions

- Skew does not automatically make the median correct. Capacity and cost questions may require the mean.
- Showing the whole distribution is not always the clearest choice.
- A box plot can hide multiple modes.
- Standard deviation and standard error answer different questions.
- The second mode is not a set of bad records to delete. It represents patients experiencing a different care process.

### Boarding field

The source recommends shipping the `boarded` field for the transition cohort so learners can discover the mechanism in Tier 2. Later assessment variants may withhold it.

### Guest speaker

An emergency department operations director or charge nurse can explain what daily dashboards show, what staff experience that the metrics miss, and how leadership responds when a metric improves while the department feels worse.

### Time cuts

| Available time | Keep |
|---|---|
| About 90 minutes | Full module. |
| About 60 minutes | Remove the logarithmic scale and empirical cumulative distribution function tasks. Keep the box-plot and boarding comparisons. |
| About 35 minutes | Keep the lossy-summary concept, four hiding mechanisms, first four Tier 1 questions, box-plot comparison, and boarding comparison. |

Below 35 minutes, the lesson becomes a demonstration rather than a practiced competency.

### Handoffs

- Rates and denominators: the rare acuity group introduces small-denominator instability.
- Uncertainty: the critique of standard error leads into estimate stability.
- Time: the 90th-percentile trend becomes a run-chart problem.
- Quality improvement: a reported metric improving is not the same as the system improving.
- Ethics: learners must distinguish what is reported from what matters to patients.

### Faculty review questions

1. Does the module need one slot, or should the empirical cumulative distribution function material receive more time?
2. Is the US emergency department measure framing suitable for international learners?
3. Should the boarding field ship immediately or after the first critique?
4. Is the nine-part module contract practical for the faculty build team?

## Build checklist

- [x] Course source converted to Markdown.
- [x] Nine-part module content record.
- [x] Deterministic R generator.
- [x] Generated CSV and data dictionary.
- [x] Pinned public CMS calibration extract, build script, and source record.
- [x] Automated data-contract checks.
- [x] Tier 1 and Tier 2 R scripts.
- [x] Critique chart generation code.
- [x] Real, null, and trivial assessment variants generated on demand.
- [x] Instructor answer key and grading rubric.
- [x] Release manifest with version, license, row count, checksum, and known issues.

The package runs end to end and is ready for review. It remains a release candidate until faculty, emergency department, accessibility, and independent-instructor reviews are recorded.
