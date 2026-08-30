# Reproducibility check

- Source database bytes: `141234176`
- Source database SHA-256: `1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a`
- SQL files: `4 read-only WITH queries`
- Python dependencies: `standard library only`
- Extension seed: `app1-six-site-v1`
- Builder target policy: `new directory only`
- Reference result: `two complete builds match byte for byte`
- Copied-validator result: `learner command enforces the eight-row manifest and ignores generated Python cache files`

Build from the accepted FND-1 database:

```powershell
python build_longitudinal.py --database <accepted-synthea-sqlite> --target <new-output-directory>
```

Validate the released package and reproduce it from the database:

```powershell
python validate_longitudinal.py . --database <accepted-synthea-sqlite>
```

The database is opened read-only. A target that already exists is rejected. A changed database fingerprint, SQL result, extension seed, site probability, source exposure, source outcome, or output byte fails validation.
