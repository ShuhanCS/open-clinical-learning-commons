# Reproducibility check

- Module: `oclc-app4-07@0.1.0`.
- Commons release: `0.85.0`.
- Checkpoint 01 release SHA-256: `8f637bef551ebe5cb91e93b3b91fef51f25736d07168b904851405c703b62c03`.
- Checkpoint 02 release SHA-256: `05e65b59f0d4c4b33dc341256141e39c02cfffc32e22aca546dbb85384cb1221`.
- Immutable manifest rows: `1,320`.
- Candidate files: `1,347`.
- Release-manifest bytes: `319268`.
- Release-manifest SHA-256: `8fc03ea9a7ebce8e0e4bf350b2699c5f74ec4a9c5ae493f25f26c94be8c2cea9`.
- External Python dependencies: `none`.

## Commands

From the Module 07 directory:

```powershell
python assemble_candidate.py --self-check
python validate_candidate.py --self-check
python assemble_candidate.py --target <new-reference-path> --reference
python validate_candidate.py --candidate <new-reference-path> --complete
```

## Required results

The assembler builds and validates both accepted checkpoint references, verifies their manifests and release records, copies every accepted byte, creates a sorted Module 07 manifest, refuses an existing destination, and produces the same immutable result for reference and learner modes. Validation must also pass from a copied candidate and reject deliberate evidence, score, gate, recommendation, authority, clinician-boundary, accessibility, and defense failures.

Independent human clean reproduction and a live or approved equivalent defense remain required before alpha.
