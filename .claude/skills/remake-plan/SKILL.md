---
name: remake-plan
description: Turn a video breakdown into a plan for the user's own version of that video: a shot list with their topic, what to film, what to record on screen, what to build as graphics, and a script outline that keeps the original's structure. Use when the user says "help me make my own version", "remake this for my product" or "plan a video like this one".
---

# Plan your own version of a video

The breakdown tells you how the original was built. The user's video keeps the structure and the craft and
replaces everything else: topic, words, face, footage, brand.

## 1. Ask two things, once

1. What is your video about (product, idea or story, in a sentence)?
2. What can you make: film yourself, record your screen, generate with AI, or all three?

If they already said, do not ask again.

## 2. Read the breakdown

Open `runs/<name>/VIDEO.md`, then only: `video/timeline.md` (one line per shot), `video/content.md` (structure),
`video/remake.md` (what the engine says each shot needs), and `video/packaging.md` for the text style.

## 3. Write `runs/<name>/remake/PLAN.md`

Use this layout:

```markdown
# Plan: <their topic>, built like <reference name>

## The idea in one line
## Structure (kept from the reference)
| Beat | Time in reference | Job of the beat | Your version |
## Shot list
| # | Length | What the reference shows | What you show | How you make it | Text on screen |
## What to collect before editing
- To film: ...
- To record on screen: ...
- To build as graphics: ...
- Sound: ...
## Script outline
## Edit settings to copy
## Check before you post
```

Rules for writing it:

- **One row per shot of the reference**, same order, same lengths within about 20%. Merge shots only when the user
  cannot make that many.
- **"How you make it" is one of**: film (give framing and light from `video/look.md`), screen recording (say which
  screen and what happens on it), graphic (say what it shows and how it moves), AI-generated (say what to prompt and
  with which reference frame). Match it to what they said they can make.
- **Script outline, not a script**: one line per beat saying what to say and how long. Never reuse the reference's
  sentences. If they want a full script, write a new one for their topic in their own voice.
- **Edit settings** come from the measured facts: cut rate, caption style and timing, sound effects, music. Run
  `python3 breakdown_machine/skillgen.py facts runs/<name>` and copy from that table.
- If an editing skill already exists for this video (`runs/<name>/skill/SKILL.md`), point to it instead of
  repeating the settings.

## 4. Stay on the right side

- Their own footage, voice, music and brand. No footage, music, logos or likeness from the reference.
- If the reference is an ad for a competitor, the plan may copy its structure, never its claims.
- Follow the platform's AI labelling rules for anything generated.
