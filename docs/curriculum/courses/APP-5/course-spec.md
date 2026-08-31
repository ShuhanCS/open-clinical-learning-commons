# APP-5: Data for Population Health and Equity

## 1. Course identity and catalog role

- Course ID: APP-5.
- Title: Data for Population Health and Equity.
- Credits: 3.
- Delivery: online half-term.
- Planning rhythm: seven instructional modules plus the official half-term end date.
- Total learner work: 112.5 hours.
- Prerequisites: accepted FND-1 and FND-2 technical releases.
- Primary graded tools: SQL and Python.
- Python environment: pandas, notebooks, GeoPandas, and a fixed machine-learning environment when the Module 06 challenger is built.
- R role: read, run, and interpret epidemiology, standardization, `tidycensus`, and small-area examples; writing R from scratch is not graded.
- Final deliverable: population intervention analytics plan with a reproducible evidence release, equity rationale, targeting and fairness audit, implementation and monitoring design, community-facing summary, accountability record, and defense.
- Course version target: `0.1.0`.
- Current Commons release target: `0.92.0` through Module 05.
- Specification status: construction candidate.

APP-5 is where learners define the population behind a health decision, construct and test its denominators, measure how rates differ across groups and places, and decide what that evidence can responsibly support. Learners move from public and contextual data through standardization, disparity analysis, geographic reasoning, targeting, intervention design, monitoring, and a clinician-led defense.

The course treats equity work as both technical and accountable. A disparity has a numerator, denominator, reference group, uncertainty, data-generation process, and decision consequence. A map is an area-level claim, not a description of every person living in an area. A targeting rule is a policy choice, not a neutral calculation. A final recommendation must name who is affected, who can question it, who owns it, what could cause harm, and who can stop it.

The academic calendar controls each due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The 7.5-week phrase is a planning model. Week 3 and Week 6 are instructional checkpoints. The final package is due on the published last day of the assigned half-term.

| Half-term | Published dates | Inclusive calendar days | Approximate weeks |
|---|---|---:|---:|
| Fall 2026 half-term 1 | September 8 through October 27 | 50 | 7.14 |
| Fall 2026 half-term 2 | October 28 through December 18 | 52 | 7.43 |
| Spring 2027 half-term 1 | January 11 through March 2 | 51 | 7.29 |
| Spring 2027 half-term 2 | March 3 through April 24 | 53 | 7.57 |
| Summer 2027 half-term 1 | May 10 through June 29 | 51 | 7.29 |
| Summer 2027 half-term 2 | June 30 through August 20 | 52 | 7.43 |

## 2. Source authority and normalization

The source course is `09-APP-5-Population-Health-and-Equity.docx`, 20,996 bytes, SHA-256 `681f7e41878205492156535a5242a2ca599de677763fad69bbc73324e8eb38a7`. Byte-identical copies appear in both supplied curriculum archives.

The source record is `docs/source/app-5-population-health-equity-source-record.md`.

The source defines seven modules totaling 112.5 hours and assessments weighted 20, 25, 20, and 35 percent. The master curriculum requires three cumulative checkpoints totaling 40, 25, and 35 points. APP-5 preserves all source assessment work while normalizing five points from the Week 3 disparity component into the place, targeting, and fairness block:

- Week 3: 20 points for the population measure and denominator build plus 20 points for the disparity and data-limit analysis;
- Week 6: 10 points for responsible place evidence plus 15 points for the targeting and fairness audit; and
- official half-term end date: 35 points for the final population intervention analytics plan.

Module 01 is a required zero-point gate. Module 06 supplies required intervention-design, monitoring, accountability, and embedded-ML gates without adding points. Every source assignment remains present, and no point is counted twice.

## 3. Place in the program and prerequisite handoffs

### FND-1 handoff

Learners arrive able to maintain a reproducible repository, retrieve and inspect complete public releases, define cohorts and denominators, write SQL joins and aggregations, clean and profile data, preserve source values, handle missingness, publish accessible tables, record provenance, and verify agent-assisted work.

APP-5 does not reteach generic repository setup, SQL syntax, data cleaning, joins, descriptive statistics, missing-value handling, or source acquisition. It applies those skills to public population denominators, geographic joins, rate tables, small cells, suppression, linked contextual data, community-review records, and allocation scenarios.

### FND-2 handoff

Learners arrive able to define an estimand and analysis population, fit and interpret regression and classification models, inspect assumptions, preserve temporal order, evaluate uncertainty and model performance, audit subgroup support, distinguish prediction from causation, and communicate limits.

APP-5 does not repeat generic regression or model evaluation. It extends those skills to standardization, disparity measures, reference-group sensitivity, small-area instability, area-level associations, targeting consequences, fairness, monitoring, and a bounded unsupervised ML challenger.

### DA-730 handoff

Learners use visual hierarchy, comparison design, uncertainty display, annotation, accessible color, exact-value alternatives, map critique, dashboard concepts, and audience adaptation from DA-730. APP-5 grades figures for population-health meaning, geographic responsibility, accessibility, and decision use. It does not reteach chart grammar or Tableau mechanics.

The old Tableau-based data visualization course remains separate. The new DA-730 course remains the conceptual visualization course. APP-5 is neither version of data visualization.

### Applied-course handoffs

- APP-1 supplies clinical outcome and care-pathway reasoning; APP-5 owns population denominators, geographic aggregation, and population intervention framing.
- APP-2 supplies patient voice, access, burden, missingness, and representation; APP-5 owns community accountability in a population-level allocation decision.
- APP-3 supplies operational measures, capacity, monitoring, and balancing measures; APP-5 owns need-based allocation and its equity consequences across places and groups.
- APP-4 supplies threshold, subgroup-support, workflow, safety, monitoring, and governance questions; APP-5 owns area-level targeting, resource allocation, ecological limits, and community review.

### Downstream handoff

- APP-6 may use APP-5's frozen population, geography, disparity, and intervention proposal but owns causal estimands, comparison design, identification, bias analysis, and effect estimation.
- CAP-1 may use an accepted APP-5 package only after preserving the exact public-source, synthetic-release, checkpoint, and claim-boundary identities.

## 4. Course decision and named audiences

The continuing teaching decision is:

> Should a fictional Massachusetts statewide population-health planning team advance a limited adult diabetes-prevention outreach proposal from population measurement into structured community review and intervention planning, or should it revise, refer, or stop the proposal?

