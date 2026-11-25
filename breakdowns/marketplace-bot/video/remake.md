---
videomd: 1
part: remake
tokens: 10434
---

## Remake plan

### Step by step

This is a talking head. Do the steps in this order; the detail for each is in the matching subsection below. 45% of the time is a motion-graphics explainer; its steps are included.

1. **Write the content**: write yours in the same 12 steps as the original (narrative line under “Content and structure”)
2. **Collect material**: the real material in the picture (live footage, UI screenshot, screen recording) needs the original files, listed under “What to prepare”; one reference image per recurring character to lock appearance across shots: Presenter
3. **Shoot**: phone held vertical, mostly medium shot; light: night / low-light ambient, no dedicated fill — the key is whatever is there (street lamps, signs, ceiling lights, screens), phone night / portrait mode; use a street lamp or sign as the key, subject just off-axis below it; grade: natural (close to the original colours) (setups under “Shoot”)
4. **Motion graphics**: have the agent make an editable first version and change the text and pictures on top of it rather than starting from scratch; the first version is only a start, where it differs from the original is under “Code build”
5. **Voice**: the original is human recording; record it yourself or use TTS; delivery per “Acting and emotion”
6. **Edit**: follow the order and lengths in the shot list; the original has 27 shots at 1.9s each; 4 transitions under “Edit”
7. **Subtitles and styled text**: import `packaging/subtitles.srt` and replace the words; timing and style under “Packaging layer”
8. **Put it together and compare**: hand the shots you made to the agent; it places them on the original timeline, keeps the original where yours are missing, and renders a side-by-side comparison with the original

**live action 14 shots → 1 scene, 3 camera setups; code render / screen capture 13 shots → 1 code project (10 parts)**

### Shooting scenes

Shoot every shot of one scene before moving to the next; within a scene, shoot the wider sizes first and the close-ups last so the lighting is set only once. Leave about 1s of handle at both ends of every take.

**S1**: shots #1, #5–#7, #9, #11, #13, #15, #18, #20, #21, #23, #25, #27 (27.04s on screen); Desk in a dark room, mesh chair, white desk, vertical teal LED tube behind, Low key with a teal accent
- Lighting: night / low-light ambient, no dedicated fill, key light frontal, cool (daylight / cool-white LED)
- Setup medium shot · moving camera (gimbal / handheld pan) · pan / track/pull-out/push-in/static: shots #1, #6, #7, #9, #11, #13, #18, #20, #21, #23, #25, #27, 24.92s on screen, shoot about 48.9s
- Setup medium shot · fixed camera (tripod / mount / on the desk) · static: shots #15, 1.54s on screen, shoot about 3.5s
- Setup medium close-up · moving camera (gimbal / handheld pan) · push-in: shots #5, 0.58s on screen, shoot about 2.6s

### Code composition

Have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code as one project, optionally on an HTML video framework such as HyperFrames or Remotion: cuts, transitions and each shot's key frames from "Rhythm and key frames", layout, colours and elements from the scenes below. Text and UI are 100% controllable, changing copy is a data change.

`rea-video code-remake <breakdown folder>` only makes a quick draft: it renders `code/remake.mp4` from each scene's sampled points / cut-out, motion and background glow and scores it. Particles, point clouds and data visualisations on a dark ground come close; an illustrated character's acting and morph transitions do not.

- Part 1: shots #2–#4 (1.7–3.7s); #2–#4 use real screen recordings
- Part 2: shots #8 (6.5–8.6s)
- Part 3: shots #10 (10.5–12.3s)
- Part 4: shots #12 (15.5–17.5s)
- Part 5: shots #14 (19.5–21.2s)
- Part 6: shots #16, #17 (22.8–26.3s)
- Part 7: shots #19 (26.8–30.7s)
- Part 8: shots #22 (33.0–36.5s)
- Part 9: shots #24 (37.0–38.2s)
- Part 10: shots #26 (39.6–43.2s)

Remake assets (all in the report folder; hand them over together with the data below to whoever writes the code, or to an LLM):
- `shots/shot_XXX_first.jpg` / `_last.jpg`: first / last frame of each shot at full size, for layout, type size and margins
- `shots/shot_XXX_strip.jpg`: key frames about every 0.5 s, to follow the animation
- `shots/shot_XXX_elements.jpg` and `_el_NN.jpg` / `_st_NN.jpg` / `_ly_NN.jpg`: full-size crop of every element once settled, numbered as in the motion timeline; redraw shapes from them, cut out icons, logos and illustrations that cannot be redrawn
- `packaging/overlays.ass`, `packaging/timeline.json`: timing, position and colour of the text

How to build the pictures (by the measured picture type):
- data chart: SVG / D3 scales for axes and marks, numbers counted up with interpolate(), bars / lines grown with spring()
- vector shapes: SVG shapes + interpolate() / spring() keyframes, positions and timing measured from the frame
- kinetic type: Word-by-word spring() entrances (offset + scale + opacity), highlight boxes on key words; match font, size and leading from the frame

