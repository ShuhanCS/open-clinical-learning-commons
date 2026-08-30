# DA-730 Module 06 specification: Uncertainty, variation, and small numbers

- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module: 06 of 13
- Scheduled block: instructional week 3
- Learner time: 8.5 hours
- Target Commons release: 0.17.0
- Module package version: 0.1.0
- Status: implementation specification
- Primary public case: CMS heart failure 30-day readmission estimates for Massachusetts hospitals
- Decision owner: health-system clinical quality committee
- Checkpoint role: closes the week-3 visualization judgment dossier

## 1. Module identity and place in the course

Module 06 teaches learners to show how much uncertainty surrounds a clinical quality estimate before they compare or rank organizations. It follows Module 05, which established that counts, crude rates, adjusted rates, and denominators answer different questions. Module 06 keeps the denominator visible and adds the source interval, reporting status, benchmark classification, and limits of pairwise interpretation.

The module uses the July 2026 CMS Unplanned Hospital Visits release. The selected measure is `READM_30_HF`, Heart failure (HF) 30-Day Readmission Rate. The source provides a risk-standardized point estimate, lower and higher estimates, denominator, reporting dates, comparison with the national rate, and footnote code for every hospital row. A matching CMS national file provides the published national rate and counts of hospitals in comparison categories. The official CMS footnote crosswalk supplies the meaning of every source code.

This is the second half of the week-3 checkpoint. Learners finish with a visualization judgment dossier that combines the chart-choice, distribution, rate, denominator, and uncertainty work from Modules 01 through 06.

The public reference implementation uses R and ggplot2 because those tools already support the course. Learners may use another approved tool if they submit editable source, reproducible output, the same source record, and the same reasoning evidence.

## 2. Healthcare decision and audience

### Decision

A Massachusetts clinical quality committee must decide which hospitals need a focused review of heart failure readmissions. The committee receives a league table sorted by the CMS point estimate. It must determine whether the ordering represents meaningful evidence or merely a precise-looking ranking of uncertain estimates.

The committee is not deciding that a hospital delivered poor care, caused a readmission, or should be penalized. It is deciding where to ask for more information, where the public estimate supports a benchmark concern, and where the available evidence does not justify a comparative claim.

### Decision owner

The primary decision owner is a clinical quality committee that includes a physician quality lead, nursing quality lead, analyst, and service-line representative. The committee can request local validation and review, but it cannot infer patient-level mechanisms from a public hospital estimate.

### Decision questions

1. Which Massachusetts hospitals have a reported heart failure readmission estimate?
2. Which hospitals does CMS classify as better, no different, or worse than the national rate?
3. How much separation does a point-only rank chart imply?
4. What changes when the CMS lower and higher estimates are shown?
5. Which rows are suppressed or unavailable, and what does the source footnote say?
6. Which hospitals warrant follow-up, and what additional local evidence should the committee request?

### Required decision language

The final note must use one of four actions:

- focused review supported by the CMS comparison category;
- monitor and validate locally;
- do not distinguish from the national benchmark using this release;
- no public estimate available, inspect the footnote before acting.

The learner may not replace these actions with a generic ranking or a claim that one hospital is statistically different from another.

## 3. Foundation skill revisited or extended

Module 06 revisits Foundations I and II through a different decision than Module 05.

### Foundations I skills revisited

- identify the observational unit as one hospital-measure reporting row;
- distinguish a point estimate from an observed patient count;
- retain the denominator, period, measure definition, and missing-value code;
- sort and summarize without losing suppressed rows;
- check that every reported point lies between its lower and higher source estimates.

### Foundations II skills revisited

- interpret an interval as a range of estimates compatible with the source method;
- distinguish comparison with a benchmark from pairwise comparison between hospitals;
- connect sample size and precision without treating denominator as the only source of uncertainty;
- explain why a rank is always available when point estimates differ, even when evidence of separation is weak;
- identify multiplicity as a reason to avoid searching a long rank list for isolated extremes.

### New application

The new work is visual uncertainty judgment. Learners compare four displays of the same public release: a point-only league table, a caterpillar plot with source intervals and benchmark status, a denominator versus interval-width view, and a reporting-status view. They then choose the display that supports committee triage without claiming more than CMS reports.

No formula for the CMS risk-standardization model is derived in this module. Learners treat the released score, interval endpoints, and benchmark category as published model outputs. A later methods course may teach hierarchical risk-standardization models in full.

## 4. Assessable learning outcomes

By the end of the module, the learner can:

