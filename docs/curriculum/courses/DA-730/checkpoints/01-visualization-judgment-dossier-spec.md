# DA-730 Checkpoint 1: visualization judgment dossier

- Checkpoint ID: DA-730-CP1
- Course: DA-730, Clinical data visualization and decision storytelling
- Due: end of instructional week 3
- Modules included: 01 through 06
- Checkpoint version: 0.1.0
- Commons release: 0.17.1
- Learner workload: included in the module hours for Modules 01 through 06
- Runnable package: `courses/data-visualization/checkpoints/01-visualization-judgment-dossier/`

## 1. Purpose

This checkpoint tests whether a learner can make and defend four different visualization choices before beginning the larger applied portfolio. It joins work from Modules 01 through 06 into one dossier for a named healthcare audience.

The learner must show four kinds of judgment:

1. choose an encoding that fits a comparison task;
2. show a distribution when a summary could hide a consequential subgroup or tail;
3. distinguish a count, crude rate, and adjusted rate while keeping the denominator visible;
4. show uncertainty and unavailable values without claiming more separation than the source supports.

The checkpoint is not four polished images placed in a folder. The figures, source files, provenance, critique, accessible alternatives, and decision brief form one submission.

## 2. Decision and audience

The learner names one primary reader who could reasonably use all four displays. Acceptable readers include a clinical service leader, quality director, population-health program director, hospital analyst, or public-health partner.

The dossier answers this question:

> What should the named reader compare, investigate, or decide after seeing these four displays, and what must remain uncertain?

The four module cases may retain their original local decision owners. The final brief must explain how the evidence demonstrates the learner's readiness to advise the named checkpoint reader.

## 3. Competencies assessed

| Module | Evidence carried into the checkpoint | Checkpoint use |
|---|---|---|
| 01. Encoding and the grammar of graphics | Variable, mark, and channel choices | Explain why position, length, area, color, or text fits the reader task. |
| 02. Perception and visual accuracy | Perception-test results and error patterns | Reject an encoding the reader would decode less accurately. |
| 03. Chart selection in practice | Comparison chart and selection matrix | Supply `comparison.png` and the dossier selection rationale. |
| 04. Distributions versus summaries | Encounter-level distribution and summary audit | Supply `distribution.png` and identify the hidden tail or subgroup. |
| 05. Rates, denominators, and adjustment | County rate comparison with denominator context | Supply `rate.png` and separate outreach scale from comparative burden. |
| 06. Uncertainty, variation, and small numbers | Interval, status, and denominator display | Supply `uncertainty.png` and state what the evidence does not separate. |

## 4. Required folder contract

The default R path uses these exact names:

```text
checkpoint-1/
  README.md
  selection-matrix.md
  figures/
    comparison.png
    distribution.png
    rate.png
    uncertainty.png
  analysis/
    comparison.R
    distribution.R
    rate.R
    uncertainty.R
  source-records/
    comparison-source.yml
    distribution-source.yml
    rate-source.yml
    uncertainty-source.yml
  critique-and-repair.md
  accessibility-check.md
  decision-brief.md
  ai-use.md
```

An approved alternative tool may replace an `.R` file with `.py`, `.ipynb`, `.twb`, `.pbix`, or another editable source file. The base name must stay the same. For example, `rate.py` may replace `rate.R`; `analysis-final.py` may not.

Do not rename the four PNG files or the four source records. The checkpoint validator uses these names to connect each figure to its analysis and provenance.

## 5. Figure contract

Each figure must be a PNG at least 600 pixels wide and 400 pixels high. Text must remain readable at normal document size. Each figure needs a title or nearby heading that identifies the measure, population, geography, and period when those fields apply.

### `comparison.png`

- Starting evidence: Module 03 `01-comparison-dot-plot.png`.
- Public source: CMS Patient survey (HCAHPS) hospital data.
- Required task: compare hospitals without implying that the displayed percentage is an overall quality score.
- Required encoding defense: explain why the chosen position or length encoding is more accurate for the task than one rejected alternative.
- Required limit: the display is descriptive and does not establish a statistically meaningful difference or cause.

### `distribution.png`

- Starting evidence: Module 04 `03-density-by-disposition.png`.
- Data: synthetic emergency-department encounters calibrated to the public CMS OP_18b time scale.
- Required task: reveal a tail, mode, pathway, or subgroup hidden by a valid summary.
- Required comparison: name the summary that would have hidden the finding.
- Required limit: the synthetic encounters do not describe an actual hospital or estimate an intervention effect.

### `rate.png`

