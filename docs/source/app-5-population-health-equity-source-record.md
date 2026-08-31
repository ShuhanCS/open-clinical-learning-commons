# APP-5 Data for Population Health and Equity source record

- Source course ID: APP-5.
- Source title: Data for Population Health and Equity.
- Source filename: `09-APP-5-Population-Health-and-Equity.docx`.
- Source bytes: 20,996.
- Source SHA-256: `681f7e41878205492156535a5242a2ca599de677763fad69bbc73324e8eb38a7`.
- Verified: 2026-08-31.
- Commons course specification: `docs/curriculum/courses/APP-5/course-spec.md`.

## Package comparison

The source document was verified in both supplied curriculum packages:

- `Curriculum-30-Credits-2026-08-29.zip`, 235,378 bytes, SHA-256 `6d40015ab409e452f465cb813f83a432d259ff02513a6667e69cc5c67ffe9f25`; and
- `OneDrive_2026-08-29 (1).zip`, 253,781 bytes, SHA-256 `7c61107cdd768b2ef3f6b804c96e6c3ff106b14a9bc2c6c79dd8d9d6870f7b08`.

The APP-5 DOCX files are byte-for-byte identical. Both are 20,996 bytes and have the SHA-256 fingerprint above.

## Source course identity

- Credits: 3.
- Source format: seven-week online block.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Primary graded tools: SQL and Python with pandas, notebooks, and GeoPandas.
- R role: read, run, and interpret epidemiology, standardization, `tidycensus`, and small-area work; writing R from scratch is not graded.
- Versioning and accountability: Git, version records, and an AI-use log.

The Commons treats the source's seven weeks as seven instructional modules inside an official half-term. Week 3 and Week 6 are instructional checkpoints. The final checkpoint is due on the official last day of the assigned half-term.

Official calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The approved half-terms range from 50 to 53 inclusive calendar days, or approximately 7.14 to 7.57 weeks. “7.5 weeks” is therefore an instructional planning phrase, not a claim that every half-term has the same number of days.

## Source purpose and ownership

APP-5 teaches learners to measure how health differs across populations and places and to turn that evidence into an accountable intervention plan. The course owns:

- population, subgroup, and denominator definition;
- linked clinical, claims, public, Census, and contextual data;
- crude and specific rates;
- direct and indirect standardization;
- disparity measures and reference-group choice;
- small numbers, cell suppression, missing equity fields, linkage limits, measurement bias, and uncertainty;
- geographic aggregation, the modifiable areal unit problem, ecological fallacy, contextual and compositional reasoning, small-area stability, geocoding, spatial joins, and non-stigmatizing maps;
- resource allocation, need-based targeting, fairness, differential impact, benefit and harm tradeoffs, and balancing measures;
- intervention analytics, implementation measures, evaluation design, community communication, feedback, and human accountability; and
- a defended equity recommendation with monitoring and stated limits.

APP-5 does not repeat generic data retrieval, SQL, cleaning, missing-value handling, regression, classification, visualization design, or reproducible repository setup. It revisits those foundation skills through population-level decisions. DA-730 owns visualization concepts; APP-5 applies them to geographic and equity evidence.

## Source module sequence

| Week | Source module | Hours | Source submission |
|---:|---|---:|---|
| 1 | Framing a population-health decision | 15.5 | Population decision charter |
| 2 | Population measures from linked data | 16.0 | Population measure build |
| 3 | Disparities and data limits | 16.5 | Disparity analysis checkpoint |
| 4 | Place-based evidence and geographic reasoning | 16.5 | Responsible map and context memo |
| 5 | Targeting and fairness | 16.0 | Targeting and fairness audit |
| 6 | Designing an accountable intervention plan | 16.0 | Draft population intervention plan |
| 7 | Defending the population recommendation | 16.0 | Final population intervention analytics plan |
| Total |  | 112.5 |  |

## Source learning objectives

The source defines six course objectives:

