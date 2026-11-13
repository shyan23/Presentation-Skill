# Anti-slop diagnosis and repair

Slop is **generic design behavior** that distracts from an idea or creates a false impression of polish. Not every gradient, icon, or card is wrong; misuse and repetition are the problem.

## Priority-weighted audit (0 none, 1 mild, 2 severe)
| Dimension | Observable tell | Targeted remedy |
|---|---|---|
| Purpose | Slide has no unique audience question | Give it a job; merge or delete if duplicate |
| Truth | Assertions not tied to evidence | Cite, qualify, or turn into a question |
| Copy | Buzzwords, "in today's rapidly evolving...", meta phrases | Replace with concrete nouns, active verbs, actual stakes |
| Headlines | Every title says only "Overview", "Benefits", "Key takeaways" | Convert to evidence-backed assertion |
| Composition | All slides = three rounded cards or title+4 bullets | Choose functional layouts: comparison, mechanism, evidence hero |
| Alignment | Jagged edges, inconsistent margins | Set a grid and baseline system |
| Hierarchy | Everything bold, same contrast, decorative big title | One focal object, secondary text subdued |
| Aesthetic | Purple-blue gradients / glows / random emoji everywhere | Restrained palette anchored to subject |
| Images | Plastic 3D blobs, empty stock handshake, generic rocket | Specific artifact or conceptual art that contributes meaning |
| Charts | Pie without purpose, dense labels, missing axis or comparator | Reconstruct as an honest analytic proof |
| Icons | Mismatched line widths, meaningless icon labels | Normalize or remove; use text or real visuals |
| Rhythm | Every slide mechanically identical | Vary shape according to information architecture |
| Technical | Cropping, tiny labels, overlapped footnotes, rasterized editable content | Fix after actual render; preserve native objects |
| Accessibility | Color-only encoding, unreadable contrast, rapid motion | Independent visual cues, higher contrast, calm transitions |

## Remediation order
1. Facts / source fidelity (can't decorate a lie).
2. Narrative: does the presentation make a coherent argument?
3. Layout and spacing: correct margins, information density, panel structures.
4. Typography and copy: specific language, headline hierarchy, line wrapping.
5. Color, charts, icon/image choices: semantic design, not pretty noise.
6. Polish: alignment, border/shadow restraint, brand texture, transitions.
7. Rerender and compare against original. Don't declare success from a code diff.

## Important counterexamples
- Three columns can be best for a genuine three-way mutually comparable taxonomy; avoid them only when arbitrary.
- A consistent visual system is valuable. Breaking every slide's grid to look "human" is counterproductive.
- Research slides may be dense for an expert audience; prefer annotated detail and a talk+appendix split rather than deleting necessary content.
- Some branded themes intentionally use gradients or rounded cards. Honor brand constraints, remove only purposeless repetition.

## Anti-slop transformation examples
- **Before:** "Leveraging Innovative Solutions" + 3 generic bulb icons. **After:** "Automating the reviewer queue removes two manual handoffs" + verified workflow before/after diagram.
- **Before:** "Our Impact" + giant "80%" without denominator. **After:** "8 of 10 trial users completed onboarding" + study N, time period, caveat; only if real data exists.
- **Before:** flowchart of 6 identical circles with wavy arrows. **After:** named decision nodes, data inputs, error conditions, branch semantics and explicit output.

## Audit report format
`slide | severity | defect | why it matters | exact fix | evidence check | render check`
Give 3 cross-deck issues and 5 highest-priority slide fixes first; expand to every slide if requested. Avoid pretending taste is objectively quantifiable; scores organize review, not replace judgment.
