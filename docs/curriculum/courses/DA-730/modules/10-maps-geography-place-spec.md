# DA-730 Module 10: Maps, geography, and place

- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module: 10 of 13
- Learner time: 8.5 hours
- Module version: 0.1.0
- Commons release: 0.21.0
- Status: runnable release candidate
- Primary audience: graduate health-data learners
- Decision owner: North Carolina population-health access planner
- Public-source case: CDC PLACES, HRSA primary-care HPSAs, and Census generalized county boundaries
- Last updated: 2026-08-30

## 1. Module identity and place in the course

Module 10 asks whether geography changes a decision.

Learners already know how to:

- encode data with marks and channels;
- judge perceptual accuracy;
- select a chart or table;
- reveal distributions;
- distinguish counts, rates, and adjustment;
- retain uncertainty and small-number context;
- make color use accessible;
- interpret time and process variation; and
- compare many groups with shared scales, order, and references.

Module 10 carries those rules into a county map.

The module is not a software tour and is not satisfied when a learner can fill polygons. It teaches a decision sequence:

1. name the place-based action;
2. define the measure and geographic unit;
3. verify the join and boundary source;
4. choose a projection and scale;
5. map the rate or estimate that matches the question;
6. build a non-map comparison for the same decision;
7. decide what each view adds;
8. identify what county geography conceals; and
9. require local evidence before action.

Module 05 owns the underlying rate, denominator, adjustment, and boundary foundations. Module 09 owns multi-group comparison. Module 10 owns the judgment that place may add context but does not add evidence by itself.

The module hands off to Module 11. When location is not the central structure, learners next decide whether flow, network, hierarchy, or composition better expresses the problem.

## 2. Healthcare decision and audience

### Decision

A North Carolina population-health access planner can invite twelve counties into an initial listening and readiness process.

The process asks:

- whether residents and local organizations identify the same concern;
- whether current primary-care access conditions support further review;
- whether neighboring counties could benefit from a regional conversation;
- what local assets and programs already exist;
- what transportation, language, cost, hours, or digital-access barriers matter;
- what evidence is still missing; and
- whether later technical assistance is appropriate.

The process does not allocate funding.

### Decision owner

The primary owner is a state or regional population-health access planner who must make the first screen explainable and reversible.

The planner needs:

- a stable county join;
- a source-defined health estimate;
- current shortage-designation context;
- spatial pattern for regional coordination;
- exact comparative evidence;
- an uncertainty path;
- a population denominator;
- source dates and rights;
- language that does not stigmatize residents; and
- a clear boundary between screening and allocation.

### Secondary audiences

Secondary audiences include:

- local public-health directors;
- primary-care and community-health-center partners;
- community-based organizations;
- rural-health partners;
- health-equity leaders;
- state data and geography staff;
- accessibility users who need the same evidence through text and tables; and
- instructors evaluating whether the package can be taught independently.

### Decision questions

The module requires learners to answer:

1. Where do higher modeled fair or poor adult health estimates appear?
2. Which counties have a highest active primary-care HPSA component score of at least 20?
3. Which counties meet both declared conditions?
4. Are those counties geographically near one another?
5. Does the map reveal a regional conversation opportunity?
6. Which exact counties and intervals support the screen?
7. What changes when the same evidence is ordered outside the map?
8. Which counties appear visually prominent because of area rather than value?
9. What is concealed by county aggregation?
10. What local evidence is required before allocation?

### Required decision language

Acceptable action language uses verbs such as:

- invite;
- verify;
- listen;
- review;
- compare;
- convene;
- investigate;
- ask;
- coordinate; and
- assess readiness.

The final decision may not automatically fund, penalize, rank community worth, or describe counties as problems.

## 3. Foundation skill revisited or extended

### Foundations I skills revisited

Learners revisit:

- file paths and reproducible scripts;
- CSV parsing;
- character identifiers with leading zeros;
- one-to-many and many-to-one joins;
- row and column checks;
- data types;
- missing-value preservation;
- deterministic sorting;
- source checksums; and
- exact output filenames.

The central technical risk is the join. A county FIPS is a character identifier, not a number. Removing a leading zero or joining on county name can silently create incorrect geography.

### Foundations II skills revisited

Learners revisit:

- population and unit definitions;
- rates and percentages;
- age adjustment;
- source intervals;
- ranks and tie rules;
- selection rules;
- reproducible derivation;
- temporal mismatch;
- measurement limits; and
- clear separation between data and decision assumptions.

### Visualization foundations revisited

Learners reuse:

- a named decision owner;
- a visible comparison reference;
- shared quantitative scales;
- accessible color and redundant cues;
- exact-value tables;
- text alternatives;
- uncertainty language;
- direct source and date labels;
- critique and repair; and
- claim discipline.

### New application

Module 10 adds:

- choropleth maps;
- bivariate place screens;
- projection choice;
- classification choice;
- generalized boundaries;
- spatial units;
- the modifiable areal unit problem;
- county area as a visual-weight problem;
- rurality and access context;
- map-versus-non-map judgment;
- place-based language; and
- the distinction among administrative boundary, service area, and travel-time geography.

## 4. Assessable learning outcomes

By the end of Module 10, the learner can:

1. name a healthcare decision for which place materially affects action;
2. reject a map when geography does not add decision value;
3. distinguish a count, percentage, adjusted estimate, designation, component score, and boundary;
4. state the grain of all three released tables;
5. preserve five-character county FIPS;
6. verify a 100-county data-to-boundary join;
7. explain why a county boundary differs from a care network or travel area;
8. map an age-adjusted health estimate rather than raw population;
9. name the map projection and its purpose;
10. use a continuous scale when no threshold exists;
11. declare every class rule when classification is used;
12. explain how arbitrary bins change apparent pattern;
13. build the exact four-class screen;
14. report the number of counties in every class;
15. build an ordered non-map comparison with intervals and a national reference;
16. mark the HPSA screen with a redundant cue;
17. explain what the map answers better;
18. explain what the non-map answers better;
19. identify when a coordinated pair is justified;
20. retain adult population without treating it as a health rate;
21. distinguish a county maximum HPSA component score from a county workforce rate;
22. distinguish current, proposed-withdrawal, and withdrawn records;
23. state the 2022 health and 2026 HPSA time mismatch;
24. describe visible spatial pattern without claiming a statistical cluster;
25. identify the modifiable areal unit problem;
26. identify within-county evidence missing from the case;
27. replace stigmatizing labels with source-defined language;
28. produce a 100-row exact table;
29. produce an equivalent text alternative;
30. document AI use or non-use; and
31. recommend a reversible readiness action rather than automatic allocation.

