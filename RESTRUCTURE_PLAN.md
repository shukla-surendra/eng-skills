# Restructure Plan

A roadmap for turning this collection from cleaned-but-overlapping dumps into a
single, de-duplicated, well-categorised, revisable knowledge base. This is a
multi-session effort — each phase is independently shippable and reversible.

---

## 1. Goals & principles

1. **One fact, one home.** Every word / phrase / idiom lives in exactly one
   canonical file, with no duplicates.
2. **Type-based organisation.** Content is grouped by what it *is*
   (word bank vs grammar vs speaking phrase vs story), not by which document it
   arrived in.
3. **Consistent, minimal schema** per entry so revision feels uniform and a
   future flash-card export is trivial.
4. **Nothing is ever lost.** Every automated move/merge is verified for content
   conservation before the old copy is deleted, and committed per step so any
   change can be rolled back.
5. **Reproducible pipeline.** Adding a new source doc later follows the same
   documented steps, not ad-hoc cleanup.
6. **Serves the real goal** — revising to speak better: fluent technical
   explanation, sentence framing, analogies, and confident meeting English.

---

## 2. Current state (baseline)

| File | Headings | Size | Nature |
|------|---------:|-----:|--------|
| vocab.md | 1777 | 952K | word bank (A–Z) |
| phrasal-verbs.md | 1546 | 660K | word bank (A–Z) |
| idioms.md | 62 | 48K | idioms |
| glossary-usage.md | 433 | 56K | mixed word/phrasal/idiom (overlaps others) |
| business-phrases.md | 119 | 56K | business/meeting phrases |
| technical-verbs.md | 64 | 56K | technical verbs + architect phrasal verbs + meeting phrases |
| explanations.md | 57 | 100K | **grab-bag**: grammar + meeting phrases + tutorials |
| mental-models.md | 55 | 84K | reading / thinking frameworks |
| stories.md | 8 | 160K | vocabulary-in-context stories |
| usage-tables.md | 3 | 4K | lookup tables |

**Known problems**

- Internal duplicates: vocab **147**, phrasal-verbs **162**, glossary-usage **23**.
- Cross-file overlap: phrasal-verbs ∩ glossary-usage **356**,
  vocab ∩ phrasal-verbs **80** (78 resolved by Phase 3b's routing/merge pass,
  2026-07-15 — see below), vocab ∩ glossary-usage **33**,
  phrasal-verbs ∩ business **11**, others smaller.
- Mixed-purpose files: `explanations.md` (3 different content types), `glossary-usage.md`
  (word + phrasal + idiom mixed together).
- Inconsistent entry schemas (rich multi-section vs terse Meaning/Example/Context).

---

## 3. Target architecture

Four buckets, ~11 canonical files. Each core word bank is A–Z, de-duplicated,
one entry per term.

```
WORD BANKS (lookup / revision)
  vocabulary.md            single words
  phrasal-verbs.md         verb + particle
  idioms-expressions.md    idioms & fixed expressions

SPEAKING & COMMUNICATION
  speaking-toolkit.md      how to explain, frame sentences, use analogies,
                           connecting phrases, "alternatives to I think"
  business-communication.md   meetings, suggestions, diplomatic phrasing
  technical-english.md     technical/architectural verbs & phrases

GRAMMAR
  grammar-notes.md         articles, tenses, used-to, until/by, adverbs …

READING & REFERENCE
  stories.md               vocabulary-in-context stories (+ their tables)
  mental-models.md         thinking frameworks (reading practice)
  reference-tables.md      quick phrase → meaning lookup tables

ROOT
  README.md                landing page / index
```

**Mapping from today → target**

| Today | Goes to |
|-------|---------|
| vocab.md | vocabulary.md |
| phrasal-verbs.md | phrasal-verbs.md |
| idioms.md + business idioms | idioms-expressions.md |
| glossary-usage.md | split by type → vocabulary / phrasal-verbs / idioms-expressions |
| business-phrases.md | business-communication.md |
| technical-verbs.md | technical-english.md (+ connecting/meeting phrases → speaking-toolkit) |
| explanations.md | **split** → grammar-notes.md + speaking-toolkit.md |
| mental-models.md | mental-models.md (unchanged) |
| stories.md | stories.md (unchanged) |
| usage-tables.md | reference-tables.md |

