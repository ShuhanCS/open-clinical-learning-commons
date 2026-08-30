# Source feasibility interpretation

## CMS Timely and Effective Care

The accepted complete release contains 138,084 facility-measure-period rows, 16 columns, 4,658 facilities, 30 measures, and 56 states or reporting jurisdictions. Its exact raw SHA-256 is `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516`.

- `EDV` has 4,658 facility rows, 3,826 reported scores, and 832 unavailable scores. It provides demand context, not local arrival counts.
- `OP_18b` has 4,658 facility rows, 4,081 reported scores, and 577 unavailable scores. It defines a public visit-duration concept, not the `CGH-ED-01` clock.
- `OP_22` has 4,658 facility rows, 3,821 reported scores, and 837 unavailable scores. It motivates an access and balancing family but does not reveal why anyone left.

Unavailable values remain unavailable; they are not zero, average, or evidence of good performance.

## CMS Complications and Deaths

The accepted complete release contains 95,800 facility-measure-period rows, 18 columns, 4,790 facilities, 20 measures, and 56 states or reporting jurisdictions. Its exact raw SHA-256 is `26dc5ada150a735fa1807cebc3274619a14495b2286fd34e9083b4508cfa367d`.

- `PSI_90` has 4,790 facility rows, 2,908 reported scores, and 1,882 unavailable scores.
- `PSI_04` has 4,790 facility rows, 1,521 reported scores, and 3,269 unavailable scores.
- `PSI_03` has 4,790 facility rows, 3,056 reported scores, and 1,734 unavailable scores.

These measures show that safety concepts need explicit populations, risk windows, support, and limitations. They do not detect a current `CGH-ED-01` event or establish the cause of harm.

## HHS facility capacity

The complete inspected historical release contains 1,045,406 facility-week rows, 128 columns, 5,172 facilities, and 226 collection weeks from 2019-12-29 through 2024-04-21. It is 481,497,539 bytes with SHA-256 `b3ef37e7e8d9888ff241caab83ec43be7e26be3c592a5a4e120acbf541edea7f`. Exactly 39,492 rows are marked corrected and 1,005,914 are not.

The repository artifact retains every one of the 15,179 Massachusetts rows across 74 facilities and 24 decision-relevant fields. Its decompressed SHA-256 is `7689038ce3dd013fe26daf3e6433b15f419a10360e19d3a063789ce5ae2c1068`. There are 15,057 reported inpatient-capacity rows, 14,807 reported inpatient-use rows, 13,877 reported adult-ICU-capacity rows, and 10,909 reported emergency-visit rows when blanks and `-999999` are kept out of the reported count.

The HHS release is historical and was collected for a specific reporting program. It demonstrates capacity, use, coverage, correction, and sentinel-value handling. It does not describe current capacity, emergency flow, or staffing in `CGH-ED-01`.

## Feasibility conclusion

The three complete public releases are feasible for measure-family orientation and source-audit instruction. Progression is conditional on keeping their aggregate grain separate from the fictional local event model. No public source supports hospital ranking, patient inference, operational diagnosis, staffing prescription, causal attribution, or implementation.
