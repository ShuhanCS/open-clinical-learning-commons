# Module 04: Distributions versus summaries

- Status: draft 0.2 for faculty review, tailored to asynchronous D2L delivery
- Date: 2026-08-18
- Source course: DA-730, Analyzing, Visualizing, and Storytelling with Data
- Supersedes: draft 0.1, 2026-08-15

| Field | Value |
|---|---|
| Slot cost | 1 module (half of a two-module week) |
| Concept core | 3 recorded segments, about 23 minutes total |
| Lab | 4 core exercises plus 2 extensions, about 65 to 75 minutes |
| Readings | About 25 minutes |
| Total student time | About 2.0 to 2.2 hours |
| D2L submission points | 7 (1 observation set, 4 core, 2 extension) |
| Canonical dataset | `ed_los_2026.csv` (8,392 rows) |
| Generator | `generate_ed_los.R` |
| Tool | R and ggplot2 via Posit Cloud |
| Portability | High. Domain-independent core; four alternates specified. |

## 0. Delivery model

Asynchronous, D2L Brightspace. Four constraints shaped every component below.

**No contiguous blocks.** Students are medical students on rotation or hospital staff working full time. The total time is affordable; a 90-minute uninterrupted sitting is not. Every element is sized for a single sitting of 15 minutes or less, and nothing carries state from one element to the next. A student who does exercise 3 on Tuesday night and exercise 4 on Saturday morning loses nothing.

**No instructor in the room.** Misconceptions cannot be caught by noticing a puzzled face. The three predictable errors in this module are converted to auto-graded D2L checks with feedback written for the specific wrong answer (section 8.4). This is the most important asynchronous adaptation in the module.

**The guest speaker is never load-bearing.** Live attendance is best-effort with recording afterward, so some students will watch after the lab and some not until exam week. No lab question or assessment item depends on speaker content.

**Cohort clinical experience is an asset.** Nearly all students work in or are familiar with hospitals. The discussion prompt (section 8.5) is built to draw on that rather than around it.

## 1. Competency statement

Given a dataset and a comparison question, the student determines whether a summary statistic faithfully represents the underlying distribution, and selects a display that reveals the distributional features relevant to the decision at hand.

Three observable behaviors, used directly as the assessment rubric:

- **C4.1 Diagnose.** Identify when a reported summary is concealing skew, multimodality, unequal group sizes, or a consequential tail.
- **C4.2 Select and justify.** Choose a display appropriate to the distribution and the decision, and defend the choice against at least one alternative. This includes correctly judging that a summary is sufficient.
- **C4.3 Connect to consequence.** State what decision changes when the distribution is revealed rather than summarized.

C4.3 is the one that distinguishes this from a statistics exercise. A student who produces a beautiful faceted density plot but cannot say what the ED should do differently has not met the competency.

## 2. Prerequisites

Within-thread: Module 01 (encoding and grammar of graphics), Module 02 (perception and the accuracy ranking), Module 03 (chart selection in practice).

Module 02 matters most. This module argues that a bar of means is the wrong encoding; that argument only lands for a student who already knows encodings can be ranked on evidence rather than taste.

From Toolbox: mean, median, SD, quantiles, histograms. Ability to run and modify a supplied R script. No modeling required.

Assumed of a transitional (pre-Toolbox) student: nothing beyond running supplied code. See section 6.

## 3. Concept core

Domain-independent and tool-independent. This is the component that never changes when the module ports to another X course.

Delivered as three recorded segments. Segmenting is not cosmetic: it lets a student watch one on a break, and lets a confused student return to the specific 8 minutes that lost them rather than scrubbing a 23-minute video.

### Segment A: Why summaries hide things (about 8 minutes)

#### A.1 Every summary is a lossy compression

A summary statistic replaces many numbers with few. That is its purpose. The question is never "is this summary correct" but rather:

> Does what this summary discards matter for the decision being made?

That is the whole module. Everything below is machinery for answering it.

