# Mitwirken

Beiträge sind willkommen, wenn sie [PUBLICATION_POLICY.md](PUBLICATION_POLICY.md) erfüllen.

Externe Beitragende arbeiten aus einem Fork und reichen einen Pull Request ein. Für reine Dokumentationsbeiträge wird kein direkter Schreibzugriff angefragt oder vergeben. Sicherheitsrelevante Meldungen folgen [SECURITY.md](SECURITY.md) und dürfen niemals in ein öffentliches Issue oder einen Pull Request gelangen.

Vor einem Pull Request:

1. Nur Dokumentation, Mermaid, eigene Visuals oder kleine synthetische nicht operative Fragmente ergänzen.
2. Open-Source-Werkzeuge mit kanonischem Link, Version und Lizenz referenzieren; ihren Code hier nicht übernehmen.
3. Jedes übernommene externe Textfragment oder Asset in `THIRD_PARTY_NOTICES.md` dokumentieren.
4. `python scripts/check_public_content.py` ausführen.
5. Kunden-, Arbeitgeber-, Partner-, Personen-, Geheim- und Zugangsdaten ausschließen.
6. Bestätigen, dass keine Datensätze, Modellartefakte, POC-Implementierung, Produktivkonfiguration oder Kundenprojektinhalte enthalten sind.
7. Offenlegen, ob KI den Beitrag erzeugt hat und welche Inputs verwendet wurden.
8. Einen kleinen Pull Request mit einem klaren Zweck einreichen.
9. Nach Änderungen an Präsentationskonfiguration oder Navigation `requirements-pages.txt` installieren, `bash scripts/build_pages.sh` ausführen und beide Sprachpfade prüfen.
10. Publication Check und CODEOWNER-Freigabe abwarten und niemals um Umgehung des Default-Branch-Rulesets bitten.

Mit dem Beitrag wird bestätigt, dass die erforderlichen Rechte für eine Veröffentlichung unter der Repository-Lizenz vorliegen. Ein bestandener automatischer Scan ersetzt kein menschliches Review.

## Synchronität von Repository und Pages

Das versionierte Markdown ist die einzige Source of Truth. GitHub Pages wird durch `.github/workflows/pages.yml` aus demselben Commit erzeugt; generierte Verzeichnisse werden weder bearbeitet noch committed. Ein fehlgeschlagener Pages-Build oder ein fehlgeschlagenes Deployment ist ein Veröffentlichungsfehler und muss behoben werden, bevor die öffentliche Site als aktuell gilt.
