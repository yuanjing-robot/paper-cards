# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

> 📄 [论文原文](https://arxiv.org/abs/2201.11903) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, et al., **NeurIPS 2022**
> 领域标签: #思维链 #Prompting #推理
> 首次笔记: @zeng417 | 最后更新: 2026-10-05

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2201.11903) |
| 官方代码 | 无官方代码（示例 prompt 已附在论文附录） |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

不训练、不加参数，只在 few-shot 示例中把「中间推理步骤」写出来，就能让大模型"一步步想"——GSM8K 数学题成绩翻倍以上，且只在约 100B+ 参数的模型上显著生效。

---

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 📝 精读笔记 | 精读 + 个人理解（角度灵活取舍） | [reading-notes.md](reading-notes.md) |
| 🌐 论文翻译 | 全文中文翻译 | [translation.md](translation.md) |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 方法成本 | 8 个带推理链的 few-shot 示例 | 纯 prompting，零训练成本 |
| 核心指标 | GSM8K：PaLM 540B 从 17.9% 提升到 56.9% | 论文报告，超过当时微调 + 验证器的 SOTA |
| 生效门槛 | 约 100B+ 参数模型显著 | 小模型上不升反降，属"涌现能力" |
| 模型 | GPT-3 175B / LaMDA / PaLM 540B | 三个模型族上均验证 |

---

## 💬 讨论与备注

- 论文附录给出了 8 个 CoT 示例 prompt，可直接抄用
- 后续 Self-Consistency（多链投票）可再提升约 10~20 个点，建议连读
- 与 ReAct（推理 + 行动）对比读，能理解 CoT 如何走向 Agent

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
