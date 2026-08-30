# Reference FHIR JSON reading

The teaching mappings use FHIR R4 shapes derived transparently from the source CSV rows.

- Patient ID: `00185faa-2760-4218-9bf5-db301acf8274`.
- Encounter ID: `6b5bfe89-1c58-42e8-87c4-847b542d5f0b`.
- Observation ID: `synthea-observation-191026`.
- Encounter subject: `Patient/00185faa-2760-4218-9bf5-db301acf8274`.
- Observation subject: the same Patient reference.
- Observation encounter: `Encounter/6b5bfe89-1c58-42e8-87c4-847b542d5f0b`.
- Observation value: numeric with a nonempty unit.

Patient, Encounter, and Observation are nested resources with typed references, unlike flat relational rows joined by key columns. These three files are reading examples. They do not claim complete FHIR profiling, validation, terminology binding, server behavior, or conformance.
