# Instructor notes

## Teaching position

This module is about choosing the denominator and comparison quantity before choosing the chart.

Do not let the lesson become a general lecture on epidemiology or a complete derivation of age standardization. The learner must leave able to distinguish a modeled count, crude prevalence, and age-adjusted prevalence in a real public health decision.

## Decision answer in one paragraph

Use modeled age-adjusted prevalence for the first cross-county partnership shortlist because the decision begins with comparative prevalence. Keep the modeled adult count and PLACES adult population in the companion table because outreach scale is a separate operational question. Treat the shortlist as a screening step, not a final invitation or funding decision. Obtain local surveillance, current service capacity, community priorities, access barriers, program readiness, and within-county evidence before acting.

## Released answer key

### Top 12 by age-adjusted prevalence

| Rank | County | Adjusted % | 95% interval | Crude rank | Count rank | Modeled count | PLACES adults | Warning |
|---:|---|---:|---|---:|---:|---:|---:|---|
| 1 | Robeson | 15.6 | 13.7 to 17.5 | 9 | 20 | 15,165 | 87,156 | No |
| 2 | Hertford | 15.0 | 13.1 to 17.2 | 7 | 73 | 3,108 | 17,171 | No |
| 3 | Bertie | 14.9 | 13.1 to 17.1 | 3 | 80 | 2,725 | 14,342 | No |
| 4 | Scotland | 14.8 | 12.9 to 16.8 | 12 | 61 | 4,447 | 26,314 | No |
| 5 | Halifax | 14.5 | 12.7 to 16.7 | 5 | 45 | 6,998 | 37,624 | No |
| 6 | Warren | 14.5 | 12.5 to 16.5 | 2 | 77 | 2,952 | 15,455 | No |
| 7 | Edgecombe | 14.3 | 12.4 to 16.3 | 8 | 47 | 6,543 | 37,386 | No |
| 8 | Anson | 13.9 | 12.1 to 15.9 | 15 | 78 | 2,927 | 17,846 | No |
| 9 | Northampton | 13.9 | 12.1 to 15.7 | 1 | 79 | 2,770 | 13,851 | No |
| 10 | Greene | 13.8 | 12.0 to 15.8 | 29 | 82 | 2,503 | 16,362 | No |
| 11 | Washington | 13.8 | 11.9 to 15.7 | 4 | 89 | 1,636 | 8,655 | Yes |
| 12 | Wilson | 13.7 | 11.9 to 15.7 | 16 | 32 | 9,947 | 60,652 | No |

The table supports a first-pass comparison. It does not demonstrate that adjacent ranks differ statistically.

### Top 12 by modeled adult count

Mecklenburg, Wake, Guilford, Forsyth, Cumberland, Durham, Gaston, Buncombe, Johnston, Union, New Hanover, and Cabarrus.

None appear in the top 12 by age-adjusted prevalence.

### Top 12 by crude prevalence

Northampton, Warren, Bertie, Washington, Halifax, Martin, Hertford, Edgecombe, Robeson, Lenoir, Hyde, and Scotland.

Nine appear in the age-adjusted top 12.

## Measured contrasts

- Count range: 428 to 93,326 modeled adults.
- Crude prevalence range: 8.5% to 20.0%.
- Age-adjusted prevalence range: 8.0% to 15.6%.
- Adult population range: 2,644 to 908,531.
- Largest count-to-adjusted rank change: 93 places.
- Largest crude-to-adjusted rank change: 57 places.
- Count and adjusted top-12 overlap: zero counties.
- Crude and adjusted top-12 overlap: nine counties.
- Training low-denominator warnings: nine counties.

These values are release checks. If a source or build changes, do not update them by hand. Rebuild, validate, review, version, and release the data.

## Counterexamples to teach

### Wake

- Modeled-count rank: 2
- Adjusted-prevalence rank: 95

Wake demonstrates why a count ranking answers population scale rather than comparative prevalence.

### Buncombe

- Modeled-count rank: 8
- Adjusted-prevalence rank: 100

This is another clear population-scale counterexample.

### Hertford

- Modeled-count rank: 73
- Adjusted-prevalence rank: 2

Hertford demonstrates how a smaller county can move into the comparative shortlist while remaining a smaller outreach population.

### Washington

- Modeled-count rank: 89
- Crude-prevalence rank: 4
- Adjusted-prevalence rank: 11
- PLACES adults: 8,655

Washington belongs in a first-pass adjusted shortlist but triggers the declared training warning. It sets up Module 06.

### Cumberland

- Crude-prevalence rank: 84
- Adjusted-prevalence rank: 27

Cumberland has the largest crude-to-adjusted rank change in the release. Ask what age adjustment changes, but do not ask learners to explain the full model from one ACS older-adult share.

## Lab answer key

### Figure 1: modeled count

Expected finding: populous counties dominate. The figure is useful for approximate scale if the model status is explicit. It is not a fair prevalence ranking.

### Figure 2: crude prevalence

Expected finding: the order changes sharply. Smaller counties appear near the top because the adult denominator is now explicit. The comparison still reflects county age structure.

