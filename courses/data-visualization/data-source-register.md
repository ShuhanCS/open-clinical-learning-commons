# Clinical data visualization source register

- Register version: `0.10.0`
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
| CDC NHSN, Weekly Hospital Respiratory Data by Jurisdiction | Weekly hospital capacity, occupancy, respiratory admissions, reporting coverage, time patterns, and cautious process review | Public jurisdiction aggregates across reporting hospitals. Reporting coverage and hospital mix change, so the data do not represent one hospital's stable internal process. | https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi |
| U.S. Census Bureau, ACS 5-year data and Summary File | Population denominators, demographic context, insurance coverage, disability, income, and housing | Public estimates with margins of error. The current API requires a key; the table-based Summary File is public without one. Use the estimate and margin of error together. | https://www.census.gov/programs-surveys/acs/data/summary-file.html |
| CDC WONDER | Mortality counts, crude and age-adjusted rates, confidence intervals, cause, place, population, and time | Public query system. Respect suppression and unreliable-rate flags. Death-certificate data describe recorded underlying causes, not every condition involved in care. | https://wonder.cdc.gov/datasets.html |
| National Library of Medicine, ClinicalTrials.gov API | Trial portfolios, enrollment, status, geography, sponsors, conditions, interventions, and reported results | Public records supplied by study sponsors and investigators. Registration does not establish intervention effectiveness or study quality. | https://clinicaltrials.gov/data-api |
| Synthea | Longitudinal synthetic patients, encounters, diagnoses, procedures, medications, and observations | Open synthetic records with no real patients. Suitable for patient journeys, Sankey diagrams, cohort funnels, and networks. Clinical realism depends on the generator modules and version. | https://synthetichealth.github.io/synthea/ |
| U.S. Food and Drug Administration, openFDA drug adverse event API | Adverse-event reporting patterns, hierarchy, time, network, and data-quality exercises | FAERS reports can contain duplicates, missing fields, and reporting bias. A report does not prove that a product caused an event. | https://open.fda.gov/apis/drug/event/ |
| Health Resources and Services Administration, primary-care Health Professional Shortage Areas | Current and historical shortage designations, component scope, scores, population context, and rural status | Public HRSA data-mart fields. A component score is not a county workforce rate, and a component designation is not automatically a whole-county designation. | https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv |
| Health Resources and Services Administration, Area Health Resources Files | County and state workforce context | Downloadable, but the included 2024-2025 technical documentation restricts reproduction and identifies copyrighted AMA, AHA, and ADA fields. Do not redistribute AHRF extracts without resolving the field-specific rights. | https://data.hrsa.gov/data/download?data=AHRF |

## Module source map

| Module | Required source | Planned extract |
|---|---|---|
| 01. Encoding and the grammar of graphics | CMS HCAHPS | Released extract: all 65 Massachusetts `H_RECMND_DY` rows from the CMS 2026-08-13 release, including 9 unavailable results and footnotes. |
| 02. Perception and visual accuracy | CMS HCAHPS | Released 10-trial task table using the Module 01 HCAHPS extract, with two trials each for dot, bar, table, pie, and bubble displays. |
| 03. Chart selection in practice | CMS hospitals | Released 10-case decision table plus two HCAHPS charts and one exact-value table using the Module 01 extract. |
| 04. Distributions versus summaries | CMS Timely and Effective Care plus calibrated synthetic encounters | Released all-national OP_18b hospital extract and a source-bounded synthetic encounter distribution. |
| 05. Rates, denominators, and adjustment | CDC PLACES, ACS, and Census TIGERweb | Released national diabetes and adult-population extracts plus a 100-county North Carolina decision table and generalized boundary file. |
| 06. Uncertainty, variation, and small numbers | CMS Unplanned Hospital Visits and Footnote Crosswalk | Released all-national heart failure readmission estimate rows plus the complete national summary, official footnotes, and a 65-hospital Massachusetts decision table. |
| 07. Color and accessible visual communication | Reused Module 06 CMS Unplanned Hospital Visits release plus W3C and CDC accessibility guidance | Released 65-row source-preserving accessibility table with redundant cues, contrast calculations, grayscale output, exact table, and text alternatives. |
| 08. Time and process variation | CDC NHSN weekly hospital respiratory data by jurisdiction | Released 6,208-row jurisdiction table and 94-week Massachusetts teaching sequence with capacity, occupancy, respiratory admissions, reporting coverage, and source-season availability. |
| 09. Comparison and small multiples | CDC PLACES county data 2024 release | Released five-measure national county table and a 100-county North Carolina comparison table with paired crude and age-adjusted estimates, uncertainty, national references, and transparent profile order. |
| 10. Maps, geography, and place | CDC PLACES, direct HRSA primary-care HPSAs, and Census generalized county boundaries | Released 100-county place-access table, 1,546-row HPSA source selection, and 7,121-point boundary release for a map-versus-non-map decision. |
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