Anscombe's quartet and the Datasaurus Dozen are the canonical demonstrations: datasets with identical means, variances, and correlations that look nothing alike. Use one briefly. Do not dwell; students find them charming and then fail to generalize. The generalization is the point.

#### A.2 What a bar chart of means discards

A bar encodes exactly one number per group, yet occupies area that implies mass where none was measured. It discards:

- **Shape.** Symmetric, skewed, and bimodal data produce identical bars.
- **Spread.** No indication whether values cluster tightly or scatter.
- **n.** A bar over 12 observations looks identical to one over 12,000.
- **The individual.** In health care the individual is often the entire point.

Adding a standard error bar addresses spread only, and does so misleadingly: SE describes precision of the estimated mean, not the range of patient experience. A narrow SE bar on 4,000 encounters signals a well-estimated mean, not a consistent one.

#### A.3 Four mechanisms by which a summary hides something

| Mechanism | What the mean does | Health care instance |
|---|---|---|
| Skew | Pulled toward the tail, describing nobody typical | Cost, LOS, wait time are all right-skewed |
| Multimodality | Lands between two real groups, describing neither | Two care pathways pooled into one metric |
| Unequal group sizes | Dominated by the largest group | Discharged patients swamp admitted patients |
| Consequential tail | Treats extremes as noise | The tail is the harmed patient |

The fourth is where health care differs from most analytics domains. In retail the tail is a rounding error. In clinical operations the tail is the patient who waited fourteen hours in a hallway. Reporting the center while the tail is the outcome of interest is the characteristic analytic failure of this field.

**Segment A close.** Before starting Segment B, a student should be able to state that a stable summary is not evidence that nothing is happening.

### Segment B: Disaggregation and the ladder of displays (about 8 minutes)

#### B.1 The disaggregation reflex

Teach this as a habit, not an insight:

> When a summary looks stable, split it before believing it.

Split by the variable that plausibly separates care pathways. If the subgroups look like the whole, the summary was honest and you have earned confidence in it. If they do not, you have found the story.

Stability is not evidence of nothing happening. Offsetting movements produce a flat mean, and a flat mean is exactly what an unchanging system and two large opposing changes have in common.

#### B.2 The ladder of displays

Each rung reveals more and costs more space and audience effort. Climbing higher is not automatically better; the correct rung is the lowest one that supports the decision.

| Rung | Display | Reveals | Blind to |
|---|---|---|---|
| 1 | Bar of means | Central tendency | Everything else |
| 2 | Mean with error bar | Precision of the estimate | Shape, n, spread of the data |
| 3 | Box plot | Median, quartiles, extremes | Multimodality |
| 4 | Box or violin with jittered points | Shape, n, individuals | Cluttered above about 1,000 points |
| 5 | Histogram or density | Full shape | Group comparison, unless faceted |
| 6 | Faceted density or ridgeline | Shape across groups | Precise values |
| 7 | ECDF | All percentiles at once, honest about n | Unfamiliar to most audiences |

Two things students consistently need told:

**The box plot has its own blind spot.** A box plot cannot show multimodality. A bimodal distribution and a uniform one can produce nearly identical boxes. Students who learn "box plots are the responsible choice" will confidently miss the exact structure this module is about. Core Exercise 1 demonstrates this directly.

**The ECDF is underused and worth teaching.** It answers "what fraction of patients waited longer than X" for every X simultaneously, which is usually the operational question. It costs unfamiliarity, so it belongs in an analyst-facing view rather than a board slide.

### Segment C: Choosing the statistic (about 7 minutes)

#### C.1 Match the statistic to the decision

The center is often the wrong number.

| The decision is about | The right statistic |
|---|---|
| Total burden, capacity, cost | Mean (it multiplies by n) |
| The typical patient | Median |
| Staffing so most patients are served | 90th percentile |
| Preventing harm | Tail mass: percent over threshold |
| Regulatory compliance | Whatever the measure specifies, which may be none of the above |

