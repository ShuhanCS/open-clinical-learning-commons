# Reproducibility check

- Source acquisition: `pass`.
- Source archive bytes: `4,506,627`.
- Source archive SHA-256: `74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4`.
- Source-manifest SHA-256: `f1d530f18fd55aacba6d99fbfef847c214c60aba66759e8746bb9713e4d872b0`.
- Checkpoint handoff rows: `240`.
- Checkpoint handoff SHA-256: `db70b4e20a17fbddd2b49f7647dd9ce5bcd064e01af5e7a7e23df9122889914e`.
- Independent geometry builds: `byte-identical outputs`.
- Independent SVG builds: `byte-identical outputs`.
- SQL checks: `32 of 32 pass`.
- Geometry rows: `1,620`.
- Matched measure rows: `1,597`.
- Unavailable rows: `23`.
- Complete exact-table rows: `1,620`.
- Copied-validator execution: `required by module validator`.
- Protected failure routes: `required by module validator self-check`.
- Existing-target overwrite: `rejected by source, handoff, analysis, and workspace builders`.

The independent build reads the committed source archive, frozen checkpoint, reference SQL, and immutable module controls. It does not read a learner answer to construct the reference outputs. The deterministic SVG uses a fixed Matplotlib SVG hash salt, fixed source order, fixed class order, fixed display projection, and fixed 100-meter topology-preserving simplification.