1. frame a population-health question with its population, denominator, geography, time frame, stakeholders, and accountable decision;
2. construct and validate population, subgroup, rate, and denominator measures from linked clinical, claims, public, and contextual data;
3. analyze disparities with standardized rates and disparity measures while accounting for small numbers, missingness, linkage limits, measurement bias, and uncertainty;
4. interpret area-level and geographic evidence without ecological fallacy or stigmatizing groups and places;
5. evaluate an intervention for targeting, resource allocation, fairness, unintended harm, and monitoring; and
6. produce a population intervention analytics plan with transparent evidence, equity rationale, implementation and monitoring measures, and accountability.

## Source assessment weights

| Source assessment | Source timing | Weight |
|---|---|---:|
| Population measure and denominator labs | End of Week 2 | 20% |
| Disparity and data-bias analysis | End of Week 3 | 25% |
| Targeting and fairness audit | End of Week 5 | 20% |
| Population intervention analytics plan | End of Week 7 | 35% |
| Total |  | 100% |

## Commons checkpoint normalization

The master curriculum requires applied-course checkpoints of 40 points at Week 3, 25 points at Week 6, and 35 points at the official half-term end date. APP-5 preserves all source assessment content while normalizing five points from the Week 3 disparity component into the place, targeting, and fairness block:

- Week 3: Module 02 population measures and denominators, 20 points; Module 03 disparities and data limits, 20 points. Module 01 is a required zero-point gate.
- Week 6: Module 04 responsible place evidence, 10 points; Module 05 targeting and fairness, 15 points. Module 06 adds required intervention-design, monitoring, accountability, and embedded-ML gates without adding points.
- Official half-term end date: Module 07 final population intervention analytics plan, 35 points.

The source assignments remain recognizable and complete. No assignment content is removed, and no point is counted twice. The course total is `40 + 25 + 35 = 100`.

## Materials the source says must be developed

The source requires:

- a synthetic population dataset with clinical and claims extracts, public-health surveillance counts, Census and contextual tables, realistic geography, small groups, and missing equity fields;
- area-level social-determinant indices and geocoded boundaries;
- a denominator guide, rate-standardization template, disparity-measures notebook, small-number and suppression rules, GeoPandas mapping template, and non-stigmatizing visualization checklist;
- a targeting and fairness audit, community-facing communication rubric, intervention-plan template, and AI-use log; and
- answer keys and assessment rubrics.

These are build requirements. The source DOCX does not contain runnable data or code.

## Commons continuing decision

The course uses a fictional Massachusetts statewide population-health planning team. The team is considering a limited adult diabetes-prevention outreach planning review and must decide whether the evidence is strong and responsible enough to support structured community review, intervention design, and a later recommendation.

Real Massachusetts census tracts provide the public geographic units. The decision, team, resource limit, implementation conditions, capacity data, community-response data, and intervention outcomes are fictional or synthetic. No real agency, health system, municipality, community organization, or funding program is represented.

The public evidence may support questions about modeled prevalence, population structure, area context, geographic pattern, uncertainty, and where more local evidence or community review may be warranted. It cannot establish observed diabetes cases, individual risk, causal effects, intervention effectiveness, community deficit, automatic eligibility, resource entitlement, or a funding decision.

The course package may recommend a bounded fictional planning path. It cannot authorize real outreach, rank real people, allocate real money, label a community, start a program, evaluate a real intervention, or make a policy decision.

## Full public evidence architecture

### CDC PLACES role

CDC PLACES supplies the complete 2025 census-tract release for the `DIABETES` measure in Massachusetts. The accepted case extract contains every matching tract row and preserves measure year, modeled crude prevalence, 95% interval, total population, adult population, state, county, and tract identity.

Official dataset metadata:

https://data.cdc.gov/api/views/cwsq-ngmh

Official data page:

https://data.cdc.gov/widgets/cwsq-ngmh?mobile_redirect=true

Official PLACES program and methodology route:

