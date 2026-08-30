# Module 13 assessment

## Decision task

Use the capstone proposal approved at Checkpoint 2 to produce and defend one stable evidence chain for two named audiences.

Your audiences must have different tasks or levels of technical detail. The source values, definitions, population, time window, uncertainty, material limitation, and action boundary must remain consistent.

## Required package

```text
module-13/
  README.md
  decision-brief.md
  figure-primary.png
  figure-supporting.png
  accessible-table.csv
  alt-text.md
  analysis.R
  source-record.yml
  transformation-record.md
  audience-adaptation-record.md
  reproducibility-check.md
  critique-response.md
  ai-use.md
  defense/
    slides.pdf
    questions-and-responses.md
```

An approved alternative tool may replace `analysis.R` with another editable source. Keep the evidence and output names stable.

## Required work

### 1. Capstone README

Include:

- audience and authority;
- secondary audience;
- decision;
- source and release;
- strongest finding;
- supported action;
- unsupported actions;
- exact reproduction commands;
- expected outputs;
- folder map;
- reviewer names or roles; and
- final status.

### 2. Primary figure

The primary figure must:

- carry the main finding;
- serve the primary audience task;
- use a finding-led title;
- preserve units and denominators;
- preserve source time and uncertainty;
- expose the material limitation when omission would mislead;
- use direct labels and non-color cues;
- name the source; and
- support the requested decision.

### 3. Supporting figure

The supporting figure must answer a different necessary question.

If no supporting figure is needed, submit a one-page `figure-supporting.png` statement that says `No supporting figure is needed` and explains why the primary figure, exact table, and brief are sufficient. The instructor must approve this path before submission.

### 4. Accessible table

The table must preserve every exact value that changes the decision, including:

- identifiers needed for interpretation;
- measure or state definition;
- value and unit;
- numerator and denominator or sample meaning;
- missingness or status;
- time window;
- source release;
- uncertainty or peer context;
- threshold origin when used;
- action; and
- interpretation limit.

### 5. Text alternative

For both figures, state:

- audience;
- decision;
- structure;
- source population;
- strongest finding;
- exact key values;
- uncertainty, missingness, or freshness;
- threshold origin when used;
- requested action;
- owner; and
- unsupported conclusion.

### 6. Source record

Record:

- publisher;
- dataset;
- complete HTTPS landing page;
- exact download or API URL;
- access date;
- release and coverage dates;
- rights or terms;
- selected fields and filters;
- row and column counts;
- checksum;
- transformations;
- missingness;
- known limits; and
- upstream dependencies.

### 7. Transformation record

Document every:

- source selection;
- filter;
- join;
- exclusion;
- recode;
- calculation;
- denominator;
- grouping;
- ordering;
- threshold;
- annotation;
- manual review; and
- export.

No material transformation may exist only in prose or manual chart editing.

### 8. Audience-adaptation record

Use this table:

| Element | Primary audience | Secondary audience | What changed | What stayed invariant | Verification evidence |
|---|---|---|---|---|---|

Cover:

- authority;
- task;
- title;
- evidence shown;
- evidence moved to table or note;
- terminology;
- annotation density;
- sequence;
- requested action;
- material limitation; and
- unsupported conclusions.

### 9. Decision brief

Write 600 to 900 words with:

- `## Audience and authority`;
- `## Finding`;
- `## Evidence`;
- `## Requested decision`;
- `## Action owner and next review`;
- `## Uncertainty or freshness`;
- `## Material limitation`; and
- `## Unsupported conclusion`.

### 10. Reproducibility check

Record:

- clean checkout or isolated folder;
- repository commit;
- operating system;
- software and package versions;
- exact commands;
- input checksums;
- output filenames;
- output row counts;
- visual inspection;
- validator results;
- tester; and
- date.

### 11. Critique response

Select one critique from Modules 01 through 13 or one instructor-approved review comment. Include:

