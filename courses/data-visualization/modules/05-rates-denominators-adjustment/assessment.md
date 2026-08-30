# Module 05 assessment

## Decision prompt

The North Carolina population-health program can invite up to 12 counties into a first adult diabetes-prevention partnership.

Create one decision figure and a rate audit that distinguishes comparative prevalence from outreach scale. Recommend a transparent first-pass shortlist and identify the local evidence required before invitations are final.

## Exact submission

Submit exactly:

```text
module-05/
  rate-audit.md
  analysis.R
  figure.png
  source-record.yml
  alt-text.md
  decision-note.md
```

Do not submit saved workspace files, generated caches, private data, or a screenshot that cannot be reproduced.

## Required data

Use:

```text
data/nc_diabetes_rates_2024.csv
```

You may use the national source extracts for verification. Do not replace or edit the released source values.

## Required analysis

Your work must:

1. name the decision owner and exact decision;
2. define the adult population and county unit;
3. identify the source measure as modeled prevalence;
4. verify the modeled-count formula using crude prevalence and the matching PLACES adult population;
5. compare modeled-count, crude-prevalence, and age-adjusted-prevalence ranks;
6. declare a reproducible rule for selecting no more than 12 counties;
7. keep population, source interval, measure year, release, adjustment status, and low-denominator warning available;
8. identify at least two counties whose interpretation changes when the quantity changes;
9. distinguish the comparative shortlist from outreach scale;
10. state the ecological limit; and
11. name at least three local facts required before action.

## `rate-audit.md`

Use these exact headings:

```text
# Rate audit
## Decision and eligible population
## Numerator concept and denominator
## Count, crude, and adjusted comparison
## Rank changes
## Low-denominator and interval checks
## Ecological limit
## Reproducibility check
## AI assistance disclosure
```

### Decision and eligible population

State:

- the program director's decision;
- adults age 18 and older as the measure population;
- county as the unit;
- the measure year and release label; and
- why a first-pass comparison is not a final funding decision.

### Numerator concept and denominator

Provide this table:

| Quantity | Numerator concept | Denominator or scale field | Adjustment | Legitimate use |
|---|---|---|---|---|
| Modeled adult count |  |  |  |  |
| Crude prevalence |  |  |  |  |
| Age-adjusted prevalence |  |  |  |  |

Write the modeled-count formula. State that the result is not observed cases.

### Count, crude, and adjusted comparison

Report:

- the top 12 under each quantity;
- overlap between the lists;
- value and rank for at least two counterexample counties; and
- why the quantities produce different orders.

### Rank changes

Name at least:

- one populous county that falls when moving from count to adjusted prevalence;
- one less populous county that rises; and
- one county whose crude and adjusted ranks differ materially.

Do not claim that ACS older-adult share fully explains the adjustment.

### Low-denominator and interval checks

State the course warning threshold. Name any shortlisted county that triggers it. Keep source intervals in the exact table and explain why Module 06 is still needed.

### Ecological limit

Write two sentences:

1. what the county estimate describes; and
2. what cannot be inferred about an individual resident.

### Reproducibility check

Record:

- input filename;
- input SHA-256;
- number of rows read;
- shortlist rule;
- output filename;
- software and package versions; and
- result of rerunning `analysis.R` in a clean session.

### AI assistance disclosure

State the tool and version when known, task assisted, prompts or prompt summary, changes made after review, and facts checked against the sources. Write `No AI assistance used` if none.

## `analysis.R`

Your script must:

- use a relative input path;
- read county FIPS as character;
- verify required columns;
- stop clearly when the input contract is broken;
- calculate modeled count only from crude prevalence and PLACES adults;
- reproduce your ranks and shortlist;
- write `figure.png`;
- print the exact decision table; and
- avoid absolute paths, private data, manual row edits, and hidden workspace objects.

You may use base R and packages already declared by the course environment. Record every added package in `source-record.yml` and your reproducibility check.

## `figure.png`

The figure must:

- answer the comparative partnership question;
- display no more than a readable county set;
- name `modeled age-adjusted prevalence` unless another measure is explicitly defended;
- show or clearly connect to the source 95% interval;
- retain adult population or modeled-count context;
- mark the training low-denominator warning;
- state `2022 measure data, PLACES 2024 release`;
- use a finding title;
- remain interpretable without color; and
- be readable at 1,600 by 1,000 pixels or equivalent.

