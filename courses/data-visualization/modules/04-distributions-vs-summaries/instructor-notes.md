# Instructor notes: Distributions versus summaries

Module version: `0.3.0`

These notes support a class taught without Ali Goff's original course document. The data are synthetic teaching data. They do not describe a real hospital, patient population, or intervention effect.

## Teaching aim

Learners should leave able to test whether a summary preserves the part of a distribution needed for a decision. They should not leave with a rule that the median is always better than the mean or that every chart must show every observation.

The central case contains two changes at once. Discharged encounters become faster, while admitted encounters worsen as boarding becomes more common. The pooled mean barely moves because the two changes oppose one another.

## Healthcare translation

Keep four healthcare elements visible throughout the session:

- **Patient groups:** most encounters end in discharge, while a smaller admitted group contains the longest stays.
- **Care processes:** the synthetic fast-track pathway shortens many discharged visits; boarding lengthens admitted visits while patients wait for inpatient beds.
- **Decision owners:** emergency-department leadership can protect fast-track gains, while hospital operations and bed-management teams investigate inpatient flow.
- **Decision boundary:** the charts show a synthetic operational signal. They do not prove that an intervention caused better or worse clinical outcomes.

Define boarding when it first appears. In this case, a boarded patient has been admitted but remains in the emergency department while waiting for an inpatient bed. Avoid teaching the long tail as a collection of statistical outliers. It represents a different hospital care process that needs a separate operational response.

## Source status

The file is deterministic and synthetic. It was designed to meet teaching conditions and was not fitted to a hospital dataset. Show learners the release record and the [course source register](../../data-source-register.md). Before a teaching release, either calibrate selected parameters to a named public aggregate source or rebuild the case from an identified Synthea release. Do not present these values as a benchmark for emergency-department performance.

## Prepare the module

From this module folder, run:

```powershell
Rscript validate_ed_los.R data/ed_los_2026.csv real
Rscript lab.R data/ed_los_2026.csv
Rscript critique_charts.R data/ed_los_2026.csv
```

If `ggplot2` is missing:

```r
install.packages("ggplot2")
```

The lab writes four charts and a monthly metrics table to `outputs/lab/`. The critique script writes three flawed charts to `outputs/critique/`.

## Reference results

The released dataset contains 8,392 encounters: 6,462 discharged and 1,930 admitted. These values should be stable for variant `real`, seed `730`.

| Measure | January | December | Change |
|---|---:|---:|---:|
| Mean length of stay | 205.6 min | 200.2 min | -2.6% |
| Median length of stay | 185.5 min | 116.5 min | -37.2% |
| 90th percentile | 294.0 min | 536.8 min | +82.6% |
| Share over 8 hours | 2.4% | 10.5% | +8.0 percentage points |

Other checks:

- overall mean is 202.9 minutes;
- overall mean divided by median is 1.335;
- boarded admitted median is 782 minutes;
- non-boarded admitted median is 252 minutes;
- admitted mean rises from 310.3 to 508.8 minutes;
- discharged mean falls from 174.3 to 108.4 minutes;
- boarding rises from about 10% to 46% of admitted encounters;
- ESI 1 contains 66 encounters;
- the unweighted average of the two disposition means is 275.2 minutes, 72.2 minutes above the pooled mean.

## Session plans

### 90 minutes

| Segment | Time |
|---|---:|
| Emergency-department brief and first chart choice | 20 min |
| Read the department-wide views | 20 min |
| Split discharged, admitted, and boarded care processes | 25 min |
| Build or critique the leadership display | 15 min |
| Patient-flow and bed-capacity debrief | 10 min |

### 60 minutes

Remove the logarithmic scale and empirical cumulative distribution tasks. Keep the box-plot comparison, the split by disposition, the split by boarding, and the decision debrief.

### 35 minutes

Teach the lossy-summary idea and four hiding mechanisms. Run the first four Tier 1 questions, then compare a box plot with the density view and reveal boarding. Below 35 minutes, treat the session as a demonstration rather than evidence that learners practiced the competency.

## Tier 1 answer key

