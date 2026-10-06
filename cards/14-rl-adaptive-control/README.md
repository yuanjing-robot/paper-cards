# 具身强化学习与自适应控制（14）

> 通过强化学习获得运动与控制能力

## 📚 论文列表

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Human-level control through deep reinforcement learning](dqn/) | Nature 2015 | [📄 原文](https://arxiv.org/abs/1312.5602) | [📝 精读笔记](dqn/reading-notes.md) | [🌐 翻译](dqn/translation.md) |
| [Proximal Policy Optimization Algorithms](ppo/) | arXiv 2017 | [📄 原文](https://arxiv.org/abs/1707.06347) | [📝 精读笔记](ppo/reading-notes.md) | [🌐 翻译](ppo/translation.md) |
| [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](sac/) | ICML 2018 | [📄 原文](https://arxiv.org/abs/1801.01290) | [📝 精读笔记](sac/reading-notes.md) | [🌐 翻译](sac/translation.md) |

---

## 📝 说明

- 论文卡片直接放在本目录下（`cards/14-rl-adaptive-control/论文短标题/`），推荐用脚本创建：

```bash
python scripts/add-paper.py --title "论文标题" --field 14-rl-adaptive-control --paper-url "https://arxiv.org/abs/xxxx.xxxxx"
```

- 如需按子方向组织，可与维护者讨论后自行创建子目录（脚本加 `--subfield 子方向名` 即可，目录不存在会自动创建）
