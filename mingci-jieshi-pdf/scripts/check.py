#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""名词解释项目验收脚本。

一次查清四件事：
  1. 索引里的双链数量、名字，与卡片文件是否 1:1 对应（缺链 / 死链 / 多余文件）
  2. 每章卡片序号是否从 01 起连续、无重号、无跳号
  3. 索引表里的「PDF/书页/段」与卡片头行写的是否一致
  4. 卡片行数是否落在合理区间（太短多半是漏抄定义，太长多半是注水）

用法（Windows，务必带 UTF-8 环境）：
  $env:PYTHONIOENCODING='utf-8'
  & 'D:\\tools\\Miniconda\\python.exe' -X utf8 check.py --root "<项目根>" --chapters 16

退出码：0 = 全部通过；1 = 有问题（细节打印在「问题」段）。
"""

import argparse
import os
import re
import sys

LINK_RE = re.compile(r"\[\[(\d{2})\s+([^\]|\n]+?)\]\]")
# 索引表行：| [[01 术语]] | english | 64/37/2 |
ROW_RE = re.compile(
    r"^\|\s*\[\[(\d{2})\s+([^\]|\n]+?)\]\]\s*\|([^|\n]*)\|([^|\n]*)\|",
    re.M,
)
HEAD_RE = re.compile(r"PDF/书页/段[^\n]*?:\s*([^\n]+)")


def pdf_page_of(cell):
    """从 '64/37/2' 或 '64 / 37 / 2' 里取 PDF 页码。"""
    m = re.match(r"\s*(\d+)", cell or "")
    return m.group(1) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="项目根目录（含 索引/ 与 零散的概念/）")
    ap.add_argument("--index-dir", default="索引")
    ap.add_argument("--cards-dir", default="零散的概念")
    ap.add_argument("--chapters", type=int, default=1, help="共几章（1..N）")
    ap.add_argument("--index-name", default="{n:02d}名词解释.md")
    ap.add_argument("--min-lines", type=int, default=25)
    ap.add_argument("--max-lines", type=int, default=90)
    args = ap.parse_args()

    idx_dir = os.path.join(args.root, args.index_dir)
    cards_root = os.path.join(args.root, args.cards_dir)
    problems = []
    total_links = total_files = 0

    print(f"{'章':<4}{'双链':>6}{'卡片':>6}  状态")
    print("-" * 40)

    for n in range(1, args.chapters + 1):
        ipath = os.path.join(idx_dir, args.index_name.format(n=n))
        if not os.path.exists(ipath):
            problems.append(f"{n:02d} 章：缺索引文件 {ipath}")
            print(f"{n:02d}      索引缺失")
            continue

        folders = [d for d in os.listdir(cards_root) if d.startswith(f"{n:02d} ")]
        if not folders:
            problems.append(f"{n:02d} 章：缺章文件夹（{cards_root}\\{n:02d} *）")
            print(f"{n:02d}      章文件夹缺失")
            continue
        cdir = os.path.join(cards_root, sorted(folders)[0])

        files = sorted(x[:-3] for x in os.listdir(cdir) if x.endswith(".md"))
        text = open(ipath, encoding="utf-8").read()
        links = [f"{m.group(1)} {m.group(2).strip()}" for m in LINK_RE.finditer(text)]
        rows = [
            (f"{m.group(1)} {m.group(2).strip()}", m.group(4).strip())
            for m in ROW_RE.finditer(text)
        ]

        total_links += len(links)
        total_files += len(files)

        file_set, link_set = set(files), set(links)
        if file_set - link_set:
            problems.append(f"{n:02d} 章：有卡片没进索引 → {sorted(file_set - link_set)[:5]}")
        if link_set - file_set:
            problems.append(f"{n:02d} 章：索引指向不存在的卡片 → {sorted(link_set - file_set)[:5]}")
        dup = sorted({x for x in links if links.count(x) > 1})
        if dup:
            problems.append(f"{n:02d} 章：索引里重复的双链 → {dup[:5]}")

        seq = []
        bad_name = []
        for f in files:
            m = re.match(r"(\d+)", f)
            if m:
                seq.append(int(m.group(1)))
            else:
                bad_name.append(f)
        if bad_name:
            problems.append(f"{n:02d} 章：文件名不以序号开头 → {bad_name[:5]}")
        if seq != list(range(1, len(seq) + 1)):
            problems.append(f"{n:02d} 章：序号不连续 {seq[:20]}")

        page_bad, lines_bad = [], []
        for name, page in rows:
            cpath = os.path.join(cdir, name + ".md")
            if not os.path.exists(cpath):
                continue
            ctext = open(cpath, encoding="utf-8").read()
            hm = HEAD_RE.search(ctext)
            card_page = pdf_page_of(hm.group(1)) if hm else None
            idx_page = pdf_page_of(page)
            if card_page and idx_page and card_page != idx_page:
                page_bad.append(f"{name}(索引{idx_page}≠卡{card_page})")
            n_lines = ctext.count("\n") + (0 if ctext.endswith("\n") else 1)
            if not (args.min_lines <= n_lines <= args.max_lines):
                lines_bad.append(f"{name}({n_lines}行)")

        if page_bad:
            problems.append(f"{n:02d} 章：索引页码与卡片不一致 → {page_bad[:5]}")
        if lines_bad:
            problems.append(f"{n:02d} 章：行数越界 → {lines_bad[:5]}")

        status = []
        if page_bad:
            status.append(f"页码×{len(page_bad)}")
        if lines_bad:
            status.append(f"行数×{len(lines_bad)}")
        print(f"{n:02d}  {len(links):>6}{len(files):>6}  {'OK' if not status else ' '.join(status)}")

    print("-" * 40)
    print(f"合计：索引双链 {total_links} 条 ｜ 卡片文件 {total_files} 个")

    if problems:
        print(f"\n问题（{len(problems)} 项）：")
        for p in problems:
            print("  -", p)
        return 1

    print("\n全部通过：双链与卡片 1:1、序号连续、页码一致、行数达标。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