### DA-730 rates-denominators-adjustment release

- Module: DA-730 Module 05, Rates, denominators, and adjustment
- CDC source: PLACES county data 2024 release, dataset `fu4u-a9bh`, measure `DIABETES`, measure year 2022
- CDC source page: https://data.cdc.gov/d/fu4u-a9bh
- CDC extract: `courses/data-visualization/modules/05-rates-denominators-adjustment/data/places_diabetes_county_2024.csv`
- CDC rows: 6,290, including both crude and age-adjusted prevalence for all 3,144 counties and the two source national-summary rows
- CDC extract SHA-256: `764b46c63508a5a6a2510ee2766866ab91abdeeaf7d633f50ae70a3aff561de6`
- ACS source: 2020-2024 ACS 5-year Detailed Table B01001, Sex by Age
- ACS source file: https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b01001.dat
- ACS extract: `courses/data-visualization/modules/05-rates-denominators-adjustment/data/acs_adult_population_county_2024.csv`
- ACS rows: all 3,222 county geographies with derived adult and age-65-plus population context and margin status
- ACS extract SHA-256: `1efa6d51591bf2941c22d09a6e8a86f70f6405f753bf59b60a0a6e99d45b24a2`
- Boundary source: Census Generalized ACS 2024 State and County service, Counties 5M
- Boundary service: https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer
- Boundary extract: 7,121 ordered coordinate rows across 100 North Carolina counties and 104 polygon parts
- Teaching table: `courses/data-visualization/modules/05-rates-denominators-adjustment/data/nc_diabetes_rates_2024.csv`
- Teaching table SHA-256: `1528b204830966dff88e00f57fc4f77b8dcf5db135daa122e8aff3679fdf32c7`
- Source record: `courses/data-visualization/modules/05-rates-denominators-adjustment/source-record.yml`
- Validation: 32 of 32 checks pass

The modeled adult count is rounded crude prevalence multiplied by the matching PLACES adult population. It is not an observed case count. The ACS population is separate context and is not substituted into that calculation. The 10,000-adult warning is a declared teaching rule, not a CDC suppression rule.

### DA-730 uncertainty-variation-small-numbers release

