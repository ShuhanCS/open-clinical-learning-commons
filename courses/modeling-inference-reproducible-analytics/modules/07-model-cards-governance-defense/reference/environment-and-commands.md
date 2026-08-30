# Reference environment and ordered commands

- Environment: Windows 11 and PowerShell
- Python: 3.12.10
- Candidate dependencies: Python standard library only; nested module evidence retains its own pinned package record
- Source commit: `ff60b209cb083dc64382617f749ec09b16a7d5bc`

## Ordered commands

1. `python assemble_candidate.py assembled/reference-1 --reference`
2. `python assembled/reference-1/validate_candidate.py assembled/reference-1`
3. `python assemble_candidate.py assembled/reference-2 --reference`
4. Compare both `release-manifest.csv` files byte for byte.
5. `python assemble_candidate.py assembled/starter --checkpoint2 <accepted-checkpoint2-directory>`
6. `python assembled/starter/validate_candidate.py assembled/starter --starter`
7. Complete the 24 learner records and validate without `--starter`.
8. Commit the exact candidate and submit it to the final checkpoint.

## Hidden-dependency check

The candidate validator uses only the standard library. All evidence paths are candidate-relative. No cache, virtual environment, personal path, credential, secret, unregistered data, or network call is required.
