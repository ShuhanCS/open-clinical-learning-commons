# Week 3 checkpoint defense

## Q01. What decision and unit of flow does this checkpoint preserve?

Answer: The checkpoint asks whether the accepted fictional service, measures, diagnostic, and human escalation rule may enter demand forecasting and capacity analysis. The unit is one synthetic adult emergency encounter from recorded arrival through recorded departure.

Evidence: `candidate/module-01/clinical-performance-charter.md` and `candidate/module-01/unit-of-flow.csv`.

Limit: Public aggregate files do not describe or identify the fictional service.

## Q02. How do the public and synthetic evidence remain separate?

Answer: The three public snapshots define measure families, source availability, and historical aggregate context. Synthetic local tables support the teaching analysis. Public hospital identifiers never enter the fictional service tables.

Evidence: `candidate/module-01/source-feasibility-interpretation.md`, `candidate/module-01/synthetic-service-declaration.md`, and `candidate/module-02/source-record.yml`.

Limit: No finding applies to a real hospital, patient, or workforce.

## Q03. Why are the Module 02 measures ready?

Answer: The release accepts 43,628 encounters after 12 declared repairs, preserves 17 complete measure specifications, and passes 30 query checks. Each rate retains its numerator, denominator, clock, unit, unavailable state, and interpretation limit.

Evidence: `candidate/module-02/measure-specifications.csv`, `candidate/module-02/defect-repair-log.csv`, and `candidate/module-02/outputs/query-checks.csv`.

Limit: Any changed rule returns to Module 02.

## Q04. Why do the four chart families fit their measures?

Answer: The p-chart uses a varying weekly encounter denominator, the XmR chart follows a continuous weekly summary, the exact Poisson u-chart preserves low counts and varying exposure, and the arrivals run chart avoids false control limits before seasonal adjustment.

Evidence: `candidate/module-03/chart-selection.csv` and `candidate/module-03/outputs/control-limits.csv`.

Limit: Module 04 owns seasonal and calendar adjustment for arrivals.

## Q05. What does the baseline instability change?

Answer: The Weeks 4 through 11 high XmR run means the provisional baseline is not treated as a stable permanent process model. It remains visible and limits causal or forecasting claims.

Evidence: `candidate/module-03/outputs/signal-audit.csv` and `candidate/module-03/performance-diagnostic.md`.

Limit: A signal is a review prompt, not a generated cause.

## Q06. What does the safety audit show?

Answer: It shows undercapture. Of 894 known true events, triggers recover 673 and incident reports recover 358. Trigger sensitivity is 75.2796 percent, incident capture is 40.0447 percent, and 379 reviewed non-events or false positives remain visible.

Evidence: `candidate/module-03/outputs/safety-surveillance.csv` and `candidate/module-03/safety-interpretation.md`.

Limit: Incident reports are not prevalence and the low run does not prove improvement.

## Q07. What bottleneck statement is supportable?

Answer: A roomed-to-clinician constraint is supported for evening shifts in Weeks 35 through 44 in the fictional release. The declared medians are 49 minutes at baseline, 66 in the target window, 44 in contemporaneous day and night shifts, and 49 in recovery.

Evidence: `candidate/module-03/outputs/process-stage-comparison.csv` and `candidate/module-03/outputs/bottleneck-reconciliation.csv`.

Limit: Root cause and staffing adequacy are not established.

## Q08. What subgroup comparison is unavailable?

Answer: The target-window language-support and mobility-support groups have 401 and 242 eligible encounters. They do not meet the 1,000-encounter teaching threshold, so a cross-group target-window claim is unavailable.

Evidence: `candidate/module-03/outputs/subgroup-window-support.csv`.

Limit: Full-release support cannot be borrowed for the narrow window.

## Q09. What does E01 authorize?

Answer: E01 opens human clinical, flow, access, and safety review within one business day when the accepted signal and corroboration conditions are met.

Evidence: `candidate/module-03/escalation-rule.md`.

Limit: E01 does not automate staffing, scheduling, routing, care, or implementation.

## Q10. How are the 40 points counted?

Answer: Module 01 contributes zero points and remains required. Module 02 contributes 20 points once. Module 03 contributes 20 points once. The sum is 40, and gates are not converted into points.

Evidence: `evidence-index.csv`, `candidate/module-02/measure-score.csv`, and `candidate/module-03/week3-score.csv`.

Limit: No score compensates for a failed gate.

## Q11. How does the checkpoint prove chain of custody?

Answer: The builder creates three accepted reference workspaces, copies 137 files, fingerprints each file, and preserves each nested manifest. Two reference assemblies match, the copied validator passes, and mutation routes fail.

Evidence: `candidate-manifest.csv` and `reproducibility-check.md`.

Limit: An upstream correction requires a new owning-module release and a rebuilt checkpoint.

## Q12. What may Module 04 do next?

Answer: Module 04 may begin demand forecasting and capacity analysis after it freezes the Week 3 evidence. It may declare a target, issue time, horizon, folds, benchmarks, and capacity question.

Evidence: `progression-decision.md` and the APP-3 course contract.

Limit: Module 04 may not establish root cause, change staffing, act clinically, automate action, implement a redesign, or introduce machine learning.
