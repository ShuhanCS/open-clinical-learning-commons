# APP-5 Module 01 instructor notes

## Instructional purpose

Module 01 slows the course down before it starts calculating. Learners must be able to say what population a measure represents, which denominator belongs to it, what geography and time period it covers, who may be affected by the decision, and what the public evidence cannot support.

The reference decision permits Module 02 curriculum construction only. It does not approve a rate, disparity, tract ranking, map, targeting rule, program, community contact, or real-world action.

## Reference case

`FMA-DP-01` is an explicitly fictional Massachusetts adult diabetes-prevention planning review. Real tract identifiers make the public-data work authentic. The council, resource constraint, intervention, capacity, community-response records, implementation stream, and outcomes are fictional or synthetic.

The planning question is whether public evidence is defined well enough to construct responsible measures and later support structured community review. It is not “Which tracts should receive funding?”

## Exact release findings

- PLACES: 1,597 Massachusetts `DIABETES` tract rows, 24 fields, 14 counties, measure year 2023, modeled crude prevalence from 0.7% to 30.5%, adult population fields from 66 to 13,070, and complete published lower and upper confidence limits.
- ACS: 1,620 Massachusetts B01001 tract rows and 100 released fields after verification of the complete 616,690-row, 200,356,282-byte national table file. The release carries all 49 estimates and 49 margins plus source and derived tract keys.
- SVI: 1,613 Massachusetts tract rows and all 158 fields. The accepted file contains 1,385 negative sentinel-like values across its fields; these remain visible for later documented interpretation rather than being recoded in Module 01.
- All 1,597 PLACES tracts appear in both ACS and SVI.
- SVI has 16 tracts without a PLACES diabetes row.
- ACS has 23 tracts without a PLACES diabetes row and seven tract records without an SVI row.
- The three-source intersection is 1,597 tracts; the union is 1,620.

Do not use the prevalence range to ask learners to identify “worst” tracts. Use it to ask why a modeled value, interval, population field, geography, and source period must travel together.

## Correct denominator reasoning

The PLACES modeled prevalence is interpreted with the adult population and methods carried by PLACES. The ACS B01001 release supplies a separate 2020-2024 population structure and margins for later denominator and standardization work. Learners may compare source populations as a data-quality question later, but they may not silently substitute one denominator into another measure.

SVI `E_TOTPOP` is not a diabetes denominator. A relative SVI rank is not a count, rate, risk probability, or eligibility threshold.

Module 01 fixes denominator roles. Module 02 fixes formulas, age bands, standard population, margin handling, and synthetic numerator construction.

## Language coaching

Require learners to distinguish:

- difference: two values are not equal;
- disparity: a measured difference across defined groups or places;
- inequity: a difference judged unfair or unjust using evidence and an explicit normative basis;
- area context: a feature measured for a geographic unit; and
- individual attribute: a feature measured for a person.

Ask who or what produced the pattern, who may be missing, and what decision could follow. Do not permit “vulnerable tract,” “high-risk resident,” “noncompliant community,” or “the SVI caused” as shorthand.

## Community accountability

Affected residents and community organizations must have a meaningful route to question the framing, require revision, add local evidence, contest burdens, and stop progression to real action. A consultation box without decision rights does not satisfy the gate.

The fictional council owns curriculum progression. No course role can authorize real outreach, funding, implementation, or policy.

## Common failure patterns

- defining the denominator as “Massachusetts adults” without source, period, tract inclusion, or age rule;
- calling modeled prevalence an observed diagnosis count;
- treating ACS and PLACES population fields as interchangeable;
- assigning SVI or a tract average to individuals;
- using “inequity” when only a numerical difference has been shown;
- ignoring unmatched tracts because the main intersection is complete for PLACES;
- framing the decision as ranking or funding before local and community evidence exists;
- allowing an agent to decide the population, equity language, or progression; and
- treating curriculum progression as real-world permission.

## Required conditions before Module 02 alpha

- faculty and population-health clinical approval of the case question;
- epidemiology and biostatistics approval of the population, denominator roles, age bands, standard population, and later standardization plan;
- Census, PLACES, and SVI methods review of the source interpretations;
- community, racial and ethnic equity, language-access, and disability-access review of the framing and decision rights;
- privacy and governance review of public-geography linkage and synthetic boundaries;
- approval of the deterministic synthetic event design; and
- independent reproduction of acquisition, normalization, profiles, workspaces, and validation.