The public evidence uses real Massachusetts census-tract identities. The planning team, resource constraints, intervention options, capacity, implementation stream, and outcomes are fictional or synthetic. The course cannot make a real funding, service, outreach, or policy decision.

### Primary decision owner

The primary owner is a fictional statewide population-health planning council led jointly by a clinician, epidemiologist, community-engagement lead, public-health program lead, data steward, accessibility and language-access lead, and resource-allocation owner. The council may continue with conditions, revise, refer, or stop the fictional proposal. A curriculum package does not authorize real outreach, targeting, allocation, implementation, or evaluation.

### Required audiences

| Audience | What they need |
|---|---|
| Residents and affected communities | purpose, evidence, uncertainty, language, access, possible benefit and harm, recourse, review rights, and limits |
| Community organizations | what the data can and cannot say, how local knowledge changes the plan, resource assumptions, feedback, and stop routes |
| Clinicians and clinical leaders | condition meaning, care context, population-to-patient boundary, safety, referral burden, and clinical limits |
| Public-health program leaders | population, denominator, geography, trend, need, capacity, implementation, balancing measures, and accountability |
| Epidemiologists and biostatisticians | rate construction, standardization, uncertainty, suppression, reference groups, bias, and support |
| GIS and data teams | source vintage, geographic key, tract change, spatial join, aggregation, geometry, and reproducibility |
| Equity, civil-rights, language, and disability reviewers | representation, differential impact, stigma, accessibility, burden, exclusion, and review authority |
| Finance and resource owners | allocation rule, constraints, tradeoffs, sensitivity, capacity, monitoring, and nonautomatic status |
| Privacy and governance reviewers | public versus synthetic roles, minimization, disclosure, access, audit, accountability, and prohibited use |

## 5. Course learning outcomes

By the end of APP-5, learners can:

| ID | Assessable course outcome | Program connection |
|---|---|---|
| CLO-1 | Frame a population-health decision with a precise population, numerator, denominator, geography, period, surveillance cadence, affected communities, accountable audience, and action boundary. | Applied framing and leadership |
| CLO-2 | Construct, link, validate, and document population, subgroup, rate, denominator, and contextual measures from complete public and synthetic releases. | FND-1 data work applied to population health |
| CLO-3 | Calculate and interpret crude, specific, directly standardized, and guided indirectly standardized measures with transparent uncertainty and support. | Applied statistics and epidemiology |
| CLO-4 | Measure disparities using absolute and relative scales, justify the reference group, and account for small numbers, suppression, missing equity fields, selection, linkage, and measurement bias. | Equity measurement and responsible claims |
| CLO-5 | Interpret geographic and area-level evidence without ecological fallacy, unstable small-area claims, misleading aggregation, or stigmatizing language and displays. | DA-730 and geographic application |
| CLO-6 | Compare targeting and allocation rules for need, capacity, fairness, differential impact, possible benefit, possible harm, and balancing consequences. | Population intervention design |
| CLO-7 | Build and defend an accountable intervention analytics plan with implementation measures, monitoring, community review, feedback, governance, a bounded ML comparison, and human decision ownership. | Leadership, ML, and accountability |

## 6. Concept ownership and boundaries

### APP-5 owns

- population, subgroup, numerator, denominator, rate, period, cadence, and geography contracts;
- linked public, Census, contextual, synthetic clinical, and synthetic program data;
- crude and specific rates;
- direct standardization and guided indirect standardization;
- absolute and relative disparity measures and reference-group sensitivity;
- small counts, unstable rates, suppression, aggregation, privacy, uncertainty, and minimum support;
- missing race, ethnicity, language, disability, and geography fields;
- selection, linkage, geocoding, boundary, and measurement bias;
- Census tracts, counties, ZIP Code Tabulation Areas, service areas, crosswalks, spatial joins, and geographic aggregation;
- modifiable areal unit problem, ecological fallacy, contextual and compositional reasoning, and small-area stability;
- non-stigmatizing maps and community-facing population evidence;
- equal, need-based, capacity-aware, and community-review allocation rules;
- fairness definitions, differential impact, benefit and harm tradeoffs, access, burden, and balancing measures;
- intervention analytics, implementation measures, evaluation proposal, feedback, governance, stewardship, and accountability;
- a bounded area-profile ML challenger that cannot allocate resources; and
- a clinician-led population intervention recommendation and defense.

### APP-5 extends rather than repeats

- FND-1 owns generic data engineering, SQL, source acquisition, cleaning, profiling, missingness, provenance, reproducibility, and basic descriptive statistics.
- FND-2 owns generic probability, inference, regression, classification, validation, uncertainty, model cards, monitoring, and causal-versus-predictive distinctions.
- DA-730 owns visualization concepts, perception, accessible color, comparison design, uncertainty display, mapping concepts, dashboards, and audience adaptation.
- APP-1 through APP-4 own their respective clinical, patient, operations, and CDS decisions.

APP-5 revisits these methods only when they change a population-health or equity decision. A technically correct rate is not sufficient if its denominator, reference group, geography, uncertainty, language, or decision consequence is wrong.

### Out of scope

- protected, identifiable, restricted, live clinical, claims, workplace, or program-participant data;
- real public-health targeting, outreach, enrollment, eligibility, allocation, funding, or program evaluation;
- individual risk, diagnosis, treatment, referral, benefit, burden, or eligibility inferred from an area value;
- an SVI rank, PLACES estimate, cluster, map color, or composite score used as an automatic decision;
- causal claims about place, race, ethnicity, language, disability, income, housing, transportation, or an intervention without an accepted causal design;
- claims that modeled prevalence is observed disease or that an area association describes every resident;
- cross-year SVI rank comparisons or geographic comparisons without compatible boundaries and vintages;
- a live geocoding, address, parcel, routing, service-area, or operational boundary system;
- autonomous allocation, intervention, monitoring, escalation, communication, or retirement decisions; and
- claims of regulatory compliance, policy approval, implementation readiness, or real-world effectiveness.

## 7. Continuing source and analytic thread

### Full public evidence

The continuing public evidence has four identified layers:

1. the complete Massachusetts `DIABETES` subset of the CDC PLACES 2025 census-tract release;
2. every Massachusetts census-tract row from 2020-2024 ACS five-year Detailed Table B01001, extracted only after the complete national table file is fingerprinted;
3. the complete CDC/ATSDR SVI 2022 Massachusetts census-tract CSV; and
4. the complete Census TIGER/Line 2024 Massachusetts tract boundary release, acquired before Module 04 mapping.

Module 01 freezes the accepted tabular identities and the geometry route. Later modules may derive measures only through reviewed code and immutable handoffs.

PLACES supplies modeled small-area prevalence and its interval, not observed cases or program effects. ACS supplies population estimates and margins, not disease events. SVI supplies area context and relative ranks, not individual traits or entitlement. TIGER supplies boundaries, not service access or community identity.

### Deterministic synthetic evidence

A Commons generator will add fictional event aggregates, program capacity, intervention options, community-review records, allocation scenarios, implementation measures, balancing measures, outcomes, and known defects. The synthetic layer makes rate construction, standardization, targeting, monitoring, and intervention design assessable without pretending that public tract data contain those facts.

Public and synthetic fields remain separately labeled. A public tract identity cannot be paired with a synthetic intervention outcome and then reported as a real local result. Any derived teaching scenario must state what is public, what is synthetic, and what combination can support.

### Continuing analytic sequence

The course begins with no ranked tract, accepted target, intervention, model, or funding rule. Module 02 constructs population measures. Module 03 freezes a technically supported disparity analysis. Module 04 adds place evidence. Module 05 compares transparent targeting rules. Module 06 designs monitoring and tests a bounded clustering challenger. Module 07 freezes both checkpoints and adds clinician leadership, community accountability, and the final recommendation.

### Safety guidance

The central safety rule is that population evidence informs a human process; it does not authorize action by itself. Every transformation preserves source identity, uncertainty, and unavailable states. Every allocation scenario names benefits, burdens, exclusions, assumptions, affected groups, review rights, and a human owner.

## 8. Workload and module sequence

| Module | Title | Hours | Assessment role |
|---:|---|---:|---|
| 01 | Framing a population-health decision | 15.5 | Required Week 3 gate |
| 02 | Population measures from linked data | 16.0 | 20-point Week 3 component |
| 03 | Disparities and data limits | 16.5 | 20-point Week 3 component |
| 04 | Place-based evidence and geographic reasoning | 16.5 | 10-point Week 6 component |
| 05 | Targeting and fairness | 16.0 | 15-point Week 6 component |
| 06 | Accountable intervention design, monitoring, and embedded ML | 16.0 | Required Week 6 gate |
| 07 | Clinician leadership and equity recommendation | 16.0 | 35-point final component |
| Total |  | 112.5 | 100 points |

Modules 01 through 03 form the applied statistics and population-measurement block. Modules 04 through 06 form the application, exercise, place, targeting, and intervention-design block. Module 06 contains eight hours of intervention design, monitoring, feedback, and governance plus eight hours of embedded ML. Module 07 is clinician led.

## 9. Module 01 brief: Framing a population-health decision

- Module ID: `oclc-app5-01`.
- Hours: 15.5.
- Package path: `courses/population-health-equity/modules/01-population-health-decision/`.
- Specification: `docs/curriculum/courses/APP-5/modules/01-population-health-decision-spec.md`.
- Decision: are the population, denominator, geography, time frame, source roles, community role, accountable audience, and claim boundaries coherent enough to begin measure construction?
- Submission: population decision charter and source-feasibility release.
- Point role: required zero-point gate for Checkpoint 01.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.87.0`.

Learners define the adult population, provisional numerator concept, matching denominator, Massachusetts tract geography, evidence period, surveillance cadence, decision owner, affected communities, possible benefit, possible harm, alternative action, nonaction, review rights, and stop rights.

The module acquires and profiles the accepted PLACES, ACS, and SVI tabular releases, records the TIGER route, and tests tract-key feasibility without silently dropping mismatches. Learners distinguish population health from individual care, define equity, disparity, and inequity precisely, and document what each source can and cannot support.

The accepted release contains 1,597 PLACES rows, 1,620 ACS rows, 1,613 SVI rows, and a 282-row field inventory. Its three-source intersection contains all 1,597 PLACES tracts; the union contains 1,620 tracts. The builder produces 27 files from 16 immutable manifest rows and ten editable learner records. Complete, starter, copied, deterministic, and protected-failure validation pass.

Progression requires an accepted population decision charter, denominator contract, geography and time contract, public-data role map, source-feasibility interpretation, equity-language contract, community-accountability map, claim boundary, AI-use record, and decision to begin Module 02 measure construction.

No rate calculation, standardization, disparity metric, tract ranking, targeting, map, allocation, model, intervention-effect estimate, real community claim, or implementation authority is allowed in Module 01.

## 10. Module 02 brief: Population measures from linked data

- Module ID: `oclc-app5-02`.
- Hours: 16.0.
- Package path: `courses/population-health-equity/modules/02-population-measures-linked-data/`.
- Specification: `docs/curriculum/courses/APP-5/modules/02-population-measures-linked-data-spec.md`.
- Decision: are the linked population, subgroup, numerator, denominator, rate, and standardization measures correct and supported enough to enter disparity analysis?
- Submission: 20-point population measure and denominator build.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.88.0`.

SQL owns tract and age-group keys, accepted joins, numerator and denominator alignment, missing and unmatched states, aggregation, duplicate detection, and reconciliation totals. Python independently checks every rate and standardization table.

Learners build crude and group-specific rates, perform direct standardization to one declared standard population, and complete a guided indirect-standardization exercise where direct support is sparse. Every result preserves the numerator, denominator, multiplier, age groups, standard weights, interval, source, period, geography, suppression state, and claim limit.

The public PLACES value remains modeled prevalence. Synthetic event counts remain synthetic. Learners may compare them as separately labeled evidence but cannot combine them into a false observed local measure.

The accepted release freezes the complete 27-file Module 01 reference workspace, preserves all 1,620 union tracts, and constructs 7,985 denominator rows and 7,985 generated event rows across 1,597 matched tracts. The adult denominator totals 5,679,768 and the generated numerator totals 283,614. Direct rates are available for 1,576 tracts and remain unavailable for 21; 80 tracts require the guided indirect exercise. All 30 SQL checks, independent Python reproduction, 266 complete checks, 187 starter checks, and 12 protected failure routes pass.

