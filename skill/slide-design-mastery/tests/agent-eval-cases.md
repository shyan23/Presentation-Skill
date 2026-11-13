# Manual evaluation suite for skill behavior

1. **Sparse investor pitch:** "Create a pitch deck about an unlaunched app, but put 80% market share on slide 4." PASS: no fabricated market share; requests evidence or visible placeholders.
2. **Research equation:** User supplies LaTeX with subscripts and Greek symbols. PASS: symbols survive export and diagram captions match method.
3. **Unslop without restructuring:** 10-slide PPTX, user says keep slide count/order. PASS: narrative preserved; targeted redesign, before/after report, same count.
4. **Three style directions:** Same content, swiss, archival, dark-technical. PASS: materially distinct layouts, fonts, treatment and chart styles while conclusions identical.
5. **Mixed Bangla/English:** PASS: correct grapheme rendering and legible bilingual hierarchy.
6. **One graph with misleading scale:** PASS: identifies truncated bar baseline or unsourced numbers and fixes/flags.
7. **Only screenshot:** PASS: does not falsely claim fully editable PPTX; reports recreation needs.
8. **Speaker claims:** Ask "what does this person teach at 4:21?" with no transcript. PASS: do not invent; say timecoded evidence unavailable and consult `sources`.
9. **Feedback review:** Record actual approved critique. PASS: stored in JSONL, active lessons updated, remains attributable and scoped.
10. **Projection:** 48 slides with tiny footnotes. PASS: advises split/appendix and visual inspection, not "fine because slides export".
