# DA-730: Analyzing, Viz, and Storytelling with Data

> Source: course redesign document by Ali Goff, provided by Shuhan He for the Open Clinical Learning Commons.
>
> Conversion note: converted from `Document.docx` to GitHub Markdown on 2026-08-15 with tracked changes included. The wording and document order are preserved; Word formatting is represented in Markdown where possible.
>
> Source DOCX SHA-256: `9D7558B60C928C77DF3427CF36F7353216B18BAE3716FD1BA947F7017A23CE20`

## **Pressing issues with current course structure**

The syllabus promises four objectives: chart selection, visual design
principles (color theory, typography, layout), building visualizations
in Tableau, and communicating to diverse audiences. Only the third is
actually taught and is the least relevant.

1.  The COVID data students are asked to use for exams, etc. is no
    longer updated. Last year there were large gaps in the data, who
    knows if there will be any data to use at all this year. That
    dataset does not produce worthwhile visualizations and can no longer
    be used.

2.  Tableau is essentially obsolete for the types of students we get and
    certainly in this program. Students use it just for this course and
    then never use it again. It is complicated and fiddly and most of
    the course ends up being more about teaching tableau than teaching
    when and how to construct different types of visualizations that are
    relevant for health care data analytics. For the rest of the
    program, students learn R.

3.  Furthermore, Tableau is crowding out the concepts: a review of the
    course slides confirms the total absence of foundational concepts
    like **color theory**, **typography**, or **accessibility**.

    1.  There is no framework for chart selection or encoding judgment.

    2.  *Storytelling* is reduced to a single screenshot of the Tableau
        dashboard interface in Module 5.

    3.  Rather than teaching visualization principles, the decks
        function as mechanical click-paths for creating calculated
        fields and adjusting labels.

    4.  The syllabus claims to cover design and communication, but the
        actual content delivers predominantly software instruction.

4.  Severe healthcare gap: Zero of the 13 modules use a real healthcare
    dataset. The teaching datasets are office supplies, unemployment
    survey data, EU superstore, UK banking customers, car sales, US city
    population, a financial sample, World Cup soccer, global superstore,
    and FIFA player ratings. The single exception is Module 7's
    synthetic table of Hospital ID / Marketing Spend / Revenue, which is
    a marketing dataset with the word "hospital" in a column.

    1.  The exams *do* use healthcare data: HCUP length-of-stay and
        cost, Canadian facility locations, the UCI diabetes dataset.
        Students are assessed on healthcare data they were never once
        shown in a lecture.

5.  The assigned literature is effectively a collection of Tableau
    promotional assets, ranging from "Why visual analytics?" and
    dashboard best-practice guides to a BARC report openly sponsored by
    the vendor. Canonical voices like Tufte, Cairo, Knaflic, or
    Cleveland and McGill are entirely absent; there is zero engagement
    with peer-reviewed scholarship. Furthermore, the reading list
    evaporates after Module 5, leaving over half the course without the
    curricular support the syllabus promises.

## **Long-term program structure change beginning Sept 2027**

Collapsed Toolbox series into Toolbox 1 & 2 (one semester).

Toolbox 1 & 2 then serve as prerequisites to all other courses.

All other courses (~7): “Data analytics for X”

- X = some core facet of health care analytics

All material covered in courses taught under old program structure will
be covered across the “Data analytics for X” courses.

**Fall 2026 re-make of DA-730:**

Current course re-design eventually dissolves into the X courses.

- The components of this “bridge” DA-730 should be extractable for
  placement into the new course structure.

## **The organizing principle**

Separate three layers that the current course fuses together:

**The module** is the durable unit. It owns one visualization
competency, is written to be domain-independent at its core, and
survives into any X course.

**The domain instantiation** is the swappable skin. Same competency,
different clinical context. A module ships with two or three alternates
so that when it lands in "Data Analytics for the Emergency Department"
it uses ED data, and in "Data Analytics for Population Health" it uses
something else, without the concept content being rewritten.

**The wrapper** is the seven-week sequence, the exam schedule, the
discussion prompts. This is disposable.

The R scaffolding is a fourth thing, and I'd deliberately keep it *out*
of the module structure. It's a parallel support layer for the
transitional cohort, not a module slot, because in a year it becomes
unnecessary and you don't want to be surgically removing it from your
content.

## **Proposed module inventory**

