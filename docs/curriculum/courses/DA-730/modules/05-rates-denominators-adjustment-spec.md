# DA-730 Module 05 specification: Rates, denominators, and adjustment

- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module: 05 of 13
- Course week: 3
- Learner time: 8.0 hours
- Specification version: 0.1.0
- Target Commons release: 0.16.0
- Status: implementation specification
- Source design: Ali Goff course redesign, expanded into the Commons contract under Shuhan He's curriculum direction
- Last updated: 2026-08-29

## 1. Module identity and place in the course

Module 05 teaches a non-negotiable healthcare data habit: a comparison is not interpretable until the numerator, denominator, population, period, and adjustment status are named.

The module follows Module 04, where learners discover that a valid summary can hide a clinically important distribution. It asks the next question: even when a percentage or rate is correctly calculated, are the compared populations large enough, defined the same way, and similar enough for the display to support the decision?

This module is the first half of the week-3 visualization judgment checkpoint. Module 06 adds formal uncertainty, variation, and small-number stability. Module 05 must therefore preserve confidence limits and small-denominator warnings without turning into a complete inference lesson.

The public reference implementation is software flexible. R is the supported learner path because the surrounding course package already provides runnable R lessons. The assessment grades the reasoning, source record, display, and decision, not loyalty to one tool.

## 2. Healthcare decision and audience

### Decision owner

The decision owner is a North Carolina population-health program director preparing a county technical-assistance cohort for adult diabetes prevention.

### Decision

The director must identify up to 12 counties for a first prevention partnership and explain how the evidence will be used for two different tasks:

1. compare modeled adult diabetes prevalence across counties; and
2. understand the scale of the adult population and modeled burden for outreach planning.

The first task needs a comparable prevalence estimate. The second needs population scale. One ranking cannot answer both.

### Required decision distinction

Learners must distinguish these quantities:

| Quantity | Legitimate use | Prohibited shortcut |
|---|---|---|
| Modeled adult count | Approximate scale for planning, derived from crude prevalence and the matching PLACES adult population | Treating it as observed diagnoses, claims, survey respondents, or a fair county ranking |
| Crude prevalence | Describing the modeled share of the current county adult population | Treating age composition as irrelevant |
| Age-adjusted prevalence | Comparing modeled prevalence after standardizing age distributions | Multiplying it by a county population to estimate local case count |
| PLACES confidence limits | Showing that every estimate has a modeled interval | Declaring significance from overlap or non-overlap alone |
| ACS adult population context | Checking population scale and the denominator's period and source | Substituting it silently for the PLACES poststratification population |

### Decision boundary

The module can support a transparent first-pass partnership shortlist and questions for local validation. It cannot establish individual risk, intervention effect, local program quality, diagnosed case inventory, budget need, causal drivers, or a final funding allocation.

## 3. Foundation skill revisited or extended

The foundation skill is proportional reasoning with an explicit analytic unit.

Learners revisit:

- multiplication, division, proportions, percentages, and percentage points;
- the distinction between a number of people and a proportion of a population;
- table joins using a stable key;
- variable names, types, missing values, and units;
- sorting and ranking;
- reproducible calculation from documented source fields; and
- writing a claim whose scope matches the data.

The extension is healthcare standardization. Learners do not derive the PLACES age-adjustment model. They learn what crude and age-adjusted prevalence answer, why the answers differ, and which one belongs with a stated decision.

The key equation is:

```text
modeled adult count = crude prevalence / 100 * matching adult population
```

The equation is allowed only with the crude estimate and the adult population used by the same PLACES release. The result remains modeled. It is not an observed count.

## 4. Assessable learning outcomes

By the end of the module, a learner can:

