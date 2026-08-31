# Monitoring and silent-failure plan

The plan retains all 20 accepted measures. Each measure keeps its unit, numerator or origin, denominator, window, cadence, direction, teaching trigger, unavailable state, human response, owner, and claim limit. Module 07 may explain their decision use but may not change their definitions or thresholds.

Monitoring covers eligibility, input availability, candidate state, suppression, burden, repeat exposure, response, latency, visible errors, silent failure, outcome availability, calibration, drift, subgroup support, version, accessibility, incidents, overrides, fallback, and retirement review.

## Silent failure

- Definition: a received request with no response, no terminal trace, and no human notice.
- Independent ledgers: request, response, terminal trace, and human notice.
- Trigger: one or more reconciled silent failures.
- Owner: patient-safety owner.
- Cadence: daily and after every declared test run in a future approved environment.
- Unavailable state: report reconciliation unavailable and stop the affected evaluation.
- Human action: verify all four ledgers, preserve the event, escalate, and investigate.
- Rate claim: none; the seeded event does not estimate a clinical rate.

## Decision boundary

All 12 escalation routes require human confirmation and decision ownership. Automatic actions total zero. Monitoring thresholds are teaching triggers, not validated control limits. No monitoring record grants permission to begin silent mode, score a patient, issue an alert, or act clinically.