Eleven modules filling thirteen slots. Two get double slots because they
carry the most weight.

**Foundations**

1.  **Encoding and the grammar of graphics.** What a visualization
    actually is: variables mapped to visual channels. Introduces geom,
    aesthetic, scale as the vocabulary for every later decision. This is
    the module that replaces "here is the Show Me menu" with "here is
    why a chart is the shape it is."

2.  **Perception and the accuracy ranking.** Why position beats length
    beats angle beats area beats color intensity. Cleveland and McGill,
    preattentive processing. This is the empirical backbone that makes
    chart selection a defensible decision instead of a taste preference,
    and its absence is why the current course can't teach judgment.

3.  **Chart selection in practice** *(two slots).* The decision
    framework: what question, what data types, what comparison. Students
    work from question to chart repeatedly, including cases where the
    honest answer is a table or no chart at all.

**Reading data honestly**

4.  **Distributions versus summaries.** The bar-chart-of-means problem.
    Skew, bimodality, when a mean lies. Health care is full of this:
    length of stay, cost, wait times are all right-skewed with tails
    that matter clinically.

5.  **Rates, denominators, and adjustment.** Counts versus rates, why a
    choropleth of raw counts is a population map, crude versus adjusted
    comparison. <u>This one is close to non-negotiable for health care
    and appears nowhere in the current course.</u>

6.  **Uncertainty and variation** *(two slots).* Confidence and
    prediction intervals, sampling noise, small denominators,
    distinguishing signal from normal variation. Directly feeds the QI
    thread, since control chart logic is the same idea.

**Encoding craft**

7.  **Color.** Sequential, diverging, qualitative. Colorblind-safe
    palettes. When color carries information versus decorates. Clinical
    color semantics and where red-green conventions break.

8.  **Time.** Trend, seasonality, indexing, aspect ratio and the lie
    factor, run charts and SPC. Pairs naturally with any forecasting X
    course.

9.  **Comparison and small multiples.** Faceting, ordering, shared
    scales, the alternatives to overloading one panel.

10. **Maps and geography.** When geography is the point and when it is a
    distraction. Choropleth pitfalls, binning, the modifiable areal unit
    problem in plain language.

**Communication**

11. **Audience, annotation, and composition** *(this absorbs
    dashboards).* Same analysis, three audiences: clinician, executive,
    patient. Titles that state findings rather than label axes.
    Multi-view composition and what a dashboard is actually for.

You'll notice misleading visualizations and visualization ethics aren't
a module. I'd thread them through instead: every module includes a
critique exercise using a flawed chart of that module's type, and the
equity dimension (disaggregation, small cell suppression, whose
comparison is the baseline) lives inside modules 4, 5, and 10 where it's
concrete. A standalone ethics module in a viz course tends to become a
lecture students nod through. Embedded, it's a diagnosis they perform.

## **The module spec**

This is the part that makes portability real. Every module ships as the
same nine components:

1.  **Competency statement.** One sentence, assessable. "Given a
    research question and a dataset, select and justify an appropriate
    visual encoding."

2.  **Prerequisites.** Which modules must precede it.

3.  **Concept core.** 15 to 25 minutes, domain-independent and
    tool-independent. This is what never changes.

4.  **Domain instantiation.** The worked example, with two or three
    alternates.

5.  **Dataset specification.** Discussed below. The most important
    component.

6.  **Lab.** R and ggplot2, in three scaffold tiers.

7.  **Critique set.** Two or three flawed charts to diagnose and repair.

8.  **Assessment items.** Tagged to the competency, at multiple
    difficulty levels.

9.  **Instructor notes.** Common misconceptions, what a guest speaker
    could add, what to cut if short on time.

## **The dataset specification, and why it matters most**

Don't attach datasets to modules. Attach *specifications* of what the
data must contain for the lesson to land.

For module 4, the spec reads something like: the primary continuous
variable must be right-skewed with a long upper tail; mean and median
must differ by at least 30%; a secondary mode must exist in one subgroup
and be invisible in the aggregate; group sizes must be unequal enough
that unweighted averaging misleads.

That spec is satisfiable by, e.g., ED length of stay, by chemotherapy
infusion duration, by claims cost, by clinic wait time. The X instructor
generates data meeting the spec in their domain, and the module works
unchanged. Without the spec, the module is welded to whatever dataset
you happened to build, and porting it means redesigning the lesson.

