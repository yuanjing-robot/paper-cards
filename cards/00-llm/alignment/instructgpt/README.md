# InstructGPT: Training language models to follow instructions with human feedback

> 📄 [论文原文](https://arxiv.org/abs/2203.02155) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Ryan Lowe, et al., **NeurIPS 2022**
> 领域标签: #RLHF #指令微调 #对齐
> 首次笔记: @zeng417 | 最后更新: 2026-10-05

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2203.02155) |
| 官方代码 | 未开源（开源替代：TRL / trlX 等复现） |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用「监督微调 → 奖励模型 → PPO 强化学习」三阶段 RLHF 流程，让语言模型从"会续写"变成"听指令、有帮助且无害"——1.3B 的 InstructGPT 输出在人工偏好评估中胜过 175B 的 GPT-3，是 ChatGPT 的直接技术前身。

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
| 参数量 | 1.3B（主力）/ 6B / 175B | 基于 GPT-3 架构 |
| 训练数据 | SFT 约 1.3 万条 / RM 约 3.3 万条 / PPO 约 3.1 万条 prompts | 标注员按指南撰写与排序 |
| 核心指标 | 人工偏好评估中 1.3B InstructGPT > 175B GPT-3 | 论文主结论 |
| 代价 | 公开 NLP 基准小幅回退 | 即"对齐税" |

---

## 💬 讨论与备注

- 「预测下一个词」的训练目标 ≠ 「有帮助、诚实、无害」的用户目标，这是全文最核心的洞察
- RLHF 三件套（SFT/RM/PPO）至今仍是主流对齐流程，中文开源模型也普遍复刻
- 后续 DPO（2023）用偏好优化替代 RL，可对比阅读

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
