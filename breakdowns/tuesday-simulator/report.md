# How this video was made: tuesday-simulator.mp4

**In one line**: A deadpan walkthrough of an absurd automation that runs a man's whole day, told as a fast list where every item gets its own diagram or fake screenshot.
**How it was made**: Mixed production: live action 74% + code / template render 26%

- 1:03 · vertical 9:16 · 29 shots, 2.2s each on average
- Confidence 76%, based on: tool measurements + AI assistant reviewed 29 shots + user corrections
- ⚠️ 16 points are uncertain, see “Open questions”

![storyboard](storyboard.jpg)

# Part one · Breakdown: how this video is built

## What makes it work

- **The hook**: 0 to 4 s: the presenter is already mid-sentence with the full workflow floating above his head, then names it. The viewer sees the finished system before any explanation.
- Every claim gets a picture within about a second: 12 of 29 shots are a split with the proof on top and the presenter below, so the joke lands without leaving his face
- The layout changes at almost every cut (wide, split, full-frame graphic), so a one-minute list never holds one look for more than a few seconds
- One diagram is reused all the way through: each step is another branch of the same workflow, which makes a list feel like one system
- Captions are one or two words in heavy italic capitals, placed at the seam of the split, so they read on both layouts

## Production pipeline at a glance

| Stage | What this video uses | Remake approach |
|---|---|---|
| **Base picture** | live action 22 shots (74%), code / template render 7 shots (26%); includes real material in 22 shots (74%) | filmed in 1 scene; screen recording / motion graphics in code |
| **Packaging** | 34 subtitle lines (bottom/middle/top, up to 2 rows): grey text, line height 2.5%; entrance: hard in×20, scale pop×6, fade in×3, slide in×1, type-on×1; keywords change colour as they are spoken; styled text ×2 (large size, tilted, blue fill, multi-colour / gradient): "pT:https://bac", "Have it cleane"; text label ×143 (1 of them follow an object): "JUST", "MOST", "WORKFLOW", "SEE.", "SIMULATOR", "INSTAGRAM1" …; Stickers / GIFs: static sticker / image ×6; Placed by spoken line ×4 (with new wording they follow the line, not the old second): styled text "Have it cleane" → 0.0s into ""cleaned up"", on "cleanedup", text label "$1000" → 0.2s before ""1000"", on "1000", static sticker / image → 0.7s after "Today 8:07 PM" …; 6 persistent layers (unchanged across cuts: lay each on once for its span, not per shot): static sticker / image 8.4–12.4s, static sticker / image 20.3–26.1s, static sticker / image 26.3–31.1s, static sticker / image 43.9–49.5s … | export `packaging/subtitles.srt` for timeline alignment |
| **Sound** | voice（human recording） | voice: record it yourself |

## Content and structure

- The narrative line below comes from reading each shot; the lines were not transcribed separately, subtitle text is under “Packaging layer”

**Narrative line**

Keep this line in a remake: same order, same job at each step, with the point refilled from your own cases, numbers and material, so it is more than a change of subject.

| Time | Shots | Job | What it says |
|---|---|---|---|
| 0.0–3.8s | #1, #2 | grab attention | Open on the finished system in frame while naming it → Give the thing an absurd, memorable name |
| 3.8–6.8s | #3 | set the scene | Show the first step of the system as a moving diagram |
| 6.8–8.3s | #4 | add information | Explain one step while the matching part of the diagram is on screen |
| 8.3–10.3s | #5 | show evidence | Show the joke result of the step as a fake screenshot |
| 10.3–12.5s | #6 | turn | Reset to the presenter before the next item |
| 12.5–18.2s | #7, #8 | add information | Next step shown as a new branch of the same diagram → Presenter carries the line between diagrams |
| 18.2–19.8s | #9 | show evidence | Pay off the step with a mock text conversation |
| 19.8–20.2s | #10 | turn | A fast cutaway back to the presenter to keep pace |
| 20.2–22.8s | #11 | show evidence | Illustrate the claim with a small animated map instead of footage |
| 22.8–37.2s | #12–#17 | add information | Presenter carries the next claim → Name the next step while its nodes are on screen → Presenter bridges to the next step → Zoom into one node to make a technical step feel concrete → Show the branch that fans out to many outputs → (… 6 points, each shot in the shot list) |
| 37.2–38.7s | #18 | turn | Back to the presenter before the biggest claim |
| 38.7–41.4s | #19 | add information | Introduce the most elaborate branch with its diagram |
| 41.4–43.8s | #20, #21 | show evidence | Show the automation acting on real-looking listings → Put the big number on screen at the moment it is said |
| 43.8–55.1s | #22–#26 | add information | Move to the next step by swapping only the top panel → Presenter carries the next claim → Another absurd step, same layout → Presenter introduces the group chat step → Show the chat automation as three nodes |
| 55.1–56.0s | #27 | turn | Signal the last item |
| 56.0–59.6s | #28 | add information | End the list on the most useful-sounding step |
| 59.6–63.9s | #29 | call to action | Close on the presenter with the offer |

## Shot list

