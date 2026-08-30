# FND-1 Module 01: Setting up a reproducible workspace

## 1. Module identity and place in the course

- Course: FND-1 Healthcare Data Foundations.
- Course position: first course in the 30-credit curriculum and first technical foundation.
- Module: 01 of 07.
- Instructional week: 1.
- Learner workload: 15.5 hours.
- Credits carried by course: 3.
- Prerequisites: none.
- Module version: 0.1.0.
- Commons release: 0.28.0.
- Status: runnable release candidate; required human reviews pending.
- Graded role: the 15-percent setup component of the cumulative Week 3 checkpoint.
- Package: `courses/healthcare-data-foundations/modules/01-reproducible-workspace/`.
- Learner workspace version: 0.1.0.
- Required learner tag: `fnd1-setup-v0.1.0`.
- Primary tools: Git, Python, Python `venv`, JupyterLab, pandas, SQLite through Python, and a supplied base-R script.
- Primary operating model: local repository and local environment with no cloud account required.

Module 01 establishes the technical floor for every later FND-1 task. It does not ask whether the learner can analyze healthcare data. It asks whether a reviewer can identify the exact project state, recreate the environment, run a small fixed task, and see the same result without relying on hidden files or the original learner's computer.

The module has one release question:

> Is this workspace ready to receive the synthetic healthcare source system and graded SQL/Python work in Module 02?

The answer must be supported by a tagged Git state, exact dependency record, stored execution evidence, independent reproduction record, and AI-use record.

### Relationship to the course checkpoints

The accepted Module 01 repository is frozen as the setup component of Checkpoint 1. Its 15-percent source weight remains intact. Module 03 later adds the separate 25-percent SQL cohort and analytic-table component. Together, those pieces form the cumulative 40-percent Week 3 checkpoint.

Module 01 is not resubmitted as a new 15-percent assignment at Week 3. The tagged accepted state is carried into the checkpoint package.

### Relationship to the official half-term calendar

This module occupies instructional Week 1 within an official MGH Institute half-term. The course uses seven instructional modules across offerings that span 49 to 52 elapsed days. Final checkpoint dates follow the published last day of the specific half-term, not a generic seventh Sunday.

Official calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

### Required starting condition

A learner may begin without prior Git, Python, SQL, R, or notebook experience. The learner needs a computer or institution-managed environment capable of running the required tools. Lack of local installation permission triggers the supported managed-environment route; it does not lower the evidence standard.

### Required ending condition

At the end of the module, the submitted repository must:

- be on `main`;
- have a clean working tree;
- preserve at least three commits;
- preserve at least one non-fast-forward merge commit;
- identify `HEAD` with an annotated `fnd1-setup-v0.1.0` tag;
- contain the exact source, SQL, script, and dependency files;
- contain an executed notebook with stored outputs;
- contain the Python/SQLite and supplied R output records;
- contain complete environment, version, reproduction, and AI-use records; and
- pass the canonical submission validator.

## 2. Technical decision and named audience

### Decision owner

The decision owner is the course instructor acting as repository maintainer. The instructor may seek technical review, but remains responsible for the recorded disposition.

### Decision

The instructor decides whether the learner workspace is safe and reproducible enough to receive the Module 02 synthetic healthcare data system and graded technical work.

The decision is about the submitted workspace. It is not a judgment of the learner's general technical ability.

### Allowed dispositions

| Disposition | Meaning | Next action |
|---|---|---|
| `accept` | Every release gate passes and no material condition remains. | Freeze the tagged setup component for Checkpoint 1 and begin Module 02. |
| `accept with conditions` | The workspace runs and no blocking gate fails, but a bounded documentation or accessibility condition remains. | Record the condition, owner, and due date; begin Module 02 under that condition. |
| `revise` | A reproducibility, execution, Git, version, documentation, or explanation defect can be corrected within the module. | Correct, rerun, recommit, and resubmit before the checkpoint freeze. |
| `refer` | The submission contains or may expose protected data, credentials, unauthorized access, or a material integrity concern. | Stop reuse and send the issue to the appropriate privacy, security, access, or academic-integrity process. |

### Primary audience

The primary audience is a clinician, researcher, quality professional, analyst, or health-system staff member entering graduate healthcare analytics with uneven prior technical experience.

The module assumes that some learners have never:

- opened a terminal;
- distinguished Python from a notebook interface;
- created an isolated package environment;
- used a relational database;
- read an R script;
- committed a file;
- worked on a branch;
- merged a branch;
- created an annotated tag; or
- reproduced another person's work from a clean target.

### Review audiences

The submitted package must also make sense to:

- an instructor reviewing technical readiness;
- a teaching assistant diagnosing setup failures;
- a second learner reproducing the work;
- a data engineer checking file and environment control;
- an accessibility reviewer checking instructions and records;
- a privacy or security reviewer checking data and credential boundaries;
- an AI-accountability reviewer checking disclosure and verification; and
- the Module 02 instructor inheriting the workspace.

### Decision evidence

The instructor uses five evidence classes:

1. execution evidence from Python, SQLite, pandas, the notebook, and supplied R;
2. repository evidence from commits, branch history, merge, status, and annotated tag;
3. environment evidence from exact versions, commands, and executable identity;
4. reproduction evidence from a fresh target and environment; and
5. accountability evidence from the learner's explanations and AI-use record.

No single screenshot, terminal transcript, or passing automated check is sufficient by itself.

### Oral check

When authorship or understanding is unclear, the instructor asks the learner to explain:

- which Python executable ran;
- how the CSV reached SQLite;
- what the primary key and checks do;
- why the database disappears after the script closes;
- why the virtual environment is not committed;
- how a tag differs from a branch;
- what the pass result proves and does not prove; and
- how one AI or troubleshooting claim was verified.

The oral check is a clarification route, not an unannounced extra assignment.

## 3. Foundation skill and handoff

### Foundation skill

The module establishes reproducible technical state. A reproducible state has a visible project boundary, explicit inputs, explicit tool requirements, fixed code, stored outputs, a recorded version, and enough instructions for another person to rerun it.

The learner practices six connected habits:

1. isolate the software environment;
2. keep source and generated outputs distinct;
3. make project state visible through Git;
4. assign a semantic version to an accepted state;
5. reproduce from a clean target; and
6. record AI assistance without outsourcing responsibility.

### Why this belongs in FND-1

FND-1 owns the trustworthy data layer. A cohort, analytic table, quality profile, descriptive result, or handoff cannot be trusted when the executing code, source version, environment, and project state are unknown. Reproducibility begins before healthcare records enter the workspace.

### Handoff into Module 02

Module 02 inherits:

- the repository structure;
- the local Python environment;
- the exact package-install pattern;
- the Git workflow;
- the semantic-version rule;
- the environment note;
- the reproduction record pattern;
- the AI-use record;
- the distinction between source files and generated outputs; and
- the accepted setup tag.

Module 02 then adds the pinned Synthea source archive, relational schema, SQLite database, data dictionary, FHIR/JSON reading examples, source record, validation output, and first SQL extracts.

### Handoff artifact

The handoff artifact is the full repository state identified by `fnd1-setup-v0.1.0`, not a ZIP file assembled from an uncommitted directory.

### What later modules may assume

After acceptance, later FND-1 modules may assume the learner can:

- navigate the repository;
- run the local Python executable;
- install from a pinned requirements file;
- launch the notebook environment;
- execute a supplied script;
- read a simple SQLite schema and query;
- inspect Git status and differences;
- work on a branch and merge it;
- identify the accepted version; and
- maintain environment, reproduction, and AI-use records.

Later modules may not assume mastery of database modeling, joins, cohort logic, data cleaning, statistical inference, or visualization design.

### Separation from FND-2

This module does not introduce model selection, statistical assumptions, inference, validation, model performance, uncertainty interpretation, or governance of analytic recommendations. Those belong to FND-2 or later domain applications.

### Separation from DA-730

The module requires readable tables, records, and stored output. It does not teach visual encoding, perception, chart selection, uncertainty display, dashboard design, or decision storytelling. Those belong to DA-730.

## 4. Assessable outcomes

