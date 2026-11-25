---
videomd: 1
name: marketplace-bot
description: 'A deadpan explainer of a bot that lowballs marketplace sellers at scale, where every step is a node of one workflow diagram and every joke lands as a real-looking chat. Made with (inferred): live action 52%, code / template render 45%, screen recording / screenshot 4%'
source:
  file: marketplace-bot.mp4
  sha256: 39f17f03f0d114d1922a37df39d77e85d85e7184e73eb7835005e4fcad3af3f5
  duration: 52.416
  size: 720x1280
  fps: 24.0
  aspect: '9:16'
shots: 27
lang: en
made_mix:
  live_action: 0.5159
  code_render: 0.4459
  screen_capture: 0.0382
confidence: 0.638
readers:
- tools
- agent
- human
open_questions: 17
generator:
  name: rea-video
  version: 0.1.0
---

# marketplace-bot.mp4

**Verdict** (inferred): Mixed production: live action 52% + code / template render 45% + screen recording / screenshot 4%; overlays: animated sticker / GIF, text labels, static graphics, static sticker, subtitles, title (composited in code / an editor); real material used: live footage (27.0s), screen recording (12.8s), UI screenshot (7.1s); audio: voice; packaging: 7 subtitle lines, text labels ×57, stickers / GIFs ×4
**What it says**: A deadpan explainer of a bot that lowballs marketplace sellers at scale, where every step is a node of one workflow diagram and every joke lands as a real-looking chat.
**Narrative**: #01-04 grab attention → #05-07 set the scene → #08-14 add information → #15 turn → #16-17 show evidence → #18 turn → #19 show evidence → #20-21 add information → #22 show evidence → #23 turn → #24-26 add information → #27 call to action
**Made with** (inferred, by duration): live action 52%, code / template render 45%, screen recording / screenshot 4%
**Remake**: live action 14 shots → 1 scene, 3 camera setups; code render / screen capture 13 shots → 1 code project (10 parts)
**Real material to collect**: 21 shots (76% of the duration), list in `video/remake.md`

## Next steps

- Remake: Capsule Cinema does the generation, assembly and checks. `rea-video remake <this dir>` hands over to it, does what can be done automatically and keeps the original elsewhere; `remake/status.md` says per shot what is left. Add incoming clips to `remake/mine.json` and run it again
- Code-rendered shots are best rebuilt in code by a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series), optionally on HyperFrames or Remotion, from the rhythm and key frames in `video/rhythm.md`; `rea-video code-remake <this dir>` only makes a quick draft for particles / data-visualisation pictures

## Open questions

- Shot #1 (0.0–1.7s): live action at only 51% confidence, runner-up AI-generated video
- Shot #3 (2.5–2.9s): photo / image: real material or generated, to confirm
- Shot #5 (3.7–4.2s): live action at only 60% confidence, runner-up AI-generated video
- Shot #7 (5.2–6.5s): live action at only 51% confidence, runner-up AI-generated video
- Shot #8 (6.5–8.6s): code / template render at only 55% confidence, runner-up still image + pan/zoom
- Shot #9 (8.6–10.5s): live action at only 51% confidence, runner-up AI-generated video
- Shot #10 (10.5–12.3s): code / template render at only 55% confidence, runner-up still image + pan/zoom
- Shot #11 (12.3–15.5s): live action at only 51% confidence, runner-up AI-generated video
- 9 more, see the `flag` lines in `video/timeline.md`

## Map

Read this page first; for detail, open only the file you need. Each line is `path | ~tokens | what is in it · when to read it`; paths are relative to this directory.

```videomd-map
video/timeline.md | 2561 | Timeline: one line per shot · what a stretch says, which shots need review, how a shot was made
video/content.md | 522 | Content and structure · what it says, the narrative line, structure, the script
video/cast.md | 327 | Cast, scenes and props · reference images for characters, first-frame prompts
video/sound.md | 191 | Sound · voice, music, sound effects, beats and sources
video/rhythm.md | 1204 | Rhythm and key frames · when cuts and transitions happen, shot lengths, the change curve, key frames of each shot
video/look.md | 1100 | Camera, lighting and editing · for filmed shots: framing, camera, lighting, kit
video/packaging.md | 2478 | Packaging · subtitles, styled text, stickers, picture-in-picture: timing and style
video/remake.md | 10446 | Remake plan · generation units, shoots, code builds, real material to collect, acting and emotion
video/shots/*.md | 691 | Per-shot detail, tokens per file on average · checking one shot: what is seen, the inference and its basis, prompts, frames
breakdown.json | 196702 | Full raw data · for programs; a model rarely needs it
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
