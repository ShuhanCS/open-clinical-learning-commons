# FND-1 Module 05: Descriptive results

## 1. Module identity and place in the course

- Course: FND-1, Healthcare Data Foundations.
- Module: 05 of 07.
- Instructional week: 5.
- Learner work: 16.0 hours.
- Module version: 0.1.0.
- Commons release: 0.33.0.
- Status target: runnable release candidate.
- Decision owner: clinical analytics reviewer.
- Checkpoint role: creates the 25-point descriptive component assembled at the Week 6 checkpoint.
- Core input: exact Module 04 resolved analytic table and retained N01 through N08 quality conditions.
- Downstream receiver: Module 06 accessible charts and time-indexed data.

Module 05 teaches learners to describe a checked healthcare table without losing its grain, denominator, time window, missing-value meaning, or synthetic-source boundary. It is not a hypothesis-testing or modeling module. The work remains technical and prepares exact evidence for visual inspection and handoff.

## 2. Technical decision and named audience

### Decision

Do the descriptive results preserve the accepted cohort, exact denominators, missing-value meaning, status, uncertainty, and source limits well enough to become the numeric source for Module 06?

### Decision owner

A clinical analytics reviewer owns the decision. This role checks whether each result still means what its label claims, whether the denominator matches the question, and whether the language stays descriptive.

### Receiving audience

- the Module 06 visualization analyst;
- the Week 6 checkpoint review panel;
- a clinical analytics team that must reproduce the tables;
- faculty scoring denominator and interpretation competence; and
- a future analyst who did not build the cohort.

### Allowed dispositions

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer` for unresolved source, quality, privacy, rights, or governance review.

Only `accept` and `accept with conditions` permit Module 06 to use the released tables.

## 3. Foundation skill and handoff

### Foundation skill

The learner turns an accepted person-level analytic table into exact descriptive evidence with an explicit denominator contract. The learner must be able to reproduce a number, trace it to rows and fields, explain its unit, and state what cannot be concluded.

### Upstream handoff

Module 04 provides:

- `resolved-analytic-table.csv`, 374 rows and 29 fields;
- SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`;
- one row per synthetic patient;
- cohort-definition version 0.1.0;
- quality-rule results with SHA-256 `c301cd46d6058329d72cc2b71649f5bb1ccf9fbff43f6c97e8b2fc008f791c06`;
- final readiness decision `proceed with conditions`; and
- N01 through N08 retained conditions.

Module 05 may not recalculate eligibility, change time zero, repair the source, drop supported extremes, or redefine a follow-up state.

### Downstream handoff

Module 06 receives:

- the unchanged resolved analytic table;
- 17 one-variable profile rows;
- 12 cross-tab cells from two complete tables;
- six rates with exact numerators, denominators, and Wilson intervals;
- two index-class stratum rows;
- 27 denominator-registry rows;
- machine-readable validation checks;
- an interpretation memo;
- source and transformation records; and
- the final reviewer disposition.

Module 06 must draw from these exact tables rather than retyping numbers from prose.

## 4. Assessable outcomes

By the end of Module 05, the learner can:

1. verify the accepted source fingerprint and person grain;
2. distinguish a variable type from the storage text used in a CSV;
3. select counts, proportions, means, standard deviations, medians, quartiles, minima, and maxima appropriately;
4. define the quartile method used by the release;
5. distinguish a cohort denominator from an available-case denominator;
6. explain why structurally missing next-event timing uses 111 recorded events rather than 374 people;
7. construct a complete cross-tab without omitting zero or small cells;
8. calculate row percentages and reconcile them to 100 percent within rounding tolerance;
9. construct a rate from a named numerator and denominator;
10. report a descriptive Wilson interval without turning it into a test of a causal or group difference;
11. build a stratified table without implying adjustment or fair comparison;
12. trace every result family through the denominator registry;
13. preserve N01 through N08 as result-level conditions;
14. separate a numeric finding from its interpretation limit;
15. reproduce all outputs from the accepted table;
16. document material AI assistance and independent verification; and
17. make an allowed release disposition for Module 06.

