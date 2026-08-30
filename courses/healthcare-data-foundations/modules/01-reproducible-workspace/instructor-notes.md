# Module 01 instructor notes and answer key

## Teaching purpose

The week ends when each learner has a workspace another person can reproduce. Do not turn setup into a survey of every development tool. One local virtual environment, one Git repository, one deterministic table, one SQLite query, one notebook, and one supplied R script are enough to expose the habits the rest of FND-1 needs.

The smoke data are not healthcare data. Any clinical interpretation is incorrect.

## 15.5-hour teaching plan

| Activity | Hours |
|---|---:|
| Orientation, workspace contract, and data boundary | 0.75 |
| Git repository, commits, and readable state | 2.00 |
| Python virtual environment and dependency installation | 2.25 |
| Python and SQLite smoke test | 2.00 |
| pandas notebook execution and stored outputs | 1.50 |
| Supplied R script: read, run, and interpret | 1.00 |
| Branch, non-fast-forward merge, and semantic version | 2.00 |
| Verified AI-assisted or manual troubleshooting record | 1.00 |
| Independent clean-target reproduction | 2.00 |
| Submission check, reflection, and release | 1.00 |
| Total | 15.50 |

## Reference answers

### Data facts

- Header: `record_id,source_label,event_count`.
- Rows: 3.
- Unique `record_id` values: 3.
- Event-count values: 3, 5, and 7.
- Sum: 15.
- Minimum: 3.
- Maximum: 7.
- Data SHA-256: `330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab`.

These values have no clinical interpretation.

### SQL reading

- `record_id TEXT PRIMARY KEY` requires a non-null unique identifier in SQLite's table contract.
- `source_label TEXT NOT NULL` refuses a missing label.
- `event_count INTEGER NOT NULL CHECK (event_count >= 0)` refuses null and negative values.
- The Python script inserts parameterized values rather than building SQL strings from row contents.
- The database is `:memory:` and disappears when the connection closes.

### Environment

- `.venv` stays local because it is large, platform specific, and reproducible from the dependency record.
- The dependency file is committed because it is part of the environment contract.
- The learner records actual versions because a file that requests a package version does not prove that the requested version ran.
- The notebook imports pandas 3.0.5 and stores evidence that every code cell ran.

### Git and versioning

- A commit records a project state and message.
- A branch names a movable line of commits.
- A merge integrates histories; this exercise requires a visible merge commit.
- An annotated tag names the accepted setup release and carries tag metadata.
- Version 0.1.0 means the first usable setup contract before a stable 1.0.0 course release.
- A typo correction can be a patch; a compatible new check can be a minor change; changing a required path or expected result can be a major change.

### R role

Learners are not graded on writing R from scratch. They must identify the input path, read the four `stopifnot` checks, run the supplied script from the workspace root, and explain the pass marker. A learner who edits the script to hide a failing check has not met the requirement.

## Instructor demonstration

1. Build a new learner copy.
2. Run starter validation.
3. show that a second build to the same path is refused.
4. Create `.venv` and install the three exact requirements.
5. Run the Python script.
6. Execute the notebook in place and inspect stored output.
7. Run the supplied R script.
8. Show `git status --short --branch`, a branch commit, the merge graph, and an annotated tag.
9. Clone into a new path and reproduce without copying `.venv`.
10. Run submission validation.

## Common failures and interventions

| Failure | Likely cause | Intervention | Evidence of resolution |
|---|---|---|---|
| `python` is not found | Python is missing or not on `PATH`. | Use the institution-supported Python install and restart the terminal. | `python --version` and environment note agree. |
| Package imports from a global environment | Learner used the wrong executable. | Run the `.venv` Python by its explicit path. | `sys.executable` points inside `.venv`. |
| Jupyter uses a different kernel | Browser session opened before the environment or selected another kernel. | Stop Jupyter, launch it from `.venv`, and select the local Python kernel. | Notebook version cell reports pandas 3.0.5. |
| Notebook has no outputs | Learner saved before execution or cleared output. | Run all cells in order and save. | Every code cell has an execution count and pass output. |
| SQLite total is not 15 | Source, SQL, or script was edited. | Restore the released files and inspect the diff before rerunning. | Fingerprint and expected result pass. |
| R cannot find the CSV | Script ran from another working directory. | Change to the workspace root and rerun the supplied command. | R output file contains the exact marker. |
| Merge does not appear | Git fast-forwarded or the learner copied files across branches. | Repeat the practice branch and merge it with `--no-ff`. | `git rev-list --merges HEAD` finds a merge. |
| Tag is lightweight | Learner omitted `-a`. | Recreate under instructor direction with an annotation. | `git cat-file -t` returns `tag`. |
| Working tree is dirty | Output or record changes were not committed. | Inspect, stage only intended files, commit, and rerun. | `git status --short` is empty. |
| Reproduction reused `.venv` | Learner copied the original directory. | Clone to a new target and build a fresh environment. | Reproduction record lists fresh install commands. |
| AI record says only "used ChatGPT" | Purpose, input, verification, and decision are missing. | Complete one row per material use and verify one exact claim. | Record connects advice to a command or primary source and observed result. |

## Accessibility and inclusion

- Demonstrate terminal commands as copyable text, not screenshots alone.
- Read terminal errors aloud and paste them into the session record after removing personal paths and secrets.
- Permit an accessible Git client when it produces the required history and tag evidence.
- Offer the same task with institution-managed Python when local install permissions are unavailable.
- Do not grade typing speed, shell memorization, prior Git vocabulary, or ability to diagnose inaccessible institutional tooling without support.

## Review sequence

1. Run the canonical validator.
2. Inspect the tagged commit and Git graph.
3. Confirm records describe observed work rather than reference values copied without evidence.
4. Check that no token, password, private URL, patient data, or personal absolute path appears.
5. Ask the learner to explain the CSV-to-SQL flow and the narrow meaning of the pass result.
6. Ask which AI suggestion was tested, how, and what changed.
7. Record score, gate results, disposition, conditions, owner, and due date.

## Release status

The package is a runnable release candidate. Technical self-checks pass. Faculty, data engineering, Python/notebook teachability, accessibility, responsible-AI, privacy, and independent-instructor reviews remain required before alpha.
