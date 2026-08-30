# Data and evidence specification

The module reads 13 immutable artifacts from accepted Modules 03 through 05. They cover split identity, model and threshold lock, transformed features, test predictions, confusion and calibration evidence, validity checks, forecast contract, temporal folds, forecasts, and aggregate errors.

No row is changed or refit. The builder stops if any accepted byte count or SHA-256 changes. Learner workspaces receive exact copies in `data/`.

## Allowed data

- public aggregate CDC data already represented by forecast outputs;
- documented Synthea and deterministic synthetic evidence already represented by prediction and validity outputs.

## Prohibited data

- protected health information;
- identifiable or linkable patient data;
- deidentified research data outside an approved governance route;
- workplace-confidential data;
- restricted licensed data without approval;
- passwords, tokens, cookies, keys, connection strings, or other secrets.

## Failure fixtures

`failure-fixtures.json` contains compact deterministic mutations, not copies of damaged accepted files. Each fixture has an ID, failure type, structured case, and exact expected rejection code.

## Boundaries

Passing tests do not establish clinical validity, fairness, safety, utility, or deployment readiness. An agent statement is not evidence until mapped to an accepted artifact and independently checked when material.
