# Module 09 instructor notes

## Teaching purpose

This module teaches that comparison is built from repeated choices: who is included, what is measured, which estimate is shown, how panels are scaled, how groups are ordered, and what reference means. Small multiples help only when those choices stay consistent.

## Preparation

Before class:

1. run `python validate_places_comparison.py`;
2. run `Rscript lab.R`;
3. run `Rscript critique_charts.R`;
4. inspect all seven PNG files at 100 percent zoom;
5. confirm that `comparison_decision_table.csv` has 500 rows;
6. compare the shared-scale and free-scale versions side by side;
7. inspect the twelve-county crude and adjusted dumbbells;
8. read the CDC PLACES methodology and selected measure definitions;
9. remind learners that the reference order is a screening device, not a validated score.

## Reproducible answer facts

| Quantity | Answer |
|---|---:|
| Selected national rows | 31,450 |
| County geographies | 3,144 |
| National summary rows | 10 |
| Measures | 5 |
| Value types per geography-measure | 2 |
| North Carolina counties | 100 |
| North Carolina teaching rows | 500 |
| Measure year | 2022 |
| Adult population range | 2,644 to 908,531 |
| Counties above all five national points | 54 |
| Counties at or below all five national points | 9 |
| Validation checks | 58 |
| Selected national SHA-256 | `2af5ce99fc7d66a18e95451084afc397e0f7392e9f1a2b5476377fd8811658d2` |
| North Carolina SHA-256 | `33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9` |

## Measure key

| Measure | Range | National point | Counties above point |
|---|---:|---:|---:|
| Current smoking | 9.7% to 25.0% | 13.2% | 89 |
| Diagnosed diabetes | 8.0% to 15.6% | 10.4% | 62 |
| Fair or poor health | 12.1% to 27.2% | 17.0% | 73 |
| No leisure activity | 15.8% to 33.1% | 23.0% | 68 |
| Obesity | 25.6% to 43.5% | 33.4% | 70 |

## Reference shortlist

The transparent teaching order selects:

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

All twelve are above the matching national point estimate on all five measures. The order among them uses the largest percentage-point gap and then county name.

Do not present this list as the correct allocation answer. It is the reproducible answer to one deliberately simple screening rule. A good learner may propose another twelve-county review list when the rule is visible and the action remains proportional.

## Concept key

### Shared scale

All five selected measures are percentages of adults and use the same 2022 measure year. A shared 0 to 46 percent scale preserves absolute prevalence differences. Free scales make each panel fill its width and can falsely imply equal variation.

A shared unit does not make the measures interchangeable. Smoking, diagnosed diabetes, self-rated health, physical activity, and obesity have different definitions and implications.

### Shared order

One county order lets a reader trace the same row across panels. Sorting each panel by its own point estimate makes local ranking easy but destroys cross-panel row tracking. The correct order depends on the reader task.

### Comparator

The reference lab uses the matching U.S. age-adjusted point estimate in every panel. The numeric value differs because the measure differs, but the definition is stable.

Using a separate state median in each state panel can answer a within-state question. It becomes misleading when the color label implies one common threshold across states.

### Crude and age adjusted

Crude prevalence describes the modeled county population as represented. Age-adjusted prevalence supports comparisons under a common age distribution. The dumbbell is not a time slope. Movement from crude to adjusted is not improvement or deterioration.

### Confidence intervals

PLACES reports 95 percent confidence intervals derived through Monte Carlo simulation. The reference subtracts the national point estimate from the county interval only to show descriptive location around zero. It does not calculate a formal difference interval or pairwise test.

### Denominator

The all-county comparison denominator is 100 counties. Adult population ranges by more than 300-fold. Age-adjusted prevalence supports comparative burden, while adult population helps estimate outreach scale. Neither should silently replace the other.

### Profile count

Counting measures above a national point is simple and transparent. It also gives five measures equal weight, ignores correlation, omits readiness and cost, and reduces continuous estimates to yes or no. Use it to teach disclosure, not to legitimize a score.

