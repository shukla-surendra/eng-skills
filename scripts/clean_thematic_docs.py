#!/usr/bin/env python3
"""Clean the two newly-downloaded thematic reference docs into standalone files.

These are NOT A-Z word dumps like the originals; they are structured by theme
(sections + numbered lists). So we preserve their structure and only:
  - unescape Google-Docs backslash escapes (\\. \\+ \\[ etc.)
  - strip **bold** wrapping and emoji from HEADING lines (clean anchors)
  - drop empty page-break headings and base64/TOC junk (safety)
  - collapse excess blank lines
  - prepend a generated, clickable Table of Contents (GitHub-compatible anchors)
"""
import re
from pathlib import Path

SRC = Path("source")

JOBS = [
    # (source, output, H1 title, toc_levels, flatten_to, skip_headings)
    # technical file has clean, meaningful levels -> keep them
    ("🔥 Technical _ Architectural Verbs.md", "technical-verbs.md",
     "Technical & Architectural English", (1, 2), None, ()),
    # business file has inconsistent Google-Docs levels -> flatten to one
    # level so it becomes a clean, flat phrasebook jump-list
    ("Business Idioms & Phrases.md", "business-phrases.md",
     "Business Idioms & Phrases", (2,), 2, ()),
    # mental-models articles: clean #/##/### hierarchy; strip embedded TOC
    # NB: only skip the pure auto "table of contents"; the "just the links"
    # section also holds a long essay, so it must be kept.
    ("001-Mental_Models.docx.md", "mental-models.md",
     "Mental Models & Thinking Frameworks", (1, 2), None,
     ("table of contents",)),
    # vocab-usage: diverse mix of word entries, category groups, tables, and
    # in-context stories -> flatten heading levels into a flat searchable list;
    # tables and prose are left exactly as they are.
    ("Vocab_Usage.md", "vocab-usage.md",
     "Vocabulary in Use", (2,), 2, ()),
]

RE_IMG_DEF = re.compile(r'^\[image\d+\]:\s*<data:image', re.I)
RE_IMG_REF = re.compile(r'!\[([^\]]*)\]\[image\d+\]')
RE_TOC_LINE = re.compile(r'^\s*\[.*\]\(#.*\)\s*$')


def convert_img_ref(m):
    alt = m.group(1).strip()
    if alt.lower().startswith(('http://', 'https://')):
        return f'![illustration]({alt.replace(chr(92), "")})'
    if alt:
        return f'*[Diagram: {alt}]*'  # base64 stripped -> keep a caption note
    return ''  # nothing usable -> drop the ref
RE_HEADING = re.compile(r'^(#{1,6})\s+(.*)$')
# backslash-escaped ASCII punctuation that Google Docs adds
# (NB: '|' is intentionally excluded so escaped pipes inside tables survive)
RE_UNESCAPE = re.compile(r'\\([.\+\~\!\[\]\(\)\-\*_#>="\'@&/:;,`])')
# true emoji / pictograph ranges to strip from headings
# (deliberately NOT touching dashes, arrows, or curly quotes)
RE_EMOJI = re.compile(
    "[" "\U0001F000-\U0001FAFF" "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF" "\U00002B00-\U00002BFF"
    "\U0000FE00-\U0000FE0F" "❤" "]",
    flags=re.UNICODE)


def clean_heading_text(t, strip_num=False):
    t = t.replace('**', '').replace('__', '')
    t = RE_EMOJI.sub('', t)
    t = re.sub(r'\s+', ' ', t).strip()
    t = t.strip('*# \t')
    if strip_num:
        t = re.sub(r'^\d+\.\s+', '', t)   # drop inconsistent leading "8. "
    return t.strip()


def github_anchor(text, seen):
    a = text.strip().lower()
    a = re.sub(r'[^\w\s-]', '', a, flags=re.UNICODE)
    a = re.sub(r'\s', '-', a)
    n = seen.get(a, 0)
    seen[a] = n + 1
    return a if n == 0 else f'{a}-{n}'


def process(src_name, out_name, title, toc_levels, flatten_to=None, skip_headings=()):
    raw = (SRC / src_name).read_text(encoding='utf-8')
    skip = {s.lower() for s in skip_headings}

    # 1) line-level clean
    lines = []
    for ln in raw.split('\n'):
        if RE_IMG_DEF.match(ln) or RE_TOC_LINE.match(ln):
            continue
        ln = RE_UNESCAPE.sub(r'\1', ln)
        ln = RE_IMG_REF.sub(convert_img_ref, ln)  # base64 ref -> external link
        lines.append(ln)

    # 2) normalize headings, drop empty/skipped ones, collect for TOC
    seen = {}
    body = []
    toc = []  # (level, text, anchor)
    skipping_under = None  # heading level we're dropping the body of
    for ln in lines:
        m = RE_HEADING.match(ln)
        if m:
            src_level = len(m.group(1))
            text = clean_heading_text(m.group(2), strip_num=bool(flatten_to))
            if skipping_under is not None:
                if not text or src_level > skipping_under:
                    continue  # still inside a skipped section
                skipping_under = None
            if not text:
                continue  # empty page-break heading
            if text.lower() in skip:
                skipping_under = src_level  # drop this heading + its body
                continue
            level = flatten_to if flatten_to else src_level
            anchor = github_anchor(text, seen)
            body.append(f'{"#" * level} {text}')
            if level in toc_levels:
                toc.append((level, text, anchor))
        else:
            if skipping_under is not None:
                continue
            body.append(ln)

    # 3) collapse 3+ blank lines
    text_body = re.sub(r'\n{3,}', '\n\n', '\n'.join(body)).strip()

    # 4) build TOC (indent nested levels)
    base = min(toc_levels)
    toc_lines = ['## Contents', '']
    for level, t, a in toc:
        indent = '  ' * (level - base)
        toc_lines.append(f'{indent}- [{t}](#{a})')

    out = f'# {title}\n\n' + '\n'.join(toc_lines) + '\n\n---\n\n' + text_body + '\n'
    Path(out_name).write_text(out, encoding='utf-8')
    return len(toc), len(out)


def main():
    for src, out, title, lvls, flatten, skips in JOBS:
        if not (SRC / src).exists():
            print(f'{out:22s} (skipped — source/{src} not present)')
            continue
        n, size = process(src, out, title, lvls, flatten, skips)
        print(f'{out:22s} TOC entries={n:4d}  {size/1024:7.1f} KB')


if __name__ == '__main__':
    main()
