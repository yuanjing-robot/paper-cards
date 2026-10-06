# Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

> 📄 [论文原文](https://arxiv.org/abs/1703.06907) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Pieter Abbeel, Wojciech Zaremba, **IROS 2017**
> 领域标签: #域随机化 #抓取 #迁移学习
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1703.06907) |
| 官方代码 | - |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

在仿真中随机化纹理、光照、相机位姿等视觉参数，让真实世界看起来只是"另一种随机化"，实现零真实数据训练的抓取迁移。

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
| 参数量 | 小型 CNN | 抓取检测 |
| 训练数据 | 合成渲染图像 | 纹理随机化 |
| 核心指标 | 真实未见物体抓取约 80% | 零真实样本 |
| 训练成本 | - | 仿真为主 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
