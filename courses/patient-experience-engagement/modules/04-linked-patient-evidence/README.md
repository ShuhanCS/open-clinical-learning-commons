# APP-2 Module 04: Linked patient evidence

This 16.5-hour module asks whether patient-reported, access, communication, digital-service, and service-use evidence can be linked without changing the meaning of any denominator.

You will work with the full 2024 MEPS HC-256 person file and four event files. The build links 174,231 official event rows to the person source, then releases a 1,255-person teaching target with 28,455 linked events. It also carries forward the accepted Module 3 synthetic response evidence without presenting it as real patient testimony.

The main submission is a 25-point response and linked-evidence analysis. You must reconcile person totals with event rows, register every denominator, estimate access and communication measures with the survey design, distinguish telehealth use from patient preference, and write a bounded interpretation.

## Start here

1. Read `data-spec.md` and `linkage-contract.json`.
2. Run `python build_linked_evidence.py --verify-committed`.
3. Build a learner workspace with `python build_workspace.py --target <new-directory>`.
4. Complete every file in that workspace.
5. Run `python validate_workspace.py <workspace> --learner` while working.
6. Remove every `REPLACE` marker and run `python validate_workspace.py <workspace>` before submission.

## Official sources

- https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256
- https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254D
- https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254E
- https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254F
- https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254G

No artifact authorizes clinical action, patient targeting, hospital ranking, a causal claim, or machine learning. Machine learning remains in Module 6.