### Mastery threshold

A learner passes with at least 80 of 100 points and every noncompensable condition satisfied.

## 5. Concept ownership and boundaries

### Concepts owned by Module 10

Module 10 owns:

- map-purpose judgment;
- rate-versus-count mapping;
- county FIPS join integrity;
- choropleth projection disclosure;
- classification disclosure;
- bivariate place-screen construction;
- map-versus-non-map comparison;
- county area as visual prominence;
- generalized-boundary limits;
- administrative boundary versus service geography;
- the modifiable areal unit problem at an applied level;
- spatial-description claim limits;
- place-based language; and
- county-screen versus resource-allocation boundaries.

### Concepts introduced but not mastered here

The module introduces but does not fully teach:

- spatial autocorrelation;
- local and global cluster statistics;
- spatial regression;
- adjacency matrices;
- point-in-polygon methods;
- geocoding;
- raster analysis;
- routing;
- drive-time and transit-time analysis;
- network service areas;
- geographic privacy;
- ecological inference; and
- formal sensitivity analysis across geographic units.

Learners may name these as next steps. They may not claim to have performed them.

### Concepts owned elsewhere

- Module 01 owns marks and channels.
- Module 02 owns perceptual accuracy.
- Module 03 owns chart selection.
- Module 04 owns distributions.
- Module 05 owns rates, denominators, adjustment, and the first boundary release.
- Module 06 owns uncertainty and small-number limits.
- Module 07 owns the standing accessibility contract.
- Module 08 owns time and process variation.
- Module 09 owns shared-scale group comparison.
- Module 11 owns flow, networks, composition, and hierarchy.
- Module 12 owns dashboards and coordinated multi-view monitoring.
- Module 13 owns final audience, annotation, narrative, and capstone integration.

### Prohibited shortcuts

Learners may not:

- join counties by display name without verifying FIPS;
- convert FIPS to an integer;
- map adult population and call it health need;
- hide the estimate type or year;
- use default map bins without recording them;
- use official-sounding category labels without a source;
- imply that polygon area represents population;
- imply that a county color applies equally to every resident;
- sum HPSA scores;
- call the maximum component score a workforce rate;
- convert every component designation into a whole-county claim;
- hide proposed-withdrawal or withdrawn statuses;
- call visible pattern a statistical cluster;
- use color as the only class cue across the package;
- remove the exact table;
- use stigmatizing place language; or
- allocate resources from the screen alone.

## 6. Lesson sequence and learner time

Total expected learner time is 8.5 hours.

| Segment | Time | Learner work | Required evidence |
|---|---:|---|---|
| Decision and rights opening | 0.35 | Name the decision, place question, and why AHRF was not redistributed. | Source and decision notes. |
| Grain and join audit | 0.50 | Inspect county, HPSA component, and polygon-point grains; verify FIPS. | Join audit. |
| Rate-versus-count critique | 0.50 | Diagnose the raw-count map. | Critique notes. |
| Projection and continuous map | 0.75 | Transform coordinates and build the health choropleth. | `health-map.png`. |
| Classification and bivariate screen | 0.75 | Build and audit the exact four-class rule. | `bivariate-map.png`. |
| Ordered comparison | 0.75 | Build the all-county non-map view with intervals and reference. | `non-map.png`. |
| Geography and aggregation | 0.50 | Examine boundary, area, rurality, service geography, and MAUP. | Place brief. |
| Language and community voice | 0.50 | Repair stigmatizing place language. | Critique repair. |
| Independent build | 2.25 | Reproduce the outputs and exact table. | Source and files. |
| Decision and accessibility | 0.90 | Write the decision note, text alternative, and AI record. | Final package. |
| Submission verification | 0.75 | Run checks and verify exact filenames. | Complete folder. |
| Total | 8.50 hours |  |  |

### Before class

Learners read:

- the CDC PLACES methodology;
- the HRSA HPSA metadata definitions used in the case;
- the Census boundary-service description;
- the source record and rights decision;
- the Module 09 handoff; and
- the Module 10 data specification.

Learners answer:

1. What does each row represent?
2. Which fields are source values?
3. Which fields are teaching rules?
4. Which date belongs to each source?
5. Why is county FIPS stored as character?
6. Why is the HPSA score not a county rate?
7. Why was the direct HPSA source used instead of AHRF clinician fields?

### Synchronous opening

The instructor shows two unlabeled figures:

- a county map shaded by adult population; and
- an ordered dot plot of age-adjusted fair or poor health.

Learners identify which questions each can and cannot answer before titles and legends are revealed.

### End-of-module checkpoint

The learner can explain, without software:

- why the map is useful for regional coordination;
- why the ordered view is necessary for exact comparison;
- why a map does not create evidence;
- why the HPSA screen is not a county workforce rate; and
- why the final action remains a local review.

## 7. Authoritative readings and public clinical sources

### Required source reading

1. CDC PLACES county data 2024 release:
   https://data.cdc.gov/d/fu4u-a9bh
2. CDC PLACES methodology:
   https://www.cdc.gov/places/methodology/index.html
3. CDC health-status measure definitions:
   https://www.cdc.gov/places/measure-definitions/health-status.html
4. HRSA primary-care HPSA source:
   https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv
5. HRSA HPSA metadata:
   https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX
6. HRSA data usage page:
   https://data.hrsa.gov/data/download?data=HPSA
7. Census generalized state and county service:
   https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer
