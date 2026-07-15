#!/usr/bin/env python3
"""One-off: move misclassified entries between vocab.md and phrasal-verbs.md.

vocab.md had ~22 genuine phrasal verbs (verb + particle, e.g. "Chalk out")
sitting in the single-word file; phrasal-verbs.md had ~500 single words
(e.g. "Gibberish", "Mundane") sitting in the two/three-word-verb file. This
reclassifies both directions in one pass, merging bodies (via dedupe.py's
existing merge_bodies/dedupe_entries) wherever the destination file already
has an entry with the same title, then re-renders both files with
render_index_doc so the A-Z index/anchors stay consistent.

Usage: python3 scripts/route_vocab_phrasal.py [--write]
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dedupe import Entry, parse_entries, dedupe_entries, render_index_doc, detect_doc_kind

ROOT = Path(__file__).resolve().parent.parent
VOCAB = ROOT / "vocab.md"
PHRASAL = ROOT / "phrasal-verbs.md"

PARTICLES = {"up","out","off","in","on","down","back","over","away","through",
             "into","around","about","along","forward","aside","apart","together",
             "across","by","under","upon","ahead","past","round"}

VOCAB_TO_PHRASAL = {
    "Blurt out","Chalk out","Churn Out","Creep out","Falling out","Hit up",
    "Hold/Held Up","Hop out","Looped in","Mellow out","Move Over","Pent up",
    "Plowed ahead","Put out","Ratting on","Rolling up","Shove up","start off",
    "Stomping around","take on","Weaned off","Weigh in",
}  # "Inside out" deliberately excluded: adverbial idiom, not a verb form.


def looks_like_single_word(title: str) -> bool:
    return " " not in title and "/" not in title


def load(path: Path):
    text = path.read_text(encoding="utf-8")
    kind, title, heading_prefix = detect_doc_kind(text)
    lines = text.splitlines()
    divider_index = next(i for i, l in enumerate(lines) if l.strip() == "---")
    entries = parse_entries(lines[divider_index + 1:], heading_prefix)
    return title, entries


def main():
    write = "--write" in sys.argv

    vocab_title, vocab_entries = load(VOCAB)
    phrasal_title, phrasal_entries = load(PHRASAL)

    phrasal_to_vocab_titles = {
        e.title for e in phrasal_entries if looks_like_single_word(e.title)
    }

    moving_out_of_vocab = [e for e in vocab_entries if e.title in VOCAB_TO_PHRASAL]
    staying_in_vocab = [e for e in vocab_entries if e.title not in VOCAB_TO_PHRASAL]

    moving_out_of_phrasal = [e for e in phrasal_entries if e.title in phrasal_to_vocab_titles]
    staying_in_phrasal = [e for e in phrasal_entries if e.title not in phrasal_to_vocab_titles]

    new_vocab_pool = staying_in_vocab + moving_out_of_phrasal
    new_phrasal_pool = staying_in_phrasal + moving_out_of_vocab

    new_vocab_pool = [Entry(e.title, e.body, i) for i, e in enumerate(new_vocab_pool)]
    new_phrasal_pool = [Entry(e.title, e.body, i) for i, e in enumerate(new_phrasal_pool)]

    final_vocab, vocab_merges = dedupe_entries(new_vocab_pool)
    final_phrasal, phrasal_merges = dedupe_entries(new_phrasal_pool)

    print(f"vocab.md:         {len(vocab_entries)} -> moved out {len(moving_out_of_vocab)}, "
          f"moved in {len(moving_out_of_phrasal)}, merged {vocab_merges} title collisions, "
          f"final {len(final_vocab)}")
    print(f"phrasal-verbs.md: {len(phrasal_entries)} -> moved out {len(moving_out_of_phrasal)}, "
          f"moved in {len(moving_out_of_vocab)}, merged {phrasal_merges} title collisions, "
          f"final {len(final_phrasal)}")

    if write:
        VOCAB.write_text(render_index_doc(vocab_title, final_vocab), encoding="utf-8")
        PHRASAL.write_text(render_index_doc(phrasal_title, final_phrasal), encoding="utf-8")
        print("Written.")
    else:
        print("Dry run only (pass --write to apply).")


if __name__ == "__main__":
    main()
