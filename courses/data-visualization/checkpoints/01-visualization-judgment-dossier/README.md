# Checkpoint 1: visualization judgment dossier

This package assembles and checks the DA-730 Week 3 submission. It uses released work from Modules 03 through 06 to create four figures with matching editable analysis and source records. Learners then complete the decision, critique, accessibility, and AI-use documents.

The full contract is in [the checkpoint specification](../../../../docs/curriculum/courses/DA-730/checkpoints/01-visualization-judgment-dossier-spec.md).

## Assemble a starter dossier

Run from the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/01-visualization-judgment-dossier/assemble_checkpoint.ps1 -Target checkpoint-1
```

If `Rscript` is not on the command path, pass its full path with `-RscriptPath`.

The target must be absent or empty. The script does not overwrite existing work.

## Complete the submission

Replace every bracketed instruction in the six Markdown templates. Revise the copied analysis and rendered figures when your argument requires it. Keep the four base names connected:

| Figure | Analysis | Source record |
|---|---|---|
| `figures/comparison.png` | `analysis/comparison.R` | `source-records/comparison-source.yml` |
| `figures/distribution.png` | `analysis/distribution.R` | `source-records/distribution-source.yml` |
| `figures/rate.png` | `analysis/rate.R` | `source-records/rate-source.yml` |
| `figures/uncertainty.png` | `analysis/uncertainty.R` | `source-records/uncertainty-source.yml` |

Approved alternative tools may replace an `.R` file with `.py`, `.ipynb`, `.twb`, or `.pbix`. Keep the base name.

## Validate the completed dossier

```powershell
python courses/data-visualization/checkpoints/01-visualization-judgment-dossier/validate_checkpoint.py checkpoint-1
```

Test the validator itself with:

```powershell
python courses/data-visualization/checkpoints/01-visualization-judgment-dossier/validate_checkpoint.py --self-check
```

The structural check does not grade clinical reasoning. An instructor still reviews the interpretation, decision, source fit, and accessibility.
