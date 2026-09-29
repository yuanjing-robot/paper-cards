# 贡献指南

感谢你为论文知识卡片库做贡献！这份指南会告诉你怎么开始。

---

## 📋 目录

- [我是新人，从哪开始？](#我是新人从哪开始)
- [怎么贡献新的论文卡片？](#怎么贡献新的论文卡片)
- [怎么补充/修改现有卡片？](#怎么补充修改现有卡片)
- [怎么更新路线图？](#怎么更新路线图)
- [提交规范](#提交规范)
- [PR Review 流程](#pr-review-流程)
- [常见问题](#常见问题)

---

## 我是新人，从哪开始？

1. **先读路线图**：找到你的研究方向，从 Level 1 开始读几篇经典论文
2. **看范例卡片**：参考 [Attention Is All You Need](cards/llm/attention-is-all-you-need/) 的完整卡片
3. **选一篇论文**：找一篇你感兴趣、且还没人认领的论文
4. **认领任务**：在 Issue 中搜索或新建一个 "paper: xxx" 的 Issue，评论 "我来做" 认领

---

## 怎么贡献新的论文卡片？

### 第一步：准备工作

```bash
# 1. 克隆仓库
git clone https://github.com/your-org/paper-cards.git
cd paper-cards

# 2. 创建新分支
git checkout -b card/论文短标题
```

### 第二步：创建卡片文件夹

**方式 A：手动复制（推荐新手）**

```bash
# Windows PowerShell
Copy-Item -Recurse templates/paper-card-template cards/llm/论文短标题

# Mac/Linux
cp -r templates/paper-card-template cards/llm/论文短标题
```

**方式 B：用脚本（推荐经常用的）**

```bash
python scripts/add-paper.py \
  --title "Attention Is All You Need" \
  --field llm \
  --author "Vaswani et al." \
  --conference "NeurIPS 2017" \
  --paper-url "https://arxiv.org/abs/1706.03762" \
  --code-url "https://github.com/tensorflow/tensor2tensor"
```

### 第三步：填写卡片

#### ✅ 必须填写的卡片（至少这 3 个）

1. **`README.md`** — 论文速览卡（基本信息 + 各卡片状态索引）
2. **`01-reuse.md`** — ① 落地复用视角（工程向）
3. **`03-innovation.md`** — ③ 创新拆解视角（研究向）

#### ⭐ 推荐填写的卡片

4. **`05-sota-compare.md`** — ⑤ 对标 SOTA 视角（适合组会分享）
5. **`06-knowledge.md`** — ⑥ 知识沉淀视角（读完都可以补几句）

#### 🔸 可选填写的卡片

6. **`02-critique.md`** — ② 批判挑错视角（找研究方向的同学填）
7. **`04-hypothesis.md`** — ④ 学术假设视角（做理论的同学填）

> 💡 **卡片不用一次写满**。先把必选的 3 张写好就能提 PR。其他卡片可以后续慢慢补，或者由其他同学补充。

### 第四步：提交 PR

```bash
git add .
git commit -m "feat: add paper card for 论文标题"
git push origin card/论文短标题
```

然后在 GitHub 上创建 Pull Request：
- **标题**：`feat: add paper card for <论文标题>`
- **描述**：简要说明你写了哪些卡片、论文的领域
- **Reviewer**：会自动分配给对应方向的 Team（通过 CODEOWNERS）

---

## 怎么补充/修改现有卡片？

发现某篇论文的卡片可以补充？或者发现了错误？

1. 直接在对应文件上修改
2. 提交 PR，标题用 `update: <论文标题> - <哪张卡/什么修改>`
3. 比如：`update: attention-is-all-you-need - add reproduce pitfalls`

**鼓励的行为**：
- 补充你复现后发现的新坑 → 更新 05-pitfalls 或 06-knowledge
- 补充新的相关论文 → 更新 README 的相关论文部分
- 修正错误信息
- 把自己的新理解加进去

---

## 怎么更新路线图？

路线图是团队知识地图的重要组成部分，更新方式：

1. 在对应路线图文件中修改（如 `roadmaps/llm-roadmap.md`）
2. 确保新增的论文链接到 `cards/` 中对应的卡片文件夹
3. 提交 PR，标题：`docs: update xxx roadmap - 说明更新内容`
4. 由对应方向的 maintainer review

> ⚠️ 注意：路线图中的论文应该都有对应的卡片（至少是速览卡）。如果还没有卡片，先建卡片再加入路线图。

---

## 提交规范

### 命名规范

| 项目 | 规范 | 示例 |
|------|------|------|
| 文件夹名 | 全小写，空格用 `-` 连接 | `attention-is-all-you-need` |
| 分支名 | `card/论文短标题` 或 `update/说明` | `card/llama2` |
| Commit 信息 | `feat:` 新增 · `update:` 更新 · `fix:` 修复 · `docs:` 文档 | `feat: add card for GPT-4` |
| PR 标题 | 同 commit 规范 | `feat: add paper card for GPT-4` |

### 写作规范

1. **语言**：中文或英文均可，但**同一领域内保持一致**（建议中文写笔记，专业术语保留英文）
2. **图片**：放在对应论文的 `assets/` 目录下，使用相对路径引用
3. **公式**：使用 LaTeX 语法（GitHub 原生支持）
4. **链接**：论文链接优先用 arXiv 或官方论文页面，代码链接用 GitHub
5. **署名**：在 README 的"维护者"处加上你的 GitHub ID

### 质量要求

- ✅ 内容准确，不编造信息
- ✅ 有自己的思考和理解（不是单纯翻译论文）
- ✅ 引用数据标注来源（哪张表、哪个实验）
- ❌ 不要大段复制论文原文
- ❌ 不要只放截图不写文字说明
- ❌ 不要为了凑字数写空话

---

## PR Review 流程

### 谁来 review？

根据你修改的内容，自动分配 reviewer：

| 修改内容 | 自动分配给 |
|---------|-----------|
| LLM 方向的卡片 | `@your-org/llm-group` |
| CV 方向的卡片 | `@your-org/cv-group` |
| 路线图 | 对应方向的 maintainer |
| 模板/仓库配置 | 所有 maintainer |

### Review 看什么？

1. **格式**：是否符合模板规范
2. **准确性**：内容是否和论文一致，有没有明显错误
3. **质量**：有没有自己的思考，是不是简单翻译
4. **完整性**：必选卡片是否都填了

### Review 通过标准

- 至少 1 位对应方向的成员 approve
- 所有评论都已回复 / 解决
- CI 检查通过（如果有配置）

---

## 常见问题

### Q：我可以只写一张卡片吗？

**A：可以。** 比如你做了复现，就只更新 ① 落地复用和 ⑥ 知识沉淀卡片。卡片是模块化的，不同的人可以补不同的部分。

### Q：论文很新，还没有复现代码，落地复用卡片怎么填？

**A：能填多少填多少。** 至少填 Input（需要什么数据、硬件）和 Cost（论文里报告的训练成本），Operation 可以先写"待复现"，Gain 填论文报告的结果。

### Q：批判挑错卡片会不会太杠精了？

**A：不会。** 批判性思维是科研的基本素养。批判挑错卡片的目的不是否定论文，而是：
1. 帮你找到真正的研究空白
2. 让团队清楚方法的边界和适用范围
3. 避免盲目跟风

关键是：**有理有据，不吹毛求疵。**

### Q：知识沉淀卡片不知道写什么怎么办？

**A：先从"一句话收获"开始。** 哪怕只写一条真的有用的经验，也比凑十条空话强。随着积累会越来越多。

可以问自己：
- 读完这篇论文，我记住了什么？
- 有什么东西我下周做项目可能用到？
- 有什么坑我以后要注意？

### Q：我想贡献但是怕写错怎么办？

**A：大胆提 PR！** Review 机制就是用来纠错的。没有人一开始就能写出完美的卡片，大家都是在 review 中共同进步的。

---

有其他问题？欢迎在 Issue 中提问，或者直接在群里问～
