# Anti-slop diagnosis and repair

Slop is **generic design behavior** that distracts from an idea or creates a false impression of polish. Not every gradient, icon, or card is wrong; misuse and repetition are the problem.

## Ten source tells: inspect in context
Based on the user-supplied timestamped transcript of [Analyst Academy's video](https://www.youtube.com/watch?v=fkxw0SrwVkA). See `sources/VIDEO_SOURCE.md` for provenance and coverage. These are qualitative review cues; a single occurrence does not establish a defect or AI authorship.

| Time | Tell | Repair and legitimate exception |
|---|---|---|
| 0:38–1:00 | Pre-title labels: all-caps eyebrows or pills | Remove labels duplicating the title. Keep a concise section marker when it supplies useful navigation. |
| 1:02–1:22 | Overlapping text | Fix object bounds, wrapping, and spacing; inspect the rendered slide. Intentional layered imagery must still preserve readable text. |
| 1:22–1:55 | Formulaic titles: colon plus punchline; dash plus contrast | Write the specific, evidence-backed finding in natural language. Punctuation itself is not banned; repeated rhetorical formulas are the signal. |
| 1:55–2:39 | Too many dramatic takeaway boxes | Keep a box when it bridges to the next slide or reveals a non-obvious insight in the evidence. Remove boxes repeating the headline or merely declaring importance. |
| 2:39–3:10 | Colored strips along rounded box edges | Remove accent rails that only decorate. Retain an edge if it consistently encodes a meaningful category/status or is required by the brand. |
| 3:10–3:26 | Forced groups of three | Let the evidence determine item count and layout; don't invent or merge ideas to fill three cards. Three real comparable items remain valid. |
| 3:26–3:54 | Inflated significance | Replace claims of importance with the concrete consequence and evidence. Keep a clear perspective without unsupported drama. |
| 3:54–4:28 | Oversized numbers | Size the number to its analytical role; retain units, denominator, period, and comparison. A hero metric can work when it truly is the central evidence. |
| 4:28–5:16 | Unneeded subtitles and repeated commentary | Check pre-title, headline, subtitle, chart heading, and callout together. Remove repeated meaning; preserve necessary scope, units, caveats, and citations. |
| 5:16–5:31 | Too many images | Replace decorative imagery with relevant evidence or space. Image-heavy slides can suit visual stories; the speaker's objection concerns ordinary corporate contexts. |

### Attention cost and repair pass
For every visible element ask: what new information, navigation, or interpretation does it provide? Remove duplication before shrinking type. Distinguish the main conclusion in the headline from a useful secondary insight in a callout.

The source's three remedies (5:40–6:50) are to learn to spot the patterns, use a good template with a proper slide master/layouts, and run a targeted repair prompt after generation. Apply the checklist across the entire deck, then rerender. The original repair prompt was offered separately and is not available here; the prompt below is our own implementation.

**Reusable post-generation prompt:**
> Review this deck for the ten source tells listed above. For each actual defect, identify the slide, redundant or distracting element, and a concrete repair. Preserve verified claims, units, caveats, citations, and required slide order. Keep justified exceptions and explain them briefly. Use the supplied template's master and layouts where appropriate. Apply repairs when editing is requested; otherwise return findings only. Render the result and check overlap, readability, and deck-level repetition. Report unresolved issues.

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
