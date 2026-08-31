# APP-4 Module 03 instructor notes

## Teaching purpose

Begin with the handoff question, not the ROC curve: does the historical evidence justify moving the fictional advisory concept into a cumulative Week 3 review? Make learners preserve the distinction between a public survey result, a model score, a candidate threshold, a clinical action, and authority to use a tool.

## Suggested sequence

1. Reconstruct the cohort flow and ask which exclusions are clinical, analytic, missingness-driven, or merely provisional.
2. Read the target as an observed HbA1c cut point and have learners explain why it is not a diagnosis.
3. Trace the development, temporal-holdout, and transport partitions before opening the model output.
4. Verify `WTMEC2YR / 2`, holdout `WTMEC2YR`, transport `WTPH2YR`, strata, and PSUs.
5. Compare the constant baseline with the fixed transparent model.
6. Read discrimination and calibration together.
7. Walk across all six candidate thresholds and translate each into flags and missed eligible cases per 1,000.
8. Show why the Module 02 `0.20` value is not promoted by appearing in executable code.
9. Inspect transport changes and require descriptive language without a causal story.
10. Review subgroup support before any subgroup performance number.
11. End with a bounded progression decision and a list of human reviews still needed.

## Reference findings

- Development has 3,652 rows and 156 outcomes.
- Temporal holdout has 1,806 rows and 97 outcomes.
- Transport stress has 2,086 rows and 75 outcomes.
- Weighted ROC AUC is `0.68783144` in holdout and `0.68422573` in transport.
- Holdout calibration-in-the-large is `-0.03946013` and slope is `0.88441129`.
- Transport calibration-in-the-large is `0.07788522` and slope is `0.81620710`.
- At `0.02`, weighted holdout sensitivity is about 0.897 but roughly 662 of 1,000 eligible cases are flagged.
- At `0.10`, roughly 17 of 1,000 are flagged but weighted holdout sensitivity is about 0.038.
- At the rejected `0.20` mechanics value, the transport partition captures no weighted outcomes.

These tradeoffs support continued review, not threshold acceptance.

## Stop conditions

Stop and return the package when a learner:

- calls the target diabetes, confirmed disease, or a diagnosis;
- hides excluded or missing rows;
- pools 2021-2023 with the earlier cycles;
- uses `WTMEC2YR` instead of `WTPH2YR` for the later blood analyte;
- tunes on holdout or transport evidence;
- chooses a threshold from AUC, net benefit, code behavior, or an agent output alone;
- reports a suppressed subgroup metric;
- attributes transport change to the pandemic, laboratory, population, or workflow without evidence;
- turns candidate flags into clinical alerts or orders; or
- claims local validity, fairness, safety, benefit, implementation readiness, or deployment authority.

Named clinical, survey-methods, calibration, equity, patient, accessibility, responsible-AI, and independent-reproduction reviews remain pending before alpha.
