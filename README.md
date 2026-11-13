# Slide Design Mastery — an agent skill for un-slopping slides

A portable agent skill that teaches Claude Code, Codex, and other skill-aware agents to **design, audit, and redesign presentation decks** with a real argument, an intentional visual style, honest data, and editable output — instead of generic AI "slide slop".

> [!NOTE]
> **Inspired by [How to Unslop Your AI-Generated Slides](https://www.youtube.com/watch?v=fkxw0SrwVkA) by [Analyst Academy](https://www.youtube.com/@AnalystAcademy).**
> The video's message, that AI-generated decks need deliberate design work to stop looking generic, is what started this project. Go watch it and support the channel.

---

## What it does

| Mode | You ask | The agent does |
|---|---|---|
| **New deck** | "Make a 12-slide thesis defense from my paper" | Writes the argument first (story arc, slide map, one claim per slide), then applies a style |
| **Unslop** | "Fix this AI-generated PPTX" | Finds clichés and defects, then fixes them without changing verified facts or slide intent |
| **Restyle** | "Show this deck in three different styles" | Uses the same narrative with different type, layout, and chart treatments |
| **Audit only** | "Critique this deck, don't edit it" | Returns BLOCKER / MAJOR / MINOR findings with a repair for each slide |

What it checks:
- **Story before style.** Every slide gets a job, an answer-style headline, and something that proves its claim.
- **14 visual styles.** Each is a full token set, not just a color swap.
- **Source integrity.** Given facts, calculations, assumptions, and placeholders are labeled separately, so numbers aren't made up.
- **Editable output.** Native shapes and charts, not flattened screenshots.
- **Accessibility and QA.** Contrast, reading order, and a check of each rendered slide.
- **Learning loop.** Only reviewed feedback is saved as a lasting lesson.

## Style profiles

```
swiss-grid            executive decisions, consulting, evidence-first talks
editorial-journal     cultural narratives, journalism, case studies
cinematic-keynote     big-stage keynotes, vision, product reveals
academic-precision    thesis defenses, ML results, engineering
data-newsroom         investigations, economic reporting, data briefing
luxury-minimal        premium brands, fashion, high-end property
playful-classroom     students, workshops, beginner lessons
startup-narrative     fundraising, product demos, business growth
neo-brutalist         creative agency, bold product brand, manifesto
archival-museum       history, museum narratives, heritage, photography
dark-technical        software architecture, infrastructure, engineering
corporate-restraint   board reviews, governance, compliance, operations
experimental-collage  creative direction, art concepts, community narratives
bangla-contemporary   Bangla education, Bangladesh storytelling, mixed-script talks
```

## Install

```bash
git clone https://github.com/shyan23/Presentation-Skill.git
cd Presentation-Skill

# Claude Code — this project only
mkdir -p .claude/skills && cp -r skill/slide-design-mastery .claude/skills/

# Claude Code — all projects
mkdir -p ~/.claude/skills && cp -r skill/slide-design-mastery ~/.claude/skills/

# Codex / other agents that read .agents/skills
mkdir -p ~/.agents/skills && cp -r skill/slide-design-mastery ~/.agents/skills/
```

Restart the agent, or reload skill discovery, after you install.

## Usage

Ask in plain language. The skill triggers on words like *slides*, *deck*, *unslop*, *pitch deck*, *thesis defense*, or *slide audit*:

```text
Use slide-design-mastery to audit this PPTX and unslop it without changing
meaning or slide order. Pick editorial or Swiss style. Return a before/after defect list.
```

```text
Use slide-design-mastery to design a 12-slide research defense in academic-precision
style. Native editable diagrams, visible citations, render-by-render QA.
```

```text
Develop three different visual directions (swiss-grid, editorial-journal,
dark-technical) for the same 8-slide narrative without changing the conclusions.
```

More prompts are in [`prompts/activation-prompts.md`](skill/slide-design-mastery/prompts/activation-prompts.md).

## Helper scripts

The scripts need Python 3.9+ and nothing else, except the PPTX audit, which needs `python-pptx`. Run them from `skill/slide-design-mastery/`:

```bash
python3 scripts/select_style.py --list                 # list styles
python3 scripts/select_style.py --id swiss-grid        # show one style's tokens
pip install python-pptx && python3 scripts/audit_pptx.py deck.pptx --json report.json
python3 scripts/import_transcript.py ...               # turn your own transcript into evidence chunks
python3 scripts/record_feedback.py --reviewed ...      # save a reviewed lesson to memory/
python3 scripts/validate_skill.py                      # check the package's integrity
```

## Layout

```
skill/slide-design-mastery/
├── SKILL.md        # router + operating contract (entry point)
├── references/     # story, visual grammar, data/diagrams, accessibility, anti-slop, QA ...
├── workflows/      # new-deck, unslop-existing-deck, audit-only
├── profiles/       # styles.json — 14 style token sets
├── examples/       # investor pitch, academic defense, teaching lesson
├── scripts/        # local CLI helpers
├── memory/         # reviewed lessons, read on future runs
├── sources/        # video provenance + space for verified transcripts
└── tests/          # agent evaluation cases
```

## Credits & attribution

- **Inspiration:** [*How to Unslop Your AI-Generated Slides*](https://www.youtube.com/watch?v=fkxw0SrwVkA) by **[Analyst Academy](https://www.youtube.com/@AnalystAcademy)** on YouTube. All credit for the idea and the "unslop" framing goes to them.
- **Honesty about what's in this repo:** The video's transcript was not used to build this skill. The guidance here is an independent design system *inspired by* the video. It is **not** a transcript, summary, or official reproduction of Analyst Academy's teaching, and it doesn't speak for them. See [`sources/VIDEO_SOURCE.md`](skill/slide-design-mastery/sources/VIDEO_SOURCE.md).
- If you have the rights to use the transcript, you can import it with `scripts/import_transcript.py` and follow `references/source-learning.md` to add claims tied to timecodes.
- Check the licenses for any fonts, logos, photos, or video frames before you use them in a deck.

---

*If this skill saved you from another gradient-blob title slide, please thank [Analyst Academy](https://www.youtube.com/@AnalystAcademy) for the inspiration.*
