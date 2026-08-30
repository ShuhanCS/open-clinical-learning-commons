# Feasible improvement brief

## Aim

Test whether a capacity-aware scheduling workflow can make the transition from discharge to wanted follow-up more reliable while preserving patient preference, safety, staff capacity, and discharge flow.

## Candidate change

Before discharge, screen each eligible person, document whether follow-up is offered, record preference and acceptance or decline, attempt scheduling within current capacity, document appointment status, and use a safe escalation route when the preferred pathway is unavailable. Do not force an appointment or treat lack of a source record as lack of need.

## Why this is feasible enough for leadership review

The task is a bounded workflow test, not a new clinical prediction program. It adds a small set of decision-relevant fields to an existing transition point. The site spread from Module 05 remains a measurement question: the global p-value is `0.27993975`, the known direct synthetic-site effect is zero, and site ranking is prohibited.

## Feasibility and unintended consequences

Leadership review must confirm scheduling capacity, workflow owner, clinical eligibility, language and communication support, patient preference, privacy, safe escalation, and staff time. The prospective test must watch discharge delay, documentation burden, unwanted appointments, cancellations, inequitable offer or completion, and substitution away from more appropriate care.

## Decision boundary

- Retrospective implementation authorization: `not authorized`
- Prospective leadership review: `supported with conditions`
- Model deployment: `not authorized`

The random forest does not change this proposal. Universal workflow measurement is still required because neither model observes the missing access states.
