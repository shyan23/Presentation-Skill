# Install `.skill/slide-design-mastery`

Unzip and keep the `.skill` folder.

Project-local Claude Code:

```bash
mkdir -p .claude/skills
cp -r .skill/slide-design-mastery .claude/skills/
```

Project-local Codex/agent skills:

```bash
mkdir -p .agents/skills
cp -r .skill/slide-design-mastery .agents/skills/
```

Reload/restart the agent's skill discovery and use: "Load slide-design-mastery and unslop my presentation, preserving the facts and rendering each slide for QA."

**Source note:** Video title identified, but transcript and creator-specific methods not verified. Add your own authorized transcript and run `scripts/import_transcript.py` for deeper evidence-based learning.
