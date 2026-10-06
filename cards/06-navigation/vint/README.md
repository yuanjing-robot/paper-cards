# ViNT: A Foundation Model for Visual Navigation

> 📄 [论文原文](https://arxiv.org/abs/2306.14846) · 💻 [官方代码](https://github.com/robodhruv/visualnav-transformer) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Arjun Majumdar et al., **CoRL 2023**
> 领域标签: #视觉导航 #基础模型 #跨本体
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2306.14846) |
| 官方代码 | [GitHub](https://github.com/robodhruv/visualnav-transformer) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用 Transformer 融合多数据集的图像目标对，学习通用的视觉导航策略，可零样本迁移到新机器人并微调到新环境，是导航基础模型代表。

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
| 参数量 | 约 4.8M | 轻量 Transformer |
| 训练数据 | 多来源导航数据集 | 跨机器人本体 |
| 核心指标 | 跨数据集/跨本体泛化 | 微调后达 SOTA |
| 训练成本 | - | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
