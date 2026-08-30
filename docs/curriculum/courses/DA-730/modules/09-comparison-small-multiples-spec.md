# DA-730 Module 09: Comparison and small multiples

- Course: DA-730, Clinical data visualization and decision storytelling
- Instructional position: week 5, first comparison-and-place module
- Learner time: 7.5 hours
- Module version: 0.1.0
- Target Commons release: 0.20.0
- Primary environment: R and ggplot2
- Data build and validation: Python 3 standard library
- Clinical source: CDC PLACES County Data 2024 release
- Public module package: `courses/data-visualization/modules/09-comparison-small-multiples/`

## 1. Module identity and place in the course

Module 09 teaches comparison as a set of visible decisions. Modules 01 through 08 established encoding, perception, chart selection, distribution, rates, adjustment, uncertainty, accessibility, and time. Module 09 asks learners to hold those rules steady while comparing many groups across repeated panels.

The key difficulty is not drawing a facet. It is preserving the meaning of a comparison from one panel to the next. A reader cannot compare reliably when every panel changes its scale, order, denominator, estimate type, reference, or status definition. Small multiples are useful only when repeated structure reduces mental work rather than hiding inconsistent choices.

The worked case uses 100 North Carolina counties and five CDC PLACES adult health measures. Every county has crude and age-adjusted point estimates, 95 percent confidence limits, adult population, and a matching national reference. Learners first show all counties. They then create and disclose one twelve-county partnership-readiness review rule.

This module does not teach geographic mapping. County names and FIPS codes are identifiers here, not permission to make a choropleth. Module 10 asks whether place itself contributes to the decision.

Accessibility remains cumulative. A repeated-panel display must work without color, retain readable labels and contrast, provide exact values, and include a structured text alternative.

## 2. Healthcare decision and audience

### Decision

A North Carolina population-health director can invite twelve counties into a partnership-readiness review. The review will ask whether local priorities, organizations, data, and intervention fit justify further planning.

The visualization does not decide:

- funding allocation;
- program selection;
- clinical treatment;
- causal explanation;
- county performance ratings;
- or whether a community is ready to participate.

### Decision owner

The primary decision owner is a state population-health director responsible for a fair, explainable first screen.

Supporting readers include:

- county health leaders who need to understand why their county appears or does not appear;
- epidemiologists who must verify measure definitions and uncertainty;
- equity and community-engagement colleagues who must identify what county aggregates omit;
- program staff estimating outreach scale from adult population;
- accessibility users who need the same comparison through non-color cues, text, and a table;
- data stewards who must reproduce the shortlist from the released source.

### Decision questions

The learner must answer:

1. Which 100 counties and five measures are compared?
2. Are the measure year, population, unit, and estimate type comparable?
3. What scale is shared across panels?
4. What county order is reused across panels?
5. What does each reference line mean?
6. Which estimates are crude and which are age adjusted?
7. How does uncertainty affect the reading?
8. Does the comparison denominator remain visible?
9. Which rule produces exactly twelve counties?
10. What does that rule omit?
11. What should happen after the review invitation?
12. What evidence is required before allocation or intervention?

### Required decision language

The final recommendation uses one of these forms:

- "Invite [twelve counties] to a readiness review because they meet [declared comparison rule]. Do not allocate resources from this screen alone because [material omitted factors]."
- "Revise the shortlist rule before invitation because [scale, comparator, weighting, uncertainty, denominator, or equity issue] changes who is selected."
- "Use the all-county comparison for discussion but do not create a twelve-county list until [named readiness or community evidence] is available."

The recommendation may identify point-estimate patterns. It may not describe selected counties as worst, least healthy, failing, causal, or ready for a specific intervention.

## 3. Foundation skill revisited or extended

### Foundations I skills revisited

- verify composite keys across county, measure, and estimate type;
- preserve five-character FIPS identifiers as text;
- pair crude and age-adjusted rows without losing source fields;
- validate one-to-one national references;
- calculate transparent derived fields;
- keep a stable order key across repeated outputs;
- pin a public query and release checksums;
- preserve complete source rows and exact field order;
- write a machine-readable comparison table;
- separate source, derived, and presentation fields.

### Foundations II skills revisited

- distinguish crude from age-adjusted prevalence;
- distinguish an estimate from an observed count;
- interpret a 95 percent confidence interval without inventing a pairwise test;
- compare point estimates on a common unit;
- recognize that rankings can be unstable or tied;
- understand how dichotomizing a continuous measure loses information;
- identify hidden weighting in a composite count;
- separate screening from validation and causal inference.

### Visualization foundations revisited

- use position on a common scale for accurate comparison;
- sort groups according to a declared reader task;
- keep repeated encodings consistent;
- use dot plots when a zero baseline is not part of the question;
- use dumbbells only when the two endpoints have a meaningful relation;
- use small multiples when repeated structure aids scanning;
- provide uncertainty, exact values, and text alternatives;
- avoid color-only identity and status.

### New application

The learner designs a multi-panel comparison where scale, order, comparator, panel density, and emphasis work as one system. The result must support a reproducible review list without pretending that visualization has solved priority setting.

## 4. Assessable learning outcomes

By the end of the module, a learner can:

1. state the comparison decision, group unit, measure set, population, year, and estimate type;
2. verify that every county has every required measure and estimate pair;
3. choose a dot plot, dumbbell, slope display, table, or small multiple for a stated task;
4. distinguish a shared unit from a shared clinical construct;
5. keep one absolute scale across comparable panels;
6. justify any transformation or free scale as a different question;
7. define and reuse one county order across panels;
8. explain when panel-specific sorting is useful and what cross-panel tracking it sacrifices;
9. define one comparator consistently across panels;
10. distinguish a constant comparator definition from a constant numeric value;
11. show crude and age-adjusted estimates without temporal language;
12. preserve 95 percent confidence limits and interpret overlap cautiously;
13. retain the 100-county denominator and adult population context;
14. calculate and label percentage-point differences from a national reference;
15. calculate within-measure competition ranks and handle ties correctly;
16. build exactly twelve review candidates from a visible, reproducible rule;
17. identify the hidden assumptions in equal-weight profile counts;
18. repair free scales, changing baselines, and overloaded rainbow profiles;
19. create accessible multi-panel figures, exact data, and text alternatives;
20. write a proportional review action and identify evidence needed before allocation.