1. name the numerator concept, denominator, unit of analysis, geography, population, period, and adjustment status for a displayed measure;
2. explain why a county map or ranking of modeled counts largely reflects population size;
3. calculate a modeled count from crude prevalence and its matching adult denominator without calling the result observed;
4. distinguish crude prevalence from age-adjusted prevalence in plain language;
5. identify counties whose apparent priority changes when moving from count to crude prevalence or from crude to age-adjusted prevalence;
6. build a denominator-aware comparison that keeps estimate, population, interval, period, and source available;
7. apply a declared low-denominator or publication rule without inventing suppression in the source data;
8. explain why county-level association cannot be assigned to an individual resident;
9. recommend a defensible county shortlist and state the local evidence needed before action; and
10. reproduce the analysis from the submitted source record and code.

Each outcome is assessed in the exact six-file submission package in Section 14.

## 5. Concept ownership and boundaries

### Concepts owned here

- numerator and denominator;
- count, proportion, percentage, prevalence, and rate language;
- matching a quantity to its eligible population;
- crude and age-adjusted prevalence;
- direct standardization as a comparison idea;
- denominator transparency;
- rank changes caused by population scale or adjustment;
- survey and model denominators;
- explicit publication and suppression rules;
- using a companion table when a chart cannot carry all context; and
- the ecological fallacy in county-level interpretation.

### Concepts introduced but completed later

- confidence intervals and interval comparison, owned by Module 06;
- mapping, classification, and spatial aggregation, owned by Module 10;
- small multiples and shared scales, owned by Module 09;
- time comparison, owned by Module 08;
- dashboard composition, owned by Module 12; and
- final audience narrative, owned by Module 13.

### Concepts explicitly out of scope

- reconstructing the CDC multilevel regression and poststratification model;
- computing a new age-adjusted prevalence from individual records;
- causal modeling of county conditions;
- individual risk prediction;
- statistical significance testing between every county pair;
- causal evaluation of a prevention program;
- patient-level diagnosis or treatment recommendations; and
- funding allocation by an automated score.

### Vocabulary rule

The module uses the source's term `prevalence`. Learners must not replace it with `incidence`, `risk`, `rate of new cases`, or `diagnosed count`. When informal course language uses `rate`, the assessed work must identify the exact source quantity as modeled prevalence.

## 6. Lesson sequence and learner time

The module totals 8.0 learner hours.

| Segment | Hours | Learner work | Evidence produced |
|---|---:|---|---|
| Decision and source orientation | 0.50 | Name the director, decision, measure, population, geography, and source releases. | Decision frame |
| Counts versus percentages | 1.00 | Calculate modeled adult counts and explain why count order follows population scale. | Calculation notes |
| Denominator audit | 1.25 | Match every quantity to its population, period, unit, and source. | Denominator table |
| Crude versus age-adjusted comparison | 1.25 | Compare rank and value changes and explain what standardization changes. | Rank-change table |
| Tiered lab | 1.75 | Run, modify, or author the count, crude, adjusted, and denominator-aware views. | Figures and decision table |
| Critique and repair | 0.75 | Repair a raw-count choropleth and a rate display that omits denominator and interval. | Critique notes |
| Independent exercise | 1.25 | Select up to 12 counties and write the source-bounded recommendation. | Assessed package draft |
| Exit check and Module 06 handoff | 0.25 | State which remaining question requires uncertainty reasoning. | Exit response |

### Scaffold levels

All levels use the same data, decision, competency, and rubric.

| Level | Support |
|---|---|
| Run | Execute the complete reference scripts, inspect the outputs, and answer the guided questions. |
| Modify | Change the county subset, sort order, annotation, or primary comparison while preserving the source and denominator contract. |
| Author | Build the analysis and figure from the released CSVs and decision prompt without using the reference display code. |

## 7. Authoritative readings and public clinical sources

### Required source orientation

1. CDC PLACES county dataset, 2024 release:
   https://data.cdc.gov/d/fu4u-a9bh
2. CDC PLACES methodology:
   https://www.cdc.gov/places/methodology/index.html
3. CDC PLACES health-outcome measure definitions:
   https://www.cdc.gov/places/measure-definitions/health-outcomes.html
4. CDC PLACES frequently asked questions:
   https://www.cdc.gov/places/faqs/index.html
