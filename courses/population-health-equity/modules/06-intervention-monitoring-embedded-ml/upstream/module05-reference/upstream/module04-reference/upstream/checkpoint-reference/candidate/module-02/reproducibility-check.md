# Reproducibility check

- Frozen handoff files verified: `29`.
- Nested Module 01 immutable rows verified: `16`.
- Synthetic source rows verified: `7,985`.
- Accepted SQL files executed: `4`.
- Accepted output tables regenerated: `10`.
- SQL query checks passed: `30 of 30`.
- Source-reconciliation checks passed: `8 of 8`.
- Adult denominator total: `5,679,768`.
- Synthetic event total: `283,614`.
- Direct rates available: `1,576`.
- Direct rates unavailable: `21`.
- Guided indirect cases: `80`.
- Independent Python reproduction: `pass`.
- Two deterministic builds: `byte-identical`.

The reproduction uses Python's standard library, SQLite, the four accepted SQL files, the frozen Module 01 handoff, and the pinned synthetic release. It does not download or substitute a newer source.
