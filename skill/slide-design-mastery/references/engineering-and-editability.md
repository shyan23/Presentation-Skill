# Engineering decks that remain functional

## Requirements by output
| Output | Must be editable? | What to verify |
|---|---:|---|
| PPTX / PowerPoint | If user requests | native text, shapes, diagrams; chart editability where possible; alt text and speaker notes |
| Google Slides | Usually yes | live text/shapes and template/theme consistency; ensure imports don't flatten content |
| PDF | No | each slide readable, links work, fonts embedded appropriately, navigation if required |
| HTML slides | yes in source | responsive layout, 16:9 projection mode, keyboard controls, print/PDF fallback, accessibility |
| PNG/JPG slide images | No | aspect ratio, text correct, export legibility, acknowledge non-editability |

## PowerPoint architecture
Prefer theme/master, reusable slide layouts, placeholders for stable content, native tables/charts/text where feasible. Native objects facilitate changes when content evolves. Avoid 300 ungrouped shapes for a simple UI screenshot, but don't flatten a diagram that needs editing. If a screenshot is unavoidable, keep source file and cite it.

## Export pipeline
1. Validate outline and sources.
2. Build deck in PPTX/HTML/Slides.
3. Render to slide PNGs and optionally contact sheet.
4. Inspect for boundaries, layout, cropped data labels, missing fonts, incorrectly flattened math, contrast, content ordering.
5. Revise, rerender, reopen/export to required formats.
6. Deliver the native project plus view-only fallback if requested.

## Functional enhancements
- Hyperlinks, table of contents, section tabs, reveal states, and embedded demos should solve a use-case; test all links and states.
- Notes provide speaker detail rather than crowding slide canvas.
- Build a fallback screenshot/recording for any live demo that relies on Wi-Fi or a fragile service.
- Keep code snippets copyable and syntax valid. Do not render every code block as an image if reuse matters.

## Tool recommendations (non-exclusive)
- `pptxgenjs` / `python-pptx` for native PPTX creation and static structure checks.
- PowerPoint/LibreOffice renderer for visual QA (if available in environment).
- Browser presentation libraries when web delivery specifically requested.
- SVG for line art and precise diagrams; convert with care if native editability is required.

## Asset hygiene
Use licensed images/fonts, track credit, and don't invent partner or brand logos. For client proprietary media, keep only what the user authorizes. Do not store sensitive deck content in global skill memory.
