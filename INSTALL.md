# Install `skill/slide-design-mastery`

Clone the repo and run these from its root (see README.md for global install).

Project-local Claude Code:

```bash
mkdir -p .claude/skills
cp -r skill/slide-design-mastery .claude/skills/
```

Project-local Codex/agent skills:

```bash
mkdir -p .agents/skills
cp -r skill/slide-design-mastery .agents/skills/
```

Reload/restart the agent's skill discovery and use: "Load slide-design-mastery and unslop my presentation, preserving the facts and rendering each slide for QA."

**Source note:** Inspired by "How to Unslop Your AI-Generated Slides" by Analyst Academy (https://www.youtube.com/watch?v=fkxw0SrwVkA). Transcript not used; add your own authorized transcript and run `scripts/import_transcript.py` for evidence-based learning.
