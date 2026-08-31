# Forecast, scenario, evaluation, and monitoring review

## Forecast decision

The target is accepted arrivals per eight-hour shift. A forecast is issued at the end of the final shift in each completed week for the next 21 shifts, or 7 days. The initial training period is Weeks 1 through 24. Evaluation uses F01 through F28 over Weeks 25 through 52, with 588 exact target rows for each eligible method.

Seasonal exponential smoothing remains accepted. Its MAE is 5.937283 arrivals per shift, RMSE is 7.307180, bias is 0.008215, and WAPE is 15.141268 percent. The Week 53 point forecast is 876.924084 arrivals. The empirical actual-equivalent planning range is 805.136639 to 970.733035 arrivals. Difficult folds and error slices remain part of the release. The interval is empirical, not a calibrated probabilistic interval.

Little's Law equilibrium is not established. The capacity tables are planning implications, not staffing requirements. Staffing recommendation is not authorized.

## Scenario and evaluation decision

Module 05 tests S00 through S03 under C01 through C05. It uses 200 paired replications for each scenario-condition cell, for 4,000 paired runs, 20 summaries, and 15 option effects. Six comparisons are null or failed. No option qualified.

At point demand, S01 improves P90 wait by 21.244986 minutes but improves median wait by only 1.958703 minutes, so its median rule fails. S02 worsens median wait by 5.803341 minutes and P90 wait by 41.617987 minutes. Under upper demand and slower service, S02 worsens median wait by 86.671644 minutes. S03 improves median wait by 0.316383 minutes and P90 wait by 14.547388 minutes at point demand, below both declared wait rules.

The prospective design contains 12 measures and eight threats. Safety and return within 72 hours were not simulated. Flex-clinician hours are modeled resource use, not a staffing recommendation. Simulation does not establish a causal effect or authorize implementation.

## Feasibility dispositions

The feasibility screen contains 28 scenario-domain rows: five supported, 18 require local evidence, and five are not supported. S00 is retained as the no-change monitoring baseline. S01 must be revised before reconsideration. S02 is stopped in its current form. S03 must be revised before reconsideration. A revised option returns through its owning assumptions, selection rules, safety and access review, and feasibility screen before any test decision.

## Monitoring and escalation

The monitoring plan contains 12 owned measures. Nine are simulated or modeled planning values and three are prospectively unavailable: safety outcome, return within 72 hours, and workforce interruption or perceived-load baseline. An unavailable value stays unavailable and never becomes zero, favorable, or safe.

Ten escalation and fallback rules specify a trigger, confirmation owner, decision owner, safeguard, fallback, documentation location, and restart condition. They create zero automatic actions. Continued no-change monitoring is the fallback. Thresholds open human review; they are not control limits, clinical orders, safe staffing levels, or automated alerts.

The dashboard is a static accessible planning artifact for the fictional service `CGH-ED-01`. It has a visible planning-evidence banner, one `h1`, logical headings, 12 cards, an exact table, text states in addition to color, and narrow-screen support. It has no script, external font, or external asset. It has no live connection or automatic alerting.

## Embedded-ML decision

The challenger is one fixed, untuned `GradientBoostingRegressor` with seed 7300600. It uses issue-time calendar, shift, lag, and completed-prior-week features. Categorical preprocessing is fit on each training fold only. All 12 leakage and environment checks pass. The transparent and challenger methods use the same 28 folds and 588 target rows.

The challenger MAE is 5.205494, RMSE is 6.554934, bias is -0.513059, and WAPE is 13.275060 percent. Weighted error cost is 4742.085347 versus 5234.268116 for the transparent method, a 9.403087 percent improvement. All four difficult folds pass their no-worse rule. Its Week 53 total is 860.277096, inside the accepted 805.136639 to 970.733035 range.

Replacement requires all eight rules. R01 requires an MAE improvement of at least 0.750000 arrivals per shift. The observed improvement is 0.731788. Seven rules pass and R01 fails, so the decision remains `retain transparent forecast`. Feature importance describes model allocation, not cause. The largest underforecasts and overforecasts remain visible, and a future challenger still needs a fresh confirmation period.

## Checkpoint conclusion

The package is complete for clinician leadership interpretation. Module 05 contributes 25 points once. Module 04 and Module 06 remain required zero-point gates. All 18 Module 04, 20 Module 05, 22 Module 06, and 20 checkpoint gates pass. The progression is `continue with conditions`.

No redesign, staffing change, clinical action, automated action, test, implementation, production scoring, or model deployment is authorized.