5. U.S. Census Bureau, ACS 5-year data:
   https://www.census.gov/data/developers/data-sets/acs-5year.html
6. U.S. Census Bureau, ACS Summary File:
   https://www.census.gov/programs-surveys/acs/data/summary-file.html
7. U.S. Census Bureau, ACS Summary File handbook:
   https://www2.census.gov/programs-surveys/acs/summary_file/handbooks/acs_table_based_summary_file_handbook.pdf
8. U.S. Census Bureau, TIGERweb ACS 2024 service:
   https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer

### Reading prompts

- What population does PLACES describe?
- Which estimates are modeled rather than direct county survey estimates?
- Why does CDC publish crude and age-adjusted prevalence?
- Which population source belongs in the modeled-count calculation?
- What does the ACS margin of error describe?
- Why can a county-level estimate not identify an individual's condition?

### Link policy

The module records full visible URLs in learner materials and source records. A release check must confirm that the links resolve or record a specific publisher access limitation.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Dataset A: CDC PLACES diabetes county extract

- Source dataset ID: `fu4u-a9bh`
- Source title: `PLACES: Local Data for Better Health, County Data 2024 release`
- Measure ID: `DIABETES`
- Measure label: `Diagnosed diabetes among adults`
- Measure year: 2022
- Data types retained: crude prevalence and age-adjusted prevalence
- Geographic scope: every source row, including 3,144 county or county-equivalent geographies and the source's national summary row
- Expected source rows: 6,290
- Expected county rows: 6,288
- Source API query: pinned in `source-record.yml` and `build_county_rates.py`
- Rights: U.S. federal public data; attribution is required by the Commons even when permission is not

The extract preserves source confidence limits, population fields, footnotes, geography identifiers, and measure labels. No source result is imputed.

### Dataset B: ACS 2020-2024 age and sex table

- Program: American Community Survey
- Product: 2024 ACS 5-year Detailed Tables
- Table: B01001, Sex by Age
- Universe: total population
- Source file: `acsdt5y2024-b01001.dat`
- Source scope: every geography in the national table file
- Teaching extract: every county row identified by a `0500000US` geography ID
- Derived fields: adult population age 18 and older, adult population margin of error, population age 65 and older, older-population margin of error, and older-adult share

The build uses the Census table-based Summary File because the 2026 Census API requires an API key. The release remains rebuildable without a private key.

### Dataset C: Census TIGERweb generalized North Carolina county boundaries

- Service: Generalized ACS 2024 State and County map service
- Layer: Counties 5M
- Vintage: January 1, 2024
- State filter: North Carolina, FIPS 37
- Expected features: 100
- Teaching purpose: render the deliberately flawed raw-count choropleth and its repair without adding a geospatial software dependency

The build flattens the public GeoJSON polygons into a CSV of longitude, latitude, county FIPS, polygon group, and point order. It does not alter boundaries.

### Dataset D: joined North Carolina teaching table

The joined table has one row per North Carolina county. It keeps the PLACES crude and age-adjusted estimates, both intervals, the matching PLACES adult population, a derived modeled adult count, ACS adult and older-population context, and source dates.

### Provenance boundary

`modeled_adult_count` is derived as crude prevalence multiplied by the PLACES adult population. It is not an observed count. The ACS population is context and a cross-source denominator check. It is not substituted into the PLACES estimate.

### Rights and privacy

All released files are aggregate public government data. They contain no patient record, protected health information, exact address, respondent record, or small cell from a clinical system.

## 9. Data dictionary and expected analytic structure

### Joined teaching table

