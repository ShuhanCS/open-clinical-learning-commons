# Prototype architecture

## Decision boundary

The prototype answers one question: can a local synthetic teaching fixture reproduce its declared normal and failure behavior with an inspectable trace?

It does not answer whether a clinical tool should exist, whether `0.03000000` is a useful threshold, whether the card belongs in a real workflow, or whether an implementation is safe.

## Components

1. `build_sandbox.py` verifies the accepted Module 04 files and generates all local fixtures.
2. `requests.ndjson.gz` records each CDS Hooks-shaped request and its embedded prefetch.
3. `prefetch-resources.ndjson.gz` exposes each FHIR R4-shaped teaching resource separately.
4. The local evaluator applies ordered branches with no server or network call.
5. `responses.ndjson.gz` records transport state, body, human notice, and observed outcome.
6. `trace-events.csv.gz` records request receipt and terminal branches.
7. The visibility audit compares request, response, terminal trace, and human notice evidence.
8. The accessibility audit blocks a malformed card before release.

## Trust boundaries

- All patient IDs begin with `SP` and refer only to Commons synthetic fixtures.
- No request contains `fhirServer`.
- The runtime has no listener, network client, credentials, or external dependency.
- FHIR and CDS Hooks structures are teaching shapes, not conformance artifacts.
- The candidate card contains no suggestion, order, external link, or clinical action.
- The threshold remains unaccepted and the design remains a mechanics fixture.

## Failure visibility

Missing, stale, inconsistent, delayed, terminology, unit, score, and model-version states return a visible teaching status. Unsupported hook or service, service unavailability, and response timeout return a visible OperationOutcome-shaped body. The silent-failure case has a received request but no response, terminal trace, or human notice, so the independent audit detects it.

## Human control

The governance council owns progression. A passing package permits Module 06 curriculum construction only. It does not permit silent-mode evaluation, real-patient scoring, implementation, production connection, or deployment.
