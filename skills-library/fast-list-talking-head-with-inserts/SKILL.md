---
name: fast-list-talking-head-with-inserts
description: Cut a scripted talking-head list video (9:16, about 60 seconds) where every claim gets its own picture within a second: the presenter full frame, a split with an insert on top and the presenter below, and full-frame motion graphics, rotating at 26 cuts a minute with one-word captions. Use when the user has a talking-head take that lists features, steps or examples and wants it fast, visual and deadpan.
---

# Fast list video: presenter, split inserts and full-frame diagrams

The reference is a 64 second vertical video: one man on a sofa lists the steps of an absurd automation. He never
leaves the couch, but the picture changes every two seconds, because each step is shown as a branch of one workflow
diagram or as a fake screenshot. The list is the script; the edit is what makes it watchable.

**Where the numbers come from.** A breakdown of `tuesday-simulator` made by rea-video 0.1.0 with the Video Breakdown
Machine. Every value in this skill is tagged **measured** (computed from the file), **seen** (visible in the
breakdown's frames) or **inferred** (a reading; treat it as a default, not a fact).

## Source facts (measured)

| Item | Measured value |
|---|---|
| Duration | 63.856 s (1531 frames at 23.976 fps) |
| Size | 1080x1920, 9:16 |
| Format | talking head |
| How it was made | live action 74%, code render 26% |
| Shots and cuts | 29 shots, 28 cuts (26 cut, 1 glitch, 1 jump) |
| Cut rate | 26.3 cuts per minute. Shot length: average 2.2 s, median 2.08 s, range 0.46 to 4.3 s |
| First 3 seconds | 1 cuts, 5 captions, 0 sound effects. First cut at 2.46 s, first caption at 0.0 s |
| Set-ups | 3 camera set-up(s). Jump cuts 1, punch-ins 0. Inserts 26% of runtime |
| Framing | medium shot 100% |
| Camera | moving 51%, fixed 49% |
| Light | soft front; key from right; ratio 1.243:1 |
| Grade | natural (close to the original colours); normal saturation; normal contrast; normal blacks |
| On-screen text (captions plus any text read in the picture) | 294 cues, 276.2 per minute, median 0.5 s on screen, median 1.0 words (max 11), centre height y = 0.437 |
| Stickers and picture-in-picture | 6 |
| Sound effects | none found |
| Music | none |
| Cuts on speech pauses | 56% |
| Loudness | -17.1 dBFS average, -1.2 dBFS peak, silence 0% |
| Confidence | 0.756 overall, shots reviewed by claude |

Two rows need a note. "On-screen text" counts every piece of text the engine read, including the labels inside the
workflow diagrams, so 276 per minute is not the caption rate; the spoken-word captions are in section 6. "Sound effects: none
found" and "Music: none" are what the engine found on a platform download with the voice on top; the review did not
listen to the sound (see the last section).

## 1. Shoot and lighting

**Set (seen).** One location: an office lounge, teal sofa, wood wall and a glass partition behind. The presenter sits
with a laptop on his knee and talks to camera. One wardrobe, one seat, no props beyond the laptop.

**Camera (seen, the set-up count is measured as 3).** Two framings of the same seat: a wide shot with the knees and
coffee table in frame, and a medium shot from the chest up. It reads as one take filmed wide and punched in, or two
cameras. Camera on a tripod at seated eye level: 12 of 12 presenter shots are static (measured), drift under 1% zoom.

**Light (measured unless marked).**
- Soft, frontal, from above. Ratio 1.2:1, so almost no shadow side on the face.
- Warm on the subject (about 3000 to 4000K), cooler behind: mixed sources.
- No key light, rim light or practical is visible (seen). This is available light, not a lit set.

**What to copy.** A clean, bright, ordinary room, a locked-off camera and two framings. **What is incidental.** The
sofa, the office, the laptop.

**To prepare besides the take.** One diagram of your system or process that every step can be a branch of, and one
screenshot or mock screenshot for each claim that needs proof. In the reference 10 of 29 shots use a split and 7 are
full-frame graphics: 17 of 29 shots, 63% of the runtime, has an insert on screen (measured from shot labels and
lengths; the label of each layout is seen).

## 2. Framing

| Layout | Shots | Face height | Face centre | Notes |
|---|---|---|---|---|
| Presenter, medium | 11 | 12 to 13% of frame height (measured) | x 0.50 to 0.53, y 0.51 (measured) | Head and chest, hands in frame |
| Presenter, wide | 1 (shot 2) | 8% (measured) | x 0.47, y 0.51 (measured) | Knees and table in frame. Used once, in the hook |
| Split | 10 | 12 to 13% (measured) | y 0.67 (measured) | Insert fills the top 45% or so; presenter is the same medium framing, moved down (seen) |
| Full-frame graphic | 7 | none | none | The diagram or screenshot fills the frame (seen) |

- The presenter's face is the same size in the medium and the split layouts (measured). Only its height in the frame
  changes: y 0.51 full frame, y 0.67 in the split. Build the split by sliding the same shot down, not by scaling it.
- The face stays centred left to right in every layout, within 0.03 of frame width (measured).

## 3. Camera motion

There are three kinds of movement, and they belong to different layouts.

**A. The presenter does not move (measured).** All 12 presenter shots are static: zoom between -0.14 and +0.51% per
second, net zoom under 1.2% over a shot, pan under 10 px per second. Do not add a push-in or a handheld effect to the
presenter. If the footage is on a tripod, leave it. If it is handheld, stabilise it.

**B. Full-frame graphics always move (measured).** All 7 graphic shots drift. Three kinds:
- Slow pan across the diagram: 5 to 20 px per second, no zoom (shots 3, 7, 11). The default.
- Push-in on one node: 2.0 to 3.4% per second, 2.7 to 6.3% over the shot, with a pan of 11 to 45 px per second
  (shots 9, 15, 16). Use it when the line names one specific thing.
- Slight pull-back with a pan: about -1.2% per second, 18 px per second (shot 17). Use it to show the whole again.
The move is linear and rigid (the whole frame moves as one plane), with a soft blur on the far edge of the diagram
(seen). On your own diagram: render it larger than the frame, then keyframe position and scale linearly across the
whole shot. No easing, no bounce.

**C. Inside a split, only the top panel moves (measured and seen).** 6 of 10 splits hold the insert still
(under 0.5% zoom, under 12 px per second). The other 4 animate the insert: a push-in of 4.1% per second (shot 5), a
pan of 9 to 50 px per second (shots 22, 26) and one pull-out of 14% per second that reveals the full listing grid
(shot 19, net -35%). The presenter half never moves.

**How to apply it.** Decide the layout for each line first (section 4). Then: presenter shots get nothing; a graphic
gets a pan, or a push-in if the line names one item; a split gets a still insert unless the insert is a screen
recording that scrolls or types on its own.

## 4. Cut rhythm

**Rate (measured).** 28 cuts in 64 seconds: 26.3 per minute. Shots average 2.2 s, median 2.1 s, shortest 0.46 s,
longest 4.3 s. 26 are hard cuts; there are no dissolves or wipes between layouts.

**The rule that carries the video (seen in the shot order).** No layout is held for two shots in a row for long. The
order of the 29 shots, F = presenter full frame, S = split, G = full-frame graphic:

```
F F G S S F G F G F G F S F G G G F S S S S F S F S F S F
```

- A presenter shot is almost always followed by an insert (S or G). The presenter is the reset between proofs.
- Runs of the same layout (G G G at 31 to 37 s, S S S S at 39 to 48 s) are different pictures inside the same layout:
  a new node or a new screenshot each time.
- Shot length by layout (measured): presenter median 1.8 s, split median 2.2 s, graphic median 2.5 s. The inserts get
  the time; the presenter gets the least.

**Where cuts land (measured).** 56% of cuts fall in a pause of the speech. The rest cut mid-sentence, on the word
that names the thing being shown. Cut on the noun, not on the breath.

**The first 3 seconds (measured times, seen content).**

| Time | What happens |
|---|---|
| 0.0 s | Wide shot. He is already talking. The finished workflow floats in a panel above his head. First caption on screen at 0.0 s |
| 0.5 to 2.1 s | Captions change four times, one or two words each |
| 2.46 s | First cut, to the same wide framing with the name of the thing in big letters |
| 3.84 s | Second cut: the first full-frame graphic. The presenter is gone for 3 seconds |

So the hook is one held shot of 2.5 s, not a fast cut: the movement in the first seconds comes from the floating
panel and the captions. The first layout change is at 3.8 s.

**Pace over time (measured from cut times).** Cuts in each 10 seconds: 4, 5, 4, 5, 5, 5, then 0 in the last 4 s.
It does not build to a faster finish. It holds roughly one pace and ends on a 4.3 s presenter shot for the call to action.

## 5. Story beats

Jobs, with the reference's times. Refill each with your own material.

| Time | Job | How the reference does it |
|---|---|---|
| 0 to 3.8 s | Hook | Shows the finished system in frame while naming it, and gives it an absurd, memorable name |
| 3.8 to 10.3 s | First item, in full | Step as a diagram, the same step explained in a split, then the result as a fake screenshot. This first item teaches the viewer the three layouts |
| 10.3 to 37 s | Items 2 to 5 | Each item: one presenter line, one or two inserts. Proof alternates between a diagram branch and a mock screenshot or map |
| 37 to 48 s | The biggest claim | A presenter reset, then four splits in a row with real-looking listings and the big number on screen as it is said |
| 48 to 59.6 s | Quick items | Three more steps at the same pace, the last one the most useful-sounding |
| 59.6 to 63.9 s | Call to action | Presenter, medium shot, 4.3 s, the longest presenter shot in the video |

One diagram runs through all of it: every item is another branch of the same workflow. That is what makes a list
feel like one system (inferred from the frames).

## 6. Captions and on-screen text

**Spoken-word captions (measured from 123 caption cues of one to three words).**
- One word at a time, sometimes two. Median on screen 0.4 s; a new caption about every 0.5 s (about 115 a minute).
- Heavy italic capitals, white, with a soft glow (seen). Line height about 3.7% of frame height, about 70 px at 1920.
- Hard in, hard out. No bounce or fade on the main captions.
- Position: y = 0.63 of frame height on presenter shots, and on the seam of the split (y 0.54 to 0.63), so the same
  caption line works in every layout. Never in the bottom fifth.
- Key words are held longer and larger: the name of the thing is on screen for 1.3 s at about 92 px (2.5 to 3.8 s).

**Text inside inserts (seen).** Diagram nodes carry short labels in small capitals (about 35 to 50 px). Mock
screenshots use the real app's type. This text is part of the picture: do not caption over it.

**Persistent layers (measured).** 6 small stickers or images stay on screen across several cuts (for example 8.4 to
12.4 s and 20.3 to 26.1 s). Lay each on once for its whole span, not shot by shot.

## 7. Sound

- Voice: one continuous recording laid under all the pictures (measured: the background sound does not reset at cuts).
  Voice is present for 57% of the runtime. Average level -17.1 dBFS, peak -1.2 dBFS, no silence (measured).
- Music: the engine marks music-like sound in three stretches (17.5 to 25 s, 35 to 41 s, 57.5 to 59.5 s) but calls
  the track not present overall, and found no tempo (measured). Treat music as unknown.
- Sound effects: none found on the effects track (measured). On a compressed download quiet effects under a voice
  are often missed, so this is "none loud enough to find", not "none".
- Default for a new edit (inferred): voice at about -16 LUFS, no music or a very low bed, a soft click on each
  insert's entrance if you want any effects at all.

## 8. Grade

Natural: normal saturation, normal contrast, normal blacks, neutral overall (measured). Teal in the sofa and warm wood
behind give the only colour contrast (seen). The graphics are dark grey with white lines and small coloured icons
(seen), so every cut from presenter to graphic is also a cut from bright to dark. Keep that contrast: do not put the
diagram on a light background if the room is light.

## 9. Procedure

1. **List the claims.** One line per item of the script. Mark the one that is the biggest claim.
2. **Give every line a layout** using section 4: presenter for the line that introduces an item, an insert (split or
   graphic) for the line that explains or proves it. Check the order string: no presenter shot longer than about
   2.5 s outside the hook and the call to action, and no more than one presenter shot between inserts.
3. **Build the inserts.** One diagram that all items branch from (render it at 2x frame size so it can pan), and one
   screenshot, mock or screen recording per proof line.
4. **Cut the take to the lines** at about 26 cuts a minute (section 4): presenter shots near 1.8 s, splits near 2.2 s,
   graphics near 2.5 s. Cut on the noun that names what the next picture shows.
5. **Place the layouts.** Split: insert on the top 45%, presenter slid down so the face centre is at y 0.67
   (section 2). Graphic: full frame.
6. **Add motion** by layout (section 3): nothing on the presenter, a linear pan or push-in on every graphic, still
   inserts in splits unless the insert moves by itself.
7. **Hook.** Open on the wide shot with the finished thing floating above the presenter's head. Hold 2.5 s. First
   layout change before 4 s.
8. **Captions** (section 6): one or two words, heavy italic capitals, y 0.63, hard in and out, about 115 a minute.
   Hold the key term for a second or more.
9. **Sound** (section 7): one continuous voice track under everything.
10. **End** on the presenter, medium shot, 4 s or a little more, with the offer.

## 10. QA checks

Check the render, not the plan.

- Cut rate between 22 and 30 per minute. Median shot between 1.7 and 2.5 s. No shot over 4.5 s.
- First cut before 3 s, first layout change before 4 s, a caption on screen in the first 0.2 s.
- An insert (split or graphic) on screen for 55 to 70% of the runtime.
- No two presenter shots in a row after the hook, except a cut between the wide and the medium framing.
- Presenter shots: net zoom under 1.5%, no added shake. Graphic shots: every one moves (pan over 5 px per second or
  zoom over 1% per second).
- Face centred within 0.03 of frame width in every presenter and split shot; face centre at y 0.67 in splits.
- Captions: one to three words, on screen 0.3 to 0.6 s on average, never below y 0.8, never over text in an insert.
- The last shot is the presenter, at least 3.5 s.

## What the breakdown does not settle

- The engine's own verdict called two filmed shots "AI video" and four splits "3D render". They were corrected by
  hand after looking at the frames. The made-with mix (filmed 74%, graphics 26%) is after that correction.
- Splits are counted as filmed shots, because the base picture is the presenter. The 26% "code render" is only the
  7 full-frame graphics.
- No one listened to the sound. Music and effects are from measurement only, and it marks the voice as possibly
  text-to-speech, which is wrong for this video.
- Whether the two framings are one take punched in or two cameras cannot be told from the frames.
- This is one video. Break down three to five in the same style before treating a number here as a rule.
