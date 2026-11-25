---
videomd: 1
part: remake
tokens: 6116
---

## Remake plan

### Step by step

This is a talking head. Do the steps in this order; the detail for each is in the matching subsection below. 26% of the time is a motion-graphics explainer; its steps are included.

1. **Write the content**: write yours in the same 17 steps as the original (narrative line under “Content and structure”)
2. **Collect material**: the real material in the picture (live footage) needs the original files, listed under “What to prepare”; one reference image per recurring character to lock appearance across shots: Presenter
3. **Shoot**: phone held vertical, mostly medium shot; light: soft frontal light (flat light) — a large source from the camera side, almost no shadow on the subject: facing a window, a ring light, or a big softbox behind the camera, 18-inch ring light or a diffused LED panel just behind and above the phone; grade: natural (close to the original colours) (setups under “Shoot”)
4. **Motion graphics**: have the agent make an editable first version and change the text and pictures on top of it rather than starting from scratch; the first version is only a start, where it differs from the original is under “Code build”
5. **Voice**: the original is human recording; record it yourself or use TTS; delivery per “Acting and emotion”
6. **Edit**: follow the order and lengths in the shot list; the original has 29 shots at 2.2s each; 2 transitions under “Edit”
7. **Subtitles and styled text**: import `packaging/subtitles.srt` and replace the words; timing and style under “Packaging layer”
8. **Put it together and compare**: hand the shots you made to the agent; it places them on the original timeline, keeps the original where yours are missing, and renders a side-by-side comparison with the original

**live action 22 shots → 1 scene, 2 camera setups; code render / screen capture 7 shots → 1 code project (5 parts)**

### Shooting scenes

Shoot every shot of one scene before moving to the next; within a scene, shoot the wider sizes first and the close-ups last so the lighting is set only once. Leave about 1s of handle at both ends of every take.

**S1**: shots #1, #2, #4–#6, #8, #10, #12–#14, #18–#29 (47.09s on screen); Office lounge: teal modular sofa, round wood coffee table, wood-panelled wall, g, Soft overhead light, cool daylight through glass
- Lighting: soft frontal light (flat light), key light frontal, warm (about 3000–4000K)
- Setup medium shot · fixed camera (tripod / mount / on the desk) · pan / track/static: shots #1, #2, #4, #6, #12, #20–#22, #25, #27, #28, 22.94s on screen, shoot about 44.9s
- Setup medium shot · moving camera (gimbal / handheld pan) · pan / track/pull-out/push-in/static: shots #5, #8, #10, #13, #14, #18, #19, #23, #24, #26, #29, 24.15s on screen, shoot about 46.1s

### Code composition

Have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code as one project, optionally on an HTML video framework such as HyperFrames or Remotion: cuts, transitions and each shot's key frames from "Rhythm and key frames", layout, colours and elements from the scenes below. Text and UI are 100% controllable, changing copy is a data change.

`rea-video code-remake <breakdown folder>` only makes a quick draft: it renders `code/remake.mp4` from each scene's sampled points / cut-out, motion and background glow and scores it. Particles, point clouds and data visualisations on a dark ground come close; an illustrated character's acting and morph transitions do not.

- Part 1: shots #3 (3.8–6.8s)
- Part 2: shots #7 (12.5–16.1s)
- Part 3: shots #9 (18.2–19.8s)
- Part 4: shots #11 (20.2–22.8s)
- Part 5: shots #15–#17 (31.2–37.2s)

Remake assets (all in the report folder; hand them over together with the data below to whoever writes the code, or to an LLM):
- `shots/shot_XXX_first.jpg` / `_last.jpg`: first / last frame of each shot at full size, for layout, type size and margins
- `shots/shot_XXX_strip.jpg`: key frames about every 0.5 s, to follow the animation
- `shots/shot_XXX_elements.jpg` and `_el_NN.jpg` / `_st_NN.jpg` / `_ly_NN.jpg`: full-size crop of every element once settled, numbered as in the motion timeline; redraw shapes from them, cut out icons, logos and illustrations that cannot be redrawn
- `packaging/overlays.ass`, `packaging/timeline.json`: timing, position and colour of the text

How to build the pictures (by the measured picture type):
- vector shapes: SVG shapes + interpolate() / spring() keyframes, positions and timing measured from the frame
- kinetic type: Word-by-word spring() entrances (offset + scale + opacity), highlight boxes on key words; match font, size and leading from the frame
- data chart: SVG / D3 scales for axes and marks, numbers counted up with interpolate(), bars / lines grown with spring()

