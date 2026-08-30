# Agent prompt constraints

Every material agent task states:

- task ID and decision question;
- exact allowed files;
- data class;
- bounded action;
- required output fields;
- prohibited files and actions;
- prohibited clinical, causal, operational, approval, and deployment claims;
- assertions or evidence checks required;
- independent verification route;
- named human owner; and
- stop condition.

Only public aggregate and documented synthetic evidence in this release may be shared. Do not share PHI, identifiable records, workplace-confidential material, restricted licensed data, secrets, or credentials.

An agent may propose tests or critique a claim. It may not approve an artifact, classify a risky data source, waive a gate, invent a citation, or sign for a person. Claims without available evidence are rejected and logged.
