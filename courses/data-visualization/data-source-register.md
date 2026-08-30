# Clinical data visualization source register

- Register version: `0.3.0`
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
| 03. Chart selection in practice | CMS hospitals | Planned multi-measure hospital table with result, response-rate, survey-volume, and source fields. |
| 04. Distributions versus summaries | Current synthetic teaching release; public calibration pending | Encounter-level emergency-department length of stay with known aggregate and subgroup patterns. |
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

## Module 04 provenance gap

The current emergency-department dataset is deterministic and fully synthetic. Its generator is based on the teaching requirements in the course design, not a patient dataset or a public hospital extract. It is appropriate for a prototype, but it does not yet satisfy the new source-first standard by itself.

Before a teaching release, record one of these resolutions:

- calibrate selected length-of-stay parameters to a named public aggregate source such as CMS Timely and Effective Care, while clearly labeling the assumptions added to create a patient-level distribution; or
- replace the encounter source with an identified Synthea release and publish every transformation used to create the teaching pattern.

The source cannot be used to claim that a real hospital, fast-track program, or boarding intervention produced the synthetic result.
