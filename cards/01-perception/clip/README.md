# Learning Transferable Visual Models From Natural Language Supervision

> 📄 [论文原文](https://arxiv.org/abs/2103.00020) · 💻 [官方代码](https://github.com/OpenAI/CLIP) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Alec Radford et al., **ICML 2021**
> 领域标签: #多模态 #视觉语言 #零样本
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2103.00020) |
| 官方代码 | [GitHub](https://github.com/OpenAI/CLIP) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用 4 亿图文对做对比学习，把图像和文本映射到同一空间，实现零样本分类和开放词汇感知，是具身开放词汇感知的基石。

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
| 参数量 | 约 0.4B (ViT-L/14) | 图像+文本双塔 |
| 训练数据 | WIT 400M 图文对 | 网络公开数据清洗 |
| 核心指标 | ImageNet 零样本 76.2% top-1 | ViT-L/14@336px |
| 训练成本 | 256 V100 × 约 12 天 | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
