# 深度阅读：Language Models are Few-Shot Learners

> 📄 对应论文：[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
> 整理者：@zeng417
> 最后更新：2026-10-08

---

> 💡 深度阅读与个人理解合并为一份。以下角度**按论文特点取舍**，不要求全部填写；建议至少写「核心方法」和「个人收获」。

## 1. 问题与动机

- 当时的主流范式是「预训练 + 下游任务微调」。它虽让架构变得任务无关，但**每个新任务仍需要成千上万条标注样本**做微调，这限制了方法的适用范围。
- 作者给出三条反对理由：
  1. **实用性**：有用任务种类极多（改语法、按抽象概念举例、评论小说……），为每个任务收集大规模监督数据很困难；
  2. **伪相关 / 过拟合**：模型越大、任务分布越窄，越容易学到训练分布里的伪相关；微调后模型在 benchmark 上「看似达到人类水平」，可能高估了真实任务能力；
  3. **不像人**：人类只需一句自然语言指令或极少量示例就能上手新任务，还能在任务间自由切换。
- 同时，Kaplan 等人的 scaling law 表明 loss 随参数量、数据量、算力呈平滑幂律下降。作者想问：**in-context learning（上下文学习）的能力，是否也会随规模一起大幅增强？**

## 2. 核心方法

- **模型**：GPT-3，decoder-only 自回归 Transformer，与 GPT-2 同架构（改进初始化、pre-norm、可逆 BPE），唯一结构改动是注意力层交替使用稠密与局部带状稀疏模式。上下文窗口 2048，共训练 8 个规模到 175B。所有模型都训练了约 3000 亿 tokens。
- **数据**：以 Common Crawl 为主，做了三步提质——(1) 按与高质量语料的相似度过滤；(2) 文档级 + 跨数据集模糊去重；(3) 混入 WebText2、Books1/2、英文维基。高质量数据集采样更多遍（WebText2 2.9、Books1 1.9、Wikipedia 3.4），Common Crawl 与 Books2 则不到一遍（0.44 / 0.43），用轻微过拟合换更高质量的数据。
- **训练**：大模型用更大 batch、更小学习率；Adam（β1=0.9，β2=0.95，ε=1e-8），学习率在 300B tokens 上余弦衰减，含 3.75 亿 token 的 warmup；175B 用 batch 320 万 tokens、LR 0.6e-4。用模型并行 + 梯度检查点。
- **评测**：不做任何梯度更新，任务完全靠 prompt 指定。三种设定——zero-shot（只给自然语言指令）、one-shot（1 个示例）、few-shot（塞进上下文窗口的尽可能多示例，通常 10–100 个）。few-shot 示例从训练集里取，不用验证/测试集标签。

## 3. 关键结果

- **完形填空 / 语言建模**：LAMBADA few-shot 达到 **86.4%**，超过当时的 SOTA（68.0）；Penn Treebank 上 zero-shot 困惑度 **20.5**，优于此前 SOTA 35.8。
- **闭卷问答**：TriviaQA zero-shot 64.3% → one-shot 68.0% → few-shot **71.2%**，在闭卷设定下超过微调模型；Natural Questions few-shot **29.9%**，仍落后微调的 44.5。
- **对话式问答**：CoQA zero-shot 81.5 → one-shot 84.0 → few-shot **85.0 F1**（论文报告）。
- **即时适应类任务**：打乱字母还原、单词字母重排、**三位数算术**（few-shot 明显优于 zero-shot）、以及“看一次定义就能在句子里用新词”，都能在 few-shot 下做出不错效果。
- **生成质量**：few-shot 生成的新闻文章，人类评审区分真伪的准确率仅约 **52%**，接近随机水平（附录 E）。
- **失效场景**：ANLI 的 few-shot 只有 36.8 / 34.0 / 40.2（随机 33%），几乎不比瞎猜好；RACE-h 46.8、RACE-m 58.1 明显偏低；Winograd（WSC）few-shot 88.6，未达微调 SOTA（90.1）。说明 few-shot 并非万能。

## 4. 批判性思考

- **“在学”还是“在认”？** 论文自己承认无法排除模型只是“认出”了预训练时见过的模式，而非真正从示例中学到新任务——in-context learning 的本质仍是开放问题。
- **规模不是全部**：有一批任务（ANLI、RACE、QuAC 等）随规模提升收益很小甚至停滞，说明存在 scaling 不能直接解决的能力短板。
- **数据污染**：训练语料来自网络，测试集内容可能泄漏进预训练。作者虽做了检测与标注，但因过滤 bug 仍残存重叠，且重训不可行——这提示大模型评测的可信度需要专门的方法论保障。
- **成本与可及性**：175B 的训练算力约 3.14×10²³ FLOPs，推理也昂贵，实际部署门槛高，且不利于学术复现。
- **prompt 敏感性**：结果高度依赖 prompt 措辞与格式；论文提到某些任务（如需要同时比较两个句子的 SuperGLUE 任务）因 prompt 形式不匹配而大幅掉分，说明评测本身对提示工程很敏感。

## 5. 个人收获

- 最大的观念冲击是：**“用文本把任务讲清楚”本身就可以是一种接口**。这把任务适配从“改模型/改参数”转移到“写好 prompt”，是后来 prompt engineering、few-shot、乃至 instruction tuning 的思想源头。
- scaling law + in-context learning 的组合，给出了“规模即能力”的可预测叙事：模型足够大时，很多任务的 zero/few-shot 表现会平滑提升，这为后续大模型路线提供了实证依据。
- 也学到评测要“看两面”：作者既列了亮眼 SOTA，也系统列出失败任务和污染风险，这种“诚实呈现弱点”的写法值得学习。
- 和已有知识的连接：GPT-3 的 few-shot 与 InstructGPT 的 RLHF 是同一问题的两个解法——前者靠 prompt 示例激活能力，后者靠对齐让模型更听指令；延伸到具身领域，可以把“language prompt 作为任务接口”迁移到 embodied agent 的任务泛化上。

## 6. 延伸阅读（可选）

- GPT-2: Language Models are Unsupervised Multitask Learners
- Scaling Laws for Neural Language Models (Kaplan et al., 2020)
- GPT-3 官方博客 "Language Models are Few-Shot Learners"
- InstructGPT: Training language models to follow instructions with human feedback

---

> ✍️ **写作提示**
> - 引用数据标明出处（论文表 X / 图 Y）
> - 不编造信息，不确定的内容标注「待确认」
> - 不要复述论文原文，用自己的话写