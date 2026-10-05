#!/usr/bin/env python3
"""
一键创建论文卡片文件夹

用法:
    python scripts/add-paper.py \
      --title "Attention Is All You Need" \
      --field 03-embodied-llm \
      --author "Vaswani et al." \
      --conference "NeurIPS 2017" \
      --paper-url "https://arxiv.org/abs/1706.03762" \
      --code-url "https://github.com/tensorflow/tensor2tensor"

参数:
    --title         论文标题（必填）
    --field         大方向目录名，如 03-embodied-llm（必填）
    --subfield      子方向目录名（可选；不填则论文直接放在大方向目录下，填了且目录不存在会自动创建）
    --author        作者列表（可选）
    --conference    会议/期刊 + 年份（可选）
    --paper-url     论文链接（可选）
    --code-url      官方代码链接（可选）
    --tags          标签，用逗号分隔（可选）
    --output-dir    输出目录，默认 cards/（可选）
"""

import argparse
import shutil
import re
from pathlib import Path


def slugify(title: str) -> str:
    """将论文标题转为文件夹名：全小写，空格转 -，移除非字母数字字符"""
    title = re.sub(r'[^a-zA-Z0-9\s-]', '', title)
    title = re.sub(r'\s+', '-', title.strip().lower())
    title = re.sub(r'-+', '-', title)
    return title.strip('-')


def update_subfield_readme(subfield_readme: Path, title: str, conference: str,
                           paper_url: str, folder_name: str):
    """自动更新子方向 README，把新论文加到论文列表里"""
    if not subfield_readme.exists():
        return False

    content = subfield_readme.read_text(encoding='utf-8')

    # 找到论文列表表格，在 "_待补充_" 那一行之前插入新论文
    # 或者直接在表格最后一行之前插入
    paper_md = f"| [{title}]({folder_name}/) | {conference or '-'} | "
    if paper_url:
        paper_md += f"[📄 原文]({paper_url}) | "
    else:
        paper_md += "- | "
    paper_md += f"[📝 精读笔记]({folder_name}/reading-notes.md) | "
    paper_md += f"[🌐 翻译]({folder_name}/translation.md) |"

    # 如果有 "_待补充_" 的占位行，替换掉
    if '_待补充_' in content:
        content = content.replace(
            "| _待补充_ | - | - | - | - |",
            paper_md
        )
    else:
        # 在表格最后插入（找 "---" 分隔线后的第一行表格内容的位置）
        # 简单做法：在表格末尾的 "---" 之前加一行
        # 找 "论文列表" 之后的表格
        lines = content.split('\n')
        in_table = False
        header_found = False
        insert_idx = -1
        for i, line in enumerate(lines):
            if '论文列表' in line:
                in_table = True
                continue
            if in_table and line.startswith('| 论文 |'):
                header_found = True
                continue
            if header_found and line.startswith('|---'):
                continue
            if header_found and line.startswith('|'):
                # 找到了第一行数据，继续往后找最后一行数据
                insert_idx = i + 1
                # 继续找直到表格结束
                j = i
                while j < len(lines) and lines[j].startswith('|'):
                    j += 1
                insert_idx = j
                break

        if insert_idx > 0:
            lines.insert(insert_idx, paper_md)
            content = '\n'.join(lines)

    subfield_readme.write_text(content, encoding='utf-8')
    return True


