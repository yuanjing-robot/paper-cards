# Mastering Diverse Domains through World Models

> 📄 [论文原文](https://arxiv.org/abs/2301.04104) · 💻 [官方代码](https://github.com/danijar/dreamerv3) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap, **arXiv 2023**
> 领域标签: #世界模型 #强化学习 #通用智能
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2301.04104) |
| 官方代码 | [GitHub](https://github.com/danijar/dreamerv3) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用固定超参数的 RSSM 世界模型横跨 150+ 任务，首个从零在 Minecraft 中采集到钻石的算法，展示世界模型路线的通用性。

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
| 参数量 | 约 200M 固定 | 全任务同一超参 |
| 训练数据 | CS:GO / Minecraft / DMC 等 | 在线交互 |
| 核心指标 | Minecraft 首个采集钻石 | 从零开始无人类数据 |
| 训练成本 | 单卡 A100 级 | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
