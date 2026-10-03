# Attention Is All You Need

> 📄 [论文原文](https://arxiv.org/abs/1706.03762) · 💻 [官方代码](https://github.com/tensorflow/tensor2tensor) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md) · 💭 [个人理解](understanding.md)
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
| 解读视频 | [B站 - 李沐讲解](https://www.bilibili.com/video/BV1pu411o7BE/) |

---

## 🎯 一句话概括

Transformer 用纯自注意力机制取代了 RNN/CNN，实现了并行计算 + 长距离依赖建模，成为几乎所有现代大模型的基础架构。

---

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 📝 精读笔记 | 6 个视角合在一起（落地复用 / 批判挑错 / 创新拆解 / 学术假设 / 对标 SOTA / 知识沉淀） | [reading-notes.md](reading-notes.md) |
| 🌐 论文翻译 | 全文中文翻译 | [translation.md](translation.md) |
| 💭 个人理解 | 个人阅读理解与思考 | [understanding.md](understanding.md) |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | 65M (base) / 213M (big) | base 6 层，big 6 层 |
| 训练数据 | WMT 2014 英德 / 英法 | 约 450 万 / 3600 万句对 |
| 核心指标 | 28.4 BLEU / 41.8 BLEU | 当时的 SOTA |
| 训练成本 | 8 P100 × 3.5 天 | 约 672 GPU 小时 |

---

## 💬 讨论与备注

- 这篇是 LLM / VLA 方向的基石，建议所有人精读
- 推荐配合李沐老师的视频讲解一起看
- 最好能手写推导一遍 self-attention 的计算过程

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解核心？看「精读笔记」
> - 想看别人读后的收获？看「个人理解」
