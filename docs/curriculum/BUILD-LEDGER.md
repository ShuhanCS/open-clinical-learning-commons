# Curriculum build ledger

- Current release: 0.36.0
- Last updated: 2026-08-30
- Active phase: FND-1 module build
- Last completed unit: FND-1 Module 07, Reproducible handoff and AI audit
- Next unit: FND-1 final checkpoint, Reproducible healthcare data toolkit

## Confirmed decisions

- FND-1 and FND-2 are separate straight-through technical foundation courses.
- APP-1 through APP-7 revisit foundations through different domain methods and decisions.
- Applied courses use seven distinct modules. Module 6 contains the week-6 application checkpoint and an embedded half-week machine-learning extension.
- Module 7 is the final clinician-led leadership block.
- Every applied course has cumulative checkpoints at instructional weeks 3 and 6 and on the official last day of the half-term.
- Three-credit courses retain 112.5 total learner hours.
- CAP-0 remains zero credits unless approved program documents change it.
- DA-730 remains separate and moves from a Tableau-centered source course to a concept-first, software-flexible visualization course.
- Public clinical sources, open datasets, and documented synthetic teaching data are core course materials.
- Every module requires exact learner, instructor, data, assessment, rubric, accessibility, and release deliverables.
- FND-1 preserves the source assessment weights through cumulative checkpoints: 40 percent at Week 3, 25 percent at Week 6, and 35 percent on the official last day.

## Source status

