# Support and suppression review

The reporting rule requires at least 50 people, 10 observed events, 10 expected events, both exposure groups, and every synthetic risk tier at a site. Passing those minimums permits reporting with caution. It does not make a comparison precise, fair, or suitable for ranking.

| Site | People | Observed | Expected | Standardized rate | 95 percent interval | Decision |
|---|---:|---:|---:|---:|---:|---|
| SITE-A | 76 | 21 | 14.05522752 | 0.27308240 | 0.16904231 to 0.41743546 | report with caution |
| SITE-B | 75 | 10 | 13.92373871 | 0.13126726 | 0.06294776 to 0.24140517 | report with caution |
| SITE-C | 68 | 10 | 10.90777066 | 0.16756230 | 0.08035263 to 0.30815303 | report with caution |
| SITE-D | 88 | 13 | 15.02338779 | 0.15815677 | 0.08421182 to 0.27045289 | report with caution |
| SITE-E | 87 | 18 | 17.02000034 | 0.19329706 | 0.11456009 to 0.30549268 | report with caution |
| SITE-F | 82 | 15 | 16.06987500 | 0.17060473 | 0.09548617 to 0.28138655 | report with caution |

SITE-B and SITE-C meet the observed-event minimum exactly. SITE-C is also close to the expected-event minimum. Their estimates remain visible because the rule was fixed in advance, but the borderline support is part of the interpretation.

The figure keeps SITE-A through SITE-F in fixed order. Color is not needed to identify a site, the cohort event rate has a separate line style, and `site-comparison.csv` is the authoritative structured alternative. The Poisson intervals treat expected counts as fixed and do not include model-estimation uncertainty.
