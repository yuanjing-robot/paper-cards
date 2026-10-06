# Using millions of emoji occurrences to learn pre-trained representations for detecting sentiment, emotion and sarcasm

> 📄 [论文原文](https://arxiv.org/abs/1508.06615) · 💻 [官方代码](https://github.com/bfelbo/DeepMoji) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Bjarke Felbo, Alan Mislove, Anders Søgaard, Iyad Rahwan, Sander Schwartz, **ACL 2017**
> 领域标签: #情感计算 #预训练 #迁移学习
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1508.06615) |
| 官方代码 | [GitHub](https://github.com/bfelbo/DeepMoji) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用 12 亿条带 emoji 的推文预训练情感表示，再迁移到情感/讽刺等下游任务，是情感计算方向大规模自监督预训练的代表。

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
| 参数量 | BiLSTM 约 4.5M | 两层 + 注意力 |
| 训练数据 | 12 亿条推文 | emoji 自监督 |
| 核心指标 | 多个情感基准 SOTA（当年） | 含讽刺检测 |
| 训练成本 | - | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