https://www.cdc.gov/places/

The 2025 tract release describes model-based small-area estimates for 40 measures. For most measures, including diagnosed diabetes, it uses 2023 BRFSS data with Census 2020 population and 2019-2023 ACS inputs. CDC states that the small-area model cannot detect effects of local interventions and cautions against using the estimates for program or policy evaluation.

PLACES may support surveillance framing, source feasibility, pattern description, uncertainty, and later transparent planning comparisons. It does not supply observed diagnoses, event counts, individual records, causal effects, program outcomes, current capacity, or community preference.

### Census ACS role

The 2020-2024 American Community Survey five-year Detailed Table B01001 supplies complete age-by-sex population estimates and margins of error for Massachusetts census tracts.

Official developer page:

https://www.census.gov/data/developers/data-sets/acs-5year.html?lv=true

Official table landing page:

https://data.census.gov/table/ACSDT5Y2024.B01001

Complete table-based Summary File:

https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b01001.dat

The Commons acquisition route fingerprints the complete national B01001 file before extracting all Massachusetts tract rows. ACS estimates and margins remain paired. Annotation and sentinel values remain explicit. The table supplies denominators and population structure; it does not supply diabetes events, diagnoses, individual data, or intervention outcomes.

### CDC/ATSDR SVI role

The CDC/ATSDR Social Vulnerability Index 2022 Massachusetts tract release supplies area-level estimates, margins, themes, and relative rankings for contextual analysis.

Official data and documentation page:

https://atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html

Accepted Massachusetts tract download route:

https://svi2.cdc.gov/webapi/Documents/download?year=2022&type=csv&category=states&name=MASSACHUSETTS

SVI ranks tracts relative to other tracts in the same release and comparison set. Different SVI releases are not interchangeable, tract boundaries can change, and percentile ranks from different years are not longitudinal measures. SVI is area context. It cannot be assigned to individuals, treated as a community trait, or used alone to determine eligibility or funding.

### Census geography role

Census TIGER/Line 2024 census-tract boundaries supply the later mapping geometry.

Official 2024 TIGER/Line page:

https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html

Official census-tract download interface:

https://www.census.gov/cgi-bin/geo/shapefiles/index.php?layergroup=Census+Tracts&year=2024

Module 04 must acquire, fingerprint, and validate the complete Massachusetts tract boundary release before mapping. Boundaries support teaching geography, not address, parcel, routing, service-area, or operational eligibility decisions.

## Synthetic intervention and accountability layer

Public PLACES, ACS, SVI, and TIGER data do not contain program capacity, outreach mode, implementation cost, community preference, reach, refusal, burden, incident, benefit, or intervention outcome truth. The Commons therefore builds a separate, unmistakably synthetic layer before targeting or intervention evaluation.

The later release must contain at least these linked records:

| Table | Required grain and role |
|---|---|
| planning-areas | one teaching geography with public-source identity and explicit evidence status |
| population-denominators | one area, age group, period, estimate, uncertainty, and source identity |
| synthetic-events | one fictional event aggregate by area, age group, and period for rate and standardization exercises |
| candidate-interventions | one fictional intervention option with resource, access, delivery, and contraindication assumptions |
| capacity | one fictional area and period with staffing, slots, language access, disability access, and travel support |
| community-review | one fictional response or concern with provenance and decision right |
| allocation-scenarios | one transparent hypothetical rule result by area and group |
| implementation-stream | one fictional period with reach, uptake, refusal, burden, cost, balancing, and outcome-availability fields |
| known-truth | one seeded denominator, missingness, linkage, targeting, fairness, monitoring, or communication defect |

Every synthetic release requires a generator version, seed, field dictionary, row counts, bytes, hashes, relationship checks, known-truth contract, defect register, explicit synthetic flag, and prohibition on real-world use. Public records may inform structure and plausible ranges, but public tract identities cannot be represented as observed intervention results.

## Source-to-module routing

