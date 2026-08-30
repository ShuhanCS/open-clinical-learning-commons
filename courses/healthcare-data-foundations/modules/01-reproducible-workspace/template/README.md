# FND-1 Module 01 learner workspace

This repository is the graded setup component for Healthcare Data Foundations. Your job is to prove that another analyst can create the environment, run the same Python, pandas, SQLite, and supplied R checks, inspect what changed, and identify the released version.

The three-row CSV is synthetic smoke-test data. It contains no patient records and supports no clinical claim.

## Required software

- Git 2.40 or later.
- Python 3.12 through 3.14.
- R 4.4 or later for the supplied read-run-interpret exercise.
- A terminal and text editor.

The reference release was tested with Python 3.12.10, SQLite 3.49.1, Git 2.54.0, R 4.6.1, pandas 3.0.5, JupyterLab 4.6.3, and nbclient 0.10.2. Record your actual versions in `environment-note.md`; do not claim the reference versions unless those are the versions you ran.

## 1. Create the repository

From the parent directory of this workspace:

```text
git init -b main learner-workspace
cd learner-workspace
git add .
git commit -m "chore: start FND-1 workspace"
```

If your copy is already a Git repository, do not initialize it again. Confirm the current branch and working-tree state with:

```text
git status --short --branch
```

## 2. Create the Python environment

Create a local virtual environment:

```text
python -m venv .venv
```

Windows PowerShell:

```text
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

macOS or Linux:

```text
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

The `.venv` directory is ignored by Git. Do not submit the environment folder.

The supplied `.gitattributes` keeps source, code, notebook, and output text files on LF line endings so the registered source checksum stays the same across operating systems.

## 3. Run the smoke tests

Windows PowerShell:

```text
.venv\Scripts\python.exe src\smoke_test.py
.venv\Scripts\jupyter.exe execute notebooks\01-smoke-test.ipynb --inplace
Rscript analysis\r-smoke-test.R
```

macOS or Linux:

```text
.venv/bin/python src/smoke_test.py
.venv/bin/jupyter execute notebooks/01-smoke-test.ipynb --inplace
Rscript analysis/r-smoke-test.R
```

Expected terminal markers:

```text
WORKSPACE_SMOKE_TEST_PASS rows=3 total=15
WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15
```

Open the notebook and confirm that every code cell ran, the pandas check passed, and the stored output includes `WORKSPACE_SMOKE_TEST_PASS`.

## 4. Practice a branch and merge

Create a branch for your environment records:

```text
git switch -c module-01-setup
```

Complete `environment-note.md`, `version-policy.md`, `reproducibility-check.md`, and `ai-use.md`. Commit the work on the branch, return to `main`, and merge with a merge commit:

```text
git add environment-note.md version-policy.md reproducibility-check.md ai-use.md notebooks/ outputs/
git commit -m "docs: record reproducible environment"
git switch main
git merge --no-ff module-01-setup -m "merge: complete Module 01 setup"
```

Use your Git client if its accessible interface is easier. The submitted history must still show the branch work and merge commit.

## 5. Run from a clean checkout

Ask a classmate or use a new local directory. Clone the repository, create a new `.venv`, install `requirements.txt`, rerun the smoke tests, and record the result in `reproducibility-check.md`. The reproducer must not reuse your original `.venv`.

Commit the completed reproduction record. Confirm that no uncommitted file remains:

```text
git status --short
```

The command should print nothing.

## 6. Tag the setup component

The workspace version is `0.1.0`. Create the required annotated tag:

```text
git tag -a fnd1-setup-v0.1.0 -m "FND-1 Module 01 setup component"
git show fnd1-setup-v0.1.0 --stat
```

Do not tag a dirty or failing workspace.

## Submission

Submit the repository URL and the exact commit identified by `fnd1-setup-v0.1.0`. The repository must contain:

- executed `notebooks/01-smoke-test.ipynb`;
- `outputs/python-sql-smoke.json`;
- `outputs/r-smoke-test.txt`;
- completed `environment-note.md`;
- completed `version-policy.md`;
- completed `reproducibility-check.md`;
- completed `ai-use.md`;
- the supplied `.gitattributes` and `.gitignore`;
- a clean Git working tree;
- at least one non-fast-forward merge commit; and
- the annotated `fnd1-setup-v0.1.0` tag.

Do not include patient data, passwords, access tokens, local environment folders, or identifying screenshots.
