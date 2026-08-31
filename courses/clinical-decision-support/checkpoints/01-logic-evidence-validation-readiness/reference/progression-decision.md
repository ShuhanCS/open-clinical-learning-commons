# Progression decision

- Progression: `continue with conditions`
- Checkpoint score: `40 of 40`
- Point source: `Module 02 20 points once plus Module 03 20 points once`
- Module 01 decision gates: `12 of 12 pass`
- Module 02 logic gates: `12 of 12 pass`
- Module 03 evidence gates: `12 of 12 pass`
- Checkpoint integrity gates: `20 of 20 pass`
- Failed gates: `none`
- Accepted clinical threshold: `none`
- Evidence candidates: `0.02, 0.03, 0.04, 0.05, 0.075, and 0.10; all unselected and unaccepted`
- Module 02 mock threshold: `0.20 rejected mechanics fixture`
- Module 04 permission: `permitted for curriculum construction`
- Module 04 scope: `alert burden, human factors, equity, less interruptive alternatives, no alert, and comparison of all six unaccepted evidence candidates`
- Module 05 permission: `prohibited until Module 04 passes`
- Diagnosis: `prohibited`
- Real-patient scoring: `prohibited`
- Clinical alerting: `prohibited`
- Clinical action: `prohibited`
- Implementation: `prohibited`
- Production connection: `prohibited`
- Deployment: `prohibited`
- Decision owner: `CGH-GIM-01 clinical decision support governance council, subject to named human review`

## Conditions

| ID | Condition | Owner | Required before |
|---|---|---|---|
| C01 | Confirm the clinical purpose, action wording, and nonaction | primary-care or endocrinology reviewer | alpha |
| C02 | Confirm the survey weights, strata, PSUs, pooling prohibition, and uncertainty method | NHANES survey-methods reviewer | alpha |
| C03 | Independently reproduce the transparent model, calibration, threshold, and transport evidence | biostatistics and calibration reviewers | alpha |
| C04 | Review FHIR R4, CDS Hooks, terminology, unit, time, suppression, and trace teaching shapes | clinical-informatics and interoperability reviewers | alpha |
| C05 | Review patient consequences, access, language, disability, privacy, and equity questions | patient, accessibility, privacy, and equity reviewers | Module 04 release |
| C06 | Quantify local-workflow proxies only with synthetic data and label them as teaching evidence | workflow and human-factors reviewers | Module 04 release |
| C07 | Compare all six candidates, a less interruptive alternative, and no alert without accepting a clinical threshold | clinical governance council | Module 04 release |
| C08 | Preserve suppressed subgroup performance and prohibit group-specific action | methods and equity reviewers | every later release |
| C09 | Verify agent-assisted records independently and preserve human ownership | responsible-AI reviewer and faculty owner | every release |
| C10 | Assign the official section and half-term dates and complete clean independent reproduction | program owner and independent reviewer | alpha |

Module 04 may begin only within the stated curriculum scope. This checkpoint does not authorize a prototype, real-patient score, clinical card, order, treatment, implementation, production connection, or deployment.