## 5. Concept ownership and out-of-scope boundaries

### Module 05 owns

- one-variable descriptive summaries;
- complete category counts;
- available-case counts;
- missing counts;
- means and sample standard deviations;
- medians and inclusive quartiles;
- minima and maxima;
- complete two-variable cross-tabs;
- row percentages;
- selected proportions called rates only when their event, population, and time window are explicit;
- Wilson 95-percent intervals as descriptive uncertainty;
- simple unadjusted stratification;
- denominator registration;
- interpretation limits; and
- descriptive release readiness.

### Module 05 does not own

- hypothesis tests or p-values;
- effect estimates or confidence intervals for group differences;
- causal inference;
- risk adjustment or standardization;
- regression;
- prediction or machine learning;
- survival analysis;
- statistical imputation;
- fairness claims from unadjusted strata;
- population inference from synthetic data;
- the full data-visualization curriculum; or
- intervention recommendations.

### Rounding rule

Counts remain integers. Means, sample standard deviations, medians, quartiles, and rates are stored to six decimal places. Display prose may use one decimal place only when the exact CSV remains linked. Calculations use unrounded values; displayed rounded values are never reused as inputs.

### Quartile rule

Q1 and Q3 use linear interpolation with inclusive endpoints, equivalent to Python `statistics.quantiles(values, n=4, method="inclusive")`. The method is part of the release contract because software defaults can differ.

## 6. Lesson sequence and learner time

| Learning activity | Hours | Evidence |
|---|---:|---|
| Source and quality-condition verification | 1.00 | source verification note |
| Variable types and one-variable summaries | 2.25 | variable profile |
| Center, spread, skew, and supported extremes | 1.75 | numeric interpretation notes |
| Missingness and available-case denominators | 1.50 | denominator records |
| Cross-tabs and row percentages | 2.25 | two complete cross-tabs |
| Rates and descriptive uncertainty | 2.00 | six rate records |
| Stratified descriptive table | 1.50 | two stratum rows |
| Guided notebook and exact checks | 1.50 | executed notebook |
| Interpretation memo and handoff decision | 1.25 | memo and disposition |
| Reproduction, accessibility, and AI audit | 1.00 | final records |
| Total | 16.00 | complete release |

### Teaching rhythm

Every new number begins with five questions: What is the unit? Who or what is counted? What is the numerator? What is the denominator? What time window and missing-value rule apply? Software syntax follows the decision.

### Feedback checkpoints

1. After source verification, faculty checks that 374 means people rather than encounters.
2. After the variable profile, faculty checks skew-sensitive summaries and N04 through N06.
3. After cross-tabs, faculty checks all cells and row-percent reconciliation.
4. After rates, faculty checks time windows and numerator-parent logic.
5. Before submission, a peer traces one prose claim through the registry to source rows.

## 7. Readings and authoritative sources

### Required module records

1. Module 03 cohort and table specifications.
2. Module 04 data specification, rule results, risk log, resolution log, and final decision.
3. This Module 05 specification.
4. The released denominator registry.

### Public references

- Python statistics documentation: https://docs.python.org/3/library/statistics.html
- Python CSV documentation: https://docs.python.org/3/library/csv.html
- STROBE reporting guidance: https://www.equator-network.org/reporting-guidelines/strobe/
- W3C accessible table concepts: https://www.w3.org/WAI/tutorials/tables/
- Synthea downloads: https://synthea.mitre.org/downloads
- Synthea CSV data dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary

### Reading questions

- When is a median more informative than a mean?
- Why can the mean still be useful when a distribution is skewed?
- Why does a 111-row available-case summary answer a different question from a 374-person rate?
- What does a Wilson interval add, and what does it not establish?
- Why is an unadjusted stratum table not a fair-comparison model?
- How does a denominator registry prevent copy-and-paste ambiguity?

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Accepted analytic input

| Property | Contract |
|---|---|
| path in Module 04 | `outputs/resolved-analytic-table.csv` |
| rows | 374 |
| fields | 29 |
| grain | one row per synthetic patient |
| bytes | 121,787 |
| SHA-256 | `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a` |
| source release | `synthea-csv-apr2020` |
| cohort definition | 0.1.0 |
| real patients | none |