| Shot | Time | Build | Picture | Camera | Colours | On-screen text |
|---|---|---|---|---|---|---|
| #3 | 3.8–6.8s | vector shapes | Full-frame motion graphic: the camera glides over a dark node canvas to a green clock node labelled Rise and Grind, connectors fanning out to the right. Caption in the lower third. | picture drifts left | ground #3a363c · #4b4a51 #5a5b65 #706c7e · drawn #677073 #827f96 #c1a8b2 #f4f8f8 | Wait2 |
| #7 | 12.5–16.1s | kinetic type | Full-frame workflow canvas: a pink play node and a globe node labelled Play Man in the box, the view sliding along the connector. Caption: SPOTIFY. | static frame, elements move inside it | ground #3a363c · #69666d #525158 #444247 #837f89 · drawn #746f78 #8c8ba1 #c4a4ad #f3f7f7 | — |
| #9 | 18.2–19.8s | data chart | Full-frame white card: a phone message thread, tilted in 3D with soft blur at the edges. A grey bubble from a friend checking in, a blue reply saying Can't talk, grinding. | push in 2%/s, picture drifts up | ground #fdfcff · #e8e8ee #d4d1d8 #a4a2ae · drawn #babdcd #55b6fb #928d9e #5d535a | Greg  / Greg |
| #11 | 20.2–22.8s | vector shapes | Full-frame split graphic: on top a simple map with a red car driving up a grey road toward beer and cigarette icons; below it the workflow node Beer and Cig Farmer on the dark canvas. | static frame, elements move inside it | ground #fefcff · #39373c #4c4b52 #bebcc2 #69666d · drawn #fefcfe #423d42 #716b70 #f7722d | 2 |
| #15 | 31.2–33.2s | data chart | Full-frame workflow canvas pushing in on a Bet365 API node feeding an orange code node labelled Arbitrage Calculator. | push in 3%/s, picture drifts left | ground #3a363c · #4b4a51 #5d5d65 #79727a · drawn #6d6973 #9292ac #ebeff2 #d28583 | — |
| #16 | 33.2–35.7s | kinetic type | Full-frame workflow canvas: a Flex Wins on Socials node with connectors fanning out to several posts, a soft light sweep across the top. | push in 2%/s, picture drifts left | ground #3a373c · #4b494e #605f67 #78747a #978d93 · drawn #777278 #ada2aa #e5e7ec #7a7bc2 | hister Delivery Book All Available Slot / apl.doordash..com...GET:https:/lapi.range |
| #17 | 35.7–37.2s | kinetic type | Full-frame workflow canvas with the six social platform nodes again, wider. Caption: SOCIAL. | pull out 1%/s, picture drifts left | ground #3a363c · #4a4950 #5a5863 #6d6a74 #8e838d · drawn #706d79 #a299a2 #7d7ac3 #e2e6ea | Delivery / BookAll Available Slots / Book All Available Slots / dash.com...GET:https://api.rangebool |

