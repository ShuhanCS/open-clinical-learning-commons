# Clinical data visualization source register

- Register version: `0.1.0`
- Retrieved or verified: 2026-08-26
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
| 01. From healthcare question to display | CMS HCAHPS | Selected communication, discharge-information, overall-rating, completed-survey, and response-rate fields. |
| 02. Categories and comparisons | CMS HCAHPS | Hospital and state comparisons with denominator and footnote fields. |
| 03. Patient distributions | Synthea; Module 04 teaching release | Encounter-level lengths of stay or another continuous care-process measure. |
| 04. Change over time | CMS timely care or CDC WONDER | Multi-period process measure or mortality rate with reporting dates. |
| 05. Relationships | CDC PLACES plus ACS | County estimate, denominator, margin of error, and community context. |
| 06. Uncertainty and benchmarking | ClinicalTrials.gov or CMS | Reported result estimates with uncertainty, or hospital outcome and volume measures. |
| 07. Patient journeys and clinical flow | Synthea | Encounter class, condition, procedure, and next state for an explicitly defined cohort. |
| 08. Clinical networks | ClinicalTrials.gov or Synthea | Sponsor-condition-site relationships or patient-level condition and service links. |
| 09. Composition and hierarchy | CDC WONDER or openFDA | Cause hierarchy or adverse-event terminology with counts and reporting limits. |
| 10. Equity and subgroup comparisons | CDC PLACES plus ACS | Population-health measure, demographic context, estimate uncertainty, and geography. |
| 11. Place and access | CDC PLACES, ACS, and HRSA AHRF | County health measure, population denominator, and workforce ratio. |
| 12. Clinical dashboards | CMS hospitals | Small measure set for one named hospital audience and monitoring decision. |
| 13. Capstone | One approved source above | Versioned learner extract with full provenance record. |

## Module 04 provenance gap

The current emergency-department dataset is deterministic and fully synthetic. Its generator is based on the teaching requirements in the course design, not a patient dataset or a public hospital extract. It is appropriate for a prototype, but it does not yet satisfy the new source-first standard by itself.

Before a teaching release, record one of these resolutions:

- calibrate selected length-of-stay parameters to a named public aggregate source such as CMS Timely and Effective Care, while clearly labeling the assumptions added to create a patient-level distribution; or
- replace the encounter source with an identified Synthea release and publish every transformation used to create the teaching pattern.

The source cannot be used to claim that a real hospital, fast-track program, or boarding intervention produced the synthetic result.
