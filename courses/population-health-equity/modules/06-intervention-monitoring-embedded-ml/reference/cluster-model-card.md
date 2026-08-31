# Cluster challenger model card

## Intended use

The challenger tests whether area-profile groupings support bounded descriptive tailoring questions. It cannot rank need, select or exclude a tract, assign resources, infer individual traits, determine fairness, replace the transparent rule, or bypass community review.

## Data and features

The matrix contains 1,597 accepted tract rows and nine fixed features: modeled prevalence, interval width, log1p adult population, fictional capacity, fictional travel, fictional burden, fictional language-access readiness, fictional disability-access readiness, and a fictional staff-ready indicator. Selection labels are excluded. Missing values fail; no imputation is allowed.

## Model

The fixed model is scikit-learn 1.9.0 KMeans with four clusters, standard scaling, seed 73056, 20 initializations, and the Lloyd algorithm. Four alternate seeds and robust, min-max, and unit-norm scaling variants are declared in advance.

## Result

The smallest base cluster contains 267 tracts. The minimum alternate-seed adjusted Rand value is 0.894. The scaling-variant median is 0.120, below the 0.60 standard, and the carried tracts span only two clusters instead of at least three. The challenger fails and is not useful.

## Authority

No cluster output changes the 28 carried rows or 280 fictional places. The transparent community-review comparison remains the only accepted planning candidate, and it still has no real-world authority.
