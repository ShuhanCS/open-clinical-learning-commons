# Synthetic release interpretation

## Accepted release

`CGH-GIM-01-SYNTHETIC-2026-08-31-v1` is accepted for offline curriculum use. It contains 1,000 synthetic adults, 25 FHIR files, 811,803 resource rows, 1,549,494,665 canonical UTF-8 bytes, and 100,178,478 committed gzip bytes. Every JSON row parses.

The upstream generator is Synthea 4.0.0 at tag commit `0185c09ea9d10a822c6f5f3ef9bdcbcbe960c813`. It ran with the pinned Temurin 17.0.20.1+1 runtime, random seed `7400202`, clinician seed `7400203`, reference date `20260831`, end date `20260831`, population `1000`, age range `18-89`, Massachusetts geography, five years of history, one generator thread, FHIR R4 bulk output, and the US Core 7.0.0 exporter setting. Two clean generations produce manifest SHA-256 `0d3c4c11e5ab29284f312d76413f8e005fb957226039d324912f80af93dcf3c0`.

## Encoding normalization

The Windows bulk output contains Windows-1252 characters in provider names. The release builder parses that source encoding and writes canonical UTF-8 JSON with deterministic gzip timestamps. Resource values are preserved. Local paths and elapsed times are excluded from the deterministic generation log.

## Duplicate resources

The source has 11,109 duplicate IDs within file:

- `Location`: 2,829;
- `Organization`: 2,760;
- `Practitioner`: 2,760; and
- `PractitionerRole`: 2,760.

The duplicates are retained. A future normalized analytic layer must define one explicit resolution rule, report before and after counts, prove that conflicting representations are handled, and show that joins do not multiply patient or encounter rows.

## Teaching use

The full FHIR release supports resource inspection, provenance, terminology, event-time reasoning, join-cardinality checks, and data-quality exercises. Sixteen linked Commons fixtures support deterministic branch, suppression, and delivery-failure tests.

## Claim boundary

Synthea creates realistic-looking synthetic records, not real clinical evidence. This release does not establish prevalence, predictor validity, model performance, calibration, decision benefit, subgroup safety, local data availability, workflow fit, alert burden, patient consequence, fairness, or deployment readiness. The passing rule tests establish mechanics only.
