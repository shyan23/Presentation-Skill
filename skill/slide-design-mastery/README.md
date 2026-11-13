# slide-design-mastery

A portable `.skill` folder to give Claude Code, Codex and other agent-skill readers a consistent method for designing, auditing, and improving slide decks. Here “attire” means **visual aesthetic/style** — 14 distinct visual treatments plus functional slide patterns and QA scripts.

## Source boundary
Inspired by [How to Unslop Your AI-Generated Slides](https://www.youtube.com/watch?v=fkxw0SrwVkA). The user-supplied timestamped transcript was reviewed on 2026-11-13. All ten tells and three remedies are mapped in `sources/VIDEO_SOURCE.md` and implemented in `references/anti-slop-audit.md`. Audio/frames and the separately offered creator prompt were not verified. The broader design system is an independent expansion.

## Install (Linux/macOS)
From the directory containing `.skill`:

```bash
# Claude Code (project local)
mkdir -p .claude/skills
cp -r .skill/slide-design-mastery .claude/skills/

# Codex / agents skill-compatible environments (project local)
mkdir -p .agents/skills
cp -r .skill/slide-design-mastery .agents/skills/
```

For global use, place the skill in `~/.claude/skills/slide-design-mastery` or `~/.agents/skills/slide-design-mastery` as appropriate for your agent. Restart the agent or reload skill discovery after installing; invoke with a matching request such as “Use slide-design-mastery to audit these slides.” File names and supported commands differ between agents.

## Three usage prompts

- “Use slide-design-mastery to design a 12-slide technical research defense. Style: academic-precision. Native diagrams/charts. Show citations and run visual QA.”
- “Audit this PPTX and unslop it without changing meaning or slide order. Choose editorial or Swiss design. Return a before/after defect list.”
- “Create a pitch deck. Choose an aesthetic suited to the audience, build an evidence-first story map, and use native editable PowerPoint shapes.”

## Memory is not model fine-tuning
The agent does not gain new weights merely by reloading. It can gain persistent context from `memory/active-lessons.md`, verified video claims in `sources/`, and example comparisons. Avoid treating unreviewed outputs as ground truth.

## Structure
- `SKILL.md`: lightweight router and required workflow.
- `profiles/styles.json`: 14 style definitions; `references/aesthetic-directions.md` explains them.
- `references/`: narrative, content, layouts, data, engineering, accessibility, evidence and anti-slop.
- `workflows/`: create, restyle, and critique execution paths.
- `scripts/`: local style chooser, PPTX static audit, transcript intake, feedback recorder, package validator.
- `memory/`: reviewed learnings read on future invocations.
- `sources/`: provenance, timestamped coverage, and source intake.
- `examples/`: three distinct deck briefs with storyboards.
- `tests/`: test cases for assessing agent responses.

## Requirements
The core skill requires no packages. Optional `.pptx` checker needs `python-pptx` (`pip install python-pptx`). Scripts are Python 3.9+ and operate locally. Check file licenses and permissions before using logos, photos, fonts, or frame captures.