| Shot | Time | Build | Picture | Camera | Colours | On-screen text |
|---|---|---|---|---|---|---|
| #2 | 1.7–2.5s | data chart | Full-frame grey card with a phone screen: a marketplace listing for a used car, the message box filling in and the keyboard up. | push in 1%/s | ground #46444a · #faf7fc #0a0912 #d1ced8 #343039 · drawn #fdf9fe #0e0a13 #d1ced7 #9f9faa | — |
| #3 | 2.5–2.9s | data chart | Same card: a grid of marketplace car listings, very short. | push in 1%/s | white | $200.PerformanceF...$3,200$6,000·2003... |
| #4 | 2.9–3.7s | data chart | Same card: another car listing with the message box prefilled. | push in 1%/s | ground #49464a · #f9f6fb #cfcbd4 #3c393e #7b7371 · drawn #fdf8fd #cec8cf #201a25 #ada7b2 | Listed aboutamonth ago.PinellasPark,FL |
| #8 | 6.5–8.6s | vector shapes | Full-frame workflow canvas: a Start node, a Facebook Marketplace scraper node and the next node, the view sliding right. Caption: START. | picture drifts left | ground #38363c · #484b52 #5f5d65 #717176 · drawn #6d6c6f #7d8b9e #f7fafd #b9bdc9 | f |
| #10 | 10.5–12.3s | vector shapes | Full-frame workflow canvas: Data Normalizer, Item filter and Lowball Algorithm nodes. Caption: ITEM. | static frame, elements move inside it | ground #38363c · #484a50 #5c5b62 #6f6f75 #8b8b94 · drawn #6e7175 #8d9599 #dfe1e9 #bc7a45 | — |
| #12 | 15.5–17.5s | vector shapes | Full-frame workflow canvas pushing toward the Lowball Algorithm node. Caption: LOWBALL. | picture drifts left | ground #38363c · #484a50 #5e5c62 #6e6f76 · drawn #707478 #a4a4af #f4f7fb #bb7b44 | — |
| #14 | 19.5–21.2s | vector shapes | Full-frame workflow canvas: Lowball Algorithm, Flaw Detection and Message Blaster nodes fanning out. Caption: THEN. | picture drifts left | ground #38363c · #4b4b53 #616068 #787984 #979bae · drawn #6c7478 #9498a8 #e6eaf2 | Deal Analyzer |
| #16 | 22.8–24.4s | data chart | Top: a marketplace listing for a pickup truck. Bottom: the workflow canvas around the Message Blaster node. | static | ground #3a373e · #faf9fd #4b4c56 #7f839c #d1d3dd · drawn #bac2d9 #fdf9fe #888a9a #141b37 | Listedaboutaminuteago.WestKelowna,BC |
| #17 | 24.4–26.3s | data chart | Top: a chat with the seller where lowball messages are being typed. Bottom: the same workflow nodes. | static | ground #fbfafe · #38363c #4a4b52 #68676e #1a73fa · drawn #3f3d43 #1d70f9 #faf8fd #8093ac | Deal Analyzer / Reportseller / Connell Bartel / ConnellBartel / YounamedthegroupBrody·2007DodgeRam1500QuadCab. / Youchanged thegroupphoto. |
| #19 | 26.8–30.7s | data chart | Top: the chat continues, the seller replying in annoyance. Bottom: the Relentless Negotiation Engine node. | static | ground #fbfafe · #38363c #4b4a51 #0a73fb #66666f · drawn #fbf9fe #3b373b #2070f7 | BEST / Quad Cab / Marketplacechatsandyourprivacy / Yep enginebayisfucked / Yepenginebayisfucked / Pretty clapped I'll take it for 1200 |
| #22 | 33.0–36.5s | kinetic type | Top: a long chat where the bot keeps messaging after being told to stop. Bottom: the Follow-up Nuke node. | pull out 2%/s | ground #fcfbff · #38363c #4c4b52 #0371fc #6b6d76 · drawn #3c383c #1d70fc #fdfaff #4c82d1 | Sent / Screwoff / 1310 / Hey you there? / Hey / Have it ready tonight |
| #24 | 37.0–38.2s | vector shapes | Full-frame workflow canvas: Opportunity Recalculator and CRM Integration nodes. Caption: PUT ALL THE LEADS | picture drifts left | ground #38363c · #474951 #676770 #56565f #8a8282 · drawn #717073 #a2a2ae #f1f5fa | Opportunity Recalculator |
| #26 | 39.6–43.2s | vector shapes | Full-frame workflow canvas: Value Calculator and deal nodes with a CRM node, the view drifting down. | push in 5%/s, picture drifts left | ground #38363c · #484a51 #6e717b #5d5c63 #818d9b · drawn #716e75 #9b969b #eaeff5 #4aa6d7 | — |

