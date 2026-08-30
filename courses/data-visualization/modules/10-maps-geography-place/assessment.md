# Module 10 assessment

## Decision prompt

You are supporting a North Carolina population-health access planner. The planner can invite twelve counties into an initial listening and readiness process. The process may lead to regional technical assistance, but it does not allocate funding.

Use the released PLACES health estimate, current primary-care HPSA context, and generalized county boundaries to decide whether a map adds useful information. Submit a rate map, a four-class screen map, an ordered non-map comparison, an exact table, and a short decision note.

## Decision boundary

Your work may recommend where to begin conversations. It may not:

- declare a county high risk, critical, deficient, bad, or a problem;
- treat a modeled estimate as an observed diagnosis count;
- treat the highest HPSA component score as a county workforce rate;
- treat score 20 as an official threshold;
- infer that 2026 HPSA status caused a 2022 health estimate;
- allocate funds from the screen alone;
- claim that the map tests clustering or causation; or
- speak for residents or local organizations that are not in the data.

## Source package

Use these files:

```text
data/nc_place_access_2026.csv
data/nc_county_boundaries_2024.csv
data/hpsa_primary_care_nc_2026_08_29.csv
```

The first two are required for every submission. Use the selected HPSA source release to verify designation scope, status, and the county maximum when needed.

## Part 1: source and geography audit

Before making a figure, verify and record:

1. the county grain of the teaching table;
2. the HPSA component grain;
3. the boundary-point grain;
4. five-character FIPS formatting;
5. the 100-county join;
6. the 7,121 boundary-point count;
7. the 104 polygon-part count;
8. the PLACES measure ID and year;
9. the HRSA snapshot date;
10. current status selection;
11. the map projection; and
12. the difference between a county boundary, service area, and travel-time area.

Place the result in `place-brief.md`.

## Part 2: health rate map

Create `health-map.png`.

Requirements:

- map `age_adjusted_fair_poor_health_pct`;
- do not map `adult_population` as health need;
- use all 100 counties;
- use the generalized boundaries and an explicitly named projection;
- use a continuous scale or defend every class boundary;
- name the measure, population, estimate type, year, and unit;
- state that PLACES values are model-based;
- keep county boundaries visible without dominating the fill;
- include an accessible legend; and
- state what the map adds to the decision.

The reference implementation uses an Albers equal-area teaching projection and a continuous 12% to 28% scale.

## Part 3: four-class screen map

Create `bivariate-map.png`.

Use the exact conditions:

1. health point estimate above the 17.0% national point estimate; and
2. highest active primary-care HPSA component score touching the county of at least 20.

Show these four classes:

- neither condition;
- health condition only;
- HPSA condition only; and
- both conditions.

Requirements:

- state both rules in the subtitle, legend, caption, or nearby text;
- state that score 20 is a teaching rule;
- avoid a red-green-only palette;
- retain a non-color reading path in the table and text alternative;
- do not call the classes risk, need, priority, criticality, or performance levels; and
- report the number of counties in each class.

## Part 4: non-map comparison

Create `non-map.png`.

Requirements:

- include all 100 counties or provide a linked all-county table;
- use one shared quantitative scale;
- order by the health point estimate with a documented tie rule;
- show the source interval;
- show the 17.0% national point reference;
- mark the HPSA screen with shape, fill, direct text, or another redundant cue;
- label the HPSA value as a component-score maximum, not a workforce rate;
- preserve the 2022 and 2026 date distinction; and
- make the county order reproducible.

## Part 5: exact decision table

Create `decision-table.csv` with exactly 100 rows.

Required columns:

```text
county_fips
county_name
health_measure_year
adult_population
age_adjusted_fair_poor_health_pct
age_adjusted_low_ci_pct
age_adjusted_high_ci_pct
national_age_adjusted_pct
health_rank_descending
active_hpsa_designations
max_active_hpsa_score
whole_county_geographic_hpsa
bivariate_screen_class
reference_review_eligible
reference_review_order
reference_shortlist
time_alignment_status
interpretation_boundary
```

File rules:

- preserve leading zeros in FIPS;
- keep one row per county;
- keep blank maximum scores blank;
- use the exact four class labels;
- keep all 19 eligible counties, not only the first twelve;
- give eligible counties review orders 1 through 19; and
- mark exactly twelve reference rows.

## Part 6: map versus non-map judgment

In `place-brief.md`, answer:

1. What decision question does the map answer better?
2. What decision question does the ordered comparison answer better?
3. Does either view work alone?
4. If a coordinated pair is justified, what role does each view have?
5. What would be lost if the map were removed?
6. What would be lost if the non-map view were removed?
7. What spatial statement is descriptive rather than tested?
8. What new evidence would be needed for travel or service-access planning?

The answer must be about the planner's task, not a generic claim that maps are engaging.

## Part 7: critique and repair

Run or inspect the three critique figures.

### C1: raw-count need map

Explain:

- why adult population is not a health rate;
- why large counties dominate;
- when population count would be relevant;
- which rate or count belongs in each decision; and
- how the title makes an unsupported claim.

### C2: arbitrary bins

Explain:

- how the breaks change apparent pattern;
- why official-sounding labels imply unsupported thresholds;
- whether a continuous scale, quantile, equal-width class, or policy threshold fits the task;
- how ties at a boundary should be handled; and
- how exact values remain available.

