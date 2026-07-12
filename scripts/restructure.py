#!/usr/bin/env python3
"""Restructure Google-Docs-exported English word dumps into clean, revisable markdown.

For each source file:
  - strip embedded base64 image definitions (huge bloat)
  - convert inline image refs `![<url>][imageN]` -> `![<url>](<url>)` (external), else drop
  - drop the auto-generated table-of-contents (standalone `[...](#anchor)` link lines)
  - parse entries at `# Heading`, clean titles (**bold**, {#anchor}, escapes, whitespace)
  - drop empty page-break headings, attaching any stray body to the previous entry
  - sort entries alphabetically (case-insensitive)
  - regenerate a clean, clickable A-Z index with GitHub-compatible anchors
"""
import re
import sys
import datetime
from pathlib import Path

SRC = Path("source")
OUT = Path(".")

JOBS = [
    ("Master Vocab Dict.md",            "vocab.md",         "Vocabulary"),
    ("Master Phrasal_Verb Dict.md",     "phrasal-verbs.md", "Phrasal Verbs"),
    ("Master_Idioms.md",                "idioms.md",        "Idioms"),
    ("Master_Explanation_And_Anology.md","explanations.md", "Explanations & Analogies"),
]

RE_IMG_DEF   = re.compile(r'^\[image\d+\]:\s*<data:image', re.I)
RE_IMG_REF   = re.compile(r'!\[([^\]]*)\]\[image\d+\]')
RE_TOC_LINE  = re.compile(r'^\s*\[[^\]]*\]\(#[^)]*\)\s*$')
RE_ANCHOR_IN_TITLE = re.compile(r'\s*\{#[^}]*\}\s*$')


def clean_title(raw: str) -> str:
    t = raw.strip()
    t = RE_ANCHOR_IN_TITLE.sub('', t)          # drop {#anchor} suffix
    t = t.replace('**', '').replace('__', '')  # drop bold markers
    t = re.sub(r'\\([!().,\-*_#`>+=~\[\]])', r'\1', t)  # unescape backslash escapes
    t = t.strip(' *#\t')
    t = re.sub(r'\s+', ' ', t)
    t = re.sub(r'[\s:;,]+$', '', t)   # drop trailing punctuation artifacts
    t = re.sub(r'(?<=\w)\.$', '', t)  # drop a single trailing period after a word
    return t.strip()


def convert_img_ref(m: re.Match) -> str:
    alt = m.group(1).strip()
    if alt.lower().startswith(('http://', 'https://')):
        url = alt.replace('\\', '')            # google docs escapes _ etc in urls
        return f'![illustration]({url})'
    return ''                                   # no usable url -> drop the ref


def github_anchor(title: str, seen: dict) -> str:
    a = title.strip().lower()
    a = re.sub(r'[^\w\s-]', '', a, flags=re.UNICODE)  # keep word chars, space, hyphen
    a = a.replace(' ', '-')
    base = a
    n = seen.get(base, 0)
    seen[base] = n + 1
    return base if n == 0 else f'{base}-{n}'


def process(src_path: Path, title: str):
    raw = src_path.read_text(encoding='utf-8')
    lines = raw.split('\n')

    # 1) line-level cleanup
    cleaned = []
    for ln in lines:
        if RE_IMG_DEF.match(ln):
            continue                            # drop base64 blob
        if RE_TOC_LINE.match(ln):
            continue                            # drop TOC link line
        ln = RE_IMG_REF.sub(convert_img_ref, ln)
        cleaned.append(ln)

    # 2) parse into entries at H1 boundaries
    entries = []          # list of (clean_title, [body_lines])
    cur_title = None
    cur_body = []
    for ln in cleaned:
        if ln.startswith('# '):
            title_txt = clean_title(ln[2:])
            if title_txt == '':
                # empty page-break heading: keep collecting body into current entry
                continue
            if cur_title is not None:
                entries.append((cur_title, cur_body))
            elif any(x.strip() for x in cur_body):
                # orphan body before first real heading -> discard (TOC remnants)
                pass
            cur_title, cur_body = title_txt, []
        else:
            cur_body.append(ln)
    if cur_title is not None:
        entries.append((cur_title, cur_body))

    # 3) trim leading/trailing blank lines in each body
    trimmed = []
    for t, body in entries:
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()
        trimmed.append((t, body))
    entries = trimmed

    # 4) sort alphabetically (case-insensitive)
    entries.sort(key=lambda e: e[0].lower())

    # 5) build anchors + grouped index
    seen = {}
    anchored = [(t, github_anchor(t, seen), body) for t, body in entries]

    def group_key(t):
        c = t.lstrip('“"\'').lstrip()[:1].upper()
        return c if c.isalpha() else '#'

    out = []
    today = datetime.date.today().isoformat()
    out.append(f'# {title}')
    out.append('')
    out.append(f'> {len(anchored)} entries · restructured {today} · sorted A–Z')
    out.append('')
    out.append('## Index')
    out.append('')
    last_group = None
    line_parts = []
    for t, a, _ in anchored:
        g = group_key(t)
        if g != last_group:
            if line_parts:
                out.append(' · '.join(line_parts)); out.append('')
                line_parts = []
            out.append(f'**{g}**'); out.append('')
            last_group = g
        line_parts.append(f'[{t}](#{a})')
    if line_parts:
        out.append(' · '.join(line_parts)); out.append('')

    out.append('---')
    out.append('')

    # 6) entries
    for t, a, body in anchored:
        out.append(f'# {t}')
        out.append('')
        out.extend(body)
        out.append('')
        out.append('[↑ Back to index](#index)')
        out.append('')

    result = '\n'.join(out).rstrip() + '\n'
    result = re.sub(r'\n{4,}', '\n\n\n', result)  # collapse excessive blank runs
    return result, len(anchored)


def main():
    for src_name, out_name, title in JOBS:
        src = SRC / src_name
        text, n = process(src, title)
        (OUT / out_name).write_text(text, encoding='utf-8')
        kb = len((OUT / out_name).read_bytes()) / 1024
        print(f'{out_name:18s} {n:5d} entries  {kb:8.1f} KB')


if __name__ == '__main__':
    main()
