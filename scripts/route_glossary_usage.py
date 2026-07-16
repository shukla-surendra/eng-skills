#!/usr/bin/env python3
"""One-off: route glossary-usage.md entries into vocab.md / phrasal-verbs.md /
idioms.md, resolving Phase 3 of RESTRUCTURE_PLAN.md.

Classification: single words -> vocab.md; 2-3 word verb+particle shapes ->
phrasal-verbs.md; everything else -> idioms.md. A short manual override list
below corrects the handful of shape-matches that aren't actually verb
phrases (e.g. "Way out" is a noun phrase, not a literal phrasal verb).

Reuses dedupe.py's merge_bodies/dedupe_entries so entries that collide with
an existing title in the destination file get merged (keep-richest, append
unique blocks), never duplicated. Deletes glossary-usage.md once every entry
has been routed, per "Retire glossary-usage.md once empty" in the plan.

Usage: python3 scripts/route_glossary_usage.py [--write]
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dedupe import Entry, parse_entries, dedupe_entries, render_index_doc, detect_doc_kind

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "glossary-usage.md"
VOCAB = ROOT / "vocab.md"
PHRASAL = ROOT / "phrasal-verbs.md"
IDIOMS = ROOT / "idioms.md"

PARTICLES = {"up","out","off","in","on","down","back","over","away","through",
             "into","around","about","along","forward","aside","apart","together",
             "across","by","under","upon","ahead","past","round"}

# Shape-matches classify() would get wrong: idiomatic noun/adjective phrases,
# not literal verb+particle forms.
MANUAL_IDIOM_OVERRIDE = {'"Left over"', "Shackles are off", "Way out"}


def classify(title: str) -> str:
    if title in MANUAL_IDIOM_OVERRIDE:
        return "idiom"
    words = title.split()
    if len(words) == 1 and "/" not in title:
        return "vocab"
    if 2 <= len(words) <= 3:
        last = re.sub(r"[^a-zA-Z]", "", words[-1]).lower()
        first = re.sub(r"[^a-zA-Z]", "", words[0]).lower()
        if last in PARTICLES and first.isalpha() and first not in PARTICLES:
            return "phrasal"
    return "idiom"


def load_index_doc(path: Path):
    text = path.read_text(encoding="utf-8")
    kind, title, heading_prefix = detect_doc_kind(text)
    lines = text.splitlines()
    divider_index = next(i for i, l in enumerate(lines) if l.strip() == "---")
    entries = parse_entries(lines[divider_index + 1:], heading_prefix)
    return title, entries


def main():
    write = "--write" in sys.argv

    glossary_title, glossary_entries = load_index_doc(GLOSSARY)
    vocab_title, vocab_entries = load_index_doc(VOCAB)
    phrasal_title, phrasal_entries = load_index_doc(PHRASAL)
    idiom_title, idiom_entries = load_index_doc(IDIOMS)

    buckets = {"vocab": [], "phrasal": [], "idiom": []}
    for e in glossary_entries:
        buckets[classify(e.title)].append(e)

    new_vocab_pool = vocab_entries + buckets["vocab"]
    new_phrasal_pool = phrasal_entries + buckets["phrasal"]
    new_idiom_pool = idiom_entries + buckets["idiom"]

    new_vocab_pool = [Entry(e.title, e.body, i) for i, e in enumerate(new_vocab_pool)]
    new_phrasal_pool = [Entry(e.title, e.body, i) for i, e in enumerate(new_phrasal_pool)]
    new_idiom_pool = [Entry(e.title, e.body, i) for i, e in enumerate(new_idiom_pool)]

    final_vocab, vocab_merges = dedupe_entries(new_vocab_pool)
    final_phrasal, phrasal_merges = dedupe_entries(new_phrasal_pool)
    final_idiom, idiom_merges = dedupe_entries(new_idiom_pool)

    print(f"glossary-usage.md: {len(glossary_entries)} entries -> "
          f"{len(buckets['vocab'])} vocab, {len(buckets['phrasal'])} phrasal, "
          f"{len(buckets['idiom'])} idiom")
    print(f"vocab.md:         {len(vocab_entries)} -> {len(new_vocab_pool)} pooled, "
          f"merged {vocab_merges} collisions, final {len(final_vocab)}")
    print(f"phrasal-verbs.md: {len(phrasal_entries)} -> {len(new_phrasal_pool)} pooled, "
          f"merged {phrasal_merges} collisions, final {len(final_phrasal)}")
    print(f"idioms.md:        {len(idiom_entries)} -> {len(new_idiom_pool)} pooled, "
          f"merged {idiom_merges} collisions, final {len(final_idiom)}")

    if write:
        VOCAB.write_text(render_index_doc(vocab_title, final_vocab), encoding="utf-8")
        PHRASAL.write_text(render_index_doc(phrasal_title, final_phrasal), encoding="utf-8")
        IDIOMS.write_text(render_index_doc(idiom_title, final_idiom), encoding="utf-8")
        GLOSSARY.unlink()
        print("Written. glossary-usage.md retired.")
    else:
        print("Dry run only (pass --write to apply).")


if __name__ == "__main__":
    main()
