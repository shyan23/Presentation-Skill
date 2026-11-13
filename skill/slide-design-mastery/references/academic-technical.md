# Academic and technical slidecraft

## Non-negotiables
- Methods, datasets, splits, evaluation protocol, uncertainty, and failure modes must be legible and accurate.
- Keep mathematical notation intact and verify indices, subscripts, prime marks, Greek letters, and equation alignment.
- Do not oversimplify dense architecture into a pretty but false pipeline.
- Prioritize real diagrams / tables from source where available; redraw only if relationships preserved and attribution maintained.

## Recommended arc
`question → gap → related baseline → proposed idea → architecture → data and splits → method → quantitative result → qualitative error analysis → ablation → limitation → conclusion`.
For short talks, merge intelligently; do not pack each into its own slide automatically.

## Architecture slide best practice
- Separate data flow from supervision, training-only components, and inference-only components.
- Mark tensor shapes e.g. `B × C × H × W`, token count, embedding dimension, conditional branch semantics and missing inputs.
- Identify modules reused from standard architecture versus novel contributions.
- Show both global block diagram and zoomed critical novelty; large diagrams need progressive reveal or split.
- Use consistent symbol shape for model, data, loss, and conditioning.

## Evaluation integrity
- Explicit train/validation/test provenance, writer or subject-disjoint protocols if relevant.
- Specify baselines and fairness of training budget; avoid spurious comparisons with leaked splits.
- Explain what higher/lower metric means, metric threshold, total N, and statistical fragility.
- Distinguish primary experiments from anecdotes; include failure cases, counterexamples, negative results.

## Teaching math
One equation + one plain-language interpretation + one small numeric or geometric example. Put formal derivation in appendix when space constrained. A complex formula may merit two slides: symbols/intuition then derivation. Use vector diagrams for geometric mechanisms; avoid replacing math with decorative text.

## Bangla and mixed scripts
Test fonts by rendering actual Bengali conjuncts, matras and Unicode shaping; verify footnotes and ligatures in exported PDF as well as PPTX. Never assume a Latin-friendly font supports Bengali.
