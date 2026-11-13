---
name: slide-design-mastery

description: Create, critique, and redesign compelling presentations with intentional visual aesthetics, clear story, functional diagrams and charts, editable output, and evidence-based improvement. Trigger on make slides, redesign slide, unslop, presentation aesthetic, art direction, investor deck, academic defense, technical talk, keynotes, slide audits, or deck review.
---

# Slide Design Mastery — Anti-Slop Art Director + Presentation Engineer

## Purpose
Treat slides as a communication system, not a collection of decorated rectangles. Produce an audience-specific argument, a deliberate aesthetic, and a technically correct, usable deck. When asked to *unslop*, preserve the verified meaning and slide intent while eliminating default AI presentation clichés. This skill supports creating new decks, rewriting, auditing, restyling, building editable decks, and iterating after critique.

**Evidence honesty:** This library was inspired by the public video **“How to Unslop Your AI-Generated Slides”**, https://www.youtube.com/watch?v=fkxw0SrwVkA. Its full transcript was not available during preparation. Do not present these instructions as verbatim or definitive teachings of its speaker. Treat them as an independently developed, evidence-labeled expansion. Only assert video-specific ideas after a transcript or frame reference has been added to `sources/` and checked using `references/source-learning.md`.

## Fast activation / router
Before designing, classify user intent and read the minimum necessary reference modules:

| User intent | Read these files |
|---|---|
| New deck from topic or notes | `references/story-architecture.md`, `references/visual-grammar.md`, `references/slide-functions.md`, `profiles/styles.json` |
| Make AI deck less generic | `references/anti-slop-audit.md`, `references/design-systems.md`, `workflows/unslop-existing-deck.md` |
| Pick aesthetic / 'attire' | `references/aesthetic-directions.md`, `profiles/styles.json` |
| Technical / academic / research | `references/academic-technical.md`, `references/data-and-diagrams.md`, `references/source-integrity.md` |
| Investor / sales / business | `references/story-architecture.md`, `references/data-and-diagrams.md`, `references/slide-functions.md` |
| Build PowerPoint/HTML/Google Slides | `references/engineering-and-editability.md`, `references/quality-assurance.md` |
| Learn more from this creator or examples | `references/source-learning.md`, `references/learning-loop.md` |
| Give rigorous critique only | `workflows/audit-only.md`, `references/anti-slop-audit.md` |

Always read `memory/active-lessons.md` if it contains actual reviewed learning. Treat entries as local preferences/examples, not verified universal truths. Read other modules on demand, not all at once; this keeps reload efficient.

## Operating contract — follow in order

### Phase 0. Determine the contract
1. Identify audience, decision, presentation setting, duration, format, aspect ratio, required brand assets, sources, and language. If absent, make a visible reasonable assumption and proceed unless a missing detail is truly blocking.
2. Choose whether the output is **slides as an editable artifact**, **a visual storyboard**, **a critique**, or **a written outline**. Do not confuse a raster picture of slides with an editable PPTX.
3. Protect source fidelity: distinguish given facts, sourced facts, calculations, assumptions, placeholders, and artistic concept imagery. Keep brand/legal/research constraints.

### Phase 1. Write the argument before applying style
1. State the one-sentence audience takeaway and expected action.
2. Arrange a story arc: context → tension/problem → evidence → key insight → solution/implication → action. For academic lectures, replace persuasion beats with prerequisite → question → method → experiment → result → limitation → implication.
3. Produce a slide map. For every slide: **job**, answer-headline, one claim, proof object, intended visual, source, and spoken-versus-visible content.
4. Delete any slide that repeats a neighboring claim without a new cognitive function.
5. Headlines should state findings ("Latency fell 38% after caching") rather than neutral topics ("Results"). Never invent the underlying result.

### Phase 2. Choose visual attire / direction deliberately
1. Choose exactly **one primary** style from `profiles/styles.json`, optionally one restrained accent influence. State why it serves the specific audience and topic. Do not blend every trend.
2. Define font role pairs, 4–6-color palette, grid, margins, spacing scale, image treatment, chart treatment, and motion policy.
3. Choose a repeatable visual identity (motif, editorial cue, or unique artifact from the topic), **not** a generic gradient/blob/shadow system.
4. Lay out key slides first: title, central proof, hardest diagram, main comparison, and closing action. Extrapolate a system from these.

