# Reference reproducibility check

- Date: 2026-08-30.
- Platform: Windows.
- Python: 3.12.10.
- Renderer dependencies: Matplotlib 3.10.9 and Pillow 11.1.0.
- Four input fingerprints verified: pass.
- Renderer self-check and existing-target refusal: pass.
- Validator self-check: pass.
- Three exact tables reproduced byte for byte: pass.
- Six figure exports reproduced byte for byte in the pinned environment: pass.
- Figure registry and text alternatives reproduced byte for byte: pass.
- Standalone copied-package render using local `data/` inputs: pass.
- PNG dimensions, DPI metadata, and SVG dimensions: pass.
- Grayscale, 50-percent width, 200-percent zoom, and reading-order review: pass.
- Incomplete learner submission rejected: pass.
- macOS reproduction: pending.
- Linux reproduction: pending.

```powershell
python render_figures.py --target <new-output-directory>
python validate_figures.py .
```
