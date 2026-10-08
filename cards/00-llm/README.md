# 大模型基础（00）

> 不限于具身场景的大模型（LLM）经典论文，作为具身智能各方向的公共基础

## 📚 论文列表

| 论文 | 会议/年份 | 原文 | 深度阅读 | 翻译 | 代码 |
|------|----------|------|---------|------|------|
| [Language Models are Few-Shot Learners](language-models-are-few-shot-learners/) | NeurIPS 2020 | [📄 原文](https://arxiv.org/abs/2005.14165) | [📝 深度阅读](language-models-are-few-shot-learners/reading-notes.md) | [🌐 翻译](language-models-are-few-shot-learners/translation.md) | - |
| _待补充_ | - | - | - | - | - |
| _待补充_ | - | - | - | - | - |

---

## 📝 说明

- 论文卡片直接放在本目录下（`cards/00-llm/论文短标题/`），推荐用脚本创建：

```bash
python scripts/add-paper.py --title "论文标题" --field 00-llm --paper-url "https://arxiv.org/abs/xxxx.xxxxx"
```

- 如需按子方向组织，加 `--subfield 子方向名` 即可（目录不存在会自动创建）
