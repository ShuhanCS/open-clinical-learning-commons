# Reference Module 03 progression decision

## Disposition

`accept with conditions`

## Accepted handoff

- Module 01 inputs and fingerprints unchanged.
- `LIN01` fit on 69 training rows in the 111-row conditional timing subset.
- `LOG01` fit on 224 training rows and 25 outcomes.
- Exact formulas, references, model matrices, coefficients, intervals, diagnostics, sparse-cell checks, and assumptions preserved.
- `LOG02` and `LOG03` remain interpretation exercises only.
- Validation and test were not used in model development.
- The training-prevalence baseline remains unchanged for Module 03.

## Conditions

1. The linear case remains conditional on recorded next-encounter timing and is not a full-cohort time-to-event result.
2. Residual and influence findings remain visible.
3. Logistic quantities remain odds or model-conditional probabilities and never become causal effects.
4. Extreme fitted probabilities and sparse cells remain review conditions.
5. Named R execution and reconciliation remain pending before alpha.
6. Module 03 must evaluate prediction with validation and one final test use; coefficient p-values do not select the model.
7. All evidence remains synthetic teaching evidence only.

## Return conditions

A changed Module 01 input, fit partition, outcome, formula, reference, transform, variance method, or interpretation quantity returns to Module 02 and requires a semantic-version decision.
