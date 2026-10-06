# Translating Embeddings for Modeling Multi-relational Data

> 📄 [论文原文](https://arxiv.org/abs/1301.3785) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Antoine Bordes, Nicolas Usunier, Alberto Garcia-Duran, Jason Weston, Oksana Yakhnenko, **NeurIPS 2013**
> 领域标签: #知识图谱 #表示学习 #链接预测
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1301.3785) |
| 官方代码 | - |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把实体嵌入向量空间、把关系建模为平移操作（head+relation≈tail），以极简方式完成知识图谱链接预测，是 KG 表示学习的开山之作。

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
| 参数量 | 实体/关系嵌入表 | 与词表线性相关 |
| 训练数据 | FB15k / WN18 | 标准 KG 基准 |
| 核心指标 | FB15k filtered Hits@10 47.7% | 链接预测 |
| 训练成本 | 单卡即可 | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