### Mastery threshold

The learner earns at least 80 percent overall and passes every noncompensable condition in Section 15. A visually polished submission fails if groups disappear, comparable panels use hidden free scales, county order changes without explanation, comparator meaning shifts, the shortlist is hand selected, or a screening rule becomes an allocation claim.

## 5. Concept ownership and boundaries

### Concepts owned by Module 09

- comparison grammar across repeated panels;
- fixed and free scales as decision choices;
- shared order versus panel-specific order;
- stable comparator definitions;
- dot plots for many-group comparisons;
- dumbbells for two related estimates;
- slope displays and their valid endpoint relations;
- small multiples and faceting;
- panel density and label strategies;
- direct reference lines;
- within-measure rank and tie handling;
- transparent multi-measure screening rules;
- exact comparison denominators;
- the distinction between a screening shortlist and a priority score.

### Concepts introduced but not mastered here

- multivariate clustering;
- principal components;
- formal composite-index validation;
- rank uncertainty;
- multiple-comparison procedures;
- Bayesian small-area comparison;
- causal drivers of county differences;
- resource-allocation optimization;
- community-based priority setting;
- spatial autocorrelation.

These may be named to define limits. They are not required methods for the submission.

### Concepts owned elsewhere

- Module 03 owns the initial chart-versus-table choice.
- Module 04 owns distributions hidden by summaries.
- Module 05 owns denominators, crude rates, and age adjustment.
- Module 06 owns uncertainty and small-number judgment.
- Module 07 owns the accessibility baseline.
- Module 08 owns time order and process variation.
- Module 10 owns maps, boundaries, and geographic aggregation.
- Foundations II owns formal inference and multivariable modeling.

### Prohibited shortcuts

- changing the x scale in each comparable panel because it fills space;
- sorting each panel differently while asking a cross-panel tracking question;
- using a separate comparator without changing the status label;
- connecting different measures as though they were time points;
- using a radar chart that hides scales and exact values;
- using color alone for dozens of counties;
- showing only state or county means when within-group variation changes the decision;
- calling age-adjusted estimates improved values;
- treating rank as a precise clinical distance;
- counting measures without disclosing equal weighting;
- hand selecting twelve counties after viewing the chart;
- converting review into automatic funding.

## 6. Lesson sequence and learner time

Total expected learner time is 7.5 hours.

| Segment | Time | Mode | Product |
|---|---:|---|---|
| Decision launch and source framing | 0.5 hour | instructor-led | initial comparison question |
| Group, measure, estimate, and denominator audit | 0.75 hour | guided | comparison audit notes |
| Scale, order, and reference workshop | 0.75 hour | mini-lesson | three comparison rules |
| Ordered dot plots and small multiples | 1.0 hour | guided lab | all-county figure |
| Crude and adjusted dumbbells | 0.75 hour | guided lab | adjustment comparison |
| Confidence intervals and ranks | 0.5 hour | worked example | uncertainty note |
| Flawed-chart critique and repair | 0.75 hour | paired critique | three repair plans |
| Independent comparison and shortlist | 1.5 hours | individual work | figures and table |
| Decision note, alternatives, and verification | 1.0 hour | individual work | final package |
| Total | 7.5 hours |  |  |

### Before class

Learners complete:

- Modules 05 through 08 or the equivalent briefing;
- the Module 09 data validator;
- a short reading of CDC PLACES methodology;
- a one-paragraph explanation of crude versus age-adjusted prevalence;
- a source note defining one selected measure.

### Synchronous opening

The instructor shows the flawed rainbow chart with thirty county lines across five measures and asks:

1. Can you find one named county?
2. Does connecting the measures create a meaningful slope?
3. Which measure determines the apparent vertical pattern?
4. What would you change first if the director must name twelve counties?

The discussion should surface that fewer colors do not solve an undefined comparison. The group needs a task, order, scale, comparator, and selection rule.

### End-of-module checkpoint

Before submission, the learner reruns the analysis, confirms 500 table rows and twelve unique shortlisted counties, inspects fixed scales and county order, checks grayscale and smaller-view outputs, reads the long description against the table, and verifies that the decision note stops at partnership review.

## 7. Authoritative readings and public clinical sources

### Required data and method reading

1. CDC PLACES County Data 2024 release: https://data.cdc.gov/d/fu4u-a9bh
2. CDC PLACES methodology: https://www.cdc.gov/places/methodology/index.html
3. CDC PLACES health outcomes: https://www.cdc.gov/places/measure-definitions/health-outcomes.html
4. CDC PLACES health risk behaviors: https://www.cdc.gov/places/measure-definitions/health-risk-behaviors.html
5. CDC PLACES health status: https://www.cdc.gov/places/measure-definitions/health-status.html

The methodology explains that PLACES uses multilevel regression and poststratification with BRFSS, ACS, and Census inputs. It also explains that point estimates and 95 percent confidence intervals come from simulated model results. The measure pages define the population, question, time frame, and limitations for smoking, diabetes, fair or poor health, physical inactivity, and obesity.

### Standing visualization sources

1. W3C Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
2. W3C Understanding Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
3. W3C Complex Images: https://www.w3.org/WAI/tutorials/images/complex/

The module's comparison rules are specified in the Commons course and module contract. Learners are not required to adopt one proprietary visualization style.

### Reading prompts

Learners answer:

- Which source systems contribute to PLACES estimates?
- What is multilevel regression and poststratification used to produce?
- What population is represented by each selected measure?
- Which measures use self-report?
- How are the 95 percent confidence limits generated?
- Why is an age-adjusted estimate useful for comparison?
- What local information is absent from a county aggregate?
- Which visual choices must remain constant for a repeated-panel comparison?

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Dataset A: five-measure national county release

- File: `data/places_county_comparison_2024.csv`
- Rows: 31,450
- Columns: 16
- Measures: 5
- Value types: crude and age adjusted
- County geographies: 3,144
- National summary rows: 10
- Measure year: 2022
- SHA-256: `2af5ce99fc7d66a18e95451084afc397e0f7392e9f1a2b5476377fd8811658d2`
- Public aggregate data: yes
- Synthetic: no

Teaching purpose:

- preserve every county for the selected measures;
- preserve crude and adjusted estimates and intervals;
- provide optional peer-state sensitivity analysis;
- keep national summary rows as authoritative references;
- allow learners to verify the North Carolina teaching release;
- demonstrate that a focused query can still preserve broad comparison context.

### Dataset B: North Carolina comparison release

- File: `data/nc_county_health_profiles_2024.csv`
- Rows: 500
- Columns: 27
- Counties: 100
- Measures per county: 5
- Measure year: 2022
- SHA-256: `33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9`
- Public aggregate data: yes
- Synthetic: no

Teaching purpose:

- provide a complete county-by-measure matrix;
- make crude, adjusted, interval, population, rank, and reference fields available together;
- support one consistent panel order;
- support fixed-scale small multiples;
- expose how a transparent screening rule creates and limits a shortlist;
- keep exact values available for accessibility and audit.

### Provenance chain

```text
CDC PLACES Socrata dataset fu4u-a9bh
  -> exact five-measure, 16-field query
  -> raw checksum 897064d1...
  -> normalized 31,450-row selected national release
  -> crude and adjusted pairs for 100 North Carolina counties
  -> matching national age-adjusted references
  -> transparent rank, gap, profile count, and order fields
  -> R comparison figures and 500-row decision table
```

### Rights and redistribution

The source metadata identifies the dataset as public domain. Commons documentation uses CC BY 4.0 and code uses MIT. The release contains no patient identifiers, patient rows, or restricted partner data.

### Data minimization

The query selects five measures and the 16 fields needed for measure identity, geography, estimate type, point estimate, interval, population, and footnote. It does not download unrelated PLACES measures or geographic levels.

### Completeness rule

The national release keeps all 3,144 county geographies and all ten selected national summary rows. The North Carolina release requires every county to have both estimate types for all five measures. A partial county profile does not silently enter the shortlist.

## 9. Data dictionary and expected analytic structure

### National source fields

| Field | Role | Expected use |
|---|---|---|
| `year` | measure year | comparability and labeling |
| `stateabbr` | state key | North Carolina or peer-state selection |
| `statedesc` | state label | accessible geography name |
| `locationname` | county or national name | reader label |
| `locationid` | geography key | five-character county FIPS or national `59` |
| `measureid` | measure key | five selected constructs |
| `measure` | source label | complete measure definition path |
| `data_value_type` | estimate label | crude or age adjusted |
| `datavaluetypeid` | estimate key | `CrdPrv` or `AgeAdjPrv` |
| `data_value` | point estimate | plotted prevalence |
| `low_confidence_limit` | interval endpoint | uncertainty display |
| `high_confidence_limit` | interval endpoint | uncertainty display |
| `totalpopulation` | population context | source audit |
| `totalpop18plus` | adult population | outreach-scale context |
| `data_value_footnote_symbol` | source note key | missingness and qualification |
| `data_value_footnote` | source note | exact source qualification |

### Teaching identity and source fields

| Field | Role |
|---|---|
| `county_fips` | stable county key |
| `county_name` | readable county label |
| `state_abbr` | fixed `NC` geography code |
| `state_name` | fixed state label |
| `measure_id` | selected source measure key |
| `measure_name` | complete source measure label |
| `measure_label` | short panel label |
| `measure_year` | common 2022 measure year |
| `adult_population` | source adult population |
| `source_footnote` | joined source note, blank in this case |

### Teaching estimate fields

| Field | Role |
|---|---|
| `crude_prevalence_pct` | crude modeled point estimate |
| `crude_low_ci_pct` | crude lower 95 percent confidence limit |
| `crude_high_ci_pct` | crude upper 95 percent confidence limit |
| `age_adjusted_prevalence_pct` | age-adjusted modeled point estimate |
| `age_adjusted_low_ci_pct` | adjusted lower 95 percent confidence limit |
| `age_adjusted_high_ci_pct` | adjusted upper 95 percent confidence limit |
| `national_age_adjusted_pct` | matching U.S. adjusted point estimate |
| `national_age_adjusted_low_ci_pct` | national lower confidence limit |
| `national_age_adjusted_high_ci_pct` | national upper confidence limit |

### Derived comparison fields

| Field | Formula or rule | Meaning |
|---|---|---|
| `difference_from_national_pct_points` | county adjusted point minus matching national adjusted point | descriptive absolute gap |
| `rank_descending_point_estimate` | 1 plus count of counties with a higher point estimate | competition rank within measure |
| `counties_compared` | fixed 100 | comparison denominator |
| `point_estimate_above_national` | gap greater than zero | descriptive direction |
| `measures_above_national` | count of five yes values | equal-weight teaching count |
| `largest_gap_measure_id` | measure with largest gap | transparent tie-break context |
| `largest_gap_pct_points` | maximum county gap | second ordering field |
| `profile_order` | count descending, gap descending, name ascending | fixed row order across panels |

### Expected analytic grain

The teaching table is long format. One row is one county-measure pair. Crude and adjusted values occupy separate columns because the assignment treats them as two related endpoints within the same county-measure observation.

The primary key is:

```text
county_fips + measure_id
```

Each county has five rows. Each measure has 100 rows. No row represents a patient, event, hospital, or direct survey respondent.

### Type rules