That last row carries the module. CMS ED throughput measures use median time. A department can improve its reported median while the experience of its worst-served patients deteriorates sharply, and both facts are true and correctly measured. This is not a hypothetical; it is the lab.

#### C.2 When a summary is the right answer

Resist teaching "always show the distribution." That trades one reflex for another.

A summary suffices when the distribution is roughly symmetric and unimodal, n is large and stable, the decision genuinely depends on the center, and the audience cannot absorb more. A board deck with twelve distributions communicates less than a board deck with one number and a footnote.

The competency is judgment about which situation you are in. C4.2 explicitly credits a correct decision to summarize.

### 3.4 Assigned readings (about 25 minutes)

Replaces the current Tableau vendor collateral with peer-reviewed biomedical literature.

- Weissgerber TL, Milic NM, Winham SJ, Garovic VD (2015). Beyond bar and line graphs: time for a new data presentation paradigm. *PLOS Biology* 13(4): e1002128. **Primary reading, about 20 minutes.** Open access, biomedical, and it makes precisely this module's argument with real published examples.
- Streit M, Gehlenborg N (2014). Bar charts and box plots. *Nature Methods* 11(2): 117. One page, about 3 minutes. Assign as a companion.
- Optional: Rousselet GA, Pernet CR, Wilcox RR (2017). Beyond differences in means. *European Journal of Neuroscience* 46(2): 1738-1748.

## 4. Domain instantiation

### 4.1 Primary: emergency department length of stay

**Scenario given to students.**

> You are the analyst for an ED that launched a fast-track pathway in January 2026. Twelve months on, the department reports success: median length of stay fell from 164 to 102 minutes, a 37 percent improvement, and the CMS-reported metric confirms it. Leadership wants to expand the pathway and has asked you for a chart for the board.
>
> Before you build it, look at the distribution.

**What the data actually contains.** Verified in the shipped file:

| Metric | Jan 2026 | Dec 2026 | Change |
|---|---|---|---|
| Mean LOS | 192 min | 201 min | +4.5% |
| Median LOS | 164 min | 102 min | -37.3% |
| 90th percentile | 297 min | 606 min | +104.1% |
| Share staying over 8 hours | 2.7% | 11.2% | 4.1x |

Both headline summaries say the department improved or held steady. The 90th percentile doubled. The share of patients held longer than eight hours quadrupled.

Both stories are true. The fast-track pathway genuinely worked: discharged patients move much faster. Simultaneously, inpatient capacity tightened and boarding grew from 10 percent to 46 percent of admitted patients. Two real, opposing changes. The mean cancels them. The median, dominated by the 77 percent of encounters that are discharges, reports only the good one.

**The decision that turns on this.** Expanding fast track addresses a problem that is already solved and does nothing for the deteriorating group. The distribution redirects the intervention from ED throughput to inpatient capacity. That is C4.3, and it is the reason this scenario was chosen over a purely statistical one.

**Why this instantiation earns its slot.** It is not a contrived trap. Fast-track pathways are real, they work, boarding is the dominant US ED crisis, and the CMS measure really is a median. Every element a student might dismiss as artificial is a feature of the actual domain. For a cohort that works in hospitals, this matters: they will recognize it.

### 4.2 Alternates

Same competency, same spec, different X course. Each keeps the two-component mixture in the minority group.

| Course | Outcome | Groups | What mode 2 represents |
|---|---|---|---|
| Oncology | Infusion chair time | Regimen | Pharmacy turnaround delays |
| Ambulatory | Clinic wait time | Visit type | Double-booked slots |
| Revenue cycle | Cost per admission | DRG class | Complication-driven outliers |
| Perioperative | Case duration | Service line | Add-on emergency cases |

## 5. Dataset specification

This is the portable artifact. The module travels as a spec, not as a file. An X instructor generates data meeting the spec in their own domain and the module works unchanged. Written the other way around, the lesson would be welded to one CSV.