1. Preserve a public clinical point estimate, lower estimate, higher estimate, denominator, reporting period, comparison category, and footnote as one analytic record.
2. Build a point-only rank view and explain why its ordering can overstate separation.
3. Build an interval display with a clearly labeled national reference value and source-defined comparison status.
4. State that overlap between two displayed intervals is descriptive and is not, by itself, a pairwise hypothesis test.
5. Identify every suppressed or unavailable row without converting source text to zero.
6. Explain why denominator and interval width are related but not interchangeable in a risk-standardized model.
7. Distinguish common-cause or sampling variation from evidence that warrants targeted follow-up, while staying inside the published comparison category.
8. Write a short decision note that names the finding, action, uncertainty, and evidence needed next.
9. Assemble the exact week-3 visualization judgment dossier from Modules 01 through 06.

### Mastery threshold

Passing work earns at least 80 of 100 points and satisfies every non-negotiable pass condition in Section 15. A high total cannot compensate for changing a suppressed value to zero, hiding the interval, or making an unsupported hospital quality claim.

## 5. Concept ownership and boundaries

### Concepts owned here

- point estimate versus interval;
- source interval endpoints;
- benchmark comparison versus pairwise comparison;
- uncertainty-aware ordering;
- caterpillar and forest-style interval displays;
- league-table failure modes;
- denominator and interval-width relationship;
- suppression and unavailable-result handling;
- descriptive interval overlap;
- multiplicity as a visual interpretation risk;
- funnel plots and control limits as method-dependent tools;
- checkpoint synthesis across chart selection, distributions, rates, and uncertainty.

### Concepts carried in from earlier modules

- audience and decision framing from Module 01;
- perceptual accuracy from Module 02;
- chart or table selection from Module 03;
- distributions and tails from Module 04;
- denominators, adjustment, and model-based estimates from Module 05.

### Concepts introduced but completed later

- accessible color and redundant encoding, completed in Module 07;
- time variation and control-chart construction, completed in Module 08;
- small multiples and repeated group comparison, completed in Module 09;
- geography, spatial aggregation, and map uncertainty, completed in Module 10;
- dashboard monitoring, completed in Module 12;
- narrative sequencing for an executive audience, completed in Module 13.

### Explicit exclusions

This module does not:

- reconstruct the CMS risk-standardization model;
- calculate a binomial confidence interval from the published denominator;
- infer a standard error by assuming the source interval is a simple Wald interval;
- build a funnel plot with invented control limits;
- treat interval overlap as a formal test between two hospitals;
- infer the quality of individual clinicians or care episodes;
- replace CMS footnote rules with an instructor-created sample-size cutoff;
- use a rank as a penalty, referral, or purchasing decision.

## 6. Lesson sequence and learner time

The module totals 8.5 learner hours.

| Segment | Hours | Learner work | Evidence produced |
|---|---:|---|---|
| Decision opening | 0.50 | Compare a point-only league table with the CMS benchmark categories. | Initial decision and confidence rating |
| Core lesson | 1.25 | Read point, interval, denominator, status, period, and benchmark fields. | Annotated source row |
| Source and footnote lab | 0.75 | Trace one reported, one too-small, and one unavailable record to CMS. | Source audit notes |
| Instructor walkthrough | 1.00 | Reproduce Massachusetts counts, ranges, statuses, and rank contrast. | Checked walkthrough table |
| Tiered visualization lab | 2.00 | Run, modify, or author four uncertainty views. | Figures and decision table |
| Critique and repair | 0.75 | Repair a league table and a small-number display. | Critique notes |
| Independent submission | 1.25 | Create the final uncertainty figure and committee note. | Module package draft |
| Week-3 checkpoint assembly | 0.75 | Assemble Modules 01 through 06 into the dossier contract. | Checkpoint folder |
| Exit check | 0.25 | State the remaining accessibility question handed to Module 07. | Exit response |

### Scaffold levels

- Run: execute the supplied R files without changing the source extract.
- Modify: change the audit set or ordering and explain the effect on interpretation.
- Author: reproduce the required fields and views in an approved tool using the pinned source files.

All three levels answer the same decision questions and submit the same final package.

## 7. Authoritative readings and public clinical sources

### Required public sources

