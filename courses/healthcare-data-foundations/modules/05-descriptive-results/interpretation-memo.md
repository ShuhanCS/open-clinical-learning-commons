# Reference interpretation memo

## Source and cohort

The release describes 374 synthetic adults with one accepted acute-care index encounter each. The analytic source and all 28 Module 04 quality checks are pinned and passing. These results do not estimate a real hospital or patient population.

## One-variable findings

Age at index has a mean of 46.120321 years and median of 43.500000 years, with five accepted ages at least 100 retained under N04 (VP02). Prior-year encounter rows are right-skewed: mean 5.716578, median 3.000000, and maximum 187. Two supported counts above 100 remain under N05 (VP09).

## Availability

Next-event elapsed time is available for 111 recorded next encounters and structurally blank for 263 people with `No encounter recorded`. The available-case median is 15.958333 days; it is not a 374-person timing summary (VP14, N03).

## Cross-tab

Among 236 people with source gender F, 20 have the 90-day acute-return endpoint, 6 the synthetic-death endpoint, and 210 no acute return recorded. These are complete row counts and unadjusted row percentages, not evidence of a gender effect (CT01).

## Rates

Thirty-six of 374 people have any recorded acute return within 90 days, 9.625668 percent with a Wilson interval of 7.034020 to 13.038277 percent (RT05). The interval is descriptive arithmetic for this synthetic cohort, not a real-population estimate.

## Stratification

The acute-return count is 24 of 314 emergency indexes and 12 of 60 inpatient indexes (ST01, ST02). The table is unadjusted; differences may reflect synthetic case mix, construction, or chance and do not establish an index-class effect.

## Conditions and Module 06 handoff

Module 06 must retain N01 through N08, use exact released CSV rows, keep small internal cells available for review, call missingness and recorded events by their source-specific meaning, and preserve the unadjusted synthetic-data boundary.

Reference disposition: `accept with conditions`.
