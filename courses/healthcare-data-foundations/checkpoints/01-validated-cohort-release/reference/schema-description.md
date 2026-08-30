# Accessible schema description

## Database purpose

The database preserves the complete pinned Synthea April 2020 CSV sample for technical instruction. All people and clinical events are synthetic. The database supports schema, retrieval, and cohort exercises, not real clinical estimates.

## Table grains

| Table | One row represents | Key |
|---|---|---|
| patients | one synthetic patient | source `id` |
| organizations | one synthetic organization | source `id` |
| providers | one synthetic provider | source `id` |
| payers | one synthetic payer | source `id` |
| encounters | one synthetic encounter | source `id` |
| allergies | one allergy row | generated `source_row_number` |
| careplans | one care-plan row | source `id` |
| conditions | one condition row | generated `source_row_number` |
| devices | one device row | generated `source_row_number` |
| imaging_studies | one imaging-study row | source `id` |
| immunizations | one immunization row | generated `source_row_number` |
| medications | one medication row | generated `source_row_number` |
| observations | one observation row | generated `source_row_number` |
| payer_transitions | one patient-payer period | generated `source_row_number` |
| procedures | one procedure row | generated `source_row_number` |
| supplies | one supply row | generated `source_row_number` |

## Relationship reading

Patients parent all patient-linked records. Encounters connect organizations, providers, payers, and most clinical events. Payers also parent medication and coverage-period rows. Observation encounter is optional: 30,363 observation rows have no encounter reference. Other registered nonblank relationships have zero orphans.

## Minimized views

The patient, encounter, and observation views expose 27 core fields. They avoid default use of synthetic names, addresses, identifiers, provider details, costs, and coverage fields while leaving the full source available for justified work.

## Known structural limits

The source is synthetic and older. Nine tables need transparent source-row surrogates. Supplies has zero rows. Codes need source documentation. The three FHIR examples demonstrate shape and references but do not claim server or resource conformance.
