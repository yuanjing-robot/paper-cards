# QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning

> 📄 [论文原文](https://arxiv.org/abs/1803.11485) · 💻 [官方代码](https://github.com/oxwhirl/pymarl) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Tabish Rashid, Mikayel Samvelyan, Christian Schröder de Witt et al., **ICML 2018**
> 领域标签: #多智能体 #值分解 #协同
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1803.11485) |
| 官方代码 | [GitHub](https://github.com/oxwhirl/pymarl) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用单调网络把各智能体的 Q 值分解合成总 Q，保证个体贪婪策略即全局最优，在星际争霸微操(SMAC)上成为长期标杆。

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
| 参数量 | 各智能体 RNN + 混合网络 | 较小 |
| 训练数据 | SMAC 星际微操 | 在线交互 |
| 核心指标 | SMAC 多图 SOTA（当年） | 3m/5m/8m 等地图 |
| 训练成本 | 单机多卡可复现 | pymarl 框架 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