### 5.1 Required conditions

| # | Condition | Threshold | Teaches |
|---|---|---|---|
| 1 | Primary outcome right-skewed | mean/median >= 1.20 | Mean misrepresents the typical case |
| 2 | Unequal group sizes | ratio >= 2.5:1 | Pooled summary tracks the majority group |
| 3 | Two-component mixture in the minority group, invisible when pooled | Minority: 2 modes, secondary >= 25% of peak height. Pooled: secondary <= 15% | Disaggregation reveals structure |
| 4 | Opposing time trends that cancel in the mean | Mean drift < 6%; p90 drift > +40% | Stability is not evidence of nothing happening |
| 5 | A rare subgroup | At least one group n < 100 | Small-denominator instability (hands off to Module 06) |
| 6 | Unweighted group means diverge from pooled mean | >= 30 min | Averaging averages is not averaging |

### 5.2 Verified realization

`ed_los_2026.csv`, 8,392 encounters, calendar year 2026, seed 730.

| # | Condition | Achieved | Result |
|---|---|---|---|
| 1 | Skew | mean 194.7 / median 138 = 1.41 | PASS |
| 2 | Group ratio | 6,462 discharged : 1,930 admitted = 3.35:1 | PASS |
| 3 | Mixture | Admitted: modes at 252 and 782 min (secondary 36% height). Pooled: secondary shoulder at 13% | PASS |
| 4 | Opposing trends | mean +4.5%, p90 +104.1% | PASS |
| 5 | Rare subgroup | ESI 1: n = 66, SE 35.9 min vs 2.1 for ESI 4 | PASS |
| 6 | Unweighted vs pooled | 266 vs 195 = +71 min | PASS |

Condition 3 is the delicate one. The pooled secondary mode sits at 13 percent of peak height: a faint shoulder in a histogram, invisible in a bar chart or box plot, unmistakable when faceted by disposition. That gradient is deliberate. A student who looks carefully at the pooled histogram is rewarded with a hint rather than handed the answer.

Note also that box plot quartiles for admitted patients move only modestly (Q1 219 to 240, median 260 to 356) while Q3 moves 321 to 776. The box plot understates the change, which sets up the rung-3 blind spot demonstration in Core Exercise 1.

### 5.3 Columns

| Column | Type | Notes |
|---|---|---|
| `encounter_id` | chr | |
| `arrival_date` | date | 2026-01-01 to 2026-12-28 |
| `esi` | int | 1 (most acute) to 5. ESI 1 deliberately rare. |
| `age_group` | chr | 18-39, 40-64, 65-79, 80+ |
| `disposition` | chr | Admitted / Discharged |
| `boarded` | int | 0/1. The answer key. See instructor notes. |
| `los_min` | int | Arrival to departure, minutes |

### 5.4 Effect variants

Per the program principle that not every analysis may return a finding, the generator ships three variants:

- `effect = "real"` (default, shipped): deterioration concealed by the summary.
- `effect = "null"`: genuinely nothing happening. A student who has learned to always find a hidden crisis will fabricate one here. That failure is worth catching in a low-stakes module.
- `effect = "trivial"`: a real, statistically detectable, clinically negligible shift. The correct answer is "do not act on this."

Use `real` for the lab. Reserve `null` and `trivial` for assessment so the finding cannot be assumed.

## 6. Lab

Structure for asynchronous delivery. One observation set plus six independent exercises. Each is self-contained, sized for a single sitting of 10 to 15 minutes, and carries no state from any other. Each has its own D2L submission point, so partial progress is visible and creditable and a student interrupted mid-week does not restart.

**Environment:** Posit Cloud workspace, dataset pre-loaded, no local installation. Closing the browser loses nothing.

**Tier policy.**

- Transitional cohort (Fall 2026): Observation Set plus Core Exercises 1 to 4 required. Extensions optional. Tier 3 optional and ungraded.
- Post-Toolbox: Observation Set dropped, Tier 3 becomes the graded default.