8. Exact Census county query:
   https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer/12/query?where=STATE%3D%2737%27&outFields=GEOID%2CNAME%2CSTATE%2CCOUNTY&returnGeometry=true&outSR=4326&f=geojson

### Standing visualization and accessibility sources

9. W3C Web Content Accessibility Guidelines 2.2:
   https://www.w3.org/TR/WCAG22/
10. W3C use-of-color guidance:
    https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
11. W3C complex-image guidance:
    https://www.w3.org/WAI/tutorials/images/complex/
12. CDC COVE Section 508 accessibility guidance:
    https://www.cdc.gov/cove/about/section-508-accessibility.html

### Rights-audit sources

13. AHRF current CSV archive inspected but not redistributed:
    https://data.hrsa.gov/DataDownload/AHRF/AHRF_2024-2025_CSV.zip
14. AHRF technical documentation archive inspected for reuse terms:
    https://data.hrsa.gov/DataDownload/AHRF/AHRF_USER_TECH_2024-2025.zip

### Reading prompts

Learners answer:

1. Which sources are directly redistributed?
2. Which source was inspected but rejected for redistribution?
3. Which source row describes a designation component?
4. Which source value is model-based?
5. Which boundary is generalized?
6. Which source date is most recent?
7. What does public access fail to establish by itself?
8. Which map choices belong to the analyst rather than the source?

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Dataset A: North Carolina health profiles

- Upstream package: Module 09
- File: `nc_county_health_profiles_2024.csv`
- Upstream rows: 500
- Upstream checksum: `33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9`
- Selected rows: 100
- Selected measure: `GHLTH`
- Measure year: 2022
- Teaching purpose: health-rate map and ordered comparison

The selected value is modeled age-adjusted prevalence of fair or poor self-rated health among adults. It is not an observed diagnosis count.

### Dataset B: primary-care HPSA source selection

- Full source rows: 79,358
- Full source bytes: 48,280,174
- Full source SHA-256: `4552ebf09bc5a40d79d71df8ea84aea165de2205953615e03571ad84f1d6b132`
- Selected rows: 1,546
- Selected columns: 28
- Selected checksum: `061fe5e18bc9cd58bd89256c686ddefbce6d77972c1139b1b339497f2eab5445`
- Selected geography: mappable North Carolina county FIPS
- Statuses retained: Designated, Proposed For Withdrawal, Withdrawn
- Teaching purpose: designation scope, current status, component score, and rights-aware public-source use

The selected source release preserves:

- HPSA identifier and name;
- designation type;
- discipline;
- score;
- status and dates;
- shortage and ratio context;
- population type;
- rural status;
- county FIPS;
- component identity and type;
- served and underserved estimates;
- source goal and shortage fields; and
- source record date.

### Dataset C: North Carolina place-access teaching table

- Rows: 100
- Columns: 29
- Grain: one county
- SHA-256: `90a575f03bc94cc0eb336d263e3f9d8afe09cf68ddb95476bf1836c0574f9a07`
- Teaching purpose: exact joined decision table

The table contains source fields and declared decision fields. It does not hide the distinction.

### Dataset D: generalized county boundaries

- Rows: 7,121
- Columns: 6
- Counties: 100
- Polygon parts: 104
- SHA-256: `6eb085f49b400d4ecf6f88646f51dd01fdd4154533262e66ade02b1d1d8f666f`
- Source coordinate system: EPSG:4326
- Teaching projection: Albers equal-area formula
- Teaching purpose: state-scale choropleth and critique maps

### Provenance chain

```text
CDC PLACES 2024 county release
  -> Module 09 five-measure North Carolina release
  -> select GHLTH
  -> one row per county

HRSA primary-care HPSA data mart, 2026-08-29 snapshot
  -> retain mappable North Carolina county FIPS
  -> preserve current and historical statuses
  -> select exact Designated rows for current context
  -> summarize component rows and unique HPSA IDs by county
  -> select highest active component score

Census Generalized ACS 2024 county service
  -> Module 05 flattened polygon release
  -> exact checksum-preserving Module 10 copy
  -> Albers equal-area teaching transformation at render time

joined county table
  -> declared two-condition screen
  -> 19 eligible counties
  -> first 12 in reproducible review order
```

### Rights decision

The direct HRSA HPSA metadata marks the selected attributes public. The usage page states no usage limitation.

The AHRF catalog page also reports no usage limitation, but the technical documentation inside the 2024-2025 archive restricts reproduction and identifies copyrighted AMA, AHA, and ADA source fields.

The Commons does not redistribute those AHRF clinician fields. The direct HPSA source provides the needed access context with a clearer public-data basis.

### Data minimization

The package does not retain:

- patient records;
- clinician names;
- personal contact fields;
- facility phone numbers;
- street addresses not required for the decision;
- individual-level survey data; or
- exact point locations.

### Completeness rule

The module preserves:

- all 100 selected county health rows;
- all 1,546 selected mappable HPSA rows;
- all status classes in the source selection;
- all 7,121 boundary points;
- all 104 polygon parts; and
- all 100 rows in the exact decision table.

No source value is imputed.

## 9. Data dictionary and expected analytic structure

### County identity

| Field | Type | Rule |
|---|---|---|
| `county_fips` | character | Five characters beginning with `37`. |
| `county_name` | character | Short display name. |
| `state_abbr` | character | `NC`. |

### Health fields

| Field | Type | Rule |
|---|---|---|
| `health_measure_id` | character | `GHLTH`. |
| `health_measure_label` | character | Fair or poor health display label. |
| `health_measure_year` | integer | 2022. |
| `adult_population` | integer | PLACES adult population context. |
| `age_adjusted_fair_poor_health_pct` | decimal | Source point estimate. |
| `age_adjusted_low_ci_pct` | decimal | Source lower interval limit. |
| `age_adjusted_high_ci_pct` | decimal | Source upper interval limit. |
| `national_age_adjusted_pct` | decimal | 17.0. |
| `difference_from_national_pct_points` | decimal | County point minus 17.0. |
| `health_rank_descending` | integer | 1 through 100, point estimate then FIPS. |
| `health_point_above_national` | character | Descriptive point direction. |