- FIPS remains five-character text.
- Percentages remain numeric values on a 0 to 100 scale.
- Adult population remains integer.
- Year remains the source measure year.
- Ranks remain integer and may have ties.
- `point_estimate_above_national` remains a descriptive yes or no field.
- Blank source footnotes remain blank.

## 10. Worked example and instructor walkthrough

### Step 1: verify the matrix

The validator confirms:

- 100 unique counties;
- 5 unique measures;
- 500 unique county-measure keys;
- all measures use year 2022;
- every county has all five measures;
- every source estimate and confidence limit is present;
- every interval contains its point estimate;
- adult population is stable across the five rows for each county.

The instructor asks why a complete matrix matters. Expected answer: missing county-measure pairs could change the shortlist and make panels appear more comparable than they are.

### Step 2: identify national references

The matching U.S. age-adjusted point estimates are:

- current smoking: 13.2 percent;
- diagnosed diabetes: 10.4 percent;
- fair or poor health: 17.0 percent;
- no leisure activity: 23.0 percent;
- obesity: 33.4 percent.

The reference definition is constant. Each panel compares a county age-adjusted point estimate with the same measure's U.S. age-adjusted point estimate. The numeric line position differs because the measures differ.

### Step 3: inspect measure ranges

North Carolina age-adjusted ranges are:

- smoking: 9.7 to 25.0 percent;
- diabetes: 8.0 to 15.6 percent;
- fair or poor health: 12.1 to 27.2 percent;
- no leisure activity: 15.8 to 33.1 percent;
- obesity: 25.6 to 43.5 percent.

The reference lab uses a shared 0 to 46 percent scale. This makes absolute prevalence level and spread comparable. It leaves more empty space in the diabetes panel, which is truthful rather than wasteful.

### Step 4: define one county order

For each county:

1. count the selected point estimates above the matching national point;
2. identify the largest percentage-point gap;
3. sort count descending;
4. sort largest gap descending;
5. sort county name ascending for remaining ties.

The order is calculated once and reused across all five panels. It supports row tracking and highlights the twelve reference review candidates.

### Step 5: draw all-county small multiples

Each panel contains:

- 100 county points;
- 100 county confidence intervals;
- one national reference line;
- the same x scale;
- the same county order;
- a triangle and dark accent for the reference shortlist;
- exact values in the linked table.

Only twelve county names print to prevent label collision. Every county remains a plotted point and exact table row.

### Step 6: calculate point differences

For every county-measure row:

```text
difference = county age-adjusted point estimate - matching national age-adjusted point estimate
```

The shortlist profile uses zero as a shared definition across panels. It also subtracts the national point from the county confidence-limit endpoints for descriptive position. This is not a formal confidence interval for a difference because covariance and the full comparison method are not calculated.

### Step 7: compare crude and adjusted estimates

A dumbbell connects the crude and age-adjusted estimate for the same county and measure. Shape and color distinguish endpoints. All panels use the same 0 to 46 percent scale.

The direction of the segment shows how age standardization changes the estimate under a common age distribution. It does not show improvement, deterioration, time, or treatment effect.

### Step 8: inspect the screening denominator

Counties above the national point estimate:

- smoking: 89;
- diabetes: 62;
- fair or poor health: 73;
- no leisure activity: 68;
- obesity: 70.

Across profiles:

- 9 counties are above zero selected national points;
- 9 are above one;
- 10 are above two;
- 9 are above three;
- 9 are above four;
- 54 are above all five.

The national comparator therefore identifies a broad North Carolina pattern more than a narrow county set.

### Step 9: produce the reference twelve

The first twelve under the transparent order are:

1. Robeson;
2. Bertie;
3. Hertford;
4. Anson;
5. Hyde;
6. Nash;
7. Warren;
8. Columbus;
9. Scotland;
10. Halifax;
11. Swain;
12. Sampson.

All twelve are above all five matching national point estimates. Their order is then determined by the largest point gap and county name.

### Step 10: write the action

The reference action invites the twelve counties to a readiness review and explicitly requests:

- county and community validation;
- within-county subgroup evidence;
- current local data;
- implementation partners and capacity;
- intervention fit;
- adult population and resource context;
- community priorities;
- a fair process for counties not selected in the first round.

The action does not allocate funds.

## 11. Guided practice

### Exercise A: scale test

Learners compare the fixed-scale reference with the free-scale critique and answer:

- Which panel looks most variable under each design?
- How many percentage points does the panel width represent?
- Does the reader need absolute prevalence or within-measure position?
- Would a standardized score answer a different question?

### Exercise B: order test

Learners create two versions:

1. one shared profile order;
2. independent descending order within each measure.

They identify which version better supports:

- finding the highest counties within one measure;
- tracing one county across measures;
- seeing whether the same counties recur;
- reading exact rank.

Neither order is universally correct. The task determines the choice.

### Exercise C: comparator test

Learners compare three candidate references:

- matching national age-adjusted point;
- North Carolina median within measure;
- a sourced program goal.

For each, they state the question, advantages, limitations, and whether one status label can be reused across panels.

### Exercise D: dumbbell interpretation

Learners write one sentence about a crude-to-adjusted segment without using:

- increased;
- decreased;
- improved;
- worsened;
- before;
- after.

An acceptable form is: "The age-adjusted estimate is 2.1 percentage points lower than the crude estimate under the source standardization method."

### Exercise E: shortlist stress test

Learners change one rule at a time:

- use four of five measures;
- prioritize largest single gap;
- include adult population as a separate readiness column;
- replace national with state median;
- require a county interval entirely above the national point.

They record which counties enter or leave and whether the decision meaning changes. The goal is to expose rule sensitivity, not to find a preferred answer by trial and error.

### Exercise F: accessibility audit

Learners remove color and inspect whether shortlist status, crude versus adjusted endpoints, county order, reference lines, and exact values remain available.

## 12. Independent exercise

### Scenario

The director has three flawed products:

