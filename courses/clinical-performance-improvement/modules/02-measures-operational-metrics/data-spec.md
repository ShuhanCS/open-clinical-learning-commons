# Operational source and measure data contract

## Release identity

- Service: `CGH-ED-01`
- Service status: fictional adult emergency service
- Source release: `cgh-ed-01-operational-v1`
- Generator version: `0.1.0`
- Seed: `73002`
- Arrival range: `2024-01-01` through `2024-12-29`
- Coverage: 364 days, 52 weeks, three eight-hour arrival shifts per day
- Raw tables: 9
- Raw rows: 318,732
- Raw storage: immutable deterministic gzip CSV

## Raw tables

| Table | Grain | Rows | Required use |
|---|---|---:|---|
| encounters | one raw encounter row plus one seeded duplicate | 43,631 | accepted population, disposition, return linkage |
| process-events | one recorded state per encounter and time | 250,821 | linked clocks and event order |
| staffing | one synthetic role per arrival shift | 4,368 | valid hours and descriptive capacity ratios |
| queue-snapshots | one queue per 30-minute interval | 17,520 | queue conservation |
| safety-events | one true event or reviewed non-event candidate | 1,274 | trigger and incident capture diagnostics |
| calendar-demand | one arrival shift | 1,092 | demand reconciliation and later forecasting |
| scenarios | one predeclared scenario without results | 4 | preserve the later evaluation boundary |
| known-truth | one generated mechanism or null condition | 10 | later recovery checks and safety truth |
| defect-register | one seeded raw defect | 12 | declared repair and measure effect |

## Clean-layer rules

SQL must keep the raw layer unchanged, deduplicate stable keys, quarantine the public-like service identifier and underage row, recover only predeclared event clocks, retain an unavailable clinician clock, conserve queue arithmetic, reconstruct impossible staff hours, derive accepted shift demand, and keep all repair effects auditable.

Every accepted record must remain synthetic. No public hospital identifier or real patient record may be added. The public CMS and HHS sources inherited from Module 01 orient measure concepts only and are not linked to `CGH-ED-01`.

## Measure output rules

`encounter-measures.csv.gz` is one accepted encounter. Shift and weekly outputs use arrival attribution. Durations require valid clocks. Rates publish numerator and denominator support. Safety types remain separate. Subgroup comparisons publish counts and unavailable clocks. No output is a target, causal result, staffing recommendation, clinical claim, or implementation decision.
