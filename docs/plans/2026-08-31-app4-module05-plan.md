# APP-4 Module 05 build plan

## Goal

Build the runnable APP-4 Module 05 package for a local, nonnetworked FHIR R4 and CDS Hooks-shaped teaching sandbox. The package must freeze the complete Module 04 reference release, test normal and failure routes, distinguish visible from silent failure, and hand a protected result to Module 06.

## Fixed contract

- Module ID: `oclc-app4-05`.
- Title: `Sandbox prototype and failure modes`.
- Hours: `16.0`.
- Course points: `0`; this is a required Checkpoint 02 gate.
- Module version: `0.1.0`.
- Commons release target: `0.82.0`.
- Design fixture: `panel-t003`.
- Threshold fixture: `0.03000000`, unaccepted.
- Runtime: Python standard library only, local file execution, no listener and no network client.
- Data: synthetic teaching records only.
- Authority: no real-patient scoring, clinical alerting, clinical action, threshold acceptance, silent-mode evaluation, implementation, production connection, or deployment.

## Work

1. Freeze and verify every immutable Module 04 reference artifact, including its full nested Week 3 chain.
2. Build deterministic FHIR R4 and CDS Hooks-shaped requests, responses, trace events, and a declared test matrix.
3. Cover normal positive, normal negative, boundary, repeat, missing, stale, inconsistent, delayed, duplicate, unavailable-service, terminology, version, suppression, accessibility, visible-failure, and silent-failure routes.
4. Build separate learner and reference workspaces with editable assessment records outside the immutable manifest.
5. Add zero-point progression gates, instructor material, answer key, protected Module 06 handoff, and deliberate validator failure routes.
6. Write the 21-section module specification and integrate the release into course, ledger, root, and curriculum checks.
7. Run focused self-checks and the complete curriculum regression.
8. Bump Commons version `0.81.0` to `0.82.0`, commit only this unit, push the branch, and verify the remote SHA.

## Done when

- The deterministic sandbox build reproduces byte for byte and refuses overwrite.
- Every declared test route has an expected result, trace, visibility state, and human notice state.
- The validator detects silent failure by comparing request, response, trace, and notice evidence rather than trusting a single log.
- The reference passes every zero-point gate while the learner starter remains incomplete.
- Module 06 receives an immutable prototype and failure release without expanded authority.
- The complete curriculum checker passes and the clean remote branch matches the local commit.