1. CMS Unplanned Hospital Visits - Hospital landing page: https://data.cms.gov/provider-data/dataset/632h-zaca
2. CMS hospital CSV release used by the build: https://data.cms.gov/provider-data/sites/default/files/resources/30edc1d0417a34b58affcc2495a02b0a_1785189969/Unplanned_Hospital_Visits-Hospital.csv
3. CMS Unplanned Hospital Visits - National landing page: https://data.cms.gov/provider-data/dataset/cvcs-xecj
4. CMS national CSV release used by the build: https://data.cms.gov/provider-data/sites/default/files/resources/d30b0557f1d06bee1d5646d2eaede709_1785189969/Unplanned_Hospital_Visits-National.csv
5. CMS Footnote Crosswalk landing page: https://data.cms.gov/provider-data/dataset/y9us-9xdf
6. CMS footnote CSV release used by the build: https://data.cms.gov/provider-data/sites/default/files/resources/f29bb7c812e242f6edfef0a4b7d0eaca_1760630713/Footnote_Crosswalk.csv
7. CMS Hospital data dictionary: https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf
8. CMS Hospitals topic page: https://data.cms.gov/provider-data/topics/hospitals

### Required reading questions

Before analysis, the learner answers:

- What is the measure ID and exact measure name?
- Is the score a raw observed proportion or a CMS risk-standardized estimate?
- What dates define the hospital and national reporting periods?
- Which columns carry the source interval?
- What does footnote 1 mean?
- What does footnote 5 mean?
- Does the source compare hospitals with one another or with the national rate?

### Reading rule

The module calls `Lower Estimate` to `Higher Estimate` the CMS source interval. It does not assign a confidence level unless a cited CMS methodology document does so for this release. The broader lesson explains confidence intervals, prediction intervals, margins of error, and control limits as different objects that cannot be substituted for one another.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Raw source A: hospital release

- Publisher: Centers for Medicare & Medicaid Services
- Dataset ID: `632h-zaca`
- Title: Unplanned Hospital Visits - Hospital
- Release date in catalog metadata: 2026-08-13
- Raw row count: 67,060
- Raw column count: 20
- Raw bytes: 19,048,784
- Raw SHA-256: `a3e64029ea6daea1f7de163e5b5054b918d0c8be986fccfc47c7a8d5b29a6d1d`
- Selected measure: `READM_30_HF`
- Selected national hospital rows: 4,790
- Selected reporting period: 2023-07-01 through 2025-06-30

The repository preserves every hospital row for the selected measure, including reported, too-small, unavailable, territorial, and Veterans Health Administration rows. It does not commit the other 13 measures from the 19 MB source because the module does not teach them. The build script downloads and validates the complete raw release before filtering.

### Raw source B: national release

- Dataset ID: `cvcs-xecj`
- Title: Unplanned Hospital Visits - National
- Release date in catalog metadata: 2026-08-13
- Raw row count: 14
- Raw bytes: 2,814
- Raw SHA-256: `44e39aedc296f00fa8477a3485a66012cbfcdefb173435199a0b03343c9402c3`
- Selected measure national rate: 21.3
- Selected reporting period: 2023-07-01 through 2025-06-30

All 14 national measure rows remain in the committed national extract so later modules can reuse the release.

### Raw source C: footnote crosswalk

- Dataset ID: `y9us-9xdf`
- Title: Footnote Crosswalk
- Release date in catalog metadata: 2026-08-13
- Raw row count: 32
- Raw bytes: 3,456
- Raw SHA-256: `5214e1468fb04c5cdeac8920f2c446cccaa65e2f6f929424cd228042a52d963e`

All 32 footnote definitions remain in the committed crosswalk. The selected hospital extract joins the text but also keeps the original code.

### Teaching release

The build creates:

- `cms_hf_readmission_hospitals_2026.csv`: all 4,790 hospital rows for `READM_30_HF`;
- `cms_unplanned_national_2026.csv`: all 14 national rows;
- `cms_footnote_crosswalk_2026.csv`: all 32 footnote definitions;
- `ma_hf_readmission_uncertainty_2026.csv`: all 65 Massachusetts rows with transparent derived fields.

### Rights and redistribution

CMS identifies the catalog as public data. The release record keeps the publisher, landing pages, exact downloads, retrieval date, hashes, and data dictionary. Course documentation and code retain the repository's CC BY 4.0 and MIT licenses. The source data remain attributed to CMS.

### Teaching purpose

The data are public aggregate hospital estimates. They are used to teach visualization judgment. They are not used to grade hospitals, compare clinicians, identify patients, or make a current purchasing decision.

## 9. Data dictionary and expected analytic structure

### National hospital extract

