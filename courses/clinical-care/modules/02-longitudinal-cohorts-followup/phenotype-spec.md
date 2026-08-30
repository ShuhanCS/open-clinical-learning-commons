# Longitudinal phenotype specification

## Decision and grain

- Decision: `is the cohort valid enough for survival analysis?`
- Initial grain: `one row per synthetic adult at the first qualifying acute encounter`
- Landmark grain: `one row per synthetic person with no index death early death or early acute return through day 30`
- Initial population: `518`
- Landmark population: `476`

## Index rule

- Eligible class: `emergency or inpatient`
- Start bound: `on or after 2010-01-01T00:00:00Z and before 2019-04-01T00:00:00Z`
- Age: `18 or older at encounter start`
- Selection: `first eligible encounter by start then encounter ID`
- Discharge origin: `index encounter stop`

## Branch rules

- Index death: `recorded death date on or before index discharge date`
- Early post-discharge death: `death date after discharge and through the discharge date plus 30 days`
- Early acute return: `first emergency or inpatient encounter after discharge and through 30 elapsed days`
- Branch precedence: `index death then early death then early acute return`
- Branch overlap in the pinned release: `0`

## Exposure and landmark

- Scheduled follow-up: `first ambulatory outpatient or wellness encounter after discharge and through 30 elapsed days`
- Exposure availability: `day 30 only`
- Landmark: `index stop plus 30 elapsed days`
- Landmark eligibility: `no index death early death or early acute return`
- Exposed at landmark: `129`
- Unexposed at landmark: `347`

## Outcome and censoring

- Primary event: `first emergency or inpatient encounter after day 30 and through day 365`
- Later events: `87`
- Exposed later events: `25`
- Unexposed later events: `62`
- Administrative end: `index stop plus 365 elapsed days`
- Later death rule: `recognize a death after day 30 through day 365 as a competing concern and censor before an acute return when it occurs first`
- Event censoring disposition: `87 event 0 competing-death censor 389 administrative-end censor`
- Maximum risk-set follow-up: `335 days`

## Claim boundary

The phenotype supports synthetic-data method instruction and a Module 03 survival analysis. It does not estimate real risk or treatment effect and does not authorize clinical action.
