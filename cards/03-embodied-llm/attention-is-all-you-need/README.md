# Attention Is All You Need

> 📄 [论文原文 (arXiv)](https://arxiv.org/abs/1706.03762) · 💻 [官方代码](https://github.com/tensorflow/tensor2tensor)
>
> Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin, **NeurIPS 2017**
> 领域标签: #LLM #Transformer #基础模型
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

## 📑 六维卡片导航

| 视角 | 卡片 | 状态 | 维护者 |
|------|------|------|--------|
| 🏗️ 落地复用 | [Input / Operation / Cost / Gain](01-reuse.md) | ✅ 已完成 | @demo |
| 🔍 批判挑错 | [Omission / Flaw / Precondition / DefectResult](02-critique.md) | ⏳ 部分完成 | @demo |
| 💡 创新拆解 | [Inherit / Modify / Break / Margin](03-innovation.md) | ✅ 已完成 | @demo |
| 🧪 学术假设 | [Hypothesis / Design / Constraint / Conclusion](04-hypothesis.md) | ⏳ 进行中 | - |
| ⚔️ 对标 SOTA | [Difference / Advantage / Disadvantage / Tradeoff](05-sota-compare.md) | ✅ 已完成 | @demo |
| 📚 知识沉淀 | [Knowledge / Law / Experience / Lesson](06-knowledge.md) | ✅ 已完成 | @demo |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | 65M (base) / 213M (big) | base 模型 6 层，big 模型 6 层 |
| 训练数据 | WMT 2014 英德 / 英法 | 约 450 万 / 3600 万句对 |
| 核心指标 | 28.4 BLEU (英德) / 41.8 BLEU (英法) | 当时的 SOTA |
| 训练成本 | 8 P100 GPU × 3.5 天 (base) | 约 672 GPU 小时 |

---

## 🔗 相关论文

### 前置必读
_无 — 这是 Transformer 的开山之作_

### 同类对比
- [_待补充_](../_) — CNN 路线的 seq2seq
- [_待补充_](../_) — RNN + Attention 路线

### 后续改进（太多了，列最重要的几个）
- [_待补充_](../_) — BERT：双向预训练
- [_待补充_](../_) — GPT 系列：自回归预训练
- [_待补充_](../_) — ViT：Transformer 进军 CV
- [_待补充_](../_) — FlashAttention：高效注意力实现

---

## 💬 讨论与备注

- 这篇论文是 LLM 方向的基石，建议所有人精读
- 推荐配合李沐老师的视频讲解一起看
- 最好能手写推导一遍 self-attention 的计算过程

---

> 💡 **快速使用指南**
> - 想了解 Transformer 怎么实现？看 ① 落地复用卡片
> - 想知道它的创新点在哪？看 ③ 创新拆解卡片
> - 和之前的 seq2seq 比怎么样？看 ⑤ 对标 SOTA 卡片
> - 有什么能带走的知识？看 ⑥ 知识沉淀卡片
