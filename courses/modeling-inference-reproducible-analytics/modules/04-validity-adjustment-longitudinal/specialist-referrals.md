# Specialist referrals

| Trigger | Refer to | Question that must be resolved |
|---|---|---|
| Unmeasured clinical preference or doubtful causal ordering | causal inference specialist and clinical owner | Is the effect identifiable, or must the claim narrow? |
| Weak real-world overlap or extreme weights | biostatistician | Should the target population, estimator, or design change? |
| Consequential MAR or MNAR assumption | missing-data specialist and data steward | Which sensitivity range is credible and decision-relevant? |
| Selected timing subset | clinical informatician and survival analyst | What generated recording, encounter, and follow-up? |
| Irregular visits, informative dropout, or complex correlation | longitudinal-modeling specialist | Which dependence and missingness model fits the process? |
| Competing events or nonproportional hazards | survival analyst and clinician | Which time-to-event estimand and model are defensible? |
| Clinical interpretation or intended use | named clinician and model-risk reviewer | Does the evidence answer the care decision safely? |

No referral is marked complete in this release. The module records the trigger and stops unsupported inference; it does not simulate approval.
