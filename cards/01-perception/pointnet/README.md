# PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation

> 📄 [论文原文](https://arxiv.org/abs/1612.00593) · 💻 [官方代码](https://github.com/charlesq34/pointnet) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Charles R. Qi, Hao Su, Kaichun Mo, Leonidas J. Guibas, **CVPR 2017**
> 领域标签: #点云 #3D视觉 #感知
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1612.00593) |
| 官方代码 | [GitHub](https://github.com/charlesq34/pointnet) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

首次提出直接在无序点云上做深度学习的对称函数网络，用点级 MLP + 最大池化保证置换不变性，成为 3D 机器人感知的基础组件。

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
| 参数量 | 约 3.5M | ModelNet40 分类模型 |
| 训练数据 | ModelNet40 / ShapeNet | 约 12k 个 3D 模型 |
| 核心指标 | ModelNet40 分类 89.2% | 点云分类当时 SOTA |
| 训练成本 | - | 单卡即可复现 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