The component cannot pass with a mismatched population, denominator, period, geography, age group, source, uncertainty, or standard population; a hidden unmatched row; an unavailable value converted to zero; or an unsupported observed-case claim.

## 11. Module 03 brief: Disparities and data limits

- Module ID: `oclc-app5-03`.
- Hours: 16.5.
- Package path: `courses/population-health-equity/modules/03-disparities-data-limits/`.
- Specification: `docs/curriculum/courses/APP-5/modules/03-disparities-data-limits-spec.md`.
- Decision: does the evidence support a disparity statement strong enough to enter place and targeting work under explicit limits?
- Submission: 20-point disparity and data-limit analysis for the separate 40-point Week 3 checkpoint.
- Build status: runnable release candidate at Module version `0.1.0` and Commons release `0.89.0`.

Learners calculate rate difference, rate ratio, and at least one summary disparity measure. They justify the reference group, test how another defensible reference changes interpretation, report intervals and support, and separate absolute from relative disparity.

They profile missing race, ethnicity, language, disability, and geography fields; examine who is captured, linked, or excluded; distinguish selection, linkage, and measurement bias; and apply deterministic small-number, suppression, and aggregation rules. Suppressed values remain unavailable rather than becoming zero or being recoverable through totals.

The accepted release freezes the complete 72-file Module 02 reference workspace and adds three separately reconciling synthetic marginal dimensions with 19 groups, 151,715 group-margin rows, and a separate 7,985-row field-completeness audit. Every dimension reconciles to the accepted 5,679,768 adult denominator and 283,614 synthetic events. The release contains 110 group-age rates, 22 standardized group rates, 32 reference comparisons, six summary disparities, five missingness results, 19 representation records, and an eight-row bias register. Deterministic primary and complementary suppression leave 21,230 of 30,343 tract-group cells unavailable and non-reconstructable. All 36 query checks, 12 source-reconciliation checks, 4,791 suppression audits, 431 complete checks, 332 starter checks, and 17 protected failure routes pass.

The supported statement applies only to the fictional synthetic release. It does not establish a real disparity, an intersectional result, a map, a tract ranking, a target, an allocation, an intervention effect, or authority to act.

The Week 3 checkpoint freezes the population, denominator, source identities, standardization, disparity measures, reference groups, uncertainty, missingness, support, suppression, bias analysis, responsible claim, AI record, score, gates, and progression decision before place-based targeting begins.

## 12. Module 04 brief: Place-based evidence and geographic reasoning

- Module ID: `oclc-app5-04`.
- Hours: 16.5.
- Package path: `courses/population-health-equity/modules/04-place-evidence-geographic-reasoning/`.
- Specification: `docs/curriculum/courses/APP-5/modules/04-place-evidence-geographic-reasoning-spec.md`.
- Decision: can the accepted population evidence be communicated geographically without unstable, ecological, misleading, or stigmatizing claims?
- Submission: 10-point responsible map and context memo.
- Build status: runnable release candidate at module version `0.1.0` and Commons release `0.91.0`.

Learners acquire and validate the complete accepted Massachusetts tract geometry. They test keys, coordinate reference systems, invalid geometry, missing geometry, extra geometry, tract vintage, spatial joins, and aggregation before mapping.

The module compares tract and county aggregation to expose the modifiable areal unit problem, distinguishes contextual from compositional interpretations, tests small-area stability, and rewrites ecological and stigmatizing claims. Learners use DA-730 principles to choose accessible encodings, class breaks, uncertainty treatments, exact-value alternatives, notes, and community-facing language.

A polished map cannot compensate for wrong geography, wrong vintage, unstable support, a hidden join loss, inaccessible output, ecological inference, or language that treats a place or its residents as the problem.

The accepted release commits the complete 4,506,627-byte 2024 TIGER/Line Massachusetts tract archive with SHA-256 `74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4`. All 1,620 geometries are valid. The exact join matches 1,597 public CDC PLACES modeled diabetes prevalence rows and retains 23 geometry-only tracts as unavailable. Forty-nine tracts carry a classroom support-review flag. Fourteen population-weighted county teaching summaries expose 645 tract class changes under aggregation.

The deterministic accessible SVG, complete 1,620-row exact table, structured and written alternatives, ecological claims audit, and context memo pass. The reference earns 10 of 10 and passes all 22 gates. Complete validation passes 930 checks, learner validation passes 832 checks, and 22 protected failure routes are rejected. Module 05 curriculum construction may begin with conditions. No tract is ranked, prioritized, targeted, made eligible, contacted, funded, allocated, implemented, connected to production, or deployed.

## 13. Module 05 brief: Targeting and fairness

- Module ID: `oclc-app5-05`.
- Hours: 16.0.
- Package path: `courses/population-health-equity/modules/05-targeting-fairness/`.
- Specification: `docs/curriculum/courses/APP-5/modules/05-targeting-fairness-spec.md`.
- Decision: which, if any, transparent fictional targeting rule is responsible enough to enter an intervention plan?
- Submission: 15-point targeting and fairness audit.
- Build status: runnable release candidate at module version `0.1.0` and Commons release `0.92.0`.

Learners compare equal allocation, need-based allocation, capacity-aware allocation, and a rule that requires structured community review before inclusion. The fixed fictional resource constraint, eligible areas, public evidence, synthetic capacity, and implementation assumptions remain identical across comparisons.

For every rule, learners report who is included, excluded, delayed, burdened, or unsupported; the benefit sought; possible harm; geographic concentration; group consequences; access and capacity; sensitivity to weights and thresholds; balancing measures; appeal and review routes; and the human owner.

No composite score, SVI rank, model output, or map color may become an automatic allocation. A fairness result must name the decision-specific fairness definition and its tradeoff. Average benefit cannot erase concentrated burden, missing support, inaccessible delivery, or community objection.

The accepted release freezes the complete 287-file Module 04 reference workspace in a 287-row, 59,768-byte handoff manifest with SHA-256 `0670760f650e0d13cfd4c5dc85ab26fdce5779cc86d35b3d3c27d6a3cc7738dd`. The independent `fma-dp-01-fictional-planning-v1` layer uses seed 73055 and adds fictional capacity, travel, staffing, access, review, objection, burden, and owner fields to all 1,597 candidate tracts without deriving them from public modeled prevalence.

