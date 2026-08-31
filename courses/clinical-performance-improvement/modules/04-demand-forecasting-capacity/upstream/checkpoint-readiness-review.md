# Measures, variation, and bottleneck readiness review

## Decision chain

The accepted decision is to continue the fictional `CGH-ED-01` adult emergency service into demand forecasting and capacity analysis with conditions. One synthetic adult emergency encounter is the unit of flow. Public CMS and HHS files define measure families and historical aggregate context. They are not linked to the fictional service and do not describe its performance.

Module 01 pins the complete CMS timely and effective care release with 138,084 rows, the complete CMS complications and deaths release with 95,800 rows, and the complete HHS capacity release with 1,045,406 rows. The service charter, entry and exit clocks, measure families, owners, and claim boundaries remain unchanged. Module 01 contributes no course points and all 12 decision gates pass.

## Measure readiness

Module 02 contains 318,732 raw rows across nine linked synthetic operational tables. After 12 declared repairs, 43,628 encounters are accepted. They include 39,975 completed encounters and 3,653 left-before-seen encounters across 1,092 shifts and 52 weeks. Seventeen measure specifications preserve each numerator, denominator, clock, unit, exclusion, unavailable state, and interpretation limit. All 30 query checks pass.

Module 02 scores 20 of 20 and all 15 measurement gates pass. A changed source identity, event branch, repair, clock, denominator, support rule, or measure specification returns to Module 02 before this checkpoint can be rebuilt.

## Variation and safety readiness

Weeks 1 through 24 remain the provisional baseline and Weeks 25 through 52 remain the evaluation period. The accepted release uses four declared chart contracts: a p-chart for weekly left-before-seen proportion, an XmR chart for the weekly mean of shift median arrival-to-clinician time, an exact low-count Poisson u-chart for incident reports per 1,000 completed encounters, and an arrivals run chart without control limits. Three predeclared rules produce nine signal records.

The p-chart center is 8.13767 percent. The XmR center is 97.636958 minutes with limits of 90.485606 and 104.788311 minutes. The incident-report center is 9.895751 per 1,000 completed encounters. The arrival run-chart median is 853. The baseline XmR high run in Weeks 4 through 11 remains visible. A signal opens review and does not prove cause.

The safety audit keeps 894 known true events, 673 trigger true positives, 358 incident true positives, and 379 reviewed non-events or trigger false positives separate. Trigger sensitivity is 75.2796 percent, incident capture is 40.0447 percent, and trigger specificity is 99.0302 percent. The incident chart has no exact Poisson limit breach. Its low run in Weeks 33 through 42 remains a review prompt, not evidence of lower prevalence or better safety.

## Bounded process diagnosis

The accepted fictional diagnosis is limited to a roomed-to-clinician constraint on evening shifts in Weeks 35 through 44. The median is 49 minutes in baseline evening shifts, 66 minutes in the target window, 44 minutes in contemporaneous day and night shifts, and 49 minutes in recovery evening shifts. Queue, throughput, wait, balancing, and recovery evidence support the bounded stage and time-window statement.

The evidence does not establish root cause, staffing adequacy, clinician productivity, or a required intervention. In the target window, language-support has 401 eligible encounters and mobility-support has 242. Those cross-group comparisons are not supported. Full-release support cannot be borrowed for the narrow window.

E01 opens human clinical, flow, access, and safety review within one business day when its accepted signal and corroboration rules are met. It does not automate staffing, scheduling, routing, care, or implementation. Event-level serious harm can still trigger immediate human review even when a chart is quiet.

## Readiness decision

Module 03 scores 20 of 20 and all 18 diagnostic gates pass. The checkpoint total is 40 of 40: Module 02 contributes 20 points once and Module 03 contributes 20 points once. Module 01 is a required zero-point gate. All 18 checkpoint integrity gates also pass.

The accepted evidence may enter Module 04 demand forecasting and capacity analysis with conditions. Module 04 must freeze the Week 3 identities, measures, baseline, signal record, safety limits, bounded diagnosis, subgroup support, and E01 ownership before it declares a target, cutoff, horizon, or capacity question. Root cause remains not established. Staffing change, clinical action, automated action, and implementation remain prohibited. Machine learning remains reserved for Module 06.
