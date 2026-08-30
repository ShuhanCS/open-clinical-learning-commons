# Reproducibility check

- Accepted component files: `78`
- Module 01 workspace-manifest SHA-256: `4f57b0bbf3e510967c5e42691eee990ce523974b7f6ea877f15f46903aa8c147`
- Module 02 workspace-manifest SHA-256: `9d78f888753b39797ad421d2576eef377ba0bc01fcca02d9ef3c9da388057c10`
- Module 03 workspace-manifest SHA-256: `067e1953d7fe7bcfaf878880bef2edf44788b846f71c478282ebe34f1a5d4d52`
- Reference assembly: `two builds match byte for byte`
- Learner assembly: `complete and prompted`
- Existing target: `rejected`
- Candidate mutation: `rejected`

The checkpoint assembles accepted module workspaces without recomputing their evidence. Each nested manifest and the checkpoint candidate manifest protect the handoff.
