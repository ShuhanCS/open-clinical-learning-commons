# Linkage and denominator audit

The public-source union contains 1,620 tract keys. All 1,597 PLACES diabetes tracts appear in ACS and SVI and are eligible for Module 02 measure construction. Sixteen additional ACS and SVI tracts have no PLACES diabetes row. Seven additional ACS tract records have neither a PLACES diabetes row nor an SVI row. The audit retains both states.

The accepted measure layer has 7,985 denominator rows and 7,985 synthetic event rows. Every synthetic row matches one independently derived tract-age denominator. There are no orphan rows, denominator mismatches, negative counts, counts above denominators, non-synthetic rows, or wrong periods.

The five age bands sum to 5,679,768 adult denominator units. The generated numerator sums to 283,614 events. All 30 SQL checks and all eight source-reconciliation checks pass.

PLACES `totalpop18plus` stays with the PLACES modeled estimate. It is not substituted for the ACS adult denominator. The two fields refer to different source constructions and vintages, so a difference is evidence to document rather than a defect to erase.