**Picture scenes** (a new scene whenever what is drawn moves or changes shape as a whole inside a shot. `frames/` holds first / middle / last full-size frames per scene, `scene_XX_layer.png` the drawn layer of the middle frame (background and text removed, alpha by how strongly it stands out), `frames/points/scene_XX.json` samples of that layer, one `x y r g b a` per row with x, y in 0–1. Place particles, trace lines or redraw shapes from these instead of guessing from a description. `track` in `frames/scenes.json` follows the layer's centre and spread over time)

| Scene | Shot | Time | Ground | Background glow | Drawn colours | Pieces | Area (x0 y0 x1 y1) | Motion |
|---|---|---|---|---|---|---|---|---|
| scene_01 | #3 | 3.8–6.8s | #3a383b | #6f686d, centre (0.67, 0.60), radius 0.19 | #6a6970 #7a7793 #bfa4b4 | 82 | 0.42 0.07 0.98 0.73 | pans (-1.8%, +0.0%)/s |
| scene_02 | #7 | 12.5–16.1s | #3a383b | #cdcbce, centre (0.13, 0.10), radius 0.20 | #9d90a1 #736e79 #e8edee | 110 | 0.01 0.00 0.96 0.64 | zoom out 2%/s, turns clockwise 0.6°/s |
| scene_03 | #9 | 18.2–19.8s | #ffffff | #e4e2e5, centre (0.43, 0.32), radius 0.29 | #8ca0c8 #c0c5d4 #5f4a52 | 18 | 0.07 0.05 0.78 0.43 | pans (-0.4%, -1.2%)/s |
| scene_04 | #11 | 20.2–22.8s | #bcb8bc | #39373a, centre (0.48, 0.72), radius 0.56 | #fefefe #4e4b4e #ec762b | 79 | 0.04 0.22 0.98 0.60 | turns clockwise 0.5°/s, points wander |
| scene_05 | #15 | 31.2–33.2s | #3a383b | #605e60, centre (0.48, 0.38), radius 0.28 | #67666c #907b92 #aeadc3 | 91 | 0.01 0.05 0.97 0.56 | zoom in 4%/s, pans (-6.6%, +0.1%)/s |
| scene_06 | #16 | 33.2–35.7s | #424043 | #afadb0, centre (0.25, 0.07), radius 0.23 | #8b899b #726b6e #b6acc4 | 101 | 0.02 0.01 0.99 0.71 | zoom in 2%/s, turns anticlockwise 0.7°/s |
| scene_07 | #17 | 35.7–37.2s | #3a383b | #636265, centre (0.39, 0.35), radius 0.27 | #716e79 #a8a2ac #8176c7 | 73 | 0.01 0.02 0.96 0.57 | zoom out 2%/s, pans (-3.2%, -0.1%)/s, points wander |

When built, score it with `rea-video compare original remake --scenes frames/scenes.json -o dir` (each side's drawn layer is taken against its own ground, so a new ground colour still compares) and fix the lowest-scoring scenes first, from `compare_worst.jpg`.

Per-shot motion timeline (measured: positions in % of frame width / height, colours sampled once the element settles; read together with the key-frame strip)

**Motion #3 3.8–6.8s · 3 events**

- Ground #3a363c; other main colours #4b4a51 #5a5b65 #706c7e; drawn layer #677073 #827f96 #c1a8b2 #f4f8f8
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 89%–95%, y 8%–10% · #5d5b63 · [crop](shots/shot_003_st_01.jpg)
- S2. never moves: shape / text block · x 71%–84%, y 9%–16% · #77777e · [crop](shots/shot_003_st_02.jpg)
- S3. never moves: shape / text block · x 84%–96%, y 34%–38% · #5b5c64 · [crop](shots/shot_003_st_03.jpg)
- S4. never moves: shape / text block · x 85%–100%, y 42%–49% · #5f5f66 · text “Beer&Cig / GET:https: / Beer & Cig” · [crop](shots/shot_003_st_04.jpg)
- S5. never moves: shape / text block · x 42%–53%, y 53%–55% · #9d9faa · [crop](shots/shot_003_st_05.jpg)
- S6. never moves: shape / text block · x 88%–100%, y 57%–61% · #5e5f67 · [crop](shots/shot_003_st_06.jpg)
- S7. never moves: shape / text block · x 84%–100%, y 67%–76% · #616168 · [crop](shots/shot_003_st_07.jpg)
- S8. never moves: shape / text block · x 52%–65%, y 71%–75% · #6c6a72 · text “Wait2” · [crop](shots/shot_003_st_08.jpg)
- [crop L1](shots/shot_003_ly_01.jpg) [crop L2](shots/shot_003_ly_02.jpg) · Continuous layer: 18% of the frame moves through the whole shot (x 27%–100%, y 5%–78%), e.g. drifting gradients, particle flow, breathing glow
1. 5.70–6.70s · middle (x 13%–53%, y 54%–69%) · changes, moves downward, ease-in-out · #76757b · text “THISAUTOMATION / ALARM / AT645” · [crop](shots/shot_003_el_01.jpg)
2. 6.04–6.70s · top (x 33%–76%, y 16%–47%) · changes, moves rightward, ease-in · #4d5459 · text “Rise and Grind” · [crop](shots/shot_003_el_02.jpg)
3. 6.50–6.57s · middle right (x 73%–82%, y 60%–66%) · disappears, instant · #b2adb0 · [crop](shots/shot_003_el_03.jpg)

**Motion #7 12.5–16.1s · 2 events**

- Ground #3a363c; other main colours #69666d #525158 #444247 #837f89; drawn layer #746f78 #8c8ba1 #c4a4ad #f3f7f7
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 67%–73%, y 2%–7% · #5b575c · [crop](shots/shot_007_st_01.jpg)
- S2. never moves: shape / text block · x 77%–82%, y 15%–18% · #57585d · [crop](shots/shot_007_st_02.jpg)
- S3. never moves: shape / text block · x 91%–96%, y 20%–22% · #62636b · [crop](shots/shot_007_st_03.jpg)
- S4. never moves: shape / text block · x 0%–10%, y 30%–35% · #6b676b · [crop](shots/shot_007_st_04.jpg)
- S5. never moves: shape / text block · x 9%–14%, y 34%–38% · #5e5a60 · [crop](shots/shot_007_st_05.jpg)
- S6. never moves: shape / text block · x 42%–58%, y 35%–38% · #8d7369 · [crop](shots/shot_007_st_06.jpg)
- S7. never moves: shape / text block · x 18%–22%, y 35%–38% · #7e7d82 · [crop](shots/shot_007_st_07.jpg)
- S8. never moves: shape / text block · x 11%–20%, y 42%–44% · #545459 · text “Wait2” · [crop](shots/shot_007_st_08.jpg)
- [crop L1](shots/shot_007_ly_01.jpg) [crop L2](shots/shot_007_ly_02.jpg) · Continuous layer: 27% of the frame moves through the whole shot (x 0%–100%, y 0%–66%), e.g. drifting gradients, particle flow, breathing glow
1. 16.07–16.14s · middle right (x 67%–89%, y 60%–66%) · appears, instant · #8f8f96 · [crop](shots/shot_007_el_01.jpg)
2. 16.07–16.14s · middle left (x 11%–40%, y 60%–66%) · changes, instant · #938d8c · [crop](shots/shot_007_el_02.jpg)

**Motion #9 18.2–19.8s · 0 events**

- Ground #fdfcff; other main colours #e8e8ee #d4d1d8 #a4a2ae; drawn layer #babdcd #55b6fb #928d9e #5d535a
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- [crop L1](shots/shot_009_ly_01.jpg) [crop L2](shots/shot_009_ly_02.jpg) · Continuous layer: 14% of the frame moves through the whole shot (x 0%–89%, y 4%–68%), e.g. drifting gradients, particle flow, breathing glow

**Motion #11 20.2–22.8s · 5 events**

- Ground #fefcff; other main colours #39373c #4c4b52 #bebcc2 #69666d; drawn layer #fefcfe #423d42 #716b70 #f7722d
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 42%–51%, y 2%–6% · #fffdff · [crop](shots/shot_011_st_01.jpg)
- S2. never moves: shape / text block · x 7%–47%, y 14%–24% · #fffdff · [crop](shots/shot_011_st_02.jpg)
- S3. never moves: shape / text block · x 51%–62%, y 14%–21% · #fff6e9 · [crop](shots/shot_011_st_03.jpg)
- S4. never moves: shape / text block · x 0%–7%, y 16%–21% · #fffdff · [crop](shots/shot_011_st_04.jpg)
- S5. never moves: shape / text block · x 61%–100%, y 51%–68% · #3a363a · [crop](shots/shot_011_st_05.jpg)
- S6. never moves: shape / text block · x 87%–100%, y 64%–68% · #48494e · [crop](shots/shot_011_st_06.jpg)
- S7. never moves: shape / text block · x 0%–100%, y 67%–100% · #3a363a · text “Beer & Cig Farmer / GET: https://api.doordash.com.. / GET: https://api.doordash.com...” · [crop](shots/shot_011_st_07.jpg)
- S8. never moves: shape / text block · x 0%–13%, y 72%–85% · #3a363a · [crop](shots/shot_011_st_08.jpg)
- [crop L1](shots/shot_011_ly_01.jpg) [crop L2](shots/shot_011_ly_02.jpg) · Continuous layer: 27% of the frame moves through the whole shot (x 0%–100%, y 0%–100%), e.g. drifting gradients, particle flow, breathing glow
1. 20.30–21.76s · top (x 0%–84%, y 2%–50%) · changes, unfolds downward (draw-on / grow / wipe), ease-out · #f0eaed · [crop](shots/shot_011_el_01.jpg)
2. 20.63–22.63s · middle right (x 58%–100%, y 20%–50%) · appears, unfolds downward (draw-on / grow / wipe), ease-in-out · #bcbac0 · [crop](shots/shot_011_el_02.jpg)
3. 21.16–22.76s · top (x 4%–100%, y 0%–26%) · changes, moves downward, ease-in · #f1edf1 · [crop](shots/shot_011_el_03.jpg)
4. 21.43–22.43s · top left (x 22%–36%, y 6%–12%) · disappears, unfolds downward (draw-on / grow / wipe), linear · #e5e1e5 · [crop](shots/shot_011_el_04.jpg)
5. 21.63–22.76s · top left (x 0%–36%, y 0%–18%) · changes, moves downward, ease-in-out · #e8e4e8 · [crop](shots/shot_011_el_05.jpg)

**Motion #15 31.2–33.2s · 1 events**

- Ground #3a363c; other main colours #4b4a51 #5d5d65 #79727a; drawn layer #6d6973 #9292ac #ebeff2 #d28583
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 44%–49%, y 11%–14% · #67666e · [crop](shots/shot_015_st_01.jpg)
- S2. never moves: shape / text block · x 78%–84%, y 15%–18% · #63636b · [crop](shots/shot_015_st_02.jpg)
- S3. never moves: shape / text block · x 42%–49%, y 22%–25% · #67676f · text “slack to Casino / ack to Casino” · [crop](shots/shot_015_st_03.jpg)
- S4. never moves: shape / text block · x 77%–84%, y 25%–28% · #64646c · [crop](shots/shot_015_st_04.jpg)
- [crop L1](shots/shot_015_ly_01.jpg) [crop L2](shots/shot_015_ly_02.jpg) · Continuous layer: 24% of the frame moves through the whole shot (x 0%–100%, y 0%–65%), e.g. drifting gradients, particle flow, breathing glow
1. 31.22–33.16s · middle (x 7%–84%, y 22%–57%) · changes, unfolds rightward (draw-on / grow / wipe), linear · #4a494e · text “Black to Casino / https://api.uber.com/v1/r.. / Bet365API” · [crop](shots/shot_015_el_01.jpg)

**Motion #16 33.2–35.7s · 0 events**

- Ground #3a373c; other main colours #4b494e #605f67 #78747a #978d93; drawn layer #777278 #ada2aa #e5e7ec #7a7bc2
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- [crop L1](shots/shot_016_ly_01.jpg) [crop L2](shots/shot_016_ly_02.jpg) · Continuous layer: 42% of the frame moves through the whole shot (x 0%–100%, y 0%–75%), e.g. drifting gradients, particle flow, breathing glow

**Motion #17 35.7–37.2s · 0 events**

- Ground #3a363c; other main colours #4a4950 #5a5863 #6d6a74 #8e838d; drawn layer #706d79 #a299a2 #7d7ac3 #e2e6ea
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 33%–42%, y 0%–2% · #5c5d65 · [crop](shots/shot_017_st_01.jpg)
- S2. never moves: shape / text block · x 62%–67%, y 4%–5% · #5b5c63 · [crop](shots/shot_017_st_02.jpg)
- S3. never moves: shape / text block · x 51%–56%, y 6%–8% · #5b5a60 · [crop](shots/shot_017_st_03.jpg)
- S4. never moves: shape / text block · x 33%–47%, y 8%–14% · #67676e · [crop](shots/shot_017_st_04.jpg)
- S5. never moves: shape / text block · x 0%–8%, y 48%–50% · #59575f · [crop](shots/shot_017_st_05.jpg)
- [crop L1](shots/shot_017_ly_01.jpg) [crop L2](shots/shot_017_ly_02.jpg) · Continuous layer: 30% of the frame moves through the whole shot (x 0%–100%, y 0%–66%), e.g. drifting gradients, particle flow, breathing glow

### Real material in the picture (the original files are needed)

22 shots, 47.09s (74%) contain real material (screen recordings, screenshots, photos, embedded video); a model cannot stand in for them:

- **live footage** (whole frame): shots #1, #2, #4–#6, #8, #10, #12–#14, #18–#29, 47.1s in all

### Acting and emotion

In a prompt, describe the visible expression and movement rather than words like “happy” or “sad”, and keep it smaller rather than bigger (strong emotion words tend to give mask faces and forced smiles); get the expression right in the first frame; for shots with lines, make the voice with its delivery first and let the picture act to it. For generated shots the Face and Movement below are already in the generation-unit prompts.

**all 22 shots**

| Shot | Who | Emotion (strength) | Face | Movement / change | Delivery | How to get it |
|---|---|---|---|---|---|---|
| #1 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #2 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #4 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #5 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #6 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #8 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #10 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #12 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #13 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #14 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #18 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #19 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #20 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #21 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #22 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #23 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #24 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #25 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #26 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #27 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #28 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |
| #29 | A | deadpan (light) | neutral brows, eyes to camera, mouth relaxed between phrases | seated, one hand gesturing at chest height, small head turns | — | actor plays it |

- **actor plays it**: Filmed: hand the face, movement and delivery to the actor as direction, and rehearse the pauses and tone against the original once
