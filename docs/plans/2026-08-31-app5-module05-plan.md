# APP-5 Module 05 build plan

## Unit

- Course: APP-5, Population Health and Equity.
- Module: 05, Targeting and fairness.
- Module ID: `oclc-app5-05`.
- Module version: `0.1.0`.
- Commons release: `0.92.0`.
- Hours: 16.0.
- Assessment: 15 points counted once in the separate 25-point Week 6 checkpoint.
- Decision: which, if any, transparent fictional targeting rule is responsible enough to enter an intervention plan?
- Next unit after acceptance: APP-5 Module 06, Accountable intervention design, monitoring, and embedded ML.

## Accepted starting point

Module 05 begins from the complete accepted Module 04 reference workspace. The handoff has 287 files, including the complete Week 3 checkpoint, the official 2024 TIGER/Line Massachusetts tract archive, exact geography and join audits, the accepted CDC PLACES teaching table, the responsible map, the support review, county teaching summaries, ecological claim limits, the 10-point score, and all 22 Module 04 gates.

The freezer must call the accepted Module 04 workspace builder, copy the resulting reference workspace without editing it, write a sorted handoff manifest, and reject a changed byte or an existing destination. Independent freezes must match byte for byte.

Module 05 may use the accepted public evidence as input. It may not reinterpret modeled prevalence as observed cases, individual risk, a real disparity, community need, priority, eligibility, consent, capacity, or an action rule.

## Fictional teaching scenario

The scenario remains `FMA-DP-01`, an explicitly fictional Massachusetts adult diabetes-prevention planning review. Real tract identifiers and accepted public measures keep the evidence work authentic. The planning council, resource constraint, service places, staff capacity, access conditions, community-review records, decisions, benefits, harms, burdens, appeals, and outcomes are fictional or synthetic.

The generator will create one deterministic planning row for every one of the 1,597 tracts with an accepted PLACES estimate. Each row must carry:

- scenario and synthetic identity;
- tract and county keys for linkage;
- fictional delivery capacity;
- fictional travel or access burden;
- fictional staff readiness;
- fictional language and disability access readiness;
- fictional community-review state;
- fictional objection and unresolved-question states;
- fictional operational burden;
- a fixed accountable owner; and
- a plain statement that the row is teaching data and authorizes no real action.

The generator must use only the Python standard library, a declared seed, and the accepted tract list. It must not make synthetic capacity, access, or community response a hidden function of the public prevalence value. Two independent generations must match byte for byte. A changed seed, tract list, source identity, schema, or output byte requires a semver decision and renewed validation.

## Fixed resource contract

Every rule receives the same fictional resource constraint:

- 280 fictional program places;
- 28 equal ten-place teaching awards;
- no partial award;
- no carryover between rules;
- the same 1,597 candidate tracts;
- the same accepted public evidence;
- the same synthetic capacity, access, and community-review layer; and
- the same claim, appeal, pause, and stop limits.

An award is a classroom comparison unit. It is not eligibility, outreach, funding, allocation, service delivery, or permission to contact a person or community.

## Four required rules

The build must compare exactly four transparent rules.

1. Equal geographic rule. Select two teaching areas per county using a fixed source-independent tie breaker. Its fairness definition is equal geographic representation across the 14 counties.
2. Need-based rule. Use the accepted modeled prevalence and its interval only as a declared classroom criterion, with limited-support rows kept visible. Its fairness definition is greater fictional attention to higher modeled area-level prevalence. This rule cannot be accepted as automatic authority.
3. Capacity-aware rule. Prefer areas with sufficient fictional delivery capacity, access readiness, and staff readiness. Its fairness definition is feasible delivery under the fixed constraint. It must expose the risk of favoring places that already have more capacity.
4. Community-review rule. Require a fictional ready-for-planning-review state, no unresolved objection, language and disability access readiness, and a county representation limit. Its fairness definition is procedural readiness with recourse. It must expose delay and exclusion caused by incomplete review.

Every rule must publish its exact criteria, tie breaker, included and excluded areas, allocated places, reason, unsupported state, and interpretation limit. No composite score, SVI rank, map color, model output, or hidden optimization may decide the result.

## Required deterministic outputs

The analysis release must create:

- a planning-source profile;
- a complete linked candidate table;
- exact rule definitions;
- one complete assignment table with all four rules and all candidate tracts;
- one summary row per rule;
- county concentration results;
- group-consequence coverage using the accepted synthetic equity margins while preserving suppression;
- access, capacity, burden, support, objection, and unresolved-review consequences;
- rule-to-rule overlap and turnover;
- predeclared sensitivity variants for each rule;
- query and reconciliation checks; and
- a machine-readable build report with fingerprints for every released output.

The group analysis may sum published synthetic population counts. It may not reconstruct suppressed cells, compare unavailable values as zero, or present the synthetic group layer as a real disparity or community preference.

Sensitivity checks must vary declared teaching assumptions, not search for a preferred answer. At minimum they must test resource quantity, support handling, capacity readiness, community-review readiness, county limits, and tie-break behavior. The release must report how many selections change and which consequences move.

## Learner and reference records

Create parallel learner templates and accepted reference records for:

1. decision and resource contract;
2. rule definitions;
3. inclusion, exclusion, delay, and burden audit;
4. fairness definition and tradeoff memo;
5. geographic concentration review;
6. group-consequence and suppression review;
7. access and capacity review;
8. sensitivity analysis;
9. benefit, harm, and balancing register;
10. community review, appeal, pause, and stop record;
11. accountable-owner record;
12. responsible claims audit;
13. Week 6 component score;
14. gate results;
15. progression decision;
16. reproducibility check; and
17. AI-use record.

Learner records use explicit `REPLACE` prompts. Reference records contain exact accepted evidence and no placeholder.

## Assessment and progression

Score the module out of 15:

- fixed decision, resource, and rule integrity: 3 points;
- inclusion, exclusion, access, capacity, and burden accounting: 4 points;
- fairness, geographic, group, benefit, harm, and sensitivity reasoning: 5 points; and
- community review, recourse, reproducibility, AI accountability, and claim limits: 3 points.

The numeric passing threshold is 12 of 15. Any noncompensable gate failure overrides the score. The reference should earn 15 of 15 with every gate passing and disposition `continue with conditions`.

Acceptance permits Module 06 curriculum construction only. The Week 6 checkpoint remains prohibited until Module 06 passes. Real eligibility, outreach, funding, allocation, community action, intervention, implementation, production connection, and deployment remain prohibited.

The reference progression decision should carry the community-review rule into Module 06 as the least unacceptable fictional planning candidate, subject to explicit human review, capacity confirmation, access repair, appeal, pause, and stop conditions. It must not authorize an automatic decision or a real action.

## Workspace and validation design

Reuse the Module 04 handoff, deterministic builder, manifest, learner/reference workspace, and mutation-test patterns. Use the Python standard library and SQLite. Do not add a new dependency.

The validator must check:

- exact upstream, synthetic-source, output, schema, and workspace identities;
- all 1,597 candidate tracts and all four assignment rows per tract;
- the fixed 280-place and 28-award constraint for every rule;
- exact inclusion, exclusion, support, access, capacity, county, group, burden, objection, and sensitivity accounting;
- preservation of suppressed and unavailable states;
- explicit fairness definitions and tradeoffs;
- benefit, harm, balancing, community-review, appeal, pause, stop, and owner records;
- the 15-point score and every noncompensable gate;
- responsible claims, AI use, progression, and authority limits; and
- deterministic learner and reference assembly.

The self-check must reject changed upstream bytes, changed synthetic bytes, a missing or duplicate tract, a hidden fifth rule, a changed resource constraint, partial awards, a public value relabeled as observed need, suppressed values changed to zero, a copied reference answer, an incomplete learner package submitted as complete, a changed score, a failed gate, automatic allocation language, missing recourse, real-action authority, and deployment language.

## Integration and release gates

Update the APP-5 course specification, course package README, root README, curriculum catalog wording where needed, build ledger, central curriculum checker, and root `VERSION`.

Release only after:

- Module 04 freeze and fingerprint checks;
- synthetic-source determinism and separation checks;
- complete rule, consequence, sensitivity, and SQL checks;
- learner and reference workspace checks;
- complete and learner validation;
- copied-validator execution;
- protected failure-route rejection;
- focused central curriculum contract;
- catalog integrity, plain-ASCII, personal-path, placeholder, and Git diff checks;
- semver checks;
- Git commit and push; and
- remote branch verification.
