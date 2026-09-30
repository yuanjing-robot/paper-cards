# Attention Is All You Need

> 📄 [论文原文 (arXiv)](https://arxiv.org/abs/1706.03762) · 💻 [官方代码](https://github.com/tensorflow/tensor2tensor) · 🌐 [中文翻译](07-translation.md) · 💭 [个人理解](08-understanding.md)
>
> Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin, **NeurIPS 2017**
> 领域标签: #LLM #Transformer #基础模型 #VLA
> 首次笔记: @demo | 最后更新: 2024-09-30

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1706.03762) |
| 官方代码 | [GitHub (tensor2tensor)](https://github.com/tensorflow/tensor2tensor) |
| 复现代码 | [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) |
| 项目主页 | _无_ |
| 解读视频 | [B站 - 李沐讲解](https://www.bilibili.com/video/BV1pu411o7BE/) |

---

## 🎯 一句话概括

Transformer 用纯自注意力机制取代了 RNN/CNN，实现了并行计算 + 长距离依赖建模，成为几乎所有现代大模型的基础架构。

---

## 📑 内容导航

| 模块 | 内容 | 状态 | 维护者 |
|------|------|------|--------|
| 🏗️ ① 落地复用 | [Input / Operation / Cost / Gain](01-reuse.md) | ✅ 已完成 | @demo |
| 🔍 ② 批判挑错 | [Omission / Flaw / Precondition / DefectResult](02-critique.md) | ⏳ 部分完成 | @demo |
| 💡 ③ 创新拆解 | [Inherit / Modify / Break / Margin](03-innovation.md) | ✅ 已完成 | @demo |
| 🧪 ④ 学术假设 | [Hypothesis / Design / Constraint / Conclusion](04-hypothesis.md) | ⏳ 进行中 | - |
| ⚔️ ⑤ 对标 SOTA | [Difference / Advantage / Disadvantage / Tradeoff](05-sota-compare.md) | ✅ 已完成 | @demo |
| 📚 ⑥ 知识沉淀 | [Knowledge / Law / Experience / Lesson](06-knowledge.md) | ✅ 已完成 | @demo |
| 🌐 ⑦ 论文翻译 | [核心章节中文翻译](07-translation.md) | ✅ 已完成 | @demo |
| 💭 ⑧ 个人理解 | [个人阅读理解与思考](08-understanding.md) | ✅ 已完成 | @demo |

> **状态说明**：✅ 已完成 · ⏳ 进行中 · ❌ 未开始

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | 65M (base) / 213M (big) | base 模型 6 层，big 模型 6 层 |
| 训练数据 | WMT 2014 英德 / 英法 | 约 450 万 / 3600 万句对 |
| 核心指标 | 28.4 BLEU (英德) / 41.8 BLEU (英法) | 当时的 SOTA |
| 训练成本 | 8 P100 GPU × 3.5 天 (base) | 约 672 GPU 小时 |

---

## 💬 讨论与备注

- 这篇论文是 LLM / VLA 方向的基石，建议所有人精读
- 推荐配合李沐老师的视频讲解一起看
- 最好能手写推导一遍 self-attention 的计算过程
- 想看个人阅读感悟？直接翻到 ⑧ 个人理解

---

> 💡 **快速使用指南**
> - 想看中文版？直接看 ⑦ 论文翻译
> - 想了解 Transformer 怎么实现？看 ① 落地复用
> - 想知道它的创新点在哪？看 ③ 创新拆解
> - 想看别人读后的收获？看 ⑧ 个人理解
> - 想带走真东西？看 ⑥ 知识沉淀
