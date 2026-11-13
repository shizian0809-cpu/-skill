#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""学习进度追踪：统计卡片被改过多少张（按内容指纹，不看修改时间）。

配合 SKILL.md「第 8 步」使用：卡片全部生成后建一次基线，此后定时比对。
Obsidian 打开、同步、复制粘贴都会刷新 mtime，所以判定依据只能是内容哈希：
内容变了才算改过；改完又改回原样，哈希相同，不计入。

用法（Windows，务必先设 UTF-8）：
  $env:PYTHONIOENCODING='utf-8'

  # 1) 建基线（只在卡片全部定稿后做一次；会把当时状态当作 0%）
  & 'D:\\tools\\Miniconda\\python.exe' -X utf8 progress.py --root "<项目根>" --init

  # 2) 日常统计（写报告 + 打印）
  & 'D:\\tools\\Miniconda\\python.exe' -X utf8 progress.py --root "<项目根>"

目录约定（与 SKILL.md 一致）：
  <项目根>\\零散的概念\\NN 第X章\\序号 术语.md     ← 卡片
  <项目根>\\_学习进度\\baseline.json | 进度报告.md | history.json

退出码：0 正常；2 缺基线。
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime

BAR_LEN = 24
CH_BAR = 12


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def scan(cards_root):
    """{ '01 第一章/01 假说.md': {...} }"""
    out = {}
    if not os.path.isdir(cards_root):
        return out
    for chapter in sorted(os.listdir(cards_root)):
        cdir = os.path.join(cards_root, chapter)
        if not os.path.isdir(cdir):
            continue
        for name in sorted(os.listdir(cdir)):
            if not name.endswith(".md"):
                continue
            p = os.path.join(cdir, name)
            text = open(p, encoding="utf-8", errors="ignore").read()
            out[f"{chapter}/{name}"] = {
                "sha": sha256(p),
                "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
                "mtime": os.path.getmtime(p),
            }
    return out


def build_report(state, base, title, delta=None):
    old = base.get("cards", {})
    total = len(state)
    modified, fresh = [], []
    for key, info in state.items():
        if key not in old:
            fresh.append(key)
        elif info["sha"] != old[key]["sha"]:
            modified.append(key)
    gone = [k for k in old if k not in state]

    pct = (len(modified) / total * 100) if total else 0.0
    filled = int(round(pct / 100 * BAR_LEN))
    bar = "█" * filled + "░" * (BAR_LEN - filled)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        f"# {title}",
        "",
        f"> 统计时间：{now}　｜　判定方式：内容指纹（改了内容才算，改回原样不算）",
        "",
        f"## 总进度 {len(modified)} / {total}　{pct:.1f}%",
        "",
    ]
    if delta:
        prev_time, prev_done = delta
        gain = len(modified) - prev_done
        sign = f"+{gain}" if gain > 0 else (f"{gain}" if gain < 0 else "±0")
        lines += [f"较上次统计（{prev_time} 的 {prev_done} 张）：**{sign} 张**", ""]
    lines += [
        "```",
        f"{bar}  {pct:.1f}%",
        "```",
        "",
        "| 章 | 已改 | 总数 | 进度 |",
        "|---|---:|---:|---|",
    ]

    chapters = {}
    for key in state:
        ch = key.split("/")[0]
        chapters.setdefault(ch, {"total": 0, "done": 0})
        chapters[ch]["total"] += 1
        if key in modified:
            chapters[ch]["done"] += 1
    for ch in sorted(chapters):
        c = chapters[ch]
        ratio = c["done"] / c["total"] * 100 if c["total"] else 0
        n = int(round(ratio / 100 * CH_BAR))
        mini = "█" * n + "░" * (CH_BAR - n)
        lines.append(f"| {ch} | {c['done']} | {c['total']} | `{mini}` {ratio:.0f}% |")

    if modified:
        recent = sorted(modified, key=lambda k: -state[k]["mtime"])[:8]
        lines += ["", "## 最近改动", ""] + [f"- {k}" for k in recent]
    if fresh:
        lines += ["", f"## 新增卡片（{len(fresh)}）", ""] + [f"- {k}" for k in fresh[:10]]
    if gone:
        lines += ["", f"## 已删除卡片（{len(gone)}）", ""] + [f"- {k}" for k in gone[:10]]

    lines += ["", "---", "", f"基线建立于 {base.get('created', '未知')}，共 {len(old)} 张。"]
    return "\n".join(lines) + "\n", modified, total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.getcwd(), help="项目根目录（含 零散的概念/）")
    ap.add_argument("--cards", default="零散的概念", help="卡片目录名")
    ap.add_argument("--state", default="_学习进度", help="状态目录名")
    ap.add_argument("--title", default="知识点学习进度", help="报告标题")
    ap.add_argument("--init", action="store_true", help="重建基线（会把当前状态当作 0%%）")
    ap.add_argument("--quiet", action="store_true", help="不打印，只写文件")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    cards_root = os.path.join(root, args.cards)
    state_dir = os.path.join(root, args.state)
    baseline = os.path.join(state_dir, "baseline.json")
    report = os.path.join(state_dir, "进度报告.md")
    history = os.path.join(state_dir, "history.json")
    os.makedirs(state_dir, exist_ok=True)

    state = scan(cards_root)
    if not state:
        print(f"卡片目录为空或不存在：{cards_root}", file=sys.stderr)
        return 2

    if args.init:
        payload = {
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cards": {k: {"sha": v["sha"], "lines": v["lines"]} for k, v in state.items()},
        }
        with open(baseline, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=1)
        print(f"基线已建立：{len(state)} 张卡 → {baseline}")
        return 0

    if not os.path.exists(baseline):
        print(f"找不到基线 {baseline}，请先运行 --init", file=sys.stderr)
        return 2

    base = json.load(open(baseline, encoding="utf-8"))
    hist = []
    if os.path.exists(history):
        try:
            hist = json.load(open(history, encoding="utf-8"))
        except Exception:
            hist = []
    delta = (hist[-1]["time"], hist[-1]["done"]) if hist else None

    text, modified, total = build_report(state, base, args.title, delta)
    with open(report, "w", encoding="utf-8") as f:
        f.write(text)

    hist.append({"time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                 "done": len(modified), "total": total})
    with open(history, "w", encoding="utf-8") as f:
        json.dump(hist[-500:], f, ensure_ascii=False, indent=1)

    if not args.quiet:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