## Lab walkthrough

### Figure 1: all counties

Ask learners to trace Robeson and Swain across all five panels. Then ask what disappears when each panel sorts itself. Point out that all 100 confidence intervals remain, even though only twelve names print.

### Figure 2: difference from national

The zero line has one definition: county age-adjusted point minus matching national age-adjusted point. Ask why the interval crossing zero is not a formal pairwise result.

### Figure 3: crude and adjusted dumbbells

Ask which counties move left or right and why that direction cannot be called improvement. Have learners state whether the decision is comparison, outreach scale, or both.

### Figure 4: profile-count denominator

The key finding is that 54 counties exceed all five national points. The national reference distinguishes North Carolina from the country more than it narrows the county list. Ask what local information should enter next.

## Critique key

### C1: free panel scales

Expected defects:

- the same visual width represents different percentage-point ranges;
- absolute measure levels disappear;
- panels appear equally variable;
- the viewer must read five axes before comparing;
- national references and intervals are missing.

The preferred repair uses one fixed prevalence scale. A standardized scale can pass only when the transformed question and loss of raw units are explicit.

### C2: changing panel baselines

Expected defects:

- red means above a different number in every state;
- the shared label suggests one common threshold;
- a county with the same value can switch class by panel;
- state mix and local distribution determine the label;
- no national or policy comparator is available.

An acceptable repair uses one reference across states or directly labels each state-specific median without reusing one status label.

### C3: overloaded rainbow profiles

Expected defects:

- thirty county identities rely on color;
- the legend is removed because it cannot fit;
- line crossings dominate;
- connecting different constructs implies continuity;
- uncertainty, population, reference, and exact values disappear.

Ordered small multiples or a profile table are stronger repairs.

## Submission review order

Review in this order:

1. source and 500-row completeness;
2. decision and action boundary;
3. shared scale and comparator definition;
4. shared ordering rule;
5. shortlist reproducibility;
6. crude and adjusted interpretation;
7. uncertainty and adult population;
8. accessibility and exact table;
9. decision note;
10. reproducibility and AI-use record.

Return the work before visual-design scoring if counties or measures disappear, the shortlist is hand selected, or the recommendation becomes automatic allocation.

## Acceptable decision language

An acceptable conclusion is:

> Invite the twelve listed counties to a partnership-readiness review because their point estimates exceed the matching national estimate on all five selected measures and they have the largest gaps under the declared teaching order. Do not allocate funds from this screen alone. Fifty-four counties meet the five-of-five condition, the measures are correlated model estimates, and the rule omits population scale, within-county inequity, local priorities, intervention fit, and implementation capacity.

Other conclusions may pass when they follow a visible rule and preserve the review boundary.

## Claims that do not pass

- "These are the twelve least healthy counties."
- "The five measures prove a common cause."
- "The crude-to-adjusted movement shows improvement."
- "Overlapping intervals prove the counties are the same."
- "A county above its state median is nationally high."
- "The score validates where funding should go."
- "The county estimate describes every group within the county."

## Accessibility review

Module 07 requirements remain binding. Check that:

- shortlist status uses shape as well as color;
- estimate type uses shape and direct legend text;
- the county order remains available through the exact table;
- small labels remain readable in print and a smaller view;
- the main pattern survives grayscale;
- the short and long alternatives name scale, order, comparator, uncertainty, and shortlist;
- the exact table contains all 500 rows.

## Handoff to Module 10

Module 10 asks whether place adds information that the ordered comparison does not. Learners must carry the same rate, denominator, uncertainty, source, accessibility, and claim rules into mapping. A map is not automatically better because the rows are counties.

## Human release gates

The module still needs named reviews for:

- population-health decision relevance;
- epidemiology and PLACES source fidelity;
- equity framing and community language;
- visualization teaching quality;
- accessibility and assistive-technology use;
- independent teachability on a clean system.
