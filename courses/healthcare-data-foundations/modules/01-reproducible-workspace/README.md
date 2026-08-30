# FND-1 Module 01: Setting up a reproducible workspace

Module 01 asks one technical question: can another learner clone, run, inspect, and version the workspace without borrowing the original analyst's machine or hidden files?

- Course: FND-1 Healthcare Data Foundations
- Week: 1
- Learner work: 15.5 hours
- Module version: 0.1.0
- Commons release: 0.28.0
- Status: runnable release candidate; human review pending
- Graded role: 15-percent setup component frozen into the cumulative Week 3 checkpoint
- Decision owner: course instructor acting as repository maintainer
- Decision: accept, accept with conditions, revise, or refer the workspace before healthcare source data enter it

This module uses a three-row synthetic smoke-test table. It contains no patient data and supports no clinical claim. The continuing Synthea healthcare database begins in Module 02.

## What learners prove

Learners create a local environment, run Python and SQLite checks, execute a supplied pandas notebook, run and interpret a supplied base-R script, preserve a readable Git history, apply semantic versioning, reproduce the work from a clean target, and document any AI assistance.

The fixed reference result is:

```text
rows=3
event_count_total=15
event_count_minimum=3
event_count_maximum=7
```

These are software-check values only.

## Package map

| Path | Purpose |
|---|---|
| `build_workspace.py` | Copies the learner template to a new path and refuses overwrite. |
| `validate_workspace.py` | Checks a starter or completed submission with Python standard-library code. |
| `template/` | Portable learner workspace. |
| `data-spec.md` | Synthetic table contract and immutable checks. |
| `source-record.yml` | Provenance, rights, and fingerprint record. |
| `assessment.md` | Exact submission, rubric, gates, and checkpoint role. |
| `instructor-notes.md` | Timing, answer key, common failures, and review guidance. |
| `release.json` | Machine-readable module release record. |

Durable module specification:

`docs/curriculum/courses/FND-1/modules/01-reproducible-workspace-spec.md`

## Build a clean learner copy

From the repository root:

```text
python courses/healthcare-data-foundations/modules/01-reproducible-workspace/build_workspace.py learner-workspace
```

The target must not exist. The builder will not merge with or overwrite another folder.

## Validate the starter

```text
python courses/healthcare-data-foundations/modules/01-reproducible-workspace/validate_workspace.py learner-workspace --mode starter
```

The starter check validates 15 file, environment, notebook, source, and smoke-test requirements.

## Validate a completed submission

```text
python courses/healthcare-data-foundations/modules/01-reproducible-workspace/validate_workspace.py learner-workspace --mode submission --require-r
```

The submission check validates 26 requirements, including completed records, stored outputs, a clean `main` branch, commit history, a merge commit, and the annotated `fnd1-setup-v0.1.0` tag.

If `Rscript` is not on `PATH`, an instructor can supply the exact executable:

```text
python courses/healthcare-data-foundations/modules/01-reproducible-workspace/validate_workspace.py learner-workspace --mode submission --require-r --rscript PATH_TO_RSCRIPT
```

## Maintainer checks

```text
python courses/healthcare-data-foundations/modules/01-reproducible-workspace/build_workspace.py --self-check
python courses/healthcare-data-foundations/modules/01-reproducible-workspace/validate_workspace.py --self-check
```

The validator self-check creates one complete fixture, proves that it passes, removes a required record from a copy, and proves that the incomplete copy fails.

## Required interpretation

A passing smoke test means the submitted environment can reproduce this small reference task. It does not prove that the learner can build the Module 02 database, define a cohort, clean healthcare data, fit a model, or make a clinical decision.

## Authoritative setup references

- Python virtual environments: https://docs.python.org/3/library/venv.html
- Python SQLite interface: https://docs.python.org/3/library/sqlite3.html
- Git concepts and commands: https://git-scm.com/book/en/v2
- JupyterLab installation and use: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
- pandas installation: https://pandas.pydata.org/docs/getting_started/install.html
- R command-line front end: https://stat.ethz.ch/R-manual/R-devel/library/utils/html/Rscript.html
- Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html

Package-version records:

- https://pypi.org/project/jupyterlab/4.6.3/
- https://pypi.org/project/nbclient/0.10.2/
- https://pypi.org/project/pandas/3.0.5/
