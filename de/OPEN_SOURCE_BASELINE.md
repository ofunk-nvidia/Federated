# Open-Source-Werkzeugbasis

Dieses Register legt fest, welche Werkzeuge als Teil des Open-Source-Referenzstacks vorgestellt werden dürfen. Ein Produktname genügt nicht: Bei jeder Aktualisierung sind konkretes Repository, Release, Lizenzdatei, Notices, Abhängigkeiten, Container-Images und Modellbedingungen zu prüfen.

| Kandidat | Rolle | Baseline-Status | Lizenznachweis |
|---|---|---|---|
| NVIDIA FLARE | föderierte Orchestrierung | zugelassener Kandidat | [Repository-Lizenz](https://github.com/NVIDIA/NVFlare/blob/main/LICENSE) |
| NeMo AutoModel | lokales Fine-Tuning und PEFT | zugelassener Kandidat | [Repository-Lizenz](https://github.com/NVIDIA-NeMo/Automodel/blob/main/LICENSE) |
| NeMo Curator | lokale Kuratierung und Decontamination | Kandidat mit Pflichtprüfung der Abhängigkeiten | [Repository-Lizenz und enthaltene Notices](https://github.com/NVIDIA-NeMo/Curator/blob/main/LICENSE) |
| NeMo RL | optionales Preference-/RL-Post-Training | zugelassener späterer Kandidat | [Repository-Lizenz](https://github.com/NVIDIA-NeMo/RL/blob/main/LICENSE) |
| TensorRT-LLM | optionale Inferenzoptimierung | zugelassener späterer Kandidat | [Repository-Lizenz](https://github.com/NVIDIA/TensorRT-LLM/blob/main/LICENSE) |
| NeMo Evaluator | Evaluationsrahmen | Prüfung der konkreten Release-Lizenz ausstehend | [Projekt-Repository](https://github.com/NVIDIA-NeMo/Evaluator) |
| NeMo Framework / Megatron Core | optionale Skalierung | Release- und Abhängigkeitsprüfung ausstehend | [NeMo-Repository](https://github.com/NVIDIA/NeMo) |
| NVIDIA NIM | produktisierte Inferenz | aus strikter OSS-Baseline ausgeschlossen | [NIM-Nutzungsbedingungen](https://docs.nvidia.com/nim/large-language-models/latest/resources/legal.html) |
| NeMo Microservices | verwaltete Plattformdienste | aus strikter OSS-Baseline ausgeschlossen | konkrete Produktbedingungen separat prüfen |

„Zugelassener Kandidat“ bedeutet Eignung für die Darstellung und weitere technische Prüfung, nicht pauschale Freigabe jeder Version, Abhängigkeit, jedes Containers, Modells, Datensatzes oder kommerziellen Einsatzes.

Open-Weight-Modelle benötigen eine getrennte Modelllizenzentscheidung. Öffentlicher GitHub-Code, öffentliche Dokumentation und herunterladbare Gewichte sind nicht automatisch Open Source oder zulässige Trainingsdaten.

Dieses Repository verlinkt Werkzeuge; es übernimmt und führt sie nicht aus. Jede Implementierung gehört in ein getrenntes freigegebenes Repository.

