# 大模型基础（00）

> 不限于具身场景的大模型（LLM）经典论文，作为具身智能各方向的公共基础

## 📚 论文列表

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](bert/) | NAACL 2019 | [📄 原文](https://arxiv.org/abs/1810.04805) | [📝 精读笔记](bert/reading-notes.md) | [🌐 翻译](bert/translation.md) |
| [Language Models are Few-Shot Learners (GPT-3)](gpt-3/) | NeurIPS 2020 | [📄 原文](https://arxiv.org/abs/2005.14165) | [📝 精读笔记](gpt-3/reading-notes.md) | [🌐 翻译](gpt-3/translation.md) |
| [LLaMA: Open and Efficient Foundation Language Models](llama/) | arXiv 2023 | [📄 原文](https://arxiv.org/abs/2302.13971) | [📝 精读笔记](llama/reading-notes.md) | [🌐 翻译](llama/translation.md) |

---

## 📝 说明

- 论文卡片直接放在本目录下（`cards/00-llm/论文短标题/`），推荐用脚本创建：

```bash
python scripts/add-paper.py --title "论文标题" --field 00-llm --paper-url "https://arxiv.org/abs/xxxx.xxxxx"
```

- 如需按子方向组织，可与维护者讨论后自行创建子目录（脚本加 `--subfield 子方向名` 即可，目录不存在会自动创建）