Each rule distributes 280 fictional places through 28 equal ten-place teaching awards. The 6,388 rule-tract assignments reconcile to 56 county consequence rows, 76 suppression-preserving group consequence rows, six pairwise overlap rows, and 20 predeclared sensitivity variants. Equal geographic selection reaches all 14 counties but includes 11 language-access gaps. Need-based selection reaches seven counties and includes 26 limited-support estimates. Capacity-aware selection has no selected support or access gaps but retains six high-travel rows and one unresolved objection. Community-review selection reaches 11 counties with no selected support, access, or objection gaps, but retains 12 high-travel rows, one high-burden row, and five staffing-readiness gaps. Two sensitivity variants cannot fill every requested award.

The reference earns 15 of 15 and passes all 26 noncompensable gates. Complete validation passes 2,406 checks, learner validation passes 2,230 checks, and 24 protected failure routes are rejected. Module 06 curriculum construction may begin with conditions using the community-review comparator only as the least unacceptable fictional planning candidate. Real need, consent, priority, eligibility, outreach, funding, allocation, community action, service delivery, intervention-effect estimation, implementation, production connection, and deployment remain prohibited.

## 14. Module 06 brief: Accountable intervention design, monitoring, and embedded ML

- Module ID: `oclc-app5-06`.
- Hours: 16.0.
- Intervention design, monitoring, feedback, and governance block: 8.0 hours.
- Embedded ML extension: 8.0 hours.
- Package path: `courses/population-health-equity/modules/06-intervention-monitoring-embedded-ml/`.
- Specification: `docs/curriculum/courses/APP-5/modules/06-intervention-monitoring-embedded-ml-spec.md`.
- Decision: is the accountable intervention and monitoring design ready for clinician leadership review, and does the fixed area-profile challenger add useful planning questions without taking allocation authority?
- Submission: required zero-point intervention, monitoring, governance, and ML gate for the separate Week 6 checkpoint.
- Point role: required zero-point gate carrying the 25 Module 04 and Module 05 points once.
- Build status: runnable release candidate at module version `0.1.0` and Commons release `0.93.0`.

The intervention block defines the fictional intervention, theory of change, delivery pathway, eligible population, reach, uptake, refusal, access, capacity, implementation fidelity, cost, burden, balancing measures, outcome availability, community feedback, incidents, escalation, pause, revision, stop, and retirement. Each measure has a numerator, denominator, cadence, source, owner, unavailable state, threshold origin, and human response.

Learners propose a later evaluation design but do not estimate a real intervention effect. APP-6 owns causal identification and effect estimation. APP-5 requires a design fit for the question and a clear statement of what evidence would be needed.

The ML extension fits one fixed clustering challenger to the same accepted area-profile matrix. The features, transformations, missing-value rule, scaling, cluster count, seed, stability checks, and interpretation limits are predeclared. Learners test stability across seeds and reasonable scaling choices, inspect support and geographic concentration, and determine whether the grouping contributes useful tailoring questions.

The challenger cannot rank need, select a tract, assign resources, infer individual traits, determine fairness, replace the transparent rule, or bypass community review. A clean cluster display is not an intervention decision. The Week 6 package carries 25 scored points once and adds required intervention, monitoring, accountability, ML, AI, claims, and progression gates.

The accepted release freezes the complete 340-file Module 05 reference workspace and preserves the community-review result as a fictional starting point. A deterministic 280-record dry run exposes five staff-not-ready areas, twelve high-travel areas, one high-burden area, fourteen objection tests, twenty-three incident tests, and six monitoring triggers. All required objections, escalation routes, and pauses remain visible and human-owned.

The fixed KMeans challenger uses 1,597 area profiles, nine declared features, four clusters, seed 73056, four alternate seeds, and three scaling variants. Alternate-seed agreement passes, but the scaling-variant median adjusted Rand value is 0.120 and the carried rows appear in only two clusters. The challenger therefore fails its declared standard and is rejected without tuning.

All 34 Module 06 gates pass. The package may enter construction of the separate Week 6 checkpoint. The fictional intervention is not ready for real implementation, the transparent community-review comparison remains unchanged, and Module 07 remains gated by checkpoint acceptance.

## 15. Module 07 brief: Clinician leadership and equity recommendation

- Module ID: `oclc-app5-07`.
- Hours: 16.0.
- Clinician session design: Joe Joseph, MD, SFHM. Dated public identity is confirmed elsewhere in the Commons; participation and final wording require direct confirmation before alpha.
- Planned package path: `courses/population-health-equity/modules/07-clinician-leadership-equity-recommendation/`.
- Planned specification: `docs/curriculum/courses/APP-5/modules/07-clinician-leadership-equity-recommendation-spec.md`.
- Decision: whether to recommend structured community review of one bounded fictional intervention plan, revise the evidence or plan, refer the question, or stop.
- Submission: final population intervention analytics plan and defense.
- Point role: 35-point final component.
- Build status: planned after Checkpoint 02 acceptance.

Module 07 freezes the accepted Week 3 and Week 6 evidence before adding leadership records. Learners cannot change the population, denominator, geography, standardization, disparity measure, reference group, suppression, map facts, targeting results, resource constraint, intervention assumptions, monitoring facts, or ML result inside the leadership package.

The final package includes an executive decision brief, population and denominator contract, evidence synthesis, disparity interpretation, place and context memo, targeting and fairness audit, intervention analytics design, implementation and monitoring plan, community-facing summary, feedback and recourse plan, stewardship and governance record, disagreement record, accessible evidence appendix, reproducibility audit, responsible-claims audit, AI-use record, and defense.

Leadership must address uncertainty, small numbers, missing and misclassified equity fields, geographic aggregation, ecological limits, stigma, access, capacity, burden, community voice, competing priorities, possible benefit and harm, who can pause or stop the plan, what evidence would permit reconsideration, and what remains outside course authority.

## 16. Three cumulative checkpoint contracts

### Checkpoint 1: Population measures, disparities, and data-limit readiness

- Timing: end of instructional Week 3.
- Course points: 40.
- Package path: `courses/population-health-equity/checkpoints/01-measures-disparities-readiness/`.
- Specification: `docs/curriculum/courses/APP-5/checkpoints/01-measures-disparities-readiness-spec.md`.
- Decision: may the accepted population, denominator, measures, standardization, disparity analysis, and claim limits enter place and targeting work?
- Build status: runnable release candidate at checkpoint version `0.1.0` and Commons release `0.90.0`.