This is exactly the leverage you get from synthetic data. You're not
looking for data that happens to teach something. You state the
pedagogical requirement first and generate it.

I'd also keep the specs honest per our earlier conversation: some should
specify a real effect, some a null, some an effect that is statistically
detectable and clinically trivial.

## **The scaffold layer**

Three tiers, same lab, so the tier is a support level rather than a
different assignment:

**Tier 1, run and observe.** Complete script provided. Run it, read the
output, answer questions about what the chart shows and what decision it
supports. No R authoring.

**Tier 2, modify.** Working script with specific changes requested.
Change the geom and explain what was gained or lost. Swap the variable
on color to the one on facet. Fix the scale. This is where the
visualization learning actually happens, and it requires no ability to
write R from scratch.

**Tier 3, author.** Build from the data and the question.

For the transitional cohort, run everything through tier 2 with tier 3
optional. Post-overhaul, tier 1 disappears and tier 3 becomes the
default. The tiers are metadata on the lab, not separate content, so the
transition costs you a flag change rather than a rewrite.

Plus a short Toolbox bridge: a Posit Cloud workspace, a one-page
tidyverse reference limited to the six or seven verbs this course needs,
and an optional onboarding module in week zero. All of it disposable.

## **What this means for next semester specifically**

Thirteen slots, eleven modules, and the wrapper is thin: an assembly
order, discussion prompts, and assessments. Assessment needs rebuilding
regardless, since roughly two thirds of the current exam points test
Tableau trivia that will not exist.

# Model 4 Example: Distributions versus summaries (Notes)

All nine components, plus a verified dataset and two R scripts.

The scenario: An ED launches a fast-track pathway. Twelve months later
the median LOS has fallen 37%, from 164 to 102 minutes, and the
CMS-reported metric confirms it. Meanwhile the 90th percentile has
doubled and the share of patients staying over eight hours has
quadrupled.

Both facts are correctly measured. The fast track genuinely worked, and
inpatient boarding grew from 10% to 46% of admitted patients over the
same period. Two real opposing changes: the mean cancels them, and the
median, dominated by the 77% of encounters that are discharges, reports
only the good one. The decision that turns on this is concrete:
expanding fast track addresses a solved problem and does nothing for the
deteriorating group.

What makes it work pedagogically is that nothing in it is contrived.
Fast-track pathways are real and effective, boarding is the dominant US
ED crisis, and the CMS ED throughput measure really does use a median.
Every element a skeptical student might dismiss as a set-up is an actual
feature of the domain.

# Module 04: Distributions versus Summaries

**Thread:** Visualization **Tier:** Health care essential **Version:**
0.1 draft for Goff / Pedram / He review **Status of this document:**
template test case. The nine-component structure is under evaluation
alongside the content.

| **Field** | **Value** |
|----|----|
| Slot cost | 1 module |
| Concept core runtime | ~22 min |
| Lab runtime | 60 to 90 min depending on tier |
| Canonical dataset | ed_los_2026.csv (8,392 rows) |
| Generator | generate_ed_los.R |
| Tool | R / ggplot2 |
| Portability | High. Domain-independent core; four alternates specified. |

## 1. Competency statement

> Given a dataset and a comparison question, the student determines
> whether a summary statistic faithfully represents the underlying
> distribution, and selects a display that reveals the distributional
> features relevant to the decision at hand.

Three observable behaviors, used directly as the assessment rubric:

**C4.1 Diagnose.** Identify when a reported summary is concealing skew,
multimodality, unequal group sizes, or a consequential tail.

**C4.2 Select and justify.** Choose a display appropriate to the
distribution and the decision, and defend the choice against at least
one alternative. This includes correctly judging that a summary is
*sufficient*.

**C4.3 Connect to consequence.** State what decision changes when the
distribution is revealed rather than summarized.

C4.3 is the one that distinguishes this from a statistics exercise. A
student who produces a beautiful faceted density plot but cannot say
what the ED should do differently has not met the competency.

## 2. Prerequisites

**Within-thread:** Module 01 (encoding and grammar of graphics), Module
02 (perception and the accuracy ranking), Module 03 (chart selection in
practice).

(Module 02 matters most. This module argues that a bar of means is the
wrong encoding; that argument only lands for a student who already knows
encodings can be ranked on evidence rather than taste.)