| Module | Source role | Protected handoff |
|---:|---|---|
| 01 | Inspect complete Massachusetts PLACES, ACS, and SVI tract releases; fix the TIGER route; define the population, denominator, geography, time, audience, community role, source roles, and claim boundary. | Population decision charter, source-feasibility release, accountability map, and permission to construct measures. |
| 02 | Link accepted public denominators and contextual fields to deterministic synthetic event aggregates; build crude, specific, direct-standardized, and guided indirect-standardized measures. | Accepted 20-point population measure and denominator component. |
| 03 | Build disparity measures, reference-group sensitivity, uncertainty, missing-equity-field audit, linkage and measurement-bias analysis, small-number rules, and suppression. | Accepted 40-point Week 3 technical release. |
| 04 | Acquire validated boundaries; test geographic aggregation, small-area stability, ecological claims, contextual and compositional language, spatial joins, and non-stigmatizing displays. | Accepted 10-point place-evidence component. |
| 05 | Compare equal, need-based, capacity-aware, and community-review targeting rules; audit differential impact, benefit, harm, and balancing measures. | Accepted 25-point Week 6 scored evidence. |
| 06 | Build the accountable intervention and monitoring design; compare a fixed unsupervised area-profile challenger with the transparent rule without allowing ML to allocate resources. | Accepted Week 6 application release and Module 07 permission. |
| 07 | Freeze both checkpoints and add clinician leadership, community-facing communication, accountability, disagreement, stewardship, monitoring, final recommendation, and defense. | Accepted or conditioned final course package. |

## Embedded machine-learning decision

Module 06 contains eight hours of intervention design, monitoring, feedback, and governance plus an eight-hour embedded-ML extension. The extension fits one fixed, predeclared clustering challenger to the same accepted area-level feature matrix used for descriptive planning. The algorithm, feature set, transformations, missing-value rule, scaling, number of clusters, seed, stability checks, and interpretation limits are fixed before results are inspected.

The challenger asks whether a reproducible area-profile grouping adds useful questions for tailoring a fictional intervention. It does not rank need, predict an individual outcome, infer a protected trait, select a tract, assign a program, set a budget, or replace community review. Learners compare cluster stability, support, missingness, geographic concentration, sensitivity to scaling and seed, and differential consequences against a transparent need-and-accountability rule.

ML may be rejected. Apparent separation, a visually tidy map, or improved average fit is not sufficient. The final decision remains human, documented, and bounded by public-source limits and affected-community review.

## Stable source decisions

- APP-5 remains a distinct applied course.
- The course totals 112.5 hours.
- SQL and Python are graded working tools; R remains read, run, and interpret.
- APP-5 owns population denominators, rate standardization, disparities, small-area reasoning, geography, targeting, fairness, intervention analytics, community accountability, and the equity recommendation.
- DA-730 owns visualization concepts; APP-5 applies them to population-health decisions.
- The continuing case is fictional, while the accepted tract-level public evidence is real and fully identified.
- PLACES is modeled prevalence, ACS and SVI are area-level estimates, and TIGER supplies geography. None supplies individual risk, observed intervention outcomes, causal effects, or allocation authority.
- Public and synthetic data roles remain separate.
- Module 06 contains eight hours of intervention design and accountability plus an eight-hour embedded-ML extension.
- Module 07 is clinician led.
- Checkpoints total 40 points at Week 3, 25 points at Week 6, and 35 points on the official half-term end date.
- Full public releases must be acquired, inspected, and fingerprinted before derived teaching evidence is created.
- No protected, identifiable, restricted, or live operational data enter the Commons or an external agent.

## Interpretation rule

The source document controls curriculum intent, workload, topic depth, and required assessment content. The master architecture controls the 40/25/35 checkpoint pattern and clinician-led final module. The Commons specification adds exact public-source routes, synthetic boundaries, filenames, checkpoint contracts, validation, accessibility, reviewers, leadership, and release controls needed to make the course runnable.
