# Open-Source Tool Baseline

This register governs which tools may be presented as part of the open-source reference stack. A product name is not enough: verify the exact repository, release, licence file, notices, dependencies, container images, and model terms at each update.

| Candidate | Role | Baseline status | Licence evidence |
|---|---|---|---|
| [NVIDIA FLARE](https://nvflare.readthedocs.io/en/main/) | federated orchestration | admitted candidate | [repository licence](https://github.com/NVIDIA/NVFlare/blob/main/LICENSE) |
| [NeMo AutoModel](https://docs.nvidia.com/nemo/automodel/latest/) | local fine-tuning and PEFT | admitted candidate | [repository licence](https://github.com/NVIDIA-NeMo/Automodel/blob/main/LICENSE) |
| [NeMo Curator](https://docs.nvidia.com/nemo/curator/latest/) | local curation and decontamination | admitted candidate with dependency review | [repository licence and bundled notices](https://github.com/NVIDIA-NeMo/Curator/blob/main/LICENSE) |
| [NeMo RL](https://docs.nvidia.com/nemo/rl/index.html) | optional preference/RL post-training | admitted later-stage candidate | [repository licence](https://github.com/NVIDIA-NeMo/RL/blob/main/LICENSE) |
| [TensorRT-LLM](https://docs.nvidia.com/tensorrt-llm/) | optional inference optimisation | admitted later-stage candidate | [repository licence](https://github.com/NVIDIA/TensorRT-LLM/blob/main/LICENSE) |
| [NeMo Evaluator](https://docs.nvidia.com/nemo/evaluator) | evaluation framework | pending exact-release licence verification | [project repository](https://github.com/NVIDIA-NeMo/Evaluator) |
| [NeMo Framework](https://docs.nvidia.com/nemo-framework/index.html) / [Megatron Core](https://docs.nvidia.com/megatron-core/developer-guide/latest/) | optional scale-up | pending exact-release and dependency review | [NeMo repository](https://github.com/NVIDIA/NeMo) |
| [Material for MkDocs 9.7.7](https://squidfunk.github.io/mkdocs-material/) | GitHub Pages presentation layer | admitted, pinned build dependency | [MIT licence](https://github.com/squidfunk/mkdocs-material/blob/9.7.7/LICENSE) |
| [NVIDIA NIM](https://docs.nvidia.com/nim/large-language-models/latest/introduction.html) | productised inference | excluded from strict OSS baseline | [NIM legal terms](https://docs.nvidia.com/nim/large-language-models/latest/resources/legal.html) |
| [NeMo Microservices](https://docs.nvidia.com/nemo/microservices/latest/) | managed platform services | excluded from strict OSS baseline | exact product terms must be assessed separately |

“Admitted candidate” means suitable for presentation and further technical evaluation; it is not blanket approval for every version, dependency, container, model, dataset, or commercial use.

Open-weight models require a separate model-licence decision. Public GitHub code, public documentation, and downloadable weights are not automatically open source or permissible training data.

This repository links to tools; it does not vendor or execute them. Any implementation belongs in a separate approved repository.

