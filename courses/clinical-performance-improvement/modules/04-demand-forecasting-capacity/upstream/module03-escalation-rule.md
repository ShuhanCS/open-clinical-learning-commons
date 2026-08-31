# Immediate escalation rule

- Rule ID: `E01`
- Decision owner: `CGH-ED-01 clinical performance and improvement council`
- Trigger: `a high C02 R1 or R2 clinician-delay signal plus a same-period C01 high signal or documented queue corroboration`
- Reference trigger point: `Week 44`
- Reference evidence: `C02 R1 high, C02 R2 above, C01 R1 high, and elevated evening queue evidence`
- Action: `open human clinical, flow, access, and safety review within one business day`
- Data stop: `if source identity, denominator, event clock, or support gate fails, stop interpretation and return to Module 02`
- Safety override: `a newly reviewed serious-harm candidate enters immediate safety review regardless of chart status`
- Automated staffing: `prohibited`
- Automated scheduling or routing: `prohibited`
- Clinical action: `prohibited`
- Implementation: `prohibited`
- Restart evidence: `accepted data repair or human review disposition with owner and date`

E01 is an escalation rule, not an intervention order. It directs accountable people to review the signal and source evidence. It does not select staff, change a schedule, route a patient, alter care, or authorize a test.
