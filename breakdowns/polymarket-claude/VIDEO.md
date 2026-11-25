---
videomd: 1
name: polymarket-claude
description: 'A phone-filmed walk-through of a trading dashboard on a real laptop, followed by a selfie explanation. Nothing is screen-recorded or animated; the proof is a finger on a real screen. Made with (inferred): live action 100%'
source:
  file: polymarket-claude.mp4
  sha256: 72cc81f31a579ee72cf6247c60f90c6a8569b5adec04d77d47860066c5c9fdb7
  duration: 41.267
  size: 720x1280
  fps: 30.0
  aspect: '9:16'
shots: 11
lang: en
made_mix:
  live_action: 1.0
confidence: 0.73
readers:
- tools
- agent
open_questions: 3
generator:
  name: rea-video
  version: 0.1.0
---

# polymarket-claude.mp4

**Verdict** (inferred): Mixed production: live action 100%; overlays: styled text, text labels, subtitles, title (composited in code / an editor); real material used: live footage (41.3s); audio: voice; packaging: styled text ×2, text labels ×310
**What it says**: A phone-filmed walk-through of a trading dashboard on a real laptop, followed by a selfie explanation. Nothing is screen-recorded or animated; the proof is a finger on a real screen.
**Narrative**: #01-02 grab attention → #03-05 show evidence → #06-09 add information → #10 turn → #11 call to action
**Made with** (inferred, by duration): live action 100%
**Remake**: live action 11 shots → 1 scene, 4 camera setups
**Real material to collect**: 11 shots (100% of the duration), list in `video/remake.md`

## Next steps

- Remake: Capsule Cinema does the generation, assembly and checks. `rea-video remake <this dir>` hands over to it, does what can be done automatically and keeps the original elsewhere; `remake/status.md` says per shot what is left. Add incoming clips to `remake/mine.json` and run it again

## Open questions

- Shot #3 (8.3–11.0s): live action at only 56% confidence, runner-up AI-generated video
- Shot #6 (15.9–18.4s): live action at only 58% confidence, runner-up screen recording / screenshot
- No AI listened to the soundtrack (the review covered the picture only): real voice versus TTS is inferred from the waveform; the effects were found on the separ…

## Map

Read this page first; for detail, open only the file you need. Each line is `path | ~tokens | what is in it · when to read it`; paths are relative to this directory.

```videomd-map
video/timeline.md | 1105 | Timeline: one line per shot · what a stretch says, which shots need review, how a shot was made
video/content.md | 316 | Content and structure · what it says, the narrative line, structure, the script
video/cast.md | 259 | Cast, scenes and props · reference images for characters, first-frame prompts
video/sound.md | 192 | Sound · voice, music, sound effects, beats and sources
video/rhythm.md | 623 | Rhythm and key frames · when cuts and transitions happen, shot lengths, the change curve, key frames of each shot
video/look.md | 1026 | Camera, lighting and editing · for filmed shots: framing, camera, lighting, kit
video/packaging.md | 4002 | Packaging · subtitles, styled text, stickers, picture-in-picture: timing and style
video/remake.md | 1084 | Remake plan · generation units, shoots, code builds, real material to collect, acting and emotion
video/shots/*.md | 749 | Per-shot detail, tokens per file on average · checking one shot: what is seen, the inference and its basis, prompts, frames
breakdown.json | 138549 | Full raw data · for programs; a model rarely needs it
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
