# How this video was made: marketplace-bot.mp4

**In one line**: A deadpan explainer of a bot that lowballs marketplace sellers at scale, where every step is a node of one workflow diagram and every joke lands as a real-looking chat.
**How it was made**: Mixed production: live action 52% + code / template render 45% + screen recording / screenshot 4%

- 0:52 · vertical 9:16 · 27 shots, 1.9s each on average
- Confidence 64%, based on: tool measurements + AI assistant reviewed 27 shots + user corrections
- ⚠️ 17 points are uncertain, see “Open questions”

![storyboard](storyboard.jpg)

# Part one · Breakdown: how this video is built

## What makes it work

- **The hook**: 0 to 3.7 s: the claim starts over the presenter with the finished workflow above his head, then three phone captures of listings being messaged flash by in two seconds. The viewer sees it working befo
- Proof in the first 4 s: three listings are messaged on screen (1.7 to 3.7 s) before any explanation
- From 5 to 22 s the cut is a strict alternation: presenter, diagram, presenter, diagram, about 2 s each, so the picture changes on every sentence
- The jokes are delivered as chats, not lines (22.8 to 36.5 s): a stacked layout keeps the diagram below while the chat types on top
- The last shot is 9 s of the presenter, four times longer than any other, for the verdict and the offer

## Production pipeline at a glance

| Stage | What this video uses | Remake approach |
|---|---|---|
| **Base picture** | live action 14 shots (52%), code / template render 10 shots (45%), screen recording / screenshot 3 shots (4%); includes real material in 21 shots (76%) | filmed in 1 scene; screen recording / motion graphics in code |
| **Packaging** | 7 subtitle lines (bottom/middle, up to 2 rows): grey text, line height 2.6%; entrance: hard in×5, slide in×1, fade in×1; text label ×57: "AUTOMATION", "SENDS", "10,000", "Alerts", "Message", "Share" …; Stickers / GIFs: animated sticker / GIF ×1, static sticker / image ×3; Placed by spoken line ×3 (with new wording they follow the line, not the old second): static sticker / image → 0.1s after "Flaw Detection", static sticker / image → 0.1s after "Flaw Detection", static sticker / image → 0.6s after "Flaw Detection"; 4 persistent layers (unchanged across cuts: lay each on once for its span, not per shot): animated sticker / GIF 0.1–2.4s, static sticker / image 26.4–30.6s, static sticker / image 26.4–30.6s, static sticker / image 26.9–31.5s | export `packaging/subtitles.srt` for timeline alignment |
| **Sound** | voice（human recording） | voice: record it yourself |

## Content and structure

- The narrative line below comes from reading each shot; the lines were not transcribed separately, subtitle text is under “Packaging layer”

**Narrative line**

Keep this line in a remake: same order, same job at each step, with the point refilled from your own cases, numbers and material, so it is more than a change of subject.

| Time | Shots | Job | What it says |
|---|---|---|---|
| 0.0–3.7s | #1–#4 | grab attention | Open on the finished system in frame while he starts the claim → Show the automation doing the thing in the first two seconds → A fast second example to imply volume → A third example in under a second |
| 3.7–6.5s | #5–#7 | set the scene | Return to the presenter to state the scale → Presenter starts the explanation → Plain presenter line before the first diagram |
| 6.5–21.2s | #8–#14 | add information | Show the first step of the system as a moving diagram → Presenter carries the line between diagrams → Next step as the next part of the same diagram → Presenter explains the choice the viewer gets → Name the key step with its node on screen → (… 7 points, each shot in the shot list) |
| 21.2–22.8s | #15 | turn | Presenter sets up the example |
| 22.8–26.3s | #16, #17 | show evidence | Put a real-looking listing next to the step that handles it → Show the joke result as a chat |
| 26.3–26.8s | #18 | turn | A half-second reset to the presenter |
| 26.8–30.7s | #19 | show evidence | Escalate the joke in the chat while naming the next node |
| 30.7–33.0s | #20, #21 | add information | Presenter reacts → Presenter introduces the follow-up step |
| 33.0–36.5s | #22 | show evidence | Pay off the follow-up step with the chat |
| 36.5–37.0s | #23 | turn | A half-second reset |
| 37.0–43.2s | #24–#26 | add information | Show where the results go → Presenter explains the last step → Last branch of the diagram |
| 43.2–52.4s | #27 | call to action | Close on the presenter with the verdict and the offer |

## Shot list

