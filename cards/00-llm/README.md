# 大模型基础（00）

> 不限于具身智能场景的大模型（LLM）经典论文：预训练语言模型、对齐与 RLHF、推理增强、检索增强生成等。作为具身智能各方向的公共基础。

---

## 📂 子方向

### [预训练语言模型](pretrain-lm/)

> 从 BERT 到 GPT-3 再到 LLaMA：预训练范式的建立、规模涌现与开源化

| 论文 | 会议/年份 | 原文 | 精读 | 翻译 | 个人理解 |
|------|----------|------|------|------|---------|
| [BERT](pretrain-lm/bert/) | NAACL 2019 | [📄 原文](https://arxiv.org/abs/1810.04805) | [📝 精读](pretrain-lm/bert/) | [🌐 翻译](pretrain-lm/bert/translation.md) | [💭 理解](pretrain-lm/bert/reading-notes.md) |
| [GPT-3](pretrain-lm/gpt-3/) | NeurIPS 2020 | [📄 原文](https://arxiv.org/abs/2005.14165) | [📝 精读](pretrain-lm/gpt-3/) | [🌐 翻译](pretrain-lm/gpt-3/translation.md) | [💭 理解](pretrain-lm/gpt-3/reading-notes.md) |
| [LLaMA](pretrain-lm/llama/) | arXiv 2023 | [📄 原文](https://arxiv.org/abs/2302.13971) | [📝 精读](pretrain-lm/llama/) | [🌐 翻译](pretrain-lm/llama/translation.md) | [💭 理解](pretrain-lm/llama/reading-notes.md) |

### [对齐与 RLHF](alignment/)

> 指令微调 + 人类反馈强化学习，让模型听懂指令、对齐人类偏好

| 论文 | 会议/年份 | 原文 | 精读 | 翻译 | 个人理解 |
|------|----------|------|------|------|---------|
| [InstructGPT](alignment/instructgpt/) | NeurIPS 2022 | [📄 原文](https://arxiv.org/abs/2203.02155) | [📝 精读](alignment/instructgpt/) | [🌐 翻译](alignment/instructgpt/translation.md) | [💭 理解](alignment/instructgpt/reading-notes.md) |

### [推理增强](reasoning/)

> 思维链等 prompting 范式，激发大模型多步推理能力

| 论文 | 会议/年份 | 原文 | 精读 | 翻译 | 个人理解 |
|------|----------|------|------|------|---------|
| [Chain-of-Thought](reasoning/chain-of-thought/) | NeurIPS 2022 | [📄 原文](https://arxiv.org/abs/2201.11903) | [📝 精读](reasoning/chain-of-thought/) | [🌐 翻译](reasoning/chain-of-thought/translation.md) | [💭 理解](reasoning/chain-of-thought/reading-notes.md) |

### [检索增强生成](retrieval-augmented/)

> 外部知识检索 + 生成结合，缓解幻觉、支持知识更新

| 论文 | 会议/年份 | 原文 | 精读 | 翻译 | 个人理解 |
|------|----------|------|------|------|---------|
| [RAG](retrieval-augmented/rag/) | NeurIPS 2020 | [📄 原文](https://arxiv.org/abs/2005.11401) | [📝 精读](retrieval-augmented/rag/) | [🌐 翻译](retrieval-augmented/rag/translation.md) | [💭 理解](retrieval-augmented/rag/reading-notes.md) |

---

## 📝 贡献指南

本方向的论文请放入对应子方向目录下。如有新的子方向建议（如高效架构、多模态对齐、Agent），欢迎提 Issue 讨论。
