# RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

> 📄 [论文原文](https://arxiv.org/abs/2005.11401) · 💻 [开源实现（HuggingFace Transformers）](https://github.com/huggingface/transformers) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, et al., **NeurIPS 2020**
> 领域标签: #检索增强 #知识密集型 #开放域QA
> 首次笔记: @zeng417 | 最后更新: 2026-10-05

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2005.11401) |
| 开源实现 | [HuggingFace Transformers](https://github.com/huggingface/transformers) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把「非参数化的文档库检索（DPR + FAISS）」与「参数化的生成模型（BART）」端到端结合，让生成模型"查着资料说话"——开放域 QA 成绩领先，生成内容幻觉更少、可以溯源。

---

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 📝 精读笔记 | 精读 + 个人理解（角度灵活取舍） | [reading-notes.md](reading-notes.md) |
| 🌐 论文翻译 | 全文中文翻译 | [translation.md](translation.md) |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | 生成器 BART-large 约 400M | 检索库为 Wikipedia 约 2100 万篇（非参数化知识） |
| 核心指标 | NQ EM 44.5 | 开放域 QA，超过 T5-11B+SSM、DPR 等基线 |
| 生成质量 | 事实性人评优于纯 BART | 幻觉更少、答案可溯源到文档 |
| 架构 | RAG-Sequence / RAG-Token 两种变体 | 对 top-k 检索文档做边缘化融合 |

---

## 💬 讨论与备注

- 今天企业知识库、聊天机器人里的「RAG」皆源于此，但工程形态已迭代（混合检索、重排、引用溯源）
- 与 REALM、RETRO、Atlas 对比读可以理解检索增强的演化谱系
- 「知识放参数里 vs 放外部库里」的 trade-off 是全文最值得消化的框架

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
