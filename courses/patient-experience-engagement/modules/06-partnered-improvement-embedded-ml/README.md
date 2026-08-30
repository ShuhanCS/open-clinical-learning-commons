# APP-2 Module 06: Partnered improvement and embedded machine learning

This 16-hour module uses eight hours for patient partnership and improvement design and eight hours for a bounded response-model comparison. It finishes the technical Week 6 case without adding course points.

Learners use the accepted Module 03 through Module 05 evidence to prepare a patient-partner session, preserve interpretation and disagreement, design an accessible discharge-information and feedback proposal, and define implementation, process, response, outcome, access, burden, accountability, and safety measures.

The embedded ML exercise compares the exact 13-cell transparent response benchmark with one bounded random forest. Both methods use `age_band`, `other_language_at_home`, and `income_group`, the same fixed split, and response factors bounded from 1.0 through 3.0. The random forest improves held-out teaching-composite absolute bias by 0.08367520 percentage points, below the prespecified 0.50 threshold, and does not change the adjustment decision.

## Package map

- [Durable module specification](../../../../docs/curriculum/courses/APP-2/modules/06-partnered-improvement-embedded-ml-spec.md)
- [Reference workspace](reference/README.md)
- [Learner workspace prompt](template/README.md)
- [Model and improvement contract](module06-contract.json)
- [Patient-partner requirements](partner-contract.csv)
- [Feature contract](feature-contract.csv)
- [Release record](release.json)

Run these checks from the repository root:

```text
python courses/patient-experience-engagement/modules/06-partnered-improvement-embedded-ml/build_partnered_improvement_ml.py --self-check
python courses/patient-experience-engagement/modules/06-partnered-improvement-embedded-ml/build_workspace.py --self-check
python courses/patient-experience-engagement/modules/06-partnered-improvement-embedded-ml/validate_workspace.py --self-check
```

The reference partnership record is a labelled simulation. It contains no actual patient or caregiver statement. A named patient or caregiver partner, direct participation terms, and final review remain required before alpha. Comment-text modeling, patient targeting, group ranking, official HCAHPS reporting, fielding, clinical action, implementation, and model deployment are prohibited.
