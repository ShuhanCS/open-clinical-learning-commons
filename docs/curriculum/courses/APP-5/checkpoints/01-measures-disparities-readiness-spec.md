# APP-5 Checkpoint 01: Population measures, disparities, and data-limit readiness

## 1. Checkpoint identity and place in the course

- Checkpoint ID: `oclc-app5-cp01`.
- Course: APP-5, Data for Population Health and Equity.
- Due point: end of instructional Week 3.
- Checkpoint version: `0.1.0`.
- Commons release: `0.90.0`.
- Accepted modules: APP-5 Modules 01, 02, and 03.
- Course points: 40.
- Point source: Module 02 contributes 20 points once and Module 03 contributes 20 points once.
- Required zero-point gate: Module 01.
- Decision: whether the accepted population, denominator, measures, standardization, disparity analysis, and claim limits may enter Module 04 place-based curriculum work.
- Package: `courses/population-health-equity/checkpoints/01-measures-disparities-readiness/`.

This is APP-5's first cumulative release gate. It joins the population decision, public-source feasibility, denominator, rate construction, standardization, synthetic equity margins, disparity measures, reference sensitivity, missingness, representation, bias, small-number rules, suppression, and responsible claim into one progression decision.

The checkpoint does not create a new analysis or rescore accepted work. A learner cannot repair a source, change a denominator, choose another standard population, revise a reference, fill an unavailable result, recover a suppressed cell, or strengthen a claim inside the checkpoint. A material correction returns to the owning module, receives a reviewed version, reproduces, and enters a rebuilt checkpoint.

The published academic calendar controls the actual due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The Week 3 label describes an instructional checkpoint. It does not replace the official dates assigned to the APP-5 section.

## 2. Decision, readers, and required answer

The checkpoint asks:

> May the accepted `FMA-DP-01` population, denominator, measures, standardization, disparity analysis, and claim limits enter Module 04 place-based curriculum work?

Primary readers are the fictional `FMA-DP-01` population-health planning council, the APP-5 faculty owner, a population-health clinician, an epidemiologist, a biostatistician, Census and ACS methods reviewers, PLACES and SVI reviewers, a GIS reviewer, race and ethnicity standards reviewer, language-access reviewer, disability reviewer, community reviewer, equity reviewer, privacy reviewer, accessibility reviewer, responsible-AI reviewer, independent reproducer, and the future Module 04 analyst.

The allowed disposition is `continue`, `continue with conditions`, `revise`, or `refer`. A continuing answer must name:

- all three accepted module identities;
- all 219 candidate files and 177 nested immutable rows;
- the 40-point source and no-double-counting rule;
- all 45 inherited and 22 checkpoint gates;
- the fictional population decision, accountable audience, nonaction, community rights, and stop rights;
- exact PLACES, ACS, and SVI identities and their distinct evidence roles;
- the adult denominator, age bands, synthetic numerator, join accounting, and standard population;
- crude, age-specific, direct, and guided indirect measures with uncertainty and support;
- available, unavailable, and sparse-support results;
- the three separate synthetic marginal dimensions and their non-intersectional boundary;
- absolute, relative, summary, and reference-sensitive disparity results;
- missing race, ethnicity, language, disability, and geography results;
- selection, linkage, and measurement-bias findings;
- primary and complementary suppression and non-reconstruction evidence;
- the exact score and every failed gate, if any;
- reviewer, condition, reproduction, claims, and AI records;
- the precise Module 04 permission and Module 05 gate; and
- every prohibited claim or action.

A continuing decision opens Module 04 curriculum construction only. It does not make a real Massachusetts disparity claim, authorize a map inside the checkpoint, rank a tract, choose a target, define eligibility, contact a resident, allocate a resource, fund a program, fit a model, estimate an intervention effect, authorize real community action, implement, connect to production, or deploy.

## 3. Accepted Module 01 population and public-source package

The checkpoint accepts Module 01 only as:

- module ID `oclc-app5-01`;
- version `0.1.0`;
- Commons release `0.87.0`;
- 27 assembled reference files;
- 16 immutable manifest rows;
- manifest size 1,907 bytes;
- manifest SHA-256 `65ea81f391ed426f63e84593588d57542e827f89f2493aa0b3a2f8b1d9a2b0e9`;
- 12 of 12 decision gates passing;
- progression `continue with conditions`; and
- zero checkpoint points.