By the end of Module 01, the learner can:

1. identify a repository root and explain the purpose of each required top-level file and folder;
2. initialize or inspect a Git repository on `main`;
3. distinguish tracked, untracked, modified, staged, and committed state;
4. write specific commit messages that describe the project change;
5. create a branch, commit on it, and preserve a non-fast-forward merge commit;
6. explain the difference among a commit, branch, merge, and annotated tag;
7. apply patch, minor, and major semantic-version meanings to this learner workspace;
8. create a local Python virtual environment without committing it;
9. install the exact dependency pins from `requirements.txt`;
10. record the actual Python executable, Python version, package versions, SQLite version, R version, Git version, operating system, architecture, and shell;
11. run a Python standard-library program from the repository root;
12. explain how the Python program reads CSV rows and inserts parameterized values into an in-memory SQLite table;
13. read the supplied SQL table constraints and fixed aggregation;
14. run a pandas notebook in the same environment and preserve the stored output;
15. run and interpret a supplied base-R script without claiming from-scratch R authorship;
16. verify that Python, pandas, SQLite, and R return the same three-row and total-15 reference facts;
17. distinguish software-test values from healthcare evidence;
18. reproduce the tagged state from a clean directory and fresh environment;
19. record commands, failures, differences, and disposition without deleting inconvenient evidence;
20. keep patient data, credentials, private URLs, and personal absolute paths out of the public submission;
21. record each material AI use, the data shared, the advice used, the human verification, and the final decision; and
22. explain why a passing setup check is necessary but not sufficient for trustworthy healthcare analysis.

### Outcome-to-evidence map

| Outcome area | Direct evidence | Supporting evidence |
|---|---|---|
| Repository structure | Required file tree and learner explanation | README and validator result |
| Git state | Commit graph, merge commit, clean `main`, annotated tag | Version-policy record |
| Environment | Fresh `.venv`, exact pins, actual version record | Notebook kernel and executable explanation |
| Python and SQLite | Terminal marker and JSON output | Source reading and oral explanation |
| pandas notebook | Executed cells and stored output | Exact package version check |
| Supplied R | R output record and learner interpretation | Script reading discussion |
| Reproduction | Clean-target record and rerun evidence | Reproducer disposition |
| AI accountability | Completed use log and verified claim | Learner accountability statement |
| Data boundary | No protected or identifying data | Source record and privacy gate |

### Minimum explanation standard

The learner must explain cause and evidence, not only list commands. For example, "the command passed" is incomplete unless the learner identifies what was checked, what result was expected, what result was observed, and what remains untested.

## 5. Concept ownership and out-of-scope boundaries

### Module 01 owns

- repository boundaries;
- required project files;
- Git status, add, commit, branch, merge, log, and annotated tag;
- semantic-version meaning for a technical workspace;
- local Python virtual environments;
- exact dependency pins;
- executable and package-version recording;
- the distinction between source, code, notebook, records, and generated output;
- one deterministic Python/SQLite smoke test;
- one supplied pandas notebook;
- one supplied base-R read-run-interpret exercise;
- clean-target reproduction;
- safe setup troubleshooting;
- AI-use disclosure and verification; and
- the limits of a software smoke test.

### Module 01 introduces but does not own deeply

- CSV field types;
- a primary key;
- non-null and check constraints;
- parameterized SQLite insertion;
- an aggregate query;
- notebook execution order; and
- cross-language result comparison.

These appear only as the smallest runnable case needed to test the workspace. Module 02 owns healthcare database structure and retrieval. Module 03 owns cohort SQL and analytic tables.

### Out of scope

Module 01 does not teach or assess:

- EHR, claims, registry, survey, or operational source systems;
- Synthea data contents;
- FHIR server operation;
- database normalization beyond reading one supplied table;
- database administration;
- cloud databases;
- SQL joins, common table expressions, or cohort logic;
- data cleaning or defect correction;
- descriptive statistics;
- inferential statistics;
- machine learning;
- chart selection or visual design;
- Docker or container orchestration;
- continuous integration setup;
- production deployment;
- pull requests or code-review platforms;
- rebasing, history rewriting, or advanced Git recovery;
- R programming from scratch;
- Python packaging;
- private package registries;
- secret-management infrastructure;
- clinical interpretation; or
- patient-level data access.

### Deliberate implementation ceiling

The reference workspace uses `requirements.txt`, `venv`, and an in-memory SQLite database. It does not add Conda, Poetry, uv, Docker, Make, task runners, or a database server. Those tools may be appropriate in another environment, but none is required to prove the Module 01 outcomes.

### Alternative tools

An institution may provide a managed Python or Git interface when local install or terminal access is unavailable. The alternative must still produce:

- an isolated environment;
- the exact package versions;
- the required scripts and stored notebook output;
- inspectable commit and merge history;
- an annotated release marker equivalent to the required Git tag; and
- clean-target reproduction.

Any equivalence decision is recorded before grading. The default Commons validator uses Git and a local Python environment.

## 6. Lesson sequence and time

### Workload table

| Sequence | Learning block | Hours | Required evidence |
|---:|---|---:|---|
| 1 | Orientation, workspace contract, and data boundary | 0.75 | Learner identifies the release question, required files, and no-clinical-claim rule. |
| 2 | Git repository, commits, and readable state | 2.00 | Initial repository, status checks, staged change, and first commit. |
| 3 | Python virtual environment and dependency installation | 2.25 | Local `.venv`, exact dependencies, actual executable and versions. |
| 4 | Python and SQLite smoke test | 2.00 | Passing terminal marker and JSON output. |
| 5 | pandas notebook execution and stored outputs | 1.50 | Three executed code cells and stored pass marker. |
| 6 | Supplied R script: read, run, and interpret | 1.00 | Passing R output and explanation of the supplied checks. |
| 7 | Branch, non-fast-forward merge, and semantic version | 2.00 | Branch commit, visible merge commit, and version examples. |
| 8 | Verified AI-assisted or manual troubleshooting record | 1.00 | One verified claim or a documented no-AI troubleshooting route. |
| 9 | Independent clean-target reproduction | 2.00 | Fresh clone or copy, fresh environment, commands, results, and disposition. |
| 10 | Submission check, reflection, and release | 1.00 | Clean `main`, completed records, annotated tag, validator result, and handoff. |
| Total |  | 15.50 |  |

### Block 1: Orientation

Instructor actions:

- show the package map;
- explain source, code, environment, output, and record roles;
- state that the CSV contains no patient or clinical information;
- show the final submission tree;
- explain the Week 3 checkpoint relationship; and
- demonstrate the accept, condition, revise, and refer dispositions.

Learner actions:

- locate each required file;
- read the data specification and source record;
- paraphrase what the pass result can and cannot mean; and
- record any access or installation constraint early.

### Block 2: Git state

Instructor demonstration:

1. initialize on `main`;
2. inspect status;
3. add only intended files;
4. inspect staged differences;
5. commit with a specific message;
6. inspect the log; and
7. show how ignored `.venv` differs from an untracked required output.

Guided learner task:

- create or inspect the repository;
- commit the initial starter state;
- modify one record;
- compare working-tree and staged changes; and
- restore only their own practice edit if needed.

The instructor does not demonstrate destructive repository-wide resets as a normal recovery method.

### Block 3: Python environment

Learners create `.venv` with the standard library and install the exact three dependencies:

```text
jupyterlab==4.6.3
nbclient==0.10.2
pandas==3.0.5
```

They record the exact executable used. Activation is optional; explicit `.venv` paths are acceptable and often easier to audit.

### Block 4: Python and SQLite

Learners trace:

1. CSV field names;
2. three row dictionaries;
3. integer conversion;
4. unique-ID check;
5. SQL schema creation;
6. parameterized insertion;
7. fixed aggregate query;
8. expected-result comparison; and
9. JSON output creation.

They must identify where a changed header, duplicate ID, negative value, row count, sum, minimum, or maximum would fail.

### Block 5: Notebook

Learners launch the notebook environment from `.venv`, run all cells in order, and save the stored outputs. They compare:

- pandas' table view;
- pandas' uniqueness and sum assertions; and
- the shared Python/SQLite function result.

