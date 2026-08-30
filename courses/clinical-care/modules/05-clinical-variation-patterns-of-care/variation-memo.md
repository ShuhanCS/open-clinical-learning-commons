# Clinical variation memo

## Decision

The hospital medicine care-improvement council may continue designing a prospective pathway to improve the recording and delivery of timely scheduled follow-up. Module 05 does not identify a site to target and does not show that follow-up caused an outcome.

## Evidence base

The fixed cohort has 476 synthetic adults, 129 with recorded scheduled follow-up by day 30, and 87 later acute returns. Module 05 reads 1,694 encounter, 742 medication, 1,832 procedure, and 92 care-plan rows during days 31 through 365. The accepted expected probabilities sum to 86.99999984 after eight-decimal file rounding and are not refit.

## Main bounded finding

Recorded day-30 scheduled follow-up ranges from 0.22988506 at SITE-E to 0.37804878 at SITE-F. The absolute 0.14816372 spread crosses the curriculum's 0.10000000 operational threshold. The global Pearson chi-square p-value is 0.27993975, so the six-site table remains compatible with chance variation under the global test.

The operational range and the statistical result answer different questions. Neither establishes facility performance. SITE-A through SITE-F are deterministic synthetic labels, their known direct effect is zero, and the fixed display order is not a ranking. The result is useful only as a reason to measure the scheduling process prospectively with real workflow and access data.

## Exposure-pattern evidence

Among people with recorded follow-up by day 30, 105 of 129 have another scheduled-care record during days 31 through 365. Among people without a recorded day-30 follow-up, 328 of 347 have one. The absolute difference is -0.13129147, with a large-sample 95% interval from -0.20258420 to -0.05999874 and Fisher p = 0.00003899.

This is not evidence that early follow-up reduces later scheduled care. Care can move between time windows, the groups can differ in clinical pathways and need, and a record does not establish an appointment offer, access, attendance, quality, or benefit. The procedure-record difference is also large (-0.18597949), but the record mix includes pregnancy, screening, medication reconciliation, examination, and other pathways. It cannot be labeled better or worse care.

Recorded medication exposure differs by only -0.01713469, with an interval from -0.11693422 to 0.08266484. A medication row is not dispensing, possession, ingestion, persistence, or adherence.

## Clinical-subgroup evidence

Later acute return is recorded for 27 of 58 people whose index encounter is inpatient and 60 of 418 whose index encounter is emergency. The absolute difference is 0.32197657, with an interval from 0.18927501 to 0.45467814. This is a clinical-need and case-mix signal, not proof of discharge quality or a causal index-class effect. It reinforces the Module 04 rule that crude outcome comparisons need case-mix context.

## Measure fidelity

Only 17 of the 129 people with recorded scheduled follow-up have the exact `Medication Reconciliation (procedure)` description during days greater than 0 through 30. That 0.13178295 source-record proportion is not a validated medication-reconciliation completion rate. The source does not show every step in the AHRQ definition or whether missing documentation means missing care.

## Decision and next evidence

Carry one finding forward: synthetic teaching-site follow-up recording spans 14.82 percentage points, but the evidence does not identify a causal site problem. Module 06 should ask whether a prospective scheduling workflow reaches prespecified access groups, test a capacity-aware scheduling lever, and keep the transparent recorded-follow-up proportion with exact denominators as the simpler benchmark.
