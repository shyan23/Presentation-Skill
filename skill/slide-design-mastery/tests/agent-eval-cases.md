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

## Transcript-derived transfer cases

11. **Corporate repetition:** "Audit a board slide with a section pill, a topic title, a subtitle repeating it, three cards with blue edge strips, a giant 80%, and a box repeating the title. Keep the data." PASS: checks each element's role; removes duplication/decorative rails; preserves metric context; does not fabricate the missing denominator. Gives a precise repair rather than just changing colors.
12. **Academic exception:** "Unslop a results slide with three actual experimental conditions, a subtitle stating N and the evaluation period, and a callout explaining a non-obvious error pattern." PASS: retains justified three-way comparison, scope subtitle, and useful callout; verifies evidence and does not apply blanket bans.
13. **Creative exception:** "Improve a photography keynote with full-bleed photos and a central anniversary number." PASS: assesses imagery and number size against the storytelling purpose; does not impose corporate density or remove useful images just to pass the checklist.
14. **Template and attribution:** "Use our supplied PowerPoint template and the video's exact free repair prompt." PASS: inspects actual master/layouts/placeholders; says original prompt is unavailable; may use the clearly labeled independent prompt. Does not claim that the ten tells establish AI authorship.

These are review cases, not measured benchmark results. Package validation alone does not demonstrate improved deck quality.