The notebook does not duplicate the full smoke-test implementation. It imports the tested function from `src/smoke_test.py`.

### Block 6: Supplied R

Learners read the supplied base-R script, identify its working-directory assumption, run it from the repository root, and explain each `stopifnot` condition.

They are assessed on execution and interpretation, not on writing new R code.

### Block 7: Branch, merge, and version

Learners complete the environment records on `module-01-setup`, commit, return to `main`, and merge with `--no-ff`. They inspect the graph and create the annotated tag only after all checks pass and the working tree is clean.

### Block 8: Troubleshooting and AI verification

Learners choose one actual setup or Git issue. If they use an AI tool, they record its exact role, inputs, relevant advice, human verification, and final decision. If they do not use AI, they record the authoritative source or command used to resolve the issue.

### Block 9: Independent reproduction

The reproducer uses a new directory and new environment. Copying `.venv` is prohibited because it avoids the environment-recreation test.

### Block 10: Release

Learners run final checks, commit the reproduction record, confirm clean state, create the annotated tag, identify the full commit hash, and submit the repository URL and tagged commit.

## 7. Readings and authoritative sources

### Required primary references

| Topic | Reference | Required use |
|---|---|---|
| Python virtual environments | https://docs.python.org/3/library/venv.html | Create and explain the local environment. |
| Python SQLite interface | https://docs.python.org/3/library/sqlite3.html | Identify connection, parameterized insertion, query, and in-memory behavior. |
| Git foundations | https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control | Explain version control and repository state. |
| Git branching | https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging | Create and merge the practice branch. |
| Git tagging | https://git-scm.com/book/en/v2/Git-Basics-Tagging | Create and inspect an annotated tag. |
| JupyterLab installation | https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html | Install and launch the notebook environment. |
| pandas installation | https://pandas.pydata.org/docs/getting_started/install.html | Confirm supported installation and environment practice. |
| Rscript | https://stat.ethz.ch/R-manual/R-devel/library/utils/html/Rscript.html | Run and interpret the supplied R script. |
| Semantic Versioning | https://semver.org/spec/v2.0.0.html | Explain patch, minor, major, and the initial 0.1.0 release. |

### Exact package records

- JupyterLab 4.6.3: https://pypi.org/project/jupyterlab/4.6.3/
- nbclient 0.10.2: https://pypi.org/project/nbclient/0.10.2/
- pandas 3.0.5: https://pypi.org/project/pandas/3.0.5/

### Required source-reading questions

For Python `venv`:

- What is isolated?
- What is not isolated?
- Why should the environment folder stay outside Git?
- How does another learner recreate it?

For Git:

- What does a commit identify?
- Why does a branch move while an accepted tag should remain fixed?
- What evidence does a merge commit preserve?
- Why is a clean working tree required before tagging?

For SQLite:

- What does `:memory:` mean?
- Why are inserted values parameterized?
- Which table constraints are checked?
- What evidence disappears after the process ends and what evidence is stored in JSON?

For notebooks:

- Why must the submitted notebook store its execution evidence?
- Why does cell order matter?
- How can the notebook use a different Python environment than the terminal?

For R:

- What does the supplied script read?
- What facts does it assert?
- What would cause it to stop?
- Why does running supplied R not demonstrate from-scratch R programming?

### Reading-use rule

The module does not grade citation formatting. It grades whether the learner can connect an authoritative reference to an observed command, result, or troubleshooting decision.

### Prohibited source practice

A copied web command is not accepted merely because it appears plausible. The learner must inspect the command for path, environment, credential, and destructive-action implications before running it.

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Dataset inventory

| Data ID | File | Rows | Columns | Synthetic | Purpose |
|---|---|---:|---:|---|---|
| `fnd1-workspace-smoke-test` | `template/data/workspace_smoke_test.csv` | 3 | 3 | yes | Test CSV reading, SQLite load/query, pandas execution, R execution, and cross-tool agreement. |

### Provenance

The Open Clinical Learning Commons created the three deterministic rows for this module. The labels and values were selected to produce an obvious fixed count, sum, minimum, and maximum without resembling a patient record or health-system performance measure.

### Rights

- Data: CC0-1.0.
- Teaching documentation: CC-BY-4.0 under the repository policy.
- Code: MIT under the repository policy.

CC0 legal text:

https://creativecommons.org/publicdomain/zero/1.0/legalcode.en

CC BY 4.0 legal text:

https://creativecommons.org/licenses/by/4.0/legalcode.en

MIT license text:

https://opensource.org/license/mit

### Registered file facts

- Bytes: 134.
- SHA-256: `330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab`.
- Encoding: UTF-8.
- Header rows: 1.
- Data rows: 3.
- Columns: 3.

### Teaching purpose

The table permits one result to be checked through four technical routes:

1. Python standard-library CSV parsing;
2. an in-memory SQLite table and aggregate query;
3. a pandas notebook; and
4. a supplied base-R script.

Agreement across those routes is easy to inspect. The table is intentionally too small to support analysis or interpretation.

### Privacy classification

The table contains:

- no names;
- no dates;
- no locations;
- no identifiers derived from a person;
- no clinical events;
- no diagnoses;
- no medications;
- no laboratory results;
- no claims;
- no free text; and
- no linkable patient or organization information.

### Claim boundary

The values 3, 5, 7, and 15 are expected software-test values. They are not counts of patients, encounters, events, services, outcomes, errors, or organizations.

The learner must not describe them as healthcare evidence.

### Source immutability

The source CSV is immutable within data version 0.1.0. A changed byte requires:

- a new data version;
- a new source record;
- a new checksum;
- new expected results;
- updated code assertions;
- updated notebook and R outputs;
- an updated answer key;
- a module semantic-version decision; and
- rerun technical and human review.

### Relationship to Synthea

The table is not part of Synthea. Module 02 introduces the pinned Synthea April 2020 archive and a relational teaching database. Keeping that source out of Module 01 makes the first week's decision narrow and testable.

## 9. Data dictionary and expected structure

### File grain

One row represents one synthetic software-test record. The row has no clinical unit of observation.

### Data dictionary

| Field | Storage in CSV | Storage in SQLite | Required | Key | Rule | Version 0.1.0 values |
|---|---|---|---|---|---|---|
| `record_id` | text | `TEXT` | yes | primary | unique and non-null | `demo-001`, `demo-002`, `demo-003` |
| `source_label` | text | `TEXT` | yes | no | non-null | `synthetic-workspace-a`, `synthetic-workspace-b`, `synthetic-workspace-c` |
| `event_count` | integer text representation | `INTEGER` | yes | no | non-null and at least zero | 3, 5, 7 |

### Ordered header

```text
record_id,source_label,event_count
```

The order is part of the starter contract so that changes are visible. Later healthcare tables may use broader schema checks that do not depend on display order.

### SQLite schema

```sql
CREATE TABLE workspace_smoke (
    record_id TEXT PRIMARY KEY,
    source_label TEXT NOT NULL,
    event_count INTEGER NOT NULL CHECK (event_count >= 0)
);
```

### Expected aggregate

| Output | Expected value |
|---|---:|
| `row_count` | 3 |
| `event_count_total` | 15 |
| `event_count_minimum` | 3 |
| `event_count_maximum` | 7 |

### Expected Python/SQLite output record

The generated JSON contains:

- `status` equal to `pass`;
- `result.row_count` equal to 3;
- `result.event_count_total` equal to 15;
- `result.event_count_minimum` equal to 3;
- `result.event_count_maximum` equal to 7;
- the Python version actually used; and
- the SQLite library version actually used by Python.

Environment versions are observed facts and may differ from the reference environment. The result facts may not differ in version 0.1.0.

### Expected R output record

```text
WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15
```

### Notebook structure

The notebook has:

- one Markdown cell stating the task and data boundary;
- three code cells;
- an exact pandas version assertion;
- a CSV read;
- column, row, uniqueness, and sum checks;
- an import of the shared Python/SQLite function; and
- a stored `WORKSPACE_SMOKE_TEST_PASS` output in the completed submission.

### Required dependency structure

`requirements.txt` contains exactly:

```text
jupyterlab==4.6.3
nbclient==0.10.2
pandas==3.0.5
```

The exact pins make the initial environment reproducible. A later module release may revise them after compatibility testing and a semantic-version decision.

### Required repository structure

```text
learner-workspace/
  .gitattributes
  .gitignore
  README.md
  VERSION
  requirements.txt
  environment-note.md
  version-policy.md
  reproducibility-check.md
  ai-use.md
  analysis/
    r-smoke-test.R
  data/
    workspace_smoke_test.csv
  notebooks/
    01-smoke-test.ipynb
  outputs/
    .gitkeep
    python-sql-smoke.json
    r-smoke-test.txt
  sql/
    00-smoke-test.sql
  src/
    smoke_test.py
```

`.venv` exists locally but is excluded from the submitted tree by `.gitignore`.

## 10. Worked example

### Worked question

Can the reference workspace load the released three-row table, enforce its narrow structure, return the same fixed facts through Python, SQLite, pandas, and R, and preserve an inspectable release state?

### Step 1: Build to a new target

From the Commons repository root:

```text
python courses/healthcare-data-foundations/modules/01-reproducible-workspace/build_workspace.py learner-workspace
```

Expected behavior:

- the target is created;
- the template files are copied;
- the source template is not modified; and
- a second build to the same target is refused.

### Step 2: Initialize Git

```text
cd learner-workspace
git init -b main
git add .
git commit -m "chore: start FND-1 workspace"
git status --short --branch
```

Expected state:

- current branch is `main`;
- the initial commit contains the starter contract; and
- no unstaged or untracked file remains except later generated output.

### Step 3: Create the environment

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

The learner records actual versions. The reference versions are not copied into the environment note as if observed.

### Step 4: Read the source

The instructor asks:

- Which field is unique?
- Which values must not be null?
- Which value cannot be negative?
- How many rows are expected?
- What sum is expected?
- What would a duplicate ID do?
- What clinical conclusion can be made?

Reference answers:

- `record_id` is unique;
- every field is non-null in the SQLite schema;
- `event_count` cannot be negative;
- 3 rows are expected;
- 15 is expected;
- duplicate insertion fails the primary-key contract or the Python uniqueness check; and
- no clinical conclusion is supported.

### Step 5: Run Python and SQLite

Windows PowerShell:

```text
.venv\Scripts\python.exe src\smoke_test.py
```

macOS or Linux:

```text
.venv/bin/python src/smoke_test.py
```

Expected marker:

```text
WORKSPACE_SMOKE_TEST_PASS rows=3 total=15
```

Expected new file:

`outputs/python-sql-smoke.json`

### Step 6: Trace the program

The worked trace connects each implementation line to the contract:

| Program action | Contract protected |
|---|---|
| Compare `reader.fieldnames` | Ordered three-field header. |
| Count rows | Exactly three records. |
| Compare unique IDs | No duplicate record ID. |
| Convert `event_count` with `int` | Integer-readable value. |
| Reject values below zero | Nonnegative rule. |
| Execute supplied SQL | Exact table schema. |
| Use `executemany` with placeholders | Values are parameters, not SQL text. |
| Query count, sum, minimum, maximum | Fixed cross-tool result. |
| Compare with expected dictionary | Silent result change is rejected. |
| Write JSON output | Observed execution evidence persists after the in-memory database closes. |

### Step 7: Execute the notebook

```text
.venv\Scripts\jupyter.exe execute notebooks\01-smoke-test.ipynb --inplace
```

or:

```text
.venv/bin/jupyter execute notebooks/01-smoke-test.ipynb --inplace
```

The learner opens the notebook and confirms:

- all three code cells have execution counts;
- pandas reports version 3.0.5;
- the three rows are visible;
- uniqueness and total assertions pass; and
- the last output includes `WORKSPACE_SMOKE_TEST_PASS`.

### Step 8: Run supplied R

From the workspace root:

```text
Rscript analysis/r-smoke-test.R
```

Expected marker and output file:

```text
WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15
```

The learner identifies that the script uses base R, reads the same CSV, checks names, row count, unique IDs, and total, then writes one text output.

### Step 9: Complete branch work

```text
git switch -c module-01-setup
```

Complete the four records, then:

```text
git add environment-note.md version-policy.md reproducibility-check.md ai-use.md notebooks/ outputs/
git commit -m "docs: record reproducible environment"
git switch main
git merge --no-ff module-01-setup -m "merge: complete Module 01 setup"
```

### Step 10: Reproduce cleanly

Another person clones or copies the repository into a new directory, creates a fresh `.venv`, installs from the committed requirements, and reruns Python, notebook, and R.

They record:

- the tagged commit;
- commands;
- actual environment;
- observed results;
- every warning, difference, retry, or failure; and
- reproduced, reproduced with conditions, or not reproduced disposition.

### Step 11: Release

After the reproduction record is committed:

```text
git status --short
git tag -a fnd1-setup-v0.1.0 -m "FND-1 Module 01 setup component"
git show fnd1-setup-v0.1.0 --stat
```

The working-tree command must print nothing before tagging.

### Worked interpretation

A correct interpretation is:

> The tagged workspace reproduced the fixed three-row software check in Python, SQLite, pandas, and the supplied R script. The evidence supports using this repository structure and environment for Module 02. It does not establish healthcare-data, SQL cohort, statistical, or clinical-analysis competency.

## 11. Guided practice

### Practice 1: Identify repository state

Instructor provides four states:

1. a new required output is untracked;
2. a record is modified but not staged;
3. a source edit is staged accidentally;
4. the working tree is clean.

Learners use status and diff commands to identify each state and state the safe next action. They do not use a repository-wide destructive reset.

### Practice 2: Choose the executable

Learners compare:

- system `python`;
- the explicit `.venv` Python path; and
- the notebook kernel.

They record which path reports pandas 3.0.5 and explain why a successful global import does not prove the local environment is complete.

### Practice 3: Read a failing constraint

The instructor demonstrates temporary copies of the data with:

- a changed header;
- a duplicate ID;
- a negative count;
- a missing row; and
- a changed total.

Learners predict which layer fails first. The released source is restored after each demonstration.

### Practice 4: Trace SQLite life cycle

Learners answer:

- when the connection opens;
- when the schema exists;
- when rows are inserted;
- when the query runs;
- when the result is copied to JSON; and
- when the database disappears.

### Practice 5: Notebook order

Learners intentionally restart the kernel and try the last cell first. They record the error, explain the missing state, then run all cells in order and save the correct output.

The incorrect attempt stays in the troubleshooting record when material; it is not concealed.

### Practice 6: Read supplied R

Learners annotate, in plain language and without editing the script:

- the working-directory assumption;
- input file;
- field-name check;
- row-count check;
- uniqueness check;
- sum check; and
- output file.

### Practice 7: Git graph

Learners create the setup branch, make one bounded record change, commit it, merge with `--no-ff`, and inspect:

```text
git log --graph --decorate --oneline --all
```

They identify the branch commit, merge commit, `main`, and later annotated tag.

### Practice 8: Semantic-version cases

Learners classify:

- correcting a typo in the environment-note instructions;
- adding a compatible new smoke-test output;
- renaming a required path used by Module 02; and
- changing the expected result while keeping the old source version.

Reference classifications:

- typo: patch;
- compatible output: minor;
- required-path rename: major;
- silent expected-result change: prohibited, then version all affected contracts before release.

### Practice 9: AI verification

Example prompt target:

> Explain why this notebook may be using a different Python environment than my terminal. Do not ask for my files, paths, credentials, or data.

The learner verifies advice with executable paths, package versions, the notebook kernel, and primary Jupyter documentation. They record what advice was accepted, changed, or rejected.

### Practice 10: Reproduction handoff

Pairs exchange only repository URLs and tagged commits. They may not exchange `.venv`, local database files, tokens, or screenshots containing personal paths. Each reproducer follows the README and records friction.

### Tiered support

Tier 1 provides the exact commands in README.

Tier 2 provides a command-to-purpose table and asks learners to fill observed results.

Tier 3 provides a scheduled technical clinic or institution-managed environment.

Support changes the scaffold, not the final evidence or gate standard.

## 12. Independent exercise

### Assignment

Build, document, reproduce, and release the Module 01 learner workspace.

### Learner constraints

The learner must:

- preserve the supplied CSV, SQL, Python, R, and dependency files;
- work in a Git repository on `main`;
- use a local or approved isolated Python environment;
- run Python, pandas notebook, SQLite, and supplied R checks;
- save the required outputs;
- complete all four records;
- preserve a branch and merge commit;
- reproduce from a clean target;
- create the annotated setup tag only after the final clean check; and
- submit the repository URL and full tagged commit.

The learner must not:

- edit expected values to make a failing run pass;
- remove a validation check;
- commit `.venv`;
- commit a token, password, private URL, or personal absolute path;
- include patient, learner, employee, or other identifying data;
- claim authorship of the supplied R script;
- copy the original environment into the reproduction target;
- flatten the Git history into one final upload; or
- describe the smoke-test values as healthcare evidence.

### Independent troubleshooting requirement

The learner records one actual failure or meaningful uncertainty. Acceptable examples include:

- Python not found;
- wrong Python executable;
- package installed globally rather than locally;
- wrong notebook kernel;
- notebook output not saved;
- R working directory wrong;
- Git fast-forward instead of merge commit;
- lightweight rather than annotated tag; or
- ignored output that should be committed.

If no error occurs, the learner may test one safe instructor-provided failure copy and record diagnosis and restoration.

### Independent reproduction requirement

The reproducer may be:

- another learner;
- a teaching assistant;
- the instructor; or
- the same learner using a clearly new directory and fresh environment when scheduling prevents peer reproduction.

Peer reproduction is preferred. Same-learner reproduction must be labeled and cannot claim independent authorship review.

### Final reflection

In no more than 250 words, the learner answers:

1. What exact state does the tag identify?
2. What evidence would break if someone changed the source CSV silently?
3. What did the clean reproduction discover that the original run could not?
4. What does the passing workspace still not prove?

The reflection may appear at the end of `reproducibility-check.md`.

## 13. Visualization or communication requirements

### Visualization requirement

No chart is required. A chart would add no value to a three-row environment smoke test. The module uses exact text, tables, commands, and stored outputs.

This is a deliberate no-display decision, not a missing assignment component.

### Required communication artifacts

The learner communicates through:

- repository README;
- environment note;
- version policy;
- reproduction record;
- AI-use record;
- notebook Markdown and stored output;
- JSON and text smoke-test outputs;
- commit messages;
- annotated tag message; and
- optional oral explanation.

### Writing requirements

Each record must:

- use descriptive headings;
- state observed values rather than copying reference values without evidence;
- use repository-relative paths;
- show copyable commands as text;
- separate expected from observed results;
- record failure as well as success;
- identify status and next action;
- avoid unsupported clinical language; and
- omit credentials and personal absolute paths.

### Table requirements

Tables need:

- a descriptive heading or nearby sentence;
- text column labels;
- expected and observed values in separate columns when compared;
- explicit pass/fail status; and
- no meaning conveyed by color alone.

### Terminal evidence

Screenshots are optional supporting evidence. They never replace copyable commands, text results, or committed output files.

When a screenshot is used:

- crop unrelated personal information;
- remove credentials and tokens;
- provide a text description;
- preserve the exact command and result as text; and
- do not rely on color alone to show success or failure.

### Commit messages

Messages should describe the project change. Acceptable examples:

- `chore: start FND-1 workspace`;
- `docs: record reproducible environment`; and
- `merge: complete Module 01 setup`.

Messages such as `stuff`, `changes`, `final`, or repeated `update` do not provide useful review history.

### Claim language

Supported:

> The tagged workspace reproduced the fixed smoke-test result.

Unsupported:

> The environment is proven to work for all healthcare data.

Supported:

> The supplied R script returned the same row count and total.

Unsupported:

> I wrote and validated an R analysis.

## 14. Exact submission package

### Repository identifier

The learner submits:

- full repository URL;
- full 40-character commit hash; and
- annotated tag `fnd1-setup-v0.1.0`.

The tag must resolve to the submitted `HEAD` commit.

### Required files

```text
learner-workspace/
  .gitattributes
  .gitignore
  README.md
  VERSION
  requirements.txt
  environment-note.md
  version-policy.md
  reproducibility-check.md
  ai-use.md
  analysis/
    r-smoke-test.R
  data/
    workspace_smoke_test.csv
  notebooks/
    01-smoke-test.ipynb
  outputs/
    .gitkeep
    python-sql-smoke.json
    r-smoke-test.txt
  sql/
    00-smoke-test.sql
  src/
    smoke_test.py
```

### Required immutable files

These remain byte-for-byte or semantically identical to the released starter:

- `.gitattributes`;
- `.gitignore`;
- `requirements.txt`;
- `data/workspace_smoke_test.csv`;
- `sql/00-smoke-test.sql`;
- `src/smoke_test.py`; and
- `analysis/r-smoke-test.R`.

Notebook execution changes metadata and outputs, so the completed notebook is expected to differ from the starter while preserving its cells and required code.

### Required generated outputs

`outputs/python-sql-smoke.json` must report:

- status `pass`;
- row count 3;
- total 15;
- minimum 3;
- maximum 7;
- actual Python version; and
- actual SQLite version.

`outputs/r-smoke-test.txt` must contain exactly:

```text
WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15
```

### Required record contents

`environment-note.md` records:

- learner identifier;
- operating system;
- architecture;
- shell;
- Python executable and version;
- pandas, JupyterLab, nbclient, and SQLite versions;
- R and Git versions;
- full workspace commit;
- install commands;
- one resolved setup failure; and
- material environment differences.

`version-policy.md` records:

- patch, minor, and major examples;
- tagged commit;
- tag command;
- clean-tree evidence;
- smoke-test status; and
- why 0.1.0 is the correct release.

`reproducibility-check.md` records:

- repository URL;
- tagged commit;
- reproducer and date;
- clean target statement;
- no reuse of original `.venv`;
- exact commands;
- expected and observed results;
- warnings, retries, failures, and differences;
- disposition; and
- conditions, owner, and date.

`ai-use.md` records:

- date;
- tool and model or `none`;
- purpose;
- data shared;
- advice used;
- human verification;
- accepted, changed, or rejected decision;
- data-boundary confirmations; and
- learner accountability statement.

### Required Git evidence

- current branch `main`;
- clean `git status --porcelain`;
- at least three commits reachable from `HEAD`;
- at least one merge commit reachable from `HEAD`;
- annotated tag object `fnd1-setup-v0.1.0`; and
- tag target equal to `HEAD`.

### Excluded content

Do not submit:

- `.venv`;
- `__pycache__`;
- notebook checkpoint directories;
- local SQLite files;
- operating-system metadata;
- secrets;
- tokens;
- passwords;
- private repository URLs;
- patient or identifying data; or
- personal absolute paths in the records.

The supplied `.gitattributes` fixes CSV, notebook, JSON, Python, R, and SQL text to LF line endings. This keeps the registered source fingerprint stable across Windows, macOS, and Linux checkouts.

### Naming policy

Required filenames and folder names are part of the handoff interface. A name change requires instructor approval and an equivalence record because Module 02 expects the accepted workspace structure.

## 15. Rubric and pass conditions

### Rubric

| Criterion | Points | Full-credit standard |
|---|---:|---|
| Environment identity and dependency control | 20 | Local environment excluded from Git; exact pins; actual executable and versions; complete commands; no secret or personal path. |
| Python, pandas, SQLite, and supplied R execution | 25 | All routes pass; notebook stores outputs; generated records show exact fixed values; learner accurately explains the narrow result. |
| Git history and semantic version | 25 | Clean `main`; readable commits; non-fast-forward merge; annotated tag at `HEAD`; correct patch, minor, and major examples. |
| Independent reproduction | 15 | New target and environment; exact rerun record; all outputs reproduced; differences and failures preserved; clear disposition. |
| AI disclosure and verification | 10 | Material uses recorded; one claim verified; protected data and credentials excluded; learner remains accountable. |
| Accessible technical communication | 5 | Clear headings, readable tables, copyable commands, repository-relative paths, explicit status, and supported claims. |
| Total | 100 |  |

