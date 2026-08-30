# Reproducibility check

- Environment: `python 3.12; numpy 2.0.2; pandas 3.0.3; scikit-learn 1.9.0; statsmodels 0.14.6`
- Source access: `read-only accepted CSV extracts`
- Random seed: `20260830`
- Bootstrap replicates: `1000`
- Split randomness: `none`
- Output result: `15 files; two complete builds match byte for byte`
- Existing-target result: `rejected`
- Changed-cohort result: `rejected`
- Changed-care-pattern result: `rejected`
- Changed-expected-outcome result: `rejected`
- Changed-contract result: `rejected`
- Changed-output result: `rejected`
- Leaked-feature result: `rejected`
- Changed-split result: `rejected`
- Invalid-progression result: `rejected`

The reference and learner workspaces assemble from the same immutable controls. The learner package contains prompts and no generated reference outputs. The copied validator runs from the assembled reference package. The pathway SVG has exact CSV tables and a structured alternative.

Independent reproduction remains required before alpha review.
