# Module 03 data specification

## Public source

`data/raw/h256dat.zip` is the full official MEPS HC-256 2024 Full Year Consolidated ASCII public-use file. The builder reads `h256.dat` directly from the ZIP. It verifies five official source fingerprints before extracting any field.

The target keeps people with `PERWT24F > 0`, `AGE24X >= 18`, and `IPDIS24 >= 1`. The 1,255 derived rows retain grouped public fields, the official final person weight, and the variance stratum and PSU. The derived file does not retain `DUPERSID` or exact age.

## Synthetic overlay

`data/synthetic/response-study.csv` contains deterministic procedural fields. The generator creates assigned mode, Q21, Q22, Q23, response, item missingness, response cells, and a bounded teaching factor. These are synthetic even when joined to public-derived fields.

## Missing states

Negative MEPS codes remain `missing or inapplicable`. A synthetic nonrespondent has `not_observed_total_nonresponse`. A respondent sent to another health facility by Q21 has Q22 and Q23 `not_applicable`. An applicable respondent may have an item marked `missing`. None of these states is no.

## Weights

`base_person_weight` is official `PERWT24F`, which already includes AHRQ's annual weighting adjustments. `bounded_response_factor` is teaching-only and adjusts only the synthetic local response layer. `analysis_weight` is their product for synthetic respondents. The factor cap is 3.0.
