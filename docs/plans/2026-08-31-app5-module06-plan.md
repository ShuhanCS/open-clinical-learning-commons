# APP-5 Module 06 build plan

## 1. Unit identity

- Course: APP-5, Data for Population Health and Equity.
- Module: 06, Accountable intervention design, monitoring, and embedded ML.
- Module ID: `oclc-app5-06`.
- Module version: `0.1.0`.
- Commons release target: `0.93.0`.
- Hours: 16.0.
- Intervention, monitoring, feedback, and governance block: 8.0 hours.
- Embedded ML block: 8.0 hours.
- Point role: required zero-point gate carrying the accepted 10 Module 04 points and 15 Module 05 points once into the separate Week 6 checkpoint.

## 2. Decision

The module asks whether one accountable fictional intervention and monitoring design is complete enough for Week 6 checkpoint review, and whether a fixed area-profile clustering challenger contributes useful tailoring questions without taking authority from the transparent community-review rule.

Curriculum-package acceptance and intervention readiness are separate decisions. A technically complete package may advance with conditions while the fictional intervention remains unready for any implementation exercise.

## 3. Accepted starting point

The build freezes the complete 340-file APP-5 Module 05 reference workspace. It does not recompute or repair the accepted public evidence, fictional planning source, resource contract, four base rules, 6,388 assignments, fairness definitions, county or group consequences, overlap, sensitivity results, 15-point score, 26 gates, claims, or authority.

The community-review rule enters Module 06 only as the least unacceptable fictional planning candidate. Its 28 selected tracts and 280 equal ten-place teaching awards are not real need, consent, priority, eligibility, outreach, funding, allocation, or service decisions.

## 4. Fictional intervention candidate

The intervention is a fictional voluntary diabetes-prevention access and navigation program for planning review. It combines accessible program information, human review, voluntary scheduling, language and disability access, navigation, community feedback, incident review, and named pause and stop rights.

The candidate does not define personal eligibility, contact a person, deliver a service, estimate an intervention effect, or authorize implementation. It preserves all five staffing-readiness gaps, twelve high-travel concerns, and one high-burden concern carried by the selected community-review comparison until a named owner resolves them.

## 5. Fictional monitoring dry run

The deterministic source ID is `fma-dp-01-monitoring-dry-run-v1`, generator version `0.1.0`, seed 73056.

The source contains 280 synthetic test records, one for each fictional place in the accepted planning candidate. The records exercise offer, response, scheduling, access, attendance, completion, fidelity, burden, feedback, objection, incident, escalation, pause, and unavailable-outcome states. They are software and governance tests, not participants, observed services, clinical outcomes, or evaluation evidence.

The generator uses stable SHA-256 routing rather than platform-dependent randomness. It cannot use public modeled prevalence to generate access, participation, incident, burden, or feedback fields.

## 6. Intervention evidence

The reference release must define:

1. the intervention and authority contract;
2. a theory of change with assumptions and failure points;
3. the delivery pathway and every human decision point;
4. the intended population without personal eligibility decisions;
5. access, capacity, cost, and burden conditions;
6. implementation and balancing measures;
7. a monitoring registry with numerator, denominator, cadence, source, owner, unavailable state, threshold origin, and human response;
8. feedback, correction, refusal, appeal, disagreement, pause, and stop routes;
9. incident, escalation, revision, retirement, and stewardship records;
10. a later evaluation proposal without an effect estimate.

## 7. Monitoring contract

Twenty predeclared measures cover readiness, offer processing, response, scheduling, access, participation, completion, fidelity, burden, feedback, objections, incidents, data availability, and stop conditions.

Thresholds are teaching triggers, not evidence-based clinical thresholds. A triggered result creates a human review or stop action in the fictional exercise. It never creates automatic outreach, eligibility, allocation, enrollment, service, or punishment.

The build reports every numerator, denominator, unavailable state, threshold result, and named response. A missing denominator, suppressed value, unresolved objection, absent access plan, staffing gap, or triggered pause cannot be converted to zero or hidden inside an average.

## 8. Fixed clustering challenger

The challenger uses all 1,597 accepted area rows from the Module 05 linked-candidate table. It does not use the 28 selection labels as a training feature.

The nine fixed features are:

1. public modeled crude diabetes prevalence percent;
2. public confidence-interval width in percentage points;
3. log-transformed public adult population field;
4. fictional capacity places;
5. fictional travel minutes;
6. fictional delivery burden score;
7. fictional language-access readiness;
8. fictional disability-access readiness;
9. fictional staff-readiness indicator.

