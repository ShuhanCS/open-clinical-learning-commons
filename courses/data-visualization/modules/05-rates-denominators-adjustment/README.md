# Module 05: Rates, denominators, and adjustment

A North Carolina population-health program can invite up to 12 counties into a first adult diabetes-prevention partnership. Which counties should receive the first invitation?

The answer changes when the display uses a modeled count, crude prevalence, or age-adjusted prevalence. That is the lesson.

## What you will be able to do

By the end of this module, you can:

- identify the numerator concept and eligible denominator behind a health measure;
- explain why count, crude prevalence, and adjusted prevalence answer different questions;
- calculate a modeled count without calling it observed;
- choose a comparable county measure for a stated decision;
- keep population, interval, period, and adjustment status with the display;
- flag a low denominator using a declared rule;
- avoid assigning a county result to an individual resident; and
- make a source-bounded recommendation for a population-health director.

## The decision

The director has two related questions:

1. Where is modeled adult diabetes prevalence higher after county age distributions are standardized?
2. How large might the outreach population be?

The first question is comparative. The second is about scale. One ranking cannot answer both.

## Start with the measure

The CDC source calls the measure `Diagnosed diabetes among adults`. PLACES reports a modeled prevalence estimate for adults age 18 and older.

It is not:

- an observed registry count;
- a claims count;
- incidence or new diagnoses;
- the percentage of all residents, including children;
- an individual risk score; or
- a measured intervention effect.

The module uses every national `DIABETES` row from the PLACES county dataset and joins the North Carolina case to public ACS population context.

## Three quantities, three questions

### Modeled adult count

The teaching release derives:

```text
modeled adult count = crude prevalence / 100 * PLACES adult population
```

This can help approximate outreach scale. It remains modeled because the prevalence is modeled.

Large counties tend to have large modeled counts even when their prevalence is lower. In this release, Mecklenburg has the largest modeled count at 93,326, while its age-adjusted prevalence ranks 58th among North Carolina counties.

### Crude prevalence

Crude prevalence estimates the share of the county's current adult population represented by the measure. It keeps the county's age distribution.

This makes it useful for describing the modeled local adult population. It can mislead a cross-county comparison when age structures differ.

### Age-adjusted prevalence

Age-adjusted prevalence standardizes age structure so counties can be compared on a more similar age basis.

It is appropriate for the first comparative shortlist in this case. It is not the county's expected local count, so do not multiply it by population.

## Why the denominator matters

Consider these statements:

- `93,326 adults`
- `10.5% crude prevalence`
- `10.8% age-adjusted prevalence`

They may describe the same county, but they do not mean the same thing.

For every value, write:

| Question | Required answer |
|---|---|
| What is counted or estimated? | The numerator concept. |
| Who could be in the measure? | The eligible population. |
| What is the unit? | People, percent, events per population, or another unit. |
| What is the geography? | County. |
| What is the period? | Measure year and release. |
| Is it crude or adjusted? | The comparison basis. |
| Is it observed, surveyed, or modeled? | The evidence type. |

If one row of this table is missing, the display is not ready for a decision.

## Two public population fields that must stay separate

PLACES carries a Census 2022 adult population used in its county modeling. The module uses that field in the modeled-count calculation.

The separate ACS file describes the 2020-2024 population and includes margins of error. It provides context and a denominator check. It is not silently substituted for the PLACES adult population.

Different sources and periods can both be useful. They cannot be treated as interchangeable.

## Adjustment in plain language

Counties have different age structures. Diagnosed diabetes prevalence is related to age. A crude comparison can therefore reflect both the health measure and the age distribution.

Age adjustment asks what the modeled comparison would look like after applying a common age standard. It improves comparability. It does not turn the estimate into a local case count or remove every difference between counties.

In the released North Carolina case:

- the largest crude-to-adjusted rank change is 57 places;
- the top 12 crude and top 12 adjusted lists share nine counties; and
- Cumberland rises from crude rank 84 to adjusted rank 27.

An older-population share can help prompt questions about rank change. It does not reconstruct or explain the complete adjustment.

## Count order is not prevalence order

The top 12 modeled counts and top 12 age-adjusted prevalence values have no counties in common in this release.

Wake illustrates the difference:

- modeled-count rank: 2;
- age-adjusted prevalence rank: 95.

Hertford illustrates the reverse:

- modeled-count rank: 73;
- age-adjusted prevalence rank: 2.

Neither quantity is wrong. Each answers a different question.

## Confidence limits travel with the estimate

PLACES supplies a 95% confidence interval for every released prevalence estimate. Keep it in the table and, when practical, the figure.

This module does not reduce intervals to a yes-or-no significance rule. Module 06 teaches uncertainty and small-number stability. Here, the interval is a reminder that a modeled point is not exact.

## Suppression and the training warning

The CDC source does not suppress the North Carolina diabetes estimates in this release.

