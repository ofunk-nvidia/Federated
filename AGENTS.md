# Agent instructions

These instructions apply to the entire repository. They are deliberately kept outside the executive-facing `README.md`.

## Language

All agent output must be in English, even when the user writes in German. This includes plans, questions, explanations, documentation, comments, reports, commit messages, issues, and pull requests. Preserve original-language quotations only when necessary and explain them in English.

## Repository purpose

This is a public, documentation-only reference architecture and GitHub-native presentation. Maintain its explanation of tools, workflows, decisions, risks, and evidence. Do not turn it into an implementation repository.

## Required reading

Before changing the repository, read:

1. `README.md`
2. `PUBLICATION_POLICY.md`
3. `OPEN_SOURCE_BASELINE.md`
4. `CONTRIBUTING.md`
5. `THIRD_PARTY_NOTICES.md`

## Operating rules

- Add only Markdown, Mermaid, project-owned visuals, or small synthetic non-operational fragments permitted by the publication policy.
- Never add or process client, engagement, employer, partner, personal, confidential, privileged, or production material.
- Never add datasets, source repositories, model weights, adapters, checkpoints, embeddings, prompts or outputs from engagements, training runs, executable POCs, credentials, deployment configuration, or customer deliverables.
- Reference open-source tools by canonical link and verified licence; do not vendor their code here.
- Treat public availability, downloadable weights, and source availability as insufficient evidence of an open-source licence.
- Use official primary sources for technical claims and record exact versions when recommending implementation dependencies.
- Do not describe NVIDIA NIM or NeMo Microservices as part of the strict open-source baseline.
- Do not claim that federated learning or open source eliminates copyright, competition, confidentiality, privacy, trade-secret, contractual, or security risk.
- Keep GitHub as the single source of truth and use GitHub-renderable Markdown, Mermaid, SVG, or reviewed raster visuals. Do not introduce PDF or PowerPoint deliverables.
- Keep changes small, reviewable, and reversible. Preserve an executive-readable narrative in `README.md`; put agent mechanics and contribution controls in their dedicated files.
- Record incorporated external excerpts or assets in `THIRD_PARTY_NOTICES.md` before merge.
- Run `python scripts/check_public_content.py` after every change. A passing scan never replaces human provenance, licence, confidentiality, privacy, and trademark review.

## Stop conditions

Stop and request explicit approval before accessing a real tenant, repository, or customer environment; accepting model-specific terms; using non-public material; incurring cost; deploying infrastructure; or creating a separate implementation repository.

Any POC or customer implementation must live in a separate, explicitly approved private repository and isolated environment. Only reviewed, sanitised, non-client-specific findings may return here.

## Documentation workflow

1. Inspect the current repository and applicable governance files.
2. Verify time-sensitive technical and licence claims against primary sources.
3. Update the smallest coherent documentation unit.
4. Prefer compact diagrams and tables when they materially improve understanding.
5. Run the publication gate.
6. Report the changed files, sources, assumptions, and residual risks.

## Suggested agent prompts

For a documentation update:

> Update only the public reference architecture. Verify primary-source links, tool licences, workflow descriptions, risks, and GitHub-renderable visuals. Do not add or run a POC, customer material, datasets, model artefacts, deployment configuration, or copied third-party content. Run the publication gate and report every material source and assumption.

For a separate POC proposal:

> Draft a self-contained plan for a new private POC repository using synthetic data only. Include approvals, licences, isolation tests, leakage tests, exit criteria, and repository boundaries. Do not create implementation files or execute training in this public reference repository.