The base challenger uses `scikit-learn==1.9.0`, `KMeans`, four clusters, `random_state=73056`, `n_init=20`, the Lloyd algorithm, log1p only for population, and standard scaling fitted on the complete 1,597-row matrix. Missing features fail the build. No imputation is allowed.

## 9. Stability and support tests

The cluster count and features are not tuned against a preferred result. Predeclared tests include:

- four alternate seeds with the base transformation and standard scaling;
- robust scaling by median and interquartile range;
- min-max scaling;
- unit-norm scaling;
- adjusted Rand agreement against the base assignment;
- cluster size and empty-cluster checks;
- county concentration and limited-support review;
- selected-candidate coverage across clusters;
- review of the 28 carried planning tracts without using cluster identity to change their selection.

The challenger is stable enough for bounded descriptive tailoring questions only if every cluster is nonempty, the smallest cluster has at least 80 tracts, all alternate-seed adjusted Rand values are at least 0.80, the median scaling-variant adjusted Rand value is at least 0.60, and the 28 carried planning tracts appear in at least three clusters. Failure preserves the transparent community-review rule and records the challenger as not useful.

Passing these tests does not validate a fairness result or authorize cluster-based action. The challenger cannot rank need, select or exclude a tract, assign resources, infer individual traits, determine fairness, replace the transparent rule, bypass community review, or enter deployment.

## 10. Deterministic analysis outputs

The planned outputs are:

- `source-profile.csv`;
- `intervention-readiness.csv`;
- `dry-run-reconciliation.csv`;
- `monitoring-results.csv`;
- `escalation-results.csv`;
- `feedback-recourse-results.csv`;
- `cluster-feature-matrix.csv.gz`;
- `cluster-assignments.csv.gz`;
- `cluster-profiles.csv`;
- `cluster-support-geography.csv`;
- `selected-tract-cluster-review.csv`;
- `challenger-stability.csv`;
- `query-checks.csv`;
- `build-report.json`.

Four reference SQL files must independently reconcile the handoff, intervention dry run, monitoring measures, cluster assignments, stability tests, score carry, authority, and progression decision.

## 11. Learner and reference records

The parallel learner and reference record set contains:

1. `intervention-and-authority-contract.md`;
2. `theory-of-change.csv`;
3. `delivery-pathway.csv`;
4. `population-access-capacity-plan.md`;
5. `implementation-measure-registry.csv`;
6. `monitoring-plan.csv`;
7. `readiness-capacity-review.csv`;
8. `dry-run-interpretation.md`;
9. `benefit-harm-balancing-register.csv`;
10. `feedback-recourse-plan.md`;
11. `incident-escalation-register.csv`;
12. `pause-stop-revision-retirement.md`;
13. `evaluation-proposal.md`;
14. `cluster-model-card.md`;
15. `cluster-stability-support-review.md`;
16. `tailoring-questions.md`;
17. `responsible-claims-audit.csv`;
18. `week6-gate-results.csv`;
19. `progression-decision.md`;
20. `reproducibility-check.md`;
21. `ai-use.md`.

Learner files contain explicit `REPLACE` prompts. Reference files contain the accepted evidence. The validator rejects copied answers, incomplete work, automatic action, changed intervention or model choices, hidden failures, fabricated community input, real-world authority, and deployment language.

## 12. Assessment and progression

Module 06 adds no course points. Thirty-four noncompensable gates cover upstream identity, public and synthetic separation, intervention design, access, monitoring, feedback, governance, clustering, stability, support, AI accountability, claim limits, reproducibility, and progression.

The release may permit construction of APP-5 Checkpoint 02 when all gates pass and the accepted 10 Module 04 points plus 15 Module 05 points remain counted once. It does not make the fictional intervention ready for real use.

## 13. Authority boundary

The module permits fictional intervention planning, monitoring dry-run analysis, and bounded descriptive clustering. It prohibits real need or consent claims, individual inference, real priority or eligibility, outreach, funding, allocation, community action, service delivery, intervention-effect estimation, implementation, production connection, and deployment.

APP-6 owns causal identification and intervention-effect estimation. Module 07 owns clinician leadership and the final recommendation after the separate Week 6 checkpoint passes.

## 14. Integration and release

The completed unit updates:

- root `VERSION` to `0.93.0`;
- the APP-5 course and package records;
- the curriculum catalog;
- the build ledger and resume instructions;
- the central curriculum checker;
- the durable Module 06 specification.

The unit is committed and pushed on `feat/roadmap-course-catalog` only after deterministic source, analysis, workspace, validator, catalog, whitespace, and repository checks pass.
