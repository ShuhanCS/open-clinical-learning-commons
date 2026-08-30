# Cumulative reproducibility check

- Date: 2026-08-30.
- Platform and architecture: Windows x86_64 reference runner.
- Python: 3.12.10.
- SQLite: 3.49.1.
- pandas: 3.0.5.
- JupyterLab: 4.6.3.
- nbclient: 0.10.2.
- R: 4.6.1.
- Module 01 smoke tests: pass with 3 rows and total 15.
- Source archive bytes and SHA-256: pass.
- Module 02 database integrity and relationships: pass.
- Five first extracts reproduced: pass.
- Four cohort SQL files rerun: pass.
- Five Module 03 outputs reproduced byte for byte: pass.
- Checkpoint release manifest: pass.
- Checkpoint validator: pass.
- Clean output targets: pass.
- Existing-target protection: pass.

## Commands

The reference uses the released Module 01 builder and validator, Module 02 database builder and query runner, Module 03 cohort builder and validator, then the checkpoint assembler and validator. Every build writes to a new target.

## Material differences

No material difference was observed on Windows. Named macOS and Linux reproduction remains pending before alpha promotion.