1. five panels with free x scales;
2. five state panels where red means above a different local median;
3. a rainbow profile chart connecting thirty counties across five measures.

The director needs one all-county comparison, one twelve-county profile, one crude-versus-adjusted comparison, and a decision note that makes the screening rule reviewable.

### Required analysis

The learner must:

1. load the released North Carolina table;
2. assert 500 rows, 100 counties, and five measures;
3. verify one 2022 measure year;
4. verify complete point estimates and confidence limits;
5. identify crude and adjusted fields;
6. choose one fixed scale for the primary panels;
7. choose and state one county order;
8. choose and state one comparator definition;
9. create an all-county figure;
10. write reproducible code for exactly twelve candidates;
11. create a shortlist profile around a shared zero or other declared comparator;
12. compare crude and adjusted estimates;
13. retain adult population and the 100-county denominator;
14. export all 500 exact rows;
15. write short and long text alternatives;
16. write a review action and pre-allocation evidence list;
17. document AI use or non-use and human verification.

### Required products

- `all-groups.png` shows all counties and measures.
- `shortlist-profile.png` shows exactly twelve counties under a declared rule.
- `adjustment-comparison.png` compares crude and adjusted estimates.
- `decision-table.csv` contains all 500 exact rows and shortlist status.
- `comparison-brief.md` documents scale, order, comparator, rule, denominator, and limits.
- `alt-text.md` provides an equivalent reading path.
- `decision-note.md` recommends a proportional next action.
- `analysis.R` regenerates the figures and table.
- `ai-use.md` records tool involvement and verification.

### Independent choice

The learner may replace the reference shortlist rule. The replacement must be decided and documented before reading the resulting twelve names. It must not use a black-box model, hidden weight, or hand adjustment.

An alternative may include population as a separate criterion, but it must explain whether the goal is comparative prevalence, outreach scale, readiness, or a combination. Mixing those questions into one score requires explicit weights and a sensitivity analysis.

## 13. Visualization and communication requirements

### All-county figure

- All 100 counties appear in every required measure panel.
- One x scale supports absolute comparison.
- One county order supports row tracking.
- The order rule is stated.
- The measure year is visible.
- The national reference definition is consistent.
- Confidence intervals remain visible.
- Shortlist emphasis uses shape or direct text as well as color.
- The source, population, estimate type, and units are visible.
- The exact table and text alternative are referenced.

### Shortlist profile

- Exactly twelve counties appear.
- A shared zero or comparator definition appears in every panel.
- County order remains consistent.
- Percentage-point differences remain available.
- Confidence limits remain visible or are available in the adjacent table.
- The title names the rule or question rather than labeling counties as bad.
- The caption states that the shortlist is for review.

### Adjustment comparison

- Crude and age-adjusted endpoints are paired only within the same county and measure.
- Endpoint identity survives grayscale.
- A fixed scale is used across comparable panels.
- No time or improvement language appears.
- Adult population remains in the table.
- The caption states that adjustment changes the comparison basis.

### Scale requirements

Free scales may be used only for a separately labeled view whose task is within-panel shape or rank. They may not replace the required absolute comparison. A transformed scale must show the formula, reference, and raw-value path.

### Ordering requirements

The learner states:

- the sorting fields;
- direction of each sort;
- tie-breaking rule;
- whether the order was selected before reading names;
- why the order fits the decision.

Panel-specific order may appear only in a separately labeled view for within-measure rank.

### Comparator requirements

Every line or zero point states:

- comparator population;
- estimate type;
- measure;
- year;
- whether the value is descriptive, target, or policy threshold.

A matching national point estimate is descriptive. It is not a goal, need threshold, or significance boundary.

### Accessibility requirements

- Color is never the only cue.
- Important points and intervals have readable contrast.
- County and estimate identity survive grayscale.
- Labels remain readable in print and a smaller view.
- A short alternative states the structure and main finding.
- A long description preserves scale, order, reference, ranges, shortlist, uncertainty, and limits.
- The exact table contains all 500 rows in predictable order.

### Claim discipline

The figures may state:

- a county point estimate is higher or lower than a matching national point;
- a measure has a specified North Carolina range;
- a declared rule selects twelve counties for review;
- crude and adjusted estimates differ;
- many counties meet the national comparison condition.

They may not state:

- a county caused its modeled estimate;
- a selected county is less healthy overall;
- one county differs significantly from another based on visual overlap;
- age adjustment improved the county;
- the profile count is validated;
- the shortlist determines funding or intervention.

## 14. Exact submission package and filenames

```text
module-09/
  comparison-brief.md
  analysis.R
  all-groups.png
  shortlist-profile.png
  adjustment-comparison.png
  decision-table.csv
  alt-text.md
  decision-note.md
  ai-use.md
```

### `comparison-brief.md`

```markdown
# Comparison brief

## Decision owner and review action

## Source, query, year, and checksums

## Groups, measures, population, and estimate types

## Completeness and missingness

## Shared scale

## Shared order and tie handling

## Comparator definition

## Shortlist rule and sensitivity

## Uncertainty and denominator

## Equity and within-county limits

## Reproducibility record
```

### `decision-table.csv`

Required columns, in order:

```text
county_fips
county_name
measure_id
measure_name
measure_year
adult_population
crude_prevalence_pct
crude_low_ci_pct
crude_high_ci_pct
age_adjusted_prevalence_pct
age_adjusted_low_ci_pct
age_adjusted_high_ci_pct
national_age_adjusted_pct
difference_from_national_pct_points
rank_descending_point_estimate
counties_compared
point_estimate_above_national
measures_above_national
profile_order
shortlist
```

The table contains 500 rows, five rows per county, and exactly twelve unique `shortlist = TRUE` counties.

### `alt-text.md`

```markdown
# Text alternative

## Short alternative

## Long description

### Decision and chart structure

### All-county comparison

### Twelve-county shortlist

### Crude and age-adjusted comparison

### Uncertainty and denominator

### Decision boundary

### Exact-value table
```

