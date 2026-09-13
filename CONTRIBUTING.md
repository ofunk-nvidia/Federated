# Contributing

Contributions are welcome when they satisfy [PUBLICATION_POLICY.md](PUBLICATION_POLICY.md).

External contributors use a fork and submit a pull request. Do not request or grant direct write access merely to contribute documentation. Security-sensitive reports follow [SECURITY.md](SECURITY.md) and must never be placed in a public issue or pull request.

Before opening a pull request:

1. Add documentation, Mermaid, project-owned visuals, or small synthetic non-operational fragments only.
2. Reference open-source tools by canonical link, version, and licence; do not vendor their code here.
3. Record every incorporated external excerpt or asset in `THIRD_PARTY_NOTICES.md`.
4. Run `python scripts/check_public_content.py`.
5. Confirm that no client, employer, partner, personal, confidential, or credential data is present.
6. Confirm that the change contains no dataset, model artefact, POC implementation, production configuration, or customer-project material.
7. Explain whether AI helped create the contribution and which inputs were used.
8. Submit a small pull request with one clear purpose.
9. If the presentation configuration or navigation changed, run `bash scripts/build_pages.sh` after installing `requirements-pages.txt` and review both language paths.
10. Wait for the publication check and applicable review: external contributions require `ofunk-nvidia` CODEOWNER approval; owner-authored changes require the Codex publication review to be recorded in the pull request. Never ask a maintainer to bypass the default-branch ruleset.

For an owner-authored change initiated in Codex, the owner's instruction authorises Codex to complete the review, record its evidence in the pull request, merge through the authenticated `ofunk-nvidia` connector after checks pass, and verify `main` and Pages. GitHub self-approval is not required. By contributing, you confirm that you have the right to submit the material under this repository’s licence. Automation or Codex review does not resolve a flagged legal, security, privacy, or licence uncertainty; such a question requires an appropriately qualified human decision.

## Repository and Pages synchronisation

The versioned Markdown is the single source of truth. GitHub Pages is generated from the same commit by `.github/workflows/pages.yml`; generated directories are never edited or committed. A Pages build or deployment failure is a publication failure and must be resolved before the public site is considered current.

