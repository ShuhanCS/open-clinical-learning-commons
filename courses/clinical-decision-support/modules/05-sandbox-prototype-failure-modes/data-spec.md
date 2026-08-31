# Data specification

## Purpose

This module turns the accepted Module 04 passive-panel fixture into inspectable local files. It tests message shape, branch behavior, trace completeness, visible failure, silent failure, latency, version handling, and accessibility. It does not test a live service or a real patient.

## Accepted upstream release

The workspace freezes the complete 302-file Module 04 reference workspace. Its immutable manifest has 285 rows, 60,302 bytes, and SHA-256 `41692b01fa2c339068fcdbf5fbc6f3e301a79ba4535d9ecb94d602cb2e4b3bf9`.

The sandbox preserves:

- design `panel-t003`;
- threshold `0.03000000` as an unaccepted fixture;
- all 12 positive Module 04 cases, including one repeat;
- all six evidence candidates and the rejected `0.20` fixture inside the upstream release;
- the Module 04 score of 25.00 points and all 20 gates; and
- every prohibition on clinical or production use.

## Generated files

| File | Grain | Rows | Role |
|---|---|---:|---|
| `data/sandbox/requests.ndjson.gz` | one sandbox case | 31 | CDS Hooks-shaped request wrapper and embedded prefetch |
| `data/sandbox/prefetch-resources.ndjson.gz` | one prefetch key per case | 184 | FHIR R4-shaped teaching resources |
| `data/sandbox/responses.ndjson.gz` | one sandbox case | 31 | response, transport, notice, and observed outcome |
| `outputs/trace-events.csv.gz` | one trace event | 61 | request and terminal branch ledger |
| `outputs/test-matrix.csv` | one declared case | 31 | expected behavior and visibility contract |
| `outputs/test-results.csv` | one executed case | 31 | expected-versus-observed result |
| `outputs/visibility-audit.csv` | one executed case | 31 | request, response, terminal trace, notice, and silence comparison |
| `outputs/accessibility-checks.csv` | one executed case | 31 | card structure checks and the blocked defect |
| `outputs/invariant-checks.csv` | one release invariant | 20 | build acceptance checks |
| `build-report.json` | one release | 1 | source identities, output identities, counts, runtime, and authority |

## Test coverage

The 31 cases cover normal positive and negative behavior, the threshold boundary, repeat exposure, missing, stale, inconsistent, and delayed input, duplicate requests, terminology and unit mismatch, hook and model version mismatch, suppressions, unavailable service, timeout, silent failure, and an accessibility defect.

The silent-failure detector does not trust a single log. It compares the request ledger with the response ledger, terminal trace, and human notice evidence. A received request with none of the other three is a seeded silent failure.

## Runtime boundary

`build_sandbox.py` uses the Python standard library. It opens local files only. It has no listener, network client, FHIR server address, authentication, or external dependency. The JSON uses FHIR R4 and CDS Hooks-shaped teaching structures but makes no conformance claim.

## Claim boundary

The sandbox does not establish clinical correctness, interoperability, latency performance, safety, utility, accessibility in practice, or production readiness. A passing test means only that the local synthetic fixture reproduced its declared result.