### `decision-note.md`

```markdown
# Decision note

## Decision owner and question

## Comparison rule

## Finding and twelve-county review list

## Action now

## Equity and population context

## Uncertainty and limits

## Evidence needed before allocation
```

### `ai-use.md`

```markdown
# AI-use record

## Tool and model

## Work delegated

## Prompts or instructions

## Outputs retained or rejected

## Source, rank, and shortlist verification

## Accessibility verification

## Human decisions
```

If no AI tool was used, the file states that directly and records the manual verification process.

### File-quality rules

- PNG files are final exports, not screenshots of code or software menus.
- `analysis.R` runs from the released data and regenerates all figures and the CSV.
- Markdown files contain complete reasoning rather than links to private notes.
- FIPS codes keep leading zeros.
- Every source link is a complete visible URL.
- No credentials, restricted data, or hidden workbook dependencies are included.

## 15. Rubric and pass conditions

| Criterion | Weight | Full-credit evidence |
|---|---:|---|
| Source fidelity and comparison structure | 15% | All counties, measures, years, estimates, intervals, populations, and references are preserved. |
| All-county small multiples | 15% | One scale, one order, and one comparator definition support reliable scanning across five panels. |
| Shortlist rule and profile | 20% | Exactly twelve counties follow a visible, reproducible review rule with no hidden weighting or allocation claim. |
| Adjustment and denominator judgment | 10% | Crude and adjusted estimates are compared accurately, and population scale remains available. |
| Uncertainty and reference interpretation | 10% | Intervals and point differences are shown without unsupported significance or equivalence claims. |
| Critique and repair | 10% | Free scales, changing baselines, and rainbow overload are diagnosed as decision problems and repaired. |
| Accessibility and exact alternatives | 10% | Redundant cues, readable contrast, complete text alternatives, and a 500-row table provide equivalent access. |
| Reproducibility | 5% | The editable analysis regenerates three figures and the table from the released CSV. |
| Decision note and AI accountability | 5% | The action fits a review decision, and tool use or non-use is recorded with human verification. |

### Score interpretation

- 90 to 100: release-ready after named human review;
- 80 to 89: passes with targeted revisions;
- 70 to 79: substantial resubmission required;
- below 70: the comparison package is not usable.

### Noncompensable pass conditions

1. All 100 counties and all five measures remain in the analysis and exact table.
2. Comparable primary panels use one visible x scale.
3. One county order is reused across comparable primary panels.
4. Every reference line has the same declared definition across panels.
5. The shortlist contains exactly twelve unique counties and follows reproducible code.
6. No hidden score, weight, or hand adjustment determines the shortlist.
7. Crude and age-adjusted estimates are not described as before and after values.
8. Interval overlap is not described as a formal pairwise test.
9. Adult population and the 100-county comparison denominator remain available.
10. The recommendation is a review action, not automatic allocation or intervention.
11. Color is not the only county, estimate-type, or status cue.
12. Short text, long text, and the complete table are present.
13. The editable analysis regenerates the submitted products.
14. No protected or restricted data are included.
15. `ai-use.md` is complete.

Failure of any one condition requires revision regardless of the weighted score.

## 16. Common errors, failure modes, and interventions

### Error 1: every panel fills its width

Symptom: free scales make all measures look equally spread.

Intervention: restore one absolute prevalence scale and ask how many percentage points each panel width represents.

### Error 2: every panel sorts itself

Symptom: the top county appears in the same visual row even though the county changes.

Intervention: choose one row-tracking order or clearly label the view as independent within-measure ranks.

### Error 3: the comparator changes silently

Symptom: red means above a different state median in every panel.

Intervention: use one comparator definition or replace the shared status label with direct panel-specific reference labels.

### Error 4: a constant numeric line is used for different measures

Symptom: every panel uses 20 percent as though it had the same clinical meaning.

Intervention: use a measure-specific reference under one stable definition or remove the line.

### Error 5: different constructs become a slope

Symptom: smoking, diabetes, health status, inactivity, and obesity are connected as a line.

Intervention: use separate aligned points or panels. Do not imply sequence or continuity across constructs.

### Error 6: color carries thirty county identities

Symptom: the legend is unreadable or removed.

Intervention: use order, direct labels, a focused subset, small multiples, or a table.

### Error 7: means hide county variation

Symptom: one North Carolina bar replaces 100 counties.

Intervention: restore county points and intervals, then add a summary only if it supports the decision.

### Error 8: age adjustment becomes improvement

Symptom: a leftward dumbbell is called better.

Intervention: replace temporal or evaluative language with the exact crude and adjusted comparison basis.

### Error 9: interval overlap becomes a test

Symptom: crossing or non-crossing intervals are described as proof of difference or equivalence.

Intervention: state that the intervals belong to separate modeled estimates and identify the formal comparison method that would be needed.

### Error 10: rank becomes distance

Symptom: rank 1 is described as much worse than rank 2 without reading values or intervals.

Intervention: show point estimates, intervals, and percentage-point differences beside rank.

### Error 11: ties are broken incorrectly

Symptom: tied point estimates receive arbitrary consecutive statistical ranks.

Intervention: use competition rank for analysis and an explicit name tie-break only for display order.

### Error 12: the profile count becomes validated

Symptom: five yes-or-no values become a named risk or equity score.

Intervention: call it a transparent teaching count, list equal weighting and omitted factors, and stop at review.

### Error 13: population disappears

Symptom: small and large counties with the same prevalence are treated as the same outreach task.

Intervention: retain adult population in the table and decision note without replacing the prevalence comparison.

### Error 14: the shortlist is hand edited

Symptom: the figure and code disagree or a favored county is inserted after viewing results.

Intervention: require exactly twelve unique counties from one runnable rule and record any sensitivity analysis separately.

### Error 15: county language stigmatizes residents

Symptom: a county is called unhealthy, noncompliant, or failing.

