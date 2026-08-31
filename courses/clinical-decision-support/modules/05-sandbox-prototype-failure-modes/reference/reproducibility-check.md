# Reproducibility check

## Commands

```powershell
python build_sandbox.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

## Results

- Sandbox builder: pass with 31 cases, 184 prefetch resources, 61 trace events, and one silent failure detected.
- Byte comparison: pass for two independent sandbox builds.
- Existing-target refusal: pass.
- Workspace builder: pass with 324 immutable rows, 302 Module 04 files, 16 editable records, and 341 assembled files.
- Learner and reference manifests: byte-identical.
- Accepted Module 04 manifest: 285 rows, 60,302 bytes, and exact SHA-256.
- Nested Week 3 manifests: 29, 73, and 102 rows, totaling 204.
- All 31 declared sandbox tests: pass.
- All 20 invariants: pass.
- Silent-failure route: detected exactly once.
- Accessibility defect: detected and blocked exactly once.
- Reference validation: 2,649 checks pass.
- Learner validation: 2,558 checks pass while progression remains unavailable.
- Copied validator: pass.
- Deliberate failure routes: 20 rejected.

The checks establish package identity and declared fixture behavior only. They do not establish interoperability, safety, clinical utility, or production readiness.