- Module: DA-730 Module 06, Uncertainty, variation, and small numbers
- CMS hospital source: Unplanned Hospital Visits - Hospital, dataset `632h-zaca`, measure `READM_30_HF`, release 2026-08-13
- CMS hospital source page: https://data.cms.gov/provider-data/dataset/632h-zaca
- Original hospital file: 67,060 rows, 19,048,784 bytes, SHA-256 `a3e64029ea6daea1f7de163e5b5054b918d0c8be986fccfc47c7a8d5b29a6d1d`
- Selected hospital extract: `courses/data-visualization/modules/06-uncertainty-variation-small-numbers/data/cms_hf_readmission_hospitals_2026.csv`
- Selected rows: all 4,790 national `READM_30_HF` hospital rows, including 3,253 reported and 1,537 too-few or unavailable results
- Selected hospital SHA-256: `e69fcee79711ef8496cb32205b492e6e3a788c4e63009bc1330a84216b0edeba`
- CMS national source: https://data.cms.gov/provider-data/dataset/cvcs-xecj
- National release: all 14 measure rows; selected national rate 21.3; SHA-256 `408c2d3f27a93c9294f9399e6a0deabfe70076685a5e06f285daf857e92161f9`
- CMS footnote source: https://data.cms.gov/provider-data/dataset/y9us-9xdf
- Footnote release: all 32 official definitions; SHA-256 `94d22120d0efcb0d6f98f3470bce8a7cffb3cf657eb95179556198c4ebae84e7`
- Teaching table: `courses/data-visualization/modules/06-uncertainty-variation-small-numbers/data/ma_hf_readmission_uncertainty_2026.csv`
- Massachusetts rows: 65, including 53 reported, 2 too few, and 10 not available
- Teaching table SHA-256: `33e6284a1064bb12600903526e4e65c009f875d9e6f6a3f25783d3a9a4b00727`
- Source record: `courses/data-visualization/modules/06-uncertainty-variation-small-numbers/source-record.yml`
- Validation: 42 of 42 checks pass

The source score is risk standardized. The release labels its endpoints Lower Estimate and Higher Estimate, so the module does not invent a confidence level. CMS comparison categories use the national rate and do not test every hospital pair. Suppressed values remain blank.

### DA-730 color-accessible-communication release

- Module: DA-730 Module 07, Color and accessible visual communication
- Upstream clinical release: Module 06 Massachusetts `READM_30_HF` table, 65 rows
- CMS source page: https://data.cms.gov/provider-data/dataset/632h-zaca
- Accessibility standards: https://www.w3.org/TR/WCAG22/
- Use of color guidance: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
- Non-text contrast guidance: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
- Complex images guidance: https://www.w3.org/WAI/tutorials/images/complex/
- CDC COVE accessibility guidance: https://www.cdc.gov/cove/about/section-508-accessibility.html
- Teaching table: `courses/data-visualization/modules/07-color-accessible-communication/data/accessibility_hf_readmission_2026.csv`
- Teaching rows: 65 source-preserving hospital rows with 11 accessibility fields
- Teaching table SHA-256: `b58168d9002a3e489213b0fafde1eca76f5b1a426c71ea3d61551671d76a49c2`
- Source record: `courses/data-visualization/modules/07-color-accessible-communication/source-record.yml`
- Validation: 66 of 66 checks pass

The module defines five reusable status cues with direct text, symbols, shapes, line types, and colors. All defined foregrounds exceed 4.5:1 contrast against white. A calculated ratio does not certify the complete chart or delivery context, so learners also test grayscale, print, a smaller view, text alternatives, and the exact-value table.

### DA-730 time-process-variation release

- Module: DA-730 Module 08, Time and process variation
- CDC source: National Healthcare Safety Network, Weekly Hospital Respiratory Data, HRD Metrics by Jurisdiction, dataset `rhwp-grxi`
- Source page: https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi
- Selected period: 2024-11-09 through 2026-08-22
- Raw selected-query rows: 6,208 across 67 jurisdictions
- Raw selected-query SHA-256: `d261cbc441069a41ef1b14347af90dfd6c59e402d7854a5e86288a4f0e9d4dc6`
- All-jurisdiction release: `courses/data-visualization/modules/08-time-process-variation/data/nhsn_hospital_capacity_jurisdiction_2024_2026.csv`
- All-jurisdiction SHA-256: `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1`
- Massachusetts teaching release: `courses/data-visualization/modules/08-time-process-variation/data/ma_hospital_capacity_time_2024_2026.csv`
- Massachusetts rows: 94 consecutive weeks and 21 fields
- Massachusetts SHA-256: `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616`
- Source record: `courses/data-visualization/modules/08-time-process-variation/source-record.yml`
- Validation: 47 of 47 checks pass

