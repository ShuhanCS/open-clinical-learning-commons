# APP-4 Module 03 assessment

## Submission

Submit the 15 named assessed records in the released workspace. The submission is the 20-point evidence, calibration, and threshold audit that completes the learner contribution to the 40-point Week 3 checkpoint.

The reference decision is `continue with conditions`. It permits Checkpoint 01 assembly for curriculum construction only. It does not accept a threshold or authorize Module 04 until the cumulative checkpoint passes.

## Rubric

| Criterion | Required evidence | Points |
| --- | --- | ---: |
| Cohort and target | Exact eligibility, exclusions, target, time, missingness, and non-diagnosis boundary | 2.0 |
| Survey design | Correct development, holdout, transport, weight, stratum, PSU, and phlebotomy-weight treatment | 2.0 |
| Model specification | Fixed transparent formula, fit partition, transformations, audit-only fields, and no leakage or retuning | 2.0 |
| Performance | Baseline and model discrimination, Brier score, log loss, prevalence, support, and uncertainty interpretation | 2.0 |
| Calibration | Calibration-in-the-large, slope, score-range table, and limits | 2.0 |
| Threshold consequences | Every candidate threshold with flags, missed cases, sensitivity, specificity, predictive value, and no accepted choice | 2.0 |
| Decision curve | Correct threshold-odds interpretation and explicit non-benefit boundary | 1.5 |
| Transport stress | Holdout-to-transport comparison without unsupported causal explanation | 1.5 |
| Subgroup support | Denominators, outcomes, effective support, suppression, uncertainty, and no group action | 1.5 |
| Week 3 component release | Exact evidence identity, conditions, invalidation, and checkpoint handoff | 1.5 |
| Reproducibility, claims, and AI | Complete evidence reproduction, bounded claims, disclosed tool use, independent checks, and human ownership | 2.0 |
| Total |  | 20.0 |

## Noncompensable gates

A numeric score cannot compensate for any of these failures:

1. changed Module 01 or Module 02 inherited evidence;
2. an incomplete or incorrect cohort, target, partition, or information-cutoff rule;
3. treating one HbA1c result as a diagnosis or confirmed disease;
4. fitting or tuning on temporal-holdout or transport rows;
5. ignoring survey weights, strata, PSUs, or the 2021-2023 phlebotomy weight;
6. missing calibration, threshold, burden, missed-case, or decision-curve evidence;
7. promoting the Module 02 `0.20` mechanics value to evidence status;
8. selecting or accepting a clinical threshold in code, by an agent, or without human governance;
9. reporting unsupported subgroup performance or authorizing group-specific action;
10. hiding missingness, an unavailable result, a failed invariant, or a material limitation;
11. undisclosed or unchecked agent use; or
12. any diagnosis, patient-level action, live scoring, alerting, implementation, production connection, or deployment claim.

## Passing standard

A passing package earns at least 14 of 20 points and passes all 12 gates. Faculty may require revision even above 14 points when the progression decision is not supported by the evidence.
