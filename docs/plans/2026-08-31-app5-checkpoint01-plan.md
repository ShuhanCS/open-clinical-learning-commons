# APP-5 Week 3 checkpoint build plan

## Purpose

Build the separate cumulative Week 3 checkpoint for APP-5, Data for Population Health and Equity. The checkpoint decides whether the accepted population, denominator, measure, standardization, disparity, missingness, bias, suppression, and claim-limit evidence may enter Module 04 place-based curriculum work.

This checkpoint is an assembly and review gate. It does not recalculate a measure, create a new disparity result, add course points, make a real Massachusetts claim, map or rank a tract, choose a target, allocate a resource, fit a model, authorize community action, implement, or deploy.

## Release identity

- Checkpoint ID: `oclc-app5-cp01`.
- Checkpoint version: `0.1.0`.
- Commons release: `0.90.0`.
- Due point: end of instructional Week 3; the official assigned half-term dates remain controlling.
- Course points: 40.
- Point source: Module 02 contributes 20 points once and Module 03 contributes 20 points once.
- Required zero-point gate: Module 01.
- Planned package: `courses/population-health-equity/checkpoints/01-measures-disparities-readiness/`.
- Planned specification: `docs/curriculum/courses/APP-5/checkpoints/01-measures-disparities-readiness-spec.md`.

## Accepted inputs

The builder must call each owning module's existing standard-library workspace builder and request its complete reference workspace.

| Module | Version | Commons | Files | Nested rows | Manifest bytes | Manifest SHA-256 | Points |
|---|---|---|---:|---:|---:|---|---:|
| `oclc-app5-01` | `0.1.0` | `0.87.0` | 27 | 16 | 1,907 | `65ea81f391ed426f63e84593588d57542e827f89f2493aa0b3a2f8b1d9a2b0e9` | 0 |
| `oclc-app5-02` | `0.1.0` | `0.88.0` | 72 | 57 | 7,588 | `330b4e9ba5071ad4529d46f4af5b15555e8db84ef1718de2a8de42d0aa76a4b0` | 20 |
| `oclc-app5-03` | `0.1.0` | `0.89.0` | 120 | 104 | 15,465 | `d9591e028ba49d79762d444d769821dc21055a712aceda3f501c0e31bb7d24b8` | 20 |

The cumulative candidate has 219 files and 177 nested immutable rows. The outer manifest must fingerprint all 219 files with a sorted path, byte count, SHA-256, module ID, module version, and role.

## Checkpoint records

Build parallel learner and reference versions of these 12 records:

1. `README.md`
2. `evidence-index.csv`
3. `measures-disparities-readiness-review.md`
4. `checkpoint-score.csv`
5. `checkpoint-gates.csv`
6. `responsible-claims-audit.md`
7. `checkpoint-defense.md`
8. `reviewer-record.md`
9. `conditions-register.csv`
10. `reproducibility-check.md`
11. `ai-use.md`
12. `progression-decision.md`

Learner records use explicit `REPLACE` prompts. Reference records contain exact accepted evidence and no placeholder.

## Point and gate contract

The score file carries the five accepted Module 02 criteria and five accepted Module 03 criteria. Module 02 totals 20. Module 03 totals 20. Module 01 and the checkpoint add zero. The cumulative total is 40, with a numeric passing threshold of 28. A gate failure overrides the score.

Carry all inherited gates:

- Module 01: 12 of 12 pass;
- Module 02: 15 of 15 pass;
- Module 03: 18 of 18 pass.

Add 22 checkpoint integrity gates covering identity, chain of custody, public and synthetic source separation, denominator and rate contracts, standardization, reference choice, uncertainty, missingness, representation, bias, separate marginal dimensions, small-number rules, primary and complementary suppression, non-reconstruction, points, claims, human review, reproduction, and bounded progression.

The reference result is 40 of 40 with all 67 inherited and checkpoint gates passing. The reference disposition is `continue with conditions`.

## Required cumulative interpretation

The readiness review must preserve these accepted facts:

- 1,620 union tracts and 1,597 linked measure tracts;
- 5,679,768 adult denominator units and 283,614 synthetic events;
- five age bands and one declared standard population;
- 1,576 available direct rates, 21 unavailable direct rates, and 80 guided indirect cases;
- three separate synthetic marginal dimensions with 19 groups, 151,715 group-margin rows, and 7,985 completeness rows;
- 110 group-age rates, 22 standardized group rates, 32 reference comparisons, and six summary disparities;
- five missingness results, 19 representation records, and eight bias records;
- 19,742 primary suppressed cells, 1,488 complementary suppressed cells, 9,113 publishable cells, and 4,791 passing non-reconstruction audits; and
- a bounded fictional synthetic disparity statement only.

Suppressed values remain unavailable. Separate margins do not support intersectional claims. Zero conditioned geography missingness does not prove perfect capture. Public PLACES modeled prevalence remains separate from synthetic event evidence.

## Progression and authority

Checkpoint acceptance may permit Module 04 curriculum construction for geometry acquisition, key and coordinate checks, spatial accounting, geographic aggregation, small-area stability, ecological and contextual reasoning, one responsible accessible map, and a context memo.

Module 05 remains prohibited until Module 04 passes. The checkpoint does not authorize a map inside the Week 3 package, tract ranking, targeting, eligibility, outreach, allocation, funding, model fitting, intervention-effect estimation, real community action, implementation, production connection, or deployment.

Twelve open conditions assign the official dates, source review, measure methods, group labels and standards, reference and uncertainty choices, missingness and representation review, bias review, suppression and privacy review, community rights, accessibility, responsible AI, and independent reproduction to named human owners before alpha.

## Deterministic package design

Reuse the established applied-course checkpoint pattern and the Python standard library.

- Eight immutable checkpoint controls: `.gitattributes`, `VERSION`, `assessment.md`, `checkpoint-contract.json`, `instructor-notes.md`, `release.json`, `build_checkpoint.py`, and `validate_checkpoint.py`.
- Twelve editable checkpoint records.
- One outer candidate manifest.
- 219 frozen candidate files.
- Expected assembled workspace: 240 files.

The builder must refuse an existing target, produce byte-identical independent reference candidates, and give learner and reference packages the same candidate manifest.

## Validation and release gates

The validator must check the exact inventory, all outer and nested fingerprints, source and release identities, point arithmetic, inherited and checkpoint gates, accepted analytic facts, unavailable and suppression states, claims, defense, reviewer and condition records, AI accountability, and progression authority.

The self-check must reject at least these failure classes:

- changed or missing candidate;
- changed or duplicated component points;
- wrong checkpoint total;
- failed inherited or checkpoint gate;
- merged public and synthetic evidence;
- changed denominator, reference, interval, or missingness result;
- intersectional inference from separate margins;
- suppressed blank changed to zero;
- a published total that makes suppression reconstructable;
- a real disparity, mapping, ranking, targeting, allocation, implementation, or deployment claim;
- incomplete defense, reviewer, conditions, AI, or reproduction record; and
- invalid Module 04 permission.

Release only after the builder and validator self-checks, copied-validator execution, focused central curriculum contract, catalog integrity check, plain-ASCII and path checks, semver check, Git commit, push, and remote verification pass.

## Integration and handoff

Update the APP-5 course specification, course package README, root README, curriculum build ledger, central curriculum checker, catalog wording where needed, and root `VERSION`. The next unit after the checkpoint is APP-5 Module 04, Place-based evidence and geographic reasoning. It begins only from the accepted checkpoint candidate and conditions.
