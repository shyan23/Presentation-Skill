# Design tokens and deliberate visual systems

## Required style contract
Declare the following before composing:

```yaml
style_id: swiss-grid
intent: rigorous, legible, decision-oriented
canvas: 16:9
palette: {background: '#F6F5F2', foreground: '#171717', accent: '#D94A3A', secondary: '#52616B', muted: '#DAD9D4'}
typography: {display: 'clean sans with bold weight', body: 'readable sans', numerals: 'tabular figures'}
layout: {grid: '12 columns', margin: '6% width', spacing: '8-point system'}
imagery: 'real-world evidence and precise crops'
shadows: none
borders: 'hairline only for structure'
motion: 'minimal reveal only when pedagogically necessary'
```

## Token hierarchy
- **Primitive tokens:** font sizes, spacing scale, border widths, radius, line weights, color hex values.
- **Semantic tokens:** hero/text, secondary/caption, border, background, source, success/warning/error (with accessible labels).
- **Component tokens:** title block, caption, chart, metric panel, image frame, section divider.
- **Slide tokens:** title layout and evidence layout may reuse same grid but different composition.

## Palette logic
Aim for neutrals carrying most structure and one meaningful saturated accent; choose cool/warm deliberately. Accents highlight the finding, not arbitrary words. Preserve contrast; contrast ratios vary by use but aim for WCAG AA 4.5:1 for ordinary text and 3:1 for large text (at least) when viewed on screen. Brand compliance overrides generic defaults if still accessible.

## Font decisions
Choose type for character: grotesk/sans for modern clarity, humanist sans for warmth and learning, serif display for editorial confidence, monospace for data/code metadata. Ensure Bengali/Arabic/CJK coverage where needed; Latin-only display fonts can cause fallback glitches. Never embed or distribute proprietary font files without rights.

## What not to do
Do not randomly alter every slide's palette, font, or border radius. Do not mistake adding decoration for design. Prefer 1 distinctive deck-wide motif that references the topic—e.g., circuit traces for network infrastructure used sparingly, redline annotation marks for review decks, page margins and running citations for museum essays.
