# Module 06 instructor notes

## Teaching purpose

The module should change the question from "Who is first?" to "What does the source support us doing?" The point rank is useful because it exposes how readily a precise order appears. The interval and CMS comparison category then show how little of that order supports a benchmark claim.

## Opening move

Show `C1-point-only-league-table.png` without its caption. Ask learners to name the action it implies. Most groups will accept the top ten as a review list. Then reveal that nine of the ten are CMS-classified no different from the national rate.

Do not start with formulas. Start with the committee consequence, then inspect the source fields that change it.

## Verified release facts

### National selected measure

| Quantity | Value |
|---|---:|
| Hospital rows | 4,790 |
| Reported scores | 3,253 |
| No different from national | 3,194 |
| Worse than national | 38 |
| Better than national | 21 |
| Number of cases too small | 1,020 |
| Not available | 517 |
| National rate | 21.3 |
| Reporting period | 2023-07-01 to 2025-06-30 |

The national summary separately publishes 38 worse, 3,253 same, 21 better, and 1,121 too few. Preserve those values as source facts. Do not force the national summary into a reconstruction from one hospital display field.

### Massachusetts

| Quantity | Value |
|---|---:|
| All rows | 65 |
| Reported | 53 |
| No different | 52 |
| Worse | 1 |
| Better | 0 |
| Too few | 2 |
| Not available | 10 |
| Reported denominators | 30 to 2,088 |
| Median denominator | 538 |
| Reported denominator under 100 | 4 |
| Point estimates | 19.7 to 25.2 |
| Interval widths | 6.9 to 9.2 |

## Top-ten answer key

| Rank | Hospital | Denominator | Score | Source interval | CMS comparison |
|---:|---|---:|---:|---|---|
| 1 | Saint Anne's Hospital | 467 | 25.2 | 21.4 to 29.6 | Worse |
| 2 | Heywood Hospital | 247 | 24.8 | 20.6 to 29.8 | No different |
| 3 | VA Boston Healthcare System - Jamaica Plain | 538 | 24.7 | 20.7 to 29.2 | No different |
| 4 | Good Samaritan Medical Center | 807 | 24.0 | 20.2 to 28.3 | No different |
| 5 | Cape Cod Hospital | 1,094 | 23.6 | 19.8 to 27.9 | No different |
| 6 | Holyoke Medical Center | 342 | 23.6 | 19.8 to 27.9 | No different |
| 7 | Signature Healthcare Brockton Hospital | 194 | 23.6 | 20.2 to 27.8 | No different |
| 8 | UMass Memorial Health - Harrington Hospital | 368 | 23.5 | 19.7 to 27.7 | No different |
| 9 | Baystate Franklin Medical Center | 289 | 23.3 | 19.5 to 27.9 | No different |
| 10 | Winchester Hospital | 646 | 23.3 | 19.5 to 27.6 | No different |

The lowest point estimate is Massachusetts General Hospital at 19.7, with source endpoints 16.4 and 23.3. It is no different from the national rate.

## Descriptive overlap

All 1,378 pairs among the 53 displayed Massachusetts intervals overlap. This is a memorable visual fact, but it is not a pairwise hypothesis test. Do not accept "none of the hospitals differ" as the answer. The defensible statement is that the display does not establish pairwise separation and the source categories compare each hospital with the national rate.

## Recommended decision

Recommend a focused review for Saint Anne's Hospital because CMS classifies it as worse than the national rate in this release. Request local validation before treating the result as a quality failure. Useful evidence includes current encounter-level outcomes, risk factors, coding, transfer patterns, follow-up access, medication reconciliation, discharge planning, and care-transition processes.

The other high point estimates may be monitored or reviewed using local criteria, but their rank alone does not support the same worse-than-national label. The 12 unavailable rows require footnote review and local evidence.

## Short-answer key

1. Any unequal point estimates can be sorted, so ranks exist even without evidence of meaningful separation.
2. One of the top ten is CMS-classified worse.
3. No. Visual overlap does not prove equivalence and does not perform a pairwise test.
4. Zero is a possible rate and would falsely report performance that CMS did not publish.
5. The score is risk standardized and is not a raw binomial proportion.
6. Ask for more recent local data, measure validation, case mix, coding, transition processes, and clinical review.
7. A benchmark comparison tests or classifies each estimate relative to a common reference; pairwise comparison asks about the difference between two hospitals.
8. A funnel or control chart needs a defined data-generating model, expected value, variance or standard error, independence assumptions, and a justified limit rule.

## Facilitation cautions

- Do not call the source endpoints 95% confidence limits unless a CMS method citation for this release is added.
- Do not let learners calculate a binomial interval from `Denominator`.
- Do not imply that a wider interval always belongs to the smallest denominator. The released risk-standardized model includes more than sample size.
- Do not treat CMS's national rate as the committee's clinical goal without a separate decision.
- Do not hide Veterans Health Administration or unavailable rows to make the table cleaner.
- Keep the measure dates visible. Public quality data lag current operations.

## Critique key

### Point-only league table

Expected defects include a verdict-like title, truncated selection, zero baseline that magnifies bar area, no source interval, no national rate, no denominator, no reporting dates, one alarming color for every row, and no missingness account.

### Hidden small numbers

Expected defects include identical point sizes, missing denominators, missing source intervals, missing benchmark, missing source status, and a generic performance title. The repair should show the interval and denominator without inventing a suppression cutoff.

## Accessibility review

The reference charts use shape and color for status, but the instructor must still inspect print and grayscale output. Learners may replace the palette. They may not remove the redundant channel or exact-value table.

## Week-3 checkpoint review

The checkpoint should contain four final figures: comparison, distribution, rate, and uncertainty. Require at least two sources. Verify that each figure still has a named audience, decision, units, provenance, and editable analysis after assembly. The uncertainty figure must retain the interval, national rate, reporting status, and pairwise-test boundary.

## Handoff to Module 07

Carry forward `02-interval-caterpillar.png`, the comparison categories, and the alt-text draft. Module 07 tests color, contrast, shapes, direct labeling, grayscale, and text alternatives without changing the statistical claim.