### Quality-condition input

| Property | Contract |
|---|---|
| path in Module 04 | `outputs/quality-rule-results.csv` |
| rows | 28 |
| retained rules | N01 through N08 |
| bytes | 3,607 |
| SHA-256 | `c301cd46d6058329d72cc2b71649f5bb1ccf9fbff43f6c97e8b2fc008f791c06` |

### Rights and safety

The source is public synthetic teaching data. The module contains no real patient data, credentials, private workplace records, or restricted source. Learners may not substitute real clinical records.

### Teaching purpose

The data is used to learn descriptive evidence contracts. It does not estimate a real hospital, health system, community, or patient population.

## 9. Exact descriptive output contract

### Variable profile

`variable-profile.csv` contains 17 rows in this order:

| ID | Field | Descriptive role | Retained condition |
|---|---|---|---|
| VP01 | death_date | date availability | N01 |
| VP02 | age_at_index | continuous | N04 |
| VP03 | gender | categorical | none |
| VP04 | race | categorical | N07 |
| VP05 | ethnicity | categorical | none |
| VP06 | index_class | categorical | none |
| VP07 | index_reason_code | text availability | N02 |
| VP08 | index_reason_description | text availability | N02 |
| VP09 | prior_365d_encounter_count | count | N05 |
| VP10 | prior_365d_acute_count | count | none |
| VP11 | prior_365d_condition_count | count | none |
| VP12 | prior_365d_medication_count | count | N06 |
| VP13 | next_30d_state | categorical | N03 and N08 |
| VP14 | next_30d_days_after_index_stop | continuous available-case | N03 |
| VP15 | acute_return_90d | binary categorical | none |
| VP16 | death_90d | binary categorical | N08 |
| VP17 | endpoint_90d | categorical | N08 |

Each row records total rows, available count, missing count, missing percent, distinct available values, numeric or date limits where applicable, category counts where applicable, and a result-level interpretation limit.

### Cross-tabs

`cross-tabs.csv` contains 12 complete cells:

- CT01: gender by 90-day endpoint, six cells, row percentages within F and M;
- CT02: index class by 90-day endpoint, six cells, row percentages within emergency and inpatient.

Zero cells remain present if a future compatible release produces them. Categories are ordered deterministically. Counts, row denominators, row percentages, and total cohort denominator are explicit.

### Rates

`rates.csv` contains six rows, each with numerator, denominator, percent, and Wilson 95-percent lower and upper limits:

| ID | Measure | Numerator | Denominator |
|---|---|---:|---:|
| RT01 | any recorded next encounter within 30 days | 111 | 374 |
| RT02 | scheduled care within 30 days | 92 | 374 |
| RT03 | urgent care within 30 days | 4 | 374 |
| RT04 | acute return within 30 days | 15 | 374 |
| RT05 | any acute return within 90 days | 36 | 374 |
| RT06 | synthetic death within 90 days | 8 | 374 |

RT01 means a next encounter was recorded in this source. It does not mean all other people received no care.

### Stratified table

`stratified-table.csv` contains two rows, emergency and inpatient index classes. Each row contains the stratum size and cohort percent, age mean/sample standard deviation/median/Q1/Q3, prior-encounter median/Q1/Q3, 90-day acute-return count and percent, and 90-day death count and percent.

The table is unadjusted description. Differences are not evidence of a class effect, case-mix fairness, or causal relationship.

### Denominator registry

`denominator-registry.csv` contains 27 rows:

- VP01 through VP17;
- CT01 and CT02;
- RT01 through RT06; and
- ST01 and ST02.

Required fields are result ID, output file, measure name, numerator definition, denominator definition, denominator count, exclusions, missing handling, time window, unit, interpretation limit, and retained quality conditions.

## 10. Worked example and instructor walkthrough

### Example: next-event timing

The cohort has 374 people. Exactly 111 have a recorded next encounter within 30 days, and 263 have the explicit state `No encounter recorded`. The elapsed-time field is structurally blank for those 263 people.