`FMA-DP-01` is an explicitly fictional Massachusetts adult diabetes-prevention planning review. The accountable audience is a fictional planning council. Real Massachusetts census-tract identifiers support reproducibility and source teaching. They do not link the case to a real program, agency, resident, patient, outreach list, funding decision, or community action.

The accepted public releases are:

| Source | Accepted rows | Fields | Role | Limit |
|---|---:|---:|---|---|
| CDC PLACES 2025 tract release, diabetes measure year 2023 | 1,597 | 24 | modeled adult diabetes prevalence and PLACES context | not observed cases, individual risk, program effect, eligibility, or allocation authority |
| 2020-2024 ACS five-year B01001 | 1,620 | 100 | tract population and age-by-sex denominator estimates with 90 percent margins | survey estimates, not events or individual records |
| CDC/ATSDR SVI 2022 Massachusetts | 1,613 | 158 | area context and source-feasibility evidence | not an individual trait, causal effect, automatic target, or funding rule |

The complete source metadata are available at:

- https://data.cdc.gov/api/views/cwsq-ngmh
- https://data.census.gov/table/ACSDT5Y2024.B01001
- https://api.census.gov/data/2024/acs/acs5/groups/B01001.json
- https://atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html

All 1,597 PLACES tracts match ACS and SVI. The three-source union contains 1,620 tracts. Every source-specific difference remains visible. Unmatched rows are preserved and explained rather than silently removed.

The release inventories 282 fields. Its source-inventory SHA-256 is `1392a8a84047cf9725daf4053dbc0ac6efdbbe1b93eb6e9ed1e0c8074b6e89dd`, field-inventory SHA-256 is `d65fb0bbde925e17e2b94ee362e43c1320d4f10467241f77cd260f50329854f7`, and join-feasibility SHA-256 is `2fc7811fc1f6350fb65581a5d946d073039b05a72006a9dd30ad829005cde1e6`.

Module 01 remains a required gate because later results depend on its population, denominator roles, geography, periods, source roles, accountable audience, community-review rights, claim limits, and stop rights. It adds no points.

## 4. Accepted Module 02 population-measure package

The checkpoint accepts Module 02 only as:

- module ID `oclc-app5-02`;
- version `0.1.0`;
- Commons release `0.88.0`;
- 72 assembled reference files;
- 57 immutable manifest rows;
- manifest size 7,588 bytes;
- manifest SHA-256 `330b4e9ba5071ad4529d46f4af5b15555e8db84ef1718de2a8de42d0aa76a4b0`;
- score 20 of 20;
- 15 of 15 measure gates passing; and
- progression `continue with conditions`.

The deterministic synthetic release is `fma-dp-01-measures-v1`, generator version `0.1.0`, seed `73052`, and period `2024`. Its source manifest has SHA-256 `9915aeb15f62d88a52cfa6304d211a4fd092d33c11e73cd5d63a14d64946823d`.

The release contains:

- 1,597 matched measure tracts;
- five adult age bands;
- 7,985 denominator rows;
- 7,985 generated event rows;
- 5,679,768 adult denominator units;
- 283,614 synthetic planning-need events; and
- 41 zero-denominator tract-age cells retained in the source structure.

The synthetic generator uses the ACS denominator structure, fixed age probabilities, a seeded fictional tract effect, and deterministic rounding. It does not use PLACES prevalence, SVI values, diagnoses, intervention outcomes, community preference, eligibility, or allocation signals.

The accepted measure release has:

| Evidence | Accepted count |
|---|---:|
| Union tracts retained | 1,620 |
| Measure tracts | 1,597 |
| Available age-specific rates | 7,944 |
| Available direct standardized rates | 1,576 |
| Unavailable direct standardized rates | 21 |
| Guided indirect-standardization cases | 80 |
| Separate public modeled-prevalence rows | 1,597 |
| SQL checks passing | 30 |
| Source-reconciliation checks passing | 8 |

