# APP-4 Module 01 instructor notes

## Teaching purpose

The module slows learners down before model and prototype work. A decision support concept is not ready because a public dataset has predictors and an outcome. Learners must first say who receives support, when, for what action, with what alternative, and with what possible harm.

## Reference interpretation

The 16 full NHANES files are technically feasible for later historical evidence work. All parse, every file has unique `SEQN`, every cycle contains the four expected components, and the all-four intersections range from 6,401 to 7,199 participants. The source structure also changes. For example, the 2021-2023 DIQ file has 9 fields while earlier DIQ files have 54. Learners must treat the later cycle as a transport stress test, not as a seamless continuation.

The source release does not settle the clinical target, eligibility, exclusions, predictors, weight treatment, threshold, card wording, or action. Those require later methods work and named human review.

## Required discussion

- Why is the user a clinician rather than the model or the patient record?
- What exact decision moment exists before encounter close?
- How does "consider confirmatory testing" differ from a diagnosis or order?
- What would make no card safer than a card?
- What local evidence is absent from NHANES?
- What could fail silently in a later sandbox?
- Who can stop the concept before and after a threshold is proposed?

## Intervention cues

Stop and redirect the learner if the submission:

- treats `LBXGH` as a clinical diagnosis without a reviewed target contract;
- calls NHANES a local validation cohort;
- ignores survey design or combines cycles without a documented future weight decision;
- copies a public participant into the fictional service;
- chooses a threshold or reports model performance early;
- makes the card an automatic order, diagnosis, denial, or treatment action;
- treats missing input as normal or zero;
- calls a dismissal an error or alert fatigue without supporting evidence; or
- turns curriculum progression into permission for live evaluation.

## Open conditions before alpha

Named review is still required for the clinical concept and wording, NHANES survey methods, intended-use and input contract, FHIR and CDS Hooks teaching shapes, Synthea generation plan, patient and workflow consequences, privacy, accessibility, responsible AI, and independent reproduction.

Joe Joseph, MD, SFHM, is designated for Module 07 under the accepted dated identity boundary. Module 01 does not imply his review, participation, or endorsement.