**Picture scenes** (a new scene whenever what is drawn moves or changes shape as a whole inside a shot. `frames/` holds first / middle / last full-size frames per scene, `scene_XX_layer.png` the drawn layer of the middle frame (background and text removed, alpha by how strongly it stands out), `frames/points/scene_XX.json` samples of that layer, one `x y r g b a` per row with x, y in 0–1. Place particles, trace lines or redraw shapes from these instead of guessing from a description. `track` in `frames/scenes.json` follows the layer's centre and spread over time)

| Scene | Shot | Time | Ground | Background glow | Drawn colours | Pieces | Area (x0 y0 x1 y1) | Motion |
|---|---|---|---|---|---|---|---|---|
| scene_01 | #8 | 6.5–8.6s | #3a383b | #61656a, centre (0.45, 0.63), radius 0.19 | #737675 #abacb4 #337ce2 | 15 | 0.03 0.41 0.99 0.65 | pans (-1.1%, +0.0%)/s |
| scene_02 | #10 | 10.5–12.3s | #3a383b | #696d72, centre (0.54, 0.65), radius 0.27 | #727678 #98a9a6 #b67a47 | 22 | 0.01 0.33 0.99 0.89 | pans (-1.0%, +0.0%)/s |
| scene_03 | #12 | 15.5–17.5s | #3a383b | #666a6f, centre (0.59, 0.62), radius 0.19 | #756f6b #909991 #dde0e6 | 11 | 0.02 0.22 0.99 0.67 | pans (-1.4%, +0.0%)/s |
| scene_04 | #14 | 19.5–21.2s | #3a383b | #57595e, centre (0.54, 0.41), radius 0.43 | #6e7676 #9da2b1 | 47 | 0.02 0.13 0.98 0.65 | pans (-1.3%, +0.0%)/s |
| scene_05 | #16 | 22.8–24.4s | #4c4f56 | #f7f7fb, centre (0.51, 0.39), radius 0.40 | #949db1 #dde0e8 #151c32 | 458 | 0.01 0.01 0.98 0.88 | near still |
| scene_06 | #17 | 24.4–26.3s | #f3f6fb | #39373a, centre (0.51, 0.77), radius 0.52 | #3e3e41 #2470ee #8894a7 | 244 | 0.03 0.05 0.97 0.74 | pans (-0.0%, +1.1%)/s |
| scene_07 | #19 | 26.8–28.6s | #f1fcfd | #39373a, centre (0.51, 0.72), radius 0.54 | #3a373a #2470f1 | 89 | 0.04 0.05 0.97 0.58 | pans (-0.1%, -1.5%)/s |
| scene_08 | #19 | 28.6–30.7s | #5073f8 | #fcfafe, centre (0.46, 0.24), radius 0.52 | #f9f9fd #39373a | 166 | 0.05 0.11 0.99 0.56 | morphs in from the last scene, pans (-0.0%, -12.6%)/s |
| scene_09 | #22 | 33.0–34.5s | #8883e3 | #fefcff, centre (0.46, 0.47), radius 0.69 | #fdfcff #39373a | 191 | 0.03 0.03 0.99 0.60 | pans (+0.0%, -2.6%)/s |
| scene_10 | #22 | 34.5–36.5s | #f5fbfd | #39373a, centre (0.53, 0.75), radius 0.53 | #2471f5 #39373a #4079d1 | 205 | 0.02 0.01 0.97 0.87 | morphs in from the last scene, pans (-0.2%, -1.9%)/s |
| scene_11 | #24 | 37.0–38.2s | #3a383b | #5c6065, centre (0.34, 0.39), radius 0.32 | #737273 #a9acb9 #3c8fd3 | 31 | 0.01 0.04 0.99 0.57 | pans (-1.4%, -0.0%)/s |
| scene_12 | #26 | 39.6–43.2s | #3a383b | #61656a, centre (0.42, 0.73), radius 0.23 | #6a696e #888688 #95b9cd | 37 | 0.00 0.31 0.91 0.97 | zoom in 6%/s, pans (-8.2%, +0.4%)/s |

When built, score it with `rea-video compare original remake --scenes frames/scenes.json -o dir` (each side's drawn layer is taken against its own ground, so a new ground colour still compares) and fix the lowest-scoring scenes first, from `compare_worst.jpg`.

Per-shot motion timeline (measured: positions in % of frame width / height, colours sampled once the element settles; read together with the key-frame strip)

**Motion #2 1.7–2.5s · 2 events**

- Ground #46444a; other main colours #faf7fc #0a0912 #d1ced8 #343039; drawn layer #fdf9fe #0e0a13 #d1ced7 #9f9faa
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: horizontal line · x 13%–89%, y 10%–12% · #fefaff · [crop](shots/shot_002_st_01.jpg)
- S2. never moves: shape / text block · x 8%–93%, y 14%–58% · #fffbff · text “4of13 / 2003 Dodge srt 4.Custom / $2,500” · [crop](shots/shot_002_st_02.jpg)
- Continuous layer: 1% of the frame moves through the whole shot (x 13%–89%, y 12%–91%), e.g. drifting gradients, particle flow, breathing glow
1. 2.20–2.40s · middle (x 56%–64%, y 61%–71%) · appears, ease-in-out · #efebf2 · [crop](shots/shot_002_el_01.jpg)
2. 2.40–2.47s · middle (x 16%–56%, y 50%–52%) · changes, instant · #bab9bb · text “Send selleramessage” · [crop](shots/shot_002_el_02.jpg)

**Motion #3 2.5–2.9s · 0 events**

- No element motion measured (still picture or only slight changes)

**Motion #4 2.9–3.7s · 0 events**

- Ground #49464a; other main colours #f9f6fb #cfcbd4 #3c393e #7b7371; drawn layer #fdf8fd #cec8cf #201a25 #ada7b2
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: horizontal line · x 11%–33%, y 10%–11% · #fefaff · [crop](shots/shot_004_st_01.jpg)
- S2. never moves: horizontal line · x 36%–73%, y 10%–11% · #fefaff · [crop](shots/shot_004_st_02.jpg)
- S3. never moves: shape / text block · x 78%–82%, y 30%–32% · #1b171e · [crop](shots/shot_004_st_03.jpg)

**Motion #8 6.5–8.6s · 0 events**

- Ground #38363c; other main colours #484b52 #5f5d65 #717176; drawn layer #6d6c6f #7d8b9e #f7fafd #b9bdc9
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 9%–20%, y 40%–42% · #727279 · [crop](shots/shot_008_st_01.jpg)
- S2. never moves: shape / text block · x 44%–56%, y 42%–43% · #929099 · [crop](shots/shot_008_st_02.jpg)
- S3. never moves: shape / text block · x 71%–80%, y 42%–44% · #77757c · [crop](shots/shot_008_st_03.jpg)
- S4. never moves: shape / text block · x 92%–100%, y 43%–45% · #68666d · [crop](shots/shot_008_st_04.jpg)
- S5. never moves: shape / text block · x 29%–38%, y 47%–48% · #908e97 · [crop](shots/shot_008_st_05.jpg)
- S6. never moves: shape / text block · x 73%–84%, y 50%–53% · #6e6b72 · text “Data Normalizer” · [crop](shots/shot_008_st_06.jpg)
- S7. never moves: shape / text block · x 11%–24%, y 52%–54% · #7b7981 · text “Start” · [crop](shots/shot_008_st_07.jpg)
- S8. never moves: shape / text block · x 49%–60%, y 52%–53% · #8d8a98 · text “FB Marketplace scraper” · [crop](shots/shot_008_st_08.jpg)
- [crop L1](shots/shot_008_ly_01.jpg) [crop L2](shots/shot_008_ly_02.jpg) · Continuous layer: 8% of the frame moves through the whole shot (x 0%–100%, y 40%–70%), e.g. drifting gradients, particle flow, breathing glow

**Motion #10 10.5–12.3s · 0 events**

- Ground #38363c; other main colours #484a50 #5c5b62 #6f6f75 #8b8b94; drawn layer #6e7175 #8d9599 #dfe1e9 #bc7a45
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 2%–22%, y 40%–43% · #77767e · [crop](shots/shot_010_st_01.jpg)
- S2. never moves: shape / text block · x 89%–100%, y 40%–44% · #88868d · [crop](shots/shot_010_st_02.jpg)
- S3. never moves: shape / text block · x 47%–62%, y 54%–55% · #9996a3 · text “Item filter” · [crop](shots/shot_010_st_03.jpg)
- S4. never moves: shape / text block · x 4%–24%, y 54%–56% · #7d7c82 · text “Normalizer” · [crop](shots/shot_010_st_04.jpg)
- S5. never moves: shape / text block · x 82%–93%, y 68%–70% · #72727a · [crop](shots/shot_010_st_05.jpg)
- S6. never moves: shape / text block · x 53%–69%, y 70%–72% · #93919b · [crop](shots/shot_010_st_06.jpg)
- S7. never moves: shape / text block · x 87%–100%, y 79%–85% · #78787f · [crop](shots/shot_010_st_07.jpg)
- S8. never moves: shape / text block · x 58%–73%, y 81%–87% · #7a7981 · [crop](shots/shot_010_st_08.jpg)
- [crop L1](shots/shot_010_ly_01.jpg) [crop L2](shots/shot_010_ly_02.jpg) · Continuous layer: 15% of the frame moves through the whole shot (x 0%–100%, y 31%–91%), e.g. drifting gradients, particle flow, breathing glow

**Motion #12 15.5–17.5s · 0 events**

- Ground #38363c; other main colours #484a50 #5e5c62 #6e6f76; drawn layer #707478 #a4a4af #f4f7fb #bb7b44
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 51%–64%, y 21%–23% · #6c6b72 · [crop](shots/shot_012_st_01.jpg)
- S2. never moves: shape / text block · x 19%–33%, y 22%–24% · #68666f · [crop](shots/shot_012_st_02.jpg)
- S3. never moves: shape / text block · x 18%–31%, y 29%–35% · #727077 · text “Normalizer / ormalizer” · [crop](shots/shot_012_st_03.jpg)
- S4. never moves: shape / text block · x 60%–71%, y 37%–38% · #77737a · [crop](shots/shot_012_st_04.jpg)
- S5. never moves: shape / text block · x 80%–98%, y 42%–45% · #6f6f76 · [crop](shots/shot_012_st_05.jpg)
- S6. never moves: shape / text block · x 49%–62%, y 43%–44% · #86828b · [crop](shots/shot_012_st_06.jpg)
- S7. never moves: shape / text block · x 80%–98%, y 50%–56% · #6a6a72 · text “Flaw” · [crop](shots/shot_012_st_07.jpg)
- S8. never moves: shape / text block · x 47%–60%, y 54%–55% · #9898a3 · text “Lowball Algorithm” · [crop](shots/shot_012_st_08.jpg)
- [crop L1](shots/shot_012_ly_01.jpg) [crop L2](shots/shot_012_ly_02.jpg) · Continuous layer: 11% of the frame moves through the whole shot (x 0%–100%, y 21%–69%), e.g. drifting gradients, particle flow, breathing glow

**Motion #14 19.5–21.2s · 0 events**

- Ground #38363c; other main colours #4b4b53 #616068 #787984 #979bae; drawn layer #6c7478 #9498a8 #e6eaf2
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 58%–69%, y 9%–13% · #6b6a73 · [crop](shots/shot_014_st_01.jpg)
- S2. never moves: shape / text block · x 2%–20%, y 14%–18% · #6e6d75 · [crop](shots/shot_014_st_02.jpg)
- S3. never moves: shape / text block · x 58%–78%, y 18%–24% · #7f7e84 · [crop](shots/shot_014_st_03.jpg)
- S4. never moves: shape / text block · x 91%–100%, y 21%–26% · #6b6a72 · [crop](shots/shot_014_st_04.jpg)
- S5. never moves: shape / text block · x 4%–22%, y 26%–31% · #717078 · [crop](shots/shot_014_st_05.jpg)
- S6. never moves: shape / text block · x 0%–16%, y 34%–37% · #6d6c74 · [crop](shots/shot_014_st_06.jpg)
- S7. never moves: shape / text block · x 9%–29%, y 42%–45% · #7b7a83 · [crop](shots/shot_014_st_07.jpg)
- S8. never moves: shape / text block · x 13%–31%, y 56%–58% · #808087 · text “Lowball Algorithm” · [crop](shots/shot_014_st_08.jpg)
- [crop L1](shots/shot_014_ly_01.jpg) [crop L2](shots/shot_014_ly_02.jpg) · Continuous layer: 20% of the frame moves through the whole shot (x 0%–100%, y 9%–69%), e.g. drifting gradients, particle flow, breathing glow

**Motion #16 22.8–24.4s · 5 events**

- Ground #3a373e; other main colours #faf9fd #4b4c56 #7f839c #d1d3dd; drawn layer #bac2d9 #fdf9fe #888a9a #141b37
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 0%–2%, y 38%–40% · #fdf9ff · [crop](shots/shot_016_st_01.jpg)
- S2. never moves: horizontal line · x 4%–96%, y 38%–44% · #fffbff · text “Send sellera message / Send / Sendselleramessage” · [crop](shots/shot_016_st_02.jpg)
- S3. never moves: shape / text block · x 98%–100%, y 38%–40% · #fcf8ff · [crop](shots/shot_016_st_03.jpg)
- S4. never moves: shape / text block · x 49%–53%, y 85%–86% · #3a363b · text “Message Blasterl” · [crop](shots/shot_016_st_04.jpg)
- [crop L1](shots/shot_016_ly_01.jpg) [crop L2](shots/shot_016_ly_02.jpg) · Continuous layer: 20% of the frame moves through the whole shot (x 0%–100%, y 39%–98%), e.g. drifting gradients, particle flow, breathing glow
1. 22.82–22.88s · bottom (x 0%–100%, y 55%–100%) · disappears, instant · #f1eef6 · text “Deal Analyzer / Flaw Detection / Message Blasterl” · [crop](shots/shot_016_el_01.jpg)
2. 22.95–23.02s · top (x 0%–100%, y 0%–48%) · changes, instant · #979fbf · text “2007DodgeRam1500QuadCab / $12,500 / Listedaboutaminuteago.WestKelowna,BC” · [crop](shots/shot_016_el_02.jpg)
3. 23.62–24.35s · bottom (x 31%–100%, y 50%–92%) · changes, moves downward, ease-in-out · #8a868f · text “Deal Analyzer / Message Blasterl / ayd” · [crop](shots/shot_016_el_03.jpg)
4. 24.22–24.28s · middle (x 40%–82%, y 42%–48%) · disappears, instant · #f1f1fa · text “Loading conversation” · [crop](shots/shot_016_el_04.jpg)
5. 24.22–24.28s · middle right (x 58%–82%, y 49%–51%) · appears, instant · #f7f3fa · text “was” · [crop](shots/shot_016_el_05.jpg)

**Motion #17 24.4–26.3s · 9 events**

- Ground #fbfafe; other main colours #38363c #4a4b52 #68676e #1a73fa; drawn layer #3f3d43 #1d70f9 #faf8fd #8093ac
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 62%–100%, y 0%–19% · #fffbff · text “Yepenginebayisfucked” · [crop](shots/shot_017_st_01.jpg)
- S2. never moves: shape / text block · x 27%–31%, y 19%–20% · #fffbff · [crop](shots/shot_017_st_02.jpg)
- S3. never moves: shape / text block · x 27%–40%, y 39%–41% · #fffbff · text “Are you drunk?” · [crop](shots/shot_017_st_03.jpg)
- S4. never moves: shape / text block · x 9%–13%, y 52%–56% · #4c4a51 · [crop](shots/shot_017_st_04.jpg)
- S5. never moves: shape / text block · x 0%–4%, y 57%–59% · #4b4a50 · [crop](shots/shot_017_st_05.jpg)
- S6. never moves: shape / text block · x 7%–11%, y 57%–59% · #4c4950 · [crop](shots/shot_017_st_06.jpg)
- [crop L1](shots/shot_017_ly_01.jpg) [crop L2](shots/shot_017_ly_02.jpg) · Continuous layer: 33% of the frame moves through the whole shot (x 0%–100%, y 4%–99%), e.g. drifting gradients, particle flow, breathing glow
1. 25.28–25.48s · top left (x 9%–29%, y 19%–24%) · disappears, moves leftward, ease-out · #99b9db · [crop](shots/shot_017_el_01.jpg)
2. 25.28–26.08s · top (x 22%–53%, y 24%–26%) · appears, slides rightward, ease-in-out · #236fff · text “Marketplacechatsandyourprivacy / YounamedthegroupBrody·2007DodgeRam1500QuadCab.” · [crop](shots/shot_017_el_02.jpg)
3. 25.28–25.48s · middle right (x 42%–96%, y 44%–45%) · disappears, ease-in-out · #8cb0ea · [crop](shots/shot_017_el_03.jpg)
4. 25.35–26.02s · middle left (x 16%–40%, y 40%–46%) · appears, slides leftward, ease-out · #b8b8c0 · text “Are you drunk? / Hell na” · [crop](shots/shot_017_el_04.jpg)
5. 25.82–26.08s · top (x 38%–62%, y 0%–5%) · changes, ease-in-out · #535b71 · text “Reportseller” · [crop](shots/shot_017_el_05.jpg)
6. 25.82–26.08s · top left (x 16%–36%, y 9%–11%) · appears, ease-in-out · #a09ca1 · [crop](shots/shot_017_el_06.jpg)
7. 25.82–26.08s · top right (x 67%–87%, y 9%–11%) · appears, ease-in-out · #908c91 · [crop](shots/shot_017_el_07.jpg)
8. 25.82–26.08s · top (x 22%–100%, y 15%–25%) · changes, ease-in-out · #5792ff · text “Connell Bartel / Marketplacechatsandyourprivacy / YounamedthegroupBrody·2007DodgeRam1500QuadCab.” · [crop](shots/shot_017_el_08.jpg)
9. 25.82–26.08s · middle left (x 16%–40%, y 35%–39%) · appears, ease-in-out · #b0b0b8 · text “Are you drunk?” · [crop](shots/shot_017_el_09.jpg)

**Motion #19 26.8–30.7s · 12 events**

- Ground #fbfafe; other main colours #38363c #4b4a51 #0a73fb #66666f; drawn layer #fbf9fe #3b373b #2070f7
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 0%–100%, y 52%–100% · #3a363b · text “Relentless Negotiation / Engine / RelentlessNegotiation” · [crop](shots/shot_019_st_01.jpg)
- S2. never moves: shape / text block · x 40%–42%, y 75%–79% · #3a363b · [crop](shots/shot_019_st_02.jpg)
- S3. never moves: shape / text block · x 84%–100%, y 90%–98% · #3a363b · [crop](shots/shot_019_st_03.jpg)
- S4. never moves: shape / text block · x 13%–16%, y 93%–100% · #3a363b · [crop](shots/shot_019_st_04.jpg)
- S5. never moves: shape / text block · x 0%–8%, y 94%–100% · #3a363b · [crop](shots/shot_019_st_05.jpg)
- S6. never moves: shape / text block · x 93%–100%, y 94%–99% · #4a4a50 · [crop](shots/shot_019_st_06.jpg)
- S7. never moves: shape / text block · x 71%–76%, y 95%–100% · #3a363b · [crop](shots/shot_019_st_07.jpg)
- S8. never moves: shape / text block · x 53%–66%, y 96%–100% · #4a4a50 · [crop](shots/shot_019_st_08.jpg)
- [crop L1](shots/shot_019_ly_01.jpg) [crop L2](shots/shot_019_ly_02.jpg) · Continuous layer: 30% of the frame moves through the whole shot (x 0%–100%, y 0%–100%), e.g. drifting gradients, particle flow, breathing glow
1. 26.90–28.23s · bottom (x 38%–71%, y 70%–100%) · changes, ease-out · #595757 · text “Relentless Negotiation / Engine / RelentlessNegotiation” · [crop](shots/shot_019_el_01.jpg)
2. 26.97–30.57s · top left (x 16%–49%, y 0%–4%) · disappears, moves leftward, ease-in-out · #45485d · text “Quad Cab / Marketplacechatsandyourprivacy / Are you drunk?” · [crop](shots/shot_019_el_02.jpg)
3. 27.37–30.23s · middle (x 2%–100%, y 34%–51%) · changes, scales up, ease-in-out · #f1f1ff · text “Paints clapped / Sent / 1050takeitorleaveit” · [crop](shots/shot_019_el_03.jpg)
4. 27.70–28.03s · top (x 40%–58%, y 14%–19%) · disappears, ease-in-out · #1d70fe · [crop](shots/shot_019_el_04.jpg)
5. 27.70–30.57s · top left (x 2%–33%, y 20%–29%) · disappears, moves rightward, ease-in-out · #b4b4bc · text “Are you drunk? / Hell na / Areyou drunk?” · [crop](shots/shot_019_el_05.jpg)
6. 28.77–29.97s · middle (x 27%–67%, y 34%–51%) · changes, unfolds upward (draw-on / grow / wipe), ease-in-out · #fffbff · text “Leaveme alone / Aa / Fine. 1300 and” · [crop](shots/shot_019_el_06.jpg)
7. 29.10–29.17s · top left (x 22%–40%, y 12%–15%) · appears, instant · #b8b8c0 · text “Hell na” · [crop](shots/shot_019_el_07.jpg)
8. 29.63–30.03s · top left (x 2%–22%, y 2%–11%) · appears, scales up, ease-in-out · #847a83 · text “Hell na” · [crop](shots/shot_019_el_08.jpg)
9. 29.63–29.97s · top left (x 16%–40%, y 6%–10%) · disappears, moves leftward, ease-in-out · #acacb4 · text “Are you drunk? / Hell na” · [crop](shots/shot_019_el_09.jpg)
10. 30.57–30.63s · top left (x 2%–11%, y 14%–19%) · appears, instant · #483d3f · [crop](shots/shot_019_el_10.jpg)
11. 30.57–30.63s · top right (x 38%–100%, y 15%–31%) · changes, instant · #70a8ff · text “PrettyclappedI'lltake it for1200 / Have it cleaned up forme tonight / Paints clapped” · [crop](shots/shot_019_el_11.jpg)
12. 30.57–30.63s · middle left (x 2%–31%, y 31%–36%) · appears, instant · #84838a · text “Hell na / Leavemealone” · [crop](shots/shot_019_el_12.jpg)

**Motion #22 33.0–36.5s · 17 events**

- Ground #fcfbff; other main colours #38363c #4c4b52 #0371fc #6b6d76; drawn layer #3c383c #1d70fc #fdfaff #4c82d1
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 0%–20%, y 55%–66% · #3a363b · [crop](shots/shot_022_st_01.jpg)
- S2. never moves: shape / text block · x 24%–42%, y 55%–70% · #3a363b · [crop](shots/shot_022_st_02.jpg)
- S3. never moves: shape / text block · x 33%–40%, y 55%–59% · #3a363b · [crop](shots/shot_022_st_03.jpg)
- S4. never moves: shape / text block · x 62%–71%, y 55%–59% · #3a363b · [crop](shots/shot_022_st_04.jpg)
- S5. never moves: shape / text block · x 71%–100%, y 55%–65% · #3a363b · [crop](shots/shot_022_st_05.jpg)
- S6. never moves: shape / text block · x 53%–100%, y 61%–100% · #3a363b · text “CRM Integration / create:lead” · [crop](shots/shot_022_st_06.jpg)
- S7. never moves: shape / text block · x 14%–69%, y 74%–93% · #3a363b · text “egotiation / Follow-up Nuke / Negotiation” · [crop](shots/shot_022_st_07.jpg)
- S8. never moves: shape / text block · x 31%–38%, y 90%–96% · #3a363b · [crop](shots/shot_022_st_08.jpg)
- [crop L1](shots/shot_022_ly_01.jpg) [crop L2](shots/shot_022_ly_02.jpg) · Continuous layer: 21% of the frame moves through the whole shot (x 0%–100%, y 0%–100%), e.g. drifting gradients, particle flow, breathing glow
1. 33.11–34.24s · bottom (x 38%–60%, y 81%–84%) · disappears, ease-in-out · #7b777c · text “Follow-up Nuke” · [crop](shots/shot_022_el_01.jpg)
2. 33.24–33.71s · top (x 38%–62%, y 0%–9%) · changes, moves leftward, ease-out · #fffbff · [crop](shots/shot_022_el_02.jpg)
3. 33.24–33.38s · top left (x 2%–42%, y 8%–10%) · disappears, instant · #8f8f97 · text “Screwoff” · [crop](shots/shot_022_el_03.jpg)
4. 33.24–33.31s · top (x 38%–60%, y 11%–20%) · disappears, instant · #2072fe · [crop](shots/shot_022_el_04.jpg)
5. 33.24–33.31s · top left (x 2%–31%, y 24%–29%) · disappears, instant · #85838b · [crop](shots/shot_022_el_05.jpg)
6. 33.24–35.77s · middle right (x 67%–98%, y 25%–52%) · changes, moves downward, ease-in-out · #f7fbff · text “Hey / Wherearetou / Hello?” · [crop](shots/shot_022_el_06.jpg)
7. 34.11–34.17s · top (x 58%–67%, y 0%–4%) · disappears, instant · #2372fe · [crop](shots/shot_022_el_07.jpg)
8. 34.11–34.17s · top left (x 2%–20%, y 6%–10%) · disappears, instant · #624f51 · [crop](shots/shot_022_el_08.jpg)
9. 34.38–35.71s · middle right (x 58%–87%, y 39%–54%) · disappears, moves rightward, ease-in-out · #1b6eff · text “Have it ready tonight / I'll stop by soon / Hey you there?” · [crop](shots/shot_022_el_09.jpg)
10. 34.77–35.31s · top (x 58%–69%, y 25%–40%) · changes, moves upward, ease-in · #66a3f2 · [crop](shots/shot_022_el_10.jpg)
11. 35.11–35.97s · top right (x 58%–84%, y 11%–22%) · disappears, moves upward, ease-in-out · #1d6fff · text “Hey you there? / Heyyou there? / Wherearetou” · [crop](shots/shot_022_el_11.jpg)
12. 35.31–36.11s · top right (x 60%–82%, y 0%–9%) · appears, scales up, ease-in-out · #2271ff · text “Hey you there? / Have it ready tonight” · [crop](shots/shot_022_el_12.jpg)
13. 35.77–36.11s · bottom (x 38%–60%, y 94%–100%) · disappears, moves rightward, ease-in · #4b4a50 · [crop](shots/shot_022_el_13.jpg)
14. 35.91–36.31s · middle (x 9%–100%, y 55%–79%) · changes, moves rightward, ease-out · #48484f · text “egotiation / Negotiation / Follow-up Nuke” · [crop](shots/shot_022_el_14.jpg)
15. 36.04–36.38s · middle left (x 2%–47%, y 46%–51%) · appears, unfolds upward (draw-on / grow / wipe), ease-in · #8e8c95 · text “FUCKKKOFFFFFFF” · [crop](shots/shot_022_el_15.jpg)
16. 36.11–36.24s · middle left (x 0%–22%, y 55%–65%) · appears, instant · #5a585f · [crop](shots/shot_022_el_16.jpg)
17. 36.11–36.17s · bottom left (x 2%–33%, y 89%–100%) · disappears, instant · #5c5759

**Motion #24 37.0–38.2s · 0 events**

- Ground #38363c; other main colours #474951 #676770 #56565f #8a8282; drawn layer #717073 #a2a2ae #f1f5fa
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- S1. never moves: shape / text block · x 0%–11%, y 1%–3% · #6a6871 · [crop](shots/shot_024_st_01.jpg)
- S2. never moves: shape / text block · x 38%–51%, y 2%–4% · #6a6870 · [crop](shots/shot_024_st_02.jpg)
- S3. never moves: shape / text block · x 0%–11%, y 8%–13% · #6b6a73 · [crop](shots/shot_024_st_03.jpg)
- S4. never moves: shape / text block · x 34%–51%, y 9%–14% · #716f78 · [crop](shots/shot_024_st_04.jpg)
- S5. never moves: shape / text block · x 38%–51%, y 21%–22% · #6f6d76 · [crop](shots/shot_024_st_05.jpg)
- S6. never moves: shape / text block · x 0%–9%, y 25%–29% · #6e6c75 · [crop](shots/shot_024_st_06.jpg)
- S7. never moves: shape / text block · x 0%–11%, y 41%–46% · #75737a · [crop](shots/shot_024_st_07.jpg)
- S8. never moves: shape / text block · x 2%–18%, y 51%–52% · #75737c · [crop](shots/shot_024_st_08.jpg)
- [crop L1](shots/shot_024_ly_01.jpg) [crop L2](shots/shot_024_ly_02.jpg) · Continuous layer: 19% of the frame moves through the whole shot (x 0%–100%, y 1%–69%), e.g. drifting gradients, particle flow, breathing glow

**Motion #26 39.6–43.2s · 10 events**

- Ground #38363c; other main colours #484a51 #6e717b #5d5c63 #818d9b; drawn layer #716e75 #9b969b #eaeff5 #4aa6d7
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

- [crop L1](shots/shot_026_ly_01.jpg) [crop L2](shots/shot_026_ly_02.jpg) · Continuous layer: 19% of the frame moves through the whole shot (x 0%–98%, y 26%–100%), e.g. drifting gradients, particle flow, breathing glow
1. 39.65–40.52s · top left (x 0%–22%, y 20%–44%) · changes, moves leftward, ease-out · #3b373c · [crop](shots/shot_026_el_01.jpg)
2. 39.65–40.52s · bottom right (x 71%–87%, y 82%–94%) · disappears, moves leftward, ease-in-out · #55555c · [crop](shots/shot_026_el_02.jpg)
3. 39.85–40.98s · middle left (x 2%–9%, y 46%–52%) · disappears, moves leftward, ease-in-out · #4b4a50 · [crop](shots/shot_026_el_03.jpg)
4. 41.12–42.12s · bottom left (x 0%–47%, y 70%–82%) · disappears, moves leftward, ease-in · #4d4a52 · [crop](shots/shot_026_el_04.jpg)
5. 41.32–41.78s · middle left (x 0%–9%, y 25%–44%) · disappears, moves leftward, ease-in · #605d66 · [crop](shots/shot_026_el_05.jpg)
6. 41.32–42.45s · bottom (x 44%–56%, y 90%–96%) · disappears, moves leftward, ease-in-out · #5a5861 · [crop](shots/shot_026_el_06.jpg)
7. 41.38–43.12s · middle left (x 0%–38%, y 46%–64%) · changes, moves leftward, linear · #4c4a50 · text “Value Calculator” · [crop](shots/shot_026_el_07.jpg)
8. 41.45–41.85s · bottom (x 58%–76%, y 75%–80%) · disappears, moves leftward, ease-in-out · #4d4a50 · [crop](shots/shot_026_el_08.jpg)
9. 41.45–43.12s · bottom left (x 9%–47%, y 82%–100%) · appears, slides downward, ease-in-out · #4d4b54 · [crop](shots/shot_026_el_09.jpg)
10. 41.45–41.92s · bottom right (x 60%–76%, y 82%–98%) · disappears, moves downward, ease-in-out · #55565e · [crop](shots/shot_026_el_10.jpg)

### Real material in the picture (the original files are needed)

21 shots, 39.84s (76%) contain real material (screen recordings, screenshots, photos, embedded video); a model cannot stand in for them:

- **live footage** (whole frame): shots #1, #5–#7, #9, #11, #13, #15, #18, #20, #21, #23, #25, #27, 27.0s in all
- **UI screenshot** (whole frame): shots #2–#4, 2.0s in all
- **screen recording** (part of the frame x9% y36% w82% h55%): shots #2, 0.8s in all
- **screen recording** (part of the frame), Phone screen recording of a marketplace app: shots #2–#4, 2.0s in all
- **screen recording** (part of the frame x8% y9% w83% h83%): shots #4, 0.8s in all
- **UI screenshot** (part of the frame x0% y25% w100% h31%): shots #16, 1.7s in all
- **screen recording** (part of the frame), Marketplace listing of a pickup truck: shots #16, 1.7s in all
- **screen recording** (part of the frame x0% y0% w100% h54%): shots #17, 1.9s in all
- **screen recording** (part of the frame), Marketplace chat with lowball offers being typed: shots #17, 1.9s in all
- **screen recording** (part of the frame x0% y0% w100% h53%): shots #19, 3.8s in all
- **screen recording** (part of the frame), Marketplace chat, seller replies: shots #19, 3.8s in all
- **UI screenshot** (part of the frame x0% y0% w100% h55%): shots #22, 3.4s in all
- **screen recording** (part of the frame), Marketplace chat, repeated follow-ups: shots #22, 3.4s in all

### Acting and emotion

In a prompt, describe the visible expression and movement rather than words like “happy” or “sad”, and keep it smaller rather than bigger (strong emotion words tend to give mask faces and forced smiles); get the expression right in the first frame; for shots with lines, make the voice with its delivery first and let the picture act to it. For generated shots the Face and Movement below are already in the generation-unit prompts.

**all 14 shots**

| Shot | Who | Emotion (strength) | Face | Movement / change | Delivery | How to get it |
|---|---|---|---|---|---|---|
| #1 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #5 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #6 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #7 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #9 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #11 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #13 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #15 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #18 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #20 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #21 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #23 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #25 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |
| #27 | A | deadpan (light) | neutral brows, eyes to camera, slight smirk on some lines | seated at a desk turned three-quarters to camera, one hand on the mouse, the other gesturing | — | actor plays it |

- **actor plays it**: Filmed: hand the face, movement and delivery to the actor as direction, and rehearse the pauses and tone against the original once