### HPSA fields

| Field | Type | Rule |
|---|---|---|
| `active_hpsa_component_rows` | integer | Designated source rows touching county. |
| `active_hpsa_designations` | integer | Unique designated HPSA IDs touching county. |
| `max_active_hpsa_score` | integer or blank | Highest designated component score. |
| `max_score_hpsa_ids` | character | IDs tied at maximum. |
| `max_score_hpsa_names` | character | Names tied at maximum. |
| `active_designation_types` | character | Sorted distinct types. |
| `active_rural_statuses` | character | Sorted distinct rural-status labels. |
| `whole_county_geographic_hpsa` | character | Yes only for current geographic single-county scope. |
| `higher_hpsa_score_screen` | character | Yes at score 20 or higher. |

### Decision fields

| Field | Type | Rule |
|---|---|---|
| `bivariate_screen_class` | character | Exact four-class label. |
| `reference_review_eligible` | character | Both conditions met. |
| `reference_review_order` | integer or blank | 1 through 19 among eligible counties. |
| `reference_shortlist` | character | Yes for order 1 through 12. |
| `time_alignment_status` | character | Exact 2022 and 2026 statement. |
| `interpretation_boundary` | character | Exact HPSA component-score limit. |

### Boundary fields

| Field | Type | Rule |
|---|---|---|
| `county_fips` | character | Joins to teaching table. |
| `county_name` | character | Census county label. |
| `polygon_group` | character | County, polygon, and ring identity. |
| `point_order` | integer | Sequential within group. |
| `longitude` | decimal | Source x coordinate in EPSG:4326. |
| `latitude` | decimal | Source y coordinate in EPSG:4326. |

### Expected analytic grain

- Health input: county-measure row.
- HPSA source input: designation component record.
- Teaching table: county.
- Boundary input: polygon point.
- Final exact table: county.
- Figure mark: county polygon, county interval, or county point.

### Join rules

1. Read all FIPS fields as character.
2. Require exactly 100 teaching county values.
3. Require exactly 100 boundary county values.
4. Reject an unmatched teaching or boundary county.
5. Do not use county name as the primary key.
6. Keep component rows separate until county aggregation is explicit.
7. Never join on ZIP code.

### Missingness rules

- Two counties have no current designated HPSA record touching them.
- Their maximum score remains blank.
- Blank maximum does not become zero.
- The lower screen class includes score below 20 or no active designation, with the distinction available in the exact table.
- Proposed-withdrawal rows remain proposed-withdrawal.
- Withdrawn rows remain withdrawn.

## 10. Worked example and instructor walkthrough

### Step 1: verify the source releases

Confirm:

- PLACES upstream checksum;
- HPSA full and selected checksums;
- boundary checksum;
- source dates;
- HRSA rights metadata; and
- the AHRF non-redistribution decision.

### Step 2: verify grains

Ask what one row means in each file.

The correct answer is:

- one county-measure estimate in Module 09;
- one HPSA component record in the selected HRSA release;
- one county in the teaching table; and
- one ordered polygon point in the boundary release.

### Step 3: select the health measure

Filter `measure_id == "GHLTH"`.

Expected result:

- 100 rows;
- one row per FIPS;
- measure year 2022;
- age-adjusted range 12.1% to 27.2%; and
- national point 17.0%.

### Step 4: select current HPSA context

Filter source status exactly equal to `Designated`.

Expected result:

- 740 component rows;
- 210 unique HPSA identifiers;
- 98 counties; and
- component scores from 3 to 24.

Do not include proposed-withdrawal or withdrawn rows in current context.

### Step 5: summarize HPSA context by county

For each county:

1. count component rows;
2. count unique HPSA identifiers;
3. select the maximum component score;
4. retain all IDs and names tied at the maximum;
5. collect designation types;
6. collect rural-status labels; and
7. identify an active geographic single-county designation.

Do not sum scores or component populations.

### Step 6: verify the join

Join on five-character county FIPS.

Expected result:

- 100 county rows;
- 100 unique FIPS;
- 98 counties with at least one active designation;
- 2 blank maximum scores; and
- no lost health estimates.

### Step 7: build the continuous health map

Use the age-adjusted health percentage as fill.

The reference scale runs from 12% to 28% and remains continuous. The map names the model-based estimate and year.

Adult population is not the fill.

### Step 8: apply the projection

Convert source longitude and latitude with the declared Albers equal-area formula:

- first standard parallel 29.5 degrees;
- second standard parallel 45.5 degrees;
- origin latitude 23 degrees; and
- central meridian 96 degrees west.

Record that the source release remains EPSG:4326.

### Step 9: define the two screen conditions

Health condition:

```text
county point estimate > 17.0
```

HPSA condition:

```text
highest current component score >= 20
```

Expected counts:

- health condition: 73;
- HPSA condition: 23; and
- both: 19.

### Step 10: build the four-class map

The exact classes are:

- Neither screen condition
- Higher health estimate only
- Higher HPSA score only
- Higher health estimate + higher HPSA score

Expected counts are 23, 54, 4, and 19 respectively.

### Step 11: build the non-map view

Order all counties by health point estimate descending, then FIPS.

Show:

- point estimate;
- source interval;
- national point reference;
- HPSA screen shape and fill; and
- a caption defining the HPSA value.

### Step 12: create the review order

Among the 19 counties meeting both conditions, order by:

1. health point descending;
2. HPSA maximum descending;
3. county name ascending; and
4. county FIPS ascending.

Mark the first twelve.

### Step 13: interpret the coordinated pair

The reference interpretation is:

- the map supports regional and neighboring-county coordination;
- the ordered view supports exact comparison and uncertainty review;
- the table supports audit and accessibility; and
- no view supports automatic allocation.

### Step 14: write the action

Invite the twelve reference counties into a listening and readiness process. Keep all nineteen eligible counties in the evidence table. Confirm source scope, local priorities, travel access, assets, and implementation capacity before further action.

