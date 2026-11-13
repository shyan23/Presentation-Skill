# Durable skill-memory learning loop

Reloading this skill is **context retrieval**, not fine-tuning. Preserve improvements in small reviewed evidence records so future sessions incorporate them. Keep quality over quantity.

## Four memory layers
1. `SKILL.md` — stable mandatory behavioral contract; modify sparingly.
2. `references/` + `profiles/styles.json` — tested design knowledge and style descriptors.
3. `memory/feedback.jsonl` — append-only, real reviewer feedback, tagged with context, failure type and approved fix.
4. `memory/active-lessons.md` — compact, auto-regenerated summary read at every run after the router; manually verify false conflicts before reusing.

## Feedback discipline
Record only meaningful improvements: `(context → observed failure → revision → evidence → applicability → anti-pattern)` and include date. A single comment "looks bad" is not enough to infer a general rule. Distinguish preference from objective failure, and do not store names, private project content, or proprietary data without permission.

## Record feedback
```bash
python scripts/record_feedback.py --context "10 min research talk"  --issue "annotation labels on small plots were unreadable"  --fix "use 18+ pt labels or split figure into two slides"  --evidence "reviewer approved revision"  --category readability --reviewed
```

After recording, new runs should read `memory/active-lessons.md`. Scores should use actual criteria: message retention in feedback, task accuracy, clarity, projection readability, design consistency, native editability, and user acceptance—not vanity measures.

## Promotion rule
A learned point becomes a default guideline only if supported by 2+ independent reviewed projects or a strong source plus a successful transfer test. Otherwise treat it as context-specific. Keep change log with provenance. If new learning conflicts with accuracy/accessibility, accuracy/accessibility wins.

## Review cadence
After every 3–5 significant decks, compare outcomes against critique rubric. Choose one small process change rather than rewriting the skill wholesale. Keep 5–12 high-value active lessons, archive older ones. Generate design variants intentionally to test generalization.