def main():
    parser = argparse.ArgumentParser(description='一键创建论文卡片文件夹')
    parser.add_argument('--title', required=True, help='论文标题')
    parser.add_argument('--field', required=True,
                        help='大方向目录名，如 03-embodied-llm')
    parser.add_argument('--subfield', default='',
                        help='子方向目录名（可选；不填则论文直接放在大方向目录下）')
    parser.add_argument('--author', default='', help='作者列表')
    parser.add_argument('--conference', default='', help='会议/期刊 + 年份')
    parser.add_argument('--paper-url', default='', help='论文链接')
    parser.add_argument('--code-url', default='', help='官方代码链接')
    parser.add_argument('--tags', default='', help='标签，用逗号分隔')
    parser.add_argument('--output-dir', default='cards', help='输出目录，默认 cards/')
    args = parser.parse_args()

    # 仓库根目录（脚本在 scripts/ 下，往上一层就是根目录）
    repo_root = Path(__file__).parent.parent
    template_dir = repo_root / 'templates' / 'paper-card-template'
    field_dir = repo_root / args.output_dir / args.field

    # 检查大方向目录是否存在
    if not field_dir.exists():
        print(f'❌ 大方向目录不存在：{field_dir}')
        print(f'   可用的大方向：')
        cards_dir = repo_root / args.output_dir
        if cards_dir.exists():
            for d in sorted(cards_dir.iterdir()):
                if d.is_dir() and not d.name.startswith('.'):
                    print(f'     - {d.name}/')
        return

    # 子方向可选：不填则论文直接放在大方向目录下；填了且不存在则自动创建
    output_dir = field_dir
    if args.subfield:
        output_dir = field_dir / args.subfield
        if not output_dir.exists():
            output_dir.mkdir(parents=True)
            (output_dir / 'README.md').write_text(
                f"# {args.subfield}\n\n> 子方向说明（待补充）\n\n"
                "## 📚 论文列表\n\n"
                "| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |\n"
                "|------|----------|------|---------|------|\n"
                "| _待补充_ | - | - | - | - |\n",
                encoding='utf-8')
            print(f'✅ 子方向目录不存在，已自动创建：{output_dir}')

    if not template_dir.exists():
        print(f'❌ 模板文件夹不存在：{template_dir}')
        return

    # 生成文件夹名
    folder_name = slugify(args.title)
    target_dir = output_dir / folder_name

    if target_dir.exists():
        print(f'❌ 目标文件夹已存在：{target_dir}')
        print(f'   如果要重新生成，请先删除该文件夹')
        return

    # 复制模板
    shutil.copytree(template_dir, target_dir)
    print(f'✅ 已创建卡片文件夹：{target_dir}')

    # 替换 README.md 中的占位符
    readme_path = target_dir / 'README.md'
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')

        # 替换标题
        content = content.replace('[论文标题]', args.title)

        # 替换作者和会议
        author_line = f'{args.author}, **{args.conference}**' if args.author and args.conference else \
                      f'{args.author}' if args.author else \
                      f'**{args.conference}**' if args.conference else \
                      '作者, **会议/期刊** 年份'
        content = content.replace('作者列表, **会议/期刊** 年份', author_line)

        # 替换标签
        if args.tags:
            tags = ' '.join(f'#{t.strip()}' for t in args.tags.split(','))
            content = content.replace('#标签1 #标签2 #标签3', tags)

        # 替换论文链接（资源链接表 + 标题下方）
        if args.paper_url:
            content = content.replace(
                '[arXiv](https://arxiv.org/abs/xxxx.xxxxx)',
                f'[论文链接]({args.paper_url})'
            )
            content = content.replace(
                '[论文原文](https://arxiv.org/abs/xxxx.xxxxx)',
                f'[论文原文]({args.paper_url})'
            )

        # 替换代码链接（资源链接表 + 标题下方）
        if args.code_url:
            content = content.replace(
                '[GitHub](https://github.com/xxx)',
                f'[GitHub]({args.code_url})'
            )
            content = content.replace(
                '[官方代码](https://github.com/xxx)',
                f'[官方代码]({args.code_url})'
            )

        readme_path.write_text(content, encoding='utf-8')
        print(f'✅ 已更新 README.md')

    # 自动更新所在目录的 README（把新论文加到索引里）
    index_readme = output_dir / 'README.md'
    if update_subfield_readme(index_readme, args.title, args.conference,
                              args.paper_url, folder_name):
        print(f'✅ 已更新论文索引：{index_readme}')

    # 更新 reading-notes.md 的标题和链接（先替换链接形式，避免丢失方括号）
    notes_path = target_dir / 'reading-notes.md'
    if notes_path.exists() and args.paper_url:
        content = notes_path.read_text(encoding='utf-8')
        content = content.replace(
            '[论文标题](https://arxiv.org/abs/xxxx.xxxxx)',
            f'[{args.title}]({args.paper_url})')
        content = content.replace('[论文标题]', args.title)
        content = content.replace('https://arxiv.org/abs/xxxx.xxxxx', args.paper_url)
        notes_path.write_text(content, encoding='utf-8')

    # 更新 translation.md 的标题和链接（同上）
    translation_path = target_dir / 'translation.md'
    if translation_path.exists() and args.paper_url:
        content = translation_path.read_text(encoding='utf-8')
        content = content.replace(
            '[论文标题](https://arxiv.org/abs/xxxx.xxxxx)',
            f'[{args.title}]({args.paper_url})')
        content = content.replace('[论文标题]', args.title)
        content = content.replace('https://arxiv.org/abs/xxxx.xxxxx', args.paper_url)
        translation_path.write_text(content, encoding='utf-8')

    print()
    print('🎉 论文卡片创建成功！')
    print(f'   路径：{target_dir.relative_to(repo_root)}')
    print()
    print('📝 下一步：')
    print(f'   1. cd {target_dir.relative_to(repo_root)}')
    print('   2. 填 README.md（速览卡 + 关键数据）')
    print('   3. 填 reading-notes.md（精读 + 个人理解，角度灵活取舍）')
    print('   4. 补充 translation.md（翻译，可选）')
    print('   5. 提 PR')
    print()
    print('🔗 论文索引已自动更新，刷新即可看到新论文')


if __name__ == '__main__':
    main()