### Phase 3. Choose slide function before layout
Select one primary function per slide from `references/slide-functions.md`: orientation, claim, evidence, comparison, mechanism, process, timeline, taxonomy, spatial, quote, case, decision, interactive demo, recap, or action. Select a suitable layout from `references/visual-grammar.md`. A layout should serve thinking, not just vary for variety.

### Phase 4. Build with disciplined craft
- One dominant point per slide; no rule that all slides must have the same number of bullets.
- Use visual hierarchy through contrast, scale, whitespace, alignment, grouping, and proximity.
- Keep text comfortable at intended viewing distance. Default large-screen talk body to ~24–32 pt, footnotes/citations smaller only when necessary; dense handout decks may depart intentionally.
- Prefer **true diagrams, plots, real screenshots, clean tables, annotated original images** over decorative AI art.
- Make important elements editable when the requested output is PPTX: native text, shapes, real charts/tables, semantic groups. Flag embedded images and non-editable objects.
- Do not invent data, numerical claims, screenshots, credentials, or sources. Ask for data or mark placeholders.
- Match all visual details to the semantic claim (e.g. a bar chart for categorical comparison, not a pie because it looks stylish).

### Phase 5. Run the anti-slop pass
Audit all slides against `references/anti-slop-audit.md`:
- Generic title/stock image/opening/ending, robotically consistent three-column cards, rounded boxes everywhere, excessive gradients, shiny illustrations, random icons, overused all-caps eyebrow labels.
- Repeated rhythm without reason, text overload, indistinct priorities, meaningless data visualization, unreadable labels, false visual precision.
- **Do not replace functional consistency with gratuitous novelty.** Preserve a coherent deck-level system while varying slide types by semantic function.

### Phase 6. Functional and visual QA
Use `references/quality-assurance.md` and `references/source-integrity.md`.
1. Verify every number, formula, label, quote, data series, time period, and citation against supplied evidence.
2. Render slide images; visually inspect every slide at presentation size for clipping, overflow, hierarchy, contrast, spacing, and legibility. Repair and render again.
3. For PPTX, audit native objects and page bounds with `python scripts/audit_pptx.py deck.pptx --json report.json` (optional `python-pptx` dependency). A script cannot fully detect visual overlaps or semantic mistakes, so human visual review remains mandatory.
4. Check a slide contact sheet for rhythm and variation, and compare the deck to the original brief.
5. Delivery: supply requested files and brief design notes. Clearly disclose any unfinished, unverifiable, or flattened elements.

### Phase 7. Feedback and compounding learning
Only when the user or a real reviewer gives actionable feedback, record the observed defect, context, fix, and evidence with `scripts/record_feedback.py`; the script rebuilds `memory/active-lessons.md`. If user supplies a verified transcript or frames, use `scripts/import_transcript.py` and annotate claims; do not pretend the model weights changed. The *external skill memory* improves future runs because the agent re-reads it.

## Branch rules
- **Audit-only:** report highest-impact defects by slide and fixes; never silently edit. See `workflows/audit-only.md`.
- **Restyle existing deck:** preserve message, numbers, and slide order unless authorized to restructure. Keep a before/after list. See `workflows/unslop-existing-deck.md`.
- **Academic / technical:** accuracy, readable equations, and visible evidence outrank trendiness. See `references/academic-technical.md`.
- **No source material:** create a *clearly labeled concept deck* with no unsourced empirical results.
- **Accessibility constraints:** contrast, color-independent encoding, reading order, alt text, captions, and sensible transitions outrank style; see `references/accessibility.md`.
- **Native deck requested:** do not deliver only rendered slide PNGs pretending they are editable. See `references/engineering-and-editability.md`.

## Deliverable quality gate
Only call a deck "finished" when its message, design, accuracy, editability (when required), and final render pass. If the user asks for a fast draft, label it a draft. Include a short assessment with what changed and limitations, not a large self-congratulatory summary.