### Observation Set (Tier 1, about 25 minutes, 1 submission)

Complete script supplied. Students run it and answer five questions. No R authoring. May be split at any question.

```r
library(tidyverse)

ed <- read_csv("ed_los_2026.csv") |>
  mutate(month = floor_date(arrival_date, "month"))

# The chart leadership is currently looking at
ed |>
  group_by(month) |>
  summarise(mean_los = mean(los_min)) |>
  ggplot(aes(month, mean_los)) +
  geom_col(fill = "steelblue") +
  labs(title = "Mean ED length of stay by month, 2026",
       x = NULL, y = "Mean LOS (minutes)")
```

**Q1.** Describe the trend. Based on this chart alone, is the department improving, worsening, or stable?

```r
# The same data, without summarising first
ggplot(ed, aes(los_min)) +
  geom_histogram(bins = 60) +
  labs(x = "LOS (minutes)", y = "Encounters")
```

**Q2.** Is this distribution symmetric? Where is most of the mass? Is there anything to the right of the main peak?

```r
ggplot(ed, aes(los_min)) +
  geom_density() +
  facet_wrap(~disposition, scales = "free_y") +
  labs(x = "LOS (minutes)")
```

**Q3.** How many peaks does each panel show? What does a second peak imply about the admitted group?

```r
ed |>
  group_by(month) |>
  summarise(mean = mean(los_min), median = median(los_min),
            p90 = quantile(los_min, 0.90),
            pct_over_8h = 100 * mean(los_min > 480)) |>
  pivot_longer(-month) |>
  ggplot(aes(month, value)) +
  geom_line(linewidth = 1) +
  facet_wrap(~name, scales = "free_y") +
  labs(x = NULL, y = NULL)
```

**Q4.** Four statistics, same data. Which say the department improved? Which say it worsened? Explain how both can be correct.

**Q5.** The board sees only the first chart. Name one decision they might make that the fourth would change.

### Core Exercise 1: The box plot blind spot (about 12 minutes, 1 submission)

Replace `geom_density()` in the Q3 plot with `geom_boxplot(aes(y = los_min, x = disposition))`.

**Submit:** your chart plus two sentences. Does the box plot show the second peak? State the general principle about what a box plot cannot reveal.

Followed by auto-graded check MC-1.

### Core Exercise 2: Which group drives the trend (about 12 minutes, 1 submission)

Take the monthly mean bar chart from the Observation Set and add `facet_wrap(~disposition)`.

**Submit:** your chart plus two sentences identifying which group drives the pooled trend, and why.

### Core Exercise 3: The mechanism (about 15 minutes, 1 submission)

Change the faceting variable from `disposition` to `boarded`.

**Submit:** your chart plus a short paragraph. What does this column represent? Explain the mechanism producing the second mode. Then state whether these encounters should be excluded from the analysis, and defend your answer.

Followed by auto-graded check MC-3. This is the module's central teachable moment, and the exclusion question is deliberate bait.

### Core Exercise 4: The operational view (about 15 minutes, 1 submission)

Build an ECDF: `stat_ecdf()` with `colour = factor(month)`.

**Submit:** your chart plus your reading of the fraction of patients exceeding 8 hours in January versus December. Which display would you put in front of an operations director, and why?

### Extension A: Log scale (about 10 minutes, optional)

Replace the histogram's linear x-axis with `scale_x_log10()`.

**Submit:** what becomes visible, what becomes harder to read, and whether you would use this for a board audience.

### Extension B: Choosing the threshold (about 10 minutes, optional)

Modify the summary table to report the 95th percentile instead of the 90th.

**Submit:** does your conclusion change? Should the choice of percentile be made before or after seeing the results, and why does that matter?

### Tier 3: Author (optional this cohort, graded default post-Toolbox)

No starter code.

