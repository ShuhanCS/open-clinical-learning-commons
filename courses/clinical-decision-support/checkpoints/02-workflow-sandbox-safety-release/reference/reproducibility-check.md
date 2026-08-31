# Reproducibility check

- Checkpoint: `oclc-app4-cp02@0.1.0`.
- Commons release: `0.84.0`.
- Candidate files: `1,030`.
- Module 04: `302 files; 285 manifest rows; 60,302 bytes; SHA-256 41692b01fa2c339068fcdbf5fbc6f3e301a79ba4535d9ecb94d602cb2e4b3bf9`.
- Module 05: `341 files; 324 manifest rows; 75,019 bytes; SHA-256 6bc3e7c0040b8ae93d273d1464459ae8d500913e0e8a423ca1e5b120256c8baf`.
- Module 06: `387 files; 369 manifest rows; 88,971 bytes; SHA-256 e6553079256fdd2a37ab042a87c2ec69812cad7074abefa7d7907e6ee7b56f7d`.
- External Python dependencies for checkpoint assembly and validation: `none`.

## Commands

From the checkpoint directory:

```powershell
python build_checkpoint.py --self-check
python validate_checkpoint.py --self-check
python build_checkpoint.py --target <new-reference-path> --reference
python validate_checkpoint.py --workspace <new-reference-path> --complete
python build_checkpoint.py --target <new-learner-path>
python validate_checkpoint.py --workspace <new-learner-path>
```

## Result

Two clean reference assemblies produce byte-identical candidate files and the same candidate manifest. The learner and reference packages contain the same immutable candidate. The assembler refuses an existing destination. Validation runs from the repository and from a copied assembled package. Deliberate mutations are rejected.

## Independent review boundary

The checkpoint reproduces the frozen release identity and synthesis. It does not rerun, tune, or improve the accepted analyses. A clean independent human reproduction of the source modules and a live learner defense remain required before alpha.
