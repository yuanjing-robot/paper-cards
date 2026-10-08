# Language Models are Few-Shot Learners

> 📄 [论文原文](https://arxiv.org/abs/2005.14165) · 📝 [深度阅读](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Brown et al. (OpenAI), **NeurIPS 2020**
> 领域标签: #大模型 #预训练 #In-context Learning #少样本 #Scaling Law
> 首次笔记: @zeng417 | 最后更新: 2026-10-08

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) |
| 代码 | - （论文未提供官方代码） |
| 成员实现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把自回归语言模型放大到 1750 亿参数（GPT-3）后，无需任何梯度更新或微调，仅靠 prompt 里给出的任务描述和少量示例（in-context learning），就能在众多 NLP 任务上接近甚至超过当时的微调 SOTA。

---

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 📝 深度阅读 | 精读 + 个人理解 | [reading-notes.md](reading-notes.md) |
| 🌐 论文翻译 | 全文中文翻译 | [translation.md](translation.md) |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | 175B（最大版本） | 共 8 个规模：125M / 350M / 760M / 1.3B / 2.7B / 6.7B / 13B / 175B，跨三个数量级 |
| 架构 | 96 层 · d_model 12288 · 96 头 · 上下文 2048 | 沿用 GPT-2 结构，注意力改为“稠密 / 局部带状稀疏”交替（Sparse Transformer） |
| 训练数据 | ~300B tokens | 混合配比：Common Crawl(过滤后) 60% · WebText2 22% · Books1 8% · Books2 8% · Wikipedia 3% |
| 核心指标 | LAMBADA few-shot 86.4%；TriviaQA few-shot 71.2%（closed-book SOTA）；CoQA few-shot 85.0 F1 | 全部为 few-shot，无微调 |
| 生成质量 | 人类判别“GPT-3 生成新闻 vs 真人新闻”的准确率仅约 52% | 接近随机猜测，见附录 E |
| 训练算力 | 约 3.14×10²³ FLOPs（≈3640 PF-days） | 论文附录 D；对应 175B 模型 |

---

## 💬 讨论与备注

- 数据污染：因为训练语料来自 Common Crawl，测试/验证集内容可能被“看到”。作者开发了一套检测工具，对大部分数据集影响很小，但对少数数据集需打星号标注（详见论文第 4 节）。
- 论文只评测 zero/one/few-shot，未做传统微调，因此 few-shot 与微调 SOTA 的对比需注意设定差异。

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「深度阅读」
> - 想看读后的思考与收获？看「深度阅读」的个人收获部分