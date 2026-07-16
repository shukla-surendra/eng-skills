#!/usr/bin/env python3
"""Restructure technical-english.md into the repo's canonical A-Z word-bank
format and route embedded phrasal verbs into phrasal-verbs.md.

technical-english.md predates the restructure pipeline: it's a numbered-list
dump (not `# Title` headings), with ~22 internal "already used earlier,
skipping" duplicate placeholders, phrasal verbs mixed in with single verbs,
and four separate "practice sentences" sections that are really one topic.

This script:
  1. Parses every `N. **Term** — meaning.` line in the whole document
     (regardless of which of the 7 numbered-list sections it's under —
     the doc's own sectioning is unreliable, e.g. "Roll back" sits in the
     single-verb list but is shaped like a phrasal verb).
  2. Drops the "used before/earlier, skipping" placeholder lines (they're
     not real entries, just a note that the word was already listed).
  3. Classifies each remaining term: 2-3 words ending in a common particle
     -> phrasal verb (destined for phrasal-verbs.md); everything else
     stays in technical-english.md as a technical verb/phrase entry.
  4. Merges the phrasal verbs into phrasal-verbs.md using dedupe.py's
     existing merge machinery (title collisions get bodies merged, not
     duplicated).
  5. Consolidates the four "practice sentences" sections into one entry.
  6. Re-renders technical-english.md with render_index_doc so it gets the
     same A-Z index + back-links every other word bank has.

Usage: python3 scripts/reorganize_technical_english.py [--write]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dedupe import Entry, dedupe_entries, render_index_doc, parse_entries, detect_doc_kind

ROOT = Path(__file__).resolve().parent.parent
TECH = ROOT / "technical-english.md"
PHRASAL = ROOT / "phrasal-verbs.md"

PARTICLES = {"up", "out", "off", "in", "on", "down", "back", "over", "away",
             "through", "into", "around", "about", "along", "forward",
             "aside", "apart", "together", "across", "by", "under", "upon",
             "ahead", "past", "round", "to", "for", "with", "against",
             "toward", "towards", "between", "from"}

# Verb+particle+object collocations (4 words) that are genuine technical
# phrases built on a phrasal verb, not clean phrasal-verb headwords (e.g.
# "Set up alerts" vs the dictionary form "Set up") - these stay in
# technical-english.md as domain-specific technical phrases rather than
# being force-fit into phrasal-verbs.md under an unusual multi-word title.
NOT_A_HEADWORD = {
    "Set up alerts", "Roll up metrics", "Bring down cost", "Call out waste",
    "Lock in config", "Scale out training", "Scale up inference",
    "Scale down inference", "Roll up stats", "Break out metrics",
    "Call out bias", "Dry run",
}

TERM_LINE = re.compile(r"^\d+\.\s+\*\*(.+?)\*\*\s+—\s+(.+?)\s*$")

PRACTICE_HEADINGS = {
    "How to Practice Speaking Naturally",
    "Practice These Architect-Style Sentences",
    "Practice These Real-Meeting Sentences (Recommended)",
    "Ready-to-Speak Phrases (Practice These)",
}


def is_placeholder(meaning: str) -> bool:
    low = meaning.lower()
    return "used" in low and "skip" in low


def is_phrasal(term: str) -> bool:
    if term in NOT_A_HEADWORD:
        return False
    words = term.split()
    return len(words) in (2, 3) and words[-1].lower().strip(".,") in PARTICLES


def parse_term_entries(lines: list[str]) -> list[Entry]:
    """Pull every `N. **Term** — meaning.` line from the whole document."""
    entries: list[Entry] = []
    order = 0
    for line in lines:
        m = TERM_LINE.match(line.strip())
        if not m:
            continue
        term, meaning = m.group(1).strip(), m.group(2).strip()
        if is_placeholder(meaning):
            continue
        if not meaning.endswith("."):
            meaning += "."
        meaning = meaning[0].upper() + meaning[1:]
        entries.append(Entry(term, [meaning], order))
        order += 1
    return entries


def parse_practice_sections(lines: list[str]) -> Entry:
    """Consolidate the 4 practice-sentence sections into one entry."""
    body: list[str] = []
    current_heading = None
    collecting = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            heading = stripped[2:].strip()
            if heading in PRACTICE_HEADINGS:
                collecting = True
                current_heading = heading
                if body:
                    body.append("")
                body.append(f"### {current_heading}")
                body.append("")
                continue
            else:
                collecting = False
                current_heading = None
                continue
        if collecting:
            if stripped == "[↑ Back to index](#index)":
                continue
            if not stripped and (not body or not body[-1].strip()):
                continue
            body.append(line)
    # trim trailing blank lines
    while body and not body[-1].strip():
        body.pop()
    return Entry("Practice Sentences (Technical & Architectural English)", body, -1)


def main() -> None:
    write = "--write" in sys.argv

    original = TECH.read_text(encoding="utf-8")
    lines = original.splitlines()

    all_terms = parse_term_entries(lines)
    practice_entry = parse_practice_sections(lines)

    phrasal_from_tech = [e for e in all_terms if is_phrasal(e.title)]
    verbs_staying = [e for e in all_terms if not is_phrasal(e.title)]

    # De-dupe within technical-english.md's own extracted verb list first
    # (same title can legitimately appear twice with different orders due
    # to the source doc's own internal repeats beyond the marked placeholders).
    verbs_staying = [Entry(e.title, e.body, i) for i, e in enumerate(verbs_staying)]
    deduped_verbs, verb_merges = dedupe_entries(verbs_staying)
    deduped_verbs.append(practice_entry)

    # --- Route phrasal verbs into phrasal-verbs.md ---
    phrasal_text = PHRASAL.read_text(encoding="utf-8")
    kind, phrasal_title, heading_prefix = detect_doc_kind(phrasal_text)
    phrasal_lines = phrasal_text.splitlines()
    divider = next(i for i, l in enumerate(phrasal_lines) if l.strip() == "---")
    existing_phrasal = parse_entries(phrasal_lines[divider + 1:], heading_prefix)

    phrasal_from_tech = [Entry(e.title, e.body, i) for i, e in enumerate(phrasal_from_tech)]
    combined_phrasal_pool = existing_phrasal + [
        Entry(e.title, e.body, len(existing_phrasal) + i)
        for i, e in enumerate(phrasal_from_tech)
    ]
    final_phrasal, phrasal_merges = dedupe_entries(combined_phrasal_pool)

    print(f"technical-english.md: {len(all_terms)} raw term lines parsed "
          f"({len(all_terms) - len(phrasal_from_tech)} verbs-shaped, "
          f"{len(phrasal_from_tech)} phrasal-shaped)")
    print(f"  verbs staying: {len(verbs_staying)} -> {len(deduped_verbs) - 1} "
          f"after internal dedup (merged {verb_merges} title groups) "
          f"+ 1 consolidated practice-sentences entry = {len(deduped_verbs)} total")
    print(f"phrasal-verbs.md: {len(existing_phrasal)} existing + "
          f"{len(phrasal_from_tech)} routed in -> {len(final_phrasal)} final "
          f"(merged {phrasal_merges} title collisions)")

    if write:
        TECH.write_text(
            render_index_doc("Technical & Architectural English", deduped_verbs),
            encoding="utf-8",
        )
        PHRASAL.write_text(
            render_index_doc(phrasal_title, final_phrasal), encoding="utf-8"
        )
        print("Written.")
    else:
        print("Dry run only (pass --write to apply).")


if __name__ == "__main__":
    main()
