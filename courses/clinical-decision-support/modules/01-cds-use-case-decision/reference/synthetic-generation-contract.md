# Synthetic generation contract

- Synthetic service: `CGH-GIM-01`.
- Upstream candidate: `Synthea 4.0.0`.
- Upstream release: https://github.com/synthetichealth/synthea/releases/tag/v4.0.0
- Resource basis: `FHIR R4`.
- Decision support basis: `CDS Hooks 2.0.1`.
- Construction owner: `APP-4 Module 02 curriculum builder`.
- First generated clinical and workflow rows: `Module 02`.
- Module 01 generated clinical rows: `0`.

Module 02 must pin the exact Synthea executable or source identity, Java and exporter environment, configuration, seed, population size, output format, generation log, resource counts, bytes, hashes, and failures. A separate deterministic Commons layer must add the fictional service, encounter decision moment, event-time availability, prediction version, requests, responses, interactions, monitoring intervals, and known truth needed across APP-4.

Every resource and table must carry an explicit synthetic status. Public NHANES participants, identifiers, rows, or values cannot be copied into the synthetic service. The generator may be informed by public field structure, but public and synthetic identities remain separate.

The future release must include normal, boundary, missing, stale, inconsistent, duplicate, delayed, terminology-mismatch, version-mismatch, and silent-failure conditions. It must not encode a clinical target, threshold, action, or card wording until the responsible later module and human reviewers accept those contracts.

No generated artifact may enter a live EHR, clinical network, patient record, decision service, or production environment.
