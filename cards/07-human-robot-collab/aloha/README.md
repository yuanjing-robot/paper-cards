# Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

> 📄 [论文原文](https://arxiv.org/abs/2304.13705) · 💻 [官方代码](https://github.com/tonyzhaozh/aloha) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Tony Zhao, Vikash Kumar, Sergey Levine, Chelsea Finn, **RSS 2023**
> 领域标签: #遥操作 #双手操作 #模仿学习
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2304.13705) |
| 官方代码 | [GitHub](https://github.com/tonyzhaozh/aloha) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用约 2 万美元的低成本双手遥操作硬件 + ACT Transformer 策略，让机器人学会插电池、拧瓶盖等精细双手任务，掀起低成本遥操作数据采集风潮。

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
| 参数量 | ACT 数千万级 | CVAE Transformer |
| 训练数据 | 50 条演示/任务 | 遥操作采集 |
| 核心指标 | 精细任务 80-90% 成功率 | 如装电池/拧瓶盖 |
| 训练成本 | 硬件约 $20k | 单卡训练 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