| Field | Type | Meaning |
|---|---|---|
| `county_fips` | character | Five-character county FIPS with leading zeros preserved. |
| `state_abbr` | character | `NC`. |
| `state_name` | character | `North Carolina`. |
| `county_name` | character | County name from PLACES. |
| `measure_id` | character | `DIABETES`. |
| `measure_name` | character | Diagnosed diabetes among adults. |
| `measure_year` | integer | BRFSS measure year reported by PLACES. |
| `release_label` | character | PLACES 2024 release. |
| `places_total_population` | integer | Census 2022 total population carried by PLACES. |
| `places_adult_population` | integer | Census 2022 adult population carried by PLACES and used for the modeled-count derivation. |
| `crude_prevalence_pct` | numeric | Modeled crude adult prevalence percentage. |
| `crude_low_95_pct` | numeric | Lower source confidence limit. |
| `crude_high_95_pct` | numeric | Upper source confidence limit. |
| `age_adjusted_prevalence_pct` | numeric | Modeled age-adjusted adult prevalence percentage. |
| `age_adjusted_low_95_pct` | numeric | Lower source confidence limit. |
| `age_adjusted_high_95_pct` | numeric | Upper source confidence limit. |
| `modeled_adult_count` | integer | Rounded crude prevalence times the matching PLACES adult population. |
| `count_status` | character | States that the count is modeled, not observed. |
| `acs_adult_population` | integer | Derived 2020-2024 ACS population age 18 and older. |
| `acs_adult_moe90` | numeric | Approximate 90% margin of error for the derived ACS adult population sum. |
| `acs_65plus_population` | integer | Derived 2020-2024 ACS population age 65 and older. |
| `acs_65plus_moe90` | numeric | Approximate 90% margin of error for the derived older-population sum. |
| `acs_65plus_share_adult_pct` | numeric | Older population divided by adult population. |
| `acs_moe_status` | character | Reports whether all component margins were available for the derived sums. |
| `adult_population_difference_pct` | numeric | Percent difference between ACS adult context and PLACES adult population. |
| `teaching_low_denominator_flag` | integer | One when the PLACES adult population is below the declared teaching threshold. |
| `source_footnote` | character | Preserved source footnote text, blank when none. |

### Source extracts

`places_diabetes_county_2024.csv` remains long: one row per geography and estimate type. `acs_adult_population_county_2024.csv` has one row per ACS county geography. `nc_county_boundaries_2024.csv` has multiple ordered coordinate rows per county and polygon part.

### Join rules

1. Preserve county FIPS as text.
2. Restrict the analytic teaching case to state FIPS `37`.
3. Require exactly one crude and one age-adjusted PLACES row per North Carolina county.
4. Require exactly one ACS county row for every North Carolina PLACES county.
5. Do not join on county name.
6. Do not replace PLACES adult population with ACS adult population.
7. Keep different source periods visible.

### Suppression rule

The source does not suppress the released North Carolina diabetes estimates. To teach publication policy honestly, the module declares a training rule rather than rewriting the source:

```text
teaching_low_denominator_flag = 1 when PLACES adult population < 10,000
```

Learners may display the estimate in the audit table but must not use a flagged county as a decisive rank without a visible warning and local validation. Module 06 later evaluates stability formally.

## 10. Worked example and instructor walkthrough

The instructor walkthrough uses three counties selected from the released file:

1. a populous county with a large modeled adult count;
2. a county with high crude prevalence and an older adult population; and
3. a county whose age-adjusted rank differs materially from its count or crude rank.

### Walkthrough sequence

1. Read the source record before reading the values.
2. Write the estimand in one sentence.
3. Calculate the modeled adult count from crude prevalence and the PLACES adult population.
4. Show that the largest count need not have the highest prevalence.
5. Compare crude and age-adjusted prevalence.
6. Inspect the older-adult share from ACS as context, without claiming it fully explains the adjustment.
7. Keep both source periods visible.
8. Choose age-adjusted prevalence for the comparative shortlist.
9. Keep modeled count and adult population in the companion table for outreach scale.
10. State what local data the director must obtain before final selection.

### Required language

Acceptable:

> The 2024 PLACES release estimates adult diabetes prevalence from 2022 source data. For cross-county comparison, the age-adjusted estimate reduces differences due to age structure. The modeled count is useful only as approximate planning scale because it is derived from modeled crude prevalence, not observed diagnoses.

Not acceptable:

> These counties have the most diabetes cases and therefore need the intervention most.

