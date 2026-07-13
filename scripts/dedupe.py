#!/usr/bin/env python3
"""De-duplicate repeated Markdown entries and regenerate navigation blocks.

This targets the repo's current canonical entry layouts:
  * A-Z word banks with `## Index` + `# Entry` blocks
  * Glossaries with `## Contents` + `## Entry` blocks

Duplicate entries are grouped case-insensitively by title. For each group, the
richest body is kept as the base and unique paragraph-sized blocks from the
other copies are appended in encounter order.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACK_TO_INDEX = "[↑ Back to index](#index)"


@dataclass
class Entry:
    title: str
    body: list[str]
    order: int


def github_anchor(title: str, seen: dict[str, int]) -> str:
    anchor = title.strip().lower()
    anchor = re.sub(r"[^\w\s-]", "", anchor, flags=re.UNICODE)
    anchor = anchor.replace(" ", "-")
    base = anchor
    count = seen.get(base, 0)
    seen[base] = count + 1
    return base if count == 0 else f"{base}-{count}"


def group_key(title: str) -> str:
    head = title.lstrip('“"\'').lstrip()[:1].upper()
    return head if head.isalpha() else "#"


def trim_blank_edges(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def strip_back_link(lines: list[str]) -> list[str]:
    body = trim_blank_edges(lines)
    if body and body[-1].strip() == BACK_TO_INDEX:
        body = trim_blank_edges(body[:-1])
    return body


def split_blocks(lines: list[str]) -> list[list[str]]:
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if line.strip():
            current.append(line)
            continue
        if current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return blocks


def normalize_block(block: list[str]) -> str:
    text = "\n".join(line.rstrip() for line in block).strip()
    text = re.sub(r"\s+", " ", text)
    return text.casefold()


def merge_bodies(entries: list[Entry]) -> list[str]:
    ranked = sorted(
        entries,
        key=lambda entry: (
            sum(len(line.strip()) for line in entry.body),
            sum(1 for line in entry.body if line.strip()),
            -entry.order,
        ),
        reverse=True,
    )
    merged_blocks: list[list[str]] = []
    seen: list[str] = []
    for entry in ranked:
        for block in split_blocks(entry.body):
            norm = normalize_block(block)
            if not norm or norm == "---":
                continue

            exact_or_subset = False
            superset_index = None
            for index, prior in enumerate(seen):
                if norm == prior or norm in prior:
                    # Already fully covered by a block we kept - safe to drop.
                    exact_or_subset = True
                    break
                if prior in norm:
                    # This block is a strict superset of one we kept (e.g. the
                    # same definition plus an extra synonym list, or a real
                    # paragraph that happens to contain a divider we already
                    # saw). Upgrade in place instead of dropping it, or we'd
                    # silently lose the extra content.
                    superset_index = index

            if exact_or_subset:
                continue
            if superset_index is not None:
                seen[superset_index] = norm
                merged_blocks[superset_index] = block
                continue

            seen.append(norm)
            merged_blocks.append(block)

    body: list[str] = []
    for index, block in enumerate(merged_blocks):
        if index:
            body.append("")
        body.extend(block)
    return body


def parse_entries(lines: list[str], heading_prefix: str) -> list[Entry]:
    entries: list[Entry] = []
    current_title: str | None = None
    current_body: list[str] = []
    order = 0

    for line in lines:
        if line.startswith(f"{heading_prefix} "):
            if current_title is not None:
                entries.append(
                    Entry(current_title, strip_back_link(current_body), order)
                )
                order += 1
            current_title = line[len(heading_prefix) + 1 :].strip()
            current_body = []
        elif current_title is not None:
            current_body.append(line)

    if current_title is not None:
        entries.append(Entry(current_title, strip_back_link(current_body), order))

    return entries


def dedupe_entries(entries: list[Entry]) -> tuple[list[Entry], int]:
    grouped: dict[str, list[Entry]] = {}
    order_of_groups: list[str] = []

    for entry in entries:
        key = entry.title.casefold()
        if key not in grouped:
            grouped[key] = []
            order_of_groups.append(key)
        grouped[key].append(entry)

    deduped: list[Entry] = []
    duplicate_groups = 0

    for key in order_of_groups:
        bucket = grouped[key]
        if len(bucket) > 1:
            duplicate_groups += 1
        canonical = min(bucket, key=lambda entry: entry.order)
        body = merge_bodies(bucket)
        deduped.append(Entry(canonical.title, body, canonical.order))

    deduped.sort(key=lambda entry: entry.title.casefold())
    return deduped, duplicate_groups


def render_index_doc(title: str, entries: list[Entry]) -> str:
    today = dt.date.today().isoformat()
    seen: dict[str, int] = {}
    anchored = [(entry.title, github_anchor(entry.title, seen), entry.body) for entry in entries]

    out = [
        f"# {title}",
        "",
        f"> {len(entries)} entries · restructured {today} · sorted A–Z",
        "",
        "## Index",
        "",
    ]

    last_group = None
    line_parts: list[str] = []
    for term, anchor, _ in anchored:
        current_group = group_key(term)
        if current_group != last_group:
            if line_parts:
                out.append(" · ".join(line_parts))
                out.append("")
                line_parts = []
            out.append(f"**{current_group}**")
            out.append("")
            last_group = current_group
        line_parts.append(f"[{term}](#{anchor})")
    if line_parts:
        out.append(" · ".join(line_parts))
        out.append("")

    out.extend(["---", ""])
    for term, _, body in anchored:
        out.append(f"# {term}")
        out.append("")
        out.extend(body)
        out.append("")
        out.append(BACK_TO_INDEX)
        out.append("")

    text = "\n".join(out).rstrip() + "\n"
    return re.sub(r"\n{4,}", "\n\n\n", text)


def render_contents_doc(title: str, entries: list[Entry], heading_prefix: str) -> str:
    seen: dict[str, int] = {}
    toc = ["## Contents", ""]
    for entry in entries:
        toc.append(f"- [{entry.title}](#{github_anchor(entry.title, seen)})")

    out = [f"# {title}", "", *toc, "", "---", ""]
    for entry in entries:
        out.append(f"{heading_prefix} {entry.title}")
        out.append("")
        out.extend(entry.body)
        out.append("")

    text = "\n".join(out).rstrip() + "\n"
    return re.sub(r"\n{4,}", "\n\n\n", text)


def detect_doc_kind(text: str) -> tuple[str, str, str]:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Expected a top-level document title.")

    title = lines[0][2:].strip()
    divider_index = next(
        (index for index, line in enumerate(lines) if line.strip() == "---"),
        None,
    )
    if divider_index is None:
        raise ValueError("Expected a `---` divider before the entry list.")

    entry_heading = next(
        (
            line.split(" ", 1)[0]
            for line in lines[divider_index + 1 :]
            if re.match(r"^#{1,6}\s+", line)
        ),
        None,
    )
    if entry_heading is None:
        raise ValueError("Could not detect entry heading level.")

    kind = "contents" if "## Contents" in text else "index"
    return kind, title, entry_heading


def dedupe_file(path: Path, write: bool) -> tuple[int, int, int]:
    original = path.read_text(encoding="utf-8")
    kind, title, heading_prefix = detect_doc_kind(original)
    lines = original.splitlines()
    divider_index = next(i for i, line in enumerate(lines) if line.strip() == "---")
    entries = parse_entries(lines[divider_index + 1 :], heading_prefix)
    deduped_entries, duplicate_groups = dedupe_entries(entries)

    if kind == "index":
        updated = render_index_doc(title, deduped_entries)
    else:
        updated = render_contents_doc(title, deduped_entries, heading_prefix)

    if write:
        path.write_text(updated, encoding="utf-8")

    return len(entries), len(deduped_entries), duplicate_groups


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Markdown files to de-duplicate")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Rewrite files in place instead of only printing stats.",
    )
    args = parser.parse_args()

    for raw_path in args.paths:
        path = (ROOT / raw_path).resolve()
        before, after, duplicate_groups = dedupe_file(path, write=args.write)
        print(
            f"{path.relative_to(ROOT)}: {before} -> {after} entries; "
            f"merged {duplicate_groups} duplicate title groups"
        )


if __name__ == "__main__":
    main()