1. **Monthly mean:** The department-wide mean changes from 205.6 to 200.2 minutes. A chief operating officer could read this as modest improvement or stability and miss the admitted patients waiting longest.
2. **Pooled histogram:** The distribution is strongly right-skewed. The boarded process is hard to see because discharged encounters outnumber admitted encounters by more than three to one.
3. **Density by disposition:** Admitted encounters show a second mode near the boarded median of 782 minutes. Discharged encounters have a shorter, single dominant process. The split turns a statistical shape into a hospital-flow question.
4. **Four monthly measures:** The mean is nearly flat and the median improves sharply. The 90th percentile and share over eight hours worsen sharply. Fast-track gains reach many discharged patients, while admitted patients increasingly remain in the emergency department waiting for beds.
5. **Decision consequence:** The first view could support declaring the department broadly improved. The fourth supports protecting fast-track gains while asking patient-flow, inpatient-capacity, and bed-management teams to address boarding and monitor the tail.

## Tier 2 guidance

1. **Box plot:** It preserves the median, quartiles, and outliers but can hide the two admitted modes. Ask learners to name the information lost, not merely whether the box plot looks cleaner.
2. **Split by disposition:** Discharged mean length of stay falls by about 66 minutes. Admitted mean length of stay rises by about 199 minutes. The pooled mean masks both changes.
3. **Split by boarding:** Non-boarded admitted encounters have a median of 252 minutes. Boarded admitted encounters have a median of 782 minutes. The second mode is a care-process signal, not bad data to delete.
4. **Log scale:** It makes a long right tail easier to see without using most of the canvas, but equal visual distances no longer represent equal numbers of minutes. Labels should help a nontechnical reader interpret the scale.
5. **Empirical cumulative distribution:** At 480 minutes, read `1 - F(480)` as the share over eight hours. That share rises from about 2.4% in January to 10.5% in December.
6. **95th percentile:** It rises from about 334.2 to 791.9 minutes, a larger change than the 90th percentile. Choosing a percentile after viewing the result invites selective reporting; choose the service threshold from the decision first.

## Critique answer key

### C1. Mean with standard error bars

The chart conceals patient-level spread, shape, group size, and multiple modes. A standard error describes precision of an estimated mean, not variation in patient experience. This matters most for the small ESI 1 group, which contains only 66 encounters. A reasonable repair is a distribution display by ESI with group counts and a statistic chosen for the operational question.

### C2. Truncated monthly mean

The 180-to-210-minute axis enlarges a small decline in the mean. Starting the axis at zero would reduce that visual exaggeration, but it would still leave the more important analytic problem: the mean hides a worsening upper tail. Replace it with the relevant percentile or threshold share, or show mean, median, 90th percentile, and the over-eight-hour share together.

### C3. Average of averages

The chart reports 275.2 minutes as the overall mean by giving the admitted and discharged means equal weight. The correct pooled mean is 202.9 minutes because the groups contain 1,930 and 6,462 encounters. Weight the group means by their counts or calculate the pooled mean from all rows. Better still, retain separate groups when the operational distinction matters.

For all three critiques, require learners to name who could be affected. Examples include boarded patients whose waits disappear in a pooled mean, staff whose capacity needs are understated, and leaders who allocate resources to the wrong process.

## Assessment answer key

### A1

An unchanged emergency department can retain the same length-of-stay distribution, admitted and discharged mix, and monthly pattern. A changed department can have discharged encounters improve while admitted encounters worsen, or can keep its mean while boarding and long waits grow. A distribution view plus time trends split by disposition and boarding distinguish these cases.

### A2

Multiple modes. A standard box plot shows a median, quartiles, and possible outliers, and can suggest skew, but it does not preserve density shape well enough to show separate modes reliably.

### A3

Any three well-explained omissions can earn full credit: sample size, spread, skew, multiple modes, unusual values, admitted and discharged mix, or the share beyond a service threshold. The learner must explain how the omission could misdirect emergency-department staffing, fast-track expansion, boarding response, or bed-capacity work.

### A4

For seed 730, the trivial variant has a two-sided Wilcoxon p-value of about 0.026, but the median changes by only 9 minutes, the 90th percentile by 5.5%, and the over-eight-hour share by 0.0 percentage points. A simple time trend or an effect summary with these values can earn full credit. The supported decision is to avoid claiming an operationally important change and continue routine monitoring.

### A5

Good answers include six aligned box plots with sample sizes, six compact violin or density plots, or a distribution summary with restrained jitter or sampling. Full credit requires a clear overplotting strategy and visible or stated group counts.

### A6

Clinic North has the better median but a much worse upper tail. The empirical cumulative distribution lets the reader compare every threshold, including the probability of waiting beyond an operational limit. A suitable question is, "What share of patients waits longer than eight hours?"

