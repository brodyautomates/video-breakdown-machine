---
name: video-to-skill
description: Turn a finished video breakdown (a folder with VIDEO.md) into an editing skill that an AI can follow to cut new footage the same way, with camera motion, cut rhythm, captions and sound as numbers. Use when the user says "turn this into an editing skill", "make a skill from this video" or "copy this edit".
---

# Turn a breakdown into an editing skill

A breakdown describes one video. A skill tells an editor, human or AI, how to build the next one. Your job is the
translation: from "shot 4 pans 14 px per second" to "inside each shot, drift 10 to 18 px per second".

## 1. Start from the measured facts

```bash
python3 breakdown_machine/skillgen.py scaffold runs/<name>
```

This writes `runs/<name>/skill/SKILL.md` with the facts table already filled from the engine's measurements and one
marked block per section for you to write. Never retype a number from memory: copy it from the facts table or from
the file the block names.

## 2. Fill each section

Each `<!-- FILL: ... -->` block says what to write and which file to read. Open only those files:

| Section | Read |
|---|---|
| Shoot and lighting, Framing, Grade | `video/look.md`, frames in `shots/` |
| Camera motion | `video/look.md`, `video/rhythm.md`, the per-shot files in `video/shots/` |
| Cut rhythm | `video/rhythm.md`, `video/timeline.md` |
| Story beats | `video/content.md` |
| Captions and on-screen text | `video/packaging.md` |
| Sound | `video/sound.md` |

How to write them:

- **Turn observations into ranges.** One video gives one sample. Write the measured value, then the range you would
  accept on a new video ("median 3.3%, keep it between 2% and 6%").
- **Tag every value**: **measured** (the engine computed it), **seen** (you can see it in a frame), **inferred**
  (your reading). An editor trusts these differently.
- **Camera motion gets the most care.** For each kind of movement give: what moves, how far (pixels or percent of
  frame), how long, the easing, when it happens (at a cut, inside a shot, on a word) and how to reproduce it on
  footage that was not shot that way (scale and position keyframes).
- **The first 3 seconds get their own beat-by-beat list** inside Cut rhythm: what is on screen at 0.0 s, when the
  first cut, caption and sound land.
- **Story beats are jobs, not lines.** "0 to 3 s: a claim with a number" is reusable. Their sentence is not, and
  copying a script is not what this is for.
- **Procedure** is numbered, in build order, and each step points at the numbers it uses.
- **QA checks** are measurable on a render: cut rate within a range, captions per minute, first cut before a time.
- Remove the FILL comment when a section is done. If the breakdown has nothing for a section (no filmed shots, so no
  lighting), say that in one line and say what replaces it.

## 3. Check it

```bash
python3 breakdown_machine/skillgen.py lint runs/<name>/skill/SKILL.md
```

Fix everything it lists and run it again until it passes. Then read the skill once as the editor who will use it:
could you cut a new video from this page alone? If a step needs a number that is not there, add it.

## 4. Hand it over

Tell the user where the file is and how to use it:

- In this project: copy the folder to `.claude/skills/<skill-name>/SKILL.md` and Claude Code will use it when they
  ask for an edit in that style.
- Anywhere else: any AI that reads Markdown can follow it.

Say what the skill cannot promise: it is built from one video. Three to five breakdowns of videos in the same
style (`breakdown_machine/compare.py`) show which numbers are the pattern and which are one editor's taste.