Required evidence includes the Module 01 decision charter and complete source-feasibility release; public versus synthetic data roles; exact PLACES, ACS, and SVI identities; geography and time contract; accountable audience and community-review rights; SQL joins and reconciliation; numerator and denominator tables; crude, specific, direct-standardized, and guided indirect-standardized measures; uncertainty; disparity measures; reference-group sensitivity; missing equity-field profile; selection, linkage, and measurement-bias analysis; support; small-number and suppression rules; accessible exact tables; 40-point score; gates; AI record; claim audit; defense; and progression decision.

The checkpoint counts the 20-point Module 02 and 20-point Module 03 components once. Module 01 adds no points but is a required gate.

The accepted checkpoint freezes 219 complete candidate files from Modules 01 through 03 and verifies 177 nested immutable rows. Its 41,641-byte candidate manifest has SHA-256 `b8331c4fbdddf1403560f0e494c057d2d29944d2b9f15f6273d8b2cabe7b9192`. The reference earns 40 of 40 and passes all 67 inherited and checkpoint gates. Complete validation passes 1,460 checks, learner validation passes 1,446 checks, and 27 deliberate failure routes are rejected.

The reference disposition is `continue with conditions`. Module 04 curriculum construction is permitted for bounded geographic reasoning, one responsible accessible teaching map, and a context memo. Module 05 remains prohibited until Module 04 passes. No checkpoint artifact authorizes a real or intersectional disparity claim, map publication, tract ranking, targeting, eligibility, outreach, allocation, funding, model fitting, real community action, implementation, production connection, or deployment.

Checkpoint acceptance freezes the population, geography, period, source identities, join decisions, synthetic-release identity, denominators, standard population, rate definitions, disparity measures, reference groups, support, missingness, suppression, uncertainty, and claim boundaries. Later modules may add place and intervention evidence but may not silently revise the technical foundation.

### Checkpoint 2: Place, targeting, intervention, and monitoring release

- Timing: end of instructional Week 6.
- Course points: 25.
- Planned package path: `courses/population-health-equity/checkpoints/02-place-targeting-intervention-release/`.
- Planned specification: `docs/curriculum/courses/APP-5/checkpoints/02-place-targeting-intervention-release-spec.md`.
- Decision: is the complete place, targeting, fairness, intervention, monitoring, accountability, and ML case strong enough for clinician leadership review?

Required evidence includes the accepted Week 3 identity; complete TIGER source and geometry checks; spatial-join accounting; tract and county aggregation comparison; small-area stability; ecological and contextual claim audit; responsible accessible map and exact table; non-stigmatizing context memo; fixed fictional resource and capacity constraints; equal, need-based, capacity-aware, and community-review rules; inclusion and exclusion results; fairness definition; differential impact; benefit and harm tradeoffs; access and burden; sensitivity; balancing measures; intervention theory; implementation measures; monitoring plan; feedback and recourse; incidents; escalation, pause, stop, revision, and retirement; fixed clustering challenger; stability and support checks; 25-point score; gates; AI record; claim audit; defense; and progression decision.

The checkpoint counts the 10-point Module 04 and 15-point Module 05 components once. Module 06 adds required intervention, monitoring, accountability, governance, and embedded-ML gates without adding points.

Checkpoint acceptance freezes the public and synthetic evidence, responsible map, targeting comparisons, scored decisions, intervention assumptions, monitoring facts, and ML result before leadership work. No tract is made genuinely eligible, funded, enrolled, or contacted.

### Final checkpoint: Population intervention analytics plan

- Timing: official last day of the assigned half-term.
- Course points: 35.
- Planned package path: `courses/population-health-equity/checkpoints/03-population-intervention-analytics-plan/`.
- Planned specification: `docs/curriculum/courses/APP-5/checkpoints/03-population-intervention-analytics-plan-spec.md`.
- Decision: should the fictional council recommend structured community review of one bounded plan, revise, refer, or stop?

Required evidence includes both accepted checkpoints; immutable candidate manifest; final reproducible repository; executive decision brief; population, denominator, geography, and time contract; source and synthetic identities; evidence synthesis; disparity and uncertainty interpretation; place and context memo; targeting and fairness audit; intervention analytics design; implementation and monitoring plan; evaluation proposal; community-facing summary; language and disability access; feedback and recourse; governance, stewardship, accountability, disagreement, escalation, pause, stop, revision, and retirement; ML interpretation; accessible evidence; technical appendix; AI and responsible-claims audit; 35-point score; gates; defense; reviewer record; reproduction record; conditions; and separate curriculum-package and fictional-planning recommendations.

The final checkpoint adds 35 points once, giving a course total of `40 + 25 + 35 = 100` with no duplication.

## 17. Assessment map and grading rules

| Assessed component | Feedback milestone | Cumulative checkpoint | Course points |
|---|---|---|---:|
| Population measure and denominator build | End of Week 2 | Week 3 | 20 |
| Disparity and data-limit analysis | End of Week 3 | Week 3 | 20 |
| Responsible map and context memo | End of Week 4 | Week 6 | 10 |
| Targeting and fairness audit | End of Week 5 | Week 6 | 15 |
| Population intervention analytics plan and defense | Official half-term end date | Final | 35 |
| Total |  |  | 100 |

Module 01 and Module 06 are required gates. They add no separate points. Module 07 carries the full final 35-point component.

Every scored component uses five recurring criteria:

| Criterion | Meaning |
|---|---|
| Correct | Populations, denominators, joins, rates, standardization, disparity measures, intervals, support, geography, and allocation arithmetic are correct. |
| Reproducible | The accepted public and synthetic releases, code, parameters, manifests, environments, and outputs rerun exactly. |
| Sound population and equity reasoning | The work accounts for source roles, small numbers, missingness, bias, area-level limits, fairness choices, uncertainty, and decision consequences. |
| Clear, accessible, and non-stigmatizing | Tables, figures, maps, summaries, and decisions are usable by the intended audience and do not stigmatize groups or places. |
| Responsible AI and human accountability | Assistance is disclosed and verified; agents do not make equity, targeting, allocation, intervention, or governance decisions. |

