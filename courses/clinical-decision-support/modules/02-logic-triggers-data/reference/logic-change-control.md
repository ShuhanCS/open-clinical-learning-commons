# Logic change control

## Controlled objects

The controlled objects are service ID, hook, hook version, user context, input contract, terminology map, branch order, reason codes, suppression rules, candidate lookback, mock score fixture, mock threshold fixture, response transport, rule cases, and expected traces.

## Version rule

Any semantic change to a condition, comparison, time window, code, unit, branch priority, result, or reason code requires a new module logic version and complete rerun of all 16 cases. A wording-only correction may use a patch version if it changes no behavior or claim.

## Human approvals

- Clinical owner: eligibility, known-diabetes suppression, prior-testing lookback, patient consequence, and card wording.
- Interoperability owner: hook, request, response, FHIR references, and version compatibility.
- Terminology owner: code systems, value sets, units, statuses, and mappings.
- Methods owner: future target, predictors, model, calibration, and threshold analysis.
- Operations owner: idempotency, delivery, logging, silent failure, rollback, and recovery.
- Governance council: progression, threshold acceptance, implementation, and retirement.

## Invalidation and rollback

A changed input definition, terminology version, FHIR profile, hook version, service boundary, time rule, or expected trace invalidates the current fixture evidence. Restore the last accepted version, preserve the failed release, record the reason, and rerun the complete contract. Silent failure or an unexpected card result forces `revise` or `refer`.

## Current boundary

This change-control record governs curriculum artifacts only. It does not authorize a production change, clinical threshold, patient score, card, implementation, or deployment.
