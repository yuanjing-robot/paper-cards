# 具身世界模型构建（04）

> 让机器人理解物理世界的运行规律

## 📚 论文列表

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [World Models](world-models/) | NeurIPS 2018 | [📄 原文](https://arxiv.org/abs/1803.10122) | [📝 精读笔记](world-models/reading-notes.md) | [🌐 翻译](world-models/translation.md) |
| [Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](muzero/) | Nature 2019 | [📄 原文](https://arxiv.org/abs/1911.08265) | [📝 精读笔记](muzero/reading-notes.md) | [🌐 翻译](muzero/translation.md) |
| [Mastering Diverse Domains through World Models](dreamer-v3/) | arXiv 2023 | [📄 原文](https://arxiv.org/abs/2301.04104) | [📝 精读笔记](dreamer-v3/reading-notes.md) | [🌐 翻译](dreamer-v3/translation.md) |

---

## 📝 说明

- 论文卡片直接放在本目录下（`cards/04-world-model/论文短标题/`），推荐用脚本创建：

```bash
python scripts/add-paper.py --title "论文标题" --field 04-world-model --paper-url "https://arxiv.org/abs/xxxx.xxxxx"
```

- 如需按子方向组织，可与维护者讨论后自行创建子目录（脚本加 `--subfield 子方向名` 即可，目录不存在会自动创建）