### Score threshold

The minimum passing score is 80 of 100.

### Noncompensable gates

All must pass:

1. Python and SQLite gate;
2. pandas notebook gate;
3. supplied R read-run-interpret gate;
4. clean reproduction gate;
5. Git state and annotated-tag gate;
6. privacy and credential gate;
7. AI disclosure gate; and
8. disposition gate.

A high point score cannot compensate for a failed gate.

### Python and SQLite gate

Pass requires:

- source fingerprint unchanged;
- script completes;
- expected terminal marker;
- expected JSON output;
- row count 3;
- total 15;
- minimum 3;
- maximum 7; and
- learner explanation consistent with the code.

### pandas notebook gate

Pass requires:

- three code cells;
- stored execution counts;
- stored outputs;
- pandas 3.0.5 check;
- source table visible;
- uniqueness and total checks pass; and
- stored workspace pass marker.

### Supplied R gate

Pass requires:

- unchanged supplied script;
- successful execution from workspace root;
- exact output file;
- accurate explanation of every check; and
- no claim of from-scratch authorship.

### Reproduction gate

Pass requires:

- new target;
- fresh environment;
- no reused `.venv`;
- exact tagged commit;
- Python, notebook, and R rerun;
- expected and observed results; and
- reproduced or reproduced with bounded conditions disposition.

### Git and version gate

Pass requires:

- `main`;
- clean state;
- readable history;
- at least one merge commit;
- annotated tag;
- tag points to `HEAD`; and
- correct semantic-version explanation.

### Privacy and credential gate

Any patient data, identifying data, exposed credential, access token, or private connection detail fails the gate and may trigger `refer`.

### AI disclosure gate

Pass requires either:

- complete material-use records and one verified claim; or
- an explicit no-AI record with the non-AI troubleshooting source and evidence.

### Disposition gate

The recorded disposition must be `accept` or `accept with conditions` for a pass. Conditions must have an owner and due date.

### Revision and regrade

Before Checkpoint 1 freeze:

- correct the defect;
- rerun every affected check;
- preserve the corrective commit;
- update the reproduction record when environment or execution changed;
- retag only under instructor direction; and
- record why the tagged target changed.

After checkpoint freeze, the accepted tag does not move. A correction receives a patch version and new tag.

## 16. Common failures and instructor interventions

| Failure | Evidence | Likely cause | Instructor intervention | Required resolution evidence |
|---|---|---|---|---|
| Python command not found | Shell cannot resolve Python. | Missing install or PATH configuration. | Route to institution-supported install; restart terminal. | Exact Python version and executable recorded. |
| Wrong Python executes | Package import or version differs. | Global executable used instead of `.venv`. | Use explicit local executable path. | `sys.executable` and package versions match the record. |
| Environment folder committed | Large platform-specific files in Git. | `.gitignore` added too late or misunderstood. | Remove only environment files from tracking and preserve requirements. | `.venv` absent from tracked files and reproducible from requirements. |
| pandas version assertion fails | Notebook kernel has another environment. | Jupyter launched outside `.venv` or wrong kernel selected. | Launch Jupyter from `.venv`; select local kernel. | Notebook reports pandas 3.0.5 and all cells pass. |
| Notebook output missing | Execution not saved or output cleared. | Learner saved starter state. | Execute in place or run all cells and save. | Stored counts and pass marker present. |
| Header validation fails | CSV edited or line imported incorrectly. | Source changed. | Inspect diff and restore registered source. | SHA-256 and ordered header pass. |
| Duplicate-ID failure | Record duplicated. | Source changed. | Explain primary-key and Python checks; restore source. | Three unique IDs pass. |
| Negative-count failure | Test value changed below zero. | Source changed. | Read SQL `CHECK`; restore source. | Nonnegative values and aggregate pass. |
| Aggregate changed | Row or value changed. | Source, insertion, or query edited. | Trace CSV through SQL and expected dictionary. | 3, 15, 3, and 7 results pass. |
| Python output not committed | Output generated after final commit. | Learner treated required evidence as disposable. | Add intended output and commit. | Output tracked and working tree clean. |
| R cannot find file | Wrong working directory. | Script launched from `analysis`. | Run from repository root. | Exact R marker and output file. |
| R check removed | Learner edits supplied script. | Attempt to bypass failure. | Restore script; discuss integrity. | Script contract and output pass; action recorded. |
| No merge commit | Fast-forward merge. | Main did not diverge or `--no-ff` omitted. | Repeat bounded branch practice with visible merge. | Merge count at least one. |
| Lightweight tag | `git tag name` used without annotation. | Tag types not distinguished. | Recreate under instructor direction with `-a`. | `git cat-file -t` returns `tag`. |
| Tag points behind HEAD | Commit added after tagging. | Final record changed later. | Decide whether to retag before freeze or create patch after freeze. | Submitted tag target equals submitted commit. |
| Dirty working tree | Generated or edited files uncommitted. | Final status skipped. | Inspect status and diff; commit only intended files. | Porcelain status empty. |
| Reproduction reuses original environment | Whole directory copied. | Learner misunderstood clean reproduction. | Use a new clone and recreate `.venv`. | Commands show fresh environment creation. |
| Record copies reference versions | Observed environment not checked. | Template values mistaken for evidence. | Run version commands and compare. | Actual values and differences recorded. |
| Personal path in record | Full local command copied. | Evidence not sanitized. | Replace with repository-relative path while preserving the relevant error. | Validator path scan passes. |
| Credential committed | Token or password pasted. | Unsafe troubleshooting or copied configuration. | Stop; rotate/revoke credential; refer if required; remove from future history under approved process. | Security owner confirms containment before reuse. |
| AI record too vague | Says only tool name or "helped." | Disclosure contract not understood. | Require purpose, input, used advice, verification, and decision. | Complete row and verified claim. |
| AI advice accepted without test | No command or primary source. | Plausibility mistaken for evidence. | Verify exact claim or reject it. | Observed test and final decision recorded. |
| Clinical claim added | Smoke values described as real events. | Synthetic software data misread. | Restate source and claim boundary. | Clinical language removed; correct interpretation provided. |

### Intervention priority

1. protect credentials, privacy, and access;
2. preserve the learner's recoverable work;
3. identify the exact failing layer;
4. use the smallest corrective action;
5. rerun the affected check;
6. rerun the complete validator before release; and
7. record what changed.

### Instructor nonintervention

The instructor must not:

- silently repair the learner repository;
- move the tag without a record;
- accept screenshots instead of runnable evidence;
- allow edited validation expectations to count as a pass;
- lower the privacy or credential gate;
- require a specific shell when an accessible equivalent meets the contract; or
- turn a setup problem into an assessment of clinical knowledge.

## 17. Accessibility, equity, privacy, and claim checks

### Accessibility requirements

The package uses:

- text instructions rather than video-only directions;
- copyable commands;
- descriptive headings;
- plain-text pass and failure markers;
- table labels that do not depend on color;
- repository-relative paths;
- no timing requirement based on typing speed;
- an accessible Git-client route when needed; and
- optional technical clinics.

The learner submission must retain those features.

### Terminal accessibility

An instructor reads commands and important output aloud during live demonstration. A learner may use:

- screen reader compatible terminal;
- high-contrast terminal theme;
- accessible Git client;
- speech input;
- keyboard-only workflow; or
- institution-managed browser environment.

The evidence contract remains the same.

### Notebook accessibility

The notebook must:

- begin with a descriptive Markdown heading;
- state the synthetic and no-clinical-claim boundary;
- keep code cells short enough to inspect;
- print text pass markers;
- not rely on color alone;
- save output in reading order; and
- avoid decorative output.

### Equity checks

The module must not reward prior access to engineering tools. Instructors provide:

- setup time inside the 15.5-hour workload;
- an institution-managed alternative for installation barriers;
- technical clinics;
- a command-to-purpose scaffold;
- error-reading practice;
- clear recovery routes; and
- equal evidence standards across operating systems.

