# Accessibility review

- The Kaplan-Meier curve uses color and line style together.
- The y-axis spans zero through one and does not magnify a small difference.
- The title names the event and grouping variable.
- The x-axis states that time begins at the day-30 landmark.
- The footer identifies the synthetic teaching cohort.
- `km-risk-table.csv` is the authoritative structured alternative.
- `fixed-time-comparison.csv` gives exact estimates and intervals in one row per prespecified time.

Structured description: both groups begin at event-free probability 1. The scheduled-follow-up estimate is slightly higher at day 30, then lower at days 90, 180, 270, and 335. At day 335, event-free probability is 0.80620155 with scheduled follow-up and 0.82132565 without a recorded follow-up encounter. The changing direction is consistent with the failed proportional-hazards screen.