Every rate preserves its numerator, denominator, multiplier, age band, geography, period, source, standard population, uncertainty, support state, suppression state, and claim limit. An unavailable value stays unavailable. Sparse support routes to the declared guided indirect exercise rather than an improvised direct result.

The direct standard is the ACS 2020-2024 adult population across the 1,597 matched tracts. Its five weights total one. The ACS approximate sum margin omits covariance and remains labeled as an approximation.

The official methods routes include:

- https://www.census.gov/content/dam/Census/programs-surveys/acs/guidance/training-presentations/20180418_MOE_Webinar_Transcript.pdf
- https://www.cdc.gov/nchs/hus/sources-definitions/age-adjustment.htm
- https://www.cdc.gov/pcd/issues/2010/jan/09_0054.htm

PLACES remains modeled prevalence. The generated event count remains synthetic. The checkpoint can compare their roles but cannot combine them into a false observed local measure.

The Module 02 score contributes 20 checkpoint points exactly once.

## 5. Accepted Module 03 disparity and data-limit package

The checkpoint accepts Module 03 only as:

- module ID `oclc-app5-03`;
- version `0.1.0`;
- Commons release `0.89.0`;
- 120 assembled reference files;
- 104 immutable manifest rows;
- manifest size 15,465 bytes;
- manifest SHA-256 `d9591e028ba49d79762d444d769821dc21055a712aceda3f501c0e31bb7d24b8`;
- score 20 of 20;
- 18 of 18 disparity gates passing; and
- progression `continue with conditions`.

Module 03 freezes the complete Module 02 evidence through a 73-row handoff manifest with SHA-256 `f5e84b251143edeb65b68d816a57492755083d8bc57c73e6bdaede381b933ef1`.

The deterministic equity release is `fma-dp-01-equity-v1`, generator version `0.1.0`, seed `73053`, and period `2024`. Its source manifest has SHA-256 `c3f7549f6fcc25e0bfd5f074a7f936e519a0bd7f9459452da903c653aee28384`.

The source contains three separate marginal dimensions:

1. combined race and ethnicity;
2. primary language; and
3. disability status.

The dimensions contain 19 declared groups, 151,715 tract-age-dimension-group rows, and a separate 7,985-row field-completeness audit. Each dimension independently reconciles to 5,679,768 denominator units and 283,614 synthetic events.

The dimensions are not joint person records. They cannot be joined to estimate an intersectional group, infer a person's combined traits, or support an intersectional action.

The accepted analysis contains:

| Evidence | Rows |
|---|---:|
| Group-age rates | 110 |
| Standardized group rates | 22 |
| Reference comparisons | 32 |
| Summary disparity records | 6 |
| Missingness results | 5 |
| Representation records | 19 |
| Bias register | 8 |
| Query checks | 36 |
| Source-reconciliation checks | 12 |

The analysis reports rate difference, rate ratio, one summary disparity measure, support, intervals, and both declared and overall references. Absolute and relative measures answer different questions. A reference choice changes the comparison and interpretation, not the source observation.

The completeness audit records:

| Field | Missing count | Interpretation boundary |
|---|---:|---|
| Race | 6,000 | source capture and classification remain incomplete |
| Ethnicity | 7,578 | source capture and classification remain incomplete |
| Primary language | 5,314 | language capture is incomplete and not an access assessment |
| Disability status | 8,376 | disability capture is incomplete and not an access assessment |
| Tract geography | 0 | conditioned on the accepted linked measure frame, not proof of perfect geographic capture |

The eight-row register separates selection, linkage, and measurement bias. Each row names an evidence route, consequence, owner, and mitigation or review need. A bias register makes the limit visible. It does not remove the bias.

The official methods routes are:

- https://www.cdc.gov/nchs/healthy-people/hp2030/methods.html
- https://stacks.cdc.gov/view/cdc/6654/cdc_6654_DS1.pdf
- https://www.cdc.gov/united-states-cancer-statistics/technical-notes/suppression.html
- https://www.cdc.gov/rdc/media/pdfs/2026/01/uscs-rdc-datadictionary-cdc-nov2024.pdf
- https://www.govinfo.gov/content/pkg/FR-2024-03-29/pdf/2024-06469.pdf
- https://aspe.hhs.gov/sites/default/files/documents/20f1e2b607af3f3b46d7668f337b679b/dhhs-implementation-guidance-data-collection-standards.pdf