| Field | Type | Meaning | Rule |
|---|---|---|---|
| `facility_id` | text | CMS facility identifier | Preserve leading zeroes and letter suffixes. |
| `facility_name` | text | Published facility name | Preserve source spelling. |
| `city` | text | Published city or town | Context only. |
| `state` | text | Two-letter state or territory code | Massachusetts filter is `MA`. |
| `county` | text | Published county or parish | Do not infer service area. |
| `measure_id` | text | CMS measure identifier | Must equal `READM_30_HF`. |
| `measure_name` | text | Published measure label | Preserve exact label. |
| `compared_to_national` | text | CMS comparison category | Keep source text. |
| `denominator` | integer or blank | Source denominator | Blank when source says Not Available. |
| `score` | decimal or blank | Risk-standardized readmission rate | Blank when unavailable. |
| `lower_estimate` | decimal or blank | Lower endpoint from CMS | Do not recompute. |
| `higher_estimate` | decimal or blank | Higher endpoint from CMS | Do not recompute. |
| `number_of_patients` | integer or blank | Source patient count field | Keep separate from denominator. |
| `number_of_patients_returned` | integer or blank | Source returned-patient count | Keep source missingness. |
| `footnote_code` | text or blank | CMS footnote code | Never treat as numeric quantity. |
| `footnote_text` | text or blank | Joined official footnote meaning | Join from the crosswalk. |
| `start_date` | ISO date | Reporting start | `2023-07-01` for selected measure. |
| `end_date` | ISO date | Reporting end | `2025-06-30` for selected measure. |
| `estimate_status` | text | `reported`, `too_few`, or `not_available` | Derived only from source score, comparison, and footnote. |
| `source_release` | text | Release pin | `2026-08-13`. |

### Massachusetts teaching table derived fields

| Field | Type | Meaning | Derivation |
|---|---|---|---|
| `reported_rank_worst_first` | integer or blank | Point-estimate rank among reported MA hospitals | Descending score, then facility name. |
| `interval_width` | decimal or blank | Width of source interval | Higher estimate minus lower estimate. |
| `contains_national_rate` | integer or blank | Whether 21.3 lies inside the source interval | 1 when lower is at most 21.3 and higher is at least 21.3. |
| `source_comparison_group` | text | Short display label | Better, no different, worse, too few, or not available. |
| `denominator_display_group` | text | Descriptive display bin | Under 100, 100 to 499, 500 or more, or unavailable. |
| `top_ten_point_rank` | integer | Whether the point estimate is in the ten highest reported values | 1 for ranks 1 through 10. |

The denominator display group is not a CMS reliability or suppression rule. It exists only to make small reported denominators visible.

### Missing-value contract

- Source text `Not Available` becomes a blank numeric field, not zero.
- The original comparison text and footnote code remain available.
- A row with footnote 1 becomes `too_few`.
- Other unavailable rows become `not_available` unless the source gives a more specific published category.
- Suppressed rows remain in row counts, tables, and status views.

## 10. Worked example and instructor walkthrough

### Reproducible source facts

For `READM_30_HF`, the July 2026 hospital release contains:

- 4,790 hospital rows nationally;
- 3,253 reported estimates;
- 3,194 rows classified no different from the national rate;
- 38 rows classified worse than the national rate;
- 21 rows classified better than the national rate;
- 1,020 rows labeled Number of Cases Too Small;
- 517 additional rows labeled Not Available.

The matching national row publishes a rate of 21.3 and reports 38 hospitals worse, 3,253 the same, 21 better, and 1,121 with too few cases. Learners preserve the national file as published and do not force its category counts to equal a reconstruction from hospital display labels.

### Massachusetts facts

The Massachusetts extract contains 65 rows:

- 53 reported estimates;
- 10 not available rows;
- 2 rows labeled Number of Cases Too Small;
- 52 reported hospitals classified no different from the national rate;
- 1 reported hospital classified worse than the national rate;
- 0 reported hospitals classified better than the national rate.

Among reported rows:

- denominators range from 30 to 2,088, with a median of 538;
- four reported hospitals have denominators under 100;
- point estimates range from 19.7 to 25.2, a spread of 5.5 percentage points;
- source interval widths range from 6.9 to 9.2 points, with a median of 7.6;
- all 1,378 pairs of displayed Massachusetts intervals overlap, a descriptive fact that is not a pairwise test.

### Rank contrast

The ten highest point estimates include Saint Anne's Hospital at 25.2, Heywood Hospital at 24.8, and VA Boston Healthcare System - Jamaica Plain at 24.7. A league table creates ten ordered positions. CMS classifies only Saint Anne's Hospital as worse than the national rate; the other nine top-ten hospitals are no different from the national rate.

