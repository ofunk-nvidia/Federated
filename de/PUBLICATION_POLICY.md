# Veröffentlichungs- und Open-Source-Policy

## Zweck

Dieses Repository ist eine reine Dokumentations-Referenzarchitektur und GitHub-native Präsentation. Es darf nur Material enthalten, das für diesen Zweck rechtmäßig veröffentlicht und weiterverwendet werden kann. Es ist kein Implementierungs-, POC-Ausführungs-, Trainings-, Deployment- oder Kundenprojekt-Repository.

Open Source reduziert Unsicherheit, beseitigt aber keine rechtlichen oder sicherheitsbezogenen Pflichten. Öffentlich abrufbares Material ohne eindeutige Lizenz ist nicht Open Source. Auch eine OSI-anerkannte Softwarelizenz beseitigt nicht automatisch Datenschutz-, Geheimhaltungs-, Marken-, Exportkontroll-, Datenbank- oder Vertragspflichten.

## Grundregel

**Unklare Herkunft, Rechteinhaberschaft, Lizenz, Vertraulichkeit oder Zweckbindung bedeutet `DENY`.**

Eine Quelle wird vor der Aufnahme geprüft. Eine nachträgliche Prüfung genügt nicht, weil der Inhalt dann bereits in der Git-Historie liegen kann.

## Zulässiges Material

- Eigene Markdown-Texte, Mermaid-Diagramme und projektinterne Visuals eines berechtigten Contributors.
- Kleine synthetische Pseudocode- und nicht operative Konfigurationsfragmente ohne vertrauliche oder beschränkte Quellen.
- Links auf Open-Source-Werkzeuge mit genauer Projekt-, Versions- und Lizenzangabe; die verlinkte Software wird dadurch nicht übernommen.
- Kurze erforderliche Auszüge aus offen lizenzierter Dokumentation mit erfüllter Attribution.
- Öffentliche Fakten mit Primärquelle und innerhalb zulässiger Zitat- und Nutzungsgrenzen.
- Generierte Inhalte nur bei dokumentierten Inputs, Generatorbedingungen, Ausgaberechten und Provenienz.

## Verbotenes Material

- Kunden-, Mandats-, Arbeitgeber-, Partner- oder interne Unternehmensdaten.
- Ausführung, Deliverables, Workspaces oder Implementierungs-Repositories von Kundenprojekten.
- Vertrauliche, beschränkte, vorab veröffentlichte, privilegierte, exportkontrollierte oder vertraglich begrenzte Informationen.
- Personenbezogene Daten ohne zwingende Erforderlichkeit und ausdrückliche Veröffentlichungsfreigabe.
- Zugangsdaten, Tokens, private Schlüssel, Zertifikate, Connection Strings, interne Hosts oder produktive Identifikatoren.
- Code, Dokumente, Screenshots, Logs, Prompts, Antworten, Modellupdates, Embeddings oder Benchmarks aus Kundenumgebungen.
- Öffentlich sichtbare Repositories oder Webseiten ohne ausdrückliche kompatible Lizenz.
- Drittmaterial, dessen Notice-, Attribution-, Quelloffenlegungs-, Copyleft-, Patent- oder Markenpflichten nicht bewertet wurden.
- Modellgewichte oder Datensätze ohne verifizierte Lizenz und dokumentierte Nutzungsbeschränkungen.
- Sämtliche Datensätze, Modellgewichte, Adapter, Checkpoints, Embedding-Indizes, Trainingsartefakte, ausführbaren POCs, Produktivkonfigurationen oder übernommenen Drittquellcodes – auch bei offener Lizenz. Sie gehören in ein getrenntes freigegebenes Repository.
- Reale Unternehmens- oder Kundennamen in synthetischen Szenarien, sofern sie nicht als notwendige öffentliche Tatsache dienen.

## Anfängliche Lizenz-Allowlist

Für Software gilt zunächst diese bewusst enge Allowlist:

- Apache-2.0
- MIT
- BSD-2-Clause
- BSD-3-Clause

CC0-1.0 und CC-BY-4.0 können nach Attributionsprüfung für Daten oder Dokumentation zugelassen werden. Andere Lizenzen, einschließlich Copyleft-Lizenzen, benötigen vor Nutzung eine dokumentierte Kompatibilitätsentscheidung. „Keine Lizenz“, individuelle Bedingungen, Research-only, Non-commercial und Source-available sind standardmäßig nicht zugelassen.

Die Allowlist ist eine Projektrichtlinie und keine Aussage, andere Open-Source-Lizenzen seien ungültig.

## Pflichtangaben zur Provenienz

Jedes übernommene externe Asset oder Textfragment muss vor dem Merge in `THIRD_PARTY_NOTICES.md` stehen:

- Name und kanonische URL;
- unveränderlicher Commit, Release oder Datensatzstand;
- Lizenz und Lizenz-URL;
- verwendete Dateien oder Artefakte;
- vorgesehene Verwendung;
- vorgenommene Änderungen;
- erforderliche Notices oder Attribution;
- Reviewer und Prüfdatum.

## Publication Gate

Jeder Pull Request muss alle Bedingungen erfüllen:

1. Der Contributor hat die Veröffentlichungscheckliste ausgefüllt.
2. Der automatische Scan findet keine bekannten Secrets oder gesperrten Dateitypen.
3. Ein Mensch prüft Provenienz, Lizenzkompatibilität, Vertraulichkeit und personenbezogene Daten.
4. Externe Inhalte sind in `THIRD_PARTY_NOTICES.md` dokumentiert.
5. Synthetische Inhalte sind gekennzeichnet und enthalten keine realen Identifikatoren.
6. Visuals besitzen Quellen- und Lizenzangaben oder wurden für das Projekt neu erstellt.
7. Generierte Inhalte dokumentieren relevante Inputs und Reviewstatus.
8. Ein Reviewer bestätigt, dass keine offizielle Unterstützung durch NVIDIA oder einen Kunden suggeriert wird.
9. Ein Reviewer bestätigt, dass die Änderung dokumentationsbezogen bleibt und kein POC- oder Kundenprojekt-Artefakt enthält.

Automatische Scans sind nur eine Mindestkontrolle. Ihr Bestehen beweist nicht, dass eine Veröffentlichung sicher oder rechtlich zulässig ist.

## Externe Beiträge

Öffentliche Sichtbarkeit erlaubt Lesen, Forken und das Vorschlagen von Änderungen; sie erteilt keine Schreib- oder Merge-Berechtigung. Externe Beiträge gelangen ausschließlich über Pull Requests aus Forks hinein. Der Repository-Inhaber prüft jede Änderung als CODEOWNER. Das Default-Branch-Ruleset muss direkte Pushes, Force Pushes, Löschung und nicht geprüfte Merges verhindern. Ein Contributor wird nicht als Collaborator hinzugefügt, nur um diesen Ablauf zu umgehen.

## Reaktion auf einen Vorfall

Falls gesperrter Inhalt in die Git-Historie gelangt:

1. Veröffentlichung und weitere Verteilung stoppen.
2. Betroffene Zugangsdaten sofort widerrufen.
3. Repository Owner und zuständige Security-/Legal-Stelle informieren.
4. Inhalt aus dem aktuellen Stand entfernen und History Rewrite bewerten.
5. Forks, Caches, Actions Logs, Releases und Downloads als potenziell offengelegt behandeln.
6. Vorfall dokumentieren und Erkennungsregel verbessern.

## Überprüfung

Diese Policy wird bei jeder neuen Datenquelle, jedem Modell, jeder Lizenz, externen Action, Veröffentlichungsform oder kundenbezogenen Nutzung überprüft.