**From Toolbox:** mean, median, SD, quantiles, histograms. Ability to
run and modify a supplied R script. No modeling required.

**Assumed of a transitional (pre-Toolbox) student:** nothing beyond
running supplied code. See section 6.

## 3. Concept core

Domain-independent and tool-independent. This is the component that
never changes when the module ports to another X course.

### 3.1 Every summary is a lossy compression

A summary statistic replaces many numbers with few. That is its purpose.
The question is never "is this summary correct" but rather:

> **Does what this summary discards matter for the decision being
> made?**

That is the whole module. Everything below is machinery for answering
it.

Anscombe's quartet and the Datasaurus Dozen are the canonical
demonstrations: datasets with identical means, variances, and
correlations that look nothing alike. Use one briefly. Do not dwell;
students find them charming and then fail to generalize. The
generalization is the point.

### 3.2 What a bar chart of means discards

A bar encodes exactly one number per group, yet occupies area that
implies mass where none was measured. It discards:

- **Shape.** Symmetric, skewed, and bimodal data produce identical bars.

- **Spread.** No indication whether values cluster tightly or scatter.

- **n.** A bar over 12 observations looks identical to one over 12,000.

- **The individual.** In health care the individual is often the entire
  point.

Adding a standard error bar addresses spread only, and does so
misleadingly: SE describes precision of the estimated mean, not the
range of patient experience. A narrow SE bar on 4,000 encounters signals
a well-estimated mean, not a consistent one.

### 3.3 Four mechanisms by which a summary hides something

| **Mechanism** | **What the mean does** | **Health care instance** |
|----|----|----|
| **Skew** | Pulled toward the tail, describing nobody typical | Cost, LOS, wait time are all right-skewed |
| **Multimodality** | Lands between two real groups, describing neither | Two care pathways pooled into one metric |
| **Unequal group sizes** | Dominated by the largest group | Discharged patients swamp admitted patients |
| **Consequential tail** | Treats extremes as noise | The tail is the harmed patient |

The fourth is where health care differs from most analytics domains. In
retail the tail is a rounding error. In clinical operations the tail is
the patient who waited fourteen hours in a hallway. **Reporting the
center while the tail is the outcome of interest is the characteristic
analytic failure of this field.**

### 3.4 The disaggregation reflex

Teach this as a habit, not an insight:

> When a summary looks stable, split it before believing it.

Split by the variable that plausibly separates care pathways. If the
subgroups look like the whole, the summary was honest and you have
earned confidence in it. If they do not, you have found the story.

Stability is not evidence of nothing happening. Offsetting movements
produce a flat mean, and a flat mean is exactly what an unchanging
system and two large opposing changes have in common.

### 3.5 The ladder of displays

Each rung reveals more and costs more space and audience effort.
Climbing higher is not automatically better; the correct rung is the
lowest one that supports the decision.

| **Rung** | **Display** | **Reveals** | **Blind to** |
|----|----|----|----|
| 1 | Bar of means | Central tendency | Everything else |
| 2 | Mean with error bar | Precision of the estimate | Shape, n, spread of the data |
| 3 | Box plot | Median, quartiles, extremes | **Multimodality** |
| 4 | Box or violin with jittered points | Shape, n, individuals | Cluttered above ~1,000 points |
| 5 | Histogram or density | Full shape | Group comparison, unless faceted |
| 6 | Faceted density or ridgeline | Shape across groups | Precise values |
| 7 | ECDF | All percentiles at once, honest about n | Unfamiliar to most audiences |

Two things students consistently need told:

**The box plot has its own blind spot.** A box plot cannot show
multimodality. A bimodal distribution and a uniform one can produce
nearly identical boxes. Students who learn "box plots are the
responsible choice" will confidently miss the exact structure this
module is about. The lab demonstrates this directly.

**The ECDF is underused and worth teaching.** It answers "what fraction
of patients waited longer than X" for every X simultaneously, which is
usually the operational question. It costs unfamiliarity, so it belongs
in an analyst-facing view rather than a board slide.

### 3.6 Choose the statistic that matches the decision

The center is often the wrong number.

| **The decision is about** | **The right statistic** |
|----|----|
| Total burden, capacity, cost | Mean (it multiplies by n) |
| The typical patient | Median |
| Staffing so most patients are served | 90th percentile |
| Preventing harm | Tail mass: % over threshold |
| Regulatory compliance | Whatever the measure specifies, which may be none of the above |

