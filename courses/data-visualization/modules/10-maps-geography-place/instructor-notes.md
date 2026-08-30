# Module 10 instructor notes

## Teaching purpose

This module is not a choropleth tutorial. It teaches learners to decide when geography changes an action, then to keep the comparative evidence available outside the map.

The strongest reference answer uses a coordinated pair:

- a map for regional pattern and neighboring-county coordination;
- an ordered comparison for rank, uncertainty, and exact reference;
- a table for audit and accessibility; and
- a decision note that requires local evidence before allocation.

## Preparation

Before teaching:

1. run `build_place_access_case.py` from the committed source selection;
2. run `validate_place_access_case.py` and confirm 60 checks;
3. render `lab.R` and inspect all four figures;
4. render `critique_charts.R` and inspect all three flawed figures;
5. verify that the exact table has 100 rows;
6. review the HRSA HPSA metadata definitions;
7. distinguish HPSA component, HPSA identifier, county, and whole-county designation;
8. rehearse the 2022 versus 2026 time limitation;
9. confirm that score 20 is described only as a teaching rule; and
10. prepare a local example of a county boundary that does not match a care network or travel area.

## Reproducible source facts

| Fact | Reference value |
|---|---:|
| PLACES source rows inherited from Module 09 | 500 |
| Selected GHLTH county rows | 100 |
| HPSA full source rows | 79,358 |
| Mappable North Carolina selected HPSA rows | 1,546 |
| Selected HPSA columns | 28 |
| Current designated component rows | 740 |
| Current unique HPSA identifiers | 210 |
| Counties touched by a current designation | 98 |
| Boundary points | 7,121 |
| Polygon parts | 104 |
| Teaching rows | 100 |
| Teaching columns | 29 |

## Reproducible decision facts

| Fact | Reference value |
|---|---:|
| Health measure year | 2022 |
| HPSA snapshot | 2026-08-29 |
| Health minimum | 12.1% |
| Health maximum | 27.2% |
| National health point | 17.0% |
| Counties above national point | 73 |
| Counties with maximum active component score at least 20 | 23 |
| Counties with a current whole-county geographic designation | 7 |
| Counties meeting both screen conditions | 19 |
| Counties in reference discussion list | 12 |
| Adult population minimum | 2,644 |
| Adult population maximum | 908,531 |

## Reference twelve

The exact order is:

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

The remaining seven eligible counties are Person, Chowan, Beaufort, Gates, Gaston, Johnston, and Guilford.

## Why the list differs from Module 09

Module 09 orders counties across five health measures. Module 10 selects one health measure and adds a primary-care HPSA component-score condition. The resulting reference list should differ.

That difference is a teaching feature. It shows that a review list is produced by a decision rule, not discovered as a permanent property of a place.

## Concept key

### Rate versus count

The health map uses an age-adjusted percentage. Adult population remains in the table and labels because it matters for scale and outreach planning.

A population map can answer where more adults live. It cannot answer where the health percentage is highest.

### HPSA component versus county

The selected HPSA value is the maximum score among designated component rows touching the county.

It is not:

- a county workforce rate;
- an average of all county designations;
- proof that the entire county is designated;
- a direct clinician count;
- a travel-time measure; or
- a funding decision.

### Whole-county designation

Only seven counties have a selected current geographic or high-needs geographic HPSA with component type `Single County`.

Most counties have population, census-tract, county-subdivision, or facility designations. Learners should not shade an entire county and call it wholly designated unless the source supports that scope.

### Projection

The boundary source uses longitude and latitude. The reference lab transforms the coordinates with an Albers equal-area formula before rendering.

The projection supports area comparison across a state map. It does not create travel-time or service-area geography.

### Classification

The continuous health map avoids invented severity categories. The four-class screen is categorical because two explicit binary decision questions are being combined.

The class labels state the rules. They do not rename them as risk or need.

### Modifiable areal unit problem

County estimates depend on county boundaries. A different aggregation, such as region, census tract, ZIP code, or service area, can change the apparent pattern.

Learners do not need to calculate a formal sensitivity analysis here. They must name the problem and state which alternative geography would matter for the decision.

### Spatial description versus inference

The map can reveal neighboring counties or broad regions worth discussing. The module does not calculate spatial autocorrelation, clusters, spillovers, or causal effects.

Language such as appears concentrated or forms a visible regional pattern can pass when paired with the descriptive boundary. Language such as statistically significant cluster does not pass without an analysis.

## Reference lab walkthrough

### Figure 1: continuous health map

Expected interpretation:

- the map provides geographic context;
- higher values appear in several eastern and southeastern counties;
- county size affects visual prominence;
- exact rank and interval are hard to recover; and
- no causal or cluster result is established.

### Figure 2: ordered comparison

Expected interpretation:

- all counties share one scale;
- intervals and the national point remain visible;
- county order is explicit;
- the HPSA screen has a redundant shape-and-fill cue; and
- this view better supports exact comparison.

### Figure 3: four-class screen

Expected class counts:

- both conditions: 19;
- health only: 54;
- HPSA only: 4; and
- neither: 23.

The map supports a regional conversation about the nineteen counties. It does not establish that the four classes are scientific categories.

### Figure 4: review list

The figure keeps all nineteen eligible counties. The first twelve use a filled triangle and the remaining seven use an open circle.

The interval, HPSA score, and adult population remain visible. Learners should see that the list limit is a planning constraint layered on top of the two source conditions.

## Critique key

### C1: raw-count need map

The map shades adult population but titles it as health need.

Repair:

1. name the actual question;
2. use a rate for relative health comparison;
3. retain population separately for outreach volume;
4. provide a table or coordinated second view; and
5. rewrite the title without claiming need.

### C2: arbitrary bins

The map uses unexplained cut points and the labels low, medium, high, and critical.

Repair:

1. use a continuous scale when no threshold exists;
2. if classes are needed, state the classification method and breaks;
3. explain why the method fits the action;
4. show exact values; and
5. avoid official-sounding category names.

### C3: stigmatizing place labels

The map turns a temporary screen into the identity `Problem county`.

Repair:

1. name the screening conditions;
2. describe system context rather than resident character;
3. state the data limits;
4. require local review; and
5. frame the action as listening or verification.

## Suggested lesson flow

| Time | Activity |
|---:|---|
| 0:00-0:25 | Decision, source rights, and map-purpose opening. |
| 0:25-0:55 | Grain, FIPS, boundary, designation, and time audit. |
| 0:55-1:25 | Rate-versus-count critique. |
| 1:25-2:10 | Continuous choropleth and projection lab. |
| 2:10-2:50 | Classification and four-class screen. |
| 2:50-3:30 | Ordered non-map comparison with intervals. |
| 3:30-4:00 | Break and independent source check. |
| 4:00-4:40 | Map-versus-non-map decision exercise. |
| 4:40-5:20 | Geography, aggregation, rurality, and service-area discussion. |
| 5:20-6:00 | Stigma, community voice, and decision-language repair. |
| 6:00-8:10 | Independent build and exact table. |
| 8:10-8:30 | Submission check and Module 11 handoff. |

## Questions to ask learners

1. What can the map reveal that the dot plot cannot?
2. What can the dot plot reveal that the map cannot?
3. Which county appears visually prominent because of area?
4. Which definition belongs to the color?
5. Is the HPSA value a county value?
6. What happens when census-tract designations are painted as a whole county?
7. What year does each source describe?
8. What would a travel-time map require?
9. What local evidence could reverse the reference order?
10. Which words describe a source condition, and which words stigmatize people?

## Acceptable decision language

An acceptable conclusion is:

> Invite the twelve reference counties into an initial listening and readiness process, while retaining all nineteen eligible counties in the evidence table. Use the map to plan regional conversations and the ordered comparison to verify estimates and uncertainty. Confirm designation scope, travel access, local priorities, and implementation capacity before proposing resource allocation.

Equivalent wording can pass.

## Claims that do not pass

- These are North Carolina's sickest counties.
- The map proves an eastern cluster.
- HPSA score 20 is HRSA's funding cutoff.
- The HPSA score is the county's physician shortage rate.
- Every highlighted county is wholly designated.
- The 2026 designations caused the 2022 health values.
- The top twelve should automatically receive funding.
- A county below the screen has no access problem.
- A county above the screen lacks local assets.

## Accessibility review

Confirm that:

- figure titles state the measure and decision role;
- legends spell out the screen conditions;
- the four classes remain distinguishable without red-green contrast;
- the ordered comparison repeats the HPSA screen with shape and fill;
- the exact table contains all 100 counties;
- the text alternative provides values and structure, not color-only description;
- the output remains readable at the submitted size; and
- county names can be recovered outside the map.

## Equity and community-language review

Look for:

- place labels that imply resident blame;
- language that erases structural conditions;
- county averages presented as every person's experience;
- rural status treated as deficit;
- HPSA designation treated as community identity;
- screening rules treated as community priorities; and
- action proposed without resident or local-organization participation.

## Source-rights lesson

The AHRF decision is worth teaching. The file is downloadable and its catalog page reports no usage limits, but the included documentation restricts reproduction and identifies copyrighted source data.

The lesson is not that AHRF is unusable. The lesson is that a Commons redistribution decision must follow the most specific source documentation. The direct HRSA HPSA data mart provides public fields without importing the AHRF conflict.

## Handoff to Module 11

Module 10 ends when ordinary comparison and geography can no longer express the structure that matters.

Module 11 asks learners to define:

- a state or transition;
- a node and edge;
- a denominator through a flow;
- a part and whole; and
- when a funnel, alluvial view, matrix, network, stacked bar, or tree fits the decision.

## Human release gates

Before alpha release, record named review from:

1. a population-health or access-planning leader;
2. an HRSA HPSA definition reviewer;
3. a geography or cartography reviewer;
4. an equity and community-language reviewer;
5. a visualization and accessibility reviewer; and
6. an independent instructor who can run the package from the README.