- `Curriculum-30-Credits-2026-08-29.zip` inspected: 11 DOCX course files.
- `OneDrive_2026-08-29 (1).zip` inspected: same 11 DOCX course files and file sizes.
- The FND-1 source file is byte-for-byte identical in both archives: 24,148 bytes and SHA-256 `70a78f38824066770b724aca907211ce6df94b3232cbeb8dbfa8389a24556692`.
- The FND-1 specification defines seven straight-through technical modules totaling 112.5 hours, three cumulative checkpoints, and a final accept/condition/revise/refer decision owned by a health-system analytics engineering lead.
- FND-1 uses the pinned Synthea April 2020 CSV archive as its continuing synthetic source. The database, deterministic defect layer, cohort, and learner release are separate versioned layers.
- MGH Institute 2026-2027 academic calendar checked: offerings are labeled half-terms and span 49 to 52 elapsed days.
- Master architecture: `docs/specs/2026-08-29-curriculum-master-architecture-spec.md`.
- DA-730 Module 01 uses the CMS HCAHPS 2026-08-13 release, filtered to all 65 Massachusetts `H_RECMND_DY` rows. The file contains 56 reported and 9 unavailable results for 2024-10-01 through 2025-09-30.
- Module 01 teaching extract SHA-256: `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74`.
- Module 01 build, 15-check validator, tiered lab, two critique charts, assessment, instructor key, and release record are complete as a runnable release candidate.
- DA-730 Module 02 reuses the Module 01 HCAHPS extract through a 10-row perception-task release with two dot, bar, table, pie, and bubble trials.
- Module 02 task SHA-256: `b792637411a00c67baa30d70688e5a9b8353cee8a2758251419e84c0c4c1cbe6`.
- Module 02 build, 12-check validator, 10 stimuli, scorer, two critique charts, assessment, instructor key, and release record are complete as a runnable release candidate.
- DA-730 Module 03 reuses the Module 01 HCAHPS extract and adds a 10-case chart-selection table covering comparison, lookup, relationship, distribution, time, composition, flow, geography, monitoring, and evidence verification.
- Module 03 case SHA-256: `0f295bd9bf94e9f5800e4fdaebea303d8cc0b28ccd3afcb01603d8e1c0a2eff8`.
- Module 03 build, 13-check validator, two HCAHPS charts, one exact-value table, two selection matrices, one flawed-dashboard critique, assessment, instructor key, and release record are complete as a runnable release candidate.
- DA-730 Module 04 preserves every national CMS OP_18b row from the 2026-08-13 Timely and Effective Care release: 4,658 hospital rows, including 4,081 reported and 577 unavailable values. The reported hospital median is 148 minutes.
- Module 04 CMS extract SHA-256: `c9603109d4ea251b8096a655c27ad42cd6313bdb1309999bee3eb37ce79ec67d`.
- Module 04 synthetic encounter release 0.2.0 contains 8,392 rows and SHA-256 `27c1c0feed8beb4ab0ac6dc77eaa3d1ed95c07b89f52f4881c25954ba43fbc55`.
- Module 04 real, null, and trivial variants pass 26, 23, and 23 checks. The lab creates four figures and a monthly table; the critique creates three intentionally flawed figures.
- DA-730 Module 05 preserves 6,290 CDC PLACES `DIABETES` rows, including crude and age-adjusted prevalence for all 3,144 counties and the source national summary.
- Module 05 CDC extract SHA-256: `764b46c63508a5a6a2510ee2766866ab91abdeeaf7d633f50ae70a3aff561de6`.
- Module 05 also preserves all 3,222 ACS county rows derived from B01001 and 100 generalized North Carolina Census county features.
- Module 05 teaching table contains 100 North Carolina counties and SHA-256 `1528b204830966dff88e00f57fc4f77b8dcf5db135daa122e8aff3679fdf32c7`.
- Module 05 passes 32 data checks. Its lab creates four figures and a decision table; its critique creates two deliberately flawed figures.
- In the pinned release, the top 12 modeled-count and top 12 age-adjusted-prevalence lists have zero counties in common. The largest count-to-adjusted rank change is 93 places.
- DA-730 Module 06 validates the complete 67,060-row CMS Unplanned Hospital Visits hospital download before preserving all 4,790 `READM_30_HF` rows, all 14 national summary rows, and all 32 official footnotes.
- Module 06 national hospital extract SHA-256: `e69fcee79711ef8496cb32205b492e6e3a788c4e63009bc1330a84216b0edeba`.
- Module 06 Massachusetts teaching table contains 65 hospital rows and SHA-256 `33e6284a1064bb12600903526e4e65c009f875d9e6f6a3f25783d3a9a4b00727`.
- Module 06 passes 42 data checks. Its lab creates four figures and a decision table; its critique creates two deliberately flawed figures.
- The Massachusetts case has 53 reported estimates, 52 CMS-classified no different from the national rate, 1 worse, 2 too few, and 10 not available. Only 1 of the ten highest point estimates is source-classified worse.
- All 1,378 displayed Massachusetts interval pairs overlap descriptively. The module states that this is not a pairwise hypothesis test and does not prove equivalence.
- DA-730 Checkpoint 1 maps Modules 03 through 06 to exact comparison, distribution, rate, and uncertainty figure names while carrying Module 01 encoding choices and Module 02 perception evidence into the selection matrix.
- The checkpoint package assembles four figures and four editable R files from the released module data, supplies four complete source records and six writing templates, and validates the completed folder contract with a Python standard-library check.
- DA-730 Module 07 reuses all 65 Module 06 Massachusetts rows and verifies that every source field used in the case remains unchanged.
- Module 07 teaching table SHA-256: `b58168d9002a3e489213b0fafde1eca76f5b1a426c71ea3d61551671d76a49c2`.
- Module 07 passes 66 data checks. Its lab creates four figures, one 65-row exact table, and one short and long text alternative; its critique creates a red-green color-only chart and a low-contrast heatmap.
- Five status cues use direct text, symbols, shapes, line types, and foreground colors. Every defined foreground exceeds 4.5:1 contrast on white, with a range of 5.54:1 to 18.88:1.
- DA-730 Module 08 preserves 6,208 CDC NHSN jurisdiction-week rows across 67 jurisdictions for 2024-11-09 through 2026-08-22.
- Module 08 all-jurisdiction SHA-256: `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1`.
- The Massachusetts teaching release contains 94 consecutive weeks and SHA-256 `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616`.
- Module 08 passes 47 data checks. Its lab creates five figures, one 94-row exact table, and one short and long text alternative; its critique creates an arbitrary dual-axis chart, a smoothed-only chart, and a chart with unsupported control limits.
- The reference individuals chart declares the first 26 weeks as an exploratory baseline. Its center is 85.23 percent, lower limit is 80.72 percent, and upper limit is 89.75 percent. The module does not convert outside-limit points into formal special-cause claims because reporting coverage, seasonality, and aggregate mix weaken the process assumptions.
- The source release preserves 120 jurisdiction-weeks with unavailable core metrics, six count-above-bed anomalies, and one coverage value above 100 percent instead of silently correcting them.
- DA-730 Module 09 preserves 31,450 CDC PLACES rows covering five 2022 measures, both crude and age-adjusted estimates for all 3,144 counties, and ten national reference rows.
- Module 09 all-selected SHA-256: `2af5ce99fc7d66a18e95451084afc397e0f7392e9f1a2b5476377fd8811658d2`.
- Its North Carolina teaching release contains 500 county-measure rows, representing 100 counties by five measures, and has SHA-256 `33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9`.
- Module 09 passes 58 data checks. Its lab creates four figures, one 500-row decision table, and one short and long text alternative; its critique creates three deliberately flawed figures.
- In the pinned release, 54 counties are above the national age-adjusted point estimate on all five selected measures and 9 are at or below it on all five. This shows why the national reference alone does not produce a narrow priority list.
- The profile count and order are declared teaching devices, not validated scores. The module keeps crude and age-adjusted values, uncertainty intervals, adult denominators, direct labels, shared scales, and exact values available for review.
- DA-730 Module 10 reuses the 100-county `GHLTH` subset from Module 09, the exact 7,121-point Census boundary release from Module 05, and a new 1,546-row North Carolina primary-care HPSA source selection.
- Module 10 HPSA source SHA-256: `061fe5e18bc9cd58bd89256c686ddefbce6d77972c1139b1b339497f2eab5445`.
- Module 10 teaching-table SHA-256: `90a575f03bc94cc0eb336d263e3f9d8afe09cf68ddb95476bf1836c0574f9a07`.
- Module 10 passes 60 data checks. Its lab creates four figures, one 100-row exact table, and one text alternative; its critique creates three deliberately flawed maps.
- The selected HRSA source contains 740 current designated component rows and 210 unique current HPSA identifiers touching 98 counties. The teaching table does not call the maximum component score a county workforce rate.
- Seventy-three counties are above the 17.0 percent national health point, 23 meet the declared score-20 HPSA screen, and 19 meet both. The reference twelve are Robeson, Scotland, Hertford, Halifax, Warren, Greene, Washington, Wilson, Anson, Lenoir, Edgecombe, and Swain.
- The AHRF 2024-2025 archives were inspected but not redistributed. Included documentation restricts reproduction and identifies copyrighted source fields, so Module 10 uses the directly public HRSA HPSA data mart.
- DA-730 Module 11 preserves selected fields from all 1,171 synthetic patients and all 53,346 encounters in the pinned Synthea April 2020 CSV sample.
- Module 11 patient SHA-256: `a208fe4ff6fc9dc5cee4a201043a2f059943b8c058fdb191e19b0f9ffbb821bf`.
- Module 11 encounter SHA-256: `00298bf68f89dee9734cf133c516ad6b7efe95c8cd15a9458e7fb09c1dca56ce`.
- Its one-person-per-index teaching cohort contains 374 adults and has SHA-256 `b3f1cf69a54fd2f38dfe6debfd009ebb1c7d2b1ef7b42d7b35c989a9f068f3ca`.
- Module 11 passes 64 data checks. Its lab creates a conserved alluvial flow, explicit-denominator matrix, endpoint composition, seven-row exact table, and text alternative; its critique creates three deliberately flawed structural displays.
- The reference screen selects `Inpatient -> No encounter recorded`: 38 synthetic patients and a 15.8 percent 90-day acute-return percentage versus 9.6 percent in the full cohort. This is a definition-audit screen, not a quality threshold.
- Synthetic names, addresses, SSNs, driver identifiers, passports, provider, organization, payer, and cost fields were not redistributed because the teaching decision does not need them.
- DA-730 Module 12 validates the complete 138,084-row CMS Timely and Effective Care hospital release before preserving every Massachusetts EDV, OP_18b, and OP_22 row.
- Module 12 source-selection SHA-256: `f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b`.
- Its teaching table contains 186 hospital-measure rows across 62 facilities and has SHA-256 `fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd`.
- Its three-row measure dictionary has SHA-256 `2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412`.
- Module 12 passes 179 data checks. Its lab creates one five-view dashboard, one three-row exact decision table, and one text alternative; its critique creates three deliberately flawed dashboards.
- The reference case selects Anna Jaques Hospital for a definition and current-data review because its public OP-22 value is 23 percent, the highest observed value among 53 reporting Massachusetts hospitals and above the mock 10-percent trigger.
- The public OP-22 period ended 590 days before release. The dashboard therefore recommends definition validation and current local data, not a current operational judgment or intervention.
- The Massachusetts medians are descriptive references. The 10-percent and 240-minute values are mock quality-improvement charter assumptions, not CMS thresholds.
- DA-730 Checkpoint 2 packages one applied artifact from each of Modules 07 through 12 into six complete evidence chains.
- The assembler regenerates six PNG figures, six exact CSV tables, six text alternatives, six editable analysis wrappers, and six prefilled source records from a clean target.
- Exact released table rows are 65 for accessibility, 94 for time, 500 for comparison, 100 for place, 7 for structure, and 3 for the dashboard.
- The package includes eight learner writing templates, a 982-line 17-section specification, instructor notes, a release record, and a Python standard-library validator.
- The validator self-check passes a valid fixture and rejects a missing dashboard. The full assembler test passes, the incomplete starter is rejected, and a nonempty target is protected from overwrite.
- The checkpoint decision owner is a DA-730 clinical analytics review panel. The decision is whether to approve, condition, revise, or refer a feasible Module 13 capstone proposal.
- The six cases remain separate populations. The checkpoint uses them as evidence of transferable readiness and does not combine them into one clinical claim.
- DA-730 Module 13 reuses the pinned Module 12 CMS teaching table instead of duplicating or silently refreshing it.
- Module 13 validates the 186-row teaching table, three-row measure dictionary, and 186-row source selection against their exact checksums and passes 66 invariant checks.
- Its lab creates a technical quality-director story, an executive quality-committee story, a three-row exact table, one accessible alternative covering both figures, an audience-adaptation reference, and a decision brief.
- Its critique creates three deliberately flawed stories covering overstated causality, hidden freshness, and annotation misdirection.
- The stable reference finding is that the historical 23-percent public OP-22 signal warrants definition and current-data review. The 590-day source lag prevents a current performance or intervention conclusion.
- The technical and executive versions preserve the same values, units, samples, reporting windows, peer references, mock-trigger origin, action owner, material limitation, and unsupported conclusions.
- All 13 DA-730 modules now have 21-section specifications and runnable teaching packages. Named human reviews remain pending before alpha.
- DA-730 Checkpoint 3 packages the Module 13 evidence into a portable final release with three pinned CMS data files, editable analysis, two audience figures, one exact three-row table, complete learner records, an accessible defense, and a reviewer disposition.
- The final checkpoint has a 17-section specification, safe PowerShell assembler, standard-library Python validator, learner and review templates, instructor answer key, and machine-readable release record.
- The assembler copies exact source tables with row counts 186, 3, and 186; renders two visually inspected PNG files; and writes the exact 3-row, 20-column selected-facility table.
- The validator self-check passes a complete fixture and rejects a missing supporting figure. Full assembly and analysis rerun pass, the incomplete starter is rejected for the intended reasons, and a nonempty target is protected from overwrite.
- Final release requires a score of at least 80, passed clinical, accessibility, reproducibility, and oral-defense gates, and an `approve` or `approve with conditions` disposition.
- DA-730 now has all 13 module packages and all three cumulative checkpoint packages as runnable release candidates. Faculty and human review still gate alpha promotion.
- FND-1 Module 01 uses a deterministic three-row, three-column synthetic software-test table with SHA-256 `330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab`.
- The Module 01 source contains no patient records and supports no clinical claim. The Synthea healthcare source system begins in Module 02.
- The Module 01 workspace builder copies a portable template to a new target and refuses an existing target.
- The standard-library validator passes a 15-check starter and a 26-check complete submission, then rejects a fixture missing the AI-use record.
- A fresh Python environment installed JupyterLab 4.6.3, nbclient 0.10.2, and pandas 3.0.5. Python 3.12.10 with SQLite 3.49.1, the executed notebook, and the supplied R 4.6.1 script returned the exact three-row and total-15 reference result.
- The clean reference submission preserved `main`, four commits, a non-fast-forward merge, an annotated `fnd1-setup-v0.1.0` tag at `HEAD`, and a clean working tree.
- Module 01 is a runnable release candidate. Faculty, data engineering, Python/notebook, R, accessibility, privacy, responsible-AI, and independent-instructor reviews remain pending before alpha.
- FND-1 Module 02 validates the pinned 8,982,431-byte Synthea April 2020 CSV archive and exact SHA-256 `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`.
- The archive contains 16 CSV tables, 82,293,440 uncompressed bytes, 168 source fields, and 471,836 rows. The relational release preserves every source row and field.
- The tested SQLite build contains 177 dictionary fields, including 9 transparent source-row surrogates, and is 141,234,176 bytes. It is rebuilt rather than stored in Git.
- Module 02 preserves 30,363 observations with missing encounter references as `NULL`, the zero-row supplies table, all six encounter classes, and zero orphan nonblank relationships.
- SQLite reports zero foreign-key failures and integrity `ok`. Three minimized views expose 27 fields for first retrieval without defaulting to identity-like or cost fields.
- Linked teaching FHIR R4 Patient, Encounter, and Observation examples resolve to one another. They are transparent CSV-derived mappings, not a conformance claim.
- Five reference extracts return 16, 6, 3, 25, and 25 rows. The standard-library runner accepts only named read-only SQL and protects nonempty output directories.
- The canonical validator passes 96 database checks and 126 complete-submission checks. Builder, query-runner, validator, source revalidation, invalid-FHIR, incomplete-record, target-overwrite, and output-overwrite checks pass.
- Module 02 is a runnable release candidate. Faculty, data engineering, clinical informatics, FHIR, rights, accessibility, privacy, responsible-AI, and independent-instructor reviews remain pending before alpha.
- FND-1 Module 03 uses four read-only SQL files to select 1,048 adult eligible emergency or inpatient events from the accepted Module 02 database.
- Deterministic event ordering selects one index for each of 374 synthetic adults: 314 emergency indexes and 60 inpatient indexes. The conserved flow excludes 690 patients with no acute event in the period and 107 with only under-18 acute events.
- The one-row-per-person analytic table contains 374 rows and 29 fields. Its SHA-256 is `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.
- Thirty-day states are 263 no encounter recorded, 92 scheduled care, 4 urgent care, and 15 acute return. Ninety-day fields contain 36 acute-return flags, 8 death flags, and complete source coverage for all 374 rows.
- Separate pre-index aggregation prevents join multiplication. Encounter, acute, condition, and medication history-count sums are 2,138, 113, 468, and 1,007.
- Five committed outputs reproduce byte for byte from the pinned database. The validator passes 600 package checks, 613 checks with upstream database reproduction, and 614 complete-submission checks; incomplete packages and existing build targets are rejected.
- Module 03 is a runnable release candidate. Faculty, SQL, clinical informatics, temporal logic, accessibility, privacy, responsible-AI, and independent-instructor reviews remain pending before alpha.
- FND-1 Checkpoint 1 preserves the source assessment weights as 15 Module 01 setup points plus 25 Module 03 SQL cohort points. Module 02 is a required relational-data gateway and adds no separate weight.
- The instructor reference assembles 45 files and registers 35 immutable artifacts. The manifest is 4,107 bytes with SHA-256 `36cf454387db595e9237f461556676db7611b3b60b2762f8554e4d9d580c96a6`.
- The checkpoint preserves five Module 02 first extracts with row counts 16, 6, 3, 25, and 25, plus all five Module 03 outputs, both data dictionaries, schema SQL, an editable relationship model, accessible SVG and text, six module evidence records, and cumulative review records.
- Learner-mode assembly from three accepted workspaces passes a 295-check starter audit. Complete reference validation passes 341 checks and invokes the 614-check Module 03 submission validator through the checkpoint subset.
- The checkpoint requires at least 32 of 40 points, 19 noncompensable gates, an adequate defense, and `accept` or `accept with conditions` before Module 04 begins.
- Checkpoint 1 is a runnable release candidate. Faculty, clinical analyst, SQL, informatics, reproducibility, accessibility, privacy, responsible-AI, and independent-instructor reviews remain pending before alpha.
- FND-1 Module 04 preserves the accepted 374-row, 29-field analytic table and SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a` as an immutable upstream input.
- Its separate deterministic defect layer contains 379 rows, 374 distinct people, five exact duplicates, 20 seeded defect families, 56 issue cases, and 68 manifest changes. The defective CSV SHA-256 is `7800c1d24093b93ce40634afe652e574a1ed2775eba8a742c0bd00bf3596a02d`.
- The module independently detects all 20 seeded rules and eight accepted natural-characteristic rules. It profiles all 29 fields and retains optional missingness, five ages at least 100, two prior-encounter counts above 100, one prior-medication count above 100, six rows in small race categories, and 12 urgent-state or death-endpoint rows as review conditions.
- The reference initial decision is `fix`; after deterministic restoration it is `proceed with conditions`. The resolved table matches the accepted file byte for byte.
- Builder, profiler, and validator self-checks pass. A clean build reproduces 13 generated artifacts byte for byte; the notebook executes four code cells in a fresh exact-version environment; validation passes 344 release checks and 340 complete-submission checks.
- Module 04 is a runnable release candidate. Faculty, notebook, clinical-informatics, accessibility, privacy, responsible-AI, and independent-instructor reviews remain pending before alpha.
- FND-1 Module 05 uses the exact 374-row Module 04 resolved table and all 28 passing quality-rule results. Both upstream fingerprints are enforced before calculation.
- The descriptive release contains 17 one-variable profiles, 12 cells across two complete cross-tabs, six cohort rates with Wilson intervals, two unadjusted index-class rows, 27 denominator records, and 18 passing invariants.
- Next-event timing uses 111 available recorded encounters rather than treating 263 structural blanks as zero. Supported ages and utilization extremes and small internal cells remain visible through N01 through N08.
- The six output SHA-256 values are recorded in the module release. A clean build reproduces all six CSV files and the build report byte for byte.
- The notebook executes four code cells in a fresh exact-version environment. The validator passes 1,101 release checks and 1,100 complete-submission checks.
- The reference decision is `accept with conditions`: Module 06 must use exact released rows, preserve denominator and interpretation limits, label strata unadjusted, and make no real-population claim.
- Module 05 is a runnable release candidate. Faculty, descriptive-statistics, clinical-informatics, notebook, accessibility, privacy, responsible-AI, and independent-instructor reviews remain pending before alpha.
- FND-1 Module 06 fingerprints the exact 29-row Module 04 missingness profile, six Module 05 rates, 27-row denominator registry, and 374-row resolved analytic table before rendering.
- F01 compares accepted and deliberately defective missingness for eight fields. F02 preserves all six Module 05 rates and Wilson intervals. F03 counts 374 selected indexes across 20 quarters, including 314 emergency and 60 inpatient indexes.
- The release contains three exact CSV tables, three 2100-by-1200 PNG files at 300 DPI, three matching SVG files, three structured text alternatives, and a 25-field figure registry with SHA-256 `5cdd846d9318d6dc8c2f3da41a6be6ce172b7c91d6465dc085e9f3790732d62b`.
- Every figure uses a zero-based quantitative axis, 8-point-or-larger type, explicit units, exact-table linkage, and redundant hatch, line, marker, or direct-label cues. Grayscale, 50-percent-width, 200-percent-zoom, reading-order, and text-equivalence reviews pass.
- A fresh Python 3.12.10 environment with Matplotlib 3.10.9 and Pillow 11.1.0 produced two identical renders. All 14 generated artifacts match the canonical release byte for byte.
- The renderer protects an existing target. The validator passes 616 release checks and 615 complete-submission checks and rejects the incomplete learner template.
- The reference decision is `accept with conditions`: the Week 6 checkpoint must preserve exact-table links, equivalent text, N01 through N08, descriptive interval meaning, selected-cohort time wording, and synthetic-data scope.
- Module 06 is a runnable release candidate. Faculty, clinical-analytics, accessibility, data-visualization, clinical-informatics, Python, privacy, responsible-AI, and independent-instructor reviews remain pending before alpha.
- FND-1 Checkpoint 2 preserves one 25-point Week 6 component: 13.75 quality points, 6.25 descriptive points, and 5 access points. These are checkpoint shares rather than added module weights.
- Its immutable contract copies 35 accepted artifacts: 11 from Module 04, 9 from Module 05, and 15 from Module 06. Reference and learner assembly each create 50 files and refuse an existing target.
- The artifact contract is 5,993 bytes with SHA-256 `ec031d23a50628b07ce15091c90a76f03241e3f4c4a17927211b74b854754a6b`. The 8,812-byte release manifest SHA-256 is `d7bb0e561309f4b61353f4485fe1d647d8a15c47e064f93acd816a77e512489d`.
- The checkpoint preserves the accepted 374-row, 29-field table, all D01 through D20 resolutions, N01 through N08 conditions, 17 profiles, 12 cross-tab cells, six rates, two strata, 27 denominator records, 18 passing checks, and all F01 through F03 access routes.
- Starter validation passes 363 checks and complete reference validation passes 389. The self-check rejects unfinished cumulative records and a missing immutable artifact.
- A score of at least 20 of 25, every gate, an adequate defense, and `accept` or `accept with conditions` permit Module 07. The reference disposition is `accept with conditions`.
- Checkpoint 2 is a runnable release candidate. Named faculty, quality, clinical, accessibility, reproducibility, privacy, responsible-AI, and independent-instructor reviews remain pending before alpha.
- FND-1 Module 07 treats accepted Checkpoint 2 version 0.1.0 as immutable and adds no new analytic result. It packages evidence, exact pipeline source, release records, a material AI audit, and technical-defense preparation.
- Its 23-row pipeline contract preserves 1 Module 01 dependency file, 13 Module 02 database files, 5 Module 03 cohort files, 2 Module 04 quality files, the Module 05 descriptive builder, and the Module 06 renderer.
- The pipeline contract is 4,478 bytes with SHA-256 `d61f208046663b80f8a591be66cc4f22fecbf0c5be7803786f75fd74cdd1d783`.
- Reference and learner assembly each create 90 files and a 74-row immutable manifest. The 10,856-byte manifest SHA-256 is `804d454dcdf43d0f625c90130b9bd5c698b51451ddcc1fd0910ca52e1bbd9111`.
- The toolkit carries 35 Checkpoint 2 evidence artifacts, ten cumulative checkpoint records, four checkpoint provenance files, 23 pipeline-source files, the pipeline contract, and the portable validator.
- The reference AI audit independently verifies that all 263 `No encounter recorded` rows retain blank next-event companion fields. Zero would invent an event at the follow-up origin and is rejected.
- Starter validation passes 585 checks and complete reference validation passes 657. Existing targets, unfinished records, and a missing immutable rate table are rejected; two clean assemblies produce the same immutable manifest.
- Module 07 drafts the exact 35-point final component. A score of at least 28, every gate, an adequate defense, and `accept` or `accept with conditions` permit final-checkpoint review.
- All seven FND-1 technical modules are now runnable release candidates. The final checkpoint and named human review remain before course completion.

## Pending confirmation

- Confirm that the intended Joe Joseph, MD, is the Sound Physicians hospital medicine leader publicly listed with FHM/SFHM and Regional Chief Medical Officer experience.
- Confirm publishable biography and current title directly before release.

## Next resume instructions

1. Read the FND-1 course, Module 07 specification and release record, final-checkpoint brief, source record, master architecture, and this ledger.
2. Treat the accepted 90-file Module 07 toolkit candidate and 74-row manifest as immutable final-checkpoint input.
3. Write the 17-section final-checkpoint specification around the source 35-point rubric, technical defense, and health-system analytics engineering lead decision.
4. Preserve D01 through D20 resolution, N01 through N08 conditions, exact descriptive meaning, equivalent access, material AI audit, and synthetic claim limits.
5. Build the protected final assembler, learner and reviewer records, instructor answer key, validator, release record, and final `accept`, `accept with conditions`, `revise`, or `refer` disposition.
6. Update the Commons version and this ledger, then commit and push the final checkpoint before starting FND-2.