> The Chief Operating Officer has a five-minute slot at the board meeting and has asked you for one chart, plus two sentences of interpretation, that accurately represents ED performance in 2026.

Build it. In an accompanying paragraph, justify your choice of display against one alternative you rejected, and state what decision your chart supports that the current mean-based chart does not.

Deliberately underspecified. Multiple correct answers exist (faceted density, ECDF, a p90 trend line, a stacked tail-share area chart). The justification is graded, not the chart type.

## 7. Critique set

Flawed charts to diagnose and repair. Generation code in `critique_charts.R`.

**C1. The dynamite plot.** Mean LOS by ESI level with SE error bars. ESI 1 (n = 66) appears as a confident bar with tight whiskers. *Diagnosis:* n is invisible; SE describes estimate precision, not patient experience; the ESI 1 estimate is unstable (SE 35.9 vs 2.1). *Repair:* box or jittered points with n labelled.

**C2. The truncated axis.** Monthly mean LOS with y-axis from 180 to 210. A 4.5 percent drift fills the panel and looks like a crisis. *Diagnosis:* two errors at once, an axis that exaggerates a trivial change and a statistic that conceals the real one. *Repair:* zero baseline for the bar, and a different statistic entirely. This is the one chart in the set where fixing the obvious flaw still leaves the chart wrong, which is the point.

**C3. The average of averages.** A table computing "overall mean LOS" as the unweighted mean of the discharged and admitted means: 266 minutes against a true 195. *Diagnosis:* averaging averages ignores group size. *Repair:* weight by n, or report groups separately.

Each critique asks: what is concealed, who is harmed by the concealment, what would you build instead.

## 8. Assessment

### 8.1 Recognition (C4.1)

**A1.** A hospital reports mean wait time is unchanged year over year. Give two distinct situations consistent with that, only one of which means nothing has changed.

**A2.** Which of these can a box plot not reveal? (a) median (b) skew (c) bimodality (d) outliers. Justify in one sentence.

**A3.** A bar chart shows mean cost by service line. State three things it does not tell you that you would need before acting.

### 8.2 Application (C4.2)

**A4.** (supplied dataset, `effect = "trivial"` variant) Produce the display you consider most appropriate and justify it against one rejected alternative. Full credit is available for concluding that a summary statistic is sufficient, provided the justification is sound.

**A5.** You have 4,000 encounters across 6 service lines for a clinical audience. Choose a display and defend it against a rejected alternative. Address why your choice does not collapse under overplotting.

**A6.** Given an ECDF of wait times for two clinics, state which clinic you would rather be treated at, and identify the fact that makes the two clinics' medians misleading.

### 8.3 Judgment and transfer (C4.3)

**A7.** (`effect = "null"` variant, unlabelled) A director believes wait times deteriorated and asks you to demonstrate it. Analyze the data and write your response. Scored primarily on whether the student reports the absence of an effect rather than manufacturing one.

**A8.** A quality dashboard reports median door-to-doc time, which has improved for six straight quarters. Complaints about long waits have risen over the same period. Explain how both can be true, and specify what you would add to the dashboard.

**A9.** (Synthesis, exam-scale) Given a fresh dataset and a stated operational decision: choose your statistic, build a display, and write a 250-word recommendation. Grading weights C4.3 at 50 percent.

### 8.4 Auto-graded misconception checks (D2L quiz items)

These substitute for the instructor noticing a puzzled face. Low-stakes or ungraded; the value is entirely in the distractor feedback, which must be written for the specific wrong answer rather than as a generic "incorrect." Deploy immediately after the linked exercise while the student still has the chart open.

**MC-1. After Core Exercise 1.**

> A box plot of admitted-patient LOS in December shows median 356 min, Q1 240, Q3 776. What can you conclude about the shape of this distribution?