Intervention: describe modeled estimates and the review decision, then name within-county variation and community evidence needed next.

### Error 16: exact values disappear

Symptom: only PNG files are submitted.

Intervention: return the package until the 500-row table and complete text alternatives exist.

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

The Module 07 contract remains binding. Every final comparison must:

- avoid color-only identity or status;
- use readable text and critical marks;
- retain a stable reading order;
- survive grayscale and print;
- remain understandable in a smaller viewing context;
- provide a short alternative and structured long description;
- provide all 500 exact rows in a predictable table;
- expose confidence limits, population, and shortlist status in the alternate path.

Dense panels require special care. It is acceptable to print only the twelve emphasized county names when every county remains plotted and the exact table provides the complete names and values.

### Equity

County aggregates can hide differences by race, ethnicity, age, disability, income, language, rurality, neighborhood, insurance, and access. A county-level screen should not define a community's needs without local participation.

The decision note includes a concise equity boundary:

> County estimates can identify a place for review, but they do not show which residents experience the burden or which response the community wants. Validate the screen with stratified local evidence and community priorities before allocation.

The learner does not invent subgroup findings when subgroup data are absent.

### Stigma and language

Use:

- "county with a higher modeled smoking prevalence estimate";
- "selected for partnership-readiness review";
- "point estimate above the matching national estimate";
- "additional local evidence is needed."

Avoid:

- "unhealthy county";
- "bad community";
- "noncompliant residents";
- "failed county";
- "high-risk people" when only a place aggregate is available.

### Privacy

The supplied releases contain public county aggregates. They contain no patient identifiers or protected health information. Learners may not enrich the assignment with patient, employee, or restricted partner records.

### Responsible claims

The strongest supportable claims are comparative and procedural:

- observed modeled point estimates differ;
- the same scale and order reveal repeated county patterns;
- many counties exceed a national point reference;
- a declared rule produces a review list;
- the rule needs local validation before resource decisions.

Unsupported claims include:

- causal explanations;
- individual or subgroup health status;
- program effectiveness;
- readiness;
- formal pairwise significance;
- justified funding allocation.

## 18. AI and agent policy

### Permitted uses

Learners may use AI tools to:

- explain plotting or reshaping errors;
- propose several comparison layouts;
- identify candidate completeness checks;
- draft plain-language titles and text-alternative structure;
- compare a learner-written shortlist rule with the rubric;
- generate a first pass of routine plot code;
- identify where scales, order, or comparator meaning changes.

### Required human work

The learner remains responsible for:

- reading CDC methodology and measure definitions;
- verifying 31,450 and 500 row checksums;
- confirming all 100 counties and five measures;
- checking crude and adjusted source values;
- recalculating references, gaps, ranks, profile counts, and shortlist;
- choosing the scale, order, comparator, and action;
- inspecting figures in color, grayscale, print, and a smaller view;
- verifying the text alternatives against the table;
- approving every county name and claim.

### Prohibited uses

AI may not:

- invent a measure definition, source value, comparator, or county result;
- create a hidden score or weighting system;
- add or remove a county after viewing the result without disclosure;
- convert interval overlap into a formal test;
- describe modeled aggregates as observed diagnoses;
- assign blame, readiness, or intervention from the screen;
- certify accessibility, epidemiology, equity, or clinical correctness;
- receive protected or restricted records.

### Minimum AI-use record

`ai-use.md` states:

- tool and model;
- work delegated;
- prompts or instructions;
- output retained, changed, or rejected;
- source and calculation checks;
- shortlist verification;
- accessibility checks;
- final human decisions.

The file is required when no AI was used as well.

## 19. Answer key and instructor notes

### Source and structure answers

- Source: CDC PLACES County Data 2024 release.
- Dataset ID: `fu4u-a9bh`.
- Selected measure year: 2022.
- Selected national rows: 31,450.
- County geographies: 3,144.
- National summary rows: 10.
- North Carolina rows: 500.
- North Carolina counties: 100.
- Measures per county: 5.
- Estimate types: crude and age adjusted.
- Source footnotes in the teaching case: none.

### National reference answers

- current smoking: 13.2 percent;
- diagnosed diabetes: 10.4 percent;
- fair or poor health: 17.0 percent;
- no leisure activity: 23.0 percent;
- obesity: 33.4 percent.

### North Carolina range answers

- current smoking: 9.7 to 25.0 percent;
- diagnosed diabetes: 8.0 to 15.6 percent;
- fair or poor health: 12.1 to 27.2 percent;
- no leisure activity: 15.8 to 33.1 percent;
- obesity: 25.6 to 43.5 percent.

### Counts above national point

- current smoking: 89 counties;
- diagnosed diabetes: 62 counties;
- fair or poor health: 73 counties;
- no leisure activity: 68 counties;
- obesity: 70 counties.

### Profile distribution

- zero measures above: 9 counties;
- one measure above: 9 counties;
- two measures above: 10 counties;
- three measures above: 9 counties;
- four measures above: 9 counties;
- five measures above: 54 counties.

### Population answer

Adult population ranges from 2,644 to 908,531. It supports outreach-scale context. It is not used in the reference prevalence order.

### Reference shortlist answer

1. Robeson;
2. Bertie;
3. Hertford;
4. Anson;
5. Hyde;
6. Nash;
7. Warren;
8. Columbus;
9. Scotland;
10. Halifax;
11. Swain;
12. Sampson.

### Critique answer

#### C1

Free scales make different percentage-point ranges occupy similar widths. The repair uses a fixed 0 to 46 percent scale for the primary absolute comparison. A standardized alternative must be separately labeled.

#### C2

Each state median changes the numeric and population basis of the red label. The repair uses one national comparator or directly labels local medians without pretending the status is shared.

#### C3

Thirty county lines rely on hue and connect five different constructs. The repair uses ordered small multiples, a focused shortlist profile, and an exact table.

### Acceptable final recommendation

