# Leadership evidence synthesis

## Decision and source boundary

The fictional `CGH-ED-01` adult emergency service asks whether it should propose a bounded test of a staffing and fast-track redesign. Public CMS and HHS sources contribute definitions and historical aggregate context. Synthetic service data support the linked teaching analysis. No public hospital is linked to the fictional service, and no result describes current real operations.

## Technical performance block

The accepted release contains 43,628 encounters: 39,975 completed and 3,653 left before seen. Weeks 1 through 24 are a provisional baseline. Four chart families and three signal rules produce nine signal records. The clinician-delay XmR baseline has a high run in Weeks 4 through 11, so it is not treated as a stable permanent process model.

The safety audit retains 894 known true events, 673 trigger true positives, 358 incident true positives, 379 trigger false positives, 75.2796 percent trigger sensitivity, 40.0447 percent incident capture, and 99.0302 percent trigger specificity. The low incident-report run does not prove safer care.

A roomed-to-clinician constraint is supported for evening shifts in Weeks 35 through 44. The accepted medians are 49 minutes at baseline, 66 in the target window, 44 in contemporaneous day and night shifts, and 49 in recovery. Root cause and staffing adequacy are not established. Target-window language-support and mobility-support counts are 401 and 242, below the 1,000-encounter teaching threshold for a supported comparison.

## Forecast and capacity block

The target is accepted arrivals per eight-hour shift, issued at the end of each completed week for the next 21 shifts. The evaluation uses 28 rolling origins and 588 common target rows per method. Seasonal exponential smoothing remains accepted with MAE 5.937283, RMSE 7.307180, bias 0.008215, and WAPE 15.141268 percent.

Week 53 has a point forecast of 876.924084 arrivals and an empirical actual-equivalent range of 805.136639 to 970.733035. Difficult folds and unsupported error slices remain visible. Little's Law equilibrium is not established. Capacity conversions are planning implications, not staffing recommendations.

## Scenario and evaluation block

S00 through S03 are tested under C01 through C05 in 4,000 paired runs. The release contains 20 scenario-condition summaries and 15 option effects. Six comparisons are null or failed, and no option qualified.

S01 improves point-demand P90 wait by 21.244986 minutes but improves median wait by only 1.958703 minutes, below its rule. S02 worsens median wait by 5.803341 minutes and P90 wait by 41.617987 minutes at point demand, and worsens median wait by 86.671644 minutes under slower-service stress. S03 improves point-demand median wait by 0.316383 minutes and P90 wait by 14.547388 minutes, below both rules.

Safety and return within 72 hours were not simulated. Flex hours are modeled resource use, not staffing recommendations. Simulation does not establish causal effect or implementation readiness.

## Feasibility, monitoring, and ML block

The 28 feasibility rows contain five supported, 18 requires-local-evidence, and five not-supported statuses. S00 is retained as the monitoring baseline. S01 and S03 require revision before reconsideration. S02 is stopped in its current form.

The monitoring package contains 12 measures, including three prospectively unavailable values, and ten human-owned escalation rules. All rules retain no-change monitoring as fallback and create zero automatic actions. The static dashboard is an accessible planning artifact with no live connection or automatic alerting.

The fixed untuned gradient-boosted challenger uses the same 28 folds and 588 target rows as the transparent method. All 12 leakage and environment checks pass. Its MAE is 5.205494 and its Week 53 total is 860.277096. R01 requires at least 0.750000 arrivals per shift of MAE improvement; the observed improvement is 0.731788. Seven of eight rules pass, so the transparent forecast remains accepted.

## Leadership conclusion

The evidence supports a complete curriculum package and an accountable leadership discussion. It does not support a current test protocol. The recommendation is `revise before testing`. Local clinical, safety, access, workforce, workflow, capacity, ownership, and prospective-data evidence must be supplied before a new scenario contract can return for review.

Clinical action, staffing and schedule changes, automation, testing, implementation, production scoring, and model deployment remain prohibited.
