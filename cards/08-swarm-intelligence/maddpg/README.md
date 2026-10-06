# Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments

> 📄 [论文原文](https://arxiv.org/abs/1706.02275) · 💻 [官方代码](https://github.com/openai/maddpg) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Ryan Lowe, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel, Igor Mordatch, **NeurIPS 2017**
> 领域标签: #多智能体 #强化学习 #博弈
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1706.02275) |
| 官方代码 | [GitHub](https://github.com/openai/maddpg) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把 DDPG 扩展到多智能体：中心化 critic + 分散执行，能学到合作/竞争混合博弈中的策略，是多智能体 RL 的标准基线。

---

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 📝 精读笔记 | 精读 + 个人理解（角度按论文特点灵活取舍） | [reading-notes.md](reading-notes.md) |
| 🌐 论文翻译 | 全文中文翻译 | [translation.md](translation.md) |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | Actor-Critic MLP | 较小 |
| 训练数据 | MPE 多智能体环境 | 在线交互 |
| 核心指标 | 合作/竞争任务优于 DDPG | 论文报告 |
| 训练成本 | 单卡可复现 | 环境轻量 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