The Module 03 score contributes 20 checkpoint points exactly once.

## 6. Point architecture and no-double-counting rule

The source course has two 20-point Week 3 components:

| Source component | Owning module | Points | Checkpoint treatment |
|---|---|---:|---|
| Population measures, linkage, standardization, uncertainty, and interpretation | Module 02 | 20 | counted once |
| Disparities, reference sensitivity, missingness, bias, suppression, and responsible claim | Module 03 | 20 | counted once |
| Population decision and source-feasibility gate | Module 01 | 0 | required, not scored |
| Cumulative checkpoint review | Checkpoint 01 | 0 | required gate, no new course points |
| Total |  | 40 | exact Week 3 total |

`checkpoint-score.csv` carries the five accepted Module 02 criteria:

| Criterion | Points |
|---|---:|
| Population, age-band, numerator, denominator, and linkage logic | 4 |
| Crude and age-specific rates | 4 |
| Direct and indirect standardization | 4 |
| Uncertainty, support, and evidence separation | 4 |
| Reproducibility, interpretation, and handoff | 4 |
| Module 02 subtotal | 20 |

It also carries the five accepted Module 03 criteria:

| Criterion | Points |
|---|---:|
| Group rates, support intervals, and standardization | 4 |
| Absolute, relative, summary, and reference-sensitivity measures | 4 |
| Missingness, representation, selection, linkage, and measurement bias | 4 |
| Primary and complementary suppression with non-reconstruction | 4 |
| Responsible claim, reproducibility, AI record, and progression | 4 |
| Module 03 subtotal | 20 |

The reference total is 40 of 40. A numeric passing threshold is 28 of 40. All gates remain noncompensable. The checkpoint cannot add a criterion, award points for defense or review, average a failed gate into a passing score, or count a component twice.

## 7. Cumulative evidence index and chain of custody

`evidence-index.csv` has one ordered row for each accepted module. Every row records:

- module ID and title;
- module and Commons versions;
- complete assembled file count;
- nested immutable manifest rows, bytes, and SHA-256;
- checkpoint points;
- inherited gate result;
- accepted progression;
- accepted decision; and
- cumulative role.

The checkpoint builder calls each owning module's existing `build_workspace.py` and requests the complete reference workspace. It verifies the expected file count, nested manifest row count, manifest byte count, and manifest SHA-256 before copying a candidate file.

The cumulative candidate contains:

| Candidate directory | Complete files | Nested immutable rows | Role |
|---|---:|---:|---|
| `candidate/module-01/` | 27 | 16 | population decision and public-source gate |
| `candidate/module-02/` | 72 | 57 | denominator, measures, standardization, and 20-point component |
| `candidate/module-03/` | 120 | 104 | disparities, limits, suppression, and 20-point component |
| Total | 219 | 177 | frozen Week 3 candidate |

`candidate-manifest.csv` fingerprints every candidate file with its relative path, bytes, SHA-256, source module, source version, and role. Candidate rows are sorted. Learner and reference packages receive the same candidate and manifest.

The outer candidate manifest is 41,641 bytes with SHA-256 `b8331c4fbdddf1403560f0e494c057d2d29944d2b9f15f6273d8b2cabe7b9192`.

The outer manifest protects all 219 complete workspace files, including the accepted reference records and the three nested manifests. The nested manifests independently protect 177 source, generated data, output, handoff, SQL, and control artifacts.

A changed candidate invalidates the checkpoint. The correction belongs in the owning module.

## 8. Integrated measures and disparities readiness review

`measures-disparities-readiness-review.md` is the main cumulative narrative. It answers one progression question rather than pasting three module summaries together.

The review reconciles these layers:

