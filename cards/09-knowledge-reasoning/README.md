# 具身知识推理（09）

> 常识、因果与符号推理能力

## 📚 论文列表

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Translating Embeddings for Modeling Multi-relational Data](transe/) | NeurIPS 2013 | [📄 原文](https://arxiv.org/abs/1301.3785) | [📝 精读笔记](transe/reading-notes.md) | [🌐 翻译](transe/translation.md) |
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](chain-of-thought/) | NeurIPS 2022 | [📄 原文](https://arxiv.org/abs/2201.11903) | [📝 精读笔记](chain-of-thought/reading-notes.md) | [🌐 翻译](chain-of-thought/translation.md) |
| [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](tree-of-thoughts/) | NeurIPS 2023 | [📄 原文](https://arxiv.org/abs/2305.10601) | [📝 精读笔记](tree-of-thoughts/reading-notes.md) | [🌐 翻译](tree-of-thoughts/translation.md) |

---

## 📝 说明

- 论文卡片直接放在本目录下（`cards/09-knowledge-reasoning/论文短标题/`），推荐用脚本创建：

```bash
python scripts/add-paper.py --title "论文标题" --field 09-knowledge-reasoning --paper-url "https://arxiv.org/abs/xxxx.xxxxx"
```

- 如需按子方向组织，可与维护者讨论后自行创建子目录（脚本加 `--subfield 子方向名` 即可，目录不存在会自动创建）