---

## 4. Canonical entry schema

Word-bank entries converge on:

```markdown
# Term
**Meaning:** short definition (required)
**Example:** one natural sentence (required)
**Use it when:** context / register — spoken, formal, tech … (optional)
**Related:** synonyms / opposites / easily-confused (optional)

<any existing richer notes kept below>
```

- Existing rich entries are **kept**, just topped with Meaning/Example if missing.
- Terse entries are **promoted** to this shape.
- This schema is what a future Anki/CSV export reads (front = Term, back = Meaning + Example).

---

## 5. Standard pipeline (for every source doc)

```
1. INGEST   drop raw export in source/ (gitignored)
2. CLEAN    strip base64 / broken TOC / escapes / {#anchors} / control chars;
            de-bold + de-emoji headings            (scripts/clean_*.py)
3. CLASSIFY tag each block: word | phrasal | idiom | phrase | grammar |
            tutorial | table | story
4. ROUTE    append each block to its canonical file
5. DEDUP    merge same-title entries (keep richest; union extra notes)
6. SORT     re-alphabetise word banks; regenerate A–Z index
7. VERIFY   content-conservation + anchor + link + build gates (§7)
8. BUILD    make docs (regenerates HTML + search index)
```

---

## 6. Phased roadmap

### Phase 0 — Foundations ✅ (done)
- [x] Convert all Google-Docs exports to clean Markdown (base64/TOC/escape removal).
- [x] Alphabetical indexes + back-links on word banks.
- [x] HTML site with full-text search (`scripts/build_docs.py`, `search-index.json`).
- [x] Link checker (`scripts/check_links.py`).
- [x] Split `vocab-usage.md` by type (pilot for §3 routing).
- [x] Repo-wide health pass (empty headings, control chars).

### Phase 1 — De-duplicate within each file
- [x] Build `scripts/dedupe.py`: find same-title entries, merge (keep richest body,
      append unique extra notes), regenerate index.
- [x] Apply to vocab (147), phrasal-verbs (162), glossary-usage (23).
- [x] Verify + commit per file.

### Phase 2 — Split the mixed-purpose files
- [x] `explanations.md` → `grammar-notes.md` + `speaking-toolkit.md`
      (tutorials + framing/analogy content). Content that was neither grammar
      nor a speaking framework (embedded vocab/idiom tables, loose example
      sentences, meeting-specific phrases) was routed to its actual canonical
      home instead — see note below.
- [x] Extract connecting phrases / meeting phrases / "alternatives to I think"
      from `technical-verbs.md` → `speaking-toolkit.md`; keep pure tech verbs in
      `technical-english.md`.
- [x] Rename `business-phrases.md` → `business-communication.md`,
      `usage-tables.md` → `reference-tables.md`.

**Note on Phase 2 execution (2026-07-13):** `explanations.md` turned out to be
messier than the original baseline table suggested — several unrelated topics
had been merged under single headings during the original conversion (e.g. one
"Article" heading actually contained Articles, Until/By, Frequency Adverbs, and
three "Used to" lessons, interleaved with two large raw vocabulary tables and a
loose sentence dump with no heading at all). Content was classified at a finer
grain than the file's own headings:
- Grammar micro-lessons → `grammar-notes.md` (9 entries).
- Tutorials, the debugging/clarifying-questions framework (consolidated from
  three near-duplicate copies into one), and meeting/connecting phrases →
  `speaking-toolkit.md` (10 entries).
- Embedded raw vocab/idiom/phrase tables, "Interesting Sentences", and an
  essay-feedback phrase bank → `glossary-usage.md` (its designated mixed
  catch-all, consistent with the baseline table).
- `Kickoff`/`Kick in` → `phrasal-verbs.md` (merged with an existing `Kick in`
  entry via `dedupe.py`). `Get under the skin`, `Voilà` → `idioms.md`.
  `Concluding Meeting`, `While someone joins` → `business-communication.md`.
  `Synonym of important` → `reference-tables.md`.
