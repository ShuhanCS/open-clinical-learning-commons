# Age-band and ACS margin method

- Population: `adults age 18 and older in the 1,597 accepted Massachusetts census tracts`.
- Denominator source: `ACS 2020-2024 five-year Detailed Table B01001`.
- Standard population: `5,679,768 matched ACS adult denominator units`.
- Age bands: `18-34, 35-49, 50-64, 65-74, and 75 years and older`.
- Crosswalk rows: `38`.

The crosswalk uses male B01001 cells 007 through 025 and female cells 031 through 049. It keeps each estimate paired with its published 90 percent margin of error. SQL sums the declared cells into five mutually exclusive adult age bands. The five bands reconcile to the accepted adult denominator for every tract.

For each age-band sum, the approximate margin is:

`sqrt(sum(nonzero-estimate component MOE squared) + largest zero-estimate component MOE squared)`

The second term is zero when no component estimate is zero. The approximation follows Census teaching guidance for sums, including its special handling of multiple zero estimates. It does not include covariance and can differ from an ACS estimate produced from microdata or variance replicate tables.

Forty-one tract-age rows have a zero denominator. Those rates remain unavailable. Twenty-one tracts therefore have no direct standardized rate. Eighty tracts have at least one age-band denominator below 50 and require the guided indirect exercise.

The ACS margin describes uncertainty in the population estimate. The Wilson interval describes uncertainty around the generated event proportion under the teaching calculation. They answer different questions and are not combined into one interval.