The all-jurisdiction release preserves 120 rows with unavailable core metrics, six published count-above-bed anomalies, and one published coverage value above 100 percent. The Massachusetts sequence has complete core metrics, but reporting coverage and the reporting hospital mix still change. Exploratory process limits identify dates for review and do not establish special cause.

### DA-730 comparison-small-multiples release

- Module: DA-730 Module 09, Comparison and small multiples
- CDC source: PLACES county data 2024 release, dataset `fu4u-a9bh`
- Source page: https://data.cdc.gov/d/fu4u-a9bh
- Methodology: https://www.cdc.gov/places/methodology/index.html
- Selected measure year: 2022
- Selected measures: current smoking, diagnosed diabetes, fair or poor self-rated health, no leisure-time physical activity, and obesity
- Raw selected-query rows: 31,450
- Raw selected-query SHA-256: `897064d10703b870afe6d55f4cf0bc7e08d1c91f5d3490584952894df3f6de4b`
- All-selected release: `courses/data-visualization/modules/09-comparison-small-multiples/data/places_county_comparison_2024.csv`
- All-selected rows: 31,450 across 3,144 counties plus 10 national summary rows
- All-selected SHA-256: `2af5ce99fc7d66a18e95451084afc397e0f7392e9f1a2b5476377fd8811658d2`
- North Carolina teaching release: `courses/data-visualization/modules/09-comparison-small-multiples/data/nc_county_health_profiles_2024.csv`
- North Carolina rows: 500, representing 100 counties by five measures with paired crude and age-adjusted estimates
- North Carolina SHA-256: `33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9`
- Source record: `courses/data-visualization/modules/09-comparison-small-multiples/source-record.yml`
- Validation: 58 of 58 checks pass

The values are model-based small-area estimates, not observed county diagnoses or direct county survey estimates. The reference profile count gives every measure equal weight and is only a transparent teaching screen. It is not a validated equity, risk, readiness, clinical, or funding score. Age-adjusted values support comparison; crude values retain population-burden context.

### DA-730 maps-geography-place release

- Module: DA-730 Module 10, Maps, geography, and place
- CDC source: PLACES county data 2024 release, measure `GHLTH`, measure year 2022
- CDC source page: https://data.cdc.gov/d/fu4u-a9bh
- HRSA source: Primary Care Health Professional Shortage Areas
- HRSA source URL: https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv
- HRSA metadata URL: https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX
- HRSA full source: 79,358 rows, 48,280,174 bytes, SHA-256 `4552ebf09bc5a40d79d71df8ea84aea165de2205953615e03571ad84f1d6b132`
- Selected HPSA release: `courses/data-visualization/modules/10-maps-geography-place/data/hpsa_primary_care_nc_2026_08_29.csv`
- Selected HPSA rows: 1,546 across 100 counties
- Selected HPSA SHA-256: `061fe5e18bc9cd58bd89256c686ddefbce6d77972c1139b1b339497f2eab5445`
- Teaching table: `courses/data-visualization/modules/10-maps-geography-place/data/nc_place_access_2026.csv`
- Teaching rows: 100 counties
- Teaching SHA-256: `90a575f03bc94cc0eb336d263e3f9d8afe09cf68ddb95476bf1836c0574f9a07`
- Census boundaries: 7,121 points and 104 polygon parts, SHA-256 `6eb085f49b400d4ecf6f88646f51dd01fdd4154533262e66ade02b1d1d8f666f`
- Source record: `courses/data-visualization/modules/10-maps-geography-place/source-record.yml`
- Validation: 60 of 60 checks pass

The reference case uses the highest current primary-care HPSA component score touching each county. That value is not a county workforce rate. Score 20 and the twelve-county review limit are declared teaching rules, not official thresholds or validated allocation rules. The map supports regional discussion; the ordered comparison and exact table support rank, uncertainty, and value review.

The 2024-2025 AHRF archives were inspected but are not redistributed. The included technical documentation contains more restrictive reuse language than the catalog page and identifies copyrighted source fields. The module uses the direct public HRSA HPSA data mart instead.
