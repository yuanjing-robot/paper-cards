# Habitat: A Platform for Embodied AI Research

> 📄 [论文原文](https://arxiv.org/abs/1904.01201) · 💻 [官方代码](https://github.com/facebookresearch/habitat-lab) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Manolis Savva, Abhishek Kadian, Oleksandr Maksymets et al., **ICCV 2019**
> 领域标签: #仿真器 #具身导航 #高效渲染
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1904.01201) |
| 官方代码 | [GitHub](https://github.com/facebookresearch/habitat-lab) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

面向室内导航的具身智能平台，渲染与感知速度比此前方案快一个数量级（1 万+ FPS），成为 PointNav/ObjectNav 的标准评测平台。

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
| 参数量 | - | 仿真平台 |
| 训练数据 | Matterport3D / Gibson 扫描 | 72k+ 场景实例 |
| 核心指标 | 渲染 10,000+ FPS | 多进程批量渲染 |
| 训练成本 | - | 平台免费开源 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
