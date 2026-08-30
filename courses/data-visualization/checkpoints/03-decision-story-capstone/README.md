# Final checkpoint: decision-story capstone

This package assembles and validates the DA-730 final submission. It reuses the released Module 12 data and Module 13 evidence design, then creates a portable starter with two figures, one exact table, editable analysis, pinned data, learner records, and an oral-defense outline.

The full contract is in [the final checkpoint specification](../../../../docs/curriculum/courses/DA-730/checkpoints/03-decision-story-capstone-spec.md).

## Due date

Submit on the official last day of the assigned MGH Institute half-term. The curriculum uses a 7.5-week planning model, but the official 2026-2027 half-terms span 49 to 52 elapsed days. Do not replace the official date with a generic "Week 7.5" date.

Official calendar: https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

## Assemble the reference starter

Run from the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/03-decision-story-capstone/assemble_checkpoint.ps1 -Target final-capstone
```

If `Rscript` is not on the command path, pass its full path with `-RscriptPath`.

The assembler:

1. refuses a nonempty target;
2. copies the three pinned Module 12 CSV files;
3. copies editable analysis and learner records;
4. renders the executive and technical figures;
5. writes the exact three-row table; and
6. leaves the learner and reviewer work visibly unfinished.

## Final folder

```text
final-capstone/
  README.md
  decision-brief.md
  figure-primary.png
  figure-supporting.png
  accessible-table.csv
  alt-text.md
  analysis/
    analysis.R
  data/
    ma_ed_public_reporting_dashboard_2026.csv
    ed_dashboard_measure_dictionary_2026.csv
    cms_ma_ed_dashboard_source_2026.csv
  source-record.yml
  transformation-record.md
  audience-adaptation-record.md
  reproducibility-check.md
  critique-response.md
  ai-use.md
  review-disposition.md
  defense/
    slides.pdf
    slides-outline.md
    questions-and-responses.md
```

The learner exports `defense/slides.pdf` from the supplied outline or another accessible slide source. The assembler does not create a false completed defense.

## Reproduce the evidence

Inside the assembled folder:

```powershell
Rscript analysis/analysis.R --output .
```

The command regenerates only:

- `figure-primary.png`;
- `figure-supporting.png`; and
- `accessible-table.csv`.

It does not overwrite learner prose, review records, or defense files.

## Validate the completed release

```powershell
python courses/data-visualization/checkpoints/03-decision-story-capstone/validate_checkpoint.py final-capstone
```

Test the validator itself with:

```powershell
python courses/data-visualization/checkpoints/03-decision-story-capstone/validate_checkpoint.py --self-check
```

The starter is expected to fail completed-folder validation. A passing folder must include completed learner records, an accessible PDF defense deck, written defense answers, an instructor disposition, a passing score, and a passed oral defense.

## Stable evidence boundary

The reference supports authorization of a local definition and current-data review. It does not support a current performance rating, causal attribution, staffing change, care change, or intervention-effect claim.
