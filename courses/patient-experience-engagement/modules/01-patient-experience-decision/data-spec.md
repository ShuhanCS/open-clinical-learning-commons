# APP-2 Module 01 data specification

## Source grain

`data/raw/HCAHPS-Hospital.csv.gz` contains the complete accepted CMS HCAHPS hospital file. Its grain is one public facility and HCAHPS measure ID per row. It contains public facility identities and hospital-level results. It contains no patient-level response rows.

## Files

| File | Rows | Purpose |
|---|---:|---|
| `data/raw/HCAHPS-Hospital.csv.gz` | 325,720 after decompression | complete immutable public source |
| `data/source-profile.csv` | 20 | source identity, dimensions, period, response support, and claim boundary |
| `data/measure-inventory.csv` | 68 | one row per HCAHPS measure ID and its reported value field |
| `data/discharge-measure-profile.csv` | 4 | full-source profile for the recovery-at-home decision anchors |

## Accepted source fields

The raw source has 22 fields covering public facility identity, measure identity, question and answer text, reported stars or values, completed survey counts, response rates, footnotes, and reporting dates.

`profile_source.py` rejects a changed header, file fingerprint, row count, facility count, measure count, reporting period, measure support, or decision-anchor profile.

## Interpretation limits

- Public rows identify facilities, not patients.
- Hospital-level reporting cannot reveal which patients were invited, who did not respond, item-level missingness, language access, mode effects within a hospital, or subgroup experience.
- The values do not identify a local intervention or establish a causal effect.
- The module uses the complete file to frame a measurement decision. It does not rank hospitals.