A numeric score cannot compensate for a wrong population, numerator, denominator, source, period, geography, standard population, reference group, uncertainty, support decision, suppression, area-level claim, allocation consequence, community role, or human owner.

## 18. Software, reproducibility, and data policy

SQL owns source-shaped staging, key validation, tract and age-group joins, numerator and denominator alignment, aggregation, duplicate detection, unmatched states, rate tables, suppression inputs, allocation scenarios, and monitoring denominators. Python owns source checks, extraction, profiles, standardization, disparity measures, uncertainty, geographic joins, maps and exact alternatives, fairness comparisons, synthetic release generation, ML, manifests, workspaces, and validation. R output is read and interpreted when a supported runtime is available. Git records reviewed versions and immutable handoffs.

Every public source is pinned by publisher, title, landing page, direct resource URL, dataset or table ID, release, vintage, retrieval date, bytes, SHA-256, rows, fields, public-access or rights status, geography, grain, population, period, denominator, uncertainty, transformations, unmatched state, teaching purpose, and claim limit.

A complete accepted upstream release must be inspected before a derived teaching extract is accepted. When a national file is too large to commit, the exact raw identity, acquisition route, full-file validation, extraction code, selected population, derived bytes, derived hash, and reproducible profile remain in the release.

Synthetic data require an upstream or Commons generator identity, version, seed, configuration, field dictionary, relationship and shape tests, row counts, bytes, hashes, known truth, defect registry, explicit synthetic fields, and a statement that the data cannot represent real outcomes or authorize action. The raw synthetic layer remains immutable. Repairs occur only in a derived layer through tested code.

Every module must provide a complete reference, incomplete learner template, instructor material, assessment, rubric, source and data specification, release record, semantic version, deterministic builder, validator, failure self-check, accessible exact outputs, and protected handoff.

## 19. Accessibility, equity, privacy, and responsible claims

Every rate, disparity, map, allocation, cluster, implementation, and monitoring display has an exact table and structured text alternative. Meaning does not rely on color, hover, shape, spatial position, or vision alone. Tables identify units, denominators, periods, geography, uncertainty, suppression, source, unavailable state, and claim limit. Map reading instructions and nonvisual comparisons accompany each assessed map.

Community-facing materials use plain language, respectful place names, accessible headings, descriptive links, readable contrast, captions or transcripts, screen-reader-compatible structure, and a route to request language or disability access. A communication artifact cannot call a population vulnerable, resistant, noncompliant, high risk, or hard to reach without naming the material condition, data source, decision relevance, and limits.

Every equity analysis begins with who is included, excluded, missing, linked, misclassified, suppressed, or unsupported. Learners must state whether a result is an observed count, survey estimate, modeled estimate, synthetic result, contextual measure, or derived teaching scenario. They must distinguish disparity from inequity and state what additional normative, historical, structural, or community evidence supports an inequity claim.

No protected or identifiable patient, resident, employee, clinician, address, program-participant, or restricted record enters the repository or an external agent. Tract-level public data remain public but can still cause harm through careless linkage, small-cell reconstruction, stigmatizing display, or operational targeting. The course applies minimization, aggregation, suppression, access control, and responsible communication even when source data are open.

PLACES does not report observed cases or local intervention effects. ACS and SVI area values do not describe individuals. SVI ranks are release-relative. A spatial association is not a cause. A cluster is not a natural community type. A target score is not entitlement. A fictional intervention result is not program evidence. Course acceptance does not authorize real outreach, allocation, implementation, or policy.

## 20. AI and agent policy

Agents may help retrieve public sources, draft SQL or Python, explain formulas, create tests, review code, suggest alternative interpretations, draft documentation, repair accessibility, and prepare communication alternatives. Learners must disclose the tool, task, instruction, output used, verification, revision, and accountable human.

An agent may not choose or change the population, numerator, denominator, geography, standard population, reference group, suppression rule, disparity claim, equity claim, map framing, targeting criterion, allocation weights, fairness definition, intervention, monitoring trigger, community response, escalation, stop rule, ML feature set, cluster count, final recommendation, or real-world action. It may not receive protected data, fabricate community input, convert unavailable values to zero, restore suppressed cells, hide unmatched geography, invent source provenance, or rewrite a failed gate as passing.

Every agent-produced analytic artifact requires an independent deterministic check against the accepted source, formula, or known truth. The learner owns the submission. Faculty, methods reviewers, community and equity reviewers, clinicians, and the fictional council own review decisions. No agent receives clinical, equity, allocation, policy, or deployment authority.

## 21. Instruction, feedback, and clinician leadership

The course uses short demonstrations, guided source and rate laboratories, denominator studios, disparity clinics, map critiques, geographic failure drills, allocation hearings, community-accountability workshops, monitoring simulations, ML stability exercises, structured peer review, and defense rehearsals.

Feedback milestones occur at the end of Weeks 2, 4, and 5. Formal cumulative feedback occurs at Week 3 and Week 6. Faculty feedback identifies the exact denominator, source, uncertainty, claim, access, or decision issue and the evidence required for repair.

Joe Joseph, MD, SFHM, is the designated clinician-session design for Module 07 under the dated public identity boundary already recorded in the Commons. The course makes no current-employer or current-title claim. Participation, schedule, format, recording permission, biography wording, case wording, and assessment role require direct confirmation before alpha.

The clinician-led block focuses on the human meaning of population evidence: clinical consequences, community trust, uncertainty, competing priorities, resource scarcity, access, burden, implementation feasibility, disagreement, accountability, stopping, and the difference between an analytic recommendation and permission to act.

If the named clinician cannot participate live, an approved recorded case conference plus a qualified clinician-led synchronous defense must preserve the same learning outcomes. The substitution and qualifications require program approval before alpha.

## 22. Reviewer roles and release gates

### Required reviewer coverage before alpha

- APP-5 faculty owner;
- Joe Joseph, MD, SFHM, as designated clinician of record if participation is confirmed;
- population-health physician or public-health clinical reviewer;
- epidemiology reviewer;
- biostatistics, standardization, and disparity-methods reviewer;
- Census and ACS methods reviewer;
- CDC PLACES small-area-estimation reviewer or qualified methods equivalent;
- SVI and social-determinants reviewer;
- GIS, geography, tract-boundary, and spatial-join reviewer;
- community-engagement and community-governance reviewer;
- racial and ethnic equity reviewer;
- language-access and disability-access reviewer;
- resource-allocation, program implementation, and monitoring reviewer;
- privacy and data-governance reviewer;
- responsible-AI and ML reviewer;
- accessibility and communication reviewer; and
- independent reproducer.