### C3: stigmatizing place labels

Explain:

- why a screening result is not a county identity;
- how the language shifts attention from systems and resources to residents;
- what source and local context are missing;
- how you would rewrite the title, legend, and decision note; and
- whose voice is required before action.

Record the critique in `place-brief.md` under `## Critique and repair`.

## Part 8: text alternative

Create `alt-text.md` with this exact structure:

```markdown
# Text alternative

## Short alternative

## Long description

### Decision and map structure

### Health map

### Four-class screen

### Ordered comparison

### Reference twelve

### Uncertainty, dates, and denominator

### Geography and equity boundary

### Exact-value table
```

The long description must include:

- the 12.1% to 27.2% health range;
- the 17.0% national point;
- 73 counties above that point;
- 23 counties meeting the HPSA screen;
- 19 counties meeting both conditions;
- the twelve county names in order;
- why the map and non-map differ; and
- the link or filename for the exact table.

Do not describe only color position.

## Part 9: decision note

Create `decision-note.md` with this exact structure:

```markdown
# Decision note

## Decision owner and question

## Why place matters

## Screen and review order

## Reference twelve

## Recommended action now

## What the map adds

## What the non-map adds

## Equity and community engagement

## Uncertainty, dates, and limits

## Evidence needed before allocation
```

The recommended action should be a listening, verification, or readiness step. It should not be a funding award.

## Part 10: source record

Create `source-record.yml` containing:

- CDC, HRSA, and Census publisher names;
- complete URLs;
- dataset, measure, service, and release identifiers;
- retrieval or source dates;
- all three committed checksums;
- the 2022 health and 2026 HPSA date distinction;
- FIPS join logic;
- current HPSA status selection;
- HPSA maximum and score-20 rule;
- boundary coordinate system and teaching projection;
- rights and reuse status;
- missingness and completeness; and
- known interpretation limits.

## Part 11: AI-use record

Create `ai-use.md` with:

```markdown
# AI-use record

## Tool and model

## Work delegated

## Prompts or instructions

## Outputs retained or rejected

## Source and rights verification

## Join, score, and shortlist verification

## Projection and accessibility verification

## Human decisions
```

If no AI was used, state that under `## Tool and model` and complete the human verification sections.

AI may suggest code or wording. It may not certify source rights, select an allocation rule, label communities, or replace the learner's map-versus-non-map judgment.

## Exact submission

```text
module-10/
  place-brief.md
  analysis.R
  health-map.png
  bivariate-map.png
  non-map.png
  decision-table.csv
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

Do not submit a dashboard workbook, proprietary packaged file, or screenshot without editable source code.

## File-quality rules

- `analysis.R` runs from a clean R session using relative paths or declared command-line arguments.
- Every output is created by the submitted source.
- No menu-only transformation is accepted.
- No source row is silently removed.
- The exact table opens as a valid CSV.
- Figure text is readable at the submitted size.
- Color is not the only way to recover the decision classes.
- Full raw URLs appear in the source record.
- AI use or non-use is declared.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Decision and place rationale | 10 | The owner, action, geographic question, and reason place matters are explicit. |
| Source, grain, rights, and time | 12 | CDC, HRSA, Census, FIPS, grain, dates, rights, hashes, and the AHRF rights decision are accurate. |
| Join and reproducibility | 8 | The 100-county join, row counts, fields, build, and exact output are reproducible. |
| Health map | 12 | Maps the age-adjusted percentage with projection, unit, year, model boundary, and defensible scale. |
| Four-class screen map | 12 | Uses the exact two conditions, four classes, accessible cues, counts, and teaching-rule disclosure. |
| Non-map comparison | 12 | Preserves common scale, order, intervals, national reference, HPSA cue, and all counties or linked exact table. |
| Map-versus-non-map judgment | 10 | Assigns each view a concrete decision role and identifies what each cannot answer. |
| Decision table and shortlist | 8 | Contains all 100 rows, 19 eligible rows, exact order, twelve reference rows, and required boundary fields. |
| Accessibility and text alternative | 8 | Provides readable figures, redundant meaning, exact values, and an equivalent long description. |
| Equity, language, and claim discipline | 5 | Avoids stigma, identifies within-county limits, and requires local voice before action. |
| AI-use record | 3 | Declares use or non-use and names human verification. |
| Total | 100 |  |

## Score interpretation

| Score | Result |
|---:|---|
| 90-100 | Pass with strong decision readiness. |
| 80-89 | Pass if all noncompensable conditions are met. |
| 70-79 | Revise and resubmit. |
| Below 70 | Does not pass. |

## Noncompensable pass conditions

A submission does not pass when any of these is true:

1. raw population is presented as a health rate or need measure;
2. the county join is incomplete or changes FIPS values;
3. HPSA score is called a county workforce rate;
4. score 20 is presented as an official threshold;
5. the 2022 and 2026 source dates are hidden;
6. a class rule or bin boundary is undisclosed;
7. the map is used without a defensible place-based decision role;
8. uncertainty and exact values are unavailable;
9. color is the only reading path;
10. the screen is used to allocate resources without local evidence;
11. stigmatizing place language remains in the final products;
12. source rights or URLs are missing;
13. AI-generated claims or code are accepted without human verification; or
14. the exact submission contract is incomplete.
