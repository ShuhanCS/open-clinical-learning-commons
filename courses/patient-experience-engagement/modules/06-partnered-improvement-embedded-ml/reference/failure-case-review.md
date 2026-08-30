# Failure-case review

The generated review contains 22 held-out rows with a threshold disagreement, a factor-cap hit, or a factor difference of at least 0.50. Each record is a synthetic response case and carries no clinical story.

The transparent benchmark has 88 false positives and 51 false negatives at the fixed 0.60 threshold. The random forest has 85 false positives and 55 false negatives. Three evaluation respondents receive a transparent factor of 3.0; the ML factors do not reach the cap.

The model uses the same three fields as the transparent response cells. It intentionally omits assigned mode, health status, proxy status, and the synthetic item truth used by the known generator. Residual bias is therefore expected. Adding those fields after reviewing held-out results would violate the feature contract.

Unsupported subgroup metrics stay blank for the missing-language, uninsured, Asian, and other-or-multiple-race rows. These blanks do not prove equal performance. They record insufficient support.

No error pattern permits comment-text modeling, group-specific contact, patient targeting, official reporting, fielding, or deployment.
