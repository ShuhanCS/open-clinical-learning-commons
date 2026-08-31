# Reproducibility check

- Module: `oclc-app5-05` version `0.1.0`.
- Commons release: `0.92.0`.
- Runtime: Python standard library and SQLite.
- Upstream payload files: `287`.
- Upstream handoff manifest SHA-256: `0670760f650e0d13cfd4c5dc85ab26fdce5779cc86d35b3d3c27d6a3cc7738dd`.
- Fictional planning rows: `1,597`.
- Synthetic source manifest SHA-256: `a9a9cd10e67164cd8c47df667f2e559f17f8baa0e2308740ce4c9d9e675c0319`.
- Candidate rows: `1,597`.
- Assignment rows: `6,388`.
- County consequence rows: `56`.
- Group consequence rows: `76`.
- Rule overlap rows: `6`.
- Sensitivity rows: `20`.
- SQL checks: `40 of 40 pass`.
- Score: `15 of 15`.
- Gates: `26 of 26 pass`.
- Build report SHA-256: `d2b2621c6b97365fb9751902d7c1eac091567d6d8f2e5b5188fc4f4bafaa700a`.

Two upstream freezes, two fictional-source generations, two output builds, and two reference workspaces must match byte for byte. The validator must pass from the copied workspace and reject copied reference answers, complete-mode learner workspaces, changed inputs or outputs, broken rule and resource contracts, suppressed values changed to zero, missing recourse, changed scores or gates, automatic-action language, real-action authority, and deployment language.