- One section (a mislabeled heading whose body was near-fully duplicated by
  the four Tutorial entries) was merged rather than carried forward twice —
  disclosed here rather than silently dropped, per goal 4.
- All merges/appends were run through `scripts/dedupe.py --write`, which also
  caught 2 pre-existing duplicate entries in `business-communication.md` that
  predated this pass (it had never been deduped before, unlike vocab/phrasal-verbs/glossary-usage in Phase 1).

### Phase 3 — Route glossary-usage + cross-file consolidation
- [ ] Classify each `glossary-usage.md` entry (word/phrasal/idiom) and route to the
      canonical word bank.
- [ ] Resolve cross-file overlaps (phrasal∩glossary 356, vocab∩phrasal 80, …):
      pick one canonical home per term, merge content, delete the rest.
- [ ] Retire `glossary-usage.md` once empty.

### Phase 3b — Separate `vocab.md` (single words) from `phrasal-verbs.md` (two/three-word verbs) ✅ (done 2026-07-15)
Both files were meant to be type-pure per the README (`vocab.md` = single
words, `phrasal-verbs.md` = verb + particle), but the original conversion
left them badly cross-contaminated: 22 genuine phrasal verbs (e.g. "Chalk
out", "Weigh in") were sitting in `vocab.md`, and — far more — **500 plain
single words** (e.g. "Gibberish", "Mundane", "Sandbox") were sitting in
`phrasal-verbs.md`. This also surfaced 78 title collisions (the same word
existed correctly in one file and incorrectly in the other, e.g. "Caveat"),
which is most of the "vocab ∩ phrasal-verbs 80" overlap noted in Known
problems above.

- [x] Built `scripts/route_vocab_phrasal.py`, which reuses `dedupe.py`'s
      existing `parse_entries` / `merge_bodies` / `dedupe_entries` /
      `render_index_doc` rather than reinventing merge logic — moved entries
      that collide with an existing title in the destination file get their
      bodies merged (keep-richest, append unique blocks), not duplicated.
- [x] Classification heuristic: an entry is a phrasal verb if it's 2–3 words
      and the last word is a common particle (up/out/off/in/on/down/back/
      over/away/through/into/around/...); otherwise, if it has no space or
      slash, it's a single word. Reviewed the smaller list (23 vocab.md
      candidates) by eye before moving — excluded **"Inside out"**, which
      matches the shape but is an adverbial idiom, not a verb form, so it
      stayed in `vocab.md`.
- [x] Dry-run first (`--write` omitted) to confirm the arithmetic before
      touching any file: 2762 total entries − 78 merges = 2684 final total,
      matching exactly.
- [x] Applied: `vocab.md` 1458→1862 entries (net; moved out 22, moved in
      500, merged 74 collisions), `phrasal-verbs.md` 1304→822 entries (moved
      out 500, moved in 22, merged 4 collisions).
- [x] Verified: header/back-link counts self-consistent, all ~5300 combined
      index/TOC anchor links resolve (checked against the same slugify logic
      `build_docs.py` uses), spot-checked a merged entry (`Caveat`) and a
      cleanly-moved one (`Chalk out`), confirmed pronunciation guides from
      Phase 4b survived the full re-render (335 present after vs 327 before
      — the +8 came from moved-in words that already had their own guide).
      Re-ran the misclassification scan after writing: 0 single words left
      in `phrasal-verbs.md`, only the deliberately-kept `Inside out` left in
      `vocab.md`.
- [ ] The remaining ~2 points of `vocab ∩ phrasal-verbs` overlap noted above
      (80 total, 78 resolved here) — negligible, re-check next time
      `dedupe.py` runs across both files.