- Starting evidence: Module 05 `03-adjusted-with-denominator.png`.
- Public sources: CDC PLACES, Census ACS population context, and Census generalized county boundaries when a map is used.
- Required task: compare age-adjusted adult diabetes prevalence while keeping the population or denominator context visible.
- Required distinction: state which question calls for the adjusted rate and which separate question calls for a modeled count.
- Required limit: PLACES values are small-area model estimates, not direct county survey estimates or observed diagnoses.

### `uncertainty.png`

- Starting evidence: Module 06 `02-interval-caterpillar.png`.
- Public source: CMS Unplanned Hospital Visits and official footnotes.
- Required task: show point estimates, source intervals, the national reference, and unavailable or too-few status without turning the display into a league table.
- Required interpretation: distinguish a point rank from source evidence of comparison.
- Required limit: displayed interval overlap is descriptive, not a pairwise hypothesis test or proof of equivalence.

Learners may revise the starting figures. A revision must preserve the source values and the module's statistical claim. The analysis file must regenerate the submitted PNG.

## 6. `README.md` contract

The dossier README is the reproduction and navigation record. It must contain these headings:

- `# Checkpoint 1: visualization judgment dossier`
- `## Audience and decision`
- `## Findings`
- `## Reproduce this dossier`
- `## Folder map`

Under `Reproduce this dossier`, list the software and package versions, working directory, exact commands, and expected output filenames. A new user starting from a clean course checkout must be able to regenerate every figure without guessing where the data live.

Under `Findings`, give one sentence for each figure. The sentence must say what changed or differed, for whom or where, and what the reader should inspect or decide next.

## 7. `selection-matrix.md` contract

The selection matrix contains exactly one row for each required figure and these columns:

| Figure | Decision | Reader task | Data structure | Display chosen | Alternative rejected | What could be hidden |
|---|---|---|---|---|---|---|
| `comparison.png` | | | | | | |
| `distribution.png` | | | | | | |
| `rate.png` | | | | | | |
| `uncertainty.png` | | | | | | |

Each row must name a concrete decision. Terms such as "better communication" or "show the data" are too general. The rejected alternative must be plausible, and the learner must explain why it is weaker for this reader task.

The matrix must use evidence from the Module 02 perception exercise at least once. The evidence may be a measured learner error pattern or the supplied perception evidence, but it cannot be a claim that one chart type is universally best.

## 8. Analysis contract

Each editable analysis file must:

1. read a committed course data file or documented public-source extract;
2. stop with a clear error when the required file or columns are missing;
3. preserve missing, unavailable, and suppressed values according to the source record;
4. make transformations visible in code;
5. write the matching figure to `figures/` with the exact required name;
6. run without manual chart editing after the script starts.

The four files may share ordinary package imports. They may not depend on an uncommitted local spreadsheet, copied patient record, hidden Tableau extract, or manual color and label edits made after rendering.

## 9. Source-record contract

Each source record uses these top-level keys:

```yaml
publisher: "..."
landing_page: "https://..."
retrieved_at: "YYYY-MM-DD"
released: "YYYY-MM-DD or source release label"
data_path: "repository-relative path"
analysis_path: "analysis/comparison.R"
figure_path: "figures/comparison.png"
sha256: "64 lowercase hexadecimal characters"
transformations:
  - "..."
known_limits:
  - "..."
```

Use the checksum of the released teaching table read by the analysis. If the analysis joins more than one file, list the other files and checksums under additional descriptive keys. Keep the required top-level `sha256` for the main analytic input.

The four records must contain at least two distinct public landing pages. Module 04's synthetic teaching data retain the CMS calibration page and must say clearly which values are synthetic.

## 10. `critique-and-repair.md` contract

This file must contain:

- `## Original problem`
- `## Evidence from Modules 01 through 06`
- `## Repair`
- `## Remaining limit`

The learner selects one flawed display from Modules 01 through 06 or documents an instructor-approved public example. The critique must identify the reader error the display invites, not only a preference about appearance. The repair may become one of the four submitted figures.

The learner must state what the repair still cannot answer. A repair that changes the data, removes inconvenient unavailable values, or implies unsupported certainty does not pass.

## 11. `accessibility-check.md` contract

This file must contain:

- `## Color and contrast`
- `## Redundant cues`
- `## Text alternatives`
- `## Reading order and labels`
- `## Checks completed`

For each figure, record:

- whether meaning survives grayscale;
- which labels, shapes, line types, or positions carry meaning without color;
- the text alternative or long description location;
- whether abbreviations, units, and reading order are clear;
- the tool or manual method used for the check and the result.

