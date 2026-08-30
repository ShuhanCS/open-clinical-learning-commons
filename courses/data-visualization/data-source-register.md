# Clinical data visualization source register

- Register version: `0.5.0`
- Retrieved or verified: 2026-08-29
- Scope: public course development and assignments

## Required source record

Every assignment dataset must record:

1. publisher and dataset title;
2. complete source URL;
3. retrieval date and release or coverage dates;
4. license, public-domain status, or terms of use;
5. variables and rows used;
6. filters, joins, recoding, aggregation, and suppression;
7. missingness, uncertainty, population, and interpretation limits;
8. checksum and build script for any committed extract.

Public access does not automatically permit every reuse. Keep the source terms with each imported table.

## Approved starting sources

| Publisher and dataset | Clinical use | Access and limits | Full URL |
|---|---|---|---|
| Centers for Medicare & Medicaid Services, Hospitals topic | Hospital quality, readmissions, infections, patient experience, timely care, and general hospital information | Public government data. Measure definitions, reporting periods, suppression, and risk adjustment vary by file. | https://data.cms.gov/provider-data/topics/hospitals |
| CMS, Timely and Effective Care - Hospital | Emergency department and hospital process comparisons, time trends, benchmarking, and dashboards | Public aggregate measures. Do not infer patient-level distributions from hospital-level summaries. | https://data.cms.gov/provider-data/dataset/yv7e-xc69 |
| CMS, Patient survey (HCAHPS) - Hospital | Patient-experience comparisons, small multiples, uncertainty, maps, and dashboards | Public hospital survey results. Keep completed-survey counts, response rates, reporting dates, and footnotes with the analysis. | https://data.cms.gov/provider-data/dataset/dgck-syfz |
| CDC, PLACES county data 2024 release | Population-health outcomes, preventive services, health-related social needs, equity comparisons, and maps | Model-based small-area estimates. CDC cautions against using them to evaluate local interventions. | https://data.cdc.gov/d/fu4u-a9bh |
| U.S. Census Bureau, ACS 5-year API | Population denominators, demographic context, insurance coverage, disability, income, and housing | Public estimates with margins of error. The current API requires a key. Use the estimate and margin of error together. | https://www.census.gov/data/developers/data-sets/acs-5year.html |
| CDC WONDER | Mortality counts, crude and age-adjusted rates, confidence intervals, cause, place, population, and time | Public query system. Respect suppression and unreliable-rate flags. Death-certificate data describe recorded underlying causes, not every condition involved in care. | https://wonder.cdc.gov/datasets.html |
| National Library of Medicine, ClinicalTrials.gov API | Trial portfolios, enrollment, status, geography, sponsors, conditions, interventions, and reported results | Public records supplied by study sponsors and investigators. Registration does not establish intervention effectiveness or study quality. | https://clinicaltrials.gov/data-api |
| Synthea | Longitudinal synthetic patients, encounters, diagnoses, procedures, medications, and observations | Open synthetic records with no real patients. Suitable for patient journeys, Sankey diagrams, cohort funnels, and networks. Clinical realism depends on the generator modules and version. | https://synthetichealth.github.io/synthea/ |
| U.S. Food and Drug Administration, openFDA drug adverse event API | Adverse-event reporting patterns, hierarchy, time, network, and data-quality exercises | FAERS reports can contain duplicates, missing fields, and reporting bias. A report does not prove that a product caused an event. | https://open.fda.gov/apis/drug/event/ |
| Health Resources and Services Administration, Area Health Resources Files | County and state health-workforce counts and provider-to-population ratios | Public workforce data assembled from multiple sources. Keep the year and source definition for each variable. | https://data.hrsa.gov/data/download |

## Module source map

| Module | Required source | Planned extract |
|---|---|---|
| 01. Encoding and the grammar of graphics | CMS HCAHPS | Released extract: all 65 Massachusetts `H_RECMND_DY` rows from the CMS 2026-08-13 release, including 9 unavailable results and footnotes. |
| 02. Perception and visual accuracy | CMS HCAHPS | Released 10-trial task table using the Module 01 HCAHPS extract, with two trials each for dot, bar, table, pie, and bubble displays. |
| 03. Chart selection in practice | CMS hospitals | Released 10-case decision table plus two HCAHPS charts and one exact-value table using the Module 01 extract. |
| 04. Distributions versus summaries | CMS Timely and Effective Care plus calibrated synthetic encounters | Released all-national OP_18b hospital extract and a source-bounded synthetic encounter distribution. |
| 05. Rates, denominators, and adjustment | CDC PLACES plus ACS | Planned county estimate, population context, denominator, margin of error, and adjustment fields. |
| 06. Uncertainty, variation, and small numbers | ClinicalTrials.gov or CMS | Planned estimates with sample size and uncertainty, including null and small-number cases. |
| 07. Color and accessible visual communication | CMS or another released module dataset | Planned clinical quality display variants for screen, print, grayscale, and text alternatives. |
| 08. Time and process variation | CMS timely care or CDC WONDER | Planned multi-period process measure or mortality rate with reporting dates. |
| 09. Comparison and small multiples | CMS, CDC PLACES, or module-approved source | Planned repeated measure across hospitals, counties, or patient groups. |
| 10. Maps, geography, and place | CDC PLACES, ACS, and HRSA AHRF | Planned county health measure, population denominator, geography, and workforce ratio. |
| 11. Flow, networks, composition, and hierarchy | Synthea, ClinicalTrials.gov, or openFDA | Planned patient transitions, research relationships, or reporting hierarchy with explicit grain. |
| 12. Dashboards and multi-view composition | CMS hospitals | Planned small hospital monitoring set for one named audience and decision. |
| 13. Audience, annotation, narrative, and capstone | One approved source above | Versioned learner extract with full provenance record. |

