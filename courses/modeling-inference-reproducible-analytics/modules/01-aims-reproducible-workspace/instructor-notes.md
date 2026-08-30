# Instructor notes

## Teaching purpose

The week slows learners down before modeling. A method is not the starting point. The starting point is a decision, a question class, a unit, a time boundary, and a claim that the available data can actually support.

## Suggested 15.5-hour sequence

| Activity | Hours |
|---|---:|
| Orientation, FND-1 handoff, and source verification | 1.5 |
| Aim taxonomy worked examples | 2.0 |
| Target and estimand workshop | 2.0 |
| Prediction time and leakage lab | 2.5 |
| Feature-role contract lab | 2.0 |
| Temporal split and baseline build | 2.0 |
| Clean reproduction and validator | 1.5 |
| Independent classification and release defense | 2.0 |
| Total | 15.5 |

## Six worked requests

Use AIM01 through AIM06 in `estimand-target-registry.csv` to show that the same healthcare domain can produce six different questions. Ask for the decision and unit before showing the answer. The methods should follow from the aim:

- AIM01 descriptive: count and proportion;
- AIM02 associational: bounded regression interpretation;
- AIM03 predictive: pipeline and held-out evaluation;
- AIM04 causal: a design and identification argument not supplied here;
- AIM05 longitudinal: repeated observations not supplied here; and
- AIM06 forecasting: an equally spaced aggregate series supplied later.

## Twelve-exercise answer key

| Exercise | Aim | Why | Reject first |
|---|---|---|---|
| EX01 | descriptive | asks what was observed in this cohort | prediction |
| EX02 | associational | asks for a conditional relationship | causal effect |
| EX03 | predictive | asks for future outcome probability at a decision time | descriptive count |
| EX04 | causal | asks what an intervention would change | ordinary association |
| EX05 | longitudinal | asks about repeated within-person change | one-row regression |
| EX06 | forecasting | asks for future aggregate values over calendar time | person-level prediction |
| EX07 | descriptive | asks for one cohort summary | regression |
| EX08 | associational | asks for a bounded conditional relationship | prediction performance |
| EX09 | predictive | asks to compare a classifier with a baseline | causal inference |
| EX10 | causal | asks for a counterfactual intervention outcome | observed proportion |
| EX11 | longitudinal | asks whether repeated trajectories differ | cross-sectional comparison |
| EX12 | forecasting | asks whether a future aggregate crosses a level | person-level classification |

Accept a different rejected method when the learner explains the mismatch correctly.

## Demonstrating leakage

Show a deliberately invalid feature list containing `next_30d_state` or `endpoint_90d`. Do not celebrate its performance. Ask what information the field contains, when it becomes known, and why a high score can be evidence of failure. Destroy or clearly quarantine any leaked candidate output.

Five leakage families must be named:

1. post-index information;
2. outcome-derived fields;
3. preprocessing fit on validation or test data;
4. split or metric fields used as predictors; and
5. identity or duplicate leakage across partitions.

## Split interpretation

The source is synthetic and old, but its time ordering is useful. The split intentionally leaves only four positive test outcomes. The correct reaction is to narrow claims and report uncertainty. The incorrect reaction is to stratify, reseed, or move rows until test metrics appear stable.

Train owns fitting. Validation may guide candidate choice, preprocessing alternatives fit on train, hyperparameters, and threshold selection. Test is opened once for the final selected pipeline in Module 03. The public artifact exposes labels for audit, but exposure does not grant permission to use them for selection.

## Baseline interpretation

The constant baseline probability is `0.111607142857`. It is not a useful clinical model. It is a minimum technical comparison that prevents a complex candidate from receiving credit merely for producing numbers.

Do not ask learners to calculate test discrimination or calibration in Module 01. Module 03 owns those metrics and the final evaluation.

## Sparse groups

The source race counts are white 308, black 33, asian 27, native 5, and other 1. The source gender counts are F 236 and M 138. Learners should identify why subgroup estimates can become unstable or disclosive even in a synthetic dataset. They should not merge categories automatically or claim fairness from these counts.

## Common failure patterns

- starting with logistic regression before stating the decision;
- calling a predictive target an estimand without a contrast;
- defining prediction time as the start rather than the stop of the index encounter;
- using birth date together with age without a reason;
- treating `next_30d_state` as a harmless utilization predictor;
- treating follow-up completion as available at time zero;
- selecting a random split because it yields more balanced outcomes;
- computing a baseline from all 374 rows;
- looking at test performance before freezing the candidate;
- confusing a passing validator with real-world validity; and
- writing "no AI used" when an agent generated or revised material work.

## Oral check prompts

Ask the learner to point to one row and explain prediction time, allowed information, label timing, and split. Then ask the learner to change one prohibited field to allowed in a copy and explain why the validator or human review should stop it.

The learner must be able to explain:

- the difference between validation and test roles;
- why the source fingerprint matters;
- why no random seed controls this temporal split;
- why a deterministic build can still encode a bad analytic decision;
- why the test-set limitation survives a passing check; and
- what would force a semantic-version decision.

## Reference review disposition

The reference disposition is `accept with conditions`. Module 02 may use the package for teaching. It may not treat the synthetic outcome, sparse groups, or four-positive test set as evidence for clinical deployment.

## Human review before alpha

Named faculty review is still required from quantitative methods, clinical informatics, Python/notebook, accessibility, privacy, responsible AI, and an independent instructor. Acceptance by the automated validator is technical evidence only.
