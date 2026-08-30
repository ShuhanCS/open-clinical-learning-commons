# Eight-minute technical handoff

## 1. Source and permitted use

The source is the pinned public synthetic Synthea April 2020 release. The toolkit is for technical education and downstream method development, not real clinical inference or production use.

## 2. Schema and grain

Module 02 preserves 16 relational source tables. The accepted analytic release has one row per selected synthetic person and one unique index encounter, with 374 rows and 29 fields.

## 3. Cohort and denominator

Module 03 selects 1,048 eligible adult acute events and one index for 374 adults. Every registered rate uses 374 unless an available-case descriptive field explicitly names a smaller denominator.

## 4. Analytic-table construction

Four read-only SQL files define eligible events, deterministic index selection, a one-row-per-person table, and validation. Separate history aggregates prevent join multiplication.

## 5. Most consequential quality issue

A duplicate person row changes the analytic grain and denominator. D01 deliberately tests that failure; it is resolved in the separate defect layer. N01 through N08 remain visible conditions.

## 6. Descriptive evidence and limit

The release contains 17 profiles, two complete cross-tabs, six rates, two unadjusted strata, and 27 denominator records. Wilson intervals are descriptive synthetic-cohort arithmetic, not real-population inference.

## 7. Accessibility path

F01 through F03 each have PNG, SVG, exact CSV, structured alternative, registry mapping, and non-color cues. The release preserves grayscale, size, zoom, reading-order, and equivalence checks.

## 8. Reproduction and validation

The toolkit contains pinned requirements and the exact database, cohort, quality, descriptive, and figure source files. A receiver starts from the verified archive, uses new targets, and compares accepted outputs by bytes and SHA-256 before complete toolkit validation.

## 9. AI-assisted step and human checks

The material audit checks the claim that 263 no-next-encounter rows must retain blank companion fields. Standard-library inspection and accepted N03 and VP14 evidence support the claim. The clinical analytics reviewer owns the final wording.

## 10. Recommended disposition and conditions

Recommend `accept with conditions`. Preserve immutable fingerprints, N01 through N08, exact denominators, equivalent access, synthetic scope, named human review, and independent reproduction. Any changed evidence, restricted data, broken access route, or unsupported claim triggers revision or referral.
