---
videomd: 1
name: tuesday-simulator
description: 'A deadpan walkthrough of an absurd automation that runs a man''s whole day, told as a fast list where every item gets its own diagram or fake screenshot. Made with (inferred): live action 74%, code / template render 26%'
source:
  file: tuesday-simulator.mp4
  sha256: b84f0eeff092fd15a9f9f3d885ee31b37bfcb18b3744ca60879fae9c437ed01b
  duration: 63.856
  size: 1080x1920
  fps: 23.976
  aspect: '9:16'
shots: 29
lang: en
made_mix:
  live_action: 0.7374
  code_render: 0.2626
confidence: 0.756
readers:
- tools
- agent
- human
open_questions: 16
generator:
  name: rea-video
  version: 0.1.0
---

# tuesday-simulator.mp4

**Verdict** (inferred): Mixed production: live action 74% + code / template render 26%; overlays: styled text, text labels, static graphics, static sticker, subtitles, title (composited in code / an editor); real material used: live footage (47.1s); audio: voice; packaging: 34 subtitle lines, styled text ×2, text labels ×143, stickers / GIFs ×6
**What it says**: A deadpan walkthrough of an absurd automation that runs a man's whole day, told as a fast list where every item gets its own diagram or fake screenshot.
**Narrative**: #01-02 grab attention → #03 set the scene → #04 add information → #05 show evidence → #06 turn → #07-08 add information → #09 show evidence → #10 turn → #11 show evidence → #12-17 add information → #18 turn → #19 add information → #20-21 show evidence → #22-26 add information → #27 turn → #28 add information → #29 call to action
**Made with** (inferred, by duration): live action 74%, code / template render 26%
**Remake**: live action 22 shots → 1 scene, 2 camera setups; code render / screen capture 7 shots → 1 code project (5 parts)
**Real material to collect**: 22 shots (74% of the duration), list in `video/remake.md`

## Next steps

- Remake: Capsule Cinema does the generation, assembly and checks. `rea-video remake <this dir>` hands over to it, does what can be done automatically and keeps the original elsewhere; `remake/status.md` says per shot what is left. Add incoming clips to `remake/mine.json` and run it again
- Code-rendered shots are best rebuilt in code by a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series), optionally on HyperFrames or Remotion, from the rhythm and key frames in `video/rhythm.md`; `rea-video code-remake <this dir>` only makes a quick draft for particles / data-visualisation pictures

## Open questions

- Shot #1 (0.0–2.5s): live action at only 59% confidence, runner-up AI-generated video
- Shot #2 (2.5–3.8s): live action at only 53% confidence, runner-up AI-generated video
- Shot #3 (3.8–6.8s): code / template render at only 52% confidence, runner-up still image + pan/zoom
- Shot #5 (8.3–10.3s): live action at only 44% confidence, runner-up screen recording / screenshot
- Shot #6 (10.3–12.5s): live action at only 59% confidence, runner-up AI-generated video
- Shot #7 (12.5–16.1s): code / template render at only 56% confidence, runner-up still image + pan/zoom
- Shot #8 (16.1–18.2s): live action at only 50% confidence, runner-up AI-generated video
- Shot #12 (22.8–26.2s): live action at only 59% confidence, runner-up AI-generated video
- 8 more, see the `flag` lines in `video/timeline.md`

## Map

Read this page first; for detail, open only the file you need. Each line is `path | ~tokens | what is in it · when to read it`; paths are relative to this directory.

```videomd-map
video/timeline.md | 2912 | Timeline: one line per shot · what a stretch says, which shots need review, how a shot was made
video/content.md | 638 | Content and structure · what it says, the narrative line, structure, the script
video/cast.md | 332 | Cast, scenes and props · reference images for characters, first-frame prompts
video/sound.md | 191 | Sound · voice, music, sound effects, beats and sources
video/rhythm.md | 1519 | Rhythm and key frames · when cuts and transitions happen, shot lengths, the change curve, key frames of each shot
video/look.md | 1067 | Camera, lighting and editing · for filmed shots: framing, camera, lighting, kit
video/packaging.md | 4612 | Packaging · subtitles, styled text, stickers, picture-in-picture: timing and style
video/remake.md | 6128 | Remake plan · generation units, shoots, code builds, real material to collect, acting and emotion
video/shots/*.md | 739 | Per-shot detail, tokens per file on average · checking one shot: what is seen, the inference and its basis, prompts, frames
breakdown.json | 208459 | Full raw data · for programs; a model rarely needs it
shots/ | - | contact sheet, first and last frame of each shot · checking by eye
storyboard.jpg | - | storyboard of the whole video · the whole video at a glance
stems/ | - | voice, music and effects stems · listening, remaking the sound
packaging/ | - | subtitle files, packaging timeline, sticker frames · remaking subtitles and packaging
frames/ | - | picture scenes: full-size frames, the drawn layer cut out and sampled, measurements · remaking rendered pictures
audio.png | - | waveform and beat chart · seeing the rhythm
```

## How to read

- One shot per line: `#<n> start-end (s) | key value | …`. A key ending in `~` is the tools' inference; keys without it are visible on screen or measured directly.
- `story` job in the story and the point · `seen` what is on screen · `act` acting (emotion, strength, face) · `camera` camera move · `overlay` overlays · `made~` how it was made (inferred) · `material~` where the material came from (inferred) · `remake` remake route · `flag` needs a second look
- Full detail for a shot is in `video/shots/<n>.md` (e.g. `video/shots/07.md`).
- What is “seen” can be checked against the frames; what is “inferred” is the tools' and image readers' judgement, with the basis in each shot file. When they disagree, trust the frames.