### A7

For seed 730, the null variant changes by -0.4% in mean, 0.0% in median, -0.3% in the 90th percentile, and -0.1 percentage points in the over-eight-hour share. Report that the expected deterioration is not present in this dataset. Recommend continued monitoring or a pre-specified follow-up analysis, not a search for a favorable subgroup.

### A8

Most patients can be seen faster while a smaller group waits much longer. The median then improves while complaints rise among people in the tail. Add a high percentile, the share beyond a service threshold, and a group or process split. The fuller view can trigger targeted capacity or flow work without undoing an intervention that helps the majority.

### A9

Use the rubric below. Multiple displays can be correct. A simple summary can earn full credit for the null or trivial variant when it is honest, justified, and tied to a decision.

## Tier 3 rubric

| Criterion | Full-credit evidence | Points |
|---|---|---:|
| Diagnose | Correctly identifies the consequential tail, hidden process, opposing trends, or honest absence of an effect. | 25 |
| Select | Uses a statistic and display matched to the stated decision. | 20 |
| Justify | Compares the choice with a reasonable alternative and names the information gained or lost. | 15 |
| Decide | Makes a supported operational recommendation and states what should change. | 30 |
| Reproduce and communicate | Script runs, labels include units, scale is honest, groups are readable without color alone, and alt text states the finding. | 10 |

Passing requires 70 points overall and at least 18 decision points. If the recommendation is absent or unsupported, the work cannot pass through visual polish alone.

## Worked Tier 3 answer

**Chart:** `outputs/lab/04-monthly-metrics.png`, produced by `lab.R`.

**Alt text:** Four monthly lines show a nearly flat mean and a falling median alongside a sharply rising 90th percentile and share of encounters over eight hours. The upper-tail deterioration accelerates late in 2026.

**Board note:** Typical emergency department length of stay improved during 2026, but the longest waits worsened: the median fell from 185.5 to 116.5 minutes while the 90th percentile rose from 294.0 to 536.8 minutes. Continue the fast-track pathway, but do not label performance an overall success until a boarding response and tail-sensitive dashboard are in place.

**Justification:** A single mean chart suggests stability and hides the operationally important tail. The four-panel chart keeps the familiar mean and median while adding the 90th percentile and threshold share that show why a separate boarding decision is needed.

Suggested score: 95/100. Diagnose 25, select 19, justify 14, decide 28, reproduce and communicate 9. A learner could improve this answer by labeling the boarding mechanism directly in the chart and presenting a narrower board-ready layout.

## Common misconceptions

- Skew does not automatically make the median correct. Total emergency-department workload, staffing hours, and capacity questions may require the mean.
- Showing the full distribution is not always the clearest choice.
- A box plot can hide multiple modes.
- Standard deviation and standard error answer different questions.
- The second mode is not a set of bad records to delete. It represents patients experiencing a different care process.
- Statistical detection does not establish clinical or operational importance, and this synthetic case does not establish patient harm or intervention causality.

## When to reveal `boarded`

For the transition cohort, ship the field in the data but do not name it during the first prediction. Reveal it during Tier 2 after learners have described the second admitted mode. For later assessment cohorts, the field may be withheld if another clinical clue lets learners form and test the mechanism without guessing blindly.

## Handoffs

- Rates and denominators: ESI 1 introduces small-denominator instability.
- Uncertainty: the standard-error critique leads into estimate stability.
- Time: the 90th-percentile trend leads into run charts.
- Quality improvement: a reported metric improving is not the same as the system improving.
- Ethics: learners must distinguish what is easy to report from what matters to patients.

## Review record

This release is a runnable candidate until the following people complete review. Record names, dates, and findings in `release.json`.

| Role | Reviewer | Status | Date | Notes |
|---|---|---|---|---|
| Faculty and source fidelity | Ali Goff or delegate | Pending | | |
| Emergency department content | Emergency medicine reviewer | Pending | | |
| Accessibility | Accessibility reviewer | Pending | | |
| Independent teachability | Instructor not involved in the build | Pending | | |

## Post-session defect log

Add one row after each teaching session. Open an issue for anything that could change an answer, score, or operational interpretation.

| Date | Cohort | Timing issue | Unclear prompt | Software failure | Unexpected interpretation | Follow-up |
|---|---|---|---|---|---|---|
| | | | | | | |