A map is not required. If you use one, explain why geography matters to the decision and provide an aligned exact comparison.

## `source-record.yml`

Include:

- CDC, Census ACS, and any boundary source used;
- full landing, metadata, query, and file URLs;
- dataset, table, measure, release, period, and geography identifiers;
- retrieval date;
- raw and released hashes when provided by the module;
- row counts;
- transformations;
- rights;
- formulas; and
- claim limits.

You may cite the module source record, but your submitted record must be complete enough for an independent reader to understand your analysis.

## `alt-text.md`

Write 80 to 180 words.

Include:

- chart form;
- displayed county set and rule;
- measured finding;
- highest and lowest displayed adjusted values;
- adult-population or modeled-count context;
- interval treatment;
- low-denominator warning; and
- source period.

Do not list decorative colors or every point.

## `decision-note.md`

Write 250 to 450 words for the population-health program director.

Use these exact headings:

```text
# Decision note
## Recommendation
## Why this quantity matches the decision
## What population scale changes
## Local validation before invitation
## Evidence boundary
```

The recommendation must name no more than 12 counties and state the selection rule. It must be conditional on local validation.

## Required exact table

Place this table in `rate-audit.md` for every recommended county:

| County FIPS | County | Adjusted prevalence | 95% interval | Crude prevalence | PLACES adults | Modeled adult count | Count rank | Crude rank | Adjusted rank | Warning |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|

Round prevalence and interval values to one decimal place. Do not round population or count values before ranking.

## Recognition questions

Answer in `rate-audit.md` after the required sections or in a clearly labeled appendix:

1. Why is a choropleth of modeled adult counts mainly a population map?
2. Why is crude prevalence not always the best county comparison?
3. Why can age-adjusted prevalence not be converted into a county count?
4. What is the correct denominator for the PLACES diabetes measure?
5. What does an interval communicate before formal comparison?
6. What makes a suppression or warning rule legitimate?
7. Give one ecological inference the county data do not support.

## Critique tasks

### C1. Raw modeled-count choropleth

Review `C1-raw-count-choropleth.png` generated by `critique_charts.R`.

Explain:

- which quantity is actually mapped;
- which denominator is hidden;
- why large counties dominate;
- who could make the wrong decision; and
- what display and companion should replace it.

### C2. Rate without denominator or interval

Review `C2-rate-without-denominator.png`.

Identify every missing element needed for the director's decision and sketch a repair.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Decision and estimand | 15 | Owner, decision, adult population, county unit, measure, period, and purpose are explicit. |
| Denominator reasoning | 20 | Count, crude, adjusted, and population fields are correctly distinguished. |
| Source and provenance | 15 | Public sources, identifiers, periods, rights, transformations, and hashes are complete. |
| Analysis and reproducibility | 15 | Code reproduces the exact table, shortlist, and figure. |
| Visualization judgment | 15 | Display supports comparison and preserves denominator, interval, and warning context. |
| Decision interpretation | 10 | Recommendation separates comparison from scale and requests local evidence. |
| Accessibility and exact values | 5 | Alt text, readable labels, redundant cues, and an exact table are present. |
| Responsible claims and AI disclosure | 5 | Model, ecological, and automation boundaries are accurate. |

Total: 100 points.

## Pass conditions

Passing requires at least 75 points and all of these:

1. no age-adjusted estimate is converted into a count;
2. no modeled count is called observed;
3. the adult denominator and source periods are visible;
4. the shortlist rule is reproducible;
5. both the figure and exact table are present;
6. the source record includes full URLs and hashes; and
7. the ecological limit is stated.

Missing a mandatory condition requires revision even when the point score is at least 75.

## Submission self-check

- [ ] Six required files only
- [ ] No absolute path
- [ ] FIPS preserved with leading zeros
- [ ] Modeled count calculated from crude prevalence and PLACES adults
- [ ] Age-adjusted estimate not converted to count
- [ ] No observed-case language
- [ ] No more than 12 recommended counties
- [ ] Selection rule reproducible
- [ ] Measure year, release, population, and adjustment status visible
- [ ] Source intervals retained
- [ ] Low-denominator rule stated
- [ ] Exact values available
- [ ] Alt text complete
- [ ] Ecological limit stated
- [ ] Local validation requested
- [ ] AI assistance disclosed
