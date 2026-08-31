# APP-4 final checkpoint build plan

## Outcome

Release the official-end-date APP-4 Clinical Decision Support package. The checkpoint must freeze the exact accepted Module 07 candidate, record its 35-point component once, adjudicate curriculum-package completeness separately from CDS readiness, and close APP-4 for curriculum construction without granting clinical or production authority.

## Fixed inputs

- Module 07: `oclc-app4-07@0.1.0`, Commons `0.85.0`, 1,347 files, 1,320 immutable rows, manifest SHA-256 `8fc03ea9a7ebce8e0e4bf350b2699c5f74ec4a9c5ae493f25f26c94be8c2cea9`.
- Module 07 release: 4,590 bytes, SHA-256 `8e2eada4dadc30d92976963bc8bd01639ea851b88e115464801ee9900ed6e7cd`.
- Checkpoint 01 release SHA-256: `8f637bef551ebe5cb91e93b3b91fef51f25736d07168b904851405c703b62c03`.
- Checkpoint 02 release SHA-256: `05e65b59f0d4c4b33dc341256141e39c02cfffc32e22aca546dbb85384cb1221`.
- Final component: 35 points, giving `40 + 25 + 35 = 100` with no duplication.
- Package disposition: `accept with conditions`.
- Separate CDS recommendation: `revise before seeking local silent-mode approval`.
- No clinical threshold is accepted. `panel-t003` and `0.03000000` remain mechanics fixtures only.
- The blocked accessibility defect, detected silent failure, 22 hazards, 20 measures, 12 human escalation routes, and failed R03/R04/R08 rules remain visible.

## Build sequence

1. Rebuild and completely validate the Module 07 reference candidate.
2. Copy all 1,347 candidate files byte for byte and create a sorted final manifest covering every copied file.
3. Add ten final-review records plus the checkpoint version, three accepted release records, and generated final manifest.
4. Preserve the 35-point score, 26 gates, 16 conditions, 14 defense answers, 14 reviewer roles, clinician boundary, AI disclosure, and all authority prohibitions.
5. Reject changed candidate bytes, release identities, score, gates, recommendation, threshold, model, failures, accessibility, reviewers, conditions, defense, tag state, and authority.
6. Keep large-package self-checks sequential and delete each temporary copy before building the next.
7. Publish a 17-section durable specification and advance Commons from `0.85.0` to `0.86.0`.
8. Run focused and complete curriculum regressions, commit, push, and remote-verify before starting APP-5.

## Boundaries

The checkpoint closes APP-4 for curriculum construction only. It does not authorize real-patient scoring, clinical threshold acceptance, clinical alerting or action, silent-mode evaluation, implementation, production connection, or deployment. The proposed release tag remains uncreated until named human review, independent reproduction, an adequate live or approved equivalent defense, and exact-commit authorization are complete.