### Phase 4 — Fill missing explanations (definition / PoS / example / figurative vs literal)
Multi-session grind, one file and one severity tier at a time. Never run a
regex substitution that spans from one heading to "the next occurrence of the
back-link" — several entries have an empty body (heading immediately followed
by the back-link with no blank-line padding), which makes such a regex
swallow one or more unrelated entries. `scripts/audit_gaps.py` (below) and any
future batch-fill pass must locate each entry by **heading-line index only**
(`# Title` → next `# ` heading), never by pattern-matching the back-link.

- [x] Build `scripts/audit_gaps.py` (heuristic: word count of entry body,
      whether it contains a quoted example sentence, whether it contains a
      part-of-speech / "means" cue). Run per file, sort worst-first.
- [x] `vocab.md` — fill the 60 entries that had ≤8 words and no example
      (2026-07-13). Remaining: 66 entries <15 words, ~306 with no
      example sentence at all — next batch should take the <15-word tier.
- [x] `phrasal-verbs.md` — fill the 59 entries that had ≤8 words and no
      example (2026-07-13). Remaining: 37 entries <15 words, ~390 with no
      example sentence.
- [ ] `phrasal-verbs.md` — next batch: the <15-word tier (37 entries).
- [ ] `vocab.md` — next batch: the <15-word tier (66 entries).
- [ ] `idioms.md` — mostly rich already; spot check the 6 flagged by the
      audit script (false positives likely — verify before editing).
- [ ] `glossary-usage.md` — uses `## Title` (not `# Title`) headings; audit
      script needs a heading-level flag before it can scan this file.
- [ ] After each file's tail is done, add figurative-vs-literal call-outs to
      entries that have both senses but only show one today (chisel, bury,
      sandbox, etc. are the pattern to follow).
- [ ] Standardise heading levels and section labels once content gaps are closed.

**Working method for future sessions:** run `python3 scripts/audit_gaps.py
<file>`, take the next worst N entries (start with N≈50–60, matches one
sitting), draft Meaning + PoS + example (+ figurative/literal split where the
word has both) in a `%%TITLE%%/%%BODY%%/%%END%%` scratch file, apply with
`scripts/apply_enrich.py <file> <scratch>`, then diff-check that
`grep -c "^# "` is unchanged and no unrelated headings were dropped before
committing.

### Phase 4b — Add pronunciation guides
Same multi-session, batch-at-a-time approach as Phase 4, and the same
insertion safety rule applies: `scripts/insert_pronunciation.py` locates each
entry by its exact `# Title` heading-line index and only *inserts* a new
`*Pronunciation:* ...` line right after the heading — it never replaces or
deletes existing lines, so it carries none of the over-matching risk Phase 4's
first (buggy) attempt had.

**Format decided:** hyphen-separated syllables with the stressed syllable in
CAPS, e.g. `*Pronunciation:* uh-STOOT` (astute). Chosen over the handful of
pre-existing dot-separated guides (`(kuh·rayj·uhs)`, no stress marked)
because marking stress is the higher-value signal for a non-native speaker —
wrong stress placement is a more common source of being misunderstood than
the vowel sounds themselves. Existing dot-style guides are left as-is for now
(not worth a mechanical reformat pass until content gaps are closed); if
they're ever normalized, do it as its own reversible, single-purpose commit.

**Scope note:** pronunciation guides add the most value on `vocab.md`
(single, often Latinate/advanced words — the ones actually mispronounced).
Most `phrasal-verbs.md` and `idioms.md` entries are common everyday words
already spoken correctly (*fire up*, *walk away*, *goofy*) — for those files,
only add a guide where a specific word inside the phrase is genuinely
non-obvious (e.g. a loanword), not mechanically to every entry.

- [x] Build `scripts/insert_pronunciation.py`.
- [x] `vocab.md` batch 1 — 59 entries, A–C range, picked for genuinely
      non-obvious stress/spelling (Aberration, Aegis, Amenity, Aplomb,
      Assiduously, Brusque, Capitulate, Caveat, Chastise, …) (2026-07-13).
- [x] `vocab.md` batch 2 — 65 entries, Circumspect → Divulge (mid-C through
      mid-D), same curation method (2026-07-13).
- [x] `vocab.md` batch 3 — 75 entries, Dogma → Fugitive (rest of D through
      end of F), same curation method (2026-07-14).
