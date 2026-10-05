# 精读笔记：BERT

> 📄 对应论文：[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
> 整理者：@zeng417
> 最后更新：2026-10-05

---

## 1. 问题与动机

- 2018 年之前，NLP 的标准做法是「任务专属模型 + 从零训练」，标注数据少、迁移差。
- GPT-1 证明了「预训练 + 微调」可行，但语言模型是**从左到右的单向**结构，每个位置只能看到前文，对句法、指代这类需要看「右边界」的任务是硬伤。
- 核心问题：**如何让 Transformer encoder 学到深度双向的上下文表示**？直接像语言模型那样双向预测下个词会被每个词"自己看见自己"（退化解），必须换一种预训练目标。

## 2. 核心方法

- **架构**：纯 Transformer encoder，base 12 层/768 隐藏/12 头/110M，large 24 层/1024 隐藏/16 头/340M。
- **MLM（Masked Language Model）**：随机遮盖 15% 的 token；其中 80% 换成 `[MASK]`、10% 换成随机词、10% 保留。混合策略是为了缓解「预训练见 `[MASK]`、微调见真词」的分布不一致。
- **NSP（Next Sentence Prediction）**：二分类判断两句 B 是否真的是 A 的下文，意图让模型理解句间关系（QA、NLI 需要）。
- **输入设计**：`[CLS]` 句 A `[SEP]` 句 B，加 segment embedding 区分句对；`[CLS]` 的最终向量当作整句分类的汇总表示。
- **两阶段使用**：先在无标注语料上预训练，再在小任务上整模型微调（只在输出层加一个轻量头）。

## 3. 关键结果

- 论文报告：GLUE 80.5（large，比当时最优系统 +7.0 点）；SQuAD v1.1 F1 93.2；MultiNLI 86.7 等，**11 项 NLP 任务同时刷新 SOTA**。
- 消融结论：去掉 MLM 只留左向 LM，GLUE 分数大幅下降 → 双向预训练是主要增益来源；NSP 对 NLI/QA 类有帮助（后来被 RoBERTa 部分推翻）。
- 小样本收益明显：低资源任务上微调 BERT 远超从零训练。

## 4. 批判性思考

- **MLM 的独立性假设**：被遮盖的 15% 词被假设为相互独立，忽略了遮盖词之间的联合分布，这是 MLM 与真实语言生成之间的结构性偏差。
- **预训练-微调不一致**：微调阶段永远见不到 `[MASK]`，生成类任务（写句子）用 BERT 天然别扭，只适合理解类任务。
- **NSP 作用存疑**：RoBERTa 用连续长句、去掉 NSP 后效果更好，说明 NSP 任务设计过于简单。
- **512 token 长度限制**：长文档、长代码场景处理不了。
- **微调不稳定**：小数据集上不同随机种子结果波动大，需要小心调参。

## 5. 个人收获

- 最大的收获是**范式**而不是模型本身：「预训练通用表示 + 下游微调」从此成为 NLP（后来是整个 AI）的标准工作流，现在的 instruction tuning、RLHF 都建立在这个两阶段思想上。
- 「遮盖重建」是一种通用的自监督思路，视觉里的 MAE（Masked Autoencoder）几乎就是 BERT MLM 的图像版——跨领域方法论是通的。
- 工程启发：`[CLS]` + 轻量输出头的设计让一个预训练底座可以低成本适配几十个任务，这种"一底座多头"的结构在今天的 embedding 检索、重排模型里依然常见。

## 6. 延伸阅读

- RoBERTa（Liu et al., 2019）：去掉 NSP、加大数据与时长的 BERT 复盘
- ELECTRA（Clark et al., 2020）：用替换词判别代替 MLM，样本效率更高
- MAE（He et al., 2022）：MLM 思想在视觉中的复现
- Transformer 原始论文卡片：[Attention Is All You Need](../../03-embodied-llm/vla-models/attention-is-all-you-need/)
