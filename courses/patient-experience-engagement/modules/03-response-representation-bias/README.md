# APP-2 Module 03: Response, representation, and survey bias

This runnable module uses the full public MEPS HC-256 person file and a deterministic synthetic survey-response layer to teach population, frame, response, item missingness, subgroup representation, and one bounded weighting adjustment.

The MEPS fields and `PERWT24F` values are public federal survey data. Q21, Q22, Q23, invitation, response, mode, and item-missingness fields are synthetic. None of the generated rates is a real patient, hospital, HCAHPS, equity, access, or clinical result.

## Build the evidence

```powershell
python build_response_evidence.py --self-check
```

## Build a learner workspace

```powershell
python build_workspace.py --target app2-module03-workspace
python app2-module03-workspace/validate_workspace.py app2-module03-workspace --learner
```

Use `--reference` for the completed faculty workspace. Builders refuse to overwrite an existing target.

Official landing page: https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256

Repository: https://github.com/ShuhanCS/open-clinical-learning-commons