The highest point estimate has a source interval of 21.4 to 29.6. The lowest point estimate, Massachusetts General Hospital at 19.7, has an interval of 16.4 to 23.3. The intervals overlap even though the point ranks are first and fifty-third. This does not prove equivalence. It shows why the league table alone cannot support a claim of separation.

### Instructor interpretation

The defensible committee action is a focused review for the one hospital CMS classifies worse than the national rate, paired with local validation of case mix, coding, care transitions, and more recent data. The committee may monitor other high point estimates, but it should not call them worse based on rank. Suppressed hospitals require footnote review and local evidence, not imputed zeroes or placement at the bottom of the list.

## 11. Guided practice

### Part A: Read one source row

Learners annotate:

- unit of observation;
- measure and adjustment status;
- point estimate;
- lower and higher estimates;
- denominator;
- reporting period;
- benchmark category;
- footnote meaning;
- claim the row can support;
- claim the row cannot support.

### Part B: Audit missingness

Learners compare:

- a reported row with a denominator under 100;
- a row with footnote 1;
- a row with footnote 5;
- a row with footnote 19.

They explain why a guessed numeric cutoff cannot reproduce the source's reporting policy.

### Part C: Build the rank view

Learners sort the 53 reported Massachusetts hospitals from highest to lowest score and label ranks 1 through 53. They record what the chart makes easy to see and what it hides.

### Part D: Add intervals and benchmark status

Learners plot every reported point with its CMS lower and higher estimates. The display includes:

- a visible reference at the national rate of 21.3;
- CMS comparison status encoded by both color and shape;
- hospital names or a readable keyed table;
- the reporting period;
- a note that intervals are source endpoints;
- a note that pairwise difference is not tested.

### Part E: Inspect denominator and interval width

Learners plot denominator against interval width and answer:

- Which small-denominator rows are still reported?
- Does denominator alone determine interval width?
- Why would a simple binomial interval be the wrong replacement for the CMS model output?
- Which source information would be needed before constructing formal funnel limits?

### Part F: Audit reporting status

Learners show all 65 Massachusetts rows in a status summary. The total must reconcile to the source and include reported, too-few, and unavailable rows.

## 12. Independent exercise

### Prompt

Prepare an uncertainty-aware recommendation for the Massachusetts clinical quality committee. Use the pinned CMS release and answer whether the ten highest point estimates represent ten defensible targets for focused review.

### Required analysis

The learner must:

1. Validate 65 Massachusetts rows and 53 reported estimates.
2. Reproduce the CMS comparison category counts.
3. Identify the ten highest reported point estimates.
4. Show every selected point with its source interval.
5. Keep the 21.3 national rate and 2023-07-01 through 2025-06-30 period visible.
6. Account for all 12 suppressed or unavailable rows.
7. Compare the rank-based shortlist with the CMS benchmark classification.
8. State what local evidence the committee should request next.

### Required answer

The decision note must answer:

- Which hospital or hospitals warrant focused review from this release?
- Which high-ranked hospitals should be monitored without being labeled worse?
- Why is a point-only top ten misleading?
- What does the denominator add?
- What does the interval add?
- What does the source not establish?

### Prohibited shortcuts

- dropping unavailable rows without counting them;
- converting Not Available to zero;
- making a homemade confidence interval from the denominator;
- labeling the top ten as statistically worse;
- treating interval overlap as a formal pairwise test;
- ranking suppressed hospitals;
- changing the published benchmark category.

## 13. Visualization and communication requirements

### Final figure requirements

`figure.png` must:

- show the selected hospital point estimates and CMS source intervals;
- show the national rate of 21.3 with a direct label;
- encode source comparison status with at least two channels;
- make suppressed rows visible in the figure, companion panel, or directly adjacent table;
- state the reporting period;
- state the measure ID;
- state that lower and higher estimates come from CMS;
- avoid implying pairwise significance;
- remain legible at 100 percent browser zoom and in grayscale.

### Rank chart requirement

The point-only rank chart is a draft for critique, not an acceptable final answer. If it appears in the final brief, it must be labeled as a comparison that overstates separation and must sit beside an uncertainty-aware replacement.

### Tables

Every table must preserve:

- facility ID;
- score;
- lower and higher estimates;
- denominator;
- comparison category;
- footnote code and text when present;
- reporting dates.

### Alt text

`alt-text.md` must name:

