# Scenario data contract

## Accepted upstream

- Module 04: `oclc-app3-04` version `0.1.0`, Commons `0.70.0`.
- Forecast: 876.924084 Week 53 arrivals, with empirical range 805.136639 to 970.733035.
- Accepted population: 43,628 synthetic adult emergency encounters.
- Service: fictional `CGH-ED-01`.
- Scenarios: S00 through S03 from the accepted Module 02 source register.
- Scenario known truth: Module 02 contains no generated scenario results and requires at least one null or failed sensitivity condition.

Module 05 does not alter the Week 3 population, measures, charts, signals, safety interpretation, bottleneck diagnosis, support rules, escalation rule, Module 04 target, folds, selected forecast, errors, or planning range.

## Simulation grain

| Object | Grain |
|---|---|
| Patient input | one synthetic arrival |
| Scenario run | one scenario, condition, and paired replication |
| Scenario summary | one scenario and condition across 200 replications |
| Paired effect | one redesign and condition relative to S00 |
| Evaluation measure | one proposed prospective measure |
| Evaluation threat | one threat, detection rule, and response |

The model runs a seven-day warm-up followed by a seven-day measurement week. Warm-up arrivals affect the starting queue but do not enter reported outcomes.

## Source roles

Encounter measures supply synthetic acuity, support-group, preparation-delay, and service-time donor profiles. Accepted shift metrics supply demand thresholds. Accepted staffing supplies the base clinician-slot schedule. The Week 53 forecast supplies the demand shape and lower, point, and upper totals.

The 20 percent effective-service factor is a teaching proxy for intermittent clinician work within the observed clinician-to-departure interval. It cannot be used to rate productivity or calculate real staffing.

## Unmodeled outcomes

The scenario has no validated causal mechanism for safety events or 72-hour returns. Every result must label both outcomes `not simulated; prospective measurement required`. Omission or a favorable claim fails the release.

## Claim boundary

The release may compare bounded synthetic scenarios under declared assumptions and propose a future evaluation. It cannot establish a real intervention effect, staffing need, safe staffing level, productivity, clinical benefit, safety, equity, feasibility, causal effect, automated action, or implementation authority.
