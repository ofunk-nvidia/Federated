# Open-Source-Werkzeugbasis

Dieses Register legt fest, welche Werkzeuge als Teil des Open-Source-Referenzstacks vorgestellt werden dürfen. Ein Produktname genügt nicht: Bei jeder Aktualisierung sind konkretes Repository, Release, Lizenzdatei, Notices, Abhängigkeiten, Container-Images und Modellbedingungen zu prüfen.

| Kandidat | Rolle | Baseline-Status | Lizenznachweis |
|---|---|---|---|
| [NVIDIA FLARE](https://nvflare.readthedocs.io/en/main/) | föderierte Orchestrierung | zugelassener Kandidat | [Repository-Lizenz](https://github.com/NVIDIA/NVFlare/blob/main/LICENSE) |
| [NeMo AutoModel](https://docs.nvidia.com/nemo/automodel/latest/) | lokales Fine-Tuning und PEFT | zugelassener Kandidat | [Repository-Lizenz](https://github.com/NVIDIA-NeMo/Automodel/blob/main/LICENSE) |
| [NeMo Curator](https://docs.nvidia.com/nemo/curator/latest/) | lokale Kuratierung und Decontamination | Kandidat mit Pflichtprüfung der Abhängigkeiten | [Repository-Lizenz und enthaltene Notices](https://github.com/NVIDIA-NeMo/Curator/blob/main/LICENSE) |
| [NeMo RL](https://docs.nvidia.com/nemo/rl/index.html) | optionales Preference-/RL-Post-Training | zugelassener späterer Kandidat | [Repository-Lizenz](https://github.com/NVIDIA-NeMo/RL/blob/main/LICENSE) |
| [TensorRT-LLM](https://docs.nvidia.com/tensorrt-llm/) | optionale Inferenzoptimierung | zugelassener späterer Kandidat | [Repository-Lizenz](https://github.com/NVIDIA/TensorRT-LLM/blob/main/LICENSE) |
| [NeMo Evaluator](https://docs.nvidia.com/nemo/evaluator) | Evaluationsrahmen | Prüfung der konkreten Release-Lizenz ausstehend | [Projekt-Repository](https://github.com/NVIDIA-NeMo/Evaluator) |
| [NeMo Framework](https://docs.nvidia.com/nemo-framework/index.html) / [Megatron Core](https://docs.nvidia.com/megatron-core/developer-guide/latest/) | optionale Skalierung | Release- und Abhängigkeitsprüfung ausstehend | [NeMo-Repository](https://github.com/NVIDIA/NeMo) |
| [Material for MkDocs 9.7.7](https://squidfunk.github.io/mkdocs-material/) | GitHub-Pages-Präsentationsschicht | zugelassene, fixierte Build-Abhängigkeit | [MIT-Lizenz](https://github.com/squidfunk/mkdocs-material/blob/9.7.7/LICENSE) |
| [NVIDIA NIM](https://docs.nvidia.com/nim/large-language-models/latest/introduction.html) | produktisierte Inferenz | aus strikter OSS-Baseline ausgeschlossen | [NIM-Nutzungsbedingungen](https://docs.nvidia.com/nim/large-language-models/latest/resources/legal.html) |
| [NeMo Microservices](https://docs.nvidia.com/nemo/microservices/latest/) | verwaltete Plattformdienste | aus strikter OSS-Baseline ausgeschlossen | konkrete Produktbedingungen separat prüfen |

„Zugelassener Kandidat“ bedeutet Eignung für die Darstellung und weitere technische Prüfung, nicht pauschale Freigabe jeder Version, Abhängigkeit, jedes Containers, Modells, Datensatzes oder kommerziellen Einsatzes.

Open-Weight-Modelle benötigen eine getrennte Modelllizenzentscheidung. Öffentlicher GitHub-Code, öffentliche Dokumentation und herunterladbare Gewichte sind nicht automatisch Open Source oder zulässige Trainingsdaten.

Dieses Repository verlinkt Werkzeuge; es übernimmt und führt sie nicht aus. Jede Implementierung gehört in ein getrenntes freigegebenes Repository.

