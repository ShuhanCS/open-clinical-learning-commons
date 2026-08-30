# Reference Module 02 progression decision

## Disposition

`accept with conditions`

## Evidence

- The accepted FND-1 input matches 121787 bytes and SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.
- The modeling cohort preserves 374 unique people and 374 unique index encounters.
- Prediction time is the index encounter stop.
- Nine default predictors are allowed and all post-index or outcome-derived fields are blocked.
- The temporal split is exactly 224/75/75 with 25/7/4 positive outcomes.
- The training-prevalence baseline is frozen at `0.111607142857`.
- The deterministic builder and validator self-checks pass.

## Conditions inherited by Module 02

1. The source is synthetic and does not support a real clinical or population estimate.
2. The split and field roles are immutable until a versioned return to Module 01.
3. The test set remains unavailable for fitting or selection.
4. Sparse source categories require explicit uncertainty and reporting review.
5. High-cardinality code, description, and reason fields remain excluded.
6. Any changed row, field role, prediction time, target, horizon, or split requires a new Module 01 disposition and semantic-version decision.

## Handoff

Module 02 receives `modeling-cohort.csv`, `split-registry.csv`, `baseline-metrics.csv`, `feature-role-contract.csv`, `estimand-target-registry.csv`, the exact environment record, source record, build report, validator, and this decision.