Two valid results answer different questions:

1. RT01 uses 111 divided by 374 to describe the proportion of cohort members with a recorded next encounter.
2. VP14 uses 111 available elapsed values to describe timing among recorded next encounters.

Using 374 as the denominator for the VP14 median would treat structural non-events as times. Filling blanks with zero would falsely place events at the follow-up origin.

### Example: skew and supported extremes

Prior-year encounter counts range from 0 to 187. The mean is approximately 5.72 and the median is 3. N05 verifies that two accepted people exceed 100 encounters. The module reports mean and median, retains the maximum, and carries the review condition. It does not delete those rows or declare them mistakes.

### Example: row percentages

For the F row in CT01, the endpoint counts must sum to 236 and the row percentages must sum to 100 within rounding tolerance. The cohort denominator remains 374 in the record, but the row-percent denominator is 236.

### Example: descriptive interval

RT06 reports 8 synthetic deaths among 374 people and a Wilson interval around that proportion. The interval describes arithmetic uncertainty for this synthetic cohort construction. It is not a population estimate, performance benchmark, or comparison with a real hospital.

## 11. Guided practice

### Practice 1: Grain before description

Verify 374 rows, 374 patient IDs, 374 index encounter IDs, and source version fields.

### Practice 2: Type and summary choice

Classify the 17 registered fields. Explain why a binary 0/1 field is summarized as a category and why a count can receive both mean and median.

### Practice 3: Missingness meaning

Compare death-date, reason-field, and next-event missingness. Name the correct available denominator for each.

### Practice 4: Center and spread

Calculate mean, sample standard deviation, median, Q1, and Q3 for age and prior encounters. Explain skew without calling an accepted extreme an error.

### Practice 5: Complete categories

Reconcile all category counts to available values. Preserve native and other race rows internally with N07 attached.

### Practice 6: Cross-tab denominator

For one CT01 row, calculate each row percentage by hand and reconcile the count sum.

### Practice 7: Rate wording

Rewrite `29.7 percent had care` as the supported `111 of 374 had a next encounter recorded in this source within 30 days`.

### Practice 8: Interval interpretation

Calculate RT05 with the supplied formula and write one supported and one unsupported interpretation.

### Practice 9: Stratification boundary

Compare emergency and inpatient descriptive rows, then list the case-mix and design information needed before a fair comparison.

### Practice 10: Registry trace

Select one memo sentence and trace it to result ID, output row, source field, denominator rule, time window, and retained condition.

## 12. Independent exercise

The learner independently:

1. verifies the two upstream fingerprints;
2. runs the descriptive builder in a new target;
3. completes or reruns the notebook;
4. verifies all 17 variable rows;
5. reconciles both cross-tabs;
6. verifies all six rates and intervals;
7. reviews both strata without a group-effect claim;
8. completes the 27-row denominator registry;
9. writes an interpretation memo using exact result IDs;
10. records transformations and reproduction;
11. discloses and verifies material AI use; and
12. records an allowed reviewer disposition.

The learner may use a different approved programming language only if the exact schemas, ordering, rounding, result IDs, hashes, and validation checks are reproduced.

## 13. Visualization and communication requirements

### Required communication

The interpretation memo contains:

- source and cohort statement;
- two one-variable findings, including one skew-sensitive example;
- one missingness or availability finding;
- one cross-tab finding with the row denominator;
- one rate finding with numerator, denominator, time window, and interval;
- one stratified finding explicitly labeled unadjusted;
- all applicable N01 through N08 conditions;
- synthetic-data claim boundary;
- Module 06 handoff; and
- final disposition.

Every numeric sentence cites a result ID.

### Optional visualization

No chart is required. Module 06 owns the accessible chart set. If a learner creates an exploratory chart, the exact table remains primary and the chart is not part of the scored release.

### Public display boundary

The internal teaching release preserves exact small cells. Any public-facing display requires audience-specific disclosure review. A teaching threshold is not a universal suppression policy.

## 14. Exact submission package