| Option | Feedback |
|---|---|
| (a) It is right-skewed | Partially right. The long upper box does indicate skew. But there is a further feature this box plot cannot show. Re-run the density plot for the same subset and compare. |
| (b) It is bimodal | True, but not knowable from this chart. The distribution is bimodal, but you are importing that from the density plot. A box plot cannot show it. That is the point. |
| (c) Nothing about shape beyond skew and spread | **Correct.** A box plot reports five numbers. Bimodal, uniform, and skewed-unimodal distributions can produce nearly identical boxes. This is the box plot's blind spot, and it is exactly the structure this dataset contains. |
| (d) It is approximately normal | No. Q3 minus median is 420 min while median minus Q1 is 116 min, which rules out normality. The more important question is what the box plot still cannot tell you even after you notice the skew. |

**MC-2. After the Critique Set (C1).**

> The error bars in chart C1 show standard error. For ESI 1 (n = 66), SE is 35.9 minutes. What does this tell a reader?

| Option | Feedback |
|---|---|
| (a) Most ESI 1 patients have LOS within about 36 min of the mean | The most common error in this module. That would be the standard deviation, which is 291 min here, eight times larger. SE describes how precisely the mean is estimated, not how much patients vary. |
| (b) The mean for ESI 1 is imprecisely estimated relative to other groups | **Correct.** SE shrinks with sample size. ESI 1's 35.9 against ESI 4's 2.1 reflects n = 66 versus n = 2,511. |
| (c) ESI 1 patients are more variable than other groups | Not from this number. They are more variable (SD 291 vs 106), but SE cannot tell you that, because SE mixes variability with sample size. Use SD, or show the distribution. |
| (d) The ESI 1 result is statistically significant | SE alone establishes nothing about significance, and no comparison has been specified. Significant compared to what? |

**MC-3. After Core Exercise 3.** Highest-value item in the module.

> You have found that 46 percent of admitted patients in December were boarded, producing a second peak above 12 hours. A colleague suggests excluding boarded encounters so the LOS metric reflects "normal ED operations." Best response?

| Option | Feedback |
|---|---|
| (a) Agree; they are outliers distorting the metric | This is the error the module exists to prevent. These are not data errors. They are the patients experiencing the worst outcomes in the department. Excluding them reports a system that looks healthy while patients wait twelve hours in hallways. |
| (b) Agree, but document the exclusion | Documentation does not fix it. A footnote does not restore information to a decision-maker reading the headline number. The exclusion still hides the department's most consequential trend. |
| (c) Disagree; these encounters are the finding, and the metric should be reported in a way that shows them | **Correct.** The tail is the outcome of interest. Change the display or the statistic, not the data. Report boarded and non-boarded separately, or report tail mass directly. |
| (d) Disagree; excluding data is never acceptable | Right conclusion, wrong reason. Exclusion is sometimes legitimate: duplicates, impossible values, encounters outside the population of interest. What makes it wrong here is that these are real patients with real outcomes, and they are the ones the analysis exists to serve. |

### 8.5 Discussion prompt (D2L, 250 words plus two replies)

Built on the cohort's clinical experience. This converts the fact that nearly every student works in a hospital into teaching content, and makes the post substantially harder to generate without the student's own observations.

> Identify a metric your institution reports that you believe misrepresents what you actually observe on the floor. What is the summary hiding: skew, two groups pooled together, an unequal denominator, or a tail? Who is affected by the concealment, and who benefits from it? What would you add to the report to make it honest, and what would that cost?
>
> In your replies, look for a pattern. Does the metric your classmate describes conceal the same mechanism as yours, or a different one?

Exercises C4.3 directly. Students not currently in a clinical setting may use a published metric, but should say so.

## 9. Instructor notes

### Common misconceptions

**"Skewed means you should use the median."** Not necessarily. For capacity and cost the mean is correct because it multiplies by n. The statistic follows the decision, not the shape.

**"Always show the whole distribution."** The overcorrection this module tends to produce. Segment C.2 and item A4 exist to counter it. Credit correct summarization explicitly, or students learn that distributions are always the graded answer.

