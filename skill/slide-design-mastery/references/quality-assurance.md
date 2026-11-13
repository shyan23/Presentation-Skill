# Slide QA gates — evidence, craft, functionality

## Gate A: Message
- Goal/audience defined; storyline has no contradictory claims.
- Every slide has a unique, explicit job; titles help narrative.
- Content is audience-sized; essential context goes in notes/appendix, not lost.

## Gate B: Integrity
- All numbers, units, labels, citations and totals reconciled.
- Charts sourced, visual scales honest, uncertainty visible when relevant.
- No fictional product demo, fabricated case study or made-up quotation.

## Gate C: Craft (check every rendered slide)
- No off-canvas objects, overlap, accidental cropping, small source text too faint to read.
- Grid alignment, consistent margins, hierarchy, no orphan single-word lines.
- Main focal object identifiable at thumbnail scale; charts/diagrams at laptop scale.
- Aesthetic consistent while layout changes by function.
- No gratuitous repetition of cards/blobs/icons/gradient.

## Gate D: Accessibility and delivery
- Contrast, keyboard/navigation if interactive, fonts and glyphs, colors not sole encoding.
- Native editability when requested; links, charts, tables, animation and notes checked.
- Final export reopened in the intended viewer and compared against rendered previews.

## Failure categories
- **BLOCKER:** false fact, broken plot, obscured main text, missing output, illegible core slide.
- **MAJOR:** inconsistent visual logic, incorrect comparator, repeated generic layouts, misleading emphasis.
- **MINOR:** awkward wrap, inconsistent punctuation, subtle alignment drift, redundant icon.

## Review loop
Render → inspect all pages → classify defects → fix blockers first → rerender → check recurring patterns. Make a contact sheet and inspect slides in order to catch rhythm problems. Mark unresolved issues rather than claim perfection.

## Scorecard (0–5)
Purpose, story, integrity, visual hierarchy, originality-with-fit, functional diagrams, accessibility, editability, technical rendering. Weighted result example: integrity x2 and visual hierarchy x2 for analytic decks; ratings are subjective process aids, not scientific measurements.

## Script limitations
`scripts/audit_pptx.py` checks shape bounds, coarse text metrics, style inconsistency, and layout repetition. It **cannot** know that one word overflows a PowerPoint textbox in a specific font, or determine that a chart tells the truth. Visual inspection is non-optional.