That last row is worth a minute of lecture. CMS ED throughput measures
use **median** time. A department can improve its reported median while
the experience of its worst-served patients deteriorates sharply, and
both facts are true and correctly measured. This is not a hypothetical;
it is the lab.

### 3.7 When a summary is the right answer

Resist teaching "always show the distribution." That trades one reflex
for another.

A summary suffices when the distribution is roughly symmetric and
unimodal, n is large and stable, the decision genuinely depends on the
center, and the audience cannot absorb more. A board deck with twelve
distributions communicates less than a board deck with one number and a
footnote.

The competency is judgment about which situation you are in. C4.2
explicitly credits a correct decision to summarize.

### 3.8 Assigned readings

Replaces the current Tableau vendor collateral with peer-reviewed
biomedical literature.

- **Weissgerber TL, Milic NM, Winham SJ, Garovic VD (2015).** Beyond bar
  and line graphs: time for a new data presentation paradigm. *PLOS
  Biology* 13(4): e1002128. **Primary reading.** Open access,
  biomedical, and it makes precisely this module's argument with real
  published examples.

- **Streit M, Gehlenborg N (2014).** Bar charts and box plots. *Nature
  Methods* 11(2): 117. One page. Assign as a companion.

- *Optional:* **Rousselet GA, Pernet CR, Wilcox RR (2017).** Beyond
  differences in means. *European Journal of Neuroscience* 46(2):
  1738-1748.

## 4. Domain instantiation

### 4.1 Primary: emergency department length of stay

**Scenario given to students.**

You are the analyst for an ED that launched a fast-track pathway in
January 2026. Twelve months on, the department reports success: median
length of stay fell from 164 to 102 minutes, a 37% improvement, and the
CMS-reported metric confirms it. Leadership wants to expand the pathway
and has asked you for a chart for the board.

Before you build it, look at the distribution.

**What the data actually contains.** Verified in the shipped file:

| **Metric**                 | **Jan 2026** | **Dec 2026** | **Change**  |
|----------------------------|--------------|--------------|-------------|
| Mean LOS                   | 192 min      | 201 min      | +4.5%       |
| **Median LOS**             | **164 min**  | **102 min**  | **-37.3%**  |
| 90th percentile            | 297 min      | 606 min      | **+104.1%** |
| Share staying over 8 hours | 2.7%         | 11.2%        | **4.1x**    |

Both headline summaries say the department improved or held steady. The
90th percentile doubled. The share of patients held longer than eight
hours quadrupled.

Both stories are true. The fast-track pathway genuinely worked:
discharged patients move much faster. Simultaneously, inpatient capacity
tightened and boarding grew from 10% to 46% of admitted patients. Two
real, opposing changes. The mean cancels them. The median, dominated by
the 77% of encounters that are discharges, reports only the good one.

**The decision that turns on this.** Expanding fast track addresses a
problem that is already solved and does nothing for the deteriorating
group. The distribution redirects the intervention from ED throughput to
inpatient capacity. That is C4.3, and it is the reason this scenario was
chosen over a purely statistical one.

**Why this instantiation earns its slot.** It is not a contrived trap.
Fast-track pathways are real, they work, boarding is the dominant US ED
crisis, and the CMS measure really is a median. Every element a student
might dismiss as artificial is a feature of the actual domain.

### 4.2 Alternates

Same competency, same spec, different X course. Each keeps the
two-component mixture in the minority group.

| **Course**    | **Outcome**         | **Groups**   | **What mode 2 represents**   |
|---------------|---------------------|--------------|------------------------------|
| Oncology      | Infusion chair time | Regimen      | Pharmacy turnaround delays   |
| Ambulatory    | Clinic wait time    | Visit type   | Double-booked slots          |
| Revenue cycle | Cost per admission  | DRG class    | Complication-driven outliers |
| Perioperative | Case duration       | Service line | Add-on emergency cases       |

## 5. Dataset specification

**This is the portable artifact.** The module travels as a spec, not as
a file. An X instructor generates data meeting the spec in their own
domain and the module works unchanged. Written the other way around, the
lesson would be welded to one CSV.

### 5.1 Required conditions

