# Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

> 📄 [论文原文](https://arxiv.org/abs/1801.01290) · 💻 [官方代码](https://github.com/haarnoja/sac) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, Sergey Levine, **ICML 2018**
> 领域标签: #最大熵 #离线策略 #连续控制
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1801.01290) |
| 官方代码 | [GitHub](https://github.com/haarnoja/sac) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

最大化期望回报 + 策略熵的离线策略算法，样本效率高、超参鲁棒，是机器人连续控制最常用的 RL 算法之一。

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
| 参数量 | 双 Q + 策略网络 | 自动温度调节 |
| 训练数据 | MuJoCo 连续控制 | 在线交互 |
| 核心指标 | 样本效率 SOTA（当年） | 多次随机种子稳定 |
| 训练成本 | 单卡可复现 | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
