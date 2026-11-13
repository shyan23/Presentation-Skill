# Workflow: build new deck

**Inputs**: brief, notes, file/source, audience, duration, output medium. **Outputs**: argument map, style contract, editable deck or requested format, QA report.

1. Read `SKILL.md` and `memory/active-lessons.md`; inspect given material.
2. Define audience decision and one sentence thesis; inventory confirmed facts and placeholders.
3. Select narrative arc from `references/story-architecture.md` and draft numbered slide map.
4. Choose primary style via `profiles/styles.json`; articulate aesthetics in typography, grid, palette, imagery, chart semantics.
5. Associate each slide with function from `references/slide-functions.md` and layout from `references/visual-grammar.md`. Limit arbitrary card grids.
6. Build native slide components, real figures and speaker notes as requested. Store data/source ledger.
7. Audit source integrity; run `scripts/audit_pptx.py` for PPTX; render and visually verify every slide.
8. Deliver with an editable primary, any requested PDF fallback, and concise known limitations.

**Stop conditions**: core evidence missing and cannot be reasonably framed as placeholder; every requested output must clearly show unresolved items rather than fabricated proof.