## 11. Guided practice

### Exercise A: FIPS failure

Convert FIPS to integer, save, reload, and attempt the boundary join.

Learners explain:

- which identifiers change;
- why the result can silently fail;
- how character import prevents it; and
- which row-count assertion detects it.

### Exercise B: name join

Attempt a join using the display county names from the health, HPSA, and boundary sources.

Learners identify:

- suffix differences;
- punctuation and county-type differences;
- historical naming risk;
- case and spacing risk; and
- why FIPS is the primary key.

### Exercise C: raw count map

Inspect `C1-raw-count-need-map.png`.

Learners answer:

1. What is actually encoded?
2. What does the title claim?
3. Which large counties dominate?
4. When would population be a valid decision variable?
5. How would a two-view repair work?

### Exercise D: projection

Draw the source longitude and latitude directly, then compare it with the Albers output.

Learners state:

- the source coordinate system;
- the rendering projection;
- what equal-area preserves approximately; and
- what neither view says about travel time.

### Exercise E: class sensitivity

Compare:

- a continuous scale;
- equal-width bins;
- quantile bins;
- the exact four-class decision screen; and
- arbitrary severity labels.

Learners state which is descriptive, which is rank-based, which is decision-based, and which is unsupported.

### Exercise F: component scope

Select three counties with many component rows and three with a whole-county geographic designation.

Learners compare:

- component-row count;
- unique HPSA ID count;
- designation type;
- component type;
- maximum score; and
- whole-county status.

### Exercise G: map versus non-map

Hide the non-map view and answer the decision. Then hide the map and answer it again.

Learners list what is lost each time.

### Exercise H: stigmatizing language

Repair:

- problem county;
- sickest place;
- critical population;
- failing rural county; and
- high-need residents.

Repairs should name the source condition and action without turning it into identity.

### Exercise I: accessibility audit

Check:

- grayscale;
- legend language;
- non-color path;
- exact table;
- text alternative;
- county-name recovery;
- print size; and
- title and caption completeness.

## 12. Independent exercise

### Scenario

The access planner asks for a briefing that can be used with state staff and local partners.

The briefing must answer:

- where place appears relevant;
- which counties meet the declared screen;
- which twelve enter the reference conversation;
- what the map adds;
- what the non-map adds;
- what remains uncertain; and
- what local evidence is required.

### Required analysis

The learner must:

1. load the three released files;
2. verify their checksums or record the package checksums;
3. preserve FIPS as character;
4. validate the 100-county join;
5. apply a named projection;
6. reproduce the health map;
7. reproduce the exact four-class map;
8. reproduce an all-county non-map comparison;
9. retain source intervals;
10. retain population context;
11. identify all nineteen eligible counties;
12. reproduce the exact twelve-county order;
13. produce the exact decision table;
14. write an equivalent text alternative;
15. write a decision note;
16. document source rights; and
17. document AI use or non-use.

### Required products

- a place brief;
- editable R analysis;
- one continuous health map;
- one four-class screen map;
- one ordered non-map comparison;
- one 100-row exact table;
- one source record;
- one text alternative;
- one decision note; and
- one AI-use record.

### Independent choice

The learner may alter:

- layout;
- type size;
- accessible palette;
- direct labels;
- map and non-map coordination; and
- annotation.

The learner may not alter the reference source values or silently change the two screen rules.

## 13. Visualization and communication requirements

### Health map

The health map must:

- include all 100 counties;
- map the age-adjusted health percentage;
- name the estimate, population, year, and unit;
- name or document the projection;
- state the classification method;
- avoid raw population as health fill;
- use visible but restrained boundaries;
- provide an accessible legend;
- state that the source is model-based; and
- state what spatial interpretation is not supported.

### Four-class screen map

The bivariate map must:

- show exactly four classes;
- state both conditions;
- use exact class labels or faithful equivalents;
- report all class counts;
- state that score 20 is a teaching rule;
- avoid risk or severity labels;
- avoid red-green-only meaning;
- retain the exact table; and
- avoid claiming whole-county designation from component records.

### Ordered non-map comparison

The non-map must:

- use one scale for every county;
- make the national point visible;
- retain the source interval;
- use a reproducible order;
- show the HPSA screen with a redundant cue;
- define blank score handling;
- keep exact values available; and
- state the time mismatch.

### Review-list view

When a focused view is included, it must:

- show all 19 eligible counties or link to them in the table;
- distinguish the first twelve from the remaining seven;
- keep uncertainty visible;
- retain the HPSA score;
- retain adult population context;
- state the ordering rule; and
- state that the list begins discussion rather than allocation.

### Projection requirements

The submission must record:

- source coordinate system;
- rendering projection;
- why the projection fits the state-scale task;
- what it does not preserve; and
- why projection does not create service-access geography.

### Classification requirements

Every classified map must record:

- method;
- exact breaks or conditions;
- inclusion rule at each boundary;
- number of classes;
- class counts;
- decision purpose; and
- exact-value path.

### Accessibility requirements

Every figure package must include:

- readable title and subtitle;
- direct definition of measure and unit;
- redundant class meaning beyond color across the package;
- a grayscale or print check;
- all 100 rows in a table;
- a short alternative;
- a structured long description; and
- a filename that identifies the view.

### Claim discipline

The final package may say:

- the point estimate is above the national point;
- a county meets a declared screen;
- several selected counties are neighbors;
- a visible pattern suggests a regional conversation; and
- local evidence is required.

It may not say:

- a statistically significant cluster exists;
- the map proves causation;
- score 20 is an official funding cutoff;
- a county has a measured workforce rate from this table;
- every resident shares the county estimate;
- the whole county is designated when only components are; or
- the screen proves allocation priority.

## 14. Exact submission package and filenames

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

### `place-brief.md`

```markdown
# Place brief

## Decision owner and action

## Why place matters

## Source, grain, rights, and dates

## County join and completeness

## Measure, population, and adjustment

## HPSA component and score definition

## Projection and boundary

## Classification and screen

## Map versus non-map judgment

## Critique and repair

## Geography and equity limits

## Reproducibility record
```

