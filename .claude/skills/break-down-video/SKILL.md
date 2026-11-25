---
name: break-down-video
description: Break down a video shot by shot into a report and a VIDEO.md package. Use when the user gives a video link or file and asks how it was made, how it was edited, whether it was filmed or made with AI, or says "break down this video".
---

# Break down a video

You run two commands and do one job by eye in between. The job by eye is what makes the result trustworthy, so do
not skip it unless the user asks for speed.

## 1. Setup (once)

If `.venv/bin/rea-video` does not exist, run `python3 breakdown_machine/install.py`. It needs ffmpeg and a Python
between 3.10 and 3.13 (it finds one, or asks `uv` for one). Tell the user plainly if something is missing.

## 2. First pass

```bash
python3 breakdown_machine/run.py <link or file> --name <short-name>
```

- A link is downloaded first. If the site refuses (Instagram often does without a login), ask the user to save
  the video and give you the file, or to allow `--cookies-from-browser chrome`. Do not try other downloaders.
- It is slow: about 15 to 20 minutes for a 60 second video on a laptop. Tell the user before you start, run it in the background and wait. The first run also downloads about 220 MB of sound models.
- Output lands in `runs/<short-name>/`.

## 3. The review (you are the eyes)

The first pass measures pixels and sound. On a video downloaded from a platform the compression wipes out the
evidence it uses, so it often calls filmed footage "AI". You fix that by looking.

1. Look at `runs/<name>/storyboard.jpg` for the whole video at a glance.
2. Open `runs/<name>/review_tasks.json`. Its instructions are written in Chinese (read them, they are the full
   rules; the engine's own guide is `.engine/rea-video/skills/rea-video/references/review.md`). In short: for every
   shot, look at the image in `images.sheet` and judge how the base picture was made.
3. Fill in every shot in `runs/<name>/review_answers.json`:
   - `label_probs`: how sure you are it is `live_action`, `ai_video`, `avatar` and so on. They should add up to 1.
   - `image_source`: for example `camera`, `screen_recording`, `ai`, `code`.
   - `evidence`: two to four things you can actually see (the same person, room and props across shots; real
     handwriting; warped hands; text that morphs). Never write evidence you did not see.
   - `description`: one or two sentences of what is on screen.
   - Fill the whole-video blocks too (`aspects`, `story`, `cast`) where you can see the answer. Leave a field empty
     instead of guessing.
4. If a shot is unclear, zoom in with the `zoom_cmd` from the tasks file before deciding.

Do the review yourself, shot by shot. Do not copy the tool's first guess into the answers.

## 4. Finish

```bash
python3 breakdown_machine/run.py --finish runs/<name>
```

It merges your review, checks `VIDEO.md` against the format, skins the report and prints the verdict.

The engine trusts its own measurements a lot, so a shot can keep a wrong verdict even after your review (a filmed
presenter still called "AI video", a split-screen shot called "3D render"). When you can see it is wrong, or the user
tells you they filmed it, set it by hand and say so in the note:

```bash
python3 breakdown_machine/run.py --correct runs/<name> --shots 4,18,29 --label live_action --note "why"
```

Labels: `live_action`, `ai_video`, `avatar`, `cg_3d`, `code_render`, `screen_capture`, `still_motion`, `static_hold`,
`anim_2d`, `stop_motion`, `film_footage`. For a split-screen shot, label the base picture (the filmed person), and
list the insert under `embedded_assets` in your review.

## 5. Tell the user

- The one-line verdict and the confidence.
- Where the two outputs are: `runs/<name>/report.html` (for them) and `runs/<name>/VIDEO.md` (for you).
- Any open questions listed at the top of `VIDEO.md`.
- Offer the next step once: "Want me to turn this into an editing skill?" (the `video-to-skill` skill).

## Rules

- Read `VIDEO.md` first and open only the files its map points to. Do not load `breakdown.json` to answer a question.
- Report numbers as the breakdown gives them. A camera position, a focal length or a light's distance is an
  estimate from the picture: say so.
- This is for learning how a video was put together and making your own with material you have the rights to.
  Never help repost someone else's video.
