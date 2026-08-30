# Reference reproduction record

- Operating system: Windows 11
- Python: 3.12.10
- Checkpoint assembler dependencies: Python standard library only
- Module analytic environments: preserved in each module requirements and environment record
- Assembly mode: reference
- Module roots: repository FND-2 Module 01 through 03 releases
- Immutable module artifacts: 72
- Immutable checkpoint controls: 6
- Manifest rows: 78
- Manifest bytes: 11241
- Manifest SHA-256: `b3760f43e5852ba90150000a4c807bc3aadfedcc688b40c4f16017dc253ca836`
- Assembled files: 89
- Existing-target refusal: pass
- Two-build manifest comparison: pass
- Complete reference validation: 500 checks
- Learner starter validation: 465 checks
- Difference: none observed

The assembler copies accepted evidence byte for byte and creates only the release manifest. It does not rerun model fitting. Module-level builder and validator results remain preserved inside their module namespaces.

The accountable technical reproducer for this reference is OpenAI Codex; named independent human reproduction remains pending before alpha.