| Layer | Accepted evidence | Limit that stays visible |
|---|---|---|
| Population decision | fictional adult population, accountable council, nonaction, review rights, and stop rights | no real council or action authority |
| Public sources | complete PLACES, ACS, and SVI tract releases | distinct modeled, denominator, and contextual roles |
| Denominator and numerator | five adult age bands, 5,679,768 denominator units, and 283,614 synthetic events | generated events are not observed cases |
| Measures | crude, age-specific, direct, and guided indirect results | unsupported and unavailable states remain explicit |
| Standardization | one declared standard population | comparison tool, not a real risk or need ranking |
| Equity margins | three separate dimensions and 19 groups | no intersectional or person-level inference |
| Disparities | absolute, relative, summary, and reference-sensitive results | fictional synthetic teaching finding only |
| Completeness | five fields with exact missingness | conditioned geography result is not capture proof |
| Bias | selection, linkage, and measurement register | visibility does not remove bias |
| Suppression | primary, complementary, unavailable, and non-reconstruction states | no zero filling or published tract total |

The public PLACES value, synthetic event rate, and synthetic equity margin are not interchangeable. They can share a population and chain of custody while retaining separate meanings.

The review cannot change a result to make the story cleaner. It cannot convert blank to zero, treat a sparse direct rate as available, substitute a new reference, join separate margins, explain a difference causally, or infer that an area-level pattern describes an individual.

## 9. Measure, standardization, uncertainty, and support readiness

The checkpoint freezes the adult denominator and all measure definitions before geographic work begins.

The adult age bands are the five accepted Module 02 bands. The standard population is the accepted 5,679,768-unit ACS adult distribution across the 1,597 matched tracts. The rate multiplier is 100,000.

Every rate must preserve:

- numerator;
- denominator;
- age band or standardized status;
- standard weight when applicable;
- period;
- geography;
- source;
- interval or margin method;
- support state;
- availability state; and
- claim boundary.

The 1,576 available direct standardized rates may enter later geographic stability work. The 21 unavailable direct rates remain unavailable. The 80 guided indirect cases remain a bounded instructional exercise and cannot be silently promoted to the same interpretation as the direct rate.

Module 04 may add geometry and study how an accepted measure behaves across geographic representations. It cannot recalculate the denominator, choose a different standard, alter an interval, fill a sparse cell, or replace an unavailable value.

Public PLACES modeled prevalence remains separate. A map may eventually show a declared public or synthetic teaching measure, but the map must name which one it shows and carry the corresponding source and claim limit.

## 10. Disparity, reference, missingness, representation, and bias readiness

The checkpoint freezes both the measure and the comparison rule.

The accepted analysis distinguishes:

- absolute disparity through rate difference;
- relative disparity through rate ratio;
- pairwise comparison to a declared reference;
- comparison to the overall rate;
- one summary disparity measure; and
- reference sensitivity.

No single measure is treated as the complete account. Absolute and relative scales can move differently. A favorable or adverse orientation, reference choice, group weighting, and summary rule affect interpretation.

The reference package retains all 32 comparisons and six summary rows. It does not choose the largest difference as a target. It does not call the reference group ideal, biologically normal, deserving, or causally protective.

Missingness and representation remain part of the result. The race, ethnicity, language, and disability missing counts cannot be hidden by reporting only complete cases. The conditioned geography count cannot be described as complete upstream capture.

The 19 representation records identify the support available for every declared group. A missing or sparse group is not a nonexistent group. A result with limited support cannot be strengthened by a more confident label.

The bias register separates:

1. selection into the teaching frame;
2. linkage across tract and source evidence; and
3. measurement and classification of the recorded field.

Module 04 may ask how place, aggregation, missing geometry, ecological context, and mapping choices interact with these accepted limits. It cannot claim that geography explains a group difference or that an area characteristic belongs to a person.

## 11. Small numbers, suppression, privacy, and responsible claims

The accepted primary suppression thresholds are:

- fewer than 16 synthetic events; or
- denominator below 100.

Primary suppression protects 19,742 tract-group cells. Complementary suppression protects another 1,488 cells when a lone primary suppression could be recovered through subtraction.

The 30,343-row publication table contains:

- 9,113 publishable rows;
- 19,742 primary suppressed rows;
- 1,488 complementary suppressed rows; and
- 21,230 total suppressed rows.

All 4,791 tract-dimension audits pass. Protected rows retain a group key, status, and reason. Their denominator, event count, rate, and interval remain blank. Blank means unavailable, not zero.

Tract totals are not published when they could reveal a protected cell. A subtotal, alternate grouping, derived percentage, chart label, tooltip, downloadable table, or map cannot reintroduce a hidden value.