```text
module-05-submission/
  VERSION
  README.md
  source-record.yml
  data-spec.md
  build_descriptive.py
  data/
    resolved-analytic-table.csv
    quality-rule-results.csv
  notebooks/
    05-descriptive-results.ipynb
  outputs/
    variable-profile.csv
    cross-tabs.csv
    rates.csv
    stratified-table.csv
    denominator-registry.csv
    descriptive-checks.csv
  interpretation-memo.md
  transformation-record.md
  reproducibility-check.md
  ai-use.md
```

Required tag: `fnd1-descriptive-v0.1.0`.

The submission does not duplicate the Module 02 database, source archive, Module 03 SQL outputs other than the accepted analytic table, or Module 04 defect layer.

## 15. Rubric and pass conditions

| Criterion | Points |
|---|---:|
| Source, grain, and quality-condition verification | 10 |
| One-variable summaries and summary-method choice | 20 |
| Missingness and denominator control | 15 |
| Complete cross-tabs and row percentages | 15 |
| Rates, time windows, and descriptive intervals | 15 |
| Stratified table and unadjusted interpretation | 10 |
| Memo, reproduction, accessibility, and AI accountability | 15 |
| Total | 100 |

### Pass threshold

At least 80 points.

### Noncompensable gates

- exact Module 04 source fingerprint;
- exact Module 04 quality-results fingerprint;
- one row per synthetic patient preserved;
- all 17 variable rows present;
- missing and available counts reconcile;
- inclusive quartile method recorded;
- both complete cross-tabs present;
- cross-tab count and row-percent reconciliation;
- all six rate numerators and denominators correct;
- interval method recorded and reproduced;
- both index-class strata present;
- unadjusted status stated;
- 27 denominator records present;
- N01 through N08 retained where applicable;
- no hypothesis, causal, risk-adjusted, or real-population claim;
- exact machine-readable outputs;
- reproducible notebook or approved accessible script path;
- material AI use disclosed and verified; and
- allowed release disposition.

Module 05 contributes 25 course percentage points to the cumulative Week 6 checkpoint. Module 06 is a required accessibility and inspection gateway and adds no separate source assessment weight.

## 16. Common failures and instructor interventions

| Failure | Intervention | Required evidence |
|---|---|---|
| Reports encounter rows as people | Return to source grain. | 374 rows and patient IDs. |
| Uses only the mean for skewed counts | Compare mean, median, quartiles, and maximum. | VP09 or VP12. |
| Deletes high utilization | Trace N05/N06 to accepted source. | Retained rows and condition. |
| Fills next-event blanks with zero | Restore structural missingness. | VP14 denominator 111. |
| Hides a small cell | Restore complete internal category record. | N07/N08 attached. |
| Uses cohort denominator for row percent | Recalculate within each row. | CT row denominator. |
| Says no encounter means no care | Rewrite to source-recorded meaning. | RT01 limit. |
| Calls an interval a real-population estimate | Reassert synthetic scope. | Rate interpretation limit. |
| Calls class strata adjusted | Remove comparison claim. | Unadjusted memo language. |
| Copies prose values by hand | Trace through result IDs. | Registry and exact CSV. |
| Adds p-values | Remove inferential substitution. | Descriptive-only output. |
| Uses AI count without checking | Recompute from source. | Independent validation result. |

## 17. Accessibility, equity, privacy, and claim checks

### Accessibility

- every table has explicit headers;
- IDs connect prose to machine-readable rows;
- counts and status do not depend on color;
- wide tables have a field dictionary and logical reading order;
- notebook Markdown states the purpose of every code section;
- `build_descriptive.py` provides a non-notebook path;
- commands are copyable;
- percentages retain their count form; and
- output filenames describe their content.

### Equity

Rare source categories remain in the exact internal record. They are not called errors or silently combined. No unadjusted category difference is labeled an inequity or a fair comparison. A later applied-course equity analysis requires an explicit question, measure, design, and governance contract.

### Privacy

All patient records are synthetic. Learners may not replace them with workplace data. Identity-like fields excluded upstream remain excluded from descriptive output.

