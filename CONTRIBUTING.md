# 贡献指南

感谢你为具身智能论文知识卡片库做贡献！这份指南会告诉你怎么开始。

---

## 📋 目录

- [我是新人，从哪开始？](#我是新人从哪开始)
- [怎么贡献新的论文卡片？](#怎么贡献新的论文卡片)
- [怎么补充/修改现有卡片？](#怎么补充修改现有卡片)
- [提交规范](#提交规范)
- [PR Review 流程](#pr-review-流程)
- [常见问题](#常见问题)

---

## 我是新人，从哪开始？

1. **看首页总览**：打开仓库首页 README，找到你感兴趣的大方向
2. **看范例卡片**：打开 `cards/` 下任意方向的论文卡片，参考其结构和内容
3. **选一篇论文**：找一篇你感兴趣、且还没人认领的论文
4. **认领任务**：在 Issue 中搜索或新建一个 "paper: xxx" 的 Issue，评论 "我来做" 认领

---

## 怎么贡献新的论文卡片？

### 第一步：准备工作

```bash
# 1. 克隆仓库
git clone https://github.com/yuanjing-robot/paper-cards.git
cd paper-cards

# 2. 拉取最新代码
git checkout main
git pull origin main

# 3. 创建新分支
git checkout -b card/论文短标题
```

### 第二步：创建卡片文件夹

**方式 A：用脚本（推荐）**

```bash
python scripts/add-paper.py \
  --title "RT-2: Vision-Language-Action Models" \
  --field 03-embodied-llm \
  --author "Brohan et al." \
  --conference "CoRL 2023" \
  --paper-url "https://arxiv.org/abs/2307.15818"
```

论文默认直接放在大方向目录下。如果想按子方向组织（如 `vla-models`），加 `--subfield vla-models` 即可，子方向目录不存在时脚本会自动创建。

脚本会自动：
- 创建论文卡片文件夹（3 个文件）
- 填好 README 里的基本信息
- 更新所在目录 README 的论文索引表

**方式 B：手动复制**

```bash
# Windows PowerShell
Copy-Item -Recurse templates/paper-card-template cards/大方向/论文短标题

# Mac/Linux
cp -r templates/paper-card-template cards/大方向/论文短标题
```

> ⚠️ 注意把 `大方向` 替换为实际目录名，比如 `cards/03-embodied-llm/rt-2`；如需子方向再加一层，如 `cards/03-embodied-llm/vla-models/rt-2`

### 第三步：填写卡片

每篇论文有 3 个文件，填写优先级如下：

#### ✅ 必须填写的文件

1. **`README.md`** — 速览卡（论文基本信息 + 关键数据 + 导航）
2. **`reading-notes.md`** — 深度阅读

#### ⭐ 推荐填写的文件

3. **`translation.md`** — 论文全文中文翻译

> 💡 **不用一次写满所有文件**。先把 README 和深度阅读写好就能提 PR，翻译可以后续慢慢补，也可以由其他同学补充。

### 第四步：提交 PR

```bash
git add .
git commit -m "feat: add paper card for 论文标题"
git push origin card/论文短标题
```

然后在 GitHub 上创建 Pull Request：
- **标题**：`feat: add paper card for <论文标题>`
- **描述**：简要说明你填了哪些文件、论文属于哪个方向
- **Reviewer**：会自动分配给对应方向的 Team（通过 CODEOWNERS）

---

## 怎么补充/修改现有卡片？

发现某篇论文的卡片可以补充？或者发现了错误？

1. 直接在对应文件上修改
2. 提交 PR，标题用 `update: <论文标题> - <什么修改>`
3. 比如：`update: 论文短标题 - 补充说明`

**鼓励的行为**：
- 补充翻译（translation.md）
- 在深度阅读的「个人收获」部分补充思考
- 完善深度阅读中的某个角度
- 修正错误信息

---

## 提交规范

### 命名规范

| 项目 | 规范 | 示例 |
|------|------|------|
| 论文文件夹名 | 全小写，空格用 `-` 连接 | `paper-title-example` |
| 分支名 | `card/论文短标题` 或 `update/说明` | `card/rt-2` |
| Commit 信息 | `feat:` 新增 · `update:` 更新 · `fix:` 修复 · `docs:` 文档 | `feat: add card for RT-2` |
| PR 标题 | 同 commit 规范 | `feat: add paper card for RT-2` |

### 写作规范

1. **语言**：中文为主，专业术语保留英文
2. **图片**：放在对应论文的 `assets/` 目录下，使用相对路径引用
3. **公式**：使用 LaTeX 语法（GitHub 原生支持）
4. **链接**：论文链接优先用 arXiv，代码链接用 GitHub
5. **署名**：在 README 的"首次笔记"处加上你的 GitHub ID

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

根据你修改的内容，自动分配 reviewer（通过 CODEOWNERS 配置）：

| 修改内容 | 自动分配给 |
|---------|-----------|
| A. 感知与认知方向（01-03） | `@yuanjing-robot/perception-group` |
| B. 学习与模型方向（04-07） | `@yuanjing-robot/learning-group` |
| C. 行动与交互方向（08-10） | `@yuanjing-robot/action-group` |
| D. 系统与生态方向（11-15） | `@yuanjing-robot/systems-group` |
| 模板/仓库配置 | `@yuanjing-robot/maintainers` |

### Review 看什么？

1. **格式**：是否符合模板规范
2. **准确性**：内容是否和论文一致，有没有明显错误
3. **质量**：有没有自己的思考，是不是简单翻译
4. **完整性**：必须填写的文件是否都填了

### Review 通过标准

- 至少 1 位对应方向的成员 approve
- 所有评论都已回复 / 解决
- CI 检查通过（如果有配置）

---

## 常见问题

### Q：深度阅读的角度都要写吗？

**A：不用。** 角度按论文特点取舍，建议至少写「核心方法」和「个人收获」。其他角度（问题动机、关键结果、批判思考、延伸阅读）可以后续补充，也可以由其他同学补。

### Q：翻译要全文翻译吗？

**A：是的，translation.md 是全文翻译。** 如果一次翻不完，可以分多次提交，每次翻译一个章节。也可以多人协作，分章节翻译。

### Q：深度阅读里的「个人收获」写什么？

**A：写你自己的思考。** 不是复述论文内容，而是：
- 你觉得这篇论文的核心价值是什么
- 它的方法你是怎么理解的
- 对你有什么启发
- 读完之后记住了什么

### Q：论文很新，还没有复现代码，落地复用视角怎么填？

**A：能填多少填多少。** 至少填 Input（需要什么数据、硬件）和 Cost（论文里报告的训练成本），Operation 可以先写"待复现"，Gain 填论文报告的结果。

### Q：我想贡献但是怕写错怎么办？

**A：大胆提 PR！** Review 机制就是用来纠错的。没有人一开始就能写出完美的卡片，大家都是在 review 中共同进步的。

---