| # | Frame | Time | What it says | Picture | Camera | Made with |
|---|---|---|---|---|---|---|
| 1 | ![#1](shots/shot_001_first.jpg) | 0:00.0 · 2.5s | grab attention: Open on the finished system in frame while n… | Wide shot: a man sits on a teal sofa in an office lounge hol… | static | live action |
| 2 | ![#2](shots/shot_002_first.jpg) | 0:02.5 · 1.4s | grab attention: Give the thing an absurd, memorable name | Same wide shot, the workflow panel still floating above him … | static | live action |
| 3 | ![#3](shots/shot_003_first.jpg) | 0:03.8 · 3.0s | set the scene: Show the first step of the system as a moving… | Full-frame motion graphic: the camera glides over a dark nod… | whole-frame zoom / pan | code / template render |
| 4 | ![#4](shots/shot_004_first.jpg) | 0:06.8 · 1.5s | add information: Explain one step while the matching part of… | Top half: six workflow nodes labelled Instagram, TikTok, Twi… | whole-frame zoom / pan | live action |
| 5 | ![#5](shots/shot_005_first.jpg) | 0:08.3 · 2.0s | show evidence: Show the joke result of the step as a fake sc… | Top half: a social feed where one post reading Rise and Grin… | smooth move | live action |
| 6 | ![#6](shots/shot_006_first.jpg) | 0:10.3 · 2.1s | turn: Reset to the presenter before the next item | Wide shot of the presenter on the sofa, laptop on his knee, … | static | live action |
| 7 | ![#7](shots/shot_007_first.jpg) | 0:12.5 · 3.7s | add information: Next step shown as a new branch of the same… | Full-frame workflow canvas: a pink play node and a globe nod… | whole-frame zoom / pan | code / template render |
| 8 | ![#8](shots/shot_008_first.jpg) | 0:16.1 · 2.1s | add information: Presenter carries the line between diagrams | Medium shot of the presenter gesturing with one hand as he e… | smooth move | live action |
| 9 | ![#9](shots/shot_009_first.jpg) | 0:18.2 · 1.5s | show evidence: Pay off the step with a mock text conversatio… | Full-frame white card: a phone message thread, tilted in 3D … | smooth move | code / template render |
| 10 | ![#10](shots/shot_010_first.jpg) | 0:19.8 · 0.5s | turn: A fast cutaway back to the presenter to keep pace | Very short medium shot of the presenter starting the next se… | smooth move | live action |
| 11 | ![#11](shots/shot_011_first.jpg) | 0:20.2 · 2.6s | show evidence: Illustrate the claim with a small animated ma… | Full-frame split graphic: on top a simple map with a red car… | smooth move | code / template render |
| 12 | ![#12](shots/shot_012_first.jpg) | 0:22.8 · 3.4s | add information: Presenter carries the next claim | Wide shot of the presenter on the sofa continuing the list. | static | live action |
| 13 | ![#13](shots/shot_013_first.jpg) | 0:26.2 · 2.3s | add information: Name the next step while its nodes are on s… | Top half: workflow nodes labelled Uber Black to Casino and B… | smooth move | live action |
| 14 | ![#14](shots/shot_014_first.jpg) | 0:28.5 · 2.6s | add information: Presenter bridges to the next step | Wide shot of the presenter, hand raised mid-gesture. | smooth move | live action |
| 15 | ![#15](shots/shot_015_first.jpg) | 0:31.2 · 2.1s | add information: Zoom into one node to make a technical step… | Full-frame workflow canvas pushing in on a Bet365 API node f… | smooth move | code / template render |
| 16 | ![#16](shots/shot_016_first.jpg) | 0:33.2 · 2.5s | add information: Show the branch that fans out to many outpu… | Full-frame workflow canvas: a Flex Wins on Socials node with… | whole-frame zoom / pan | code / template render |
| 17 | ![#17](shots/shot_017_first.jpg) | 0:35.7 · 1.4s | add information: Call back to the social nodes from the star… | Full-frame workflow canvas with the six social platform node… | whole-frame zoom / pan | code / template render |
| 18 | ![#18](shots/shot_018_first.jpg) | 0:37.2 · 1.5s | turn: Back to the presenter before the biggest claim | Medium shot of the presenter leaning into the next point. | smooth move | live action |
| 19 | ![#19](shots/shot_019_first.jpg) | 0:38.7 · 2.7s | add information: Introduce the most elaborate branch with it… | Top half: a long row of workflow nodes for a marketplace scr… | smooth move | live action |
| 20 | ![#20](shots/shot_020_first.jpg) | 0:41.4 · 1.3s | show evidence: Show the automation acting on real-looking li… | Top half: a marketplace grid of used motorcycles, then one l… | static | live action |
| 21 | ![#21](shots/shot_021_first.jpg) | 0:42.7 · 1.1s | show evidence: Put the big number on screen at the moment it… | Top half: more motorcycle listings scrolling. Bottom half: t… | static (subject moves) | live action |
| 22 | ![#22](shots/shot_022_first.jpg) | 0:43.8 · 4.3s | add information: Move to the next step by swapping only the … | Top half: the listings give way to a workflow node labelled … | whole-frame zoom / pan | live action |
| 23 | ![#23](shots/shot_023_first.jpg) | 0:48.1 · 1.5s | add information: Presenter carries the next claim | Wide shot of the presenter on the sofa. Caption: EVERY. | smooth move | live action |
| 24 | ![#24](shots/shot_024_first.jpg) | 0:49.6 · 1.9s | add information: Another absurd step, same layout | Top half: workflow nodes labelled Steak and Monster Delivery… | smooth move | live action |
| 25 | ![#25](shots/shot_025_first.jpg) | 0:51.5 · 1.0s | add information: Presenter introduces the group chat step | Short medium shot of the presenter. Caption: WE HAVE A CHAT. | static | live action |
| 26 | ![#26](shots/shot_026_first.jpg) | 0:52.5 · 2.7s | add information: Show the chat automation as three nodes | Top half: workflow nodes Find Facebook Group, Filter Recent … | smooth move | live action |
| 27 | ![#27](shots/shot_027_first.jpg) | 0:55.1 · 0.8s | turn: Signal the last item | Short medium shot of the presenter. Caption: FINALLY, | whole-frame zoom / pan | live action |
| 28 | ![#28](shots/shot_028_first.jpg) | 0:56.0 · 3.6s | add information: End the list on the most useful-sounding st… | Top half: a larger workflow labelled Search eBay Deals, Find… | whole-frame zoom / pan | live action |
| 29 | ![#29](shots/shot_029_first.jpg) | 0:59.6 · 4.3s | call to action: Close on the presenter with the offer | Medium shot of the presenter delivering the closing line to … | smooth move | live action |

## Cast, scenes and props

- **Visual style**: Filmed footage in natural office light, cut with flat vector workflow diagrams on a dark dotted canvas (glow, depth blur) and phone screenshots. Captions in white heavy italic capitals with a soft glo

| Id | Name | Kind | Look | Role | Voice | Shots |
|---|---|---|---|---|---|---|
| A | Presenter | person | Man in his twenties, wavy brown hair, short beard, oversized charcoal tee, navy shorts, steel wristwatch on the left wrist | Narrator, on camera throughout | — | #1, #2, #4–#6, #8, #10, #12–#14, #18–#29 |

- Character consistency: Presenter appear across multiple shots; lock an anchor image first and feed it as reference in later shots

**Scenes**

| Scene | Where | When | Set / light | Shots |
|---|---|---|---|---|
| S1 | Office lounge: teal modular sofa, round wood coffee table, wood-panelled wall, g | Daytime, interior | Soft overhead light, cool daylight through glass | #1, #2, #4–#6, #8, #10, #12–#14, #18–#29 |

**Props / products / logos**

- Laptop (shots #1, #2, #6, #12, #14, #23): Open on his knee in the wide shots
- Workflow diagram (shots #1–#4, #7, #11, #13, #15–#17, #19, #22, #24, #26, #28): The recurring automation canvas, shown as a floating panel, a top-half insert and full frame

## Camera and lighting

- Framing: shot size medium shot 100%; subject is a face (shot size from face height)
- Camera: moving camera (gimbal / handheld pan) 51%, fixed camera (tripod / mount / on the desk) 49%; typical move pan / track
- Lighting: Available office light: soft ceiling downlights and daylight through glass behind and to the side. No visible key light or rim light. (image reading; pixel measurements in the fold below)
- Grade: natural (close to the original colours); normal saturation, normal contrast, normal blacks, overall neutral
- Format: talking head (face as subject 100%, objects / hands as subject 0%, handheld 51%); image readers: Scripted talking-head list video with motion-graphic and screenshot inserts

<details class="ref"><summary>Per-item measurements and image readings (11)</summary>

| Aspect | Item | Verdict | Sources |
|---|---|---|---|
| Framing | shot size | medium shot | measured |
| Camera | camera support | mixed: moving camera (gimbal / handheld pan) 51%, fixed camera (tripod / mount / on the desk) 49% | measured |
| Camera | set-ups / locations | One location, two framings of the same seat: a wide shot with the knees in frame and a tighter medium shot. Looks like one take punched in, or two phones. | agent review |
| Camera | likely gear | Phone or mirrorless camera on a tripod at seated eye level. A guess from the framing and depth of field. | agent review |
| Lighting | soft / hard | soft light (wide lit-to-shadow ramp) | measured |
| Lighting | colour temperature | warm (about 3000–4000K) | measured |
| Lighting | overall lighting | Available office light: soft ceiling downlights and daylight through glass behind and to the side. No visible key light or rim light. | agent review |
| Grade | colour grade | natural (close to the original colours) | measured |
| Grade | overall grade | Natural, slightly cool, with teal in the sofa and warm wood behind. Moderate contrast. | agent review |
| Editing | editing style | Fast alternation between the presenter and inserts every 1 to 3 seconds. Three layouts rotate: presenter full frame, a split with the insert on top and the presenter below, and a full-frame graphic. Hard cuts only. | agent review |
| Format | video format | Scripted talking-head list video with motion-graphic and screenshot inserts | measured: talking head; agent review |

- Note: lighting ratio, soft / hard, colour temperature and shot size are measured on the subject's pixels (the face when there is one, otherwise the in-focus region, which is an estimate); platform transcodes crush the shadows, so hardness and fill read conservative; camera angle, light source, catchlight and rim light follow the image readers. Where measurement and readers disagree, both are listed.

</details>

## Packaging layer (subtitles / styled text / stickers / sound-effect hits)

- 34 subtitle lines (bottom/middle/top, up to 2 rows): grey text, line height 2.5%; entrance: hard in×20, scale pop×6, fade in×3, slide in×1, type-on×1; keywords change colour as they are spoken
- styled text ×2 (large size, tilted, blue fill, multi-colour / gradient): "pT:https://bac", "Have it cleane"
- text label ×143 (1 of them follow an object): "JUST", "MOST", "WORKFLOW", "SEE.", "SIMULATOR", "INSTAGRAM1" …
- Stickers / GIFs: static sticker / image ×6
- Placed by spoken line ×4 (with new wording they follow the line, not the old second): styled text "Have it cleane" → 0.0s into ""cleaned up"", on "cleanedup", text label "$1000" → 0.2s before ""1000"", on "1000", static sticker / image → 0.7s after "Today 8:07 PM" …
- 6 persistent layers (unchanged across cuts: lay each on once for its span, not per shot): static sticker / image 8.4–12.4s, static sticker / image 20.3–26.1s, static sticker / image 26.3–31.1s, static sticker / image 43.9–49.5s …

<details class="ref"><summary>text timeline (120 rows)</summary>

| Time | Kind | Text | Style | In / out | SFX |
|---|---|---|---|---|---|
| 0.00–0.10s | text label | JUST | white text, grey outline, line height 3.9% (about 75px) | hard out | — |
| 0.50–0.70s | text label | MOST | white text, grey outline, bold, line height 3.7% (about 70px) | hard in / slide out | — |
| 0.80–1.80s | text label | WORKFLOW | white text, grey outline, bold, line height 3.5% (about 68px) | hard out | — |
| 1.90–2.10s | text label | SEE. | white text, line height 3.8% (about 72px) | hard in / hard out | — |
| 2.50–3.80s | text label | SIMULATOR | white text, grey outline, line height 4.8% (about 92px) | hard out | — |
| 3.80–6.80s | subtitle · follows an object | Wait2 | grey text, grey outline, line height 3.4% (about 66px) | hard in / hard out | — |
| 6.80–8.30s | text label | INSTAGRAM1 | white text, line height 2.2% (about 42px) | hard in | — |
| 6.80–8.30s | subtitle | TIKTOK1 | grey text, line height 1.8% (about 35px) | hard in / hard out | — |
| 6.80–8.30s | text label | TWITTER1 | grey text, keywords highlighted in grey, line height 1.8% (about 35px) | hard in / hard out | — |
| 6.80–8.30s | subtitle | POT:https://backend.blotato..POST:https: | grey text, line height 2.7% (about 52px) | hard in / hard out | — |
| 6.80–8.30s | styled text | pT:https://backend.blotato...OST:http//b | grey text, line height 5.6% (about 108px) | hard in | — |
| 6.80–8.40s | text label | "RISEAND GRIND | white text, grey outline, line height 3.8% (about 72px) | hard in / slide out | — |
| 7.00–8.10s | subtitle | FACEBOOK1 | black text, line height 2.5% (about 48px) | hard in / fade out | — |
| 8.40–8.60s | text label | TO ALL | white text, grey outline, line height 3.8% (about 74px) | hard in / hard out | — |
| 8.50–9.60s | text label | 3h | white text, line height 1.5% (about 28px) | hard in / fade out (bounces / changes colour midway) | — |
| 8.50–9.60s | text label | stop saying this | red text, keywords highlighted in cyan, line height 2.2% (about 42px) | hard in / hard out (bounces / changes colour midway) | — |
| 8.50–9.60s | text label | Sara Miller·2h | black text, line height 1.7% (about 33px) | fade out (bounces / changes colour midway) | — |
| 8.50–9.60s | text label | SHUT UP | cyan text, keywords highlighted in brown, line height 1.9% (about 36px) | hard out (bounces / changes colour midway) | — |
| 8.50–9.60s | subtitle | Nicole James·2h | black text, line height 1.9% (about 37px) | fade out (bounces / changes colour midway) | — |
| 8.50–9.60s | text label · follows an object | PLEASESTOP | white text, black outline, bold, line height 1.9% (about 37px) | hard out (bounces / changes colour midway) | — |
| 8.90–9.10s | text label | SOCIAL | white text, grey outline, bold, line height 3.6% (about 69px) | hard in / hard out | — |
| 9.50–10.30s | text label | PLATFORMS. | white text, grey outline, bold, line height 3.3% (about 63px) | hard out | — |
| 9.80–10.20s | text label | KevinBrown·2h | white text, line height 2.1% (about 41px) | hard in / hard out | — |
| 9.90–10.10s | text label | Kyle Anderson· 2h | black text, line height 2.1% (about 41px) | hard in / hard out | — |
| 9.90–10.10s | subtitle | BrianMoore·2h | black text, line height 1.9% (about 37px) | hard in / hard out | — |
| 10.00–10.10s | text label | stop saying this | white text, line height 1.9% (about 37px) | hard in / hard out | — |
| 10.00–10.10s | text label | Sara Miller · 2h | black text, line height 1.9% (about 37px) | hard in / hard out | — |
| 10.00–10.10s | text label | SHUT UP | red text, keywords highlighted in cyan, line height 1.8% (about 35px) | hard in / hard out | — |
| 10.30–10.60s | text label | FIVE | white text, blue outline, line height 4.2% (about 81px) | hard in / hard out | — |
| 10.80–11.10s | text label | AFTER | white text, grey outline, line height 4.1% (about 78px) | hard in / hard out | — |
| 11.40–11.70s | text label | IS | white text, blue outline, line height 4.5% (about 85px) | hard in / hard out | — |
| 11.80–12.20s | text label | IT | white text, blue outline, line height 4.2% (about 81px) | hard in / hard out | — |
| 12.50–16.10s | subtitle | Play Man in the box | white text, line height 2.9% (about 55px) | hard in / hard out | — |
| 12.50–16.10s | subtitle | GET:https://api.spotify.com/v... | grey text, line height 3.2% (about 61px) | hard in / hard out | — |
| 16.10–16.70s | text label | WILL | white text, blue outline, bold, line height 3.7% (about 70px) | hard in / hard out | — |
| 16.80–17.30s | text label | REPLY | white text, blue outline, bold, line height 3.7% (about 70px) | hard in / slide out | — |
| 17.50–17.60s | text label | EVERY | white text, blue outline, bold, line height 3.7% (about 70px) | hard in / hard out | — |
| 17.90–18.20s | text label | WITH | white text, keywords highlighted in grey, bold, line height 3.7% (about 70px) | hard in / hard out | — |
| 18.00–19.60s | subtitle | Read8:07PM | grey text, line height 2.1% (about 40px) | pop / fade out (bounces / changes colour midway) | — |
| 18.00–19.60s | subtitle | Today 8:07 PM | grey text, line height 3.0% (about 59px) | pop / hard out (bounces / changes colour midway) | — |
| 19.00–19.60s | subtitle | 三 | grey text, gradient, line height 2.4% (about 46px) | fade in / hard out | — |
| 19.80–20.20s | text label | THIS WILL | white text, grey outline, line height 3.8% (about 74px) | hard in / hard out | — |
| 20.00–20.60s | subtitle | Beer & Cig Farmer ⏎ GET: https://api.doo | white text, line height 3.2% (about 62px) | pop / hard out | — |
| 21.00–22.40s | subtitle | Beer & Cig Farmer | white text, line height 3.0% (about 57px) | slide in / fade out | — |
| 21.00–22.80s | subtitle | 2 | grey text, line height 2.4% (about 46px) | hard out | — |
| 23.00–23.50s | text label | AUTOMATICALLY | white text, grey outline, bold, line height 3.0% (about 59px) | hard in / shrink out | — |
| 23.10–23.60s | text label | TIME | white text, grey outline, line height 4.2% (about 81px) | fade in / hard out | — |
| 23.90–24.10s | text label | WHEN | white text, blue outline, bold, line height 3.7% (about 70px) | hard out | — |
| 24.40–24.60s | text label | CIGARETS | white text, grey outline, bold, line height 3.4% (about 65px) | hard in / hard out | — |
| 24.70–25.20s | text label | ARRIVES | white text, grey outline, line height 3.9% (about 75px) | hard in / hard out | — |
| 25.20–25.70s | text label | THE | white text, blue outline, line height 4.1% (about 78px) | hard in / hard out | — |
| 25.90–26.20s | text label | API | white text, grey outline, line height 4.1% (about 79px) | hard in | — |
| 26.00–28.50s | text label | Uber Black to Casino | white text, line height 1.7% (about 33px) | pop / hard out | — |
| 26.00–27.00s | text label | Nait | grey text, grey outline, line height 1.4% (about 26px) | pop / shrink out (bounces / changes colour midway) | — |
| 26.00–28.50s | text label | Waiti | grey text, line height 1.6% (about 31px) | type-on / hard out | — |
| 26.20–26.70s | text label | ORDERS | white text, grey outline, bold, line height 3.3% (about 63px) | hard in / hard out | — |
| 26.90–27.10s | text label | UBER | white text, grey outline, line height 3.8% (about 74px) | hard in / hard out | — |
| 27.30–27.70s | text label | TO THE | white text, grey outline, line height 3.8% (about 74px) | hard in / hard out | — |
| 27.90–28.50s | text label | CASINO. | white text, grey outline, bold, line height 3.4% (about 65px) | hard in / hard out | — |
| 28.50–28.80s | text label | DURING | white text, blue outline, line height 3.8% (about 74px) | hard in / hard out | — |
| 28.80–29.10s | text label | TO THE. | white text, grey outline, line height 4.2% (about 81px) | hard in / hard out | — |
| 29.30–29.90s | text label | CASINO, | white text, grey outline, line height 4.2% (about 81px) | hard out | — |
| 29.90–30.10s | text label | DIFFERENT | white text, blue outline, bold, line height 3.5% (about 68px) | hard in / hard out | — |
| 30.40–30.70s | text label | WILL | white text, grey outline, line height 3.9% (about 75px) | hard in / hard out | — |
| 30.80–31.10s | text label | FIRST, | white text, blue outline, line height 4.7% (about 90px) | hard in / hard out | — |
| 31.00–32.10s | subtitle | Black to Casino | grey text, line height 3.8% (about 72px) | pop / shrink out | — |
| 31.00–32.10s | subtitle | https://api.uber.com/v1/r.. | grey text, grey outline, line height 3.9% (about 75px) | pop / fade out | — |
| 32.50–32.60s | subtitle | ack to Casino ⏎ //api.uber.com/v1/r. | grey text, line height 3.3% (about 64px) | hard in / hard out | — |
| 33.00–35.10s | subtitle | POST:bp | grey text, line height 2.1% (about 41px) | pop / hard out | — |
| 33.00–35.10s | subtitle | ge Calculator | white text, line height 2.4% (about 46px) | type-on | — |
| 33.00–35.70s | subtitle | FlexWins on Socials | white text, line height 2.7% (about 52px) | fade in / hard out | — |
| 35.20–35.70s | subtitle | als | grey text, grey outline, bold, line height 1.5% (about 28px) | hard out | — |
| 37.40–37.70s | text label | YOU ARE | white text, grey outline, bold, line height 3.6% (about 69px) | hard in / hard out | — |
| 37.50–38.70s | text label | Lowball Algorithm | grey text, keywords highlighted in black, line height 2.5% (about 48px) | hard out | — |
| 38.00–38.40s | text label | SPORTS | white text, blue outline, bold, line height 3.4% (about 65px) | hard in / hard out | — |
| 38.50–38.60s | text label | Fla | grey text, grey outline, line height 1.7% (about 33px) | hard in / hard out | — |
| 38.50–38.60s | text label | Itemfilter | grey text, line height 1.9% (about 37px) | hard in / hard out | — |
| 38.50–38.60s | text label | Data Normalizer | grey text, keywords highlighted in grey, line height 1.9% (about 37px) | hard in / hard out | — |
| 38.80–39.20s | text label | TO MY | white text, grey outline, bold, line height 3.6% (about 69px) | hard in / hard out | — |
| 39.00–39.10s | text label | Messag | grey text, line height 1.6% (about 31px) | hard in / hard out | — |
| 39.00–39.10s | text label | FlawDetection | grey text, keywords highlighted in grey, line height 2.1% (about 41px) | hard in / hard out | — |
| 39.00–39.10s | text label | Lowball Algorithm | grey text, line height 2.3% (about 45px) | hard in / hard out | — |
| 39.00–39.10s | text label | Item filter | grey text, line height 1.9% (about 37px) | hard in / hard out | — |
| 39.00–39.10s | text label | Data Normalizer | grey text, keywords highlighted in grey, line height 1.7% (about 33px) | hard in / hard out | — |
| 39.50–39.60s | text label | 二 | green text, grey box, bold, line height 2.2% (about 42px) | hard in / hard out | — |
| 39.50–39.60s | subtitle | place scraper | grey text, line height 1.5% (about 28px) | hard in / hard out | — |
| 39.50–39.90s | text label | FACEBOOK | white text, grey outline, bold, line height 3.0% (about 59px) | hard in / hard out | — |
| 39.90–40.30s | text label | MARKETPLACE | white text, grey outline, bold, line height 3.0% (about 59px) | hard in / hard out | — |
| 40.00–40.60s | subtitle | Data Normalizer | grey text, line height 1.5% (about 29px) | hard in | — |
| 40.50–41.30s | text label | AUTOMATION | white text, grey outline, bold, line height 3.0% (about 59px) | hard out | — |
| 40.90–41.20s | text label | Lowball Algorithm | grey text, line height 2.1% (about 41px) | hard in / hard out | — |
| 40.90–41.40s | text label | ormalizer | grey text, line height 1.6% (about 31px) | hard out | — |
| 41.00–41.10s | subtitle | sendMe | grey text, grey outline, line height 1.1% (about 21px) | hard in / hard out | — |
| 41.40–41.60s | text label | STRICTLY | white text, grey outline, bold, line height 3.3% (about 63px) | fade in / hard out | — |
| 41.50–43.70s | text label | 2015Harley-DavidsonSportster883 | black text, line height 2.4% (about 46px) | hard in / hard out (bounces / changes colour midway) | — |
| 41.50–43.70s | text label | Listed 19 daysago·Auburn,WA | white text, grey outline, keywords highlighted in grey, line height 2.0% (about 39px) | hard in / hard out (bounces / changes colour midway) | — |
| 41.50–41.60s | text label | Hi John,is thisstill available? | blue text, black outline, line height 2.1% (about 41px) | hard in / hard out | — |
| 41.50–43.70s | text label | Send | blue text, white outline, blue box, line height 2.1% (about 41px) | hard in / hard out (bounces / changes colour midway) | — |
| 41.50–43.10s | text label | W | black text, line height 2.5% (about 48px) | hard in (bounces / changes colour midway) | — |
| 41.50–43.10s | text label | e | white text, black outline, line height 2.1% (about 41px) | hard in (bounces / changes colour midway) | — |
| 41.50–43.60s | subtitle | S | black text, keywords highlighted in black, line height 2.6% (about 50px) | hard in / hard out (bounces / changes colour midway) | — |
| 41.50–42.40s | subtitle | K | black text, keywords highlighted in black, line height 2.7% (about 52px) | hard in / hard out | — |
| 41.50–43.60s | text label | a | white text, black outline, line height 2.2% (about 42px) | hard in / hard out (bounces / changes colour midway) | — |
| 41.50–41.60s | text label | H | grey text, keywords highlighted in black, line height 2.4% (about 46px) | hard in / hard out | — |
| 41.50–41.60s | text label | D | white text, black outline, bold, line height 2.4% (about 46px) | hard in / hard out | — |
| 41.60–42.10s | text label | LOWBALL | white text, grey outline, bold, line height 3.3% (about 63px) | hard in / hard out | — |
| 42.00–42.10s | text label | Paint is cooked ill | white text, black outline, line height 2.0% (about 39px) | hard in / hard out | — |
| 42.00–42.10s | subtitle | in | grey text, keywords highlighted in black, line height 1.5% (about 28px) | hard in / hard out | — |
| 42.00–43.10s | text label | U | white text, keywords highlighted in black, line height 1.8% (about 34px) |  (bounces / changes colour midway) | — |
| 42.10–42.60s | text label | 8.9Kmiles·Redmond | white text, line height 1.5% (about 28px) | hard out | — |
| 42.30–42.60s | text label | $4,900 ⏎ 2018Harley-DavidsonSportsterX.. | white text, black outline, line height 2.1% (about 41px) | type-on / hard out | — |
| 42.50–42.60s | text label | $5,299 $6,500 | white text, line height 2.3% (about 44px) | hard out | — |
| 42.50–42.60s | text label | 1.5Kmiles·Auburn | white text, keywords highlighted in grey, line height 1.6% (about 31px) | hard in / hard out | — |
| 42.50–42.60s | text label | 10.000 | white text, grey outline, bold, line height 3.7% (about 70px) | hard in / hard out | — |
| 42.60–43.20s | text label | HARLEYS | white text, grey outline, bold, line height 3.3% (about 63px) | pop / hard out | — |
| 43.00–43.70s | subtitle | 1 of 15 | white text, black box, line height 2.7% (about 53px) | hard in / hard out | — |
| 43.00–43.60s | text label | Sendselleramessage | white text, black outline, line height 2.2% (about 43px) | hard in | — |
| 43.00–43.10s | styled text | Have it cleaned upl | blue text, gradient, line height 2.3% (about 44px) | hard in / hard out | — |
| 43.00–43.10s | subtitle | "cleaned up" | white text, black outline, line height 2.7% (about 52px) | hard in / hard out | — |
| 43.00–43.10s | subtitle | upstairs | white text, black outline, line height 2.8% (about 54px) | hard in / hard out | — |

</details>

**Stickers / GIFs / picture-in-picture**

| Time | Kind | Position | Motion | Confidence | Crop |
|---|---|---|---|---|---|
| 8.40–12.40s | static sticker / image | x40% y86% w15% h6% | static | medium (unchanged across a cut) | ![sticker_01](packaging/sticker_01.jpg) |
| 20.30–26.10s | static sticker / image | x15% y69% w15% h9% | static | medium (unchanged across a cut) | ![sticker_02](packaging/sticker_02.jpg) |
| 26.30–31.10s | static sticker / image | x40% y86% w15% h9% | static | medium (unchanged across a cut) | ![sticker_03](packaging/sticker_03.jpg) |
| 43.90–49.50s | static sticker / image | x70% y77% w15% h9% | static | medium (unchanged across a cut) | ![sticker_04](packaging/sticker_04.jpg) |
| 52.60–55.90s | static sticker / image | x40% y86% w15% h9% | static | medium (unchanged across a cut) | ![sticker_05](packaging/sticker_05.jpg) |
| 56.10–63.80s | static sticker / image | x40% y86% w15% h9% | static | medium (unchanged across a cut) | ![sticker_06](packaging/sticker_06.jpg) |

| Time | Layer | Spoken line |
|---|---|---|
| 20.30s | static sticker / image | 0.7s after "Today 8:07 PM" |
| 43.00s | styled text "Have it cleane" | 0.0s into ""cleaned up"", on "cleanedup" |
| 43.10s | text label "$1000" | 0.2s before ""1000"", on "1000" |
| 43.90s | static sticker / image | 0.1s after ""1000"" |

- Remake: import `packaging/subtitles.srt` into your editor and replace the words; styled version in `packaging/overlays.ass`; find matching stickers and GIFs in an asset library

## Sound

**Voice**

- male-leaning
- Source: human recording
- Remake: record it yourself: phone or lavalier mic close to the mouth, in a quiet room; rewrite the lines from the script table

**Listen to the tracks**

- voice: [stems/vocals.wav](stems/vocals.wav)

<details class="ref"><summary>Sound measurements and evidence</summary>

![audio](audio.png)

- Loudness -17.1 dBFS, peak -1.2 dBFS
- sound runs across cuts, laid in post as one bed (background changes 4.1dB at cuts vs 4.3dB within shots)
- Voice on 57% of the duration, pitch about 123.5Hz
- Voice source: human recording (human recording 73%, TTS voice-over 20%, native dialogue from the AI video model 7%)
  - 74% of the picture is live footage: the voice is most likely location sound or a human voice-over

</details>

## Open questions

- Shot #1 (0.0–2.5s): live action at only 59% confidence, runner-up AI-generated video
- Shot #2 (2.5–3.8s): live action at only 53% confidence, runner-up AI-generated video
- Shot #3 (3.8–6.8s): code / template render at only 52% confidence, runner-up still image + pan/zoom
- Shot #5 (8.3–10.3s): live action at only 44% confidence, runner-up screen recording / screenshot
- Shot #6 (10.3–12.5s): live action at only 59% confidence, runner-up AI-generated video
- Shot #7 (12.5–16.1s): code / template render at only 56% confidence, runner-up still image + pan/zoom
- Shot #8 (16.1–18.2s): live action at only 50% confidence, runner-up AI-generated video
- Shot #12 (22.8–26.2s): live action at only 59% confidence, runner-up AI-generated video
- Shot #14 (28.5–31.2s): live action at only 50% confidence, runner-up AI-generated video
- Shot #16 (33.2–35.7s): code / template render at only 56% confidence, runner-up still image + pan/zoom
- Shot #17 (35.7–37.2s): code / template render at only 57% confidence, runner-up still image + pan/zoom
- Shot #20 (41.4–42.7s): live action at only 40% confidence, runner-up screen recording / screenshot
- Shot #21 (42.7–43.8s): live action at only 48% confidence, runner-up screen recording / screenshot
- Shot #23 (48.1–49.6s): live action at only 51% confidence, runner-up AI-generated video
- Shot #25 (51.5–52.5s): live action at only 59% confidence, runner-up AI-generated video
- No AI listened to the soundtrack (the review covered the picture only): real voice versus TTS is inferred from the waveform; the effects were found on the separated effects track and their types are estimated from the sound. Play the stems and each effect under “Sound” to check

# Part two · Remake plan

## Remake it yourself: do it in this order

Copy the method and the rhythm, not the pictures: keep what each part does and fill it with your own content and material.

This is a talking head. Do the steps in this order; the detail for each is in the matching subsection below. 26% of the time is a motion-graphics explainer; its steps are included.

1. **Write the content**: write yours in the same 17 steps as the original (narrative line under “Content and structure”)
2. **Collect material**: the real material in the picture (live footage) needs the original files, listed under “What to prepare”; one reference image per recurring character to lock appearance across shots: Presenter
3. **Shoot**: phone held vertical, mostly medium shot; light: soft frontal light (flat light) — a large source from the camera side, almost no shadow on the subject: facing a window, a ring light, or a big softbox behind the camera, 18-inch ring light or a diffused LED panel just behind and above the phone; grade: natural (close to the original colours) (setups under “Shoot”)
4. **Motion graphics**: have the agent make an editable first version and change the text and pictures on top of it rather than starting from scratch; the first version is only a start, where it differs from the original is under “Code build”
5. **Voice**: the original is human recording; record it yourself or use TTS; delivery per “Acting and emotion”
6. **Edit**: follow the order and lengths in the shot list; the original has 29 shots at 2.2s each; 2 transitions under “Edit”
7. **Subtitles and styled text**: import `packaging/subtitles.srt` and replace the words; timing and style under “Packaging layer”
8. **Put it together and compare**: hand the shots you made to the agent; it places them on the original timeline, keeps the original where yours are missing, and renders a side-by-side comparison with the original

### Shoot

Shoot every shot of one scene before moving to the next; within a scene, shoot the wider sizes first and the close-ups last so the lighting is set only once. Leave about 1s of handle at both ends of every take.

**S1**: shots #1, #2, #4–#6, #8, #10, #12–#14, #18–#29 (47.09s on screen); Office lounge: teal modular sofa, round wood coffee table, wood-panelled wall, g, Soft overhead light, cool daylight through glass
- Lighting: soft frontal light (flat light), key light frontal, warm (about 3000–4000K)
- Setup medium shot · fixed camera (tripod / mount / on the desk) · pan / track/static: shots #1, #2, #4, #6, #12, #20–#22, #25, #27, #28, 22.94s on screen, shoot about 44.9s
- Setup medium shot · moving camera (gimbal / handheld pan) · pan / track/pull-out/push-in/static: shots #5, #8, #10, #13, #14, #18, #19, #23, #24, #26, #29, 24.15s on screen, shoot about 46.1s

### Code build

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

<details class="ref"><summary>Motion #3 3.8–6.8s · 3 events</summary>

![#3 3.8–6.8s](shots/shot_003_strip.jpg)

- Ground #3a363c; other main colours #4b4a51 #5a5b65 #706c7e; drawn layer #677073 #827f96 #c1a8b2 #f4f8f8
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#3 3.8–6.8s](shots/shot_003_elements.jpg)

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

</details>

<details class="ref"><summary>Motion #7 12.5–16.1s · 2 events</summary>

![#7 12.5–16.1s](shots/shot_007_strip.jpg)

- Ground #3a363c; other main colours #69666d #525158 #444247 #837f89; drawn layer #746f78 #8c8ba1 #c4a4ad #f3f7f7
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#7 12.5–16.1s](shots/shot_007_elements.jpg)

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

</details>

<details class="ref"><summary>Motion #9 18.2–19.8s · 0 events</summary>

![#9 18.2–19.8s](shots/shot_009_strip.jpg)

- Ground #fdfcff; other main colours #e8e8ee #d4d1d8 #a4a2ae; drawn layer #babdcd #55b6fb #928d9e #5d535a
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#9 18.2–19.8s](shots/shot_009_elements.jpg)

- [crop L1](shots/shot_009_ly_01.jpg) [crop L2](shots/shot_009_ly_02.jpg) · Continuous layer: 14% of the frame moves through the whole shot (x 0%–89%, y 4%–68%), e.g. drifting gradients, particle flow, breathing glow

</details>

<details class="ref"><summary>Motion #11 20.2–22.8s · 5 events</summary>

![#11 20.2–22.8s](shots/shot_011_strip.jpg)

- Ground #fefcff; other main colours #39373c #4c4b52 #bebcc2 #69666d; drawn layer #fefcfe #423d42 #716b70 #f7722d
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#11 20.2–22.8s](shots/shot_011_elements.jpg)

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

</details>

<details class="ref"><summary>Motion #15 31.2–33.2s · 1 events</summary>

![#15 31.2–33.2s](shots/shot_015_strip.jpg)

- Ground #3a363c; other main colours #4b4a51 #5d5d65 #79727a; drawn layer #6d6973 #9292ac #ebeff2 #d28583
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#15 31.2–33.2s](shots/shot_015_elements.jpg)

- S1. never moves: shape / text block · x 44%–49%, y 11%–14% · #67666e · [crop](shots/shot_015_st_01.jpg)
- S2. never moves: shape / text block · x 78%–84%, y 15%–18% · #63636b · [crop](shots/shot_015_st_02.jpg)
- S3. never moves: shape / text block · x 42%–49%, y 22%–25% · #67676f · text “slack to Casino / ack to Casino” · [crop](shots/shot_015_st_03.jpg)
- S4. never moves: shape / text block · x 77%–84%, y 25%–28% · #64646c · [crop](shots/shot_015_st_04.jpg)
- [crop L1](shots/shot_015_ly_01.jpg) [crop L2](shots/shot_015_ly_02.jpg) · Continuous layer: 24% of the frame moves through the whole shot (x 0%–100%, y 0%–65%), e.g. drifting gradients, particle flow, breathing glow
1. 31.22–33.16s · middle (x 7%–84%, y 22%–57%) · changes, unfolds rightward (draw-on / grow / wipe), linear · #4a494e · text “Black to Casino / https://api.uber.com/v1/r.. / Bet365API” · [crop](shots/shot_015_el_01.jpg)

</details>

<details class="ref"><summary>Motion #16 33.2–35.7s · 0 events</summary>

![#16 33.2–35.7s](shots/shot_016_strip.jpg)

- Ground #3a373c; other main colours #4b494e #605f67 #78747a #978d93; drawn layer #777278 #ada2aa #e5e7ec #7a7bc2
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#16 33.2–35.7s](shots/shot_016_elements.jpg)

- [crop L1](shots/shot_016_ly_01.jpg) [crop L2](shots/shot_016_ly_02.jpg) · Continuous layer: 42% of the frame moves through the whole shot (x 0%–100%, y 0%–75%), e.g. drifting gradients, particle flow, breathing glow

</details>

<details class="ref"><summary>Motion #17 35.7–37.2s · 0 events</summary>

![#17 35.7–37.2s](shots/shot_017_strip.jpg)

- Ground #3a363c; other main colours #4a4950 #5a5863 #6d6a74 #8e838d; drawn layer #706d79 #a299a2 #7d7ac3 #e2e6ea
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#17 35.7–37.2s](shots/shot_017_elements.jpg)

- S1. never moves: shape / text block · x 33%–42%, y 0%–2% · #5c5d65 · [crop](shots/shot_017_st_01.jpg)
- S2. never moves: shape / text block · x 62%–67%, y 4%–5% · #5b5c63 · [crop](shots/shot_017_st_02.jpg)
- S3. never moves: shape / text block · x 51%–56%, y 6%–8% · #5b5a60 · [crop](shots/shot_017_st_03.jpg)
- S4. never moves: shape / text block · x 33%–47%, y 8%–14% · #67676e · [crop](shots/shot_017_st_04.jpg)
- S5. never moves: shape / text block · x 0%–8%, y 48%–50% · #59575f · [crop](shots/shot_017_st_05.jpg)
- [crop L1](shots/shot_017_ly_01.jpg) [crop L2](shots/shot_017_ly_02.jpg) · Continuous layer: 30% of the frame moves through the whole shot (x 0%–100%, y 0%–66%), e.g. drifting gradients, particle flow, breathing glow

</details>

### Acting and emotion

In a prompt, describe the visible expression and movement rather than words like “happy” or “sad”, and keep it smaller rather than bigger (strong emotion words tend to give mask faces and forced smiles); get the expression right in the first frame; for shots with lines, make the voice with its delivery first and let the picture act to it. For generated shots the Face and Movement below are already in the generation-unit prompts.

<details class="ref"><summary>all 22 shots</summary>

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

</details>

- **actor plays it**: Filmed: hand the face, movement and delivery to the actor as direction, and rehearse the pauses and tone against the original once

### Edit

- Cut in the order and lengths of the shot list
- Approach: Fast alternation between the presenter and inserts every 1 to 3 seconds. Three layouts rotate: presenter full frame, a split with the insert on top and the presenter below, and a full-frame graphic. Hard cuts only.
- Rhythm: 26.3 cuts per minute, 2.14s average live-action shot; 3 camera set-up(s) / location(s); 1 jump cut(s) and 0 punch-in(s) within the same set-up; inserts (screenshots / screen recordings / cards / stock) take 26%; 56% of cuts land in pauses of the speech; transitions cut×26, glitch transition×1, jump cut×1

**Transitions**

| Time | Into shot | Transition |
|---|---|---|
| 43.8–44.3s | #22 | glitch transition, 0.5s |

## Appendix

### Shot by shot

Each shot has two parts: what is visible on screen, and how the tools infer it was made (with the basis); remake prompts last. Folded by default.

<details class="ref"><summary>#1 00:00.000–00:02.461 · live action + code / editor overlays (subtitles); brings in real material (live footage)</summary>

![shot_001](shots/shot_001.jpg)

**Visible on screen** (check against the frames)
- Picture: Wide shot: a man sits on a teal sofa in an office lounge holding a laptop and talks to camera. A floating dark panel showing a large automation workflow sits above his head. Big italic white caption, one or two words at a time.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.1 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): JUST / MOST / WORKFLOW / SEE.
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 57%, AI-generated video 17%, 3D render 7% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Photographic texture: noise σ=0.37, 141 colours, 15% flat blocks
  - 83% of sampled frames show a frontal face on a fixed camera, voice on the audio track

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#2 00:02.461–00:03.837 · live action + code / editor overlays (subtitles); brings in real material (live footage)</summary>

![shot_002](shots/shot_002.jpg)

**Visible on screen** (check against the frames)
- Picture: Same wide shot, the workflow panel still floating above him as he names the automation. Captions pop word by word.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.1 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): HELL YEAH / SIMULATOR
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 52%, AI-generated video 21%, code / template render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - 68% of adjacent frames are exact duplicates, only local elements move (typical of template / motion-graphics animation, or a hold with local motion)
  - Photographic texture: noise σ=0.43, 137 colours, 14% flat blocks
  - 96% of background pixels never change frame to frame while local elements move: 2D compositing / code-driven motion graphics

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#3 00:03.837–00:06.798 · code / template render</summary>

![shot_003](shots/shot_003.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame motion graphic: the camera glides over a dark node canvas to a green clock node labelled Rise and Grind, connectors fanning out to the right. Caption in the lower third.
- Text track (text in the picture/bottom): Wait2
- Text track (text in the picture/middle): Rise and Grind / Beer&Cig / GET:https: / Beer & Cig
- Text track (text in the picture/middle): THISAUTOMATION / ALARM / AT645 / EVERY
- Motion beats within the shot: 4.34s
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small monospace labels
- [AI assistant review] Edges stay perfectly sharp while the whole canvas pans, with a synthetic depth blur on far nodes: drawn, not filmed
- [AI assistant review] No sensor noise or lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 50%, still image + pan/zoom 21%, screen recording / screenshot 20% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.11px residual, no local motion) → pan/zoom on a still image: zoom +0.1%/s, pan 12px/s
  - Rendered texture: 65% flat colour blocks, 95% of pixels use only 13 colours, 29% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#4 00:06.798–00:08.300 · live action + code / editor overlays (subtitles, styled text); brings in real material (live footage)</summary>

![shot_004](shots/shot_004.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: six workflow nodes labelled Instagram, TikTok, Twitter, Facebook, Threads, LinkedIn. Bottom half: the presenter, medium shot, talking.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); three-quarter key + fill (standard set-up); key light frame right, three-quarter front; lighting ratio about 1.4:1 (0.5 stops); soft light (wide lit-to-shadow ramp)
- Text track (subtitle/middle): POST:https:/backend.blotato..POST:https: / POT:https://backend.blotato..POST:https: / POST:https:/backend.blozat...POST:hp://b
- Text track (subtitle/middle): LINKEDIN1 / THREADS1 / FACEBOOK1 / ST:https://backend.blotat...PbsT:httpg./
- Text track (subtitle/middle): AUTOMATICALLY / "RISEAND GRIND
- Text track (title/top): INSTAGRAM1 / TIKTOK1 / TWITTER1
- Motion beats within the shot: 7.30s
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Whole frame moves as one rigid transform (99% inliers, 0.11px residual, no local motion) → pan/zoom on a still image: zoom -0.2%/s, pan 12px/s

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#5 00:08.300–00:10.344 · live action + code / editor overlays (subtitles, title, static sticker); brings in real material (live footage)</summary>

![shot_005](shots/shot_005.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: a social feed where one post reading Rise and Grind gets annoyed replies. Bottom half: the presenter delivering the line.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); backlit / background brighter than subject; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.1 stops); soft light (almost no lit / shadow edge)
- Text on objects in the scene (not subtitles): Nicole James·2h, PLEASESTOP, BrianMoore·2h, Hulk Hogan, 3h, @hulkhogan_reincarnated
- Text track (subtitle/middle): JakeWilson·2h / stop saying this / Sara Miller·2h / SHUT UP
- Text track (subtitle/middle): SaraMiller·2h / SHUT UP / Kyle Anderson·2h / Kyle Anderson · 2h
- Text track (subtitle/middle): Kyle Anderson· 2h / stop saying this / Nicole James·2h / Nicole James ·2h
- Text track (subtitle/middle): Nicole James·2h / PLEASESTOP / BrianMoore·2h / stop saying this
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 42%, screen recording / screenshot 26%, AI-generated video 12% (fused_agent)
- Material: the user's real material: live footage

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#6 00:10.344–00:12.471 · live action + code / editor overlays (subtitles, static sticker); brings in real material (live footage)</summary>

![shot_006](shots/shot_006.jpg)

**Visible on screen** (check against the frames)
- Picture: Wide shot of the presenter on the sofa, laptop on his knee, turning to the next item. Caption: ALSO,
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.3 stops); soft light (wide lit-to-shadow ramp)
- Text track (subtitle/middle): FIVE / AFTER / IS / IT
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 57%, AI-generated video 19%, 3D render 7% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Photographic texture: noise σ=0.19, 135 colours, 18% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#7 00:12.471–00:16.141 · code / template render</summary>

![shot_007](shots/shot_007.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas: a pink play node and a globe node labelled Play Man in the box, the view sliding along the connector. Caption: SPOTIFY.
- Text track (text in the picture/middle): Beer&Cig Farmer / GET:https://api.doordash.com. / Beer& Cig Farmer / Beer & Cig Farmer
- Text track (text in the picture/middle): Wait2 / Play Man in the box / GET:https://api.spotify.com/v... / GET:https://api.spotify.com/vi..
- Text track (text in the picture/middle): SPOTIFY / PLAY / IN THE BOX / ALICE
- Motion beats within the shot: 13.10s
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small monospace labels
- [AI assistant review] Edges stay perfectly sharp while the whole canvas pans, with a synthetic depth blur on far nodes: drawn, not filmed
- [AI assistant review] No sensor noise or lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 54%, still image + pan/zoom 24%, screen recording / screenshot 13% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.11px residual, no local motion) → pan/zoom on a still image: zoom -0.6%/s, pan 5px/s
  - Rendered texture: 56% flat colour blocks, 95% of pixels use only 23 colours, 28% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#8 00:16.141–00:18.227 · live action + code / editor overlays (subtitles); brings in real material (live footage)</summary>

![shot_008](shots/shot_008.jpg)

**Visible on screen** (check against the frames)
- Picture: Medium shot of the presenter gesturing with one hand as he explains the next automation.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.3:1 (0.3 stops); soft light (almost no lit / shadow edge)
- Text on objects in the scene (not subtitles): Hey man, just wanted to check in., We'vebeenconcerned aboutyou
- Text track (subtitle/middle): WILL / REPLY / EVERY / WITH
- Text track (subtitle/middle): iMessage / Today 8:07PM / Hey man, just wanted to check in.
- Text track (subtitle/middle): We'vebeenconcerned aboutyou / lately :I
- Text track (subtitle/middle): Can't talk,grinding / Read8:07PM
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 49%, AI-generated video 22%, 3D render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Photographic texture: noise σ=0.20, 136 colours, 17% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#9 00:18.227–00:19.770 · code / template render</summary>

![shot_009](shots/shot_009.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame white card: a phone message thread, tilted in 3D with soft blur at the edges. A grey bubble from a friend checking in, a blue reply saying Can't talk, grinding.
- Text on objects in the scene (not subtitles): Hey man, just wanted to check in., We'vebeenconcerned aboutyou
- Text track (text in the picture/middle): iMessage / Today 8:07PM / Hey man, just wanted to check in. / Today 8:07 PM
- Text track (text in the picture/middle): We'vebeen concerned about you / lately :/ / lately :I
- Text track (text in the picture/middle): Can't talk,grinding / Read8:07PM / Read 8:07 PM / Can't talk, grinding
- Text track (text in the picture/middle): TALK / GRINDING
- [AI assistant review] A rebuilt message thread on pure white, tilted in perspective with a synthetic depth blur
- [AI assistant review] Bubbles and avatar are flat vector shapes with no screen glare or moire
- [AI assistant review] Camera drift is a single rigid move

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 78%, screen recording / screenshot 8%, 3D render 3% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 84% flat colour blocks, 95% of pixels use only 3 colours, 15% axis-aligned edges
  - Nearly colourless frame (saturation 0.02) with only 3 colours: a flat UI / document picture, not a shaded 3D render

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#10 00:19.770–00:20.229 · live action + code / editor overlays (subtitles, text labels); brings in real material (live footage)</summary>

![shot_010](shots/shot_010.jpg)

**Visible on screen** (check against the frames)
- Picture: Very short medium shot of the presenter starting the next sentence. Caption: FIRST THING.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.0:1 (0.1 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/bottom): Beer & Cig Farmer / GET: https://api.doordash.com..
- Text track (text/middle): THIS WILL
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Whole frame moves as one rigid transform (95% inliers, 0.15px residual, no local motion) → pan/zoom on a still image: zoom +0.1%/s, pan 9px/s
  - Photographic texture: noise σ=0.15, 138 colours, 17% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#11 00:20.229–00:22.814 · code / template render + code / editor overlays (static sticker)</summary>

![shot_011](shots/shot_011.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame split graphic: on top a simple map with a red car driving up a grey road toward beer and cigarette icons; below it the workflow node Beer and Cig Farmer on the dark canvas.
- Text track (text in the picture/bottom): Beer & Cig Farmer / GET: https://api.doordash.com.. / GET: https://api.doordash.com... / GET:https://api.doordash.com..
- Text track (text in the picture/middle): DOORDASH / BEER / CIGARETS / TO
- Text track (text in the picture/top): 2
- [AI assistant review] Flat illustrated map: grey roads, an orange arrow and a red car icon moving along a path
- [AI assistant review] Lower half is the same vector workflow canvas as earlier shots
- [AI assistant review] No photographic texture anywhere in the frame

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 70%, 3D render 10%, screen recording / screenshot 8% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 59% flat colour blocks, 95% of pixels use only 28 colours, 33% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#12 00:22.814–00:26.193 · live action + code / editor overlays (subtitles, text labels, static sticker); brings in real material (live footage)</summary>

![shot_012](shots/shot_012.jpg)

**Visible on screen** (check against the frames)
- Picture: Wide shot of the presenter on the sofa continuing the list.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.3 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): AUTOMATICALLY / TIME / WHEN / CIGARETS
- Text track (subtitle/middle): Nait / UberBlack to Casino / Wait / GET:https://api.uber.com/v1/r.
- Text track (text/middle): API
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 57%, AI-generated video 19%, 3D render 7% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Photographic texture: noise σ=0.20, 135 colours, 17% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#13 00:26.193–00:28.529 · live action + code / editor overlays (subtitles, text labels, static graphics, static sticker); brings in real material (live footage)</summary>

![shot_013](shots/shot_013.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: workflow nodes labelled Uber Black to Casino and Bet365 API. Bottom half: the presenter, medium shot.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.3 stops); soft light (wide lit-to-shadow ramp)
- Text track (subtitle/middle): lait / Uber Black to Casino / Wait / GET:https://api.uber.com/v1/r..
- Text track (subtitle/middle): ORDERS / UBER / TO THE / CASINO.
- Text track (text/middle): DURING
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#14 00:28.529–00:31.156 · live action + code / editor overlays (subtitles, static sticker); brings in real material (live footage)</summary>

![shot_014](shots/shot_014.jpg)

**Visible on screen** (check against the frames)
- Picture: Wide shot of the presenter, hand raised mid-gesture.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): TO THE. / CASINO, / DIFFERENT / WILL
- Text track (subtitle/middle): ber Black to Casino / GET:https://api.uber.com/v1/r..
- Text track (subtitle/middle): Bet365API / Arbitrage Calculator / GET:https://api.bet365.com
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 49%, AI-generated video 22%, 3D render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Photographic texture: noise σ=0.21, 135 colours, 17% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#15 00:31.156–00:33.242 · code / template render</summary>

![shot_015](shots/shot_015.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas pushing in on a Bet365 API node feeding an orange code node labelled Arbitrage Calculator.
- Text track (text in the picture/middle): Black to Casino / https://api.uber.com/v1/r.. / slack to Casino / ack to Casino
- Text track (text in the picture/middle): Bet365API / Arbitrage Calculator / GET:https://api.bet365.com / Flex
- Text track (text in the picture/middle): THE SPORTS / BETTING / ARBITRAGE. / ANY TIME
- Text track (text in the picture/middle): POST:btp
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small monospace labels
- [AI assistant review] Edges stay perfectly sharp while the whole canvas pans, with a synthetic depth blur on far nodes: drawn, not filmed
- [AI assistant review] No sensor noise or lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 70%, 3D render 12%, screen recording / screenshot 6% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 65% flat colour blocks, 95% of pixels use only 14 colours, 35% axis-aligned edges
  - Per-frame sharpness oscillates periodically (period 2 frames, correlation 0.86) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#16 00:33.242–00:35.744 · code / template render</summary>

![shot_016](shots/shot_016.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas: a Flex Wins on Socials node with connectors fanning out to several posts, a soft light sweep across the top.
- Text track (text in the picture/middle): POST:bp / POST:btp / POST:htp / INSTAGRAM
- Text track (text in the picture/middle): ageCalculator / FlexWins on Socials / GET:https://api.stocktwits.c... / ge Calculator
- Text track (text in the picture/middle): YOU / BETTING / WIN / WILLSEND
- Text track (text in the picture/top): hister Delivery Book All Available Slot / apl.doordash..com...GET:https:/lapi.rang
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small monospace labels
- [AI assistant review] Edges stay perfectly sharp while the whole canvas pans, with a synthetic depth blur on far nodes: drawn, not filmed
- [AI assistant review] No sensor noise or lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 54%, still image + pan/zoom 23%, screen recording / screenshot 13% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.12px residual, no local motion) → pan/zoom on a still image: zoom +2.2%/s, pan 11px/s
  - Rendered texture: 47% flat colour blocks, 95% of pixels use only 25 colours, 26% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#17 00:35.744–00:37.162 · code / template render</summary>

![shot_017](shots/shot_017.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas with the six social platform nodes again, wider. Caption: SOCIAL.
- Text track (text in the picture/middle): INSTAGRAM / TIKTOK / TWITTER
- Text track (text in the picture/middle): LINKEDIN / THREADS / FACEBOOK / MEDIA
- Text track (text in the picture/top): Delivery / BookAll Available Slots / n...GET:https:lapi.rangeb / Book All Available Slots
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small monospace labels
- [AI assistant review] Edges stay perfectly sharp while the whole canvas pans, with a synthetic depth blur on far nodes: drawn, not filmed
- [AI assistant review] No sensor noise or lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 55%, still image + pan/zoom 21%, screen recording / screenshot 13% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.17px residual, no local motion) → pan/zoom on a still image: zoom -1.2%/s, pan 18px/s
  - Rendered texture: 55% flat colour blocks, 95% of pixels use only 19 colours, 19% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#18 00:37.162–00:38.705 · live action + code / editor overlays (subtitles); brings in real material (live footage)</summary>

![shot_018](shots/shot_018.jpg)

**Visible on screen** (check against the frames)
- Picture: Medium shot of the presenter leaning into the next point.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); three-quarter key + fill (standard set-up); key light frame right, three-quarter front; lighting ratio about 1.6:1 (0.6 stops); soft light (wide lit-to-shadow ramp)
- Text track (subtitle/middle): YOU ARE / SPORTS
- Text track (subtitle/middle): Deal Analyzer / RelentlessNegotiation / TWITTER1 / Follow-up Nukpportunity Recalculator CRN
- Text track (title/top): Fla / Itemfilter / Lowball Algorithm / FBMarketplace scraper
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Photographic texture: noise σ=0.20, 136 colours, 17% flat blocks
  - Duplicate frames follow a 24→30 pattern (19%, period 4): a 24/25fps source transcoded up, typical of AI-generated video, 3D / animation renders or cinema footage

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#19 00:38.705–00:41.375 · live action + code / editor overlays (subtitles, static graphics); brings in real material (live footage)</summary>

![shot_019](shots/shot_019.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: a long row of workflow nodes for a marketplace scraper and negotiation engine. Bottom half: the presenter.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.1 stops); soft light (almost no lit / shadow edge)
- Text on objects in the scene (not subtitles): Deal Analyzer, Relentless Negotiation, Follow-upNukapportunity Recalculator CRM Integration, Deal Alert, sendMe
- Text track (subtitle/middle): Deal Analyzer / Relentless Negotiation / Follow-upNukapportunity Recalculator CRM / Engine
- Text track (subtitle/middle): TO MY / FACEBOOK / MARKETPLACE / AUTOMATION
- Text track (subtitle/middle): Deal Alert / sendMe
- Text track (title/top): Messag / Lowball Algorithm / FlawDetection / Data Normalizer
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Per-frame sharpness oscillates periodically (period 6 frames, correlation 0.09) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#20 00:41.375–00:42.709 · live action + code / editor overlays (subtitles, text labels, title, static graphics); brings in real material (live footage)</summary>

![shot_020](shots/shot_020.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: a marketplace grid of used motorcycles, then one listing opening with a message box where a lowball offer is typed on the phone keyboard. Bottom half: the presenter.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); backlit / background brighter than subject; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.3:1 (0.3 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): Hi John,is thisstill available? / Send / Paint is cooked ill / $5,299 $6,500
- Text track (subtitle/middle): W / E / R / P
- Text track (subtitle/middle): A / S / D / H
- Text track (subtitle/middle): STRICTLY / LOWBALL / 10.000
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 38%, screen recording / screenshot 17%, AI-generated video 14% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 31% flat colour blocks, 95% of pixels use only 96 colours, 40% axis-aligned edges
  - Per-frame sharpness oscillates periodically (period 2 frames, correlation 0.32) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI
  - 83% of sampled frames show a frontal face on a fixed camera, voice on the audio track

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#21 00:42.709–00:43.794 · live action + code / editor overlays (subtitles, title, static graphics, styled text); brings in real material (live footage)</summary>

![shot_021](shots/shot_021.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: more motorcycle listings scrolling. Bottom half: the presenter. Caption: 10,000.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); backlit / background brighter than subject; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.3:1 (0.3 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): Have it cleaned upl / Send / Have it cleaned up for me tonight I'll t / $1000
- Text track (subtitle/middle): "cleaned up" / upstairs / "1000"
- Text track (subtitle/middle): W / e / t / U
- Text track (subtitle/middle): a / S
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 46%, screen recording / screenshot 14%, AI-generated video 12% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 31% flat colour blocks, 95% of pixels use only 98 colours, 39% axis-aligned edges
  - 83% of sampled frames show a frontal face on a fixed camera, voice on the audio track

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#22 00:43.794–00:48.090 · live action + code / editor overlays (subtitles, text labels, static graphics, static sticker); brings in real material (live footage)</summary>

![shot_022](shots/shot_022.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: the listings give way to a workflow node labelled Tinder API. Bottom half: the presenter keeps talking through several captions.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); three-quarter key + fill (standard set-up); key light frame right, three-quarter front; lighting ratio about 1.4:1 (0.4 stops); soft light (wide lit-to-shadow ramp)
- Text on objects in the scene (not subtitles): Tinder APi, GET:https://www.tinder.com/api
- Text track (subtitle/middle): Tinder APi / GET:https://www.tinder.com/api
- Text track (subtitle/middle): THIS / AUTOMATICALLY / SWIPE / ON
- Text track (text/middle): EVERY
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Whole frame moves as one rigid transform (95% inliers, 0.10px residual, no local motion) → pan/zoom on a still image: zoom +0.1%/s, pan 9px/s

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#23 00:48.090–00:49.633 · live action + code / editor overlays (subtitles, text labels, static sticker); brings in real material (live footage)</summary>

![shot_023](shots/shot_023.jpg)

**Visible on screen** (check against the frames)
- Picture: Wide shot of the presenter on the sofa. Caption: EVERY.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): LUNCH / DINNER
- Text track (subtitle/middle): Wait3 / Steak & Monster Delivery / GET:https//api.doordash.com..
- Text track (text/middle): WILL
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 49%, AI-generated video 22%, 3D render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Photographic texture: noise σ=0.21, 136 colours, 17% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#24 00:49.633–00:51.510 · live action + code / editor overlays (subtitles, text labels, static graphics); brings in real material (live footage)</summary>

![shot_024](shots/shot_024.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: workflow nodes labelled Steak and Monster Delivery. Bottom half: the presenter.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): Wait3 / Steak & Monster Delivery / GET:https://api.doordash.com.. / GET:https://api.doordash.com...
- Text track (subtitle/middle): STEAK / WHITE / MONSTER.
- Text track (text/middle): Ⅱ
- Text track (text/middle): WE HAVE A CHAT
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Per-frame sharpness oscillates periodically (period 6 frames, correlation 0.56) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#25 00:51.510–00:52.469 · live action + code / editor overlays (text labels); brings in real material (live footage)</summary>

![shot_025](shots/shot_025.jpg)

**Visible on screen** (check against the frames)
- Picture: Short medium shot of the presenter. Caption: WE HAVE A CHAT.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); three-quarter key + fill (standard set-up); key light frame right, three-quarter front; lighting ratio about 1.4:1 (0.5 stops); soft light (wide lit-to-shadow ramp)
- Text track (text/middle): BOT
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 57%, AI-generated video 19%, 3D render 7% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Photographic texture: noise σ=0.20, 140 colours, 16% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#26 00:52.469–00:55.138 · live action + code / editor overlays (subtitles, text labels, static graphics, static sticker); brings in real material (live footage)</summary>

![shot_026](shots/shot_026.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: workflow nodes Find Facebook Group, Filter Recent Discussions, Send WhatsApp. Bottom half: the presenter.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); three-quarter key + fill (standard set-up); key light frame right, three-quarter front; lighting ratio about 1.5:1 (0.6 stops); soft light (wide lit-to-shadow ramp)
- Text on objects in the scene (not subtitles): Find Facebook Group  Filter Recent Discussions, SendWhatsA, message:s
- Text track (subtitle/middle): Find Facebook Group  Filter Recent Discu / SendWhatsA / message:s / Send WhatsAppA
- Text track (subtitle/middle): AUTOMATICALLY / ARGUE / PEOPLE / LOCAL
- Text track (text/middle): f
- Text track (text/middle): FINALLY
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Per-frame sharpness oscillates periodically (period 6 frames, correlation 0.12) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#27 00:55.138–00:55.973 · live action + code / editor overlays (text labels, static sticker); brings in real material (live footage)</summary>

![shot_027](shots/shot_027.jpg)

**Visible on screen** (check against the frames)
- Picture: Short medium shot of the presenter. Caption: FINALLY,
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); three-quarter key + fill (standard set-up); key light frame right, three-quarter front; lighting ratio about 1.4:1 (0.5 stops); unclear
- Text track (text/middle): THE
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Whole frame moves as one rigid transform (93% inliers, 0.16px residual, no local motion) → pan/zoom on a still image: zoom +0.0%/s, pan 3px/s
  - Photographic texture: noise σ=0.20, 136 colours, 17% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#28 00:55.973–00:59.560 · live action + code / editor overlays (subtitles, text labels, title, static graphics, static sticker); brings in real material (live footage)</summary>

![shot_028](shots/shot_028.jpg)

**Visible on screen** (check against the frames)
- Picture: Top half: a larger workflow labelled Search eBay Deals, Find Profitable Items, Item Lists, Log Transaction. Bottom half: the presenter. Caption: FLIPPER.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.3:1 (0.3 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): ItemLists / Get Item Details / ListItemforSale / LogTransaction
- Text track (subtitle/middle): FLIPPER / BOT, / BUY / BULK
- Text track (text/middle): I'LL MAKE
- Text track (title/top): SearcheBayDealsFindProfitableItems / GET:https://svcs.ebay.com/se. / GET:https://svcs.ebay.com/se...
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Frame is a two-part composite: an inserted graphic or screenshot fills the top half, the filmed presenter stays on the bottom half
- [AI assistant review] The top panel has hard straight edges and no shared lighting with the room

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Whole frame moves as one rigid transform (95% inliers, 0.13px residual, no local motion) → pan/zoom on a still image: zoom +0.5%/s, pan 3px/s

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#29 00:59.560–01:03.856 · live action + code / editor overlays (subtitles, static graphics, static sticker); brings in real material (live footage)</summary>

![shot_029](shots/shot_029.jpg)

**Visible on screen** (check against the frames)
- Picture: Medium shot of the presenter delivering the closing line to camera.
- Acting: deadpan (light) · neutral brows, eyes to camera, mouth relaxed between phrases
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.3 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): THIS / SOON / AUTOMATION, / JUST
- [AI assistant review] The same man, grey tee, blue shorts, wristwatch, teal sofa and wood-panelled office appear in every filmed shot, consistent across the whole minute
- [AI assistant review] Natural hand gestures and head turns with real motion blur; no warping of fingers, watch or laptop
- [AI assistant review] Background glass wall, ceiling lights and plant stay geometrically stable from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter. On split shots the insert on the top half is an overlay; the base picture is the filmed presenter.
  - Photographic texture: noise σ=0.21, 137 colours, 16% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

### Metadata clues

- Encoder: `Lavf62.12.100`

### Notes

- Deterministic forensics is reliable on motion, whole-frame pan/zoom, rendered texture and 24→30 fps conversion; telling live action from AI from 3D needs image reading (a VLM or an AI assistant's review), and a look at the frames yourself.
- Platform transcoding usually strips metadata; missing metadata proves nothing.
- The full data is in `breakdown.json`; the package for models starts at `VIDEO.md`.

---

Made with [REA-VIDEO](https://github.com/JuneYaooo/rea-video) · https://github.com/JuneYaooo/rea-video