- the measure and geography;
- how many hospital estimates are displayed;
- the national reference value;
- the one source-classified worse result;
- the number of no-different and unavailable results;
- the practical takeaway that ranks exceed the evidence of separation.

Alt text should not list every hospital. The decision table provides exact values.

### Claim boundary

Use "CMS classifies this hospital as worse than the national rate for this measure and period." Do not write "this hospital provides worse care" or "this hospital caused more readmissions."

## 14. Exact submission package and filenames

### Module submission

```text
module-06/
  uncertainty-brief.md
  analysis.R
  figure.png
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

An approved tool may replace `analysis.R` with one editable source file. The six other files remain required.

### `uncertainty-brief.md`

Required headings:

```text
# Uncertainty brief
## Decision and audience
## Measure and population
## Point-rank finding
## Interval finding
## Reporting-status audit
## Recommendation
## Evidence needed next
## Limits
```

### `source-record.yml`

Required keys:

```yaml
publisher:
dataset_id:
dataset_title:
landing_page:
download_url:
retrieved_at:
release_date:
measure_id:
measure_name:
reporting_period:
geography_filter:
raw_bytes:
raw_sha256:
selected_rows:
reported_rows:
suppressed_or_unavailable_rows:
national_rate:
build_script:
teaching_extract_sha256:
data_dictionary:
footnote_crosswalk:
rights:
known_limits:
```

### `decision-note.md`

Maximum 350 words. Required headings:

```text
# Decision note
## Finding
## Action
## Uncertainty
## Evidence needed next
```

### Week-3 checkpoint submission

Module 06 closes this exact course checkpoint:

```text
checkpoint-1/
  README.md
  selection-matrix.md
  figures/
    comparison.png
    distribution.png
    rate.png
    uncertainty.png
  analysis/
  source-records/
  critique-and-repair.md
  accessibility-check.md
  decision-brief.md
  ai-use.md
