# Week 6 checkpoint defense

## Q01. What target and issue time does the forecast preserve?

Answer: The target is accepted arrivals per eight-hour shift. The issue time is the end of the final shift in each completed week, before forecasting the next 21 shifts over 7 days.

Evidence: `candidate/module-04/forecast-plan.md` and `candidate/module-04/forecast-contract.json`.

Decision consequence: Module 07 must discuss demand in the accepted unit and horizon.

Limit: A changed target, cutoff, or horizon returns to Module 04.

## Q02. How was the forecast evaluated without future leakage?

Answer: F01 through F28 cover Weeks 25 through 52 after an initial Weeks 1 through 24 training period. Every eligible method uses the same 588 target shifts.

Evidence: `candidate/module-04/fold-audit.csv`, `candidate/module-04/outputs/folds.csv`, and `candidate/module-04/outputs/forecast-predictions.csv`.

Decision consequence: The accepted method comparison may enter leadership review.

Limit: These folds do not serve as a fresh future confirmation period.

## Q03. What forecast result and uncertainty are accepted?

Answer: Seasonal exponential smoothing has MAE 5.937283, RMSE 7.307180, bias 0.008215, and WAPE 15.141268 percent. Week 53 is 876.924084 arrivals with an empirical actual-equivalent range of 805.136639 to 970.733035.

Evidence: `candidate/module-04/outputs/error-summary.csv` and `candidate/module-04/outputs/forecast-findings.json`.

Decision consequence: Module 07 may use the point and range as bounded planning evidence.

Limit: The range is empirical, not a calibrated probabilistic interval.

## Q04. What capacity and staffing conclusion is supported?

Answer: Capacity tables describe planning implications under the accepted forecast. Little's Law equilibrium is not established.

Evidence: `candidate/module-04/outputs/capacity-implication.csv`, `candidate/module-04/outputs/littles-law-check.csv`, and `candidate/module-04/capacity-interpretation.md`.

Decision consequence: Leadership may identify questions that need local review.

Limit: Staffing recommendation and schedule change are not authorized.

## Q05. Did any scenario qualify?

Answer: No. S00 through S03 were tested under C01 through C05 in 4,000 paired runs, and the selected option remains none.

Evidence: `candidate/module-05/outputs/scenario-findings.json` and `candidate/module-05/scenario-comparison.md`.

Decision consequence: Module 07 receives no implementation candidate.

Limit: The least unfavorable option cannot be selected after the fact.

## Q06. Which failed scenario evidence matters most?

Answer: Six comparisons are null or failed. S01 misses its median wait rule. S02 worsens median and P90 wait at point demand and worsens median wait by 86.671644 minutes under slower-service stress. S03 misses both point-demand wait rules.

Evidence: `candidate/module-05/outputs/sensitivity-review.csv` and `candidate/module-05/outputs/scenario-findings.json`.

Decision consequence: Revision must address the failed rules and stress behavior.

Limit: Safety and return within 72 hours were not simulated.

## Q07. What are the four feasibility dispositions?

Answer: Retain S00 as the monitoring baseline, revise S01 before reconsideration, stop S02 in its current form, and revise S03 before reconsideration.

Evidence: `candidate/module-06/outputs/decision-change.csv` and `candidate/module-06/feasibility-review.md`.

Decision consequence: Module 07 may explain, recommend revision, or refer these dispositions.

Limit: A disposition is not implementation authority.

## Q08. Which measures are prospective or unavailable?

Answer: The plan has 12 measures. Nine have simulated or modeled planning values. Safety outcome, return within 72 hours, and workforce interruption or perceived-load baseline are prospectively unavailable.

Evidence: `candidate/module-06/outputs/monitoring-measures.csv` and `candidate/module-06/monitoring-stewardship.md`.

Decision consequence: Leadership must assign ownership for prospective collection before a future test decision.

Limit: Unavailable never means zero, favorable, safe, or not applicable.

## Q09. What do the monitoring and escalation rules authorize?

Answer: Twelve owned measures and ten human-owned escalation rules support investigation, pause review, clinical review, and interpretability review. Continued no-change monitoring is the fallback.

Evidence: `candidate/module-06/outputs/monitoring-measures.csv` and `candidate/module-06/outputs/escalation-fallback.csv`.

Decision consequence: Module 07 may confirm owners, cadence, and response levels.

Limit: The rules create zero automatic actions and do not start a test.

## Q10. What does the dashboard permit?

Answer: The static dashboard communicates the 12 exact planning measures for fictional service CGH-ED-01 with semantic headings, text states, an exact table, and narrow-screen support.

Evidence: `candidate/module-06/outputs/monitoring-dashboard.html` and `candidate/module-06/dashboard-review.md`.

Decision consequence: It may support a bounded leadership discussion.

Limit: It has no live connection, automatic alerting, clinical control, or production authority.

## Q11. Is the ML challenger comparable and leakage-bounded?

Answer: Yes. One fixed untuned GradientBoostingRegressor with seed 7300600 uses eligible issue-time features, training-only preprocessing, the same 28 folds, and the same 588 target rows. All 12 leakage and environment checks pass.

Evidence: `candidate/module-06/ml-contract.json`, `candidate/module-06/outputs/leakage-tests.csv`, and `candidate/module-06/outputs/ml-split-registry.csv`.

Decision consequence: The challenger may be compared under the predeclared replacement rules.

Limit: Feature importance is not causal and no production scoring is authorized.

## Q12. Why was the challenger not accepted?

Answer: R01 requires an MAE improvement of at least 0.750000 arrivals per shift. The observed improvement is 0.731788. Seven of eight rules pass, so the final decision is retain transparent forecast.

Evidence: `candidate/module-06/outputs/decision-change.csv` and `candidate/module-06/model-comparison.md`.

Decision consequence: Seasonal exponential smoothing remains the accepted method for Module 07.

Limit: Rounding, retuning, another model, or a post-hoc threshold cannot repair R01 inside this checkpoint.

## Q13. How are points and gates counted?

Answer: Module 04 contributes 0 points, Module 05 contributes 25 points once, and Module 06 contributes 0 points. All 18 Module 04, 20 Module 05, 22 Module 06, and 20 checkpoint gates pass.

Evidence: `evidence-index.csv`, `candidate/module-05/week6-score.csv`, and `checkpoint-gates.csv`.

Decision consequence: The cumulative Week 6 score is 25 of 25.

Limit: No score compensates for any failed inherited or checkpoint gate.

## Q14. What may Module 07 do?

Answer: Module 07 may conduct clinician leadership review, communicate the bounded recommendation, assign owners, require revision, or refer the package. The progression is continue with conditions.

Evidence: `progression-decision.md` and `module07-handoff.md`.

Decision consequence: Joe Joseph, MD, may lead the planned interpretation and defense unit once participation details are confirmed.

Limit: Module 07 may not rewrite the candidate or authorize clinical, staffing, automated, testing, implementation, production-scoring, or deployment action.