### Instructor stop points

- Stop when a learner multiplies age-adjusted prevalence by population.
- Stop when a learner calls a modeled count observed.
- Stop when a learner combines ACS and PLACES periods without labeling them.
- Stop when a learner claims an individual resident has a county-level characteristic.
- Stop when a learner treats a rank as a funding formula.

## 11. Guided practice

### Tier 1: Run

Learners execute `lab.R` and inspect:

1. modeled adult counts by county;
2. crude prevalence for the same county set;
3. a denominator-aware age-adjusted comparison with source intervals;
4. counties with the largest count-to-adjusted and crude-to-adjusted rank changes; and
5. an exact decision table.

Required questions:

1. Which counties appear important only because they are populous?
2. Which counties rise when the display changes from count to crude prevalence?
3. Which counties change after age adjustment?
4. Which quantity belongs in the partnership shortlist and which belongs in capacity planning?
5. Which low-denominator counties require a warning?
6. What does the source interval add even before Module 06 teaches formal comparison?

### Tier 2: Modify

Learners must make three changes:

- change the displayed county subset while preserving a reproducible rule;
- add a direct adult-population or modeled-count label to the companion view; and
- write a subtitle that names the measure year, release, and adjustment status.

They must also produce one failed version that omits a denominator and explain why it fails.

### Tier 3: Author

Learners build an independent comparison from `nc_diabetes_rates_2024.csv`. The work must still pass the source, denominator, accessibility, and claim rules.

### Guided-practice exit condition

The learner can explain, without code, why count, crude prevalence, and age-adjusted prevalence can produce three different county orders.

## 12. Independent exercise

### Prompt

> The North Carolina population-health program can invite up to 12 counties into a first adult diabetes-prevention partnership. Create one decision figure and a short audit that distinguishes comparative prevalence from outreach scale. Recommend a transparent first-pass shortlist and identify the local information required before invitations are final.

### Required analysis

The learner must:

1. define the decision and the eligible adult population;
2. calculate or verify modeled adult count from the crude estimate and matching denominator;
3. compare count, crude, and age-adjusted ranks;
4. declare a reproducible shortlist rule;
5. keep adult population, source interval, period, adjustment status, and low-denominator flag available;
6. identify at least two counties whose interpretation changes across quantities;
7. separate a comparison recommendation from a service-volume observation;
8. state the ecological limit; and
9. name at least three local facts needed before action.

### Acceptable shortlist rules

- highest age-adjusted prevalence followed by local readiness review;
- highest age-adjusted prevalence within declared regions, with adult population used only for capacity planning;
- a transparent two-stage rule using adjusted prevalence first and local feasibility second; or
- another rule whose numerator, denominator, purpose, and tradeoff are explicit.

### Unacceptable shortlist rules

- highest modeled count presented as highest risk;
- highest crude prevalence without acknowledging age structure;
- multiplying age-adjusted prevalence by population;
- averaging count and prevalence ranks into an invented score;
- excluding small counties without stating a rule; or
- treating the PLACES estimate as observed county diagnoses.

## 13. Visualization and communication requirements

### Required assessed figure

`figure.png` must support the comparative partnership decision. It must:

- use age-adjusted prevalence as the primary comparison unless the learner defends another comparable quantity;
- identify the displayed counties and selection rule;
- show or provide source confidence limits;
- keep the adult denominator or modeled count available through a companion panel, label, or exact table;
- identify low-denominator warnings;
- state `2022 measure data, PLACES 2024 release`;
- avoid a red-green-only distinction;
- use direct labels or a readable lookup path;
- avoid area as the only encoding of close prevalence values; and
- include a finding title rather than only a topic label.

### Count display rule

A count display may appear as context, but its title or annotation must say `modeled adult count` and `not observed cases`. Raw or modeled counts may not be mapped as if color represented prevalence.

### Map rule

The critique set includes a raw-count choropleth because it is a common failure. The repaired learner decision figure does not have to be a map. Module 10 later decides when geography itself is necessary.

