# Stewardship, governance, and retirement

## Stewardship

| Asset | Steward | Review trigger | Protected rule |
|---|---|---|---|
| Intended use and product brief | clinical decision owner | purpose or action changes | no silent expansion of use |
| Logic and rule | clinical informatics owner | trigger suppression input or version changes | new version and full regression |
| Terminology and units | terminology owner | code system unit or mapping changes | fail visibly on mismatch |
| Historical evidence and model | evidence and model-risk owners | source model or evaluation changes | preserve untouched evaluations |
| Threshold and alert budget | governance council | any proposed threshold | local evidence and explicit approval required |
| Interface and accessibility | accessibility and workflow owners | any card or interaction change | blocked defects cannot ship |
| Safety case | patient-safety owner | hazard failure or control changes | human stop and fallback retained |
| Monitoring and silence detection | monitoring and patient-safety owners | measure ledger or threshold changes | independent reconciliation retained |
| Data and privacy | data steward and privacy owner | data class route or retention changes | minimum necessary and no unauthorized data |
| Candidate package | APP-4 faculty owner | any byte or decision changes | new semver release and reproduction |

## Decision rights

The fictional governance council may continue curriculum review, require revision, refer, or stop. A local clinical organization would own any real evaluation decision. Clinicians retain review and override. Patient-safety and accessibility owners may stop the affected route. Security and privacy owners may stop a data route. An independent reviewer may withhold reproduction acceptance.

No learner, model, analyst, or agent receives clinical authority or a decision or sign-off right.

## Disagreement

Disagreement is recorded with the issue, evidence, affected people, effect on the recommendation, owner, response, unresolved status, and escalation route. Silence is not agreement. Raising a safety, access, burden, privacy, or model concern must not trigger blame or retaliation.

## Retirement

Retire the concept when its intended use is no longer defensible, no accountable owner exists, required data or controls cannot be maintained, failure detection is unavailable, burden or exclusion cannot be addressed, local benefit cannot justify harm, or safe fallback and stop authority cannot be guaranteed. Retirement records preserve the evidence and reason; they do not erase failed history.
