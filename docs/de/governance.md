# Governance

[Überblick](../../de/README.md) · [Architektur](architecture.md) · [Workflow](workflow.md) · [Toolchain](toolchain.md) · [Governance](governance.md) · [English](../en/governance.md)

## Leitprinzip

Datenzugriff, lokale Nutzung, Trainingsnutzung, mandatsübergreifender Transfer, Aggregation und Modellfreigabe sind getrennte Entscheidungen. Eine Freigabe auf einer Stufe beinhaltet keine Freigabe der nächsten.

```mermaid
flowchart LR
    A["Zugriff"] --> B["Lokale Nutzung"]
    B --> C["Training"]
    C --> D["Export"]
    D --> E["Aggregation"]
    E --> F["Release"]
```

Jeder Übergang benötigt eine ausdrückliche Policy-Entscheidung und Evidenz.

## Informationsklassen

| Klasse | Typischer Inhalt | Standardbehandlung |
|---|---|---|
| Öffentlich | freigegebene Publikationen und öffentliche Methoden | nach Rechteprüfung geeignet |
| Wiederverwendbare Methode | ausdrücklich freigegebene abstrakte Methoden | nach Kontrollen föderierbar |
| Vertrauliches Mandat | interne Analyse und Kundenprozesse | nur lokal |
| Hochsensitiv | Preise, Angebote, Kapazität, M&A, Strategie, Personendaten | von Federation ausschließen |
| Unbekannt | unklare Herkunft, Rechte oder Zweckbindung | ablehnen |

## Release Gate

Ein gemeinsamer Adapter wird erst Release-Kandidat, wenn Legal, Kartellrecht, Privacy, Security, Model Risk und Mandatsverantwortung den definierten Zweck, die Evidenz, Angriffe und Restrisiken geprüft haben.

Technische Kontrollen reduzieren Risiken, erzeugen aber keine Rechte. Modellupdates können weiterhin Informationen offenlegen. Eine nicht extrahierte Canary belegt nur das Ergebnis eines definierten Tests und nicht, dass Leakage unmöglich ist.

## Veröffentlichung des Repositories

Dieses öffentliche Repository enthält ausschließlich Beschreibungen. Die [Veröffentlichungs-Policy](../../de/PUBLICATION_POLICY.md) regelt die Inhaltsaufnahme, die [Open-Source-Werkzeugbasis](../../de/OPEN_SOURCE_BASELINE.md) Werkzeugangaben und das automatische Publication Gate einen Mindestscan. Human Review bleibt verpflichtend.
