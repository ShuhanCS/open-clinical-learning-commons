# APP-3 Checkpoint 01 build plan

## Objective

Build the end-of-Week-3 APP-3 checkpoint, `Measures, variation, and bottleneck readiness`, from the accepted Module 01 through Module 03 reference workspaces. The checkpoint must freeze one cumulative evidence chain, carry 40 course points exactly once, and decide whether Module 04 demand forecasting and capacity work may begin.

## Fixed module handoff

| Module | Version | Commons release | Reference files | Manifest rows | Manifest bytes | Manifest SHA-256 | Checkpoint points |
|---|---|---|---:|---:|---:|---|---:|
| `oclc-app3-01` | 0.1.0 | 0.66.0 | 25 | 14 | 1,741 | `ecd8400c5e972e7070d64770086d752a89fd8bc659a1c5c1345c612d0236605d` | 0 |
| `oclc-app3-02` | 0.1.0 | 0.67.0 | 58 | 43 | 5,266 | `868f87c365de83e052c3acee6c7742586a8007dd75d9976343b2f06dfbf622e4` | 20 |
| `oclc-app3-03` | 0.1.0 | 0.68.0 | 54 | 40 | 5,115 | `6528e85f2324fd4b2068788598417be96f6c3a699a587a6ef5eb63f176b0242f` | 20 |

The checkpoint accepts 137 candidate files. It does not recompute, repair, or reinterpret an accepted module inside the assembled release.

## Evidence that must survive assembly

- the fictional `CGH-ED-01` service, one synthetic adult emergency encounter as the unit of flow, and the no-public-linkage rule;
- three complete public source identities and their role as measure-family and historical context evidence only;
- 43,628 accepted synthetic encounters, 39,975 completed encounters, 3,653 left-before-seen encounters, 1,092 shifts, and 52 weeks;
- 17 measure specifications, 12 auditable repairs, and 30 passing query checks;
- the provisional Weeks 1 through 24 baseline, four chart contracts, three predeclared signal rules, and nine signal records;
- 894 known true safety events, 673 trigger true positives, 358 incident true positives, and 379 reviewed non-events or false positives;
- the bounded roomed-to-clinician constraint on evening shifts in Weeks 35 through 44, with medians of 49, 66, 44, and 49 minutes across the declared comparison groups;
- target-window language-support and mobility-support comparisons marked not supported;
- E01 as human review within one business day with no automated, staffing, clinical, or implementation action; and
- every inherited source, denominator, clock, unavailable-state, support, claim, and progression boundary.

## Point and gate contract

- Module 01 is a required zero-point gate.
- Module 02 contributes its accepted 20 points once.
- Module 03 contributes its accepted 20 points once.
- The checkpoint total is 40 points.
- All 12 Module 01, 15 Module 02, and 18 Module 03 gates remain required.
- Eighteen checkpoint integrity gates cover identity, immutability, point accounting, inherited evidence, claim limits, defense, reproduction, and progression.
- A score cannot compensate for any failed inherited or checkpoint gate.

## Learner and reference records

The checkpoint has eight editable records:

1. `README.md`;
2. `evidence-index.csv`;
3. `measures-variation-readiness-review.md`;
4. `checkpoint-gates.csv`;
5. `checkpoint-defense.md`;
6. `reproducibility-check.md`;
7. `ai-use.md`; and
8. `progression-decision.md`.

The reference defense answers 12 fixed questions. The template leaves explicit prompts without pretending that a learner has completed the review.

## Assembly contract

`build_checkpoint.py` will use the existing module workspace builders and Python standard library. It will:

- create accepted reference workspaces for Modules 01 through 03;
- verify exact file counts before copying;
- write every candidate file under `candidate/module-01/`, `candidate/module-02/`, or `candidate/module-03/`;
- write a sorted file-level `candidate-manifest.csv` with bytes and SHA-256;
- keep learner and reference candidate bytes identical;
- refuse to overwrite a target; and
- prove that two independent reference assemblies match.

With 137 candidate files, seven immutable checkpoint controls, eight editable records, and one candidate manifest, each assembled workspace will contain 153 files.

## Validation routes

`validate_checkpoint.py` will validate complete and learner assemblies and run from a copied checkpoint. Its self-check will reject at least:

1. a changed candidate file;
2. a missing candidate file;
3. changed Module 01 points;
4. duplicate Module 02 points;
5. duplicate Module 03 points;
6. a wrong 40-point total;
7. a failed inherited gate;
8. a failed checkpoint gate;
9. a changed signal count;
10. a signal presented as cause;
11. a staffing recommendation;
12. an unsupported subgroup claim;
13. automated escalation;
14. an incomplete defense;
15. invalid Module 04 permission;
16. a missing AI or reproduction field; and
17. an incomplete learner record presented as complete.

## Reference progression

The planned reference disposition is `continue with conditions`. Module 04 permission is `permitted for demand forecasting and capacity analysis`. That permission opens curriculum construction only. It does not establish a root cause, authorize a staffing or clinical change, approve implementation, or allow Module 04 to alter the accepted Week 3 evidence.

## Release handoff

- Checkpoint version: 0.1.0.
- Commons release target: 0.69.0.
- Durable specification: `docs/curriculum/courses/APP-3/checkpoints/01-measures-variation-readiness-spec.md`.
- Package: `courses/clinical-performance-improvement/checkpoints/01-measures-variation-readiness/`.
- Next durable unit after acceptance: APP-3 Module 04, `Demand forecasting and capacity`.
- Base-R control-chart verification remains a named pre-alpha condition until an independent R runtime executes it.