### Claims

- Counts and summaries describe this synthetic teaching cohort only.
- Missing does not mean negative or clinically absent.
- Recorded next encounter does not measure all care.
- Extreme does not mean erroneous.
- A Wilson interval is not a real-population estimate here.
- Unadjusted strata do not establish a group or setting effect.
- No clinical quality, safety, access, utilization, equity, or intervention claim is supported.

## 18. AI policy, disclosure, and verification

### Permitted uses

- explain a summary statistic;
- compare denominator choices;
- diagnose a cross-tab error;
- suggest test cases;
- check code readability;
- draft an interpretation sentence; and
- edit documentation.

### Prohibited uses

- invent counts or intervals;
- select a denominator to make a rate look favorable;
- hide small or inconvenient cells;
- alter a source or expected value to pass validation;
- add an inferential or causal claim without a later approved design;
- infer real patient or hospital performance;
- share protected data or credentials; or
- fabricate notebook output or reproduction evidence.

### Required record

For each material use, record date, tool and model, purpose, data shared, advice used, human verification, accepted/changed/rejected decision, and affected result or artifact.

At least one AI-suggested count, method, denominator, interval, interpretation, or code path is checked against source rows, independent code, or authoritative documentation.

## 19. Answer key and instructor materials

### Source facts

- rows and people: 374;
- fields: 29;
- emergency indexes: 314;
- inpatient indexes: 60;
- gender F: 236;
- gender M: 138;
- recorded next encounter within 30 days: 111;
- scheduled care: 92;
- urgent care: 4;
- 30-day acute return: 15;
- 90-day acute return: 36;
- 90-day synthetic death: 8.

### Numeric reference facts

| Field | Mean | Sample SD | Median | Q1 | Q3 | Min | Max |
|---|---:|---:|---:|---:|---:|---:|---:|
| age at index | 46.120321 | 20.125717 | 43.500000 | 30.000000 | 62.750000 | 18 | 107 |
| prior encounters | 5.716578 | 12.907586 | 3.000000 | 1.000000 | 9.000000 | 0 | 187 |
| prior acute encounters | 0.302139 | 1.351058 | 0.000000 | 0.000000 | 0.000000 | 0 | 13 |
| prior conditions | 1.251337 | 0.848235 | 1.000000 | 1.000000 | 2.000000 | 0 | 5 |
| prior medications | 2.692513 | 11.353879 | 1.000000 | 0.000000 | 2.000000 | 0 | 185 |
| next-event days among recorded events | 16.011993 | 10.792264 | 15.958333 | 6.937500 | 27.947916 | 0.9 | 29.958333 |

### Cross-tab reference facts

- F endpoint counts: 20 acute return, 6 death, 210 no acute return recorded.
- M endpoint counts: 16 acute return, 2 death, 120 no acute return recorded.
- Emergency-index endpoint counts: 24 acute return, 7 death, 283 no acute return recorded.
- Inpatient-index endpoint counts: 12 acute return, 1 death, 47 no acute return recorded.

### Reference disposition

`accept with conditions`.

Conditions:

- keep every result tied to its denominator registry row;
- retain N01 through N08;
- keep exact CSV tables primary;
- use descriptive and unadjusted wording;
- preserve the synthetic-data boundary; and
- make Module 06 reproduce values directly from released tables.

## 20. Runnable acceptance checks

The release validator must check:

1. exact source bytes and SHA-256;
2. exact quality-results bytes and SHA-256;
3. source rows and fields;
4. patient uniqueness;
5. index uniqueness;
6. source and cohort version labels;
7. all 28 upstream rules pass;
8. N01 through N08 are present;
9. protected nonempty target;
10. module version 0.1.0;
11. 17 variable-profile rows;
12. registered variable order;
13. available plus missing equals 374;
14. exact categorical totals;
15. exact numeric means;
16. exact sample standard deviations;
17. exact inclusive quartiles;
18. exact minima and maxima;
19. death-date availability;
20. paired reason-field availability;
21. next-event available denominator;
22. N04 through N06 supported extremes retained;
23. N07 and N08 conditions retained;
24. CT01 six complete cells;
25. CT02 six complete cells;
26. cross-tab count conservation;
27. row-denominator conservation;
28. row-percent reconciliation;
29. six rate rows;
30. exact rate numerators;
31. exact rate denominators;
32. exact percentages;
33. exact Wilson lower limits;
34. exact Wilson upper limits;
35. RT01 source-recorded wording;
36. two stratum rows;
37. stratum counts sum to 374;
38. stratum percentages sum to 100;
39. exact emergency summaries;
40. exact inpatient summaries;
41. unadjusted interpretation limit;
42. 27 denominator-registry rows;
43. unique result IDs;
44. every profile ID registered;
45. every cross-tab ID registered;
46. every rate ID registered;
47. both stratum IDs registered;
48. explicit numerator definitions;
49. explicit denominator definitions;
50. explicit denominator counts;
51. explicit missing handling;
52. explicit time windows;
53. explicit units;
54. explicit interpretation limits;
55. N01 through N08 appear in the registry;
56. machine-readable checks all pass;
57. exact output ordering;
58. exact output hashes;
59. notebook is valid JSON;
60. stable notebook cell IDs;
61. required notebook narrative sections;
62. clean notebook execution;
63. source record exists;
64. transformation record exists;
65. interpretation memo cites result IDs;
66. reproduction record exists;
67. AI-use record exists;
68. no unfinished placeholder in complete submission;
69. no personal absolute path;
70. no Unicode dash in contract files;
71. allowed disposition;
72. builder self-check;
73. validator self-check;
74. complete release validation;
75. complete submission validation;
76. incomplete submission rejection;
77. clean byte-for-byte reproduction; and
78. exact Module 06 handoff.

### Automated and human boundary

Automation proves structure, arithmetic, ordering, formulas, registered conditions, and fingerprints. Human review decides whether a selected statistic fits the field, wording preserves meaning, the memo answers a useful descriptive question, the accessible route is usable, AI verification is substantive, and the final disposition fits the evidence.

## 21. Release status, reviewers, version, and known issues

### Release identity

- Module ID: `oclc-fnd1-05`.
- Module version: 0.1.0.
- Commons release: 0.33.0.
- Status target: runnable release candidate.
- Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

### Semantic-version decision

Module 0.1.0 establishes the first descriptive-output, denominator-registry, interval, interpretation, and Module 06 handoff contract. Commons 0.33.0 adds the compatible FND-1 module without changing Modules 01 through 04 or Checkpoint 1.

### Required human reviewers

| Role | Reviewer | Status |
|---|---|---|
| FND-1 faculty owner | unassigned | pending |
| Clinical analytics reviewer | unassigned | pending |
| Descriptive statistics | unassigned | pending |
| Clinical informatics and denominator meaning | unassigned | pending |
| Python and notebook teachability | unassigned | pending |
| Accessibility | unassigned | pending |
| Privacy and data governance | unassigned | pending |
| Responsible AI | unassigned | pending |
| Independent reproduction and teachability | unassigned | pending |

### Known issues after technical implementation

1. Named human review is pending.
2. macOS and Linux reproduction remain pending.
3. The source is synthetic and older.
4. Wilson intervals are descriptive arithmetic here and are not real-population estimates.

The first clean build locked six output files in `release.json`. RT01 through RT06 Wilson intervals are 25.274719 to 34.496768, 20.507004 to 29.207355, 0.416679 to 2.717296, 2.445359 to 6.511164, 7.034020 to 13.038277, and 1.087782 to 4.163484 percent. Emergency and inpatient stratum counts are 314 and 60; their acute-return percentages are 7.643312 and 20.000000, and their synthetic-death percentages are 2.229299 and 1.666667. A clean notebook run executed four code cells with four outputs. The validator passes 1,101 release checks and 1,100 complete-submission checks.

### Context-safe handoff

Implementation and clean reproduction are complete. Module 06 must consume the six released CSV files directly, retain N01 through N08, and cannot silently recalculate or relabel the results.
