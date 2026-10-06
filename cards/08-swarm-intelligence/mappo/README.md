# The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games

> 📄 [论文原文](https://arxiv.org/abs/2103.01955) · 💻 [官方代码](https://github.com/marlbenchmark/on-policy) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Chao Yu, Akash Velu, Eugene Vinitsky, Jiaxuan Gao et al., **NeurIPS 2022 (D&C)**
> 领域标签: #多智能体 #PPO #协同
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2103.01955) |
| 官方代码 | [GitHub](https://github.com/marlbenchmark/on-policy) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

给 PPO 加上序列优势估计等改造后（MAPPO），在合作任务上匹敌或超越专门的值分解方法，简单方法重新成为强基线。

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
| 参数量 | Actor-Critic MLP/RNN | 较小 |
| 训练数据 | SMAC / MPE / Hanabi | 在线交互 |
| 核心指标 | SMAC/MPE 匹配或超越 QMIX | 且训练更稳定 |
| 训练成本 | 单机可复现 | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
