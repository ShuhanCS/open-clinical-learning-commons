# Reference environment note

- Operating system tested: Windows 11
- Architecture: 64-bit
- Shell: PowerShell
- Python: 3.12.10
- Builder and validator runtime dependencies: Python standard library only
- Later-course analysis pins: exact versions in `requirements.txt`
- Source encoding: UTF-8
- Generated line endings: LF

Reference commands from the repository root:

```text
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/build_modeling_workspace.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/validate_modeling_workspace.py --self-check
```

The dependency file establishes the common FND-2 analysis environment before Module 02. Module 01's deterministic data build does not import those packages, which keeps source verification and split reproduction available when a scientific package installation is temporarily unavailable.