The module uses a declared training rule:

```text
warn when PLACES adult population is below 10,000
```

Nine counties trigger it. The warning means that a rank should not be decisive without local validation. It does not mean CDC marked the estimate invalid.

Never invent source suppression. If your organization uses a publication threshold, name who set it, which field it uses, and what happens to the displayed value.

## The ecological fallacy

A county estimate describes an area. It does not describe every resident.

You may write:

> Robeson has the highest modeled age-adjusted prevalence in this North Carolina release.

You may not write:

> A resident of Robeson is more likely to have diabetes because they live there.

The county comparison does not identify an individual's diagnosis, risk, exposure, access, behavior, or treatment.

## Public sources

- CDC PLACES county dataset, 2024 release: https://data.cdc.gov/d/fu4u-a9bh
- CDC PLACES methodology: https://www.cdc.gov/places/methodology/index.html
- CDC PLACES health-outcome definitions: https://www.cdc.gov/places/measure-definitions/health-outcomes.html
- CDC PLACES FAQ: https://www.cdc.gov/places/faqs/index.html
- Census ACS 5-year data: https://www.census.gov/data/developers/data-sets/acs-5year.html
- Census ACS Summary File: https://www.census.gov/programs-surveys/acs/data/summary-file.html
- Census ACS Summary File handbook: https://www2.census.gov/programs-surveys/acs/summary_file/handbooks/acs_table_based_summary_file_handbook.pdf
- Census generalized ACS 2024 county map service: https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer

Read `source-record.yml` before analyzing the data.

## Run the package

Requirements:

- Python 3 for the source build and validator;
- R 4.3 or later for the reference lesson; and
- R package `ggplot2`.

From this module directory:

```powershell
python validate_county_rates.py
Rscript lab.R
Rscript critique_charts.R
```

Generated files go to `outputs/`, which is working space and is not part of the assessed submission.

## Rebuild the source data

```powershell
python build_county_rates.py
```

The build downloads about 201 MB of public source data, verifies pinned hashes, and writes four compact teaching CSV files.

The source hash check is intentional. If a publisher changes a file, the correct response is a new reviewed data release, not a silent overwrite.

## Tier 1: Run

Run `lab.R`. It produces:

1. `01-modeled-count.png`
2. `02-crude-prevalence.png`
3. `03-adjusted-with-denominator.png`
4. `04-rank-change.png`
5. `county_decision_table.csv`

Answer:

1. Why do the top modeled-count and adjusted-prevalence lists differ?
2. Which quantity should drive the first comparative shortlist?
3. Which quantity helps plan outreach scale?
4. Which counties change most across rankings?
5. Which counties receive the training warning?
6. What local information could change the shortlist?

## Tier 2: Modify

Make these changes:

1. Select a different reproducible comparison set.
2. Add a population or modeled-count annotation that remains readable.
3. Rewrite the title so it states a measured finding.
4. Produce one version without a denominator and explain why it fails.

Do not alter the source values or replace the denominator.

## Tier 3: Author

Build an independent decision figure from `data/nc_diabetes_rates_2024.csv`.

Your design may differ from the reference. It must still:

- answer the director's comparative question;
- use an appropriate quantity;
- keep population and interval context available;
- state measure year, release, and adjustment status;
- flag low denominators;
- provide exact values and alt text; and
- avoid claims the source cannot support.

## Critique set

Run `critique_charts.R`.

### C1. Raw modeled-count choropleth

The map title says `Adults with diabetes by county`. It does not say modeled, does not show the adult denominator, and makes populous counties look like the highest-prevalence counties.

Repair:

- decide whether the task is comparison or service scale;
- use a comparable prevalence estimate for comparison;
- keep the modeled count in a table for scale;
- name the modeled nature of the count; and
- do not assume a map is needed simply because county geography exists.

### C2. Rate without denominator or interval

The chart says `County diabetes rates` and `Percent`. It omits the adult population, age-adjustment status, source interval, period, model status, and low-denominator warning.

Repair:

- name the exact estimate;
- show or provide the interval;
- retain the adult denominator;
- identify low denominators;
- label the period and release; and
- use an exact companion table.

## Independent assignment

The program can invite up to 12 counties. Submit the exact package in `assessment.md`.

The strongest response uses age-adjusted prevalence for a transparent comparative shortlist, keeps modeled count and adult population for capacity planning, and makes the recommendation conditional on local evidence.

## What local evidence is still needed

At minimum, ask for:

- current local surveillance or clinical counts with definitions;
- prevention services already available;
- access barriers and transportation;
- community priorities and trusted partners;
- program capacity and readiness;
- within-county differences; and
- evidence that the proposed intervention fits local needs.

## Handoff to Module 06

This module preserves confidence limits and flags small denominators. Module 06 asks how much confidence the director should place in the apparent differences and which rankings overstate the evidence.
