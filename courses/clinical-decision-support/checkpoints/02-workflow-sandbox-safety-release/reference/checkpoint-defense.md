# Checkpoint defense

## Q01. What exactly is frozen at this checkpoint?

- Exact answer: `1,030 files: 302 from Module 04, 341 from Module 05, and 387 from Module 06`.
- Evidence: `candidate-manifest.csv` and `evidence-index.csv`.
- Decision consequence: Any changed, missing, or additional candidate file fails the release.
- Limit: The checkpoint does not recompute or improve accepted evidence.

## Q02. How are Week 6 points counted?

- Exact answer: `Module 04 contributes 25.00 points once; Modules 05 and 06 contribute 0.00 points`.
- Evidence: `checkpoint-score.csv` and `candidate/module-04/module-score.csv`.
- Decision consequence: The cumulative Week 6 total is 25.00 of 25.00.
- Limit: A summary row is not a second score and points cannot compensate for a failed gate.

## Q03. Which gates are required?

- Exact answer: `20 Module 04, 20 Module 05, 22 Module 06, and 20 checkpoint gates; 82 total`.
- Evidence: the four `gate-results.csv` or `checkpoint-gates.csv` files.
- Decision consequence: Every gate must pass for progression.
- Limit: The 62 inherited gates remain owned by their source modules.

## Q04. What design and threshold reach the sandbox?

- Exact answer: `panel-t003, a passive contextual panel fixture; 0.03000000, an unaccepted mechanics fixture; accepted threshold none`.
- Evidence: `candidate/module-04/candidate-design-review.md` and `candidate/module-05/prototype-release.md`.
- Decision consequence: The design may be discussed as a teaching fixture only.
- Limit: No clinical threshold is selected, accepted, or recommended.

## Q05. What did the sandbox establish?

- Exact answer: `31 declared cases produced their expected local nonnetworked behavior, including normal, boundary, repeat, missing, stale, inconsistent, delayed, terminology, version, visible-failure, and silent-failure routes`.
- Evidence: `candidate/module-05/test-matrix-review.csv`.
- Decision consequence: The traceable teaching package can enter safety review.
- Limit: Passing sandbox mechanics do not establish interoperability, safety, usability, or clinical utility.

## Q06. Which failures cannot be summarized away?

- Exact answer: `17 inherited failure modes, one independently reconciled silent failure, and one blocked malformed-card accessibility defect`.
- Evidence: `candidate/module-05/failure-mode-register.csv`, `candidate/module-06/silent-failure-monitoring.md`, and `candidate/module-05/accessibility-review.csv`.
- Decision consequence: Removing or relabeling any one fails the checkpoint.
- Limit: Seeded failures do not estimate clinical event rates.

## Q07. What does the safety case establish?

- Exact answer: `22 of 22 hazards have detection, control, ownership, escalation, fallback, stop, restart, and retirement routes`.
- Evidence: `candidate/module-06/safety-case.md` and `candidate/module-06/hazard-review.csv`.
- Decision consequence: The teaching package is organized enough for leadership review.
- Limit: Completeness of a safety case does not prove the concept is safe in care.

## Q08. How will silence and unavailable monitoring be handled?

- Exact answer: `reconcile four independent ledgers; one or more silent failures triggers human investigation; unavailable reconciliation stops the affected evaluation`.
- Evidence: `candidate/module-06/silent-failure-monitoring.md`.
- Decision consequence: Absence from a service log cannot be interpreted as successful handling.
- Limit: Unavailable is not zero, favorable, safe, or not applicable.

## Q09. What monitoring and escalation ownership exists?

- Exact answer: `20 monitoring measures and 12 human-owned escalation routes, with zero automatic actions`.
- Evidence: `candidate/module-06/monitoring-plan.csv` and `candidate/module-06/incident-escalation-review.csv`.
- Decision consequence: Owners can investigate, pause, stop, fall back, restart, or retire through the specified routes.
- Limit: Teaching triggers are not validated clinical control limits.

## Q10. Was the ML comparison fair?

- Exact answer: `the fixed gradient-boosting challenger used 7,544 common rows, three predictors, the same splits, weights, threshold candidates, alert budgets, and no post-holdout tuning`.
- Evidence: `candidate/module-06/ml-contract-review.md` and `candidate/module-06/outputs/leakage-tests.csv`.
- Decision consequence: The replacement rules may be applied to the declared comparison.
- Limit: A fair historical comparison does not establish local validity or utility.

## Q11. Why was the challenger not accepted?

- Exact answer: `8 of 11 replacement rules pass; R03, R04, and R08 fail`.
- Evidence: `candidate/module-06/model-comparison.md` and `candidate/module-06/outputs/replacement-rules.csv`.
- Decision consequence: The transparent model remains retained under the conjunctive rule.
- Limit: Better weighted Brier score does not waive worse untouched-set discrimination or subgroup degradation.

## Q12. What are the exact failed ML results?

- Exact answer: `temporal-holdout AUC difference -0.00743486; transport-stress AUC difference -0.01928938; worst supported subgroup AUC degradation 0.10385240`.
- Evidence: `candidate/module-06/model-comparison.md`.
- Decision consequence: R03, R04, and R08 remain failed without rounding, rule movement, retuning, or threshold changes.
- Limit: Subgroup results preserve support limits and do not authorize group-specific action.

## Q13. What may Module 07 decide?

- Exact answer: `Module 07 may interpret the frozen evidence, assign human ownership, state uncertainty, recommend continue with conditions, revise, refer, or stop, and defend the recommendation`.
- Evidence: `module07-handoff.md`.
- Decision consequence: Clinician leadership review is permitted.
- Limit: Module 07 may not rewrite the candidate, tune a model, accept a threshold, or create new clinical evidence.

## Q14. What authority remains absent?

- Exact answer: `real-patient scoring, clinical threshold acceptance, clinical alerting, clinical action, silent-mode evaluation, implementation, production connection, and deployment are prohibited`.
- Evidence: `checkpoint-contract.json`, `responsible-claims-check.md`, and `module07-handoff.md`.
- Decision consequence: Progression remains curriculum construction only.
- Limit: Neither a full score nor an accepting progression decision expands authority.