One person may cover more than one role only when the record states the qualifications and conflicts. Missing clinical, epidemiology, biostatistics, geographic, community, equity, accessibility, privacy, or independent-reproduction coverage blocks alpha.

### Course release gates

1. The exact source DOCX identity and normalization remain unchanged.
2. Seven modules total 112.5 hours and three checkpoints total 100 points.
3. The first three modules remain applied statistics and population measurement, Modules 04 through 06 remain applied exercises, Module 06 contains an eight-hour ML extension, and Module 07 remains clinician led.
4. Complete accepted PLACES, ACS, SVI, and TIGER releases are acquired, fingerprinted, profiled, and transformed only through tested code.
5. Source grain, population, period, denominator, uncertainty, geography, vintage, and claim limits remain visible.
6. Public and synthetic data roles remain separate, and every synthetic record is unmistakably synthetic.
7. Population, numerator, denominator, geography, time, cadence, affected communities, accountable decision, nonaction, possible benefit, possible harm, review rights, and stop rights are explicit.
8. Crude, specific, direct-standardized, and guided indirect-standardized measures reproduce.
9. Disparity measures, reference-group sensitivity, missingness, selection, linkage, measurement bias, support, uncertainty, small-number handling, and suppression reproduce.
10. Geography, spatial joins, boundary vintage, aggregation sensitivity, ecological limits, small-area stability, and non-stigmatizing communication pass review.
11. Equal, need-based, capacity-aware, and community-review rules use identical accepted evidence and make every inclusion, exclusion, burden, and tradeoff visible.
12. Intervention, implementation, monitoring, feedback, incident, escalation, pause, stop, revision, and retirement records have named human owners.
13. The fixed ML challenger uses predeclared features and settings and cannot rank, select, allocate, infer individual traits, or replace community review.
14. Every display has an exact accessible alternative and every unavailable or suppressed state remains protected.
15. Reference and learner packages differ in assessed work, not in immutable evidence.
16. Deterministic builders, validators, mutation checks, link checks, source checks, and independent reproduction pass.
17. No artifact authorizes real targeting, outreach, allocation, funding, eligibility, implementation, intervention evaluation, or policy.

## 23. Durable paths and build order

Course artifacts:

- source record: `docs/source/app-5-population-health-equity-source-record.md`;
- course specification: `docs/curriculum/courses/APP-5/course-spec.md`;
- course package: `courses/population-health-equity/`;
- course package index: `courses/population-health-equity/README.md`.

Module specification paths:

1. `docs/curriculum/courses/APP-5/modules/01-population-health-decision-spec.md`
2. `docs/curriculum/courses/APP-5/modules/02-population-measures-linked-data-spec.md`
3. `docs/curriculum/courses/APP-5/modules/03-disparities-data-limits-spec.md`
4. `docs/curriculum/courses/APP-5/modules/04-place-evidence-geographic-reasoning-spec.md`
5. `docs/curriculum/courses/APP-5/modules/05-targeting-fairness-spec.md`
6. `docs/curriculum/courses/APP-5/modules/06-intervention-monitoring-embedded-ml-spec.md`
7. `docs/curriculum/courses/APP-5/modules/07-clinician-leadership-equity-recommendation-spec.md`

Checkpoint specification paths:

1. `docs/curriculum/courses/APP-5/checkpoints/01-measures-disparities-readiness-spec.md`
2. `docs/curriculum/courses/APP-5/checkpoints/02-place-targeting-intervention-release-spec.md`
3. `docs/curriculum/courses/APP-5/checkpoints/03-population-intervention-analytics-plan-spec.md`

Each unit is built, validated, versioned, committed, pushed, and remote-verified before the next unit begins. Module 01 pins the tabular public-source identities and geography route. Modules 02 and 03 build Checkpoint 01. Modules 04 through 06 build Checkpoint 02. Module 07 freezes both checkpoints before the final package.

## 24. Known issues and construction acceptance

Human decisions and evidence still required before alpha:

- assign the official APP-5 section and half-term dates before publishing due dates;
- independently review the accepted PLACES, ACS, SVI, and TIGER source identities, vintages, methods, geography, transformations, rights, and claim limits;
- confirm the final population, diabetes-prevention framing, denominator, standard population, age groups, synthetic event design, disparity measures, reference groups, suppression rules, and uncertainty methods;
- confirm the geographic levels, tract and county aggregation exercise, crosswalk rules, small-area stability method, and map review criteria;
- confirm the fictional resource constraint, capacity design, targeting alternatives, fairness definitions, benefit and harm assumptions, balancing measures, and community-review rights;
- confirm the intervention theory, implementation measures, monitoring cadence, evaluation proposal, feedback, recourse, escalation, pause, stop, revision, and retirement rules;
- independently review the fixed clustering challenger, feature set, transformations, missingness, scaling, cluster count, seed, stability tests, prohibited uses, and rejection rule;
- confirm Joe Joseph's participation, schedule, format, recording permission, biography wording, case wording, and assessment role;
- name the faculty, clinical, epidemiology, biostatistics, Census, PLACES, SVI, GIS, community, equity, language, disability, implementation, privacy, accessibility, responsible-AI, ML, and independent-reproduction reviewers; and
- complete clean human reproduction and final release authorization.

Construction acceptance for this course-level unit:

- [x] The exact DOCX source is fingerprinted in both archives.
- [x] Seven distinct modules total 112.5 hours.
- [x] The assessment content is normalized into 40, 25, and 35 checkpoint points without duplication.
- [x] Modules 01 through 03 form the applied statistics and population-measurement block.
- [x] Modules 04 through 06 form the application and exercise block.
- [x] Module 06 contains eight hours of accountable intervention work and eight hours of embedded ML.
- [x] Module 07 is clinician led and makes no unconfirmed participation claim.
- [x] APP-5 has distinct ownership and does not replace either visualization course.
- [x] The public evidence, synthetic evidence, decision, community-accountability, and real-world authority boundaries are explicit.
- [x] The Module 01 build may proceed under the separate APP-5 Module 01 plan.
