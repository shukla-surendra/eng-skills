#!/usr/bin/env python3
"""Split vocab-usage.md into three purpose-built files by content type.

  - glossary-usage.md : word/phrase definition entries (+ category headers)
  - reference-tables.md : standalone reference tables (in the glossary region)
  - stories.md        : titled stories, each kept WITH its vocabulary table
Content is conserved: the union of the three == the source body (verified separately).
"""
import re
from pathlib import Path

SRC = Path("vocab-usage.md")


def parse_blocks(text):
    lines = text.split('\n')
    start = next(i for i, l in enumerate(lines) if l.strip() == '---') + 1
    blocks = []
    cur, body = None, []
    for l in lines[start:]:
        if l.startswith('## '):
            if cur is not None:
                blocks.append((cur, body))
            cur, body = l[3:].strip(), []
        elif cur is not None:
            body.append(l)
    if cur is not None:
        blocks.append((cur, body))
    return blocks


def has_table(body):
    return any(x.lstrip().startswith('|') for x in body)


def prose_len(body):
    return len(' '.join(x for x in body if not x.lstrip().startswith('|')).strip())


def is_story_heading(h):
    return h.lower().startswith(('title:', 'story:'))


def github_anchor(text, seen):
    a = re.sub(r'[^\w\s-]', '', text.strip().lower(), flags=re.UNICODE)
    a = re.sub(r'\s', '-', a)
    n = seen.get(a, 0)
    seen[a] = n + 1
    return a if n == 0 else f'{a}-{n}'


def render(title, blocks):
    seen = {}
    toc = ['## Contents', '']
    out = []
    for h, body in blocks:
        anchor = github_anchor(h, seen)
        toc.append(f'- [{h}](#{anchor})')
        out.append(f'## {h}')
        out.extend(body)
    text = f'# {title}\n\n' + '\n'.join(toc) + '\n\n---\n\n' + '\n'.join(out)
    return re.sub(r'\n{3,}', '\n\n', text).rstrip() + '\n'


def main():
    blocks = parse_blocks(SRC.read_text(encoding='utf-8'))

    # find where the stories region begins (first titled/long story block)
    story_start = None
    for i, (h, b) in enumerate(blocks):
        if is_story_heading(h) or (prose_len(b) > 300 and 'Meaning' not in ' '.join(b)):
            story_start = i
            break
    if story_start is None:
        story_start = len(blocks)

    glossary_region = blocks[:story_start]
    story_region = blocks[story_start:]

    glossary = [(h, b) for h, b in glossary_region if not has_table(b)]
    tables = [(h, b) for h, b in glossary_region if has_table(b)]

    files = {
        'glossary-usage.md': ('Vocabulary Glossary (Usage)', glossary),
        'reference-tables.md': ('Reference Tables', tables),
        'stories.md':        ('Vocabulary in Context — Stories', story_region),
    }
    for fn, (title, blks) in files.items():
        Path(fn).write_text(render(title, blks), encoding='utf-8')
        print(f'{fn:20s} {len(blks):4d} blocks  {len(Path(fn).read_bytes())/1024:7.1f} KB')


if __name__ == '__main__':
    main()
