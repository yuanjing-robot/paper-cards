# GPT-3: Language Models are Few-Shot Learners

> 📄 [论文原文](https://arxiv.org/abs/2005.14165) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, et al., **NeurIPS 2020**
> 领域标签: #预训练 #少样本学习 #规模法则
> 首次笔记: @zeng417 | 最后更新: 2026-10-05

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2005.14165) |
| 官方代码 | 无官方开源（论文以 API 形式发布） |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

GPT-3 把 decoder-only 语言模型放大到 175B 参数，发现**不做任何微调、只在 prompt 里放几个示例（in-context learning）**就能完成大量任务，把 NLP 从「微调范式」推向「prompt 范式」。

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
| 参数量 | 175B | 96 层、隐藏 12288、96 头、上下文 2048 |
| 训练数据 | 约 300B tokens | 过滤后 Common Crawl（约 570GB）+ WebText2 + 书籍 + 维基 |
| 核心指标 | TriviaQA few-shot 71.2 / LAMBADA 86.4 | 论文报告，多数任务 few-shot 超微调 SOTA |
| 训练成本 | 约 3.14×10^23 FLOPs | 相当于数百 V100 GPU·年，当时只有巨头玩得起 |

---

## 💬 讨论与备注

- 「in-context learning 到底在学什么」至今仍是活跃的研究问题
- 建议配合 Scaling Laws（Kaplan et al., 2020）一起读，理解"为什么要堆这么大"
- 论文 75 页、附录极长，重点读正文前 30 页即可

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