The module does not grade:

- typing speed;
- terminal memorization;
- ownership of a high-performance computer;
- paid software;
- prior Git vocabulary;
- use of one preferred editor; or
- avoidance of all setup errors.

Accurate diagnosis and documentation of an error can be evidence of learning.

### Privacy checks

The learner workspace must contain no:

- patient data;
- clinical screenshots;
- names or identifiers from work systems;
- employee or student records;
- access tokens;
- passwords;
- private keys;
- private database connection strings;
- private repository URLs;
- unredacted personal absolute paths; or
- copied logs containing those items.

### Security response

If a credential enters Git:

1. stop sharing and validation;
2. revoke or rotate the credential through the authorized owner;
3. preserve an incident record outside the public repository;
4. follow approved history-remediation steps;
5. confirm containment; and
6. resume only after the owner approves.

Deleting the visible line alone is not sufficient when the credential remains in history.

### Claim checks

Every submission must pass these statements:

- The table is deterministic synthetic software-test data.
- The result proves only the narrow reference task ran.
- Agreement across tools does not validate future healthcare sources.
- A passing environment does not validate a cohort.
- A passing environment does not validate data quality.
- A passing environment does not validate a statistical model.
- A passing environment does not support a clinical decision.

### Rights checks

The source record and included data license remain present. Learners do not add proprietary datasets or copied workplace code to the public submission.

### Small-file exception

No small-cell disclosure rule is needed because the table contains no people or organizations. The module explicitly states this reason instead of implying that all small counts are safe.

## 18. AI policy, disclosure, and verification

### Permitted uses

An approved AI or agent tool may help:

- explain an environment error;
- explain a Git command;
- translate a terminal message into plain language;
- suggest safe diagnostic commands;
- compare a notebook kernel with a terminal executable;
- improve record clarity; or
- propose tests for a setup claim.

### Prohibited uses

The learner may not use an AI tool to:

- fabricate command output;
- fabricate a reproduction;
- fabricate a Git history;
- fabricate an annotated tag;
- fill records with unobserved versions;
- edit checks or expected values to force a pass;
- conceal an error;
- send patient or identifying data;
- send credentials or private connection details;
- send private repository content without authorization; or
- replace the learner's own explanation of submitted work.

### Required record fields

For every material use, record:

- date;
- tool and model;
- purpose;
- data shared;
- relevant advice or output used;
- human verification;
- whether the advice was accepted, changed, or rejected; and
- resulting repository change when applicable.

### Verification hierarchy

Prefer:

1. an observed command or file state;
2. official Python, Git, Jupyter, pandas, R, or SemVer documentation;
3. the released module source and validator; and
4. instructor confirmation for an unresolved institutional constraint.

An AI answer is not verification.

### Required verification case

The learner verifies at least one material claim. Example:

- AI claim: the notebook is using a different Python environment.
- Test: print the notebook executable, compare with the `.venv` path, and check pandas version.
- Primary source: Jupyter kernel or installation documentation.
- Observed result: exact paths and versions.
- Decision: accept, modify, or reject the advice.

### No-AI route

A learner who uses no AI tool records:

- tool and model: `none`;
- purpose: `no AI assistance used`;
- the actual troubleshooting source;
- the command or documentation used;
- the observed evidence; and
- the same accountability statement.

### Data minimization

Before sharing any error with an AI tool, remove:

- usernames;
- home-directory paths;
- repository credentials;
- tokens;
- organization names when unnecessary;
- private URLs;
- patient or identifying content; and
- unrelated log lines.

### Accountability statement

The learner states that they ran and inspected every submitted command, file, result, and claim and remain responsible for the tagged release.

### AI gate failure

Missing disclosure is revised. Fabricated evidence, concealed use that changes authorship, protected-data sharing, or credential exposure may trigger `refer` under program policy.

## 19. Answer key and instructor notes

### Reference environment

The Commons release was tested with:

- Python 3.12.10;
- SQLite 3.49.1 through Python;
- Git 2.54.0 for Windows;
- R 4.6.1;
- pandas 3.0.5;
- JupyterLab 4.6.3; and
- nbclient 0.10.2.

Learner versions of Python, SQLite, Git, and R may differ within supported ranges. The three Python package versions must match the release pins.

### Reference data answers

| Check | Answer |
|---|---|
| File bytes | 134 |
| SHA-256 | `330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab` |
| Rows | 3 |
| Columns | 3 |
| Unique IDs | 3 |
| Count values | 3, 5, 7 |
| Total | 15 |
| Minimum | 3 |
| Maximum | 7 |

### Reference Python explanation

The script reads UTF-8 CSV with `csv.DictReader`, compares the ordered field names, loads all three rows, checks unique IDs, converts counts to integers, rejects negative values, creates an in-memory SQLite table, inserts parameterized tuples, queries count/sum/minimum/maximum, compares the query result with the expected dictionary, and writes a JSON record.

### Reference SQLite explanation

The primary key protects record identity. Non-null rules protect required fields. The `CHECK` rejects a negative test count. Parameter placeholders keep row values separate from SQL syntax. The in-memory database is temporary; the JSON record persists the checked facts and environment versions.

### Reference notebook explanation

The notebook confirms that the local environment can import the exact pandas version, read the same file, preserve the expected columns and rows, check uniqueness and sum, import the shared script function, and store the pass result. It is not a separate analysis.

### Reference R explanation

The supplied script uses only base R. It assumes the working directory is the repository root, reads the CSV, compares field names, checks three rows, checks three unique IDs, checks total 15, and writes a plain-text pass marker. Running it demonstrates read-run-interpret competency only.

### Reference Git explanation

The initial commit records the starter. The setup branch holds a bounded record change. The non-fast-forward merge preserves a visible point where the branch was integrated. The annotated tag names the accepted 0.1.0 setup state. A clean working tree proves the tag does not omit local changes.

### Reference semantic-version cases

- Patch: fix wording or a noncontractual instruction without changing paths or results.
- Minor: add a compatible new check or record field while preserving the old interface.
- Major: rename a required path, change an expected result contract, or make the old Module 02 handoff incompatible.

### Reference interpretation

The strongest supported statement is:

> The tagged repository reproduced the fixed Module 01 software check using the recorded environment and can proceed to the Module 02 synthetic healthcare source build.

The strongest required limit is:

> The pass does not validate healthcare data, a cohort, data quality, a model, or a clinical decision.

### Grading sequence

1. Confirm repository URL and tag.
2. Check out the exact tagged commit.
3. Run canonical submission validation with R required.
4. Inspect the Git graph and tag object.
5. Read the four completed records.
6. Compare recorded and observed environment facts.
7. Ask the learner to trace CSV to SQLite and explain result limits.
8. Score the six criteria.
9. Record all eight gates.
10. Record disposition, conditions, owner, and due date.

### Cut plan for compressed teaching

Do not cut:

- environment creation;
- Python/SQLite execution;
- notebook execution;
- supplied R interpretation;
- branch and merge;
- clean reproduction;
- AI disclosure; or
- final tag.

Compress:

- live lecture;
- repeated command demonstrations;
- optional Git-client comparison; and
- extended semantic-version examples.

### Extension for advanced learners

Advanced learners may add an operating-system matrix or another safe smoke test. The extension cannot replace the required files, exact results, merge, reproduction, or AI record and is not needed for full credit.

## 20. Runnable acceptance checks

### Builder checks

`build_workspace.py --self-check` verifies:

1. the canonical template exists;
2. all core template files exist;
3. a new target receives the files; and
4. an existing target is protected from overwrite.

### Starter validator checks

Starter mode reports 15 contract checks covering:

1. workspace path exists;
2. all 14 core files exist;
3. `VERSION` is 0.1.0;
4. `requirements.txt` contains exactly three expected pins;
5. source SHA-256 matches;
6. notebook is valid JSON;
7. notebook uses nbformat 4;
8. notebook has three code cells;
9. notebook contains pandas code;
10. notebook imports `run_smoke_test`;
11. notebook contains the workspace pass marker;
12. Python smoke script executes;
13. Python marker reports three rows;
14. Python marker reports total 15; and
15. generated Python/SQLite result matches the expected dictionary.