> Invite Robeson, Bertie, Hertford, Anson, Hyde, Nash, Warren, Columbus, Scotland, Halifax, Swain, and Sampson Counties to a partnership-readiness review under the declared five-measure teaching order. This does not establish that they are the least healthy counties or that funding should follow automatically. Fifty-four counties exceed all five national point estimates, and the screen omits population reach, within-county inequity, local priorities, intervention fit, cost, and implementation capacity.

### Claims that fail

- "These are the twelve worst counties."
- "The counties share one causal risk profile."
- "Age adjustment shows improvement."
- "Non-overlapping visual intervals prove pairwise significance."
- "Five measures above national validate a funding score."
- "The county result applies equally to every resident."

### Instructor facilitation notes

1. Start with the action and why only twelve invitations are available.
2. Ask learners to state the comparison denominator before drawing.
3. Show the free-scale critique beside the fixed-scale repair.
4. Make learners trace one county across five panels.
5. Require the comparator definition in words before drawing a line.
6. Use the 54-of-100 result to challenge national-only priority rules.
7. Treat the reference shortlist as an auditable example, not an answer to defend.
8. End by naming the people and evidence missing from the county aggregate.

## 20. Runnable acceptance checks

### Data build

From the module directory:

```powershell
python build_places_comparison.py
```

Expected behavior:

- downloads the exact pinned five-measure query;
- stops if the raw checksum changes;
- requires the exact 16-field schema;
- requires 31,450 selected rows;
- requires five measure IDs and two estimate types;
- requires one common 2022 measure year;
- requires complete point estimates and intervals;
- requires 500 complete North Carolina county-measure pairs;
- writes deterministic national and teaching releases.

Offline rebuild:

```powershell
python build_places_comparison.py --raw-input places-comparison-pinned-query.csv
```

### Data validation

```powershell
python validate_places_comparison.py
```

Expected result:

```text
Module 09 CDC PLACES comparison data passed 58 checks.
Selected rows: 31,450; SHA-256: 2af5ce99fc7d66a18e95451084afc397e0f7392e9f1a2b5476377fd8811658d2
North Carolina rows: 500; SHA-256: 33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9
```

### Reference lab

```powershell
Rscript lab.R
```

Expected outputs:

```text
output/
  01-all-counties-ordered-small-multiples.png
  02-shortlist-difference-from-national.png
  03-crude-age-adjusted-dumbbells.png
  04-profile-count-denominator.png
  comparison_decision_table.csv
  alt-text-reference.md
```

### Critique set

```powershell
Rscript critique_charts.R
```

Expected outputs:

```text
critique-output/
  C1-free-panel-scales.png
  C2-changing-panel-baselines.png
  C3-overloaded-rainbow-profiles.png
```

### Visual acceptance

The instructor or reviewer confirms:

- all outputs open successfully;
- all 100 counties appear in every primary measure panel;
- one 0 to 46 percent scale is used across the five primary panels;
- one county order is reused;
- national reference lines use one definition;
- confidence intervals remain visible;
- shortlist status uses triangle and color;
- crude and adjusted endpoints use shape and color;
- the profile count labels all six possible counts;
- captions remain readable at normal zoom;
- the exact table contains 500 rows;
- the text alternative matches the table and figures.

### Repository checks

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
node --check curriculum-data.js
node --check site.js
git diff --check
```

All checks must pass before the module release is committed.

## 21. Release status, reviewers, version, and known issues

### Release status

- Module version: 0.1.0
- Commons release: 0.20.0
- Status: runnable release candidate
- Technical validation date: 2026-08-29
- Data validator: 58 of 58 checks pass
- Lab execution: four PNGs, one CSV, and one Markdown text alternative pass
- Critique execution: three deliberately flawed PNGs pass
- Tested environment: Windows, Python 3, R 4.6.1, ggplot2 4.0.3

### Required human reviewers

| Review role | Reviewer | Status | Required evidence |
|---|---|---|---|
| Population-health decision relevance | unassigned | pending | review action and shortlist use fit practice |
| Epidemiology and CDC PLACES fidelity | unassigned | pending | method, measures, intervals, adjustment, and claims are accurate |
| Equity and community language | unassigned | pending | county framing avoids stigma and names local validation |
| Visualization teaching quality | unassigned | pending | scale, order, comparator, and critique sequence teach the intended judgment |
| Accessibility and assistive technology | unassigned | pending | figures, text, and table provide equivalent access |
| Independent teachability | unassigned | pending | a new instructor can run and teach the package on a clean system |

### Known issues

1. Named human reviews remain pending.
2. PLACES values are model-based small-area estimates rather than direct county survey estimates or observed diagnoses.
3. The five selected measures include self-reported behavior, diagnosis, height, weight, and general health.
4. County aggregates do not reveal within-county variation, community priorities, readiness, cost, or intervention fit.
5. The reference profile count gives every measure equal weight and is not a validated score.
6. Point direction and interval overlap do not establish formal pairwise results.
7. The all-county figure prints only twelve county names; the exact table preserves all names and values.
8. Static accessibility checks do not cover every browser, assistive technology, printer, or viewing condition.
9. Technical execution has been tested on Windows. macOS and Linux clean-run verification remains pending.

### Release decision

Technical release is permitted when all automated checks pass and repository integration is current. Instructional release still requires named human review. Any revision that changes the source query, checksums, selected measures, row count, profile-order rule, required outputs, or interpretation boundary requires a new module version and updated release metadata.

### Handoff to Module 10

Module 10 inherits:

- the 100-county and five-measure source releases;
- crude, adjusted, interval, population, and reference fields;
- exact FIPS identifiers;
- the distinction between comparison and outreach scale;
- the accessible encoding and exact-table contract;
- the rule that a screening list is not an allocation decision;
- the requirement to name what county aggregation conceals.

Module 10 must compare a map with a non-map alternative. It may reuse one selected measure or a clearly defined review subset, but it must not imply that geographic color adds evidence by itself.
