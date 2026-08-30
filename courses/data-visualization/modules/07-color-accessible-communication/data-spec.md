# Module 07 data specification

## Purpose

The release supports one question: can a clinical quality committee recover the same CMS finding in color, grayscale, print, text, and a table?

Module 07 does not import a new clinical dataset. It reuses the exact Module 06 Massachusetts release so learners can test accessibility without changing the statistical claim.

## Upstream clinical release

- File: `../06-uncertainty-variation-small-numbers/data/ma_hf_readmission_uncertainty_2026.csv`
- Rows: 65
- Columns: 26
- SHA-256: `33e6284a1064bb12600903526e4e65c009f875d9e6f6a3f25783d3a9a4b00727`
- CMS landing page: https://data.cms.gov/provider-data/dataset/632h-zaca
- Measure: `READM_30_HF`
- Period: 2023-07-01 through 2025-06-30
- Source release: 2026-08-13

The upstream release contains 53 reported estimates, 2 too-few rows, and 10 not-available rows. Among reported estimates, CMS classifies 52 as no different from national and 1 as worse.

## Released file

| File | Rows | Columns | SHA-256 |
|---|---:|---:|---|
| `data/accessibility_hf_readmission_2026.csv` | 65 | 27 | `b58168d9002a3e489213b0fafde1eca76f5b1a426c71ea3d61551671d76a49c2` |

## Preserved source fields

| Field | Type | Rule |
|---|---|---|
| `facility_id` | text | Preserve the source identifier and any letter suffix. |
| `facility_name` | text | Preserve the public source name. |
| `city` | text | Preserve the public source city. |
| `county` | text | Preserve the public source county context. |
| `measure_id` | text | Always `READM_30_HF`. |
| `measure_name` | text | Preserve the CMS name. |
| `denominator` | integer or blank | Preserve the source denominator. Do not infer a value. |
| `score` | decimal or blank | Preserve the source score. |
| `lower_estimate` | decimal or blank | Preserve the source lower estimate. |
| `higher_estimate` | decimal or blank | Preserve the source higher estimate. |
| `start_date` | ISO date | Preserve `2023-07-01`. |
| `end_date` | ISO date | Preserve `2025-06-30`. |
| `estimate_status` | text | Preserve `reported`, `too_few`, or `not_available`. |
| `source_comparison_group` | text | Preserve the shortened source category. |
| `footnote_text` | text or blank | Preserve the joined official footnote text. |
| `source_release` | ISO date | Preserve `2026-08-13`. |

## Accessibility fields

| Field | Type | Derivation and use |
|---|---|---|
| `display_status` | text | Uses source comparison group for reported rows, otherwise `too few` or `not available`. |
| `display_label` | text | Plain-language direct label for the source status. |
| `display_symbol` | text | Short redundant cue: `B`, `N`, `W`, `T`, or `NA`. |
| `display_shape` | text | Human-readable shape name. |
| `display_shape_code` | integer text | Base R and ggplot2 shape code. |
| `display_line_type` | text | Solid, dashed, or dotted redundant line cue. |
| `display_color_hex` | text | Six-digit uppercase foreground color. |
| `contrast_on_white` | decimal | WCAG relative-luminance contrast ratio against white. |
| `contrast_on_black` | decimal | WCAG relative-luminance contrast ratio against black. |
| `reading_order` | integer | Reported scores descending, then too-few and not-available rows by facility name. |
| `short_alt_row` | text | Row-level exact-value alternative for a data table or long description. |

## Encoding contract

| Source meaning | Label | Symbol | Shape | Code | Line | Color | Contrast on white |
|---|---|---|---|---:|---|---|---:|
| Better | Better than national | B | square | 15 | solid | `#1B7837` | 5.54:1 |
| No different | No different from national | N | circle | 16 | solid | `#2166AC` | 5.90:1 |
| Worse | Worse than national | W | triangle | 17 | solid | `#B2182B` | 6.87:1 |
| Too few | Too few cases | T | x | 4 | dashed | `#4D4D4D` | 8.45:1 |
| Not available | Not available | NA | plus | 3 | dotted | `#111111` | 18.88:1 |

Color is never the only cue. The display must pair it with the label, symbol, shape, line type, position, or an exact table. The minimum ratio above is not permission to remove redundant cues.

## Contrast calculation

The build converts each sRGB component to relative luminance and calculates:

```text
(lighter luminance + 0.05) / (darker luminance + 0.05)
```

The calculation checks the defined foreground against a white or black background. A final chart must be tested again after export because antialiasing, transparency, line width, adjacent colors, print, and compression can change practical legibility.

## Missing-value contract

- Reported rows keep score, lower estimate, higher estimate, and denominator.
- Too-few and not-available rows keep blank score and interval fields.
- Missing source values do not become zero, the national rate, a category midpoint, or a visual position on the estimate axis.
- Every unavailable row remains in the exact-value table and text alternative.

## Build and validation

`build_accessibility_case.py` uses Python's standard library. It checks the upstream checksum, preserves the selected source fields, adds the fixed accessibility cues, computes contrast, sorts the reading order, and writes the release.

`validate_accessibility_case.py` runs 66 checks covering source identity, source values, statuses, missingness, ordering, encoding, contrast, and text alternatives.

## Interpretation limits

- A passing numerical contrast ratio does not prove that a complete visualization is accessible.
- The module does not simulate every color-vision condition, display, printer, zoom level, browser, or assistive technology.
- The source intervals remain CMS lower and higher estimates. The module does not assign a confidence level.
- CMS categories compare a hospital with the national rate. They do not test every hospital pair.
- The public estimates do not establish a causal quality difference or patient-level experience.