The strongest supported checkpoint claim is:

> The accepted fictional synthetic evidence may enter Module 04 place-based curriculum construction with conditions, while every disparity, missingness, bias, support, and suppression limit remains explicit.

The package does not support:

- a real Massachusetts disparity;
- an intersectional disparity;
- a biological or causal explanation;
- a deficit label for a community;
- a real map or tract ranking inside the checkpoint;
- targeting, eligibility, outreach, allocation, or funding;
- model fitting or intervention-effect estimation;
- real community action;
- implementation or production connection; or
- deployment.

## 12. Noncompensable inherited and checkpoint gates

The inherited gate totals are:

- Module 01: 12 of 12;
- Module 02: 15 of 15; and
- Module 03: 18 of 18.

Checkpoint 01 adds 22 integrity gates:

1. all three accepted module identities and complete reference workspaces are exact;
2. the 219-row candidate manifest is sorted and complete;
3. all 177 nested immutable rows match their accepted manifests;
4. PLACES, ACS, and SVI identities and public roles remain exact;
5. the fictional population, denominator roles, geography, time, audience, nonaction, and community rights remain exact;
6. all 1,620 union tracts, 1,597 measure tracts, joins, unmatched states, and reconciliations remain visible;
7. the five age bands, denominator, numerator, multiplier, and standard population remain exact;
8. all uncertainty, support, direct availability, and guided indirect states remain exact;
9. public modeled prevalence remains separate from synthetic event evidence;
10. the three marginal dimensions remain separate and cannot support intersectional inference;
11. all 19 groups and declared and overall references remain exact;
12. all group-age, standardized, pairwise, summary, and sensitivity results reproduce;
13. all five missingness and 19 representation results remain visible;
14. all eight selection, linkage, and measurement-bias records remain visible;
15. primary and complementary suppression counts and rules reproduce;
16. all 21,230 suppressed values remain blank and all 4,791 non-reconstruction audits pass without tract totals;
17. Module 01 has zero points and Modules 02 and 03 have 20 points once each;
18. all 45 inherited gates pass;
19. the score is 40 and all 22 checkpoint gates pass;
20. defense, review, conditions, reproduction, AI, and claims records are complete;
21. the supported claim remains fictional and non-intersectional; and
22. progression grants only bounded Module 04 curriculum construction while every real-world action route remains prohibited.

All 67 inherited and checkpoint gates must pass. A failed gate forces `revise` or `refer` regardless of the score.

## 13. Learner records, defense, review, and conditions

Learner and reference packages contain 12 checkpoint records:

| Record | Required content |
|---|---|
| `README.md` | decision, use, points, gates, progression, and authority boundary |
| `evidence-index.csv` | module identities, nested manifests, points, gates, progressions, decisions, and roles |
| `measures-disparities-readiness-review.md` | one integrated readiness decision with exact evidence and limits |
| `checkpoint-score.csv` | ten criteria, two 20-point subtotals, and the 40-point total |
| `checkpoint-gates.csv` | 22 ordered gates with status, evidence, and owner |
| `responsible-claims-audit.md` | strongest supported claims and every prohibited claim or action |
| `checkpoint-defense.md` | 15 ordered answers, each with evidence and a limit |
| `reviewer-record.md` | construction review and 17 required named review roles |
| `conditions-register.csv` | 12 conditions with owner, verifier, status, and blocking effect |
| `reproducibility-check.md` | candidate, nested manifests, points, gates, builds, mutations, and human reproduction |
| `ai-use.md` | complete accountable agent-use record |
| `progression-decision.md` | score, gates, permission, scope, conditions, and prohibitions |

Every learner record contains `REPLACE` and remains incomplete by design. Every reference record is complete and contains no placeholder.

The 15 defense questions ask the learner to explain:

1. which releases are frozen;
2. how the 40 points are counted;
3. what population and source roles remain in scope;
4. what denominator and linkage are accepted;
5. what rates and standardization support;
6. how public and synthetic measures stay separate;
7. what the synthetic equity layer contains;
8. what disparity and reference evidence is accepted;
9. what missingness and representation limits remain;
10. how selection, linkage, and measurement bias are handled;
11. how suppression prevents reconstruction;
12. what responsible disparity statement is supported;
13. what cumulative evidence conflict was resolved;
14. what Module 04 may do; and
15. what remains prohibited and unresolved.

