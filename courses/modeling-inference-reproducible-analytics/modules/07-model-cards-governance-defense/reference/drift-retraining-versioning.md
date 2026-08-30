# Reference drift, retraining, and versioning

## Drift types and detection

- Data drift changes field distributions, ranges, missingness, or source identity.
- Label drift changes prevalence, timing, completeness, or outcome meaning.
- Calibration drift changes the relation between probabilities and observed frequency.
- Concept drift changes the relation between available predictors and outcome.
- Workflow drift changes when, by whom, or for what decision a prediction would be seen.
- Population drift changes eligibility, setting, representation, or transport assumptions.

The ten monitoring signals are simulated review contracts. They do not claim that live drift was observed.

## Review and retraining entry

No automatic retraining is permitted. A trigger begins investigation. Retraining requires a justified new population and decision, rights-cleared data, frozen target and prediction-time contract, new train/validation/test design, adequate events, subgroup and consequence plan, baseline comparison, uncertainty, failure testing, independent reproduction, rollback plan, and named approval. The current untouched test set cannot be reused as a tuning set.

## Version rule

Any retraining creates a new model version even when code is unchanged. Changed source or decision may require a major version; added compatible evidence or governance may require a minor version; documentation-only corrections may use a patch. The new candidate must preserve the prior release, compare against the safe fallback and prior model on preregistered evidence, define rollback, and receive a fresh package disposition and model-use recommendation.
