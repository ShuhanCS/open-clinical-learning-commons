# Curriculum build ledger

- Current release: 0.26.0
- Last updated: 2026-08-30
- Active phase: foundation-course specification and build
- Last completed unit: DA-730 final checkpoint, Decision-story capstone and defense
- Next unit: FND-1 straight-through technical foundations course

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

## Source status

- `Curriculum-30-Credits-2026-08-29.zip` inspected: 11 DOCX course files.
- `OneDrive_2026-08-29 (1).zip` inspected: same 11 DOCX course files and file sizes.
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

## Pending confirmation

- Confirm that the intended Joe Joseph, MD, is the Sound Physicians hospital medicine leader publicly listed with FHM/SFHM and Regional Chief Medical Officer experience.
- Confirm publishable biography and current title directly before release.

## Next resume instructions

1. Read the master curriculum architecture and the source curriculum documents for the first foundation course.
2. Confirm the exact FND-1 course title, catalog number, source-module ownership, and checkpoint outcomes from the extracted curriculum evidence.
3. Keep FND-1 separate from FND-2 and teach its technical sequence straight through rather than using the applied-course rhythm.
4. Write the durable FND-1 course specification before broad implementation.
5. Define exact Week 3, Week 6, and final deliverables, public or synthetic datasets, reproducibility, accessibility, AI accountability, assessment, and release checks.
6. Build and release FND-1 modules one by one, then move to the separate FND-2 build.