### `decision-table.csv`

Required columns, in this order:

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

The file must contain exactly 100 data rows.

### `source-record.yml`

The record must include complete raw URLs, source dates, identifiers, rights, checksums, transformations, join rules, projection, class rules, and known limits.

### `alt-text.md`

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

### `decision-note.md`

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

### `ai-use.md`

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

### File-quality rules

- Every required file exists.
- `analysis.R` runs from a clean session.
- Figures are reproducible from released data.
- The table has exactly 100 rows.
- FIPS values remain five characters.
- The full URLs are not truncated.
- No source or decision date is hidden.
- No color-only path is required.
- AI use or non-use is explicit.

## 15. Rubric and pass conditions

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Decision and place rationale | 10 | The owner, action, geographic question, and reason place matters are explicit. |
| Source, grain, rights, and time | 12 | CDC, HRSA, Census, FIPS, grain, dates, rights, hashes, and AHRF decision are accurate. |
| Join and reproducibility | 8 | The 100-county join, fields, row counts, code, and exact output are reproducible. |
| Health map | 12 | Maps age-adjusted percentage with projection, unit, year, model boundary, and defensible scale. |
| Four-class screen map | 12 | Uses exact conditions, four classes, accessible cues, counts, and teaching-rule disclosure. |
| Non-map comparison | 12 | Preserves common scale, order, intervals, national reference, HPSA cue, and exact path. |
| Map-versus-non-map judgment | 10 | Assigns each view a concrete decision role and identifies what each cannot answer. |
| Decision table and shortlist | 8 | Contains 100 rows, 19 eligible, exact order, twelve reference rows, and required boundaries. |
| Accessibility and text alternative | 8 | Provides readable figures, redundant meaning, exact values, and equivalent description. |
| Equity, language, and claim discipline | 5 | Avoids stigma, identifies within-county limits, and requires local voice. |
| AI-use record | 3 | Declares use or non-use and records human verification. |
| Total | 100 |  |

### Score interpretation

| Score | Result |
|---:|---|
| 90-100 | Pass with strong decision readiness. |
| 80-89 | Pass when every noncompensable condition is met. |
| 70-79 | Revise and resubmit. |
| Below 70 | Does not pass. |

### Noncompensable pass conditions

The submission fails when any of these is true:

1. raw population is presented as a health rate or need measure;
2. FIPS is damaged or the county join is incomplete;
3. source grain is incorrect;
4. HPSA score is called a county workforce rate;
5. score 20 is presented as an official threshold;
6. proposed-withdrawal or withdrawn records are treated as designated;
7. the 2022 and 2026 dates are hidden;
8. a class rule or bin is undisclosed;
9. the map lacks a place-based decision purpose;
10. uncertainty and exact values are unavailable;
11. color is the only reading path;
12. the screen automatically allocates resources;
13. stigmatizing place language remains;
14. source rights or full URLs are missing;
15. AI output is not human-verified; or
16. the exact folder contract is incomplete.

## 16. Common errors, failure modes, and interventions

### Error 1: FIPS becomes numeric

Symptom: leading zeros disappear or joins fail.

Intervention: import FIPS as character and assert five-character length before joining.

### Error 2: county names become keys

Symptom: suffix, punctuation, or county-equivalent differences create unmatched rows.

Intervention: use FIPS as the primary key and names as an audit field.

### Error 3: population becomes health need

Symptom: large counties dominate a red map titled need.

Intervention: separate relative health rate from outreach volume.

### Error 4: age-adjusted estimate becomes count

Symptom: a percentage is described as people diagnosed.

Intervention: restate the measure, model, adult population, and estimate type.

### Error 5: default bins become official

Symptom: software-generated breaks appear without explanation.

Intervention: record the method and use continuous scale when no threshold exists.

### Error 6: arbitrary labels imply severity

Symptom: low, medium, high, and critical appear without a source.

Intervention: name the actual numeric range or decision condition.

### Error 7: map area becomes data weight

Symptom: large rural polygons appear more important than small urban counties.

Intervention: use the non-map comparison and state the visual-area effect.

### Error 8: projection is invisible

Symptom: longitude and latitude are drawn without documentation.

Intervention: name source coordinates, transformation, and projection purpose.

### Error 9: projection becomes service access

Symptom: a county map is interpreted as travel-time access.

Intervention: name the additional road, transit, origin, destination, and time data required.

### Error 10: HPSA component becomes county rate

Symptom: the maximum score is labeled county workforce shortage.

Intervention: use the full phrase highest active component score touching the county.

### Error 11: scores are summed

Symptom: counties with many component rows receive impossible totals.

Intervention: count components, count unique IDs, and retain a declared maximum separately.

### Error 12: every county is wholly designated

Symptom: any census-tract or facility designation colors the whole county as designated.

Intervention: inspect designation and component type; use the whole-county field only when supported.

### Error 13: status is ignored

Symptom: withdrawn records enter current analysis.

Intervention: filter exact `Designated` status and preserve all statuses in the source selection.

### Error 14: visible pattern becomes cluster proof

Symptom: a map caption says statistically significant cluster.

Intervention: replace with descriptive language or perform and document a spatial analysis outside module scope.

### Error 15: dates become contemporaneous

Symptom: the 2022 health and 2026 HPSA values are described as one period.

Intervention: print the time-alignment statement in table, figure, and note.

### Error 16: screen becomes truth

Symptom: counties outside the class are described as not needing support.

Intervention: state the two selected conditions and what they omit.

### Error 17: shortlist becomes allocation

Symptom: first twelve receive funds automatically.

Intervention: change action to listening, verification, and readiness review.

### Error 18: map stands alone

Symptom: exact county values and intervals cannot be recovered.

Intervention: require the ordered comparison and exact table.

### Error 19: non-map stands alone

Symptom: regional coordination and neighboring counties are invisible.

Intervention: state whether geography matters and add the map only when it does.

### Error 20: place language stigmatizes