Each answer requires an `Answer:`, `Evidence:`, and `Limit:` line. A polished answer without traceable evidence or an authority boundary is incomplete.

The reviewer record separates completed construction checks from 17 named human review roles still pending before alpha. No unconfirmed person is represented as having completed a review.

The 12 open conditions cover official dates, source roles, denominator and measure methods, group labels and standards, references and uncertainty, missingness and representation, the bias register, suppression and privacy, community rights, accessibility, responsible AI, and clean independent reproduction. Each has an owner, verifier, open status, and alpha block.

## 14. Deterministic assembly contract

`build_checkpoint.py` uses only the Python standard library and the accepted module builders.

Assembly order:

1. refuse an existing target;
2. verify all checkpoint controls and the chosen learner or reference record set;
3. copy the eight immutable checkpoint controls;
4. copy the 12 learner or reference records;
5. build the complete Module 01 reference workspace;
6. require 27 files, 16 nested rows, 1,907 manifest bytes, and the accepted manifest SHA-256;
7. build the complete Module 02 reference workspace;
8. require 72 files, 57 nested rows, 7,588 manifest bytes, and the accepted manifest SHA-256;
9. build the complete Module 03 reference workspace;
10. require 120 files, 104 nested rows, 15,465 manifest bytes, and the accepted manifest SHA-256;
11. copy all 219 candidate files under their module directories;
12. write the sorted outer candidate manifest; and
13. require exactly 240 assembled files.

The assembled workspace has:

- eight immutable checkpoint controls;
- 12 editable checkpoint records;
- 219 frozen candidate files; and
- one candidate manifest.

Total: 240 files.

Two reference builds must return the same report and byte-identical candidate manifest. A learner build must receive the same candidate manifest. Candidate-file hashes must match between independent builds. An existing target must be rejected.

The accepted candidate manifest is 41,641 bytes with SHA-256 `b8331c4fbdddf1403560f0e494c057d2d29944d2b9f15f6273d8b2cabe7b9192`.

## 15. Validation, copied execution, and mutation rejection

`validate_checkpoint.py` uses only the Python standard library.

Complete reference validation performs 1,460 checks. Learner validation performs 1,446 checks. Validation covers:

- exact file inventory;
- all 219 outer candidate fingerprints, roles, and source identities;
- all three nested manifests and 177 nested fingerprints;
- checkpoint contract, release, version, points, gates, package, and authority;
- exact Module 01 case, source inventory, field inventory, and join contract;
- exact Module 02 denominator, numerator, rate, standardization, query, reconciliation, score, and gate contracts;
- exact Module 03 source, disparity, missingness, suppression, query, reconciliation, score, and gate contracts;
- evidence index and no-double-counting rule;
- the 13-row checkpoint score file;
- 22 ordered checkpoint gates;
- every required cumulative result and claim limit;
- 15 defense answers with evidence and limits;
- 17 reviewer roles and 12 conditions;
- reproduction routes;
- AI accountability;
- progression, Module 04 scope, Module 05 gate, and all authority prohibitions; and
- absence of personal absolute paths.

The validator copied inside the assembled workspace validates that workspace successfully. The package therefore does not depend on an unshipped local validator.

The self-check rejects 27 deliberate failure routes:

1. changed candidate;
2. missing candidate;
3. changed Module 01 points;
4. duplicated Module 02 points;
5. duplicated Module 03 points;
6. wrong checkpoint total;
7. failed inherited gate;
8. failed checkpoint gate;
9. merged public and synthetic evidence;
10. changed denominator;
11. changed reference result;
12. missing interval;
13. hidden conditioned missingness;
14. intersectional claim from separate margins;
15. suppressed blank relabeled as zero;
16. published total that makes suppression reconstructable;
17. real disparity claim;
18. mapping or ranking authority;
19. targeting or allocation authority;
20. incomplete defense;
21. missing construction reviewer field;
22. missing condition;
23. missing AI accountability field;
24. invalid progression permission;
25. implementation authority;
26. deployment authority; and
27. missing reproduction route.

