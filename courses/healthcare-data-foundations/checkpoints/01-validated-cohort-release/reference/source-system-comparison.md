# Healthcare source-system comparison

| Source type | Origin | Common grain | Strength for analytics | Material limit | Decision it can support |
|---|---|---|---|---|---|
| EHR | care documentation and orders | patient event or note | clinical detail and workflow timing | documentation and care-process bias | local care and workflow review |
| Claims | billing and adjudication | claim line or episode | broad utilization and paid-service history | payment purpose and lag | utilization and financial review |
| Registry | defined condition or procedure collection | eligible patient or event | consistent focused variables | selection and participation limits | condition-specific tracking |
| Survey | sampled respondent report | response | experience and patient voice | nonresponse and recall | experience improvement |
| Operational | scheduling staffing and capacity systems | transaction or interval | current process and resource signals | local definitions and changing workflows | operations management |
| FHIR | standardized exchange resources | resource | portable structure and references | implementation variation | exchange and integration review |
| Public aggregate | agency reporting programs | facility geography or period | external comparison and transparency | aggregation lag and suppressed detail | descriptive public benchmarking |
| Synthetic | generator-derived records | generated patient or event | safe reproducible technical practice | not representative or clinically observed | method teaching and pipeline testing |

## Source chosen for this checkpoint

The Synthea relational release permits a complete public workspace-to-cohort exercise without exposing real patients. It fits technical teaching and exact reproduction. It cannot estimate real prevalence, utilization, mortality, access, quality, or treatment effect.
