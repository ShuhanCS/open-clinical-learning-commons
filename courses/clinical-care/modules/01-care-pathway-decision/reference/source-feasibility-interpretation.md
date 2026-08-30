# Source feasibility interpretation

## F01 through F12

- F01 source synthetic people: The complete pinned release has 1,171 synthetic people and supports a full-source cohort flow rather than a convenience sample.
- F02 initial adult index cohort: The first qualifying acute event yields 518 synthetic adults and fixes the pathway entry population.
- F03 index deaths: Nine (9) people have a recorded death date on or before the index discharge date. Date-granular death and timestamped discharge require this explicit branch, and these people cannot enter the day-30 risk set.
- F04 early post-discharge deaths: Eight (8) deaths after the discharge date and through day 30 remain visible as a safety and cohort-flow branch and are not eligible for the landmark comparison.
- F05 early acute returns: Twenty-five (25) acute returns through day 30 remain visible and are excluded from the day-30 comparison rather than silently dropped.
- F06 day-30 landmark eligible: Four hundred seventy-six (476) people have no index death, early post-discharge death, or early acute return and form the comparison risk set.
- F07 scheduled follow-up: One hundred twenty-nine (129) landmark-eligible people have scheduled care in the first 30 days, providing an exposure group with limited but usable teaching support.
- F08 later acute returns: Eighty-seven (87) people have an acute return after day 30 and through day 365, supporting time-to-event instruction while retaining uncertainty.
- F09 exposed later acute returns: Twenty-five (25) later outcomes occur in the scheduled-follow-up group; no effect is calculated in Module 01.
- F10 unexposed later acute returns: Sixty-two (62) later outcomes occur in the comparator; baseline case mix and support must be examined before any adjusted comparison.
- F11 distinct index organizations: The landmark population spans sixty-four (64) organizations, creating sparse and unstable raw site cells.
- F12 raw site comparison readiness: Raw organization ranking is not ready. Module 02 must create a documented deterministic six-site teaching extension for stable method instruction.

## Feasibility conclusion

The complete synthetic source supports a longitudinal cohort, landmark, exposure, time-to-event outcome, and later risk-adjustment teaching case. Progression is conditional on full-source reproduction, explicit extension provenance, and no causal or real-site claim.

## Immortal-time and landmark explanation

Scheduled follow-up is observed during the first 30 days after discharge. It is not known at discharge. Assigning exposed status at discharge would incorrectly credit time a person had to remain alive and without an early acute return to receive follow-up. The day-30 landmark assigns exposure only after the window closes and starts the primary outcome risk set then. Index deaths, early post-discharge deaths, and early returns remain in the initial cohort flow.

## Source and claim boundary

Synthea supplies synthetic records without real patients. The exact counts support technical instruction and a decision to continue building the analytic case. They do not estimate real prevalence, care quality, access, equity, facility performance, treatment effect, or clinical benefit and do not authorize implementation.
