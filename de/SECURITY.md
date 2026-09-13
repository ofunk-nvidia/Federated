# Repository-Sicherheit

[Überblick](README.md) · [Architektur](../docs/de/architecture.md) · [Deployment](../docs/de/deployment.md) · [Workflow](../docs/de/workflow.md) · [Toolchain](../docs/de/toolchain.md) · [Governance](../docs/de/governance.md) · [English](../SECURITY.md)

## Unterstützte Inhalte

Unterstützt werden ausschließlich der aktuelle Default Branch und das daraus erzeugte GitHub-Pages-Deployment. Dies ist ein reines Dokumentations-Repository; es enthält keine unterstützte Produktivsoftware oder Kundenimplementierung.

## Meldung eines Sicherheitsproblems

Credentials, personenbezogene Daten, vertrauliches Material, Exploit-Details oder vermutete Kundeninformationen gehören niemals in ein öffentliches Issue, eine Discussion, einen Pull Request, Commit oder Fork.

Wenn aktiviert, ist GitHubs Private Vulnerability Reporting im Security-Tab zu verwenden. Ist dieser Kanal nicht verfügbar, wird der Repository-Inhaber über einen bestehenden vertrauenswürdigen privaten Kanal kontaktiert; zunächst werden nur die minimal nötigen Informationen zur Einrichtung eines sicheren Meldewegs offengelegt. Nicht sensitive Dokumentationsfehler dürfen als normales Issue oder Pull Request gemeldet werden.

## Beitragsgrenze

- Externe Beitragende arbeiten aus einem Fork und schlagen Änderungen über einen Pull Request vor.
- Für einen Dokumentationsbeitrag wird kein direkter Schreibzugriff vergeben.
- Der Repository-Inhaber ist CODEOWNER für sämtliche Inhalte und die Kontrolldateien selbst.
- Pull-Request-Workflows nutzen ein Read-only-Token, keine Repository Secrets und ephemere GitHub-hosted Runner.
- Pages wird erst deployt, nachdem vertrauenswürdiger Inhalt `main` erreicht hat.
- Drittanbieter-Actions sind auf vollständige unveränderliche Commit-SHAs fixiert.
- Ein bestandenes automatisches Gate autorisiert weder Merge noch Veröffentlichung.

## Erforderliche GitHub-Einstellungen

Der Repository-Inhaber pflegt ein aktives Ruleset für den Default Branch mit Pflicht-Pull-Requests, mindestens einer Freigabe, CODEOWNER-Review, Verwerfen veralteter Freigaben, Freigabe des letzten prüfbaren Pushes, Auflösung von Conversations, Publication-Statuscheck, Lösch- und Force-Push-Schutz sowie ohne regulären Bypass. Workflows aus Fork-Pull-Requests benötigen Inhaberfreigabe und erhalten Read-only-Berechtigungen. Private Vulnerability Reporting und Dependabot Alerts sind aktiviert.

Diese Einstellungen sind die Enforcement-Kontrollen. Diese Datei und `CODEOWNERS` dokumentieren das Ziel, ersetzen aber kein GitHub-Ruleset.

## Sicherheitsvorfall

Gelangen unzulässige Informationen in die Git-Historie, werden Pages und weitere Veröffentlichung gestoppt, Credentials sofort widerrufen, minimale Incident-Evidenz gesichert, Forks/Caches/Logs bewertet, das Material aus dem aktuellen Tree entfernt, ein koordiniertes History-Rewrite geprüft und das Gate vor Wiederaufnahme verbessert.
