# Data visualization and systems diagrams

## Chart choice by analytic task
- Compare categories: ordered horizontal bars (long names) or vertical columns; baseline usually zero for lengths.
- Compare before/after paired subjects: slopegraph or dumbbell; if paired identity matters.
- Trend over time: line, with real time intervals; annotate change-point/uncertainty.
- Part-to-whole: stacked bars or small multiples; pie only for a few obvious proportions summing to a clear 100%.
- Distribution: histogram, box/violin (expert context), ECDF; show sample size.
- Relationship: scatter/hexbin with axes, units, potential confounders.
- Ranking: dot plot or sorted bars; avoid pseudo-3D charts.
- Flow volume: Sankey only if actual quantities available; otherwise use a process diagram.
- Matrix/correlation: carefully scaled heatmap with legible legend and colorblind-safe choices.
- Model comparison: scorecard only alongside protocol, CI/variance and test split.

## Honest design
- Label axis name, unit, period, sampling frame, sample size, source, and important caveats.
- Use consistent scales for repeated small multiples; show uncertainty when stakes justify it.
- Do not truncate bar baselines silently. For non-zero line baseline, emphasize actual range and disclose scale.
- Don't draw sharp precision from coarse data. Ensure symbols, signs, decimals, and totals reconcile.
- If the user's provided numbers conflict, surface the conflict; never pick the prettier one.

## Diagram grammar
Define named primitives: data, transform, decision, external actor, feedback, output. Use one shape role per primitive; use arrowhead direction consistently. Group by stage or ownership. For a neural network, label tensor dimensions and conditioning path; for data pipelines, show source, filters, train/val/test separation, caches, and leakage risks. Prefer 3-level progressive disclosure: whole system → subsystem → critical failure/decision.

## Accessible annotations
Use callouts near actual evidence, not detached legends. Avoid red/green-only semantics. For every color, provide text/shape encoding. Keep one salient difference highlighted and de-emphasize context.

## Example research result
Instead of a giant F1 figure in isolation: "Model A improves writer-held-out F1 from 0.69 to 0.74" **only if verified**, with dataset, split, metric definition, confidence interval if available, and source. If not, use placeholders or a visualized evaluation plan.
