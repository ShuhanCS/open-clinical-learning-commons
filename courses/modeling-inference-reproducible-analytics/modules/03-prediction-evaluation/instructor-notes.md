# Instructor notes

## Suggested 16.5-hour sequence

| Activity | Hours |
|---|---:|
| Upstream handoff and three-part data split | 1.0 |
| Pipeline fitting and transformed-feature audit | 2.0 |
| Training-only resampling lab | 2.0 |
| Validation metrics and model selection | 2.0 |
| Leaked-model failure lab | 1.0 |
| Threshold consequences and lock | 2.0 |
| One-time test evaluation | 2.0 |
| Calibration and uncertainty | 1.5 |
| Subgroup counts, suppression, and accessible evidence | 1.5 |
| Reproduction and oral defense | 1.5 |
| Total | 16.5 |

## Core teaching move

Keep asking, "Which partition is allowed to answer this question?" Training estimates model parameters. Resampling checks training stability. Validation selects the candidate and threshold. Test estimates the locked workflow once. A good number on the wrong partition is still wrong evidence.

## Selection answer key

Validation has 75 rows and 7 outcomes.

| Model | ROC AUC | Average precision | Brier | Selection result |
|---|---:|---:|---:|---|
| `BASE` | 0.50000000 | 0.09333333 | 0.08495615 | retained comparator |
| `LOG01` | 0.44957983 | 0.09196407 | 0.08615760 | fails all three candidate rules |
| `ML01` | 0.58613445 | 0.15806484 | 0.08468750 | selected |
| `LEAK01` | 1.00000000 | 1.00000000 | 0.00000014 | prohibited before review |

The selection rule is deliberately modest and mechanical. An eligible candidate must have Brier score no worse than the baseline, ROC AUC at least 0.55, and average precision no worse than baseline. `ML01` is the only candidate that meets all three. That makes it the selected teaching model, not a clinically validated model.

## Leakage demonstration

Ask learners to inspect the semantic timing of `next_30d_state` and `endpoint_90d` before showing performance. Both fields contain future or outcome-derived information. `LEAK01` therefore fails even if its AUC is 1. Performance cannot rescue an invalid feature set.

## Threshold answer key

The validation consequence rule requires sensitivity of at least 5 of 7 outcomes. Among the observed `ML01` probabilities meeting that requirement, choose the threshold with the fewest false positives; break a tie with the highest threshold. The locked threshold is 0.08513264. At validation it gives 5 true positives, 2 false negatives, 30 false positives, and 38 true negatives.

This is not a universal clinical threshold. It is a visible teaching consequence selected from validation evidence.

## Test answer key

- Test rows: 75.
- Outcomes: 4.
- `ML01` ROC AUC: 0.58802817, with stratified bootstrap interval 0.26760563 to 0.91549296.
- Average precision: 0.14682471, interval 0.05532198 to 0.58716356.
- Brier score: 0.05097579.
- Sensitivity: 2/4 = 0.50000000.
- Specificity: 48/71 = 0.67605634.
- PPV: 2/25 = 0.08000000.
- NPV: 48/50 = 0.96000000.
- False positives: 23.
- False negatives: 2.

The four outcomes dominate interpretation. Wide uncertainty is expected. The high NPV largely reflects low prevalence and must not be read as proof of safety.

## Baseline threshold lesson

The constant baseline assigns every test row the same probability. Applying its own constant as the threshold labels every row positive because the rule uses greater than or equal to. This yields sensitivity 1, specificity 0, and PPV equal to prevalence. It is a consequence illustration, not a proposed decision policy.

## Calibration lesson

The exact five groups contain 15 rows each. Observed outcomes by group are 0, 2, 0, 1, and 1. The nonmonotonic pattern and small counts prevent a stable calibration claim. The plot helps learners see the mismatch; the CSV provides the exact evidence.

Do not add a calibration slope or intercept to this release. With four test outcomes, it would add a fragile number without changing the decision. Module 04 should first review validity and data structure.

## Subgroup lesson

Ten observed subgroup rows are reported across gender, race, ethnicity, and index class. Five are suppressed because they have fewer than 20 rows or fewer than two outcomes or nonoutcomes. Even the unsuppressed rows are descriptive teaching estimates. Learners may discuss what is unknown, but may not rank groups or declare fairness.

## Common failures

- fitting the encoder on all 374 rows;
- treating cross-validation as a substitute for temporal validation;
- choosing the random forest because it looked best on test;
- dropping the constant baseline;
- allowing the leaked model into a leaderboard;
- using ROC AUC alone;
- changing the threshold after seeing two false negatives;
- reporting rates without counts and prevalence;
- calling four outcomes enough for stable calibration;
- comparing suppressed subgroup metrics;
- saying `ML01` is superior when the evidence only supports the frozen rule; and
- equating model selection with clinical readiness.

## Oral check

Give the learner one proposed change, such as adding a predictor after seeing the test false negatives. Ask which module and evidence partition must reopen. The correct response returns to the pre-test design process, versions the contract, and preserves the original test result rather than silently reusing test as validation.

## Reference recommendation

`continue to validity review with conditions`. Preserve the exact test evidence, four-outcome limitation, 23 false positives, subgroup suppression, synthetic-data boundary, and one-time-test rule. Module 04 must not treat selected prediction features as a causal adjustment set.
