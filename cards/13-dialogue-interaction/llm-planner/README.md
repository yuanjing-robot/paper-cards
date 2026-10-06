# LLM-Planner: Grounded Planning for Embodied Agents with Large Language Models

> 📄 [论文原文](https://arxiv.org/abs/2312.10435) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Chan Hee Song, Jianan Wu, Clayton Washington, Brian Sadler, Wei-Lun Chao, Yu Su, **NeurIPS 2023**
> 领域标签: #LLM规划 #具身导航 #接地
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2312.10435) |
| 官方代码 | - |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

给 LLM 注入场景的物体列表等接地信息，仅用少量样本就能在具身指令跟随任务（ALFRED）上做 grounded 规划。

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
| 参数量 | 依赖 GPT-3/4 等 | 不训练或轻量微调 |
| 训练数据 | ALFRED 指令任务 | 场景物体清单 |
| 核心指标 | ALFRED few-shot 大幅提升 | 可融入动态场景信息 |
| 训练成本 | API/单卡 | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