- [x] `vocab.md` batch 4 — 77 entries, Galvanize → Junta (G through J),
      same curation method (2026-07-14).
- [x] `vocab.md` batch 5 — 51 entries, Kooky → Nuisance (K through N),
      same curation method (2026-07-14).
- [x] `vocab.md` batch 6 — 79 entries, Obfuscate → Punitive (O through P),
      same curation method (2026-07-16).
- [x] `vocab.md` batch 7 — 80 entries, Quay → Stifling (Q, R, and into S),
      same curation method (2026-07-16).
- [ ] `vocab.md` batch 8 — continue from **Stifle** (missed in batch 7 —
      "Stifling" got covered but the base form "Stifle" was skipped by
      mistake; pick it up first) through the rest of S and into T. ~870
      vocab entries remain unguided; picking up mid-list per the curation
      rule (skip simple/common words; prioritize Latinate, low-frequency,
      or silent-letter words).
- [ ] `vocab.md` batches 8+ — continue alphabetically until the file is done.
- [ ] `phrasal-verbs.md` / `idioms.md` — light pass only, per the scope note
      above; most entries don't need one.
- [ ] `glossary-usage.md` — blocked on the same `## ` heading-level issue as
      Phase 4.

**Working method for future sessions:** pick the next ~50–60 word-bank
entries lacking a pronunciation guide (`python3 scripts/audit_gaps.py` can be
adapted, or just scan headings manually for the next alphabetical slice),
skip words whose pronunciation is already obvious to an English speaker,
draft `%%TITLE%%/%%PRON%%/%%END%%` entries, apply with
`scripts/insert_pronunciation.py <file> <scratch>`, then confirm
`grep -c "^# "` is unchanged before committing.

### Phase 5 — Revision features
- [ ] Anki/CSV flash-card export per word bank (`scripts/export_cards.py`).
- [ ] Optional tags: theme (tech / daily / business) and difficulty, to enable
      filtered revision on the site.
- [ ] "Random 20" / daily-revision view on the site.

### Phase 6 — Maintenance
- [ ] Document the §5 pipeline in README for future source docs.
- [ ] Optional CI: run `make check` on push.

---

## 7. Safety & verification gates (run at every automated step)

1. **Content conservation** — word count and table-row count of (new files) ==
   (old files), within a tiny delta explained only by generated TOC/back-links.
2. **No orphaned anchors** — every generated index / TOC link resolves to a real id.
3. **Link check** — `scripts/check_links.py` passes.
4. **Build** — `make docs` succeeds; `search-index.json` targets all resolve.
5. **Commit boundary** — one commit per file/step, so any change is revertible.
6. **Spot-check** — read a random sample of merged entries by eye.

> Rule: never delete a source/old file until its content is proven to live in the
> new location by gates 1–2.

---

## 8. Open decisions (need your call before the relevant phase)

| # | Decision | Options | Default |
|---|----------|---------|---------|
| D1 | De-dup policy | keep-richest vs merge-all-notes | **merge-all unique notes** |
| D2 | Rich vs terse entries | standardise to schema vs keep as-is | **keep rich, add missing Meaning/Example** |
| D3 | `mental-models.md` | keep as reading vs fold into a "reading" folder | keep at root |
| D4 | Tagging (Phase 5) | add theme/difficulty metadata or not | add lightweight tags |
| D5 | Flash cards | Anki `.apkg` vs plain CSV/TSV | **CSV/TSV** (portable) |

---

## 9. Tooling (scripts/)

| Script | Role | Status |
|--------|------|--------|
| restructure.py | Google-Docs → clean A–Z word bank | done |
| clean_thematic_docs.py | clean thematic/mixed docs | done |
| split_vocab_usage.py | split by content type | done (generalise in Phase 3) |
| build_docs.py | render HTML site + search index | done |
| check_links.py | validate relative links | done |
| dedupe.py | merge duplicate entries | done |
| route.py | classify + route blocks to canonical files | **Phase 3** |
| export_cards.py | flash-card export | **Phase 5** |