Symptom: problem county or sick residents appears.

Intervention: describe source conditions, systems, and next questions.

### Error 21: AHRF is assumed open because downloadable

Symptom: copyrighted clinician fields are redistributed without reviewing included documentation.

Intervention: follow the specific source terms and use the direct public HPSA source for this release.

### Error 22: AI certifies the map

Symptom: an AI-generated interpretation is accepted without source, join, or language review.

Intervention: require the AI-use record and named human verification.

## 17. Accessibility, equity, privacy, and responsible claims

### Accessibility

The required package provides several reading paths:

- continuous health map;
- four-class screen map;
- ordered all-county comparison;
- exact table;
- short alternative;
- long description; and
- reproducible source code.

The maps alone are not the accessible product.

The learner must verify:

- title meaning without legend guessing;
- non-red-green palette;
- redundant HPSA cue in the non-map view;
- readable class names;
- county-name recovery from table and comparison;
- grayscale and print behavior;
- sufficient contrast;
- text size at delivery resolution; and
- equivalent numeric findings in the long description.

### Equity

The selected health estimate and shortage designation can identify questions. They cannot establish community priorities.

The package must state that county aggregates conceal:

- racial and ethnic inequities;
- income and insurance variation;
- disability access;
- language access;
- transportation;
- broadband;
- clinic hours;
- affordability;
- trust;
- local assets;
- community organizations;
- historical disinvestment;
- intervention fit; and
- readiness.

### Rurality

Rural status is context, not deficit.

The module does not assume:

- rural means low quality;
- urban means adequate access;
- county area equals travel burden;
- facility presence equals usable access; or
- a rural label describes every community in a county.

### Place language

Use:

- counties meeting the declared screen;
- counties invited for local review;
- areas with higher modeled estimates;
- current designation components touching the county; and
- communities whose priorities must be confirmed.

Avoid:

- problem county;
- sickest place;
- failing area;
- bad population;
- deficient community; and
- critical county without a source threshold.

### Privacy

The released data are public county and designation aggregates. No patient-level data are included.

Privacy still matters when learners propose future data. Small-area subgroup mapping, point locations, service use, or rare outcomes can create re-identification or stigma risk and require separate governance.

### Responsible claims

Every final claim must identify whether it is:

- a published source estimate;
- a published source designation;
- a derived comparison;
- a declared teaching screen;
- a visible spatial description;
- a planning assumption; or
- a proposed local question.

## 18. AI and agent policy

### Permitted uses

AI may help:

- explain projection code;
- draft FIPS validation checks;
- propose accessible palettes;
- compare class labels;
- draft text-alternative structure;
- identify inconsistent terminology;
- test whether figure and table counts agree;
- suggest critique questions; and
- edit learner-written prose for clarity.

### Required human work

The learner must personally verify:

- complete source URLs;
- source rights;
- checksums;
- the AHRF non-redistribution decision;
- grain definitions;
- FIPS joins;
- current status filtering;
- HPSA score interpretation;
- projection formula and declaration;
- class rules;
- all measured counts;
- shortlist order;
- accessibility;
- equity and place language; and
- final recommendation.

### Prohibited uses

AI may not:

- invent source terms;
- certify public-domain status;
- infer missing HPSA scope;
- label blank scores as zero;
- silently change a class rule;
- choose an allocation threshold;
- declare a statistical cluster from visual inspection;
- certify accessibility or cartographic validity;
- label a community; or
- replace local engagement.

### Minimum AI-use record

The record states:

- tool and model;
- prompts or instructions;
- work delegated;
- outputs retained;
- outputs rejected;
- source and rights verification;
- join and shortlist verification;
- projection verification;
- accessibility verification; and
- human decisions.

No AI use is acceptable when explicitly recorded.

## 19. Answer key and instructor notes

### Source answers

- PLACES dataset ID: `fu4u-a9bh`
- PLACES selected measure: `GHLTH`
- PLACES measure year: 2022
- HPSA discipline: Primary Care
- HPSA snapshot date: 2026-08-29
- Census service: Generalized ACS 2024 State and County
- County join key: five-character FIPS
- Source boundary coordinates: EPSG:4326
- Teaching projection: Albers equal-area formula

### Source-release answers

- Full HPSA rows: 79,358
- Full HPSA bytes: 48,280,174
- Selected HPSA rows: 1,546
- Selected HPSA columns: 28
- Designated rows: 740
- Proposed-withdrawal rows: 104
- Withdrawn rows: 702
- Active HPSA IDs: 210
- Active counties: 98
- Teaching rows: 100
- Teaching columns: 29
- Boundary points: 7,121
- Polygon parts: 104

### Health answers

- Minimum: 12.1%
- Maximum: 27.2%
- National point: 17.0%
- Counties above national point: 73
- Adult population minimum: 2,644
- Adult population maximum: 908,531

### HPSA screen answers

- County maximum active score range: 11 to 24
- Counties at score 20 or higher: 23
- Counties with whole-county geographic designation: 7
- Counties with no current designated record: 2

### Four-class answers

| Class | Count |
|---|---:|
| Higher health estimate + higher HPSA score | 19 |
| Higher health estimate only | 54 |
| Higher HPSA score only | 4 |
| Neither screen condition | 23 |

### Reference twelve answer

1. Robeson
2. Scotland
3. Hertford
4. Halifax
5. Warren
6. Greene
7. Washington
8. Wilson
9. Anson
10. Lenoir
11. Edgecombe
12. Swain

### Remaining eligible counties

13. Person
14. Chowan
15. Beaufort
16. Gates
17. Gaston
18. Johnston
19. Guilford

### Map answer

The map is useful because it can reveal neighboring counties and broad regional pattern for planning shared conversations. It also shows how county area affects visual prominence.

The map does not support exact ranking, formal cluster inference, travel access, causal interpretation, or allocation by itself.

### Non-map answer

The ordered comparison is useful because it preserves one quantitative scale, all source intervals, the national point, the HPSA screen, and the county order.

It does not show neighboring counties or regional configuration efficiently.

