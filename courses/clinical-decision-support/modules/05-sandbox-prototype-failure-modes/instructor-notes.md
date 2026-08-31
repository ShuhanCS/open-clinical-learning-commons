# Instructor notes

## Teaching purpose

The learner has already reviewed evidence, burden, workflow, and equity. This module asks a narrower question: when the accepted teaching fixture runs, can a reviewer trace every branch and see when it fails?

Keep the prototype local. Learners inspect files and run Python commands. They do not start a web server, call an EHR, use real records, or send a clinical message.

## Suggested 16-hour sequence

| Block | Hours | Work |
|---|---:|---|
| Upstream freeze and architecture | 2.0 | verify Module 04, map trust boundaries, inspect runtime |
| FHIR-shaped prefetch | 2.5 | inspect Patient, Encounter, Observation, Condition, Bundle, and Parameters shapes |
| CDS Hooks-shaped requests and responses | 2.5 | trace hook, context, prefetch, card, empty-card, and OperationOutcome routes |
| Normal, boundary, repeat, and suppression tests | 2.0 | reproduce expected branches and explain no-card states |
| Input, terminology, unit, and version failures | 2.5 | compare visible status with hidden absence |
| Service, timeout, and silent-failure drill | 2.0 | reconcile four independent ledgers |
| Accessibility and authority review | 1.0 | block the malformed card and audit prohibited actions |
| Release and Module 06 handoff | 1.5 | run validation, make the human disposition, freeze evidence |

## Instructor checks

- Ask the learner to find one request in all four ledgers.
- Ask why an empty card array is not evidence of low risk.
- Ask why a request record alone cannot prove delivery.
- Ask how a visible timeout differs from the seeded silent failure.
- Ask what the sandbox proves and what it cannot prove.
- Stop the exercise if the learner adds a real endpoint, patient identifier, action suggestion, accepted threshold, or deployment claim.

## Reference findings

The release contains 31 cases, 184 prefetch resources, 31 response envelopes, and 61 trace events. All 31 declared tests pass. One silent failure is detected because its received request has no response, terminal trace, or human notice. One malformed card is detected and blocked before release.

The correct progression is `continue with conditions`. The result supports Module 06 curriculum construction only.