### Companion table minimum

The audit or companion table must include:

- county name and FIPS;
- crude prevalence;
- age-adjusted prevalence;
- source interval;
- PLACES adult population;
- modeled adult count;
- adjustment status;
- measure year and release; and
- warning flag or footnote.

### Accessibility

Every figure requires alt text. Color must be redundant with position, label, shape, line type, or pattern. The exact values must be available in `rate-audit.md` or a generated CSV.

## 14. Exact submission package and filenames

Submit exactly this package:

```text
module-05/
  rate-audit.md
  analysis.R
  figure.png
  source-record.yml
  alt-text.md
  decision-note.md
```

### `rate-audit.md`

Required headings:

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

The file must contain an exact table for the recommended counties and any county used as a counterexample.

### `analysis.R`

The script must:

- read the released CSV from a relative path;
- preserve FIPS as text;
- reproduce the shortlist and `figure.png`;
- calculate modeled count only from crude prevalence and PLACES adult population;
- fail clearly when required fields are absent;
- avoid absolute local paths; and
- print the decision table used in the audit.

### `figure.png`

The figure must be readable at 1,600 by 1,000 pixels or an equivalent aspect and resolution. The file must not require hover interaction to understand the conclusion.

### `source-record.yml`

Required keys:

- source titles and publishers;
- full visible landing, metadata, query, and file URLs;
- dataset, table, measure, geography, and release identifiers;
- retrieval date;
- raw and released file hashes;
- row counts;
- transformations;
- rights;
- derived-field formulas; and
- limits.

### `alt-text.md`

Write 80 to 180 words. Name the chart form, finding, highest and lowest displayed values, denominator context, interval treatment, and low-denominator warnings. Do not list every pixel or color.

### `decision-note.md`

Write 250 to 450 words for the population-health program director. Include:

- recommendation;
- why the chosen quantity matches the decision;
- how count changes capacity planning but not comparative prevalence;
- two counties whose interpretation changes;
- local evidence needed before action; and
- a concise statement of what the data cannot establish.

## 15. Rubric and pass conditions

The module is scored out of 100 points.

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Decision and estimand | 15 | The owner, decision, adult population, geography, measure, period, and purpose are explicit. |
| Denominator reasoning | 20 | Counts, crude prevalence, adjusted prevalence, and their denominators are correctly distinguished. |
| Source and provenance | 15 | The CDC, ACS, and TIGERweb sources, identifiers, periods, rights, transformations, and hashes are complete. |
| Analysis and reproducibility | 15 | The code reproduces the table, shortlist, and figure from the released data. |
| Visualization judgment | 15 | The display supports comparison, preserves context, and avoids the raw-count and adjustment traps. |
| Decision interpretation | 10 | The recommendation separates comparative need from service scale and asks for local validation. |
| Accessibility and exact values | 5 | Alt text, redundant encoding, readable labels, and an exact table are present. |
| Responsible claims and AI disclosure | 5 | Model, ecological, and automation boundaries are accurate and assistance is disclosed. |

### Pass standard

Passing requires at least 75 points and all of these mandatory conditions:

1. no age-adjusted estimate is converted into a count;
2. no modeled count is called observed;
3. the adult denominator and source period are visible;
4. the shortlist rule is reproducible;
5. the figure and exact table are both present;
6. the source record includes full URLs and hashes; and
7. the ecological limit is stated.

A mandatory-condition failure requires revision even when the numeric score is 75 or higher.

## 16. Common errors, failure modes, and interventions

