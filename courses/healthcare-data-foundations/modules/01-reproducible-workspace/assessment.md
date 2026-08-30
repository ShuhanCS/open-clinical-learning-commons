# Module 01 assessment: Reproducible workspace setup component

## Course role

This assessment is the 15-percent setup component of FND-1. The accepted tagged submission is frozen and included in the cumulative Week 3 checkpoint with the separate 25-percent SQL cohort component.

## Decision

The instructor decides whether the workspace is ready to receive the Module 02 synthetic healthcare sources and graded SQL/Python work.

Allowed dispositions:

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer` for privacy, security, access, or academic-integrity review.

## Exact submission

Submit the repository URL and the full commit hash referenced by the annotated `fnd1-setup-v0.1.0` tag. The tagged commit must contain:

1. `README.md`;
2. the supplied `.gitattributes` and `.gitignore`;
3. `VERSION` containing `0.1.0`;
4. exact `requirements.txt` pins;
5. the supplied CSV and SQL files unchanged;
6. `src/smoke_test.py` unchanged;
7. an executed `notebooks/01-smoke-test.ipynb` with stored pass outputs;
8. the supplied `analysis/r-smoke-test.R` unchanged;
9. `outputs/python-sql-smoke.json`;
10. `outputs/r-smoke-test.txt`;
11. completed `environment-note.md`;
12. completed `version-policy.md`;
13. completed `reproducibility-check.md`; and
14. completed `ai-use.md`.

The Git repository must be on `main`, have a clean working tree, preserve at least three commits, contain at least one merge commit, and identify `HEAD` with the annotated setup tag.

## Required demonstrations

The learner must show that they can:

- state which Python executable ran the work;
- explain why `.venv` is not committed;
- trace the CSV through Python into an in-memory SQLite table;
- identify the SQL primary key, non-null rules, and nonnegative check;
- explain what the notebook adds to the script-based check;
- run and interpret the supplied R result without claiming to have authored the R code;
- distinguish a commit, branch, merge, and tag;
- explain why `0.1.0` is an initial usable release;
- reproduce the tagged commit from a clean directory; and
- verify one material AI suggestion or document that no AI tool was used.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Environment identity and dependency control | 20 | A local `.venv` is excluded; exact commands and actual versions are recorded; requirements match the release; no credential or personal absolute path appears. |
| Python, pandas, SQLite, and supplied R execution | 25 | Script, notebook, SQL, and R checks pass; stored outputs show 3 rows and total 15; learner explains the result and its narrow meaning. |
| Git history and semantic version | 25 | Clean `main`; readable commits; non-fast-forward merge; annotated setup tag at `HEAD`; patch/minor/major examples fit this workspace. |
| Independent reproduction | 15 | A clean target and fresh environment reproduce all required outputs; commands, differences, failures, and disposition are recorded. |
| AI disclosure and verification | 10 | Every material use is recorded; one claim is checked with a command or authoritative source; no protected data or credential is shared; learner accepts responsibility. |
| Accessible technical communication | 5 | Files use headings, plain text, meaningful link text, readable tables, and copyable commands; status and next action are explicit. |
| Total | 100 |  |

## Pass conditions

A passing submission requires all of the following:

- at least 80 points;
- Python/SQLite smoke-test gate passed;
- pandas notebook gate passed with stored outputs;
- supplied R read-run-interpret gate passed;
- clean-reproduction gate passed;
- Git and annotated-tag gate passed;
- privacy and credential gate passed;
- AI disclosure gate passed; and
- `accept` or `accept with conditions` disposition.

A score of 80 or more cannot override a failed gate.

## Automatic validation

The instructor runs the canonical validator from the Commons checkout:

```text
python courses/healthcare-data-foundations/modules/01-reproducible-workspace/validate_workspace.py PATH_TO_SUBMISSION --mode submission --require-r
```

Automatic checks support the decision; they do not replace review of the learner's explanations, Git history, AI verification, accessibility, or independent reproduction record.

## Revision rule

A learner may correct setup defects until the course checkpoint closes. The revised submission needs a new commit. If the tagged commit changes, delete and recreate the local setup tag only under instructor direction, push the corrected annotated tag, and record why the tag moved. After Checkpoint 1 is frozen, a corrected setup release uses a new patch version rather than moving the accepted tag.
