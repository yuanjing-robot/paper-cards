# Visual Language Maps for Robot Navigation

> 📄 [论文原文](https://arxiv.org/abs/2210.05714) · 💻 [官方代码](https://github.com/cvr-rgc/vlmaps) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Chenguang Huang, Oier Mees, Andy Zeng, Wolfram Burgard, **ICRA 2023**
> 领域标签: #开放词汇 #导航 #视觉语言
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2210.05714) |
| 官方代码 | [GitHub](https://github.com/cvr-rgc/vlmaps) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把 LSeg 视觉语言特征融合进 3D 重建地图，生成"能用自然语言查询"的空间地图，让机器人按语言指令定位物体与导航。

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
| 参数量 | 依赖 LSeg | 不额外训练导航网络 |
| 训练数据 | HM3D / MP3D 扫描 | 在线建图 |
| 核心指标 | 语言目标导航 SOTA | 多数据集提升明显 |
| 训练成本 | - | 微调为主 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
