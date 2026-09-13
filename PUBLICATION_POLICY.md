# Publication and Open-Source Policy

## Purpose

This repository is a documentation-only reference architecture and GitHub-native presentation. It may contain only material that can be lawfully published and reused for that purpose. It is not an implementation, POC execution, training, deployment, or customer-delivery repository.

Open source reduces uncertainty but does not remove legal or security obligations. Publicly accessible material without a clear licence is not open source. An OSI-approved software licence does not by itself remove privacy, confidentiality, trademark, export-control, database-right, or contractual restrictions.

## Default rule

**Unclear origin, ownership, licence, confidentiality, or purpose means `DENY`.**

Do not commit a source first and investigate later. Complete the review before the content enters Git history.

## Allowed material

- Original Markdown, Mermaid diagrams, and project-owned visuals created for this public repository by an authorised contributor.
- Small synthetic pseudocode and non-operational configuration fragments created without confidential or restricted source material.
- Links to open-source tools whose exact project, version, and licence are identified; linked software is not thereby incorporated.
- Brief, necessary excerpts from openly licensed documentation, with attribution and reuse conditions recorded.
- Public facts quoted or summarised within applicable limits and linked to their primary source.
- Generated content only when the inputs, generator terms, output rights, and provenance are documented.

## Prohibited material

- Client, engagement, employer, partner, or internal company data.
- Customer-project execution, deliverables, workspaces, or implementation repositories.
- Confidential, restricted, pre-release, privileged, export-controlled, or contractually limited information.
- Personal data that is not strictly necessary and explicitly approved for publication.
- Credentials, tokens, private keys, certificates, connection strings, internal hosts, or production identifiers.
- Source code, documents, screenshots, logs, prompts, outputs, model updates, embeddings, or benchmarks taken from customer environments.
- Publicly visible repositories or webpages without an explicit compatible licence.
- Third-party material whose notice, attribution, source-disclosure, copyleft, patent, or trademark obligations have not been assessed.
- Model weights or datasets without a verified licence and documented training/use restrictions.
- Any dataset, model weight, adapter, checkpoint, embedding index, training artefact, executable POC, production configuration, or vendored third-party source code, even if openly licensed. Those belong in a separate approved repository.
- Real company or customer names in synthetic scenarios unless the reference is a necessary public fact.

## Initial licence allowlist

The initial low-complexity allowlist for software contributions is:

- Apache-2.0
- MIT
- BSD-2-Clause
- BSD-3-Clause

CC0-1.0 and CC-BY-4.0 may be accepted for data or documentation after attribution review. Other licences, including copyleft licences, require a documented compatibility decision before use. “No licence”, custom terms, research-only terms, non-commercial terms, and source-available licences are not approved by default.

The allowlist is a project policy, not a statement that other open-source licences are invalid.

## Required provenance record

Every external asset or excerpt incorporated into the repository must be recorded in `THIRD_PARTY_NOTICES.md` before merge with:

- source name and canonical URL;
- immutable commit, release, or dataset version;
- licence and licence URL;
- files or artefacts used;
- intended project use;
- modifications performed;
- required notices or attribution;
- reviewer and review date.

## Publication gate

Every pull request must satisfy all of these conditions:

1. The contributor completed the pull-request publication checklist.
2. The automated scanner found no known secret pattern or prohibited file type.
3. A human reviewed provenance, licence compatibility, confidentiality, and personal data.
4. External content appears in `THIRD_PARTY_NOTICES.md`.
5. Synthetic material is labelled synthetic and contains no real identifiers.
6. Visuals include source and licence metadata or are original project assets.
7. Generated content records its relevant inputs and review status.
8. A reviewer confirms that the change does not imply official NVIDIA or customer endorsement.
9. A reviewer confirms that the change remains documentation-only and contains no POC or customer-delivery artefact.

Automated scanning is a minimum control. Passing it does not prove that publication is safe.

## Incident response

If prohibited content enters Git history:

1. Stop publication and further distribution.
2. Revoke exposed credentials immediately.
3. Notify the repository owner and the relevant security or legal contact.
4. Remove the content from the current tree and assess history rewriting.
5. Treat forks, caches, Actions logs, releases, and downloaded copies as potentially exposed.
6. Record the incident and improve the detection rule.

## Review cadence

Review this policy whenever the repository adds a new data source, model, licence, external action, publication channel, or customer-facing use case.