**"Box plots are the safe choice."** The most consequential misconception here, because it is half right and produces confident blindness to exactly this module's structure. Core Exercise 1 and MC-1 exist to break it. Do not cut either.

**Confusing SD with SE.** Predictable, and in asynchronous delivery invisible unless checked. That is what MC-2 is for.

**Reading the second mode as an error.** Students frequently propose filtering the boarding patients as outliers. In a live classroom this is the teachable moment of the module and you would sit on it. Asynchronously it passes silently unless provoked, which is why Core Exercise 3 asks the exclusion question directly and MC-3 grades the answer.

### The `boarded` column

It is the answer key. Three options:

1. **Ship it (default).** Students find the mechanism themselves in Core Exercise 3. Best for the transitional cohort.
2. **Withhold it, release after Core Exercise 2.** Harder, better discovery.
3. **Withhold permanently for assessment variants,** so the mechanism must be inferred.

### Guest speaker (enrichment, never prerequisite)

An ED operations director or charge nurse describing boarding makes the tail concrete in a way no chart can. Live on Zoom for students who can schedule it, always recorded.

Nothing in the lab or assessment depends on it. A student who watches the recording during exam week rather than module week loses no credit. This is a deliberate constraint of the asynchronous format, not an underuse of the speaker.

Ask the speaker to address three things: what the daily dashboard shows, whether it matches what the floor experiences, and what happened the last time a metric improved while the department felt worse. Fifteen minutes plus questions. Request that third item specifically. It is the one that is quotable in the discussion thread for students who could not attend live.

### Cutting for time

- **Full slot (about 2.1 hours):** everything.
- **Reduced (about 1.5 hours):** drop both Extensions. Keep Core Exercises 1 to 4 and all three MC checks.
- **Minimum viable (about 50 minutes):** Segments A and B, Observation Set Q1 to Q4, Core Exercises 1 and 3, MC-1 and MC-3. This retains the competency. Below this the module becomes a demonstration rather than a skill.

Note that the MC checks survive every cut. Asynchronously they are cheaper than the exercises and catch more.

### Module pairing

Pair with Module 05 (rates and denominators) in the same week. The hand-off runs through ESI 1 at n = 66: this module raises small-denominator instability, Module 05 answers it. Across a week boundary that connection weakens considerably.

### Submission format

Students submit an R script plus rendered output (knitted HTML, or one PNG per exercise). This replaces the packaged `.twbx` workbooks the current course requires. Consequences worth noting: files are far smaller, they open without any software installed, they are reviewable on a phone between cases, and the code portion can be partially auto-checked. Across seven weeks this is a material reduction in grading load, which matters when the same two people are building the rest of the program.

### Thread hand-offs

- **To Module 05 (rates and denominators):** ESI 1 at n = 66 raises "is this rate stable," which Module 05 answers.
- **To Module 06 (uncertainty):** SE instability in C1 and MC-2 is the direct set-up.
- **To Module 08 (time):** the p90 trend line is a run chart waiting to happen.
- **To QI thread:** the distinction between a metric improving and a system improving is the core QI measurement problem.
- **To ethics thread:** Segment C.1 raises measuring what is reported versus what matters. Do not resolve it here; flag it and hand off.

### Open questions for review

1. Does this module carry one slot, or does the ECDF material justify expansion?
2. Is the CMS median framing too US-specific if the program recruits internationally?
3. Should `boarded` ship by default, or is discovery worth the added difficulty for the transitional cohort?
4. Is nine components the right template granularity, or is this over-specified for a two-person build?
5. Are three auto-graded MC checks per module sustainable across 13 modules, or should they be reserved for the two or three highest-risk misconceptions program-wide? At roughly 45 minutes of authoring each, three per module across 13 modules is about 30 hours.
6. Seven D2L submission points per module is 91 across the course. Is that within tolerance for D2L gradebook management, or should the four core exercises collapse to a single submission with four parts?