```

The four figures must use at least two approved public or synthetic sources. `selection-matrix.md` maps each decision question to the chosen display and rejected alternatives. `decision-brief.md` names the audience, finding, decision, uncertainty, and material limit. Missing editable analysis or provenance makes the checkpoint incomplete.

## 15. Rubric and pass conditions

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Source and measure integrity | 15 | Correct CMS release, measure, period, geography, hashes, and source record. |
| Missingness and footnote handling | 15 | All 65 rows reconcile; no unavailable value becomes zero; source codes and text remain. |
| Interval display | 20 | Point, source endpoints, national rate, status, and labels are accurate and readable. |
| Rank critique | 15 | Explains why 53 ranks do not equal 53 distinguishable performance levels. |
| Statistical interpretation | 15 | Separates benchmark comparison, descriptive overlap, and pairwise testing. |
| Decision consequence | 10 | Recommends focused review, monitoring, or no public conclusion with evidence needed next. |
| Accessibility and communication | 5 | Redundant encoding, readable type, direct labels, and useful alt text. |
| Reproducibility and AI record | 5 | Clean run, editable source, complete provenance, and verified AI-use record. |
| Total | 100 | 80 required to pass. |

### Non-negotiable pass conditions

The submission fails until corrected if it:

- treats a suppressed or unavailable value as zero;
- omits the source interval from the final figure;
- calls the point-only top ten statistically worse;
- treats interval overlap as a formal pairwise test;
- omits the national comparison context;
- changes the source reporting period or measure;
- lacks editable analysis or provenance;
- makes an individual patient, clinician, or causal quality claim.

## 16. Common errors, failure modes, and interventions

| Error | Why it matters | Instructor response |
|---|---|---|
| Ranking only the point estimate | Ordering appears more certain than the source evidence. | Require the same points with source intervals and status. |
| Calling every interval a 95% confidence interval | The release columns are labeled lower and higher estimates. | Use source interval unless a CMS method citation supports a stronger label. |
| Reading overlap as no difference | Visual overlap is not a formal pairwise test. | Ask which hypothesis and variance would be needed. |
| Reading non-overlap as causation | Separation does not identify why rates differ. | Return to risk adjustment, period, and local validation. |
| Creating a binomial interval | The CMS score is risk standardized, not a raw proportion. | Keep the published endpoints. |
| Inferring a suppression cutoff | CMS publishes codes and rules that are not reconstructed by one denominator. | Preserve the source status and footnote. |
| Dropping unavailable hospitals | The display hides a material part of the public evidence. | Add a reporting-status panel and reconcile to 65. |
| Treating the national rate as a target | A benchmark is not automatically a clinical goal. | Name the committee decision and local standard separately. |
| Claiming pairwise hospital differences | CMS category is comparison with the national rate. | Rewrite the claim around the published comparator. |
| Building unsupported funnel limits | Control limits require a defined sampling model. | Use denominator versus interval width as a descriptive view only. |

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Use shape plus color for benchmark status.
- Use a colorblind-safe palette with adequate contrast.
- Label the national reference directly.
- Keep hospital names or IDs available in a table.
- Provide alt text and an exact-value decision table.
- Do not rely on pale interval lines that disappear in print.
- Test grayscale output before submission.

### Equity

Risk adjustment and public reporting do not remove structural differences in access, illness burden, referral patterns, or resources. Learners must not describe a hospital or community as failing based on a single public estimate. A focused review should ask whether the model, data completeness, and available supports fit the patients served.

The module does not hide small hospitals. It distinguishes reported estimates from source-suppressed results and asks what additional evidence is needed. This avoids treating missing public data as either perfect performance or proof of failure.

### Privacy

The files contain hospital-level aggregate data and no patient identifiers. Learners may not attempt record linkage, patient identification, or reconstruction of suppressed cells.

### Responsible claim template

"For the 2023-07-01 through 2025-06-30 CMS reporting period, [hospital] has a published risk-standardized heart failure readmission estimate of [score], with source lower and higher estimates of [lower] and [higher]. CMS classifies it as [category] relative to the national rate. This supports [review or monitoring action], not a causal claim about care quality."

## 18. AI and agent policy

AI tools may assist with code, chart alternatives, prose editing, and reproducibility checks. They may not replace source verification or statistical judgment.

### Required `ai-use.md`

For each material use, record:

- tool and model when known;
- date;
- prompt or task summary;
- files or passages affected;
- source values independently checked;
- code executed;
- outputs inspected;
- corrections made;
- unresolved concern.

### Prohibited AI uses

- inventing an interval level or methodology citation;
- filling a suppressed CMS value;
- guessing a footnote meaning;
- calling two hospitals significantly different from visual overlap alone;
- writing a causal explanation not supported by the source;
- submitting unexecuted generated code;
- creating fictional local validation evidence.

### Verification rule

The learner remains responsible for every number and claim. AI-generated code must be executed from a clean copy of the submitted package. AI-generated prose must be checked against the pinned CSVs, source record, and final figure.

## 19. Answer key and instructor notes

### Required numeric answers

- National selected hospital rows: 4,790.
- National reported scores: 3,253.
- Massachusetts rows: 65.
- Massachusetts reported scores: 53.
- Massachusetts not available: 10.
- Massachusetts number of cases too small: 2.
- Massachusetts CMS comparison counts among reported: 52 no different, 1 worse, 0 better.
- National published rate: 21.3.
- Massachusetts reported denominator range: 30 to 2,088.
- Massachusetts reported denominator median: 538.
- Massachusetts point-estimate range: 19.7 to 25.2.
- Massachusetts point-estimate spread: 5.5 points.
- Massachusetts interval-width range: 6.9 to 9.2 points.
- Highest point estimate: Saint Anne's Hospital, 25.2, source interval 21.4 to 29.6, CMS status worse.
- Second point estimate: Heywood Hospital, 24.8, source interval 20.6 to 29.8, CMS status no different.
- Lowest point estimate: Massachusetts General Hospital, 19.7, source interval 16.4 to 23.3, CMS status no different.
- Top-ten point ranks classified worse: 1 of 10.
- Descriptively overlapping interval pairs among the 53 reported rows: 1,378 of 1,378.

### Interpretation key

The league table makes a continuous set of uncertain estimates look like an ordered performance ladder. The interval display shows substantial uncertainty, and the CMS benchmark category sharply narrows the defensible action. The correct response is not to erase ranks or intervals. It is to use each for the question it can answer.

Only Saint Anne's Hospital is source-classified worse than the national rate in the Massachusetts extract. This supports focused review, not a verdict about care. The other high point estimates may be monitored and checked locally, but their rank alone does not justify the same label.

All displayed intervals overlap descriptively. The answer key must state that this is not a pairwise significance test and does not prove hospital equivalence.

### Checkpoint key

A complete week-3 dossier contains four decision-ready figures, not six module folders copied without synthesis. The selection matrix should explain why each final view was kept. The rate figure must retain its denominator. The uncertainty figure must retain the interval and reporting status. At least two sources must appear, and every figure must trace to editable analysis and a source record.

### Acceptable alternative conclusions

A learner may recommend monitoring rather than immediate focused review if the note explicitly acknowledges the CMS worse-than-national classification and explains the committee's decision threshold. A learner may include more Massachusetts hospitals in an exploratory review if the final language separates source evidence from local follow-up criteria.

## 20. Runnable acceptance checks

### Build checks

The build must fail if:

- any raw source byte count or SHA-256 differs from the pinned release;
- the hospital source does not contain 67,060 rows;
- the selected measure does not contain 4,790 rows;
- the national file does not contain 14 rows;
- the footnote crosswalk does not contain 32 rows;
- a source footnote code used by the selected measure lacks crosswalk text;
- the Massachusetts filter does not contain 65 rows.

### Data checks

The validator must check:

- unique facility ID within the selected measure;
- exact measure ID and reporting period;
- reported score count nationally and in Massachusetts;
- interval containment for every reported score;
- blank numeric fields for unavailable rows;
- exact Massachusetts status and comparison counts;
- denominator, score, and interval-width ranges;
- deterministic ranking with name tie-break;
- top-ten comparison contrast;
- national benchmark and category counts;
- footnote joins;
- output file hashes.

### R checks

`lab.R` must create:

- `01-point-rank.png`;
- `02-interval-caterpillar.png`;
- `03-denominator-and-width.png`;
- `04-reporting-status.png`;
- `ma_hf_uncertainty_decision_table.csv`.

`critique_charts.R` must create:

- `C1-point-only-league-table.png`;
- `C2-hidden-small-n.png`.

Both scripts must stop with a useful error when required columns, expected rows, or ggplot2 are missing.

### Visual checks

The reviewer inspects each PNG for:

- readable labels;
- unclipped notes;
- correct reference line;
- visible intervals;
- redundant status encoding;
- meaningful source and period text;
- no accidental claim that rank equals difference;
- no black boxes, missing glyphs, or overlapping panels.

### Repository checks

The repository validator must confirm:

- exactly 21 numbered specification sections;
- every required module file exists;
- release metadata matches module version 0.1.0 and Commons 0.17.0;
- root and course version markers agree;
- the build ledger points next to Module 07 and checkpoint verification;
- JavaScript syntax remains valid;
- `git diff --check` passes.

## 21. Release status, reviewers, version, and known issues

### Version decision

Module 06 adds a new complete module and closes the first course checkpoint. The Commons version moves from 0.16.0 to 0.17.0. The module package begins at 0.1.0.

### Technical release gate

The module may be marked `runnable-release-candidate` when:

- source downloads reproduce pinned byte counts and hashes;
- all four committed data files reproduce their hashes;
- the validator passes every check;
- four lab figures, one decision table, and two critique figures render;
- the 21-section repository contract passes;
- Module 06 and checkpoint links are integrated into course documentation.

### Required human reviews

| Review | Reviewer | Release question |
|---|---|---|
| Visualization and source fidelity | Named visualization faculty member | Are values, intervals, labels, and comparison categories faithful to CMS? |
| Clinical quality interpretation | Clinician or quality leader | Does the recommendation support review without implying causation or punishment? |
| Statistical interpretation | Named quantitative reviewer | Are benchmark, overlap, multiplicity, and model boundaries described correctly? |
| Accessibility | Named accessibility reviewer | Are status, labels, contrast, alt text, and exact values usable without color? |
| Independent teachability | Instructor other than the author | Can the module and checkpoint run from the committed package? |

### Known issues

- CMS labels the interval columns Lower Estimate and Higher Estimate; this module does not invent a confidence level.
- The risk-standardized model cannot be reconstructed from the public extract alone.
- Source categories compare each hospital with the national rate and do not test every hospital pair.
- Descriptive interval overlap does not establish statistical equivalence.
- The national summary's too-few count is preserved as published and may not equal a simple count of one hospital display category.
- Public data lag current operations and do not replace local, more recent validation.
- Facility names and participation can change after the pinned release.
- The reference implementation is tested on Windows; clean macOS and Linux runs remain a human release check.

### Handoff to Module 07

Module 07 takes the final interval display and asks whether every committee member can read it without relying on color. It owns color choice, contrast, redundant encoding, grayscale behavior, and accessible communication. Module 06 hands off the exact status categories, interval lines, benchmark, decision table, and alt-text draft.

### Handoff to checkpoint review

Before Module 07 begins, the instructor verifies the week-3 dossier contract from Modules 01 through 06. This is an assembly and judgment check, not a new analysis. Learners revise any figure that loses its decision, denominator, interval, source, accessibility note, or editable analysis during synthesis.
