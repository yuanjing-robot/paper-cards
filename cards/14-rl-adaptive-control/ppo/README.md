# Proximal Policy Optimization Algorithms

> 📄 [论文原文](https://arxiv.org/abs/1707.06347) · 💻 [官方代码](https://github.com/openai/baselines) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov, **arXiv 2017**
> 领域标签: #策略梯度 #强化学习 #通用基线
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1707.06347) |
| 官方代码 | [GitHub](https://github.com/openai/baselines) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用裁剪替代目标限制策略更新步长，兼顾实现简单与性能稳定，成为 RL/机器人训练最常用的默认算法（也是 RLHF 的底座）。

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
| 参数量 | MLP/网络随任务 | 实现极简 |
| 训练数据 | Atari / MuJoCo / 机器人 | 在线交互 |
| 核心指标 | 连续+离散控制强基线 | 工业界广泛使用 |
| 训练成本 | 单卡起 | 任务相关 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