- original problem;
- likely reader error;
- affected decision;
- repair;
- evidence that values remained stable;
- accessibility check;
- reviewer response; and
- remaining limit.

### 12. AI-use record

Document:

- tools and models;
- dates;
- work delegated;
- material prompts;
- outputs used;
- revisions;
- number checks;
- definition checks;
- source checks;
- cross-audience checks;
- accessibility checks;
- human decisions; and
- final responsibility.

If no generative AI was used, state that and describe the manual checks.

### 13. Oral defense

Submit an accessible PDF slide deck and written answers to the questions asked.

The presentation is no longer than eight minutes:

1. audience and decision;
2. source and population;
3. finding;
4. primary figure;
5. supporting question;
6. audience adaptation;
7. material limitation;
8. requested action; and
9. reproducibility and accessibility.

The question period is approximately seven minutes.

## Scaffold options

### Run

Use the released Module 13 reference case. Regenerate both figures, rewrite the decision brief in your own words, complete the records, and defend the stable evidence chain.

### Modify

Use the released source and values. Change the primary audience, secondary audience, title, annotations, sequence, or supporting figure while preserving every invariant.

### Author

Use the approved Checkpoint 2 capstone proposal and an approved open or synthetic source. Build the complete final package.

All paths use the same rubric and pass gates.

## Critique repairs

### C1: overstated causality

Rewrite the title, restore the source design, name the evidence required for a causal claim, and narrow the action.

### C2: hidden freshness

Restore the reporting window, release date, lag, historical-use label, and current-local-data requirement.

### C3: annotation misdirection

Remove dramatic unsupported annotation, restore threshold origin and freshness hierarchy, and state the validation action.

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Audience, authority, and decision | 10 | Two named audiences, realistic authority, one stable decision. |
| Finding and claim integrity | 15 | Finding, interpretation, recommendation, and action remain supported and separate. |
| Primary and supporting views | 15 | Primary carries the decision; supporting view answers a different necessary question. |
| Audience adaptation | 10 | Adaptable elements change while source, values, definitions, limits, and action remain stable. |
| Annotation and narrative sequence | 10 | Title and annotations guide attention without causal, freshness, or threshold distortion. |
| Reproducibility and provenance | 10 | Editable analysis, source record, transformation record, and clean-run evidence are complete. |
| Accessibility | 10 | Exact table, equivalent alternative, non-color cues, readable hierarchy, and delivery checks. |
| Clinical, ethical, and equity boundary | 10 | No causal, current, stigmatizing, subgroup, or unauthorized action claim. |
| Critique response and AI record | 5 | Repair and AI verification are specific, complete, and evidence-backed. |
| Oral defense | 5 | Learner answers source, method, limit, alternative, access, and action questions accurately. |
| Total | 100 |  |

## Pass conditions

All are required:

- score at least 80;
- two named audiences;
- one stable decision;
- one primary figure;
- supporting figure answers a different question or has an approved omission record;
- exact accessible table;
- equivalent text alternative;
- full source record;
- full transformation record;
- audience adaptation record;
- clean reproduction;
- material limitation;
- bounded action;
- complete AI record; and
- completed oral defense.

## Automatic return conditions

Return without grading if:

- source values differ between audience versions;
- the title claims cause without a causal design;
- a historical value is labeled current;
- a scenario trigger is called an official threshold;
- a descriptive peer value is called a benchmark;
- a reporting window, uncertainty, or material denominator is hidden;
- the requested action exceeds the evidence;
- the supporting figure repeats the primary question;
- the exact table or text alternative is missing;
- the source record or transformation record is incomplete;
- the figures cannot be regenerated;
- AI-assisted values or definitions are not verified;
- the learner cannot explain submitted code or prose; or
- real patient or restricted partner data appear in the public package.

## Reference answer boundary

For the released case, the supported decision is to authorize definition validation and current local data review. The 23-percent public OP-22 value is historical. The reference does not support a current performance judgment, causal attribution, staffing decision, care change, or intervention-effect claim.
