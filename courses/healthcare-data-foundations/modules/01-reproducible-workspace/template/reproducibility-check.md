# Independent reproduction check

- Original repository URL: [REPLACE: full URL]
- Tagged commit tested: [REPLACE: full commit hash]
- Reproducer: [REPLACE: name or approved identifier]
- Reproduction date: [REPLACE: YYYY-MM-DD]
- Clean target location: [REPLACE: state that a new directory was used; omit personal absolute paths]
- Reused original `.venv`: no

## Commands run

[REPLACE: exact clone, environment, install, Python, notebook, and R commands. Remove credentials and personal absolute paths.]

## Expected and observed results

| Check | Expected | Observed | Status |
|---|---|---|---|
| Python and SQLite | `WORKSPACE_SMOKE_TEST_PASS rows=3 total=15` | [REPLACE] | [REPLACE: pass/fail] |
| pandas notebook | 3 rows, unique IDs, total 15, stored pass marker | [REPLACE] | [REPLACE: pass/fail] |
| supplied R script | `WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15` | [REPLACE] | [REPLACE: pass/fail] |
| required files | all present | [REPLACE] | [REPLACE: pass/fail] |

## Differences and failures

[REPLACE: record every difference, warning, retry, and failure. If none occurred, state "No differences or failures observed." Do not erase failed attempts.]

## Reproduction decision

- Decision: [REPLACE: reproduced / reproduced with conditions / not reproduced]
- Conditions or next action: [REPLACE: exact condition, owner, and date, or "None"]