### Coordinated-pair answer

Use both when the planner needs regional coordination and exact comparative review. Use the table and text alternative as the audit and accessibility path.

### Critique answers

#### C1

Adult population is mislabeled as health need. The repair maps the health percentage and retains population in a separate view or table for outreach scale.

#### C2

Unexplained breaks and severity words imply official categories. The repair uses a continuous scale or states a decision-based method and exact breaks.

#### C3

The phrase problem county turns a screen into identity. The repair names source conditions and frames the action as local review.

### Rights answer

The direct HPSA source is redistributed because its metadata marks the selected fields public and the usage page reports no limitation. AHRF clinician fields are not redistributed because the included technical documentation contains more restrictive reuse language and identifies copyrighted source fields.

### Acceptable final recommendation

Invite the reference twelve into an initial listening and readiness process, retain all nineteen eligible counties in the evidence table, use the map for regional planning, use the ordered view for exact comparison, and verify local access, designation scope, community priorities, assets, and capacity before allocation.

### Claims that fail

- The twelve are North Carolina's worst counties.
- The map proves a cluster.
- Score 20 is an official threshold.
- HPSA score is the county's workforce rate.
- Every highlighted county is wholly designated.
- The current HPSA caused the older health estimate.
- The map justifies automatic funding.

### Instructor facilitation notes

Ask learners to compare their Module 09 list with the Module 10 list. The difference demonstrates that screening output changes when the decision question and source rule change.

Do not let the lesson become a search for the right color palette. Return to:

- the owner;
- the action;
- the grain;
- the source rule;
- what geography adds;
- what the map hides; and
- what must be learned locally.

## 20. Runnable acceptance checks

### Data build

From the repository root:

```powershell
python courses/data-visualization/modules/10-maps-geography-place/build_place_access_case.py
```

Expected checksums:

```text
HPSA selected: 061fe5e18bc9cd58bd89256c686ddefbce6d77972c1139b1b339497f2eab5445
Teaching table: 90a575f03bc94cc0eb336d263e3f9d8afe09cf68ddb95476bf1836c0574f9a07
Boundaries: 6eb085f49b400d4ecf6f88646f51dd01fdd4154533262e66ade02b1d1d8f666f
```

### Data validation

```powershell
python courses/data-visualization/modules/10-maps-geography-place/validate_place_access_case.py
```

Expected result:

```text
Module 10 place and access data passed 60 checks.
```

### Reference lab

```powershell
Rscript courses/data-visualization/modules/10-maps-geography-place/lab.R --output "$env:TEMP\oclc-da730-m10-lab"
```

Expected files:

```text
01-health-choropleth.png
02-health-ordered-comparison.png
03-bivariate-screen-map.png
04-reference-review-list.png
place_decision_table.csv
alt-text-reference.md
```

### Critique set

```powershell
Rscript courses/data-visualization/modules/10-maps-geography-place/critique_charts.R --output "$env:TEMP\oclc-da730-m10-critique"
```

Expected files:

```text
C1-raw-count-need-map.png
C2-arbitrary-bin-map.png
C3-stigmatizing-place-labels.png
```

### Visual acceptance

Human inspection confirms:

1. the health map contains all 100 counties;
2. the map is not visibly distorted by raw longitude-latitude rendering;
3. the continuous legend shows 12% through 28%;
4. the four screen classes are distinguishable;
5. the screen legend states conditions rather than severity;
6. the non-map view contains all 100 county labels;
7. every interval is visible;
8. the national point is visible;
9. the HPSA screen uses shape and fill;
10. the review plot contains 19 counties;
11. exactly 12 use the reference cue;
12. labels do not clip;
13. captions state the key interpretation boundaries; and
14. critique figures are visibly and pedagogically flawed.

### Repository checks

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
node --check curriculum-data.js
node --check site.js
git diff --check
```

The course checker requires 21 numbered sections, exact package files, Commons 0.21.0 metadata, and pinned row counts and checksums.

## 21. Release status, reviewers, version, and known issues

### Release status

- Module version: 0.1.0
- Commons release: 0.21.0
- Status: runnable release candidate
- Source build: complete
- Data validation: 60 of 60 checks pass
- Reference lab: complete
- Critique set: complete
- Assessment: complete
- Instructor key: complete
- Visual inspection: complete on Windows
- Named human reviews: pending

### Required human reviewers

Before alpha release, record named review from:

1. population-health and access-planning leader;
2. HRSA HPSA definition and source-fidelity reviewer;
3. geography or cartography reviewer;
4. equity and community-language reviewer;
5. visualization and accessibility reviewer; and
6. independent instructor.

### Known issues

1. PLACES values are model-based small-area estimates.
2. The 2022 health measure and 2026 HPSA snapshot are not contemporaneous.
3. The HPSA value is a maximum component score, not a county workforce rate.
4. Score 20 is a teaching rule, not an official threshold.
5. The twelve-county list is a planning-capacity assumption, not a validated priority score.
6. County boundaries do not represent travel time, referral networks, service areas, or community identity.
7. County aggregates conceal within-county differences and local assets.
8. The map describes visible pattern but does not test spatial clustering.
9. The Albers implementation is a teaching formula, not a production geographic library.
10. Static accessibility checks do not cover every assistive technology, printer, or viewing context.
11. macOS and Linux clean-run verification remain pending.
12. Human reviews remain pending.

### Release decision

Version 0.1.0 can remain a runnable release candidate. It cannot become alpha until the named human review roles are recorded and any material findings are resolved.

### Handoff to Module 11

Module 11 inherits:

- explicit data grain;
- source rights and checksum discipline;
- exact FIPS and county context;
- accessible color, table, and text-alternative contracts;
- the rule that a display structure must serve a decision;
- the distinction between screening and allocation; and
- the requirement to name what a structure hides.

Module 11 changes the central question. Instead of asking where, it asks whether the decision depends on transitions, connections, hierarchy, or part-to-whole structure. Learners must define every node, edge, state, denominator, and dropped record before choosing a flow, network, or composition display.