| Failure | Why it matters | Instructor intervention |
|---|---|---|
| Ranking modeled counts | Large counties dominate even when prevalence is lower. | Ask what decision population size answers. |
| Dividing by total population | PLACES diabetes describes adults age 18 and older. | Require the learner to write the eligible population beside the formula. |
| Multiplying adjusted prevalence by population | The standardized estimate does not describe the county's current age mix. | Recalculate with crude prevalence and label the result modeled. |
| Calling prevalence incidence | Prevalence is not a rate of new diagnoses. | Return to the source measure definition. |
| Treating ACS as the PLACES denominator | The sources have different periods and roles. | Keep both fields and label the population actually used. |
| Omitting confidence limits | A precise-looking point invites false certainty. | Require intervals in the table even before Module 06. |
| Hiding small denominators | A rank can look decisive when the population is small. | Apply and explain the training warning rule. |
| Reading a county result as an individual trait | Aggregate data do not establish individual status. | Add an ecological-limit sentence. |
| Creating a composite priority score | Arbitrary weights hide value judgments. | Separate comparison, scale, readiness, and feasibility. |
| Mapping raw counts | Color becomes a population map. | Repair with a comparable rate and an exact companion table. |

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

- Use high-contrast text and marks.
- Do not rely on red and green.
- Use aligned position for close prevalence comparisons.
- Provide exact values and alt text.
- Keep county labels readable without hover.
- State the adjustment status in text, not color alone.

### Equity

County rankings can stigmatize places and hide differences within counties. The module uses county names because a state program acts through county partnerships, but it requires respectful language and a local-validation step.

Learners must not describe counties or residents as unhealthy, noncompliant, irresponsible, costly, or deficient. Use phrases such as `higher modeled age-adjusted prevalence in this release`.

The decision note must ask about access, program readiness, community priorities, barriers, trusted partners, existing services, and within-county differences before action.

### Privacy

All data are aggregate and public. The module does not permit linkage to individual records or attempts to infer an individual's diagnosis.

### Responsible claim template

> In the 2024 PLACES release, County A has a higher modeled age-adjusted prevalence than County B. The estimate supports a comparative screening question for the state program. It does not identify individual residents, explain the difference, count observed diagnoses, or establish that one intervention will work.

## 18. AI and agent policy

AI may help with:

- generating candidate chart layouts;
- explaining a source field after the learner verifies it;
- checking code structure;
- drafting alt text from measured outputs;
- identifying places where denominator language is missing; and
- proposing questions for local validation.

AI may not:

- invent a denominator, source value, suppression rule, county fact, or local program condition;
- call a modeled estimate observed;
- select counties without a declared human-authored decision rule;
- infer individual disease status;
- convert adjusted prevalence into a local case count;
- claim causation from county comparisons; or
- replace source verification.

The learner must disclose the tool, version when known, tasks assisted, prompts or summary of prompts, changes made after checking, and facts verified against the source.

The final recommendation remains the learner's responsibility.

## 19. Answer key and instructor notes

### Core answer

The county with the largest modeled adult count is not automatically the county with the highest adult diabetes prevalence. Modeled count answers a scale question and is driven strongly by adult population. Crude prevalence describes the modeled share of the county's current adult population. Age-adjusted prevalence supports a more comparable county ranking by standardizing age structure.

### Expected decision form

The strongest response uses age-adjusted prevalence for the initial comparative shortlist, keeps modeled count and adult population in a companion table for outreach scale, flags low denominators, and makes the shortlist conditional on local readiness and community evidence.

### Minimum acceptable denominator statement

> The prevalence denominator is the adult population age 18 and older. The modeled count is derived from the crude PLACES estimate and the matching Census 2022 adult population carried by that release. The 2020-2024 ACS adult population is separate context and is not substituted into the calculation.

### Minimum acceptable adjustment statement

> Crude prevalence describes the modeled county adult population as it is. Age-adjusted prevalence standardizes age structure for comparison. The adjusted estimate is not the county's expected count.

### Minimum acceptable ecological statement

> A county estimate describes an area, not every resident. It cannot identify an individual's diagnosis or explain why the county estimate is higher.

### Instructor review prompts

- Which quantity matches the decision?
- Which denominator is eligible?
- Are source periods mixed?
- Is a modeled value labeled as modeled?
- Does the display expose or hide population scale?
- Does the shortlist rule encode an unstated value judgment?
- What local evidence could reverse the recommendation?

### Handoff to Module 06

