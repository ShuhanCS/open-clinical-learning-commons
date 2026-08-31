# APP-4 Module 04: Alert burden, human factors, and equity

This 16.5-hour module asks whether one candidate design is supportable enough to enter a nonproduction sandbox. It does not choose a clinical threshold or authorize an alert.

## What you receive

- the complete accepted Week 3 reference checkpoint under `upstream/checkpoint01/`;
- a 1,000-person synthetic frame and 1,200 scripted encounter opportunities;
- 7,200 offline candidate comparisons across all six unaccepted evidence thresholds;
- interruptive-banner, passive-panel, and no-alert comparisons;
- session burden, scripted interaction, access, and equity evidence; and
- the assessment, decision, source, and validation controls for this module.

The public NHANES evidence and synthetic workflow evidence answer different questions. Keep them separate. The NHANES rows describe historical classification tradeoffs. The synthetic rows let you examine workflow assumptions and failure states. Neither source proves local utility, burden, patient benefit, fairness, or safety.

## Your work

Complete all 16 records in the workspace root. The main decision is whether one design may proceed as a Module 05 sandbox fixture. Compare every threshold, the passive contextual panel, and no alert. State what happens to interruptions, repeats, unavailable inputs, hidden work, language access, disability access, patient communication, override, and stop authority.

Do not call the `0.20` Module 02 fixture an evidence threshold. Do not treat a scripted dismissal as fatigue, misuse, or poor care. Do not fill suppressed equity cells or infer a group comparison that the support rule withholds.

Run the validator before submission:

```powershell
python validate_workspace.py --root .
```

Package acceptance permits only bounded Module 05 sandbox construction. Real-patient scoring, clinical threshold acceptance, clinical alerting, clinical action, implementation, production connection, and deployment remain prohibited.
