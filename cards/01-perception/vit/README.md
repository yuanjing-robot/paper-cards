# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

> 📄 [论文原文](https://arxiv.org/abs/2010.11929) · 💻 [官方代码](https://github.com/google-research/vision_transformer) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Alexey Dosovitskiy et al., **ICLR 2021**
> 领域标签: #视觉 #Transformer #预训练
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2010.11929) |
| 官方代码 | [GitHub](https://github.com/google-research/vision_transformer) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把图像切成 16×16 patch 直接喂给标准 Transformer，证明大规模预训练下纯 ViT 可以完全取代 CNN，是具身视觉骨干的通用选择。

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
| 参数量 | 86M (Base) / 632M (Huge) | ViT-B/16 与 ViT-H/14 |
| 训练数据 | ImageNet-1k / ImageNet-21k | 最大约 3 亿张图 |
| 核心指标 | ImageNet 88.55% top-1 | ViT-H/14，21k 预训练 |
| 训练成本 | TPUv3 × 8 ~ ×32 | 论文报告区间 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
