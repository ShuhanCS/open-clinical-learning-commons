# Data specification

## Accepted public-derived handoff

Module 05 fingerprints five accepted Module 04 files: the release record, linked-person table, linked-event table, source inventory, and denominator registry. They contain 1,255 people, 28,455 events, and references to all 25 official MEPS source files. The build stops if any byte or release permission changes.

`module04-linked-persons.csv` keeps module-scoped teaching identifiers, grouped public fields, `PERWT24F`, `VARSTR`, `VARPSU`, access fields, and the synthetic response handoff. `module04-linked-events.csv` supplies the person-level any-telehealth indicator. It does not supply portal access or preference.

## Synthetic comment layer

`comment-opportunities.csv` contains one deterministic opportunity for each of the 782 accepted synthetic respondents. The assigned channel, language-support offer, accessible-format offer, return score, and return state are synthetic.

`synthetic-comments.csv` contains 420 received comments. Each comment is generated from fixed English phrase templates and has an explicit synthetic data class. Direct MEPS person and event identifiers are absent.

The instructor directory retains the fixed theme truth, 120 simulated double-coding records, and 420 assisted-label audit rows. Instructor truth is excluded from assembled learner workspaces.

## Public group estimates

Public estimates use `PERWT24F`, `VARSTR`, and `VARPSU`. Domain variance retains sampled PSUs outside the domain as zero contributions. A reportable teaching estimate needs at least 50 valid records, 10 positive records, 10 negative records, and two contributing PSUs.

Unsupported rows retain the source group and counts but leave estimates blank. Contrasts use one joint linearized survey calculation. They remain descriptive and exploratory.

## Comment counts

Comment counts use the 420 received synthetic comments as their denominator. They are not survey-weighted. They cannot estimate patient prevalence, sentiment, saturation, access, trust, discrimination, or channel preference.