Submitting learner prompts as a complete reference package is also rejected.

## 16. Progression contract and Module 04 handoff

The reference disposition is:

- checkpoint score `40 of 40`;
- Module 01 decision gates `12 of 12 pass`;
- Module 02 measure gates `15 of 15 pass`;
- Module 03 disparity gates `18 of 18 pass`;
- checkpoint integrity gates `22 of 22 pass`;
- failed gates `none`;
- progression `continue with conditions`;
- Module 04 permission `permitted for curriculum construction`;
- Module 05 permission `prohibited until Module 04 passes`; and
- every real-world claim and action route `prohibited`.

Module 04 receives:

- the fictional population decision, accountable audience, community rights, and claim boundary;
- exact PLACES, ACS, and SVI identities and source roles;
- the accepted 1,620-tract union and 1,597-tract measure frame;
- the five age bands, 5,679,768 denominator units, and 283,614 synthetic events;
- crude, age-specific, direct, and guided indirect measure evidence;
- the standard population, uncertainty, support, and unavailable states;
- the three separate marginal dimensions and 19 groups;
- 110 group-age rates, 22 standardized rates, 32 reference comparisons, and six summaries;
- five missingness results, 19 representation records, and eight bias records;
- all primary, complementary, unavailable, and non-reconstruction states;
- the 40-point Week 3 score;
- all 12 open conditions; and
- every claim and action prohibition.

Module 04 may:

- acquire the complete accepted 2024 Massachusetts tract geometry;
- verify geometry source identity, vintage, keys, coordinate reference system, missing rows, extra rows, and invalid shapes;
- preserve every spatial join state;
- compare tract and county aggregation;
- study small-area stability and aggregation sensitivity;
- distinguish contextual from compositional evidence;
- teach ecological fallacy and non-stigmatizing place language;
- create one responsible accessible teaching map with an exact table and text alternative; and
- write a place and context memo for later review.

The fixed geometry routes are:

- https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html
- https://www.census.gov/cgi-bin/geo/shapefiles/index.php?layergroup=Census+Tracts&year=2024

Module 04 may not:

- change the population, denominator, numerator, standard population, rate, disparity, reference, missingness, bias, or suppression result;
- map a protected or reconstructable value;
- map a joint intersectional result from separate margins;
- rank tracts or communities;
- choose a target or eligibility rule;
- begin Module 05 targeting or allocation work early;
- infer an individual trait from an area value;
- claim a causal place effect;
- authorize outreach, allocation, funding, or intervention;
- fit a model or estimate an intervention effect;
- implement, connect, or deploy.

## 17. Release, review, and exit criteria

Checkpoint version `0.1.0` exits as a runnable release candidate at Commons `0.90.0` only when:

- two independent reference assemblies match;
- learner and reference candidates are identical;
- existing-target refusal passes;
- all 219 outer fingerprints match;
- all three nested manifests and 177 immutable rows match;
- the candidate manifest is exactly 41,641 bytes with the accepted SHA-256;
- the copied validator passes;
- reference validation passes 1,460 checks;
- learner validation passes 1,446 checks;
- all 27 deliberate failure routes are rejected;
- learner prompts are rejected as complete;
- the score is 40 with no duplication;
- all 67 inherited and checkpoint gates pass;
- all unavailable and suppressed states remain protected;
- the claim remains fictional and non-intersectional;
- the defense has 15 complete answers;
- the reviewer and 12-condition records are complete;
- progression matches the bounded Module 04 permission;
- Module 05 remains gated; and
- every real-world action route remains prohibited.

Named APP-5 faculty, population-health clinical, epidemiology, biostatistics, Census and ACS, PLACES, SVI, GIS, race and ethnicity standards, language-access, disability, community, equity, privacy, accessibility, responsible-AI, and independent-reproduction reviews remain required before alpha.

The official APP-5 section must map this checkpoint to the published academic calendar before assigning a due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The release is a curriculum construction candidate. It is not permission to make a real disparity claim, publish a map from the checkpoint, rank a tract, target a community, determine eligibility, contact a resident, allocate a resource, fund a program, fit a model, estimate intervention effects, implement, connect to production, or deploy.