| # | Frame | Time | What it says | Picture | Camera | Made with |
|---|---|---|---|---|---|---|
| 1 | ![#1](shots/shot_001_first.jpg) | 0:00.0 · 1.7s | grab attention: Open on the finished system in frame while h… | Presenter seated at a desk in a dark room, a teal light tube… | smooth move | live action |
| 2 | ![#2](shots/shot_002_first.jpg) | 0:01.7 · 0.8s | grab attention: Show the automation doing the thing in the f… | Full-frame grey card with a phone screen: a marketplace list… | smooth move | screen recording / screenshot |
| 3 | ![#3](shots/shot_003_first.jpg) | 0:02.5 · 0.4s | grab attention: A fast second example to imply volume | Same card: a grid of marketplace car listings, very short. | smooth move | screen recording / screenshot |
| 4 | ![#4](shots/shot_004_first.jpg) | 0:02.9 · 0.8s | grab attention: A third example in under a second | Same card: another car listing with the message box prefille… | smooth move | screen recording / screenshot |
| 5 | ![#5](shots/shot_005_first.jpg) | 0:03.7 · 0.6s | set the scene: Return to the presenter to state the scale | Back to the presenter with the workflow panel floating above… | smooth move | live action |
| 6 | ![#6](shots/shot_006_first.jpg) | 0:04.2 · 1.0s | set the scene: Presenter starts the explanation | Same framing, the presenter gesturing with both hands. Capti… | smooth move | live action |
| 7 | ![#7](shots/shot_007_first.jpg) | 0:05.2 · 1.2s | set the scene: Plain presenter line before the first diagram | Presenter at the desk, no panel, hand on the mouse. | smooth move | live action |
| 8 | ![#8](shots/shot_008_first.jpg) | 0:06.5 · 2.1s | add information: Show the first step of the system as a movi… | Full-frame workflow canvas: a Start node, a Facebook Marketp… | whole-frame zoom / pan | code / template render |
| 9 | ![#9](shots/shot_009_first.jpg) | 0:08.6 · 1.9s | add information: Presenter carries the line between diagrams | Presenter at the desk, looking at camera. | smooth move | live action |
| 10 | ![#10](shots/shot_010_first.jpg) | 0:10.5 · 1.8s | add information: Next step as the next part of the same diag… | Full-frame workflow canvas: Data Normalizer, Item filter and… | whole-frame zoom / pan | code / template render |
| 11 | ![#11](shots/shot_011_first.jpg) | 0:12.3 · 3.1s | add information: Presenter explains the choice the viewer ge… | Presenter at the desk, one hand raised. | smooth move | live action |
| 12 | ![#12](shots/shot_012_first.jpg) | 0:15.5 · 2.1s | add information: Name the key step with its node on screen | Full-frame workflow canvas pushing toward the Lowball Algori… | whole-frame zoom / pan | code / template render |
| 13 | ![#13](shots/shot_013_first.jpg) | 0:17.5 · 2.0s | add information: Presenter bridges to the next step | Presenter at the desk. | smooth move | live action |
| 14 | ![#14](shots/shot_014_first.jpg) | 0:19.5 · 1.7s | add information: Show the branch that sends the messages | Full-frame workflow canvas: Lowball Algorithm, Flaw Detectio… | whole-frame zoom / pan | code / template render |
| 15 | ![#15](shots/shot_015_first.jpg) | 0:21.2 · 1.5s | turn: Presenter sets up the example | Presenter at the desk, hand sweeping across. | static (subject moves) | live action |
| 16 | ![#16](shots/shot_016_first.jpg) | 0:22.8 · 1.7s | show evidence: Put a real-looking listing next to the step t… | Top: a marketplace listing for a pickup truck. Bottom: the w… | static | code / template render |
| 17 | ![#17](shots/shot_017_first.jpg) | 0:24.4 · 1.9s | show evidence: Show the joke result as a chat | Top: a chat with the seller where lowball messages are being… | static | code / template render |
| 18 | ![#18](shots/shot_018_first.jpg) | 0:26.3 · 0.5s | turn: A half-second reset to the presenter | Very short presenter shot. Caption: THEN IT | smooth move | live action |
| 19 | ![#19](shots/shot_019_first.jpg) | 0:26.8 · 3.8s | show evidence: Escalate the joke in the chat while naming th… | Top: the chat continues, the seller replying in annoyance. B… | static | code / template render |
| 20 | ![#20](shots/shot_020_first.jpg) | 0:30.7 · 1.0s | add information: Presenter reacts | Presenter at the desk, smiling slightly. | smooth move | live action |
| 21 | ![#21](shots/shot_021_first.jpg) | 0:31.6 · 1.4s | add information: Presenter introduces the follow-up step | Presenter at the desk. | smooth move | live action |
| 22 | ![#22](shots/shot_022_first.jpg) | 0:33.0 · 3.4s | show evidence: Pay off the follow-up step with the chat | Top: a long chat where the bot keeps messaging after being t… | smooth move | code / template render |
| 23 | ![#23](shots/shot_023_first.jpg) | 0:36.5 · 0.5s | turn: A half-second reset | Very short presenter shot. Caption: UPS. | smooth move | live action |
| 24 | ![#24](shots/shot_024_first.jpg) | 0:37.0 · 1.2s | add information: Show where the results go | Full-frame workflow canvas: Opportunity Recalculator and CRM… | whole-frame zoom / pan | code / template render |
| 25 | ![#25](shots/shot_025_first.jpg) | 0:38.2 · 1.4s | add information: Presenter explains the last step | Presenter at the desk. | smooth move | live action |
| 26 | ![#26](shots/shot_026_first.jpg) | 0:39.6 · 3.6s | add information: Last branch of the diagram | Full-frame workflow canvas: Value Calculator and deal nodes … | smooth move | code / template render |
| 27 | ![#27](shots/shot_027_first.jpg) | 0:43.2 · 9.2s | call to action: Close on the presenter with the verdict and … | Presenter at the desk for the closing lines, the longest sho… | smooth move | live action |

## Cast, scenes and props

- **Visual style**: Filmed presenter in a dark room with a teal practical, cut with flat vector workflow diagrams on a dark dotted canvas and phone app captures on a grey card. Bold condensed white captions.

| Id | Name | Kind | Look | Role | Voice | Shots |
|---|---|---|---|---|---|---|
| A | Presenter | person | Man in his twenties, wavy brown hair, short beard, olive tee, wristwatch, seated in a mesh office chair | Narrator, on camera | — | #1, #5–#7, #9, #11, #13, #15, #18, #20, #21, #23, #25, #27 |

- Character consistency: Presenter appear across multiple shots; lock an anchor image first and feed it as reference in later shots

**Scenes**

| Scene | Where | When | Set / light | Shots |
|---|---|---|---|---|
| S1 | Desk in a dark room, mesh chair, white desk, vertical teal LED tube behind | Night look, interior | Low key with a teal accent | #1, #5–#7, #9, #11, #13, #15, #18, #20, #21, #23, #25, #27 |

**Props / products / logos**

- Workflow diagram (shots #1, #5, #6, #8, #10, #12, #14, #16, #17, #19, #22, #24, #26): The recurring automation canvas: floating panel, full frame, and the lower panel of the stacked shots
- Phone captures (shots #2–#4, #16, #17, #19, #22): Marketplace listings and chats

## Camera and lighting

- Framing: shot size medium shot 98%, medium close-up 2%; subject is a face (shot size from face height)
- Camera: moving camera (gimbal / handheld pan) 94%, fixed camera (tripod / mount / on the desk) 6%; typical move push-in
- Lighting: Dark room. A soft key from the front, a vertical teal LED tube behind him as the only practical, which also rims his hair and shoulder. (image reading; pixel measurements in the fold below)
- Grade: natural (close to the original colours); high saturation, normal contrast, normal blacks, overall cool
- Format: talking head (face as subject 100%, objects / hands as subject 0%, handheld 94%); image readers: Scripted talking-head explainer with workflow graphics and phone screen recordings

<details class="ref"><summary>Per-item measurements and image readings (11)</summary>

| Aspect | Item | Verdict | Sources |
|---|---|---|---|
| Framing | shot size | medium shot | measured |
| Camera | camera support | moving camera (gimbal / handheld pan) | measured |
| Camera | set-ups / locations | One set-up: the presenter at a desk, turned three-quarters to a camera at seated eye level. Looks like a tripod; every presenter shot has the same framing. | agent review |
| Camera | likely gear | Mirrorless camera or phone on a tripod. A guess from the fixed framing and the soft background. | agent review |
| Lighting | soft / hard | soft light (almost no lit / shadow edge) | measured |
| Lighting | colour temperature | neutral (about 5000K) | measured |
| Lighting | overall lighting | Dark room. A soft key from the front, a vertical teal LED tube behind him as the only practical, which also rims his hair and shoulder. | agent review |
| Grade | colour grade | natural (close to the original colours) | measured |
| Grade | overall grade | Dark and cool: deep blacks, teal accent from the tube, natural skin. | agent review |
| Editing | editing style | Hook is three phone captures in two seconds. Then the presenter alternates with full-frame workflow graphics every 1 to 2 seconds; proof arrives as stacked panels (a chat on top, the diagram below). Hard cuts only. | agent review |
| Format | video format | Scripted talking-head explainer with workflow graphics and phone screen recordings | measured: talking head; agent review |

- Note: lighting ratio, soft / hard, colour temperature and shot size are measured on the subject's pixels (the face when there is one, otherwise the in-focus region, which is an estimate); platform transcodes crush the shadows, so hardness and fill read conservative; camera angle, light source, catchlight and rim light follow the image readers. Where measurement and readers disagree, both are listed.

</details>

## Packaging layer (subtitles / styled text / stickers / sound-effect hits)

- 7 subtitle lines (bottom/middle, up to 2 rows): grey text, line height 2.6%; entrance: hard in×5, slide in×1, fade in×1
- text label ×57: "AUTOMATION", "SENDS", "10,000", "Alerts", "Message", "Share" …
- Stickers / GIFs: animated sticker / GIF ×1, static sticker / image ×3
- Placed by spoken line ×3 (with new wording they follow the line, not the old second): static sticker / image → 0.1s after "Flaw Detection", static sticker / image → 0.1s after "Flaw Detection", static sticker / image → 0.6s after "Flaw Detection"
- 4 persistent layers (unchanged across cuts: lay each on once for its span, not per shot): animated sticker / GIF 0.1–2.4s, static sticker / image 26.4–30.6s, static sticker / image 26.4–30.6s, static sticker / image 26.9–31.5s

<details class="ref"><summary>text timeline (64 rows)</summary>

| Time | Kind | Text | Style | In / out | SFX |
|---|---|---|---|---|---|
| 0.00–0.20s | text label | AUTOMATION | white text, blue outline, line height 4.5% (about 57px) | hard out | — |
| 0.20–0.60s | text label | SENDS | white text, blue outline, line height 4.8% (about 61px) | hard in / hard out | — |
| 0.80–1.20s | text label | 10,000 | white text, blue outline, line height 5.5% (about 70px) | fade in / hard out | — |
| 0.90–1.70s | text label | Description | black text, white outline, line height 2.3% (about 30px) | type-on / hard out | — |
| 1.20–1.70s | text label | Message | black text, line height 2.3% (about 29px) | hard in / hard out | — |
| 1.20–1.70s | text label | Share | black text, line height 2.2% (about 28px) | hard in / hard out | — |
| 1.40–1.60s | text label | Alerts | grey text, line height 2.3% (about 30px) | pop / hard out | — |
| 1.50–1.70s | text label | Save | black text, line height 2.2% (about 28px) | hard in / hard out | — |
| 1.50–1.60s | text label | more | white text, keywords highlighted in grey, line height 1.8% (about 23px) | hard out | — |
| 3.90–4.30s | text label | BASICALLY | white text, blue outline, line height 4.8% (about 62px) | hard in / hard out | — |
| 4.50–4.60s | text label | THISWORKS | white text, blue outline, line height 4.6% (about 59px) | hard in / hard out | — |
| 4.60–5.20s | text label | IS | white text, grey outline, blue box, line height 5.1% (about 65px) | hard out | — |
| 5.40–5.60s | text label | START | white text, blue outline, line height 5.2% (about 67px) | hard in / hard out | — |
| 5.90–6.30s | text label | THETRIGGER, | white text, blue outline, line height 4.9% (about 63px) | hard in | — |
| 6.30–6.60s | text label | START | white text, grey outline, line height 5.1% (about 65px) | hard out | — |
| 8.80–9.30s | text label | DEALS. | white text, blue outline, blue box, line height 4.8% (about 62px) | hard in / hard out | — |
| 9.50–10.00s | text label | TAKETHEDATA | white text, blue outline, line height 4.3% (about 55px) | hard in / hard out | — |
| 10.50–12.30s | subtitle | Item filter | grey text, line height 3.0% (about 38px) | hard in / hard out | — |
| 12.30–12.90s | text label | YOU CAN CHOOSE | white text, blue outline, line height 4.2% (about 54px) | hard in / hard out | — |
| 12.90–13.30s | text label | ITEMS | white text, blue outline, blue box, line height 4.9% (about 63px) | hard out | — |
| 13.40–13.70s | text label | TYPICALLY | white text, blue outline, line height 4.6% (about 59px) | hard out | — |
| 13.70–14.10s | text label | IGO | white text, blue outline, line height 5.6% (about 72px) | hard in / hard out | — |
| 14.30–14.90s | text label | FOR CARS | white text, blue outline, line height 4.8% (about 62px) | hard in / hard out | — |
| 14.90–15.50s | text label | ITWILL | white text, blue outline, line height 5.5% (about 71px) | — | — |
| 15.50–17.50s | subtitle | Lowball Algorithm | grey text, line height 2.7% (about 35px) | hard in / hard out | — |
| 15.50–17.50s | subtitle | Flaw | grey text, grey outline, line height 2.2% (about 28px) | hard in / hard out | — |
| 17.50–17.90s | text label | SHOULD | white text, blue outline, line height 4.8% (about 61px) | hard in / hard out | — |
| 17.90–18.30s | text label | LOWBALL | white text, blue outline, line height 4.9% (about 63px) | hard in / hard out | — |
| 18.30–18.60s | text label | THIS | white text, blue outline, line height 5.5% (about 71px) | hard in / hard out | — |
| 18.80–19.10s | text label | ITEM. | white text, blue outline, line height 5.7% (about 73px) | hard in / hard out | — |
| 19.50–21.10s | subtitle | Message B | grey text, line height 2.4% (about 31px) | hard in / slide out | — |
| 21.90–22.10s | text label | EVEN | white text, blue outline, line height 4.9% (about 63px) | hard in / hard out | — |
| 22.30–22.70s | text label | AFTER | white text, blue outline, line height 4.8% (about 62px) | hard in / hard out | — |
| 23.00–26.30s | subtitle | Flaw Detection | grey text, line height 2.7% (about 34px) | slide in / hard out | — |
| 26.30–26.80s | text label | TO THE | white text, blue outline, line height 5.4% (about 69px) | hard out | — |
| 29.00–29.10s | subtitle | Engine | grey text, line height 2.6% (about 33px) | hard in / hard out | — |
| 29.40–30.50s | subtitle | Relentless Negotiation ⏎ Engine | white text, line height 2.4% (about 31px) | fade in / fade out | — |
| 30.70–31.50s | text label | POSSIBLE | white text, blue outline, line height 5.2% (about 66px) | hard out | — |
| 31.30–31.60s | text label | USUALLY | white text, blue outline, line height 4.7% (about 60px) | fade in / hard out | — |
| 31.90–32.20s | text label | POINT, | white text, blue outline, line height 5.6% (about 72px) | hard in / slide out | — |
| 32.50–32.80s | text label | GHOST | white text, cyan box, line height 5.0% (about 64px) | hard in / hard out | — |
| 36.50–36.90s | text label | UPS. | white text, blue outline, line height 5.4% (about 69px) | hard in / shrink out | — |
| 38.50–38.80s | text label | THEN | white text, blue outline, line height 5.4% (about 69px) | hard in / fade out | — |
| 38.90–39.10s | text label | GOTO | white text, blue outline, line height 5.2% (about 66px) | hard in / hard out | — |
| 39.50–39.60s | text label | alculator | grey text, line height 2.7% (about 35px) | hard in / hard out | — |
| 39.50–39.60s | text label | VALUE | white text, grey outline, line height 4.8% (about 62px) | hard in / hard out | — |
| 43.00–43.80s | text label | THIS IS GREAT | white text, grey outline, line height 4.5% (about 57px) | hard out | — |
| 44.00–44.30s | text label | HAVE | white text, blue outline, line height 5.5% (about 71px) | hard in / hard out | — |
| 44.40–44.60s | text label | MANUAL | white text, grey outline, line height 4.7% (about 60px) | hard out | — |
| 44.60–45.10s | text label | LABOR | white text, grey outline, line height 4.8% (about 62px) | hard out | — |
| 45.50–46.00s | text label | LOWBALLING | white text, grey outline, line height 4.9% (about 63px) | hard in / hard out | — |
| 46.00–46.20s | text label | ON | white text, blue outline, line height 5.2% (about 67px) | hard in / hard out | — |
| 46.30–46.80s | text label | MARKETPLACE. | white text, blue outline, line height 4.1% (about 52px) | hard in / hard out | — |
| 47.00–47.20s | text label | DO | white text, blue outline, line height 5.1% (about 65px) | hard in / hard out | — |
| 47.30–47.80s | text label | 10,000 | white text, blue outline, line height 5.3% (about 68px) | shrink out | — |
| 48.00–48.40s | text label | THESE | white text, blue outline, line height 5.8% (about 74px) | hard in | — |
| 48.40–48.70s | text label | IF YOU WANT | white text, blue outline, line height 5.0% (about 64px) | hard in / hard out | — |
| 48.70–49.10s | text label | THIS | white text, blue outline, line height 5.5% (about 70px) | hard out | — |
| 49.30–49.60s | text label | JUST | white text, blue outline, line height 5.4% (about 69px) | hard in / hard out | — |
| 49.90–50.10s | text label | "FACEBOOK | green text, green outline, line height 4.6% (about 59px) | fade in / hard out | — |
| 50.50–50.60s | text label | THEN | white text, grey outline, line height 5.3% (about 68px) | hard in / hard out | — |
| 50.90–51.30s | text label | SEND YOU | white text, grey outline, line height 5.7% (about 73px) | hard in / hard out | — |
| 51.40–52.00s | text label | MARKETPLACE | white text, grey outline, line height 4.1% (about 52px) | hard out | — |
| 52.00–52.40s | text label | WORKFLOW. | white text, grey outline, line height 4.3% (about 55px) | hard in | — |

</details>

**Stickers / GIFs / picture-in-picture**

| Time | Kind | Position | Motion | Confidence | Crop |
|---|---|---|---|---|---|
| 0.10–2.40s | animated sticker / GIF | x10% y14% w15% h11% | animated | medium (unchanged across a cut) | ![sticker_01](packaging/sticker_01.jpg) |
| 26.40–30.60s | static sticker / image | x55% y71% w20% h9% | static | medium (unchanged across a cut) | ![sticker_02](packaging/sticker_02.jpg) |
| 26.40–30.60s | static sticker / image | x5% y89% w15% h9% | static | medium (unchanged across a cut) | ![sticker_03](packaging/sticker_03.jpg) |
| 26.90–31.50s | static sticker / image | x35% y69% w25% h6% | static | medium (unchanged across a cut) | ![sticker_04](packaging/sticker_04.jpg) |

| Time | Layer | Spoken line |
|---|---|---|
| 26.40s | static sticker / image | 0.1s after "Flaw Detection" |
| 26.40s | static sticker / image | 0.1s after "Flaw Detection" |
| 26.90s | static sticker / image | 0.6s after "Flaw Detection" |

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

- Loudness -17.4 dBFS, peak -1.1 dBFS
- sound runs across cuts, laid in post as one bed (background changes 4.5dB at cuts vs 4.6dB within shots)
- Voice on 43% of the duration, pitch about 132.8Hz
- Voice source: human recording (human recording 73%, TTS voice-over 20%, native dialogue from the AI video model 7%)
  - 52% of the picture is live footage: the voice is most likely location sound or a human voice-over

</details>

## Open questions

- Shot #1 (0.0–1.7s): live action at only 51% confidence, runner-up AI-generated video
- Shot #3 (2.5–2.9s): photo / image: real material or generated, to confirm
- Shot #5 (3.7–4.2s): live action at only 60% confidence, runner-up AI-generated video
- Shot #7 (5.2–6.5s): live action at only 51% confidence, runner-up AI-generated video
- Shot #8 (6.5–8.6s): code / template render at only 55% confidence, runner-up still image + pan/zoom
- Shot #9 (8.6–10.5s): live action at only 51% confidence, runner-up AI-generated video
- Shot #10 (10.5–12.3s): code / template render at only 55% confidence, runner-up still image + pan/zoom
- Shot #11 (12.3–15.5s): live action at only 51% confidence, runner-up AI-generated video
- Shot #12 (15.5–17.5s): code / template render at only 55% confidence, runner-up still image + pan/zoom
- Shot #13 (17.5–19.5s): live action at only 51% confidence, runner-up AI-generated video
- Shot #14 (19.5–21.2s): code / template render at only 55% confidence, runner-up still image + pan/zoom
- Shot #15 (21.2–22.8s): live action at only 50% confidence, runner-up AI-generated video
- Shot #21 (31.6–33.0s): live action at only 51% confidence, runner-up AI-generated video
- Shot #24 (37.0–38.2s): code / template render at only 54% confidence, runner-up still image + pan/zoom
- Shot #25 (38.2–39.6s): live action at only 51% confidence, runner-up AI-generated video
- Shot #27 (43.2–52.4s): live action at only 51% confidence, runner-up AI-generated video
- No AI listened to the soundtrack (the review covered the picture only): real voice versus TTS is inferred from the waveform; the effects were found on the separated effects track and their types are estimated from the sound. Play the stems and each effect under “Sound” to check

# Part two · Remake plan

## Remake it yourself: do it in this order

Copy the method and the rhythm, not the pictures: keep what each part does and fill it with your own content and material.

This is a talking head. Do the steps in this order; the detail for each is in the matching subsection below. 45% of the time is a motion-graphics explainer; its steps are included.

1. **Write the content**: write yours in the same 12 steps as the original (narrative line under “Content and structure”)
2. **Collect material**: the real material in the picture (live footage, UI screenshot, screen recording) needs the original files, listed under “What to prepare”; one reference image per recurring character to lock appearance across shots: Presenter
3. **Shoot**: phone held vertical, mostly medium shot; light: night / low-light ambient, no dedicated fill — the key is whatever is there (street lamps, signs, ceiling lights, screens), phone night / portrait mode; use a street lamp or sign as the key, subject just off-axis below it; grade: natural (close to the original colours) (setups under “Shoot”)
4. **Motion graphics**: have the agent make an editable first version and change the text and pictures on top of it rather than starting from scratch; the first version is only a start, where it differs from the original is under “Code build”
5. **Voice**: the original is human recording; record it yourself or use TTS; delivery per “Acting and emotion”
6. **Edit**: follow the order and lengths in the shot list; the original has 27 shots at 1.9s each; 4 transitions under “Edit”
7. **Subtitles and styled text**: import `packaging/subtitles.srt` and replace the words; timing and style under “Packaging layer”
8. **Put it together and compare**: hand the shots you made to the agent; it places them on the original timeline, keeps the original where yours are missing, and renders a side-by-side comparison with the original

### What to prepare

- Real files shown in the picture (screenshots, photos, recordings; get the originals):
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

### Shoot

Shoot every shot of one scene before moving to the next; within a scene, shoot the wider sizes first and the close-ups last so the lighting is set only once. Leave about 1s of handle at both ends of every take.

**S1**: shots #1, #5–#7, #9, #11, #13, #15, #18, #20, #21, #23, #25, #27 (27.04s on screen); Desk in a dark room, mesh chair, white desk, vertical teal LED tube behind, Low key with a teal accent
- Lighting: night / low-light ambient, no dedicated fill, key light frontal, cool (daylight / cool-white LED)
- Setup medium shot · moving camera (gimbal / handheld pan) · pan / track/pull-out/push-in/static: shots #1, #6, #7, #9, #11, #13, #18, #20, #21, #23, #25, #27, 24.92s on screen, shoot about 48.9s
- Setup medium shot · fixed camera (tripod / mount / on the desk) · static: shots #15, 1.54s on screen, shoot about 3.5s
- Setup medium close-up · moving camera (gimbal / handheld pan) · push-in: shots #5, 0.58s on screen, shoot about 2.6s

### Code build

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

<details class="ref"><summary>Motion #2 1.7–2.5s · 2 events</summary>

![#2 1.7–2.5s](shots/shot_002_strip.jpg)

- Ground #46444a; other main colours #faf7fc #0a0912 #d1ced8 #343039; drawn layer #fdf9fe #0e0a13 #d1ced7 #9f9faa
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#2 1.7–2.5s](shots/shot_002_elements.jpg)

- S1. never moves: horizontal line · x 13%–89%, y 10%–12% · #fefaff · [crop](shots/shot_002_st_01.jpg)
- S2. never moves: shape / text block · x 8%–93%, y 14%–58% · #fffbff · text “4of13 / 2003 Dodge srt 4.Custom / $2,500” · [crop](shots/shot_002_st_02.jpg)
- Continuous layer: 1% of the frame moves through the whole shot (x 13%–89%, y 12%–91%), e.g. drifting gradients, particle flow, breathing glow
1. 2.20–2.40s · middle (x 56%–64%, y 61%–71%) · appears, ease-in-out · #efebf2 · [crop](shots/shot_002_el_01.jpg)
2. 2.40–2.47s · middle (x 16%–56%, y 50%–52%) · changes, instant · #bab9bb · text “Send selleramessage” · [crop](shots/shot_002_el_02.jpg)

</details>

<details class="ref"><summary>Motion #3 2.5–2.9s · 0 events</summary>

- No element motion measured (still picture or only slight changes)

</details>

<details class="ref"><summary>Motion #4 2.9–3.7s · 0 events</summary>

![#4 2.9–3.7s](shots/shot_004_strip.jpg)

- Ground #49464a; other main colours #f9f6fb #cfcbd4 #3c393e #7b7371; drawn layer #fdf8fd #cec8cf #201a25 #ada7b2
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#4 2.9–3.7s](shots/shot_004_elements.jpg)

- S1. never moves: horizontal line · x 11%–33%, y 10%–11% · #fefaff · [crop](shots/shot_004_st_01.jpg)
- S2. never moves: horizontal line · x 36%–73%, y 10%–11% · #fefaff · [crop](shots/shot_004_st_02.jpg)
- S3. never moves: shape / text block · x 78%–82%, y 30%–32% · #1b171e · [crop](shots/shot_004_st_03.jpg)

</details>

<details class="ref"><summary>Motion #8 6.5–8.6s · 0 events</summary>

![#8 6.5–8.6s](shots/shot_008_strip.jpg)

- Ground #38363c; other main colours #484b52 #5f5d65 #717176; drawn layer #6d6c6f #7d8b9e #f7fafd #b9bdc9
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#8 6.5–8.6s](shots/shot_008_elements.jpg)

- S1. never moves: shape / text block · x 9%–20%, y 40%–42% · #727279 · [crop](shots/shot_008_st_01.jpg)
- S2. never moves: shape / text block · x 44%–56%, y 42%–43% · #929099 · [crop](shots/shot_008_st_02.jpg)
- S3. never moves: shape / text block · x 71%–80%, y 42%–44% · #77757c · [crop](shots/shot_008_st_03.jpg)
- S4. never moves: shape / text block · x 92%–100%, y 43%–45% · #68666d · [crop](shots/shot_008_st_04.jpg)
- S5. never moves: shape / text block · x 29%–38%, y 47%–48% · #908e97 · [crop](shots/shot_008_st_05.jpg)
- S6. never moves: shape / text block · x 73%–84%, y 50%–53% · #6e6b72 · text “Data Normalizer” · [crop](shots/shot_008_st_06.jpg)
- S7. never moves: shape / text block · x 11%–24%, y 52%–54% · #7b7981 · text “Start” · [crop](shots/shot_008_st_07.jpg)
- S8. never moves: shape / text block · x 49%–60%, y 52%–53% · #8d8a98 · text “FB Marketplace scraper” · [crop](shots/shot_008_st_08.jpg)
- [crop L1](shots/shot_008_ly_01.jpg) [crop L2](shots/shot_008_ly_02.jpg) · Continuous layer: 8% of the frame moves through the whole shot (x 0%–100%, y 40%–70%), e.g. drifting gradients, particle flow, breathing glow

</details>

<details class="ref"><summary>Motion #10 10.5–12.3s · 0 events</summary>

![#10 10.5–12.3s](shots/shot_010_strip.jpg)

- Ground #38363c; other main colours #484a50 #5c5b62 #6f6f75 #8b8b94; drawn layer #6e7175 #8d9599 #dfe1e9 #bc7a45
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#10 10.5–12.3s](shots/shot_010_elements.jpg)

- S1. never moves: shape / text block · x 2%–22%, y 40%–43% · #77767e · [crop](shots/shot_010_st_01.jpg)
- S2. never moves: shape / text block · x 89%–100%, y 40%–44% · #88868d · [crop](shots/shot_010_st_02.jpg)
- S3. never moves: shape / text block · x 47%–62%, y 54%–55% · #9996a3 · text “Item filter” · [crop](shots/shot_010_st_03.jpg)
- S4. never moves: shape / text block · x 4%–24%, y 54%–56% · #7d7c82 · text “Normalizer” · [crop](shots/shot_010_st_04.jpg)
- S5. never moves: shape / text block · x 82%–93%, y 68%–70% · #72727a · [crop](shots/shot_010_st_05.jpg)
- S6. never moves: shape / text block · x 53%–69%, y 70%–72% · #93919b · [crop](shots/shot_010_st_06.jpg)
- S7. never moves: shape / text block · x 87%–100%, y 79%–85% · #78787f · [crop](shots/shot_010_st_07.jpg)
- S8. never moves: shape / text block · x 58%–73%, y 81%–87% · #7a7981 · [crop](shots/shot_010_st_08.jpg)
- [crop L1](shots/shot_010_ly_01.jpg) [crop L2](shots/shot_010_ly_02.jpg) · Continuous layer: 15% of the frame moves through the whole shot (x 0%–100%, y 31%–91%), e.g. drifting gradients, particle flow, breathing glow

</details>

<details class="ref"><summary>Motion #12 15.5–17.5s · 0 events</summary>

![#12 15.5–17.5s](shots/shot_012_strip.jpg)

- Ground #38363c; other main colours #484a50 #5e5c62 #6e6f76; drawn layer #707478 #a4a4af #f4f7fb #bb7b44
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#12 15.5–17.5s](shots/shot_012_elements.jpg)

- S1. never moves: shape / text block · x 51%–64%, y 21%–23% · #6c6b72 · [crop](shots/shot_012_st_01.jpg)
- S2. never moves: shape / text block · x 19%–33%, y 22%–24% · #68666f · [crop](shots/shot_012_st_02.jpg)
- S3. never moves: shape / text block · x 18%–31%, y 29%–35% · #727077 · text “Normalizer / ormalizer” · [crop](shots/shot_012_st_03.jpg)
- S4. never moves: shape / text block · x 60%–71%, y 37%–38% · #77737a · [crop](shots/shot_012_st_04.jpg)
- S5. never moves: shape / text block · x 80%–98%, y 42%–45% · #6f6f76 · [crop](shots/shot_012_st_05.jpg)
- S6. never moves: shape / text block · x 49%–62%, y 43%–44% · #86828b · [crop](shots/shot_012_st_06.jpg)
- S7. never moves: shape / text block · x 80%–98%, y 50%–56% · #6a6a72 · text “Flaw” · [crop](shots/shot_012_st_07.jpg)
- S8. never moves: shape / text block · x 47%–60%, y 54%–55% · #9898a3 · text “Lowball Algorithm” · [crop](shots/shot_012_st_08.jpg)
- [crop L1](shots/shot_012_ly_01.jpg) [crop L2](shots/shot_012_ly_02.jpg) · Continuous layer: 11% of the frame moves through the whole shot (x 0%–100%, y 21%–69%), e.g. drifting gradients, particle flow, breathing glow

</details>

<details class="ref"><summary>Motion #14 19.5–21.2s · 0 events</summary>

![#14 19.5–21.2s](shots/shot_014_strip.jpg)

- Ground #38363c; other main colours #4b4b53 #616068 #787984 #979bae; drawn layer #6c7478 #9498a8 #e6eaf2
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#14 19.5–21.2s](shots/shot_014_elements.jpg)

- S1. never moves: shape / text block · x 58%–69%, y 9%–13% · #6b6a73 · [crop](shots/shot_014_st_01.jpg)
- S2. never moves: shape / text block · x 2%–20%, y 14%–18% · #6e6d75 · [crop](shots/shot_014_st_02.jpg)
- S3. never moves: shape / text block · x 58%–78%, y 18%–24% · #7f7e84 · [crop](shots/shot_014_st_03.jpg)
- S4. never moves: shape / text block · x 91%–100%, y 21%–26% · #6b6a72 · [crop](shots/shot_014_st_04.jpg)
- S5. never moves: shape / text block · x 4%–22%, y 26%–31% · #717078 · [crop](shots/shot_014_st_05.jpg)
- S6. never moves: shape / text block · x 0%–16%, y 34%–37% · #6d6c74 · [crop](shots/shot_014_st_06.jpg)
- S7. never moves: shape / text block · x 9%–29%, y 42%–45% · #7b7a83 · [crop](shots/shot_014_st_07.jpg)
- S8. never moves: shape / text block · x 13%–31%, y 56%–58% · #808087 · text “Lowball Algorithm” · [crop](shots/shot_014_st_08.jpg)
- [crop L1](shots/shot_014_ly_01.jpg) [crop L2](shots/shot_014_ly_02.jpg) · Continuous layer: 20% of the frame moves through the whole shot (x 0%–100%, y 9%–69%), e.g. drifting gradients, particle flow, breathing glow

</details>

<details class="ref"><summary>Motion #16 22.8–24.4s · 5 events</summary>

![#16 22.8–24.4s](shots/shot_016_strip.jpg)

- Ground #3a373e; other main colours #faf9fd #4b4c56 #7f839c #d1d3dd; drawn layer #bac2d9 #fdf9fe #888a9a #141b37
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#16 22.8–24.4s](shots/shot_016_elements.jpg)

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

</details>

<details class="ref"><summary>Motion #17 24.4–26.3s · 9 events</summary>

![#17 24.4–26.3s](shots/shot_017_strip.jpg)

- Ground #fbfafe; other main colours #38363c #4a4b52 #68676e #1a73fa; drawn layer #3f3d43 #1d70f9 #faf8fd #8093ac
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#17 24.4–26.3s](shots/shot_017_elements.jpg)

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

</details>

<details class="ref"><summary>Motion #19 26.8–30.7s · 12 events</summary>

![#19 26.8–30.7s](shots/shot_019_strip.jpg)

- Ground #fbfafe; other main colours #38363c #4b4a51 #0a73fb #66666f; drawn layer #fbf9fe #3b373b #2070f7
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#19 26.8–30.7s](shots/shot_019_elements.jpg)

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

</details>

<details class="ref"><summary>Motion #22 33.0–36.5s · 17 events</summary>

![#22 33.0–36.5s](shots/shot_022_strip.jpg)

- Ground #fcfbff; other main colours #38363c #4c4b52 #0371fc #6b6d76; drawn layer #3c383c #1d70fc #fdfaff #4c82d1
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#22 33.0–36.5s](shots/shot_022_elements.jpg)

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

</details>

<details class="ref"><summary>Motion #24 37.0–38.2s · 0 events</summary>

![#24 37.0–38.2s](shots/shot_024_strip.jpg)

- Ground #38363c; other main colours #474951 #676770 #56565f #8a8282; drawn layer #717073 #a2a2ae #f1f5fa
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#24 37.0–38.2s](shots/shot_024_elements.jpg)

- S1. never moves: shape / text block · x 0%–11%, y 1%–3% · #6a6871 · [crop](shots/shot_024_st_01.jpg)
- S2. never moves: shape / text block · x 38%–51%, y 2%–4% · #6a6870 · [crop](shots/shot_024_st_02.jpg)
- S3. never moves: shape / text block · x 0%–11%, y 8%–13% · #6b6a73 · [crop](shots/shot_024_st_03.jpg)
- S4. never moves: shape / text block · x 34%–51%, y 9%–14% · #716f78 · [crop](shots/shot_024_st_04.jpg)
- S5. never moves: shape / text block · x 38%–51%, y 21%–22% · #6f6d76 · [crop](shots/shot_024_st_05.jpg)
- S6. never moves: shape / text block · x 0%–9%, y 25%–29% · #6e6c75 · [crop](shots/shot_024_st_06.jpg)
- S7. never moves: shape / text block · x 0%–11%, y 41%–46% · #75737a · [crop](shots/shot_024_st_07.jpg)
- S8. never moves: shape / text block · x 2%–18%, y 51%–52% · #75737c · [crop](shots/shot_024_st_08.jpg)
- [crop L1](shots/shot_024_ly_01.jpg) [crop L2](shots/shot_024_ly_02.jpg) · Continuous layer: 19% of the frame moves through the whole shot (x 0%–100%, y 1%–69%), e.g. drifting gradients, particle flow, breathing glow

</details>

<details class="ref"><summary>Motion #26 39.6–43.2s · 10 events</summary>

![#26 39.6–43.2s](shots/shot_026_strip.jpg)

- Ground #38363c; other main colours #484a51 #6e717b #5d5c63 #818d9b; drawn layer #716e75 #9b969b #eaeff5 #4aa6d7
Element crops (numbers match the motion list below; L = the continuously moving layer mid-shot and at the end, S = elements that never move), full-size files in `shots/`:

![#26 39.6–43.2s](shots/shot_026_elements.jpg)

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

</details>

### Acting and emotion

In a prompt, describe the visible expression and movement rather than words like “happy” or “sad”, and keep it smaller rather than bigger (strong emotion words tend to give mask faces and forced smiles); get the expression right in the first frame; for shots with lines, make the voice with its delivery first and let the picture act to it. For generated shots the Face and Movement below are already in the generation-unit prompts.

<details class="ref"><summary>all 14 shots</summary>

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

</details>

- **actor plays it**: Filmed: hand the face, movement and delivery to the actor as direction, and rehearse the pauses and tone against the original once

### Edit

- Cut in the order and lengths of the shot list
- Approach: Hook is three phone captures in two seconds. Then the presenter alternates with full-frame workflow graphics every 1 to 2 seconds; proof arrives as stacked panels (a chat on top, the diagram below). Hard cuts only.
- Rhythm: 29.8 cuts per minute, 1.93s average live-action shot; 1 camera set-up(s) / location(s); 3 jump cut(s) and 0 punch-in(s) within the same set-up; inserts (screenshots / screen recordings / cards / stock) take 48%; 67% of cuts land in pauses of the speech (cutting on breaths); transitions cut×22, jump cut×4

## Appendix

### Shot by shot

Each shot has two parts: what is visible on screen, and how the tools infer it was made (with the basis); remake prompts last. Folded by default.

<details class="ref"><summary>#1 00:00.000–00:01.667 · live action + code / editor overlays (subtitles, animated sticker / GIF); brings in real material (live footage)</summary>

![shot_001](shots/shot_001.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter seated at a desk in a dark room, a teal light tube behind him, talking to camera. A floating dark panel with the whole workflow sits above his head. Bold white caption, one word at a time.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.3:1 (0.4 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/bottom): Description / Needsheadeverythingtodothejobcomeswith / carnewhead,gaskets,spray,boltsoldonestil
- Text track (subtitle/bottom): car.Hard piped,custom paint,small turbo. / more
- Text track (subtitle/middle): AUTOMATION / SENDS / 10,000 / Alerts
- Text track (subtitle/middle): 4of13 / 2003Dodgesrt4.Custom
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 49%, AI-generated video 17%, 3D render 11% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 34% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 14% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Per-frame sharpness oscillates periodically (period 4 frames, correlation 0.65) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#2 00:01.667–00:02.458 · screen recording / screenshot + code / editor overlays (animated sticker / GIF); brings in real material (UI screenshot, screen recording)</summary>

![shot_002](shots/shot_002.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame grey card with a phone screen: a marketplace listing for a used car, the message box filling in and the keyboard up.
- Text track (text in the picture/bottom): ABC / space / return
- Text track (text in the picture/middle): 4of13 / 2003 Dodge srt 4.Custom
- Text track (text in the picture/middle): $2,500 / Listed 14days ago·Land OLakes,FL
- Text track (text in the picture/middle): Send selleramessage / Flooded100 / Send
- [AI assistant review] A phone-sized app screen on a flat grey ground with rounded corners: real marketplace listing photos, prices and a keyboard
- [AI assistant review] Text is typed character by character into the message box, as in a screen recording
- [AI assistant review] No perspective, glare or camera shake: a capture placed on a card, not a filmed phone

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: screen recording / screenshot 100%, live action 0%, AI-generated video 0% (user)
- Material: the user's real material: UI screenshot, screen recording
  - screen recording: a light UI panel holding 19 text items (19 of them small type)
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to screen recording / screenshot: Phone screen recordings of a marketplace app placed on a grey card.
  - Rendered texture: 35% flat colour blocks, 95% of pixels use only 34 colours, 48% axis-aligned edges

- Remake: Screen recording / screenshot: rebuild from a real screen recording or web screenshot; real material the user must supply: UI screenshot (whole frame), screen recording (part of the frame x9% y36% w82% h55%), screen recording (part of the frame)

</details>

<details class="ref"><summary>#3 00:02.458–00:02.875 · screen recording / screenshot; brings in real material (UI screenshot, screen recording)</summary>

![shot_003](shots/shot_003.jpg)

**Visible on screen** (check against the frames)
- Picture: Same card: a grid of marketplace car listings, very short.
- Text track (text in the picture/bottom): $3,000$3,800.200.. / $4,500·2000Acura1.
- Text track (text in the picture/middle): Justlisted / $700$1,000.honda.. / $500.HondaCivic
- Text track (text in the picture/middle): $200.PerformanceF...$3,200$6,000·2003...
- [AI assistant review] A phone-sized app screen on a flat grey ground with rounded corners: real marketplace listing photos, prices and a keyboard
- [AI assistant review] Text is typed character by character into the message box, as in a screen recording
- [AI assistant review] No perspective, glare or camera shake: a capture placed on a card, not a filmed phone

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: screen recording / screenshot 100%, live action 0%, AI-generated video 0% (user)
- Material: the user's real material: UI screenshot, screen recording; real or not, to confirm: photo / image
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to screen recording / screenshot: Phone screen recordings of a marketplace app placed on a grey card.
  - Photographic texture: noise σ=0.15, 127 colours, 19% flat blocks

- Remake: Screen recording / screenshot: rebuild from a real screen recording or web screenshot; real material the user must supply: UI screenshot (whole frame), screen recording (part of the frame)

</details>

<details class="ref"><summary>#4 00:02.875–00:03.667 · screen recording / screenshot; brings in real material (UI screenshot, screen recording)</summary>

![shot_004](shots/shot_004.jpg)

**Visible on screen** (check against the frames)
- Picture: Same card: another car listing with the message box prefilled.
- Text track (text in the picture/bottom): a / S / d / f
- Text track (text in the picture/bottom): Z / X
- Text track (text in the picture/bottom): 123 / space / return
- Text track (text in the picture/middle): 2000AcuraIntegra·GSSedan4D / $4,500
- [AI assistant review] A phone-sized app screen on a flat grey ground with rounded corners: real marketplace listing photos, prices and a keyboard
- [AI assistant review] Text is typed character by character into the message box, as in a screen recording
- [AI assistant review] No perspective, glare or camera shake: a capture placed on a card, not a filmed phone

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: screen recording / screenshot 100%, live action 0%, AI-generated video 0% (user)
- Material: the user's real material: UI screenshot, screen recording
  - screen recording: a light UI panel holding 21 text items (19 of them small type)
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to screen recording / screenshot: Phone screen recordings of a marketplace app placed on a grey card.
  - Rendered texture: 28% flat colour blocks, 95% of pixels use only 37 colours, 44% axis-aligned edges

- Remake: Screen recording / screenshot: rebuild from a real screen recording or web screenshot; real material the user must supply: UI screenshot (whole frame), screen recording (part of the frame x8% y9% w83% h83%), screen recording (part of the frame)

</details>

<details class="ref"><summary>#5 00:03.667–00:04.250 · live action + code / editor overlays (text labels); brings in real material (live footage)</summary>

![shot_005](shots/shot_005.jpg)

**Visible on screen** (check against the frames)
- Picture: Back to the presenter with the workflow panel floating above him.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium close-up; moving camera (gimbal / handheld pan); soft frontal light (flat light); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.3:1 (0.4 stops); soft light (almost no lit / shadow edge)
- Text track (text/middle): BASICALLY
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 58%, AI-generated video 13%, 3D render 9% (fused_agent)
- Material: the user's real material: live footage

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#6 00:04.250–00:05.250 · live action + code / editor overlays (subtitles, static graphics); brings in real material (live footage)</summary>

![shot_006](shots/shot_006.jpg)

**Visible on screen** (check against the frames)
- Picture: Same framing, the presenter gesturing with both hands. Caption: BASICALLY,
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan)
- Text track (subtitle/middle): THISWORKS / IS
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 61%, AI-generated video 13%, 3D render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 37% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 12% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.19, 137 colours, 19% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#7 00:05.250–00:06.500 · live action + code / editor overlays (subtitles, static graphics); brings in real material (live footage)</summary>

![shot_007](shots/shot_007.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk, no panel, hand on the mouse.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan)
- Text track (subtitle/middle): START / THETRIGGER,
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 49%, AI-generated video 21%, 3D render 9% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 53% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.12, 134 colours, 24% flat blocks
  - Per-frame sharpness oscillates periodically (period 5 frames, correlation 0.30) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#8 00:06.500–00:08.625 · code / template render</summary>

![shot_008](shots/shot_008.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas: a Start node, a Facebook Marketplace scraper node and the next node, the view sliding right. Caption: START.
- Text track (text in the picture/middle): f
- Text track (text in the picture/middle): FB Marketplace scraper / Data Normalizer / Start
- Text track (text in the picture/middle): START / FACEBOOK / SCRAPER / ANDIT
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small labels
- [AI assistant review] The canvas moves as one rigid plane with a synthetic depth blur at the far edge: drawn, not filmed
- [AI assistant review] No sensor noise or room lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 53%, still image + pan/zoom 30%, screen recording / screenshot 7% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.10px residual, no local motion) → pan/zoom on a still image: zoom +0.4%/s, pan 9px/s
  - Rendered texture: 66% flat colour blocks, 95% of pixels use only 7 colours, 32% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#9 00:08.625–00:10.542 · live action + code / editor overlays (subtitles); brings in real material (live footage)</summary>

![shot_009](shots/shot_009.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk, looking at camera.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): DEALS. / TAKETHEDATA / PUTIT / ITEM
- Text track (subtitle/middle): Item filter / Data Normalizer
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 49%, AI-generated video 21%, 3D render 9% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 53% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.12, 129 colours, 24% flat blocks
  - Per-frame sharpness oscillates periodically (period 2 frames, correlation 0.01) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#10 00:10.542–00:12.333 · code / template render</summary>

![shot_010](shots/shot_010.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas: Data Normalizer, Item filter and Lowball Algorithm nodes. Caption: ITEM.
- Text track (text in the picture/middle): Item filter / Normalizer
- Text track (text in the picture/middle): FILTER / OF YOUR CHOICE / SO
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small labels
- [AI assistant review] The canvas moves as one rigid plane with a synthetic depth blur at the far edge: drawn, not filmed
- [AI assistant review] No sensor noise or room lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 53%, still image + pan/zoom 31%, screen recording / screenshot 6% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.06px residual, no local motion) → pan/zoom on a still image: zoom +0.5%/s, pan 7px/s
  - Rendered texture: 57% flat colour blocks, 95% of pixels use only 13 colours, 24% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#11 00:12.333–00:15.458 · live action + code / editor overlays (subtitles, static graphics); brings in real material (live footage)</summary>

![shot_011](shots/shot_011.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk, one hand raised.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): YOU CAN CHOOSE / ITEMS / TYPICALLY / IGO
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 50%, AI-generated video 21%, 3D render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 54% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 5% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.12, 131 colours, 23% flat blocks
  - Per-frame sharpness oscillates periodically (period 2 frames, correlation 0.04) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#12 00:15.458–00:17.542 · code / template render</summary>

![shot_012](shots/shot_012.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas pushing toward the Lowball Algorithm node. Caption: LOWBALL.
- Text track (text in the picture/middle): Normalizer / Item filter / ormalizer / Iltem filter
- Text track (text in the picture/middle): Lowball Algorithm / Flaw
- Text track (text in the picture/middle): LOWBALL / ALGORITHM / DETERMINING / MUCH
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small labels
- [AI assistant review] The canvas moves as one rigid plane with a synthetic depth blur at the far edge: drawn, not filmed
- [AI assistant review] No sensor noise or room lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 53%, still image + pan/zoom 30%, screen recording / screenshot 7% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.09px residual, no local motion) → pan/zoom on a still image: zoom -0.4%/s, pan 9px/s
  - Rendered texture: 61% flat colour blocks, 95% of pixels use only 10 colours, 39% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#13 00:17.542–00:19.500 · live action + code / editor overlays (subtitles); brings in real material (live footage)</summary>

![shot_013](shots/shot_013.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.1 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): LOWBALL / THIS / ITEM.
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 50%, AI-generated video 21%, 3D render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 54% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.12, 130 colours, 24% flat blocks
  - Per-frame sharpness oscillates periodically (period 4 frames, correlation 0.32) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#14 00:19.500–00:21.208 · code / template render</summary>

![shot_014](shots/shot_014.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas: Lowball Algorithm, Flaw Detection and Message Blaster nodes fanning out. Caption: THEN.
- Text track (text in the picture/middle): Deal Analyzer
- Text track (text in the picture/middle): Flaw Detection / Message Bia / Lowball Algorithm / Message Bi
- Text track (text in the picture/middle): THEN / THROUGH / DETECTION / TO
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small labels
- [AI assistant review] The canvas moves as one rigid plane with a synthetic depth blur at the far edge: drawn, not filmed
- [AI assistant review] No sensor noise or room lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 53%, still image + pan/zoom 31%, screen recording / screenshot 6% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.05px residual, no local motion) → pan/zoom on a still image: zoom +0.6%/s, pan 8px/s
  - Rendered texture: 50% flat colour blocks, 95% of pixels use only 16 colours, 23% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#15 00:21.208–00:22.750 · live action + code / editor overlays (subtitles, static graphics); brings in real material (live footage)</summary>

![shot_015](shots/shot_015.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk, hand sweeping across.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; fixed camera (tripod / mount / on the desk); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.1 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): THEPRICE / EVEN / AFTER
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 48%, AI-generated video 20%, AI avatar (talking head) 9% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 54% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 5% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.11, 136 colours, 24% flat blocks
  - Per-frame sharpness oscillates periodically (period 4 frames, correlation 0.42) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI
  - 100% of sampled frames show a frontal face on a fixed camera, voice on the audio track

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#16 00:22.750–00:24.417 · code / template render; brings in real material (UI screenshot, screen recording)</summary>

![shot_016](shots/shot_016.jpg)

**Visible on screen** (check against the frames)
- Picture: Top: a marketplace listing for a pickup truck. Bottom: the workflow canvas around the Message Blaster node.
- Text track (text in the picture/bottom): Flaw Detection / Message Blasterl
- Text track (text in the picture/middle): 2007DodgeRam1500QuadCab / $12,500 / 2007 Dodge Ram 1500 Quad Cab
- Text track (text in the picture/middle): Listedaboutaminuteago.WestKelowna,BC
- Text track (text in the picture/middle): Send sellera message / Send / Sendselleramessage / Yepenginebayl
- [AI assistant review] Two stacked panels: a phone chat or listing capture on top, the vector workflow canvas below
- [AI assistant review] Top panel has real app type and photos; bottom panel is the same drawn node graph as the full-frame graphics
- [AI assistant review] No filmed element in the frame

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 61%, 3D render 12%, screen recording / screenshot 10% (fused_agent)
- Material: mixed (includes real material): UI screenshot, screen recording
  - UI screenshot: a light UI panel holding 9 text items (8 of them small type)
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 36% flat colour blocks, 95% of pixels use only 67 colours, 31% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed; real material the user must supply: UI screenshot (part of the frame x0% y25% w100% h31%), screen recording (part of the frame)

</details>

<details class="ref"><summary>#17 00:24.417–00:26.292 · code / template render; brings in real material (screen recording)</summary>

![shot_017](shots/shot_017.jpg)

**Visible on screen** (check against the frames)
- Picture: Top: a chat with the seller where lowball messages are being typed. Bottom: the same workflow nodes.
- Text track (text in the picture/bottom): Opp / Oppe
- Text track (text in the picture/bottom): Flaw Detection / Message Blasterl
- Text track (text in the picture/middle): Marketplacechatsandyourprivacy / YounamedthegroupBrody·2007DodgeRam1500Qu / Yep engine bay is fucked / PrettyclappedI'lltakeitfor1200
- Text track (text in the picture/middle): You changed thegroupphoto. / Yep engine bay is fucked / Youchangedthegroupphoto. / Yepenginebay isfucked
- [AI assistant review] Two stacked panels: a phone chat or listing capture on top, the vector workflow canvas below
- [AI assistant review] Top panel has real app type and photos; bottom panel is the same drawn node graph as the full-frame graphics
- [AI assistant review] No filmed element in the frame

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 63%, 3D render 12%, screen recording / screenshot 11% (fused_agent)
- Material: mixed (includes real material): screen recording
  - screen recording: a light UI panel holding 10 text items (10 of them small type)
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 53% flat colour blocks, 95% of pixels use only 39 colours, 32% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed; real material the user must supply: screen recording (part of the frame x0% y0% w100% h54%), screen recording (part of the frame)

</details>

<details class="ref"><summary>#18 00:26.292–00:26.833 · live action + code / editor overlays (text labels, static sticker); brings in real material (live footage)</summary>

![shot_018](shots/shot_018.jpg)

**Visible on screen** (check against the frames)
- Picture: Very short presenter shot. Caption: THEN IT
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.3:1 (0.3 stops); soft light (almost no lit / shadow edge)
- Text track (text/middle): TO THE
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 61%, AI-generated video 15%, 3D render 6% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 54% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.12, 128 colours, 25% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#19 00:26.833–00:30.667 · code / template render + code / editor overlays (static sticker); brings in real material (screen recording)</summary>

![shot_019](shots/shot_019.jpg)

**Visible on screen** (check against the frames)
- Picture: Top: the chat continues, the seller replying in annoyance. Bottom: the Relentless Negotiation Engine node.
- Text on objects in the scene (not subtitles): Marketplacechatsandyourprivacy
- Text track (text in the picture/bottom): Relentless Negotiation / Engine / RelentlessNegotiation
- Text track (text in the picture/middle): Are you drunk? / Hell na / Paints clapped / 1050takeitorleaveit
- Text track (text in the picture/middle): Paints clapped / Sent / 1050takeitorleaveit / Leaveme alone
- Text track (text in the picture/middle): Paints clapped / 1050takeitorleaveit / Leavemealone / Have it ready tonight
- Motion beats within the shot: 27.67s
- [AI assistant review] Two stacked panels: a phone chat or listing capture on top, the vector workflow canvas below
- [AI assistant review] Top panel has real app type and photos; bottom panel is the same drawn node graph as the full-frame graphics
- [AI assistant review] No filmed element in the frame

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 70%, screen recording / screenshot 10%, 3D render 9% (fused_agent)
- Material: mixed (includes real material): screen recording
  - screen recording: a light UI panel holding 9 text items (9 of them small type)
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 58% flat colour blocks, 95% of pixels use only 31 colours, 39% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed; real material the user must supply: screen recording (part of the frame x0% y0% w100% h53%), screen recording (part of the frame)

</details>

<details class="ref"><summary>#20 00:30.667–00:31.625 · live action + code / editor overlays (subtitles, static sticker); brings in real material (live footage)</summary>

![shot_020](shots/shot_020.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk, smiling slightly.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): POSSIBLE / USUALLY
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 100%, AI-generated video 0%, AI avatar (talking head) 0% (user)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - [User correction] Changed to live action: Filmed presenter, same set-up as the other presenter shots.
  - Low-light shot: 54% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.12, 131 colours, 24% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#21 00:31.625–00:33.042 · live action + code / editor overlays (subtitles, text labels, title); brings in real material (live footage)</summary>

![shot_021](shots/shot_021.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); low key (subject lit on its own, background held black); key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.1:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/bottom): qotiation / Follow-up Nuke
- Text track (subtitle/middle): POINT, / GHOST
- Text track (subtitle/middle): 1310 / Hey you there?
- Text track (text/middle): Hey
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 50%, AI-generated video 21%, 3D render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 54% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.13, 126 colours, 24% flat blocks
  - Per-frame sharpness oscillates periodically (period 4 frames, correlation 0.57) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#22 00:33.042–00:36.458 · code / template render; brings in real material (UI screenshot, screen recording)</summary>

![shot_022](shots/shot_022.jpg)

**Visible on screen** (check against the frames)
- Picture: Top: a long chat where the bot keeps messaging after being told to stop. Bottom: the Follow-up Nuke node.
- Text on objects in the scene (not subtitles): Hey, Hey/Hey/Hey
- Text track (text in the picture/bottom): egotiation / Follow-up Nuke / Negotiation
- Text track (text in the picture/bottom): f
- Text track (text in the picture/middle): Hey / Wherearetou / Hello? / 1310
- Text track (text in the picture/middle): Wherearetou / Hello? / 1310 / I'll stop by soon
- [AI assistant review] Two stacked panels: a phone chat or listing capture on top, the vector workflow canvas below
- [AI assistant review] Top panel has real app type and photos; bottom panel is the same drawn node graph as the full-frame graphics
- [AI assistant review] No filmed element in the frame

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 63%, screen recording / screenshot 14%, 3D render 11% (fused_agent)
- Material: mixed (includes real material): UI screenshot, screen recording
  - UI screenshot: a light UI panel holding 11 text items (11 of them small type)
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 66% flat colour blocks, 95% of pixels use only 22 colours, 35% axis-aligned edges
  - Per-frame sharpness oscillates periodically (period None frames, correlation 0.00) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed; real material the user must supply: UI screenshot (part of the frame x0% y0% w100% h55%), screen recording (part of the frame)

</details>

<details class="ref"><summary>#23 00:36.458–00:36.958 · live action + code / editor overlays (text labels); brings in real material (live footage)</summary>

![shot_023](shots/shot_023.jpg)

**Visible on screen** (check against the frames)
- Picture: Very short presenter shot. Caption: UPS.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.3 stops); soft light (almost no lit / shadow edge)
- Text track (text/middle): UPS.
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 62%, AI-generated video 15%, 3D render 6% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 54% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.12, 126 colours, 24% flat blocks

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#24 00:36.958–00:38.208 · code / template render</summary>

![shot_024](shots/shot_024.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas: Opportunity Recalculator and CRM Integration nodes. Caption: PUT ALL THE LEADS
- Text track (text in the picture/middle): Opportunity Recalculator
- Text track (text in the picture/middle): CRM Integration / create:lead
- Text track (text in the picture/middle): PUT ALLTHELEADS / INTO THECRM, / INTOTHECRM
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small labels
- [AI assistant review] The canvas moves as one rigid plane with a synthetic depth blur at the far edge: drawn, not filmed
- [AI assistant review] No sensor noise or room lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 52%, still image + pan/zoom 28%, screen recording / screenshot 11% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Whole frame moves as one rigid transform (100% inliers, 0.11px residual, no local motion) → pan/zoom on a still image: zoom +0.2%/s, pan 9px/s
  - Rendered texture: 50% flat colour blocks, 95% of pixels use only 17 colours, 37% axis-aligned edges

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#25 00:38.208–00:39.583 · live action + code / editor overlays (subtitles, static graphics); brings in real material (live footage)</summary>

![shot_025](shots/shot_025.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): THEN / GOTO / Execu / Value Calculator
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 49%, AI-generated video 21%, 3D render 8% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 53% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.13, 126 colours, 24% flat blocks
  - Per-frame sharpness oscillates periodically (period 6 frames, correlation 0.29) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Source is live action: reshoot per the shooting plan (shot size / camera setup / lighting); run rea-video plan --mode ai to remake with AI instead; real material the user must supply: live footage (whole frame)

</details>

<details class="ref"><summary>#26 00:39.583–00:43.208 · code / template render</summary>

![shot_026](shots/shot_026.jpg)

**Visible on screen** (check against the frames)
- Picture: Full-frame workflow canvas: Value Calculator and deal nodes with a CRM node, the view drifting down.
- Text track (text in the picture/middle): Execute P / Value Calculator / CALCULATOR. / Execute Puro
- [AI assistant review] Flat vector node graph on a dark dotted canvas: rounded square nodes with icons, thin curved connectors, small labels
- [AI assistant review] The canvas moves as one rigid plane with a synthetic depth blur at the far edge: drawn, not filmed
- [AI assistant review] No sensor noise or room lighting on the graphic

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: code / template render 71%, 3D render 12%, 2D animation 6% (fused_agent)
- Material: rendered by the creator
- Basis (tool measurements, not necessarily visible to the eye):
  - Rendered texture: 62% flat colour blocks, 95% of pixels use only 12 colours, 22% axis-aligned edges
  - Per-frame sharpness oscillates periodically (period 2 frames, correlation 0.17) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

- Remake: Code render: have a strong coding model (such as Claude Opus 5.5 or later, or the Gemini 4 series) rebuild it in code from the rhythm, key frames and layout, optionally on an HTML video framework such as HyperFrames or Remotion; 100% controllable, no video model needed

</details>

<details class="ref"><summary>#27 00:43.208–00:52.417 · live action + code / editor overlays (subtitles, static graphics); brings in real material (live footage)</summary>

![shot_027](shots/shot_027.jpg)

**Visible on screen** (check against the frames)
- Picture: Presenter at the desk for the closing lines, the longest shot in the video.
- Acting: deadpan (light) · neutral brows, eyes to camera, slight smirk on some lines
- Camera / lighting: medium shot; moving camera (gimbal / handheld pan); night / low-light ambient, no dedicated fill; key light frontal (from the camera side; both sides of the subject about equally bright); lighting ratio about 1.2:1 (0.2 stops); soft light (almost no lit / shadow edge)
- Text track (subtitle/middle): THIS IS GREAT / HAVE / MANUAL / LABOR
- Motion beats within the shot: 46.00s
- [AI assistant review] The same man (wavy brown hair, olive tee, wristwatch), mesh office chair, white desk and vertical teal light tube appear in every filmed shot
- [AI assistant review] Natural hand gestures with real motion blur, correct fingers and a stable watch
- [AI assistant review] The dark room, chair mesh and light tube keep their geometry from shot to shot

**How it was made, as inferred by the tools** (inferred, not seen)
- Inference: live action 49%, AI-generated video 21%, 3D render 9% (fused_agent)
- Material: the user's real material: live footage
- Basis (tool measurements, not necessarily visible to the eye):
  - Low-light shot: 53% of the frame is near-black but grainy (not a solid fill), flat blocks cover only 6% of the lit part, and there is a face: the flat blocks / small palette come from crushed shadows, not counted as rendered texture
  - Photographic texture: noise σ=0.13, 127 colours, 24% flat blocks
  - Per-frame sharpness oscillates periodically (period 6 frames, correlation 0.05) with no duplicate frames: frame interpolation / rate conversion, or just the rhythm of a re-encode (transcodes whose platform tags were stripped show it too); not enough on its own to call AI

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
