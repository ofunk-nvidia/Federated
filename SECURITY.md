# Repository security

[Overview](README.md) · [Architecture](docs/en/architecture.md) · [Deployment](docs/en/deployment.md) · [Workflow](docs/en/workflow.md) · [Toolchain](docs/en/toolchain.md) · [Governance](docs/en/governance.md) · [Deutsch](de/SECURITY.md)

## Supported content

Only the current default branch and its generated GitHub Pages deployment are maintained. This is a documentation-only repository; it contains no supported production software or customer implementation.

## Reporting a security concern

Do not put credentials, personal data, confidential material, exploit details, or suspected customer information in a public issue, discussion, pull request, commit, or fork.

Use GitHub private vulnerability reporting from the repository Security tab when it is enabled. If that channel is unavailable, contact the repository owner through an existing trusted private channel and disclose only the minimum information needed to establish a secure reporting route. Non-sensitive documentation errors may use a normal issue or pull request.

## Contribution boundary

- External contributors work from a fork and propose changes through a pull request.
- No contributor receives direct write access merely to submit documentation.
- The repository owner is CODEOWNER for all content and for the control files themselves.
- Pull-request workflows use a read-only token, no repository secrets, and GitHub-hosted ephemeral runners.
- Pages deployment runs only after trusted content reaches `main`.
- Third-party actions are pinned to full immutable commit SHAs.
- A passing automated gate never authorises merge or publication.

## Required GitHub settings

The repository owner maintains an active default-branch ruleset with pull requests required, at least one approval, CODEOWNER review, stale-approval dismissal, approval of the latest reviewable push, conversation resolution, the publication status check, deletion protection, force-push protection, and no routine bypass. Fork pull-request workflows require owner approval and receive read-only workflow permissions. Private vulnerability reporting and Dependabot alerts are enabled.

These settings are enforcement controls. This file and `CODEOWNERS` document intent but do not replace the GitHub ruleset.

## Security incident

If prohibited information enters Git history, stop Pages publication, revoke any credential immediately, preserve minimal incident evidence, assess forks/caches/logs, remove the material from the current tree, decide whether coordinated history rewriting is necessary, and improve the gate before resuming publication.