### Figure 3: adjusted prevalence with denominator

Expected finding: age-adjusted prevalence supports the comparison while population and modeled count remain visible. Washington is the only adjusted top-12 county that triggers the 10,000-adult warning.

The intervals overlap substantially. Learners should not claim that every rank is a statistically distinguishable difference.

### Figure 4: rank change

Expected finding: the apparent priority depends on the quantity. Wake and Buncombe move from the highest modeled-count ranks to the lowest adjusted-prevalence ranks. Hertford, Bertie, Warren, Anson, Northampton, Greene, and Washington move in the opposite direction.

## Critique key

### C1. Raw modeled-count choropleth

Errors:

- the title calls modeled values `Adults with diabetes` without qualification;
- population scale drives the fill;
- the adult denominator is hidden;
- no prevalence, interval, model status, period, or exact value is available;
- geography adds visual prominence without answering the comparative question; and
- a director could mistake outreach scale for higher prevalence.

Repair:

Use an aligned age-adjusted prevalence comparison for the shortlist. Add source intervals and a companion table with PLACES adults and modeled count. Keep a map only if place-based logistics or regional pattern is part of the decision. If a map remains, use a comparable prevalence estimate and supply exact values.

### C2. Rate without denominator or interval

Errors:

- `rate` is vague;
- `percent` does not name the adult population;
- adjustment status is hidden;
- source interval is missing;
- measure year and release are absent;
- model status is absent;
- no low-denominator warning appears; and
- the director cannot see service scale.

Repair:

Name `modeled age-adjusted prevalence among adults age 18 and older`. Add intervals, period, release, and warning shape. Pair the figure with an exact table containing adult population and modeled count.

## Model language

Accept:

- modeled prevalence;
- modeled adult count;
- source estimate;
- first-pass comparison;
- higher in this release;
- supports local follow-up; and
- cannot establish individual status or cause.

Require revision:

- observed cases;
- actual number with diabetes;
- incidence;
- people in this county are more likely because they live there;
- the program will reduce diabetes; or
- this county deserves more funding.

## Denominator checkpoints

Ask these aloud:

1. Who is eligible for the numerator concept?
2. Which population belongs in the calculation?
3. Does the source period match the population period?
4. Is the displayed value crude or adjusted?
5. Is the value observed, surveyed, or modeled?
6. What decision does population size answer?

Do not accept `the county population` as a complete denominator answer. The source population is adults age 18 and older.

## ACS handling

The ACS file is intentionally separate from the PLACES population field.

Strong learners may notice that ACS adults differ from PLACES adults by -6.4% to 8.5% across the 100 counties. The median difference is about -0.2%. This is expected because the sources and periods differ.

Do not let learners choose whichever denominator produces the preferred count. The formula uses the PLACES adult population because it travels with the crude model estimate.

The ACS margin of error remains useful population context and prepares learners for Module 06.

## Training warning

The nine flagged counties are:

- Alleghany
- Camden
- Clay
- Gates
- Graham
- Hyde
- Jones
- Tyrrell
- Washington

Be explicit: this is a course threshold, not a CDC rule. The source value remains in the audit table. The warning changes the certainty of the decision, not the historical source.

## Accessibility review

The reference adjusted view uses:

- aligned horizontal position;
- direct population and count text;
- shape plus text for the warning;
- visible intervals;
- high-contrast labels; and
- a separate exact CSV.

Accept another design when it provides the same information access. Do not require the reference colors or chart type.

## Equity and place language

Require `higher modeled age-adjusted prevalence in this release` rather than labels such as unhealthy, high-risk people, noncompliant, or deficient.

The final note should invite local validation rather than announce intervention on a county. Ask learners whose knowledge is absent from the public dataset and how a county-wide estimate may hide communities within the county.

## Grading anchors

### Excellent

The learner chooses a decision-matched quantity, keeps denominator and interval context, shows meaningful rank changes, uses a transparent shortlist rule, asks for local evidence, and writes a claim that remains within the model and ecological boundaries.

### Passing

The learner correctly distinguishes the three quantities, reproduces the analysis, includes all six files, and avoids prohibited claims. The display may be plain.

### Revision required

Any mandatory-condition failure in `assessment.md`, especially converting adjusted prevalence to count, calling a modeled count observed, hiding the adult denominator, or making an individual inference.

## Suggested pacing

| Time | Activity |
|---:|---|
| 0:00 to 0:30 | Decision and source orientation |
| 0:30 to 1:30 | Count versus percentage calculation |
| 1:30 to 2:45 | Denominator audit |
| 2:45 to 4:00 | Crude versus adjusted comparison |
| 4:00 to 5:45 | Tiered lab |
| 5:45 to 6:30 | Critique and repair |
| 6:30 to 7:45 | Independent assignment |
| 7:45 to 8:00 | Exit check and Module 06 handoff |

## Exit check

The learner passes the exit when they can complete this sentence accurately:

> I would use age-adjusted prevalence for ________, crude prevalence for ________, and a modeled count for ________. I still need Module 06 because ________.
