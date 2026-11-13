# Learn from the referenced video and future credible sources

## Current provenance status
Video: https://www.youtube.com/watch?v=fkxw0SrwVkA
Observed title: "How to Unslop Your AI-Generated Slides". Video transcript and speaker metadata could not be reliably retrieved during skill creation. Therefore no statements in this pack are presented as direct quotes or unique methods of that creator.

## Upgrade the skill to faithfully learn from that person
1. Obtain a transcript via YouTube's "Show transcript" or from a user-authorized transcription of video audio. Preserve transcript language and timecodes if available.
2. Save plain text or VTT locally. Run `python scripts/import_transcript.py path/to/transcript.vtt` (optional `--creator "NAME"`). The script writes timestamped chunks to `sources/` and a provenance manifest; it does **not** invent insights or call AI models.
3. Read chunks one by one and use `sources/CLAIM_TEMPLATE.md` to capture explicit principles, exact examples, counterexamples, constraints, and confidence, each with timecodes.
4. Separate **descriptive** (what is visually done at 02:15) from **prescriptive** (what speaker explicitly recommends). Frame interpretations as your own, not the speaker's.
5. Where examples or before/afters are visible, take authorized reference screenshots and log timecode plus exact feature (grid, typography, image crop, etc). Distinguish user-uploaded images from generated reconstructions.
6. Add source-confirmed patterns to relevant `references` only after validation. Use bounded direct quotations, citing original video, and avoid storing full copyrighted transcript as distributed data unless authorized.
7. Create at least 3 transfer tests: apply the principle to corporate, academic, and creative slides; record when it breaks.

## Observation format
`claim_id | video timecode | observed element | speaker explicitly states? | generalized principle | evidence confidence | transfer test | exceptions`.

## How to avoid overfitting one designer
A creator's aesthetic choices are context-bound. Learn decision heuristics and constraints, not just favorite fonts/colors/one demo deck. Apply comparative exercises and value cognitive clarity over surface resemblance. Remember: recreating a person's personal identity or reproducing copyrighted slides is not the objective.