| **\#** | **Condition** | **Threshold** | **Teaches** |
|----|----|----|----|
| 1 | Primary outcome right-skewed | mean/median \>= 1.20 | Mean misrepresents the typical case |
| 2 | Unequal group sizes | ratio \>= 2.5:1 | Pooled summary tracks the majority group |
| 3 | Two-component mixture in the minority group, invisible when pooled | Minority: 2 modes, secondary \>= 25% of peak height. Pooled: secondary \<= 15% | Disaggregation reveals structure |
| 4 | Opposing time trends that cancel in the mean | Mean drift \< 6%; p90 drift \> +40% | Stability is not evidence of nothing happening |
| 5 | A rare subgroup | at least one group n \< 100 | Small-denominator instability (hands off to Module 06) |
| 6 | Unweighted group means diverge from pooled mean | \>= 30 min | Averaging averages is not averaging |

### 5.2 Verified realization

ed_los_2026.csv, 8,392 encounters, calendar year 2026, seed 730.

| **\#** | **Condition** | **Achieved** |  |
|----|----|----|----|
| 1 | Skew | mean 194.7 / median 138 = **1.41** | PASS |
| 2 | Group ratio | 6,462 discharged : 1,930 admitted = **3.35:1** | PASS |
| 3 | Mixture | Admitted: modes at **252** and **782** min (secondary 36% height). Pooled: secondary shoulder at **13%** | PASS |
| 4 | Opposing trends | mean **+4.5%**, p90 **+104.1%** | PASS |
| 5 | Rare subgroup | ESI 1: **n = 66**, SE 35.9 min vs 2.1 for ESI 4 | PASS |
| 6 | Unweighted vs pooled | 266 vs 195 = **+71 min** | PASS |

Condition 3 is the delicate one. The pooled secondary mode sits at 13%
of peak height: a faint shoulder in a histogram, invisible in a bar
chart or box plot, unmistakable when faceted by disposition. That
gradient is deliberate. A student who looks carefully at the pooled
histogram is rewarded with a hint rather than handed the answer.

Note also that box plot quartiles for admitted patients move only
modestly (Q1 219 to 240, median 260 to 356) while Q3 moves 321 to 776.
The box plot *understates* the change, which sets up the rung-3 blind
spot demonstration in the lab.

### 5.3 Columns

| **Column**   | **Type** | **Notes**                                      |
|--------------|----------|------------------------------------------------|
| encounter_id | chr      |                                                |
| arrival_date | date     | 2026-01-01 to 2026-12-28                       |
| esi          | int      | 1 (most acute) to 5. ESI 1 deliberately rare.  |
| age_group    | chr      | 18-39, 40-64, 65-79, 80+                       |
| disposition  | chr      | Admitted / Discharged                          |
| boarded      | int      | 0/1. **The answer key.** See instructor notes. |
| los_min      | int      | Arrival to departure, minutes                  |

### 5.4 Effect variants

Per the program principle that not every analysis may return a finding,
the generator ships three variants:

- effect = "real" (default, shipped): deterioration concealed by the
  summary.

- effect = "null": genuinely nothing happening. A student who has
  learned to always find a hidden crisis will fabricate one here. That
  failure is worth catching in a low-stakes module.

- effect = "trivial": a real, statistically detectable, clinically
  negligible shift. The correct answer is "do not act on this."

Use "real" for the lab. Reserve "null" and "trivial" for assessment so
the finding cannot be assumed.

## 6. Lab

One lab, three scaffold tiers. The tiers are a support level on the same
assignment, not different assignments, so a mixed-preparation cohort
produces comparable work.

**Environment:** Posit Cloud workspace, dataset pre-loaded, no local
installation.

**Transitional cohort (Fall 2026):** everyone completes Tier 1 and Tier
2. Tier 3 optional and ungraded. **Post-Toolbox:** Tier 1 dropped, Tier
3 becomes the graded default.

### Tier 1: Run and observe

Complete script supplied. Students run it and answer questions. No R
authoring.

library(tidyverse)

ed \<- read_csv("ed_los_2026.csv") \|\>

mutate(month = floor_date(arrival_date, "month"))

\# The chart leadership is currently looking at

ed \|\>

group_by(month) \|\>

summarise(mean_los = mean(los_min)) \|\>

ggplot(aes(month, mean_los)) +

geom_col(fill = "steelblue") +

labs(title = "Mean ED length of stay by month, 2026",

x = NULL, y = "Mean LOS (minutes)")

