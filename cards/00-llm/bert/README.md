# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> 📄 [论文原文](https://arxiv.org/abs/1810.04805) · 💻 [官方代码](https://github.com/google-research/bert) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova, **NAACL 2019**
> 领域标签: #预训练 #Transformer #NLP
> 首次笔记: @zeng417 | 最后更新: 2026-10-05

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1810.04805) |
| 官方代码 | [GitHub (google-research/bert)](https://github.com/google-research/bert) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

BERT 用「掩码语言模型 + 下一句预测」在 Transformer encoder 上做深度双向预训练，确立了「预训练 → 微调」范式，成为分类、抽取、检索等理解类 NLP 任务的通用底座。

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
| 参数量 | 110M (base) / 340M (large) | base 12 层 / large 24 层 Transformer encoder |
| 训练数据 | 约 16GB 纯文本 | BooksCorpus + 英文维基百科 |
| 核心指标 | GLUE 80.5 / SQuAD v1.1 F1 93.2 | 论文报告，当时 11 项 NLP 任务 SOTA |
| 训练成本 | large 约 64 块 TPU 芯片 × 4 天 | 以今天眼光看不算贵 |

---

## 💬 讨论与备注

- 建议与 GPT 系列（decoder-only）对比读，理解 encoder / decoder 两条路线的分化
- 中文场景常用衍生版本：chinese-bert-wwm、RoBERTa-wwm-ext 等
- NSP 任务后来被 RoBERTa 证明收益存疑，读时可带着批判眼光

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
