# Candidate design review

## Required comparison

| Evidence candidate | Synthetic cards | Cards per session | Repeat cards | Banner interruptions | Passive-panel interruptions | NHANES holdout flags per 1,000 | NHANES holdout missed per 1,000 | Sandbox mechanics |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0.02000000 | 116 | 0.9667 | 16 | 116 | 0 | 661.57323641 | 2.99863880 | at least 10 positive cases |
| 0.03000000 | 12 | 0.1000 | 1 | 12 | 0 | 325.40301123 | 11.59062056 | at least 10 positive cases |
| 0.04000000 | 3 | 0.0250 | 0 | 3 | 0 | 172.19709642 | 18.50350918 | fewer than 10 positive cases |
| 0.05000000 | 3 | 0.0250 | 0 | 3 | 0 | 105.90526558 | 22.40498219 | fewer than 10 positive cases |
| 0.07500000 | 0 | 0.0000 | 0 | 0 | 0 | 36.68485865 | 27.19881351 | no positive cases |
| 0.10000000 | 0 | 0.0000 | 0 | 0 | 0 | 17.08750038 | 27.92703988 | no positive cases |

No alert produces zero cards and zero interruptions. In the historical temporal holdout, it leaves the full weighted event prevalence of 29.04272000 per 1,000 unprompted by design. That comparison does not prove that an alert is better, safer, or clinically useful.

## Interpretation

The public and synthetic quantities are not interchangeable. The NHANES columns describe historical classification tradeoffs. The synthetic columns describe one scripted workload. The zero-card results at 0.075 and 0.10 show that the synthetic score distribution differs from the public evidence. They do not validate those thresholds.

At 0.02, the scripted banner would add 116 interruptions and 16 repeat cards. At 0.03, the passive panel supplies 12 positive cases across 10 sessions without scripted interruption. Most access and equity slices at 0.03 remain suppressed, and 39 candidate-frame encounters have unavailable inputs across every design.

## Human-governed sandbox recommendation

- Design: `panel-t003`.
- Role: passive contextual panel fixture for Module 05 mechanics only.
- Threshold role: `0.03000000` remains an unaccepted sandbox fixture.
- Reason to prototype: 12 scripted positive cases permit normal, repeat, unavailable, view, dismissal, deferment, acknowledgment, and unresolved tests without choosing the 116-interruption banner route.
- Conditions: preserve every unavailable state, test language and disability access, show uncertainty and nonaction, keep human override, count repeat exposure, and stop if the panel implies diagnosis, ordering, treatment, or accepted threshold status.
- Rejected authority: no real-patient scoring, no clinical threshold acceptance, no clinical alerting, no silent-mode evaluation, no implementation, no production connection, and no deployment.
