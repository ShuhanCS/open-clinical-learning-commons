# Module 09 assessment

## Decision prompt

You support a North Carolina population-health director who can invite twelve counties into a partnership-readiness review. The director has received an overloaded rainbow chart and five small-multiple panels that change scales and reference lines. The graphics make some counties look consistently extreme, but the comparison rule is not visible.

Build a comparison package that shows all 100 counties, preserves five CDC PLACES measures and their uncertainty, and explains how your twelve-county review list was created. The list opens a conversation. It does not allocate funds, assign blame, or prescribe an intervention.

## Source boundary

Use `data/nc_county_health_profiles_2024.csv` or rebuild it from the pinned CDC PLACES query. You may use `data/places_county_comparison_2024.csv` for a declared peer-state sensitivity analysis.

Do not:

- introduce patient-level or restricted data;
- remove counties because they crowd the chart;
- replace age-adjusted values with crude values without changing the question;
- use a different x scale or ordering rule in comparable panels without a visible reason;
- change the comparator from one panel to another without naming it;
- turn interval overlap into a significance test;
- call the profile count a validated risk or equity score;
- treat a higher modeled estimate as evidence of cause, readiness, or failed leadership;
- select counties only because a map or color makes them look prominent.

## Part 1: comparison audit

In `comparison-brief.md`, answer:

1. Who owns the decision and what happens after a county is shortlisted?
2. What is one row in the teaching release?
3. Which estimates are crude and which are age adjusted?
4. What does the adult population add to the decision?
5. Which panels are comparable in unit, population, year, scale, and reference definition?
6. What order will be reused across panels?
7. What information is lost when each panel sorts independently?
8. What information is lost when every panel uses a free scale?
9. What does a national reference reveal, and why does it fail to produce a narrow list here?
10. What evidence would be required before a partnership invitation becomes a funding or intervention decision?

Record the exact source URL, query, retrieval date, checksums, selected measures, measure year, and tool versions.

## Part 2: run the reference lab

Run:

```powershell
Rscript lab.R
```

Inspect all four figures, the exact table, and the text alternative. Record:

- how the same county order helps scanning across five panels;
- what the shared 0 to 46 percent scale preserves;
- why the national reference has the same definition but a different numeric value in each measure panel;
- which counties move when crude values become age adjusted;
- why 54 counties above all five national point estimates weakens a national-only screening rule;
- which facts remain available only in the exact table and long description.

## Part 3: critique and repair

Run:

```powershell
Rscript critique_charts.R
```

For each flawed display, document the reader task, defect, likely decision error, repair, evidence that the repair worked, and one remaining limit.

### C1: free panel scales

Explain why every measure appears to have comparable spread when each panel stretches its local range. Repair the display with a shared absolute scale or a clearly named transformed scale that answers a different question.

### C2: changing panel baselines

Explain why using each state's own diabetes median changes the meaning of red from panel to panel. Repair the display with one declared comparator or directly label each comparator and stop using a shared status label.

### C3: overloaded rainbow profiles

Explain why thirty connected color-only lines do not support county identification or reliable comparison. Repair the display with ordered small multiples, direct labels, a focused subset, or an exact table. Do not connect different measures as though they were a time series.

## Part 4: all-county comparison

Create `all-groups.png`. It must:

- include all 100 counties and all five age-adjusted measures;
- keep one x scale across the five comparable prevalence panels;
- keep one county order across panels;
- state the ordering rule;
- show the matching national age-adjusted reference in every panel;
- preserve the CDC 95 percent confidence limits;
- label the measure year and source;
- distinguish any emphasized counties without relying on color alone;
- point to the exact table and text alternative.

The figure does not need to print all 100 names if the exact table and stable order provide a clear access path. Every point must remain present.

## Part 5: shortlist profile

Create `shortlist-profile.png` for exactly twelve counties. The figure must answer: on which measures, and by how much, does each shortlisted county differ from the matching national point estimate?

Use one consistent zero definition across panels. If you standardize values, record the formula and retain percentage-point values in `decision-table.csv`.

The shortlist rule must be explicit and reproducible. You may use the reference rule or create a defensible alternative. An alternative rule must state:

- included measures;
- weights, if any;
- comparator;
- uncertainty treatment;
- population or capacity role;
- tie-breaking;
- why the rule is suitable for review but not automatic allocation.

## Part 6: adjustment comparison

Create `adjustment-comparison.png` that shows crude and age-adjusted estimates for the twelve shortlisted counties. A dumbbell, slope display, aligned dots, or table may be used.

The figure must:

- keep crude and adjusted estimates distinguishable without hue;
- use a fixed scale across comparable panels;
- avoid words such as improvement, decline, before, or after;
- state that age adjustment changes the comparison question rather than changing county health;
- keep adult population in the exact table.

## Part 7: exact-value table

`decision-table.csv` contains all 500 county-measure rows and at least these columns:

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

The table is sorted first by the declared county order, then by a fixed measure order. It includes exactly twelve counties with `shortlist = TRUE`.

## Part 8: text alternative

`alt-text.md` contains:

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

The short alternative identifies the five-panel comparison and main finding in one or two sentences. The long description names the order, scale, reference, measure ranges, shortlisted counties, uncertainty, denominator, and interpretation limits. It points to `decision-table.csv` for all values.

## Part 9: decision note

`decision-note.md` contains:

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

The action may invite counties to a readiness review, request local validation, or revise the comparison rule. It may not automatically allocate money or prescribe a program from the five PLACES estimates.

## Exact submission

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

An approved alternative tool may replace `analysis.R` with an editable source file that regenerates all three figures and the CSV. Manual edits made only to exported PNG files do not meet the requirement.

## Rubric

| Criterion | Weight | Full-credit evidence |
|---|---:|---|
| Source fidelity and comparison structure | 15% | All counties, measures, years, estimates, intervals, populations, and references are preserved. |
| All-county small multiples | 15% | One scale, one order, and one comparator definition support reliable scanning across five panels. |
| Shortlist rule and profile | 20% | Exactly twelve counties follow a visible, reproducible review rule with no hidden weighting or allocation claim. |
| Adjustment and denominator judgment | 10% | Crude and adjusted estimates are compared accurately, and population scale remains available. |
| Uncertainty and reference interpretation | 10% | Intervals and point differences are shown without unsupported significance or equivalence claims. |
| Critique and repair | 10% | Free scales, changing baselines, and rainbow overload are diagnosed as decision problems and repaired. |
| Accessibility and exact alternatives | 10% | Redundant cues, readable contrast, complete text alternatives, and a 500-row table provide equivalent access. |
| Reproducibility | 5% | The editable analysis regenerates figures and table from the released data. |
| Decision note and AI accountability | 5% | The action fits a review decision, and AI use or non-use is recorded with human verification. |

Passing requires at least 80 percent overall and every pass condition below.

## Noncompensable pass conditions

- All 100 counties and all five measures remain in the analysis and exact table.
- Comparable panels use one visible x scale or a clearly justified transformation.
- One county order is reused across comparable panels.
- Every reference line has the same declared definition across panels.
- The shortlist contains exactly twelve unique counties and follows reproducible code.
- No hidden composite score or undeclared weight determines the shortlist.
- Crude and age-adjusted estimates are not described as before and after values.
- Interval overlap is not described as a formal pairwise test.
- Adult population and the 100-county comparison denominator remain available.
- The recommendation is a review action, not automatic allocation or intervention.
- Color is not the only county, estimate-type, or status cue.
- Short text, long text, and the complete table are present.
- The analysis is editable and reproducible.
- No restricted patient or partner data are included.
- `ai-use.md` is complete, including when no AI was used.
