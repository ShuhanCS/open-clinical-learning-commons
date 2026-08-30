# Reference environment note

- Learner: instructor technical reference.
- Operating system and version: Windows reference runner.
- Computer architecture: x86_64.
- Shell: PowerShell.
- Python version: 3.12.10.
- Python executable used: environment-managed `python` command.
- pandas version: 3.0.5.
- JupyterLab version: 4.6.3.
- nbclient version: 0.10.2.
- SQLite version reported by Python: 3.49.1.
- R version: 4.6.1.
- Git version: 2.54.0.windows.1.
- Workspace tag: `fnd1-setup-v0.1.0`.
- Checkpoint tag: `fnd1-checkpoint1-v0.1.0` after human approval.

## Installation record

The clean reference environment created an isolated Python environment and installed the three exact requirement pins. SQL used Python's SQLite library. The supplied R smoke test ran through the installed R command.

## One resolved setup failure

The clean run verified that output targets must not already exist. Reusing a target was rejected, a new target was selected, and the complete build then passed.

## Material differences from the reference environment

No material difference was observed during the Windows technical reproduction. Named macOS and Linux runs remain pending.