The learner keeps the PLACES confidence limits and low-denominator flags but does not decide which county differences are distinguishable. Module 06 owns that question.

## 20. Runnable acceptance checks

The released module must provide one command path that rebuilds the data and one that validates the committed release.

### Source build checks

1. The CDC query returns 6,290 `DIABETES` rows: crude and age-adjusted rows for 3,144 counties plus the source national summary row.
2. Every retained source row keeps the measure year, geography, value type, estimate, limits, population, and footnote fields.
3. The ACS source file hash and byte count match the pinned 2024 table file.
4. The ACS county extract contains every `0500000US` row and preserves county FIPS as text.
5. Adult and age-65-plus estimates use the declared B01001 cells.
6. Derived margins of error use the documented root-sum-of-squares rule for sums.
7. The TIGERweb extract contains exactly 100 North Carolina county features.
8. Every North Carolina feature flattens into at least one closed polygon part.

### Joined-data checks

9. The teaching table contains exactly 100 rows and 100 unique county FIPS values.
10. Every row has one crude and one age-adjusted prevalence estimate.
11. Confidence limits contain their point estimates.
12. `modeled_adult_count` equals rounded crude prevalence times PLACES adult population.
13. ACS and PLACES adult populations remain separate.
14. At least one county triggers the declared low-denominator warning.
15. At least one county changes rank materially between count and adjusted prevalence.
16. The boundary file covers the same 100 county FIPS values.

### Lab and critique checks

17. The lab produces four PNG files and one exact decision CSV.
18. The critique script produces a raw modeled-count choropleth and a rate display that hides denominator and interval.
19. Every repaired reference chart uses readable labels and non-color cues where needed.
20. All figures render without absolute paths or private data.

### Curriculum checks

21. The specification has all 21 numbered contract sections.
22. The course specification points to the exact learner package and runnable module directory.
23. The root catalog, course page, module page, atlas, source register, and build ledger carry the current release.
24. `release.json` parses and records technical validation plus pending human reviews.
25. `git diff --check` passes before commit.

The validator must exit nonzero on any failed structural or data check.

## 21. Release status, reviewers, version, and known issues

### Version plan

| Artifact | Version |
|---|---|
| Module specification | 0.1.0 |
| Runnable module | 0.1.0 |
| CDC source extract | 0.1.0 |
| ACS county extract | 0.1.0 |
| North Carolina teaching table | 0.1.0 |
| Boundary extract | 0.1.0 |
| Commons release | 0.16.0 |

### Technical release criteria

- source build completes from a clean directory with public network access;
- committed hashes match regenerated files;
- validation checks pass;
- all lab and critique outputs render;
- the exact assessment and answer key agree;
- current integration pages identify Module 05 as complete; and
- the next ledger unit is Module 06.

### Required human reviews

| Review | Required reviewer | Status at technical release |
|---|---|---|
| Visualization and source fidelity | Data-visualization faculty member | Pending |
| Population-health content | Population-health clinician or practitioner | Pending |
| Accessibility | Accessibility reviewer | Pending |
| Independent teachability | Instructor who did not build the module | Pending |

### Known issues allowed at technical release

- The CDC estimates are model-based, not direct county measurements.
- The PLACES release label, measure year, and source population year differ and must remain visible.
- The ACS context uses 2020-2024 survey estimates and does not replace the PLACES Census 2022 population.
- Derived ACS margins of error for sums are approximations from published component margins.
- The teaching suppression threshold is a declared course rule, not a CDC suppression rule.
- The generalized county boundaries support instruction but are not suitable for parcel, address, or operational routing decisions.
- Human content, accessibility, source-fidelity, and teachability reviews remain pending.

### Release decision

The technical release may be labeled `runnable-release-candidate` after every automated acceptance check passes. It may not be labeled reviewed, production-ready, or institutionally approved until the named human reviews are recorded.

### Handoff to Module 06

Module 06 begins with the interval columns and low-denominator counties preserved here. It asks how much confidence the director should place in apparent differences and which rankings overstate the available evidence.