The printed count is a stable release summary, not a claim that each grouped check maps one-to-one to a single program branch.

### Submission validator checks

Submission mode adds completion and repository requirements and reports 26 checks. It verifies:

1. every starter requirement;
2. every notebook code cell has a stored execution count;
3. stored notebook output contains `WORKSPACE_SMOKE_TEST_PASS`;
4. Python/SQLite JSON output exists;
5. supplied R text output exists;
6. all four learner records have no `[REPLACE:` placeholders;
7. learner records contain no Windows user-home absolute path;
8. learner records contain no macOS `/Users/` absolute path;
9. learner records contain no Linux `/home/` absolute path;
10. JSON status is `pass`;
11. JSON row count is 3;
12. R output equals the exact reference marker;
13. target is a Git repository;
14. current branch is `main`;
15. working tree is clean;
16. at least three commits are reachable;
17. at least one merge commit is reachable;
18. the required tag exists;
19. the required tag is annotated;
20. the tag resolves to the submitted `HEAD`; and
21. optional required-R execution passes when enabled.

The grouped release count remains 26 because related path and Git assertions are reported as contract groups.

### Validator self-check

`validate_workspace.py --self-check`:

1. builds a starter fixture;
2. proves starter mode accepts it;
3. completes all records;
4. runs the Python/SQLite smoke test;
5. creates the reference R output;
6. stores notebook execution evidence;
7. creates a Git repository;
8. creates the setup branch;
9. creates a branch commit;
10. merges with a non-fast-forward merge commit;
11. creates an annotated tag;
12. proves submission mode accepts the complete fixture;
13. copies the complete fixture;
14. removes `ai-use.md`; and
15. proves submission mode rejects the incomplete fixture.

### Clean-target release test

Maintainer acceptance requires:

- build to a new target;
- starter validation;
- fresh Python environment;
- exact dependency installation;
- Python/SQLite execution;
- notebook execution in place;
- supplied R execution;
- completed reference records;
- Git branch, merge, and annotated tag;
- submission validation with R required;
- nonempty-target refusal; and
- cleanup limited to the verified temporary target.

### Repository-level checker

`scripts/check-curriculum-specs.ps1` must verify:

- this specification exists;
- it has exactly 21 numbered sections;
- all required package files exist;
- module version is 0.1.0;
- Commons release is 0.28.0;
- learner workload is 15.5 hours;
- data rows and columns are 3 and 3;
- source bytes are 134;
- source checksum matches;
- starter check count is 15;
- submission check count is 26;
- builder and validator self-checks pass;
- clean assembly passes;
- Python, notebook, and R runs pass;
- nonempty-target refusal passes;
- incomplete-submission rejection passes; and
- no Unicode em dash or en dash appears in the module contract.

### Syntax checks

Maintainers run:

```text
python -m py_compile courses/healthcare-data-foundations/modules/01-reproducible-workspace/build_workspace.py
python -m py_compile courses/healthcare-data-foundations/modules/01-reproducible-workspace/validate_workspace.py
python -m py_compile courses/healthcare-data-foundations/modules/01-reproducible-workspace/template/src/smoke_test.py
python -m json.tool courses/healthcare-data-foundations/modules/01-reproducible-workspace/template/notebooks/01-smoke-test.ipynb
```

### Human acceptance checks

Automation cannot decide:

- whether commands are pedagogically clear;
- whether the learner understands the execution flow;
- whether an accessibility route is usable;
- whether an AI verification is meaningful;
- whether an apparent privacy or integrity concern needs referral;
- whether the 15.5-hour workload is realistic; or
- whether another instructor can teach the module.

Named human review remains required before alpha.

## 21. Release status, reviewers, version, and known issues

### Release identity

- Module ID: `oclc-fnd1-01`.
- Module title: Setting up a reproducible workspace.
- Module version: 0.1.0.
- Commons release: 0.28.0.
- Data ID: `fnd1-workspace-smoke-test`.
- Data version: 0.1.0.
- Status: runnable release candidate.
- Release date: 2026-08-30.
- Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

### Semantic-version decision

This is module version 0.1.0 because it is the first runnable implementation of the Module 01 contract. It establishes the learner file interface, exact source, expected result, dependency pins, Git evidence, submission gates, and handoff to Module 02.

Commons moves from 0.27.0 to 0.28.0 because a compatible runnable module package, validator, assessment, and instructor key have been added without changing the already published course architecture.

### Technical status

Completed:

- 21-section module specification;
- safe standard-library workspace builder;
- portable learner template;
- exact dependency pins;
- deterministic three-row source;
- source record and data specification;
- Python/SQLite smoke test;
- supplied pandas notebook;
- supplied base-R script;
- learner environment, version, reproduction, and AI-use templates;
- assessment and rubric;
- instructor answer key;
- standard-library validator;
- valid and invalid self-check fixtures; and
- machine-readable release record.

### Required review roles

| Review role | Reviewer | Status | Required decision |
|---|---|---|---|
| FND-1 faculty owner | unassigned | pending | Technical sequence and assessment fit. |
| SQL and data engineering | unassigned | pending | SQLite and repository handoff are technically sound. |
| Python and notebook teachability | unassigned | pending | Environment and notebook instructions work for novices. |
| R read-run-interpret path | unassigned | pending | Supplied R exercise fits the course boundary. |
| Accessibility | unassigned | pending | Terminal, notebook, table, and alternative-tool routes are usable. |
| Privacy and data governance | unassigned | pending | Data and credential boundaries are sufficient. |
| Responsible AI | unassigned | pending | Disclosure and verification requirements are proportionate and clear. |
| Independent reproduction and teachability | unassigned | pending | A second instructor can build and teach from a clean checkout. |

### Promotion rule

The module remains a runnable release candidate until every required human role records a named decision. Alpha promotion requires all release-blocking findings resolved or bounded with an owner and date.

### Known issues

1. Named human reviews are pending.
2. The reference environment was technically tested on Windows; macOS and Linux learner paths are specified but still need named independent reproduction.
3. Local R installation can be a barrier. An institution-managed R route needs confirmation before a live cohort.
4. Git hosting is not required by the runnable package, but repository URL submission requires an institution-approved remote for a live course.
5. The validator checks for common personal home paths in learner records but cannot detect every possible secret or identifying string. Human privacy review remains mandatory.
6. The validator checks Git structure, not the instructional quality of every commit message.
7. Same-learner clean reproduction is permitted only when peer scheduling prevents an independent reproducer and must be labeled.
8. Package versions will age. They remain frozen for release 0.1.0 until a tested version update is issued.

### No silent changes

A change to any of these requires a release decision:

- required path;
- dependency pin;
- source byte;
- source checksum;
- expected result;
- notebook cell contract;
- R check;
- Git evidence;
- assessment weight;
- score threshold;
- noncompensable gate;
- checkpoint handoff; or
- AI, privacy, or accessibility requirement.

### Context-safe handoff to Module 02

After this release, resume at FND-1 Module 02.

Read:

- `docs/curriculum/courses/FND-1/course-spec.md`;
- this module specification;
- `courses/healthcare-data-foundations/modules/01-reproducible-workspace/release.json`;
- `docs/source/fnd-1-healthcare-data-foundations-source-record.md`; and
- `docs/curriculum/BUILD-LEDGER.md`.

Then:

1. preserve the accepted Module 01 workspace interface;
2. inspect the pinned Synthea April 2020 CSV archive;
3. lock the exact included source files, sizes, rows, fields, and checksums;
4. define the relational table grains, keys, types, and expected relationships;
5. build the SQLite teaching database deterministically;
6. add a data dictionary and accessible schema description;
7. add supplied FHIR R4 Patient, Encounter, and Observation reading examples;
8. build first SQL extracts and validation checks;
9. write the 21-section Module 02 specification;
10. create the assessment, instructor key, validator, and release record;
11. run from a clean target;
12. update Commons version and build ledger;
13. commit and push Module 02; and
14. keep cohort selection and analytic-table construction in Module 03.
