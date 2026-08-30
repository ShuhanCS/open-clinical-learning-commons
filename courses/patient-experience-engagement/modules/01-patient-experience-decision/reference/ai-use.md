# AI-use record

- Tool and model: `OpenAI Codex`
- Date: `2026-08-30`
- Purpose: `draft and test the APP-2 Module 01 public-source profile and decision package`
- Prompt or task: `build a runnable patient-experience decision module from the supplied curriculum and complete CMS HCAHPS hospital source`
- Data classes shared: `public hospital-level CMS data and public curriculum text; no patient-level, protected, identifiable, credential, or restricted data`
- Files affected: `Module 01 specifications, source records, profile code, validators, templates, and reference records`
- Output used, modified, or rejected: `code and prose were retained after exact source profiling, deterministic comparison, claim-boundary review, and human-directed scope decisions`
- Material claim: `the source contains 325,720 rows, 4,790 facilities, 68 measure IDs, 3,949 numeric response-rate facilities, and no patient-level response rows`
- Independent verification: `SHA-256 checks, streaming CSV counts, one-row-per-facility-and-measure checks, committed-profile comparison, and mutation rejection`
- Correction or retained action: `retained the full compressed public source and prohibited hospital ranking, patient-level inference, causal claims, and implementation`
- Human owner: `Shuhan He`
- Accountability statement: `The human course owner remains accountable for curriculum approval, patient-partner terms, clinical claims, and release decisions.`