## Released source packages

### CMS HCAHPS Massachusetts recommendation extract

- Module: DA-730 Module 01, Encoding and the grammar of graphics
- CMS release: 2026-08-13
- Coverage: 2024-10-01 through 2025-09-30
- Extract: `courses/data-visualization/modules/01-encoding-grammar/data/hcahps_ma_recommend_2026.csv`
- Source record: `courses/data-visualization/modules/01-encoding-grammar/source-record.yml`
- Build: `courses/data-visualization/modules/01-encoding-grammar/build_hcahps.R`
- Validation: 15 of 15 checks pass
- Original CMS file: `HCAHPS-Hospital.csv`, 105,461,119 bytes, SHA-256 `b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc`
- Teaching extract SHA-256: `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74`

### DA-730 perception-task release

- Module: DA-730 Module 02, Perception and visual accuracy
- Upstream extract: Module 01 CMS HCAHPS Massachusetts recommendation release
- Task file: `courses/data-visualization/modules/02-perception-accuracy/data/perception_tasks_2026.csv`
- Source record: `courses/data-visualization/modules/02-perception-accuracy/source-record.yml`
- Build: `courses/data-visualization/modules/02-perception-accuracy/build_perception_tasks.R`
- Validation: 12 of 12 checks pass
- Stimuli: 10 matched trials plus 2 critique charts
- Scoring self-check: 100% correct with zero gap error for a perfect response file
- Task SHA-256: `b792637411a00c67baa30d70688e5a9b8353cee8a2758251419e84c0c4c1cbe6`

### DA-730 chart-selection release

- Module: DA-730 Module 03, Chart selection in practice
- Upstream extract: Module 01 CMS HCAHPS Massachusetts recommendation release
- Case file: `courses/data-visualization/modules/03-chart-selection/data/selection_cases_2026.csv`
- Source record: `courses/data-visualization/modules/03-chart-selection/source-record.yml`
- Build: `courses/data-visualization/modules/03-chart-selection/build_selection_cases.R`
- Validation: 13 of 13 checks pass
- Cases: 10 question-to-display decisions covering comparison, lookup, relationship, distribution, time, composition, flow, geography, monitoring, and evidence verification
- Runnable outputs: two HCAHPS charts, one exact lookup table, two matrices, and one intentionally flawed dashboard
- Case SHA-256: `0f295bd9bf94e9f5800e4fdaebea303d8cc0b28ccd3afcb01603d8e1c0a2eff8`

### DA-730 distributions-versus-summaries release

- Module: DA-730 Module 04, Distributions versus summaries
- Public source: CMS Timely and Effective Care - Hospital, `OP_18b`, release 2026-08-13
- Source page: https://data.cms.gov/provider-data/dataset/yv7e-xc69
- Original CMS file: 138,084 rows, 34,150,899 bytes, SHA-256 `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516`
- CMS extract: `courses/data-visualization/modules/04-distributions-vs-summaries/data/cms_ed_op18b_2026.csv`
- CMS rows: all 4,658 national OP_18b hospital rows, including 4,081 reported and 577 unavailable values
- CMS extract SHA-256: `c9603109d4ea251b8096a655c27ad42cd6313bdb1309999bee3eb37ce79ec67d`
- Synthetic release: `courses/data-visualization/modules/04-distributions-vs-summaries/data/ed_los_2026.csv`
- Synthetic rows: 8,392 encounters; data version 0.2.0; variant `real`; seed 730
- Synthetic SHA-256: `27c1c0feed8beb4ab0ac6dc77eaa3d1ed95c07b89f52f4881c25954ba43fbc55`
- Source record: `courses/data-visualization/modules/04-distributions-vs-summaries/source-record.yml`
- Validation: real 26 of 26, null 23 of 23, and trivial 23 of 23 checks pass

The median of 4,081 reported CMS hospital values is 148 minutes. It anchors only the discharged pathway center. CMS does not provide the generated patient-level distribution, monthly trend, disposition mix, boarding process, tail, acuity, age, or intervention effect. Those remain explicit instructional assumptions and cannot support a real-hospital claim.
