# Reference eight-minute technical handoff

1. Decision and use boundary: the candidate is technically acceptable with conditions; model use is teaching only.
2. Source, grain, target, prediction time, and split: 374 synthetic index-encounter rows; 90-day acute return predicted at encounter stop; 224/75/75 with 25/7/4 outcomes.
3. Baseline, model, test counts, and uncertainty: baseline 0.111607142857; `ML01`; ROC AUC 0.58802817 with wide 0.26760563 to 0.91549296 interval; 48/23/2/2.
4. Calibration, threshold, subgroup, and validity: Brier 0.05097579; threshold 0.08513264; five subgroup rows suppressed; prediction is not causal and validity conditions remain.
5. Public forecast and coverage limits: 94 Massachusetts jurisdiction weeks; damped-Holt MAE 14.99587157; changing reporting coverage and weak fold prevent operations use.
6. Tests, failures, agent audit, and independent checks: 18 accepted tests; ten intended failure rejections; three independent checks; four claims adjudicated.
7. Monitoring, stop, rollback, retirement, and fallback: ten simulated signals; changed identity, leakage, failed tests, prohibited data or claims stop use; safe fallback is no model or forecast action.
8. Package disposition and model-use recommendation: `accept with conditions` and separately `teaching use only`; named live review remains pending.