Module 07 teaches the full accessibility workflow. At Checkpoint 1, a learner must identify and repair obvious barriers. Color alone, a filename used as alt text, or a statement that the chart "looks accessible" does not pass.

## 12. `decision-brief.md` contract

The brief must contain:

- `## Audience`
- `## Finding`
- `## Decision`
- `## Uncertainty`
- `## Material limitation`

The brief is 500 to 900 words. It may cite all four cases as evidence of visualization judgment, but it must end with one concrete action, comparison, investigation, or deferral for the named reader. If the evidence does not support action, the decision may be to collect a named missing measure or avoid a false comparison.

The brief may not combine the four populations into one clinical claim. HCAHPS hospital responses, synthetic emergency visits, county diabetes estimates, and heart-failure readmission estimates answer different questions.

## 13. `ai-use.md` contract

This file must contain:

- `## Tool and model`
- `## Work delegated`
- `## Prompts or instructions`
- `## Verification`
- `## Human decisions`

If no generative AI was used, state that under `Tool and model` and explain how the analysis and prose were checked. If AI was used, identify the tool, the work assigned to it, and the records kept. The learner remains responsible for every source value, transformation, label, accessibility statement, and decision claim.

## 14. Reproducible assembly

From the repository root, assemble the starter dossier with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/01-visualization-judgment-dossier/assemble_checkpoint.ps1 -Target checkpoint-1
```

If `Rscript` is not on the command path, supply its full path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/01-visualization-judgment-dossier/assemble_checkpoint.ps1 -Target checkpoint-1 -RscriptPath "C:\Path\To\Rscript.exe"
```

The assembler refuses to write into a nonempty target. It renders all four released module cases, copies the exact figure, analysis, and source-record names, and adds the six learner writing templates.

The learner then completes the prose, revises analysis and figures when needed, and runs:

```powershell
python courses/data-visualization/checkpoints/01-visualization-judgment-dossier/validate_checkpoint.py checkpoint-1
```

The validator checks structure, required headings, source fields, checksums, figure dimensions, editable analysis, public-source diversity, and unfinished placeholders. It does not grade whether a clinical interpretation is sound.

## 15. Rubric

| Criterion | Weight | Pass evidence |
|---|---:|---|
| Decision and chart selection | 20% | Every display fits a named decision, reader task, and data structure; a plausible alternative is rejected with evidence. |
| Statistical and clinical interpretation | 25% | The learner distinguishes summaries from distributions, counts from rates, adjustment from observation, and point ranks from evidence of comparison. |
| Reproducibility and provenance | 20% | All four figures regenerate from editable sources; all source records identify the released input, checksum, transformation, and limit. |
| Critique and repair | 10% | The learner identifies a likely reader error, repairs it without changing the evidence, and names the remaining limit. |
| Accessibility | 15% | Meaning does not rely on color alone; labels, reading order, and text alternatives preserve the finding. |
| Decision brief and AI accountability | 10% | The brief supports one concrete next step without joining unrelated populations; AI use and human verification are recorded. |

Passing requires at least 80 percent overall and a pass in every gate below. A high total score cannot compensate for a missing source, inaccessible display, or unsupported clinical claim.

## 16. Noncompensable pass gates

- All four PNG files open and meet the minimum dimensions.
- Each figure has a matching editable analysis file and source record.
- At least two distinct approved public landing pages are recorded.
- Missing, unavailable, and suppressed source values are not silently imputed.
- The distribution is labeled synthetic and does not claim to describe a real hospital.
- The rate figure distinguishes modeled count, crude prevalence, and age-adjusted prevalence.
- The uncertainty figure does not turn point rank or interval overlap into a pairwise significance claim.
- Every figure has a text alternative and does not rely on color alone.
- The decision brief names the audience, finding, decision, uncertainty, and material limitation.
- The AI-use record is complete, including when no AI was used.
- The submission contains no patient-level clinical records or restricted partner data.

## 17. Instructor review and release decision

The instructor records one disposition:

- `pass`: all gates pass and the overall score is at least 80 percent;
- `revise`: the work is recoverable, but one or more gates or scoring criteria remain incomplete;
- `refer`: the work has a source, privacy, academic-integrity, or patient-data concern that requires program review.

The instructor should run the validator before reading the narrative. A passing validator means the package is structurally complete. It does not replace review of the source interpretation, clinical meaning, accessibility, or decision claim.

Checkpoint 1 closes the fundamentals portion of DA-730. Module 07 begins the applied portfolio and makes the accessibility requirements binding for every later display.
