# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

> 📄 [论文原文](https://arxiv.org/abs/2305.10601) · 💻 [官方代码](https://github.com/princeton-nlp/tree-of-thought-llm) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Shunyu Yao, Dian Yu, Jeffrey Zhao et al., **NeurIPS 2023**
> 领域标签: #思维树 #搜索 #推理
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2305.10601) |
| 官方代码 | [GitHub](https://github.com/princeton-nlp/tree-of-thought-llm) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把推理组织成可搜索的树：LLM 生成中间想法、自评估、可回溯与多路探索，将"系统 2"式深思带入大模型解题。

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
| 参数量 | GPT-4 验证 | 推理框架不训练 |
| 训练数据 | Game of 24 / 写作 / 填字 | 3 类任务 |
| 核心指标 | Game of 24 4% → 74% | IO 提示 vs ToT |
| 训练成本 | API 调用成本 | 无训练 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分