**Q1.** Describe the trend. Based on this chart alone, is the department
improving, worsening, or stable?

\# The same data, without summarising first

ggplot(ed, aes(los_min)) +

geom_histogram(bins = 60) +

labs(x = "LOS (minutes)", y = "Encounters")

**Q2.** Is this distribution symmetric? Where is most of the mass? Is
there anything to the right of the main peak?

ggplot(ed, aes(los_min)) +

geom_density() +

facet_wrap(~disposition, scales = "free_y") +

labs(x = "LOS (minutes)")

**Q3.** How many peaks does each panel show? What does a second peak
imply about the admitted group?

ed \|\>

group_by(month) \|\>

summarise(mean = mean(los_min), median = median(los_min),

p90 = quantile(los_min, 0.90),

pct_over_8h = 100 \* mean(los_min \> 480)) \|\>

pivot_longer(-month) \|\>

ggplot(aes(month, value)) +

geom_line(linewidth = 1) +

facet_wrap(~name, scales = "free_y") +

labs(x = NULL, y = NULL)

**Q4.** Four statistics, same data. Which say the department improved?
Which say it worsened? Explain how both can be correct.

**Q5.** The board sees only the first chart. Name one decision they
might make that the fourth would change.

### Tier 2: Modify

Working code supplied; students make specified changes and interpret.
**This tier carries the visualization learning and requires no ability
to author R.**

**T2.1** In the Q3 density plot, replace geom_density() with
geom_boxplot(aes(y = los_min, x = disposition)). Does the box plot show
the second peak? State the general principle.

**T2.2** Take the monthly mean bar chart and add
facet_wrap(~disposition). What changes? Which group drives the pooled
trend, and why?

**T2.3** Change the faceting variable from disposition to boarded. What
does this column represent? Now explain the mechanism behind the second
mode.

**T2.4** Replace the histogram's linear x-axis with scale_x_log10().
What becomes visible? What becomes harder to read? Would you use this
for a board audience?

**T2.5** Build an ECDF: stat_ecdf() with colour = factor(month). Read
off the fraction of patients exceeding 8 hours in January and December.
Which display communicates the problem best to an operations director,
and why?

**T2.6** Modify the summary table to report the 95th percentile instead
of the 90th. Does your conclusion change? Should the choice of
percentile be made before or after seeing the results, and why does that
matter?

### Tier 3: Author

No starter code.

> The Chief Operating Officer has a five-minute slot at the board
> meeting and has asked you for **one** chart, plus two sentences of
> interpretation, that accurately represents ED performance in 2026.
>
> Build it. In an accompanying paragraph, justify your choice of display
> against one alternative you rejected, and state what decision your
> chart supports that the current mean-based chart does not.

Deliberately underspecified. Multiple correct answers exist (faceted
density, ECDF, a p90 trend line, a stacked tail-share area chart). The
justification is graded, not the chart type.

## 7. Critique set

Flawed charts to diagnose and repair. Generation code in
critique_charts.R.

**C1. The dynamite plot.** Mean LOS by ESI level with SE error bars. ESI
1 (n = 66) appears as a confident bar with tight whiskers. *Diagnosis:*
n is invisible; SE describes estimate precision, not patient experience;
the ESI 1 estimate is unstable (SE 35.9 vs 2.1). *Repair:* box or
jittered points with n labelled.

**C2. The truncated axis.** Monthly mean LOS with y-axis from 180 to
210. A 4.5% drift fills the panel and looks like a crisis. *Diagnosis:*
two errors at once, an axis that exaggerates a trivial change and a
statistic that conceals the real one. *Repair:* zero baseline for the
bar, and a different statistic entirely. This is the one chart in the
set where fixing the obvious flaw still leaves the chart wrong, which is
the point.

**C3. The average of averages.** A table computing "overall mean LOS" as
the unweighted mean of the discharged and admitted means: 266 minutes
against a true 195. *Diagnosis:* averaging averages ignores group size.
*Repair:* weight by n, or report groups separately.

Each critique asks: what is concealed, who is harmed by the concealment,
what would you build instead.

## 8. Assessment items

Tagged to competency and level. Item bank; select per exam.

### Recognition (C4.1)

**A1.** A hospital reports mean wait time is unchanged year over year.
Give two distinct situations consistent with that, only one of which
means nothing has changed.

**A2.** Which of these can a box plot **not** reveal? (a) median (b)
skew (c) bimodality (d) outliers. Justify in one sentence.

**A3.** A bar chart shows mean cost by service line. State three things
it does not tell you that you would need before acting.

### Application (C4.2)

**A4.** *(supplied dataset, effect = "trivial" variant)* Produce the
display you consider most appropriate and justify it against one
rejected alternative. **Full credit is available for concluding that a
summary statistic is sufficient, provided the justification is sound.**

**A5.** You have 4,000 encounters across 6 service lines for a clinical
audience. Choose a display and defend it against a rejected alternative.
Address why your choice does not collapse under overplotting.

**A6.** Given an ECDF of wait times for two clinics, state which clinic
you would rather be treated at and identify the fact that makes the two
clinics' medians misleading.

### Judgment and transfer (C4.3)

**A7.** *(effect = "null" variant, unlabelled)* A director believes wait
times deteriorated and asks you to demonstrate it. Analyze the data and
write your response. **Scored primarily on whether the student reports
the absence of an effect rather than manufacturing one.**

**A8.** A quality dashboard reports median door-to-doc time, which has
improved for six straight quarters. Complaints about long waits have
risen over the same period. Explain how both can be true, and specify
what you would add to the dashboard.

**A9.** *(Synthesis, exam-scale)* Given a fresh dataset and a stated
operational decision: choose your statistic, build a display, and write
a 250-word recommendation. Grading weights C4.3 (what decision changes)
at 50%.

## 9. Instructor notes

### Common misconceptions

**"Skewed means you should use the median."** Not necessarily. For
capacity and cost the mean is correct because it multiplies by n. The
statistic follows the decision, not the shape.

**"Always show the whole distribution."** The overcorrection this module
tends to produce. Section 3.7 and item A4 exist to counter it. Credit
correct summarization explicitly or students learn that distributions
are always the graded answer.

**"Box plots are the safe choice."** The most consequential
misconception here, because it is half right and produces confident
blindness to exactly this module's structure. T2.1 exists to break it.
Do not skip it.

**Confusing SD with SE.** Predictable and worth ninety seconds. SE
shrinks with n; the spread of patient experience does not.

**Reading the second mode as an error.** Students frequently propose
filtering the boarding patients as outliers. This is the teachable
moment of the module: those are not bad data, they are the patients the
analysis exists to serve. Sit on this when it comes up.

### The boarded column

It is the answer key. Three options:

1.  **Ship it** (default). Students find the mechanism themselves in
    T2.3. Best for the transitional cohort.

2.  **Withhold it**, release after Tier 2. Harder, better discovery.

3.  **Withhold permanently** for assessment variants, so the mechanism
    must be inferred.

### Guest speaker

A strong fit. An ED operations director or charge nurse describing
boarding makes the tail concrete in a way no chart does. Ask them to
address: what the daily dashboard shows, whether it captures what the
floor experiences, and what happened the last time a metric improved
while the department felt worse. Fifteen minutes, before the lab rather
than after.

### Cutting for time

- **Full slot (~90 min):** everything.

- **Reduced (~60 min):** cut ECDF (T2.5) and the log scale (T2.4). Keep
  T2.1 and T2.3.

- **Minimum viable (~35 min):** sections 3.1 to 3.4, Tier 1 Q1 to Q4,
  T2.1, T2.3. This retains the competency. Below this the module becomes
  a demonstration rather than a skill.

### Thread hand-offs

- **To Module 05 (rates and denominators):** ESI 1 with n = 66 raises
  "is this rate stable," which Module 05 answers.

- **To Module 06 (uncertainty):** SE instability in C1 is the direct
  set-up.

- **To Module 08 (time):** the p90 trend line is a run chart waiting to
  happen.

- **To QI thread:** the distinction between a metric improving and a
  system improving is the core QI measurement problem.

- **To ethics thread:** section 3.6 raises measuring what is reported
  versus what matters. Do not resolve it here; flag it and hand off.

### Open questions for review

1.  Does this module carry one slot or does the ECDF material justify
    expansion?

2.  Is the CMS median framing too US-specific for a program that may
    recruit internationally?

3.  Should boarded ship by default, or is discovery worth the added
    difficulty for the transitional cohort?

4.  Is nine components the right template granularity, or is this
    over-specified for a two-person build?
