# Checkpoint defense

## Q01. Which releases are frozen?

Answer: APP-4 Modules 01, 02, and 03 at versions `0.1.0` and Commons releases `0.77.0`, `0.78.0`, and `0.79.0` are frozen as complete reference workspaces.

Evidence: The 245-row candidate manifest and the three nested release manifests reproduce.

Limit: The checkpoint cannot repair an inherited module inside `candidate/`.

## Q02. How are the 40 points counted?

Answer: Module 01 contributes zero points as a required gate. Module 02 contributes 20 points once, and Module 03 contributes 20 points once.

Evidence: `checkpoint-score.csv` totals `40 of 40` without adding checkpoint criteria.

Limit: A point total cannot compensate for a failed gate.

## Q03. What clinical purpose remains in scope?

Answer: The fictional service may continue curriculum work on a nonbinding candidate support concept that asks a clinician to consider whether confirmatory HbA1c testing is appropriate.

Evidence: The accepted Module 01 charter and Module 02 logic release name the clinician, encounter moment, intended support, nonaction, owners, and stop rights.

Limit: The package does not diagnose, order, treat, deny, target, or act automatically.

## Q04. What do the public and synthetic sources support?

Answer: NHANES supports historical cohort, model, calibration, threshold, transport, and subgroup teaching evidence. The Synthea and Commons release supports nonproduction logic and failure mechanics.

Evidence: The checkpoint preserves 16 complete NHANES XPT files and 25 synthetic FHIR files with separate identities.

Limit: Neither source establishes local workflow validity, patient benefit, or clinical permission.

## Q05. Did the logic tests pass?

Answer: Yes. All 16 normal and failure cases match their expected result and ordered trace.

Evidence: `candidate/module-02/rule-test-results.csv` has 16 passing rows.

Limit: Passing mechanics do not make the fixture score or threshold clinically correct.

## Q06. How is the Module 02 value of 0.20 handled?

Answer: It is rejected as a mechanics fixture and is not an evidence candidate.

Evidence: The accepted Module 02 and Module 03 records preserve the fixture and its rejection.

Limit: It cannot enter Module 04 as a recommendation or accepted threshold.

## Q07. What does the historical target mean?

Answer: `LBXGH >= 6.5%` means one observed survey laboratory result is at or above the declared cut point.

Evidence: The cohort and target contract preserves the source field and exact rule.

Limit: It is not a diagnosis, confirmation of disease, treatment indication, or patient recommendation.

## Q08. How are development, holdout, and transport separated?

Answer: The model is fit on 2013-2016 development evidence. The 2017-2018 temporal holdout is evaluated without retuning, and 2021-2023 remains a separate transport stress test using `WTPH2YR`.

Evidence: Partition counts are 3,652, 1,806, and 2,086 rows, with zero holdout or transport fit rows.

Limit: These are historical survey partitions, not a local prospective evaluation.

## Q09. What do performance and calibration support?

Answer: The fixed transparent model shows historical discrimination above a constant baseline and measurable calibration differences in the holdout and transport evidence.

Evidence: Holdout ROC AUC is `0.68783144` with calibration slope `0.88441129`; transport ROC AUC is `0.68422573` with slope `0.81620710`.

Limit: Moderate historical performance does not establish clinical utility or local validity.

## Q10. What do the threshold comparisons show?

Answer: Lower candidates flag more records and miss fewer observed outcomes, while higher candidates flag fewer records and miss more outcomes.

Evidence: Holdout flags range from `661.57323641` per 1,000 at `0.02` to `17.08750038` at `0.10`; missed outcomes range from `2.99863880` to `27.92703988` per 1,000.

Limit: No candidate is selected or accepted, and historical flags are not local card burden.

## Q11. How are decision-curve and subgroup results bounded?

Answer: Decision-curve quantities are interpreted under declared threshold odds. Unsupported subgroup performance remains suppressed.

Evidence: The temporal holdout has eight reportable and eight suppressed subgroup rows; transport has five reportable and 11 suppressed rows.

Limit: The evidence does not prove patient benefit, fairness, a group trait, or a group-specific action.

## Q12. What conflict between logic and evidence was resolved?

Answer: The checkpoint preserves the Module 02 mechanics branch for trace teaching but refuses to import its score or `0.20` value into the historical evidence contract.

Evidence: All six Module 03 evidence candidates remain separate and unaccepted.

Limit: Module 04 must not quietly substitute the mechanics fixture for an evidence candidate.

## Q13. What may Module 04 do?

Answer: Module 04 may compare alert burden, human factors, access, equity, all six unaccepted candidates, a less interruptive alternative, and no alert for curriculum construction.

Evidence: The progression decision says `continue with conditions` and grants bounded Module 04 permission.

Limit: Prototype work remains gated by Module 04, and no real patient may be scored.

## Q14. What remains prohibited and unresolved?

Answer: Diagnosis, real-patient scoring, clinical threshold acceptance, alerting, ordering, treatment, implementation, production connection, and deployment remain prohibited. Named human reviews remain open.

Evidence: The checkpoint contract, gates, AI record, and progression decision preserve these conditions.

Limit: A runnable curriculum release is not clinical approval.
