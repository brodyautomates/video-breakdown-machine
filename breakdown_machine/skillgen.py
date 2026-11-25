"""Turn a breakdown into an editing skill your AI can use.

    python3 breakdown_machine/skillgen.py check    runs/NAME            is the breakdown complete?
    python3 breakdown_machine/skillgen.py facts    runs/NAME            print the measured numbers
    python3 breakdown_machine/skillgen.py scaffold runs/NAME [--name N] write runs/NAME/skill/SKILL.md to fill in
    python3 breakdown_machine/skillgen.py lint     runs/NAME/skill/SKILL.md   is the finished skill usable?

The script does the part that must be exact: it reads the numbers the engine measured and writes them into the
skill, so no number in a skill is typed from memory. The AI does the part that needs judgement: it fills each
marked section from the breakdown's files (the video-to-skill skill tells it how).
"""
import argparse
import re
import statistics
import sys
from pathlib import Path

from common import die, load_breakdown, rel, say, slugify

NEEDED = ["VIDEO.md", "breakdown.json", "video/timeline.md", "video/look.md", "video/rhythm.md",
          "video/packaging.md", "video/sound.md", "video/content.md"]
FILL = "<!-- FILL"
SECTIONS = ["Camera motion", "Cut rhythm", "Captions", "Sound", "Procedure", "QA"]


def g(d, *keys, default=None):
    for k in keys:
        if not isinstance(d, dict) or k not in d:
            return default
        d = d[k]
    return d


def pct(x):
    return f"{round(100 * float(x))}%"


def shares(d, top=3):
    if not isinstance(d, dict) or not d:
        return "not measured"
    items = sorted(d.items(), key=lambda kv: -float(kv[1]))[:top]
    return ", ".join(f"{k.replace('_', ' ')} {pct(v)}" for k, v in items if float(v) > 0.005)


def facts(out: Path) -> dict:
    b = load_breakdown(out)
    src, summ, aud, asp = b.get("source", {}), b.get("summary", {}), b.get("audio", {}), b.get("aspects", {})
    shots = b.get("shots", [])
    durs = [float(s.get("duration", 0)) for s in shots if s.get("duration")]
    dur = float(src.get("duration") or summ.get("duration") or sum(durs) or 0)
    fps = float(src.get("fps") or 0)
    cues = g(b, "packaging", "text_cues", default=[]) or []
    cue_len = [float(c["t1"]) - float(c["t0"]) for c in cues if "t0" in c and "t1" in c]
    cue_words = [len(str(c.get("text", "")).split()) for c in cues]
    cue_y = [c["bbox_median"][1] + c["bbox_median"][3] / 2 for c in cues if isinstance(c.get("bbox_median"), list) and len(c["bbox_median"]) == 4]
    sfx = g(aud, "sfx", "events", default=[]) or []
    ed = asp.get("editing", {})
    light = asp.get("lighting", {})
    first3 = {
        "cuts": sum(1 for s in shots[1:] if float(s.get("start", 9e9)) < 3.0),
        "captions": sum(1 for c in cues if float(c.get("t0", 9e9)) < 3.0),
        "sfx": sum(1 for e in sfx if float(e.get("t", 9e9)) < 3.0),
        "first_cut_s": round(float(shots[1]["start"]), 2) if len(shots) > 1 else None,
        "first_caption_s": round(min((float(c["t0"]) for c in cues), default=-1), 2) if cues else None,
    }
    return {
        "name": Path(src.get("filename") or out.name).stem,
        "tool": f"{g(b, 'tool', 'name', default='rea-video')} {g(b, 'tool', 'version', default='')}".strip(),
        "duration": round(dur, 3), "size": f"{src.get('width')}x{src.get('height')}", "aspect": src.get("aspect_ratio"),
        "fps": round(fps, 3), "frames": round(dur * fps) if fps else None,
        "shots": len(shots), "cuts": max(0, len(shots) - 1),
        "transitions": {k: v for k, v in (summ.get("transitions") or {}).items() if k != "start"},
        "mix": {m.get("label", "?"): m.get("ratio", 0) for m in summ.get("production_mix", [])},
        "overlays": summ.get("overlay_kinds") or [],
        "confidence": summ.get("confidence"),
        "reviewed": g(b, "analysis", "review", "by"),
        "cuts_per_min": ed.get("cuts_per_min", round(60 * max(0, len(shots) - 1) / dur, 1) if dur else None),
        "avg_shot": round(statistics.mean(durs), 2) if durs else None,
        "median_shot": round(statistics.median(durs), 2) if durs else None,
        "shot_range": (round(min(durs), 2), round(max(durs), 2)) if durs else None,
        "jump_cuts": ed.get("jump_cuts"), "punch_ins": ed.get("punch_ins"), "setups": ed.get("positions"),
        "cuts_in_pauses": ed.get("cuts_in_pauses"), "beat_synced": aud.get("beat_synced_edit"),
        "insert_share": ed.get("insert_share"),
        "format": g(asp, "format", "result", "format"),
        "shot_sizes": g(asp, "framing", "shot_sizes", default={}),
        "camera": g(asp, "camera", "support_shares", default={}),
        "light_setup": g(light, "result", "setup"), "light_ratio": g(light, "measured", "ratio"),
        "key_side": g(light, "measured", "key_side"), "light_words": light.get("words") or {},
        "grade_words": g(asp, "grade", "words", default={}),
        "caption_cues": len(cues),
        "cues_per_min": round(60 * len(cues) / dur, 1) if dur and cues else 0,
        "cue_median_s": round(statistics.median(cue_len), 2) if cue_len else None,
        "cue_max_words": max(cue_words) if cue_words else None,
        "cue_median_words": statistics.median(cue_words) if cue_words else None,
        "cue_y": round(statistics.median(cue_y), 3) if cue_y else None,
        "stickers": g(b, "packaging", "counts", "stickers", default=0),
        "sfx": len(sfx), "sfx_types": sorted({str(e.get("type")) for e in sfx}),
        "music": bool(g(aud, "music", "present", default=aud.get("music_likely"))), "bpm": aud.get("tempo_bpm"),
        "voice_share": g(aud, "voice", "ratio"),
        "rms": aud.get("rms_dbfs"), "peak": aud.get("peak_dbfs"), "silence": aud.get("silence_ratio"),
        "first3": first3,
    }


def facts_md(f: dict) -> str:
    r = f["shot_range"] or ("?", "?")
    trans = ", ".join(f"{v} {k}" for k, v in f["transitions"].items()) or "none recorded"
    rows = [
        ("Duration", f"{f['duration']} s" + (f" ({f['frames']} frames at {f['fps']} fps)" if f["frames"] else "")),
        ("Size", f"{f['size']}, {f['aspect']}"),
        ("Format", str(f["format"] or "not classified").replace("_", " ")),
        ("How it was made", shares(f["mix"], 5)),
        ("Shots and cuts", f"{f['shots']} shots, {f['cuts']} cuts ({trans})"),
        ("Cut rate", f"{f['cuts_per_min']} cuts per minute. Shot length: average {f['avg_shot']} s, median {f['median_shot']} s, range {r[0]} to {r[1]} s"),
        ("First 3 seconds", f"{f['first3']['cuts']} cuts, {f['first3']['captions']} captions, {f['first3']['sfx']} sound effects. First cut at {f['first3']['first_cut_s']} s, first caption at {f['first3']['first_caption_s']} s"),
        ("Set-ups", f"{f['setups']} camera set-up(s). Jump cuts {f['jump_cuts']}, punch-ins {f['punch_ins']}. Inserts {pct(f['insert_share'] or 0)} of runtime"),
        ("Framing", shares(f["shot_sizes"])),
        ("Camera", shares(f["camera"])),
        ("Light", f"{str(f['light_setup'] or 'not measured').replace('_', ' ')}; key from {f['key_side'] or '?'}; ratio {f['light_ratio']}:1" if f["light_setup"] else "not measured (no filmed shots)"),
        ("Grade", "; ".join(str(v) for v in list(f["grade_words"].values())[:4]) or "not measured"),
        ("On-screen text (captions plus any text read in the picture)", f"{f['caption_cues']} cues, {f['cues_per_min']} per minute, median {f['cue_median_s']} s on screen, median {f['cue_median_words']} words (max {f['cue_max_words']}), centre height y = {f['cue_y']}" if f["caption_cues"] else "none found"),
        ("Stickers and picture-in-picture", str(f["stickers"])),
        ("Sound effects", f"{f['sfx']} ({', '.join(f['sfx_types'])})" if f["sfx"] else "none found"),
        ("Music", (f"yes, {f['bpm']} BPM" if f["bpm"] else "yes") if f["music"] else "none"),
        ("Cuts on speech pauses", pct(f["cuts_in_pauses"]) if f["cuts_in_pauses"] is not None else "not measured"),
        ("Loudness", f"{f['rms']} dBFS average, {f['peak']} dBFS peak, silence {pct(f['silence'] or 0)}"),
        ("Confidence", f"{f['confidence']} overall" + (f", shots reviewed by {f['reviewed']}" if f["reviewed"] else ", no visual review")),
    ]
    out = ["| Item | Measured value |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in rows]
    return "\n".join(out)


TEMPLATE = """---
name: {skill}
description: {fill} one or two sentences: what kind of video this skill builds and when to use it. Start with a verb. -->
---

# {title}

{fill} two or three sentences: what the reference video is and why it works. Read video/content.md and the top of VIDEO.md. -->

**Where the numbers come from.** A breakdown of `{name}` made by {tool} with the Video Breakdown Machine. Every value
in this skill is tagged **measured** (computed from the file), **seen** (visible in the breakdown's frames) or
**inferred** (a reading; treat it as a default, not a fact).

## Source facts (measured)

{facts}

## 1. Shoot and lighting

{fill} for filmed shots only: the set, where the camera is, the light (direction, quality, ratio), what to copy and what
is incidental. Read video/look.md and look at shots/ frames. If nothing was filmed, say how the pictures were made instead
(AI, code, screen recording) and what to prepare. -->

## 2. Framing

{fill} shot sizes, where the subject sits in frame, headroom, how framing changes across cuts. Read video/look.md. -->

## 3. Camera motion

{fill} every kind of movement and its size: reframe steps at cuts, push-ins, pans, handheld float, zooms on inserts.
Give numbers (px per second, percent scale change, duration, easing) and say how to apply each to new footage.
Read video/look.md, video/rhythm.md and the per-shot files in video/shots/. -->

## 4. Cut rhythm

{fill} cut rate over time (does it speed up?), shot lengths by section, what triggers a cut (pause, beat, new idea),
transitions. Include the first 3 seconds beat by beat. Read video/rhythm.md and video/timeline.md. -->

## 5. Story beats

{fill} the structure as reusable beats with times: hook, promise, steps, payoff, call to action. Read video/content.md.
Describe the job each beat does. Do not copy the script. -->

## 6. Captions and on-screen text

{fill} position, size, words per caption, timing against the voice, colour, highlight, how text enters and leaves,
stickers and picture-in-picture. Read video/packaging.md. -->

## 7. Sound

{fill} voice level, music (yes or no, BPM, level under the voice), each sound effect type and what it lands on.
Read video/sound.md. -->

## 8. Grade

{fill} the look in plain words plus the measured values. Read video/look.md. -->

## 9. Procedure

{fill} numbered steps to build a new video this way from raw material, in order. Each step names the numbers above it
depends on. -->

## 10. QA checks

{fill} a checklist a render must pass, each one measurable (cut rate within a range, caption count per minute, first cut
before N seconds, and so on). Check the render, not the plan. -->

## What the breakdown does not settle

{fill} the open questions from VIDEO.md and anything you could not verify from the frames. -->
"""


def cmd_check(out: Path) -> bool:
    missing = [n for n in NEEDED if not (out / n).exists()]
    for n in missing:
        say(f"missing  {n}")
    if missing:
        say(f"{rel(out)} is not a complete breakdown. Run: python3 breakdown_machine/run.py --finish {rel(out)}")
        return False
    say(f"ok   {rel(out)} is a complete breakdown")
    return True


def cmd_scaffold(out: Path, name):
    if not cmd_check(out):
        sys.exit(1)
    f = facts(out)
    skill = slugify(name or f"edit-like-{f['name']}")
    title = f"Edit like \"{f['name']}\""
    target = out / "skill" / "SKILL.md"
    if target.exists() and FILL not in target.read_text(encoding="utf-8"):
        die(f"{rel(target)} already exists and is finished. Delete it first if you want a new one.")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEMPLATE.format(skill=skill, title=title, name=f["name"], tool=f["tool"], facts=facts_md(f), fill=FILL + ":"),
                      encoding="utf-8")
    say(f"ok   wrote {rel(target)} with the measured facts filled in")
    say(f"NEXT: fill every section marked '{FILL}' from the breakdown's files, then run:")
    say(f"  python3 breakdown_machine/skillgen.py lint {rel(target)}")


def cmd_lint(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    problems = []
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        problems.append("no front matter block at the top (--- name / description ---)")
    else:
        fm = m.group(1)
        if not re.search(r"^name:\s*[a-z0-9][a-z0-9-]{2,63}\s*$", fm, re.M):
            problems.append("front matter: name must be lowercase letters, digits and hyphens")
        d = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not d or len(d.group(1)) < 40:
            problems.append("front matter: description is missing or too short to tell an AI when to use the skill")
        elif len(d.group(1)) > 1024:
            problems.append("front matter: description is over 1024 characters")
    left = text.count(FILL)
    if left:
        problems.append(f"{left} section(s) still hold a FILL marker")
    for s in SECTIONS:
        if not re.search(rf"^##+ .*{re.escape(s)}", text, re.M | re.I):
            problems.append(f"no section heading containing \"{s}\"")
    body = text[m.end():] if m else text
    cam = re.search(r"^## .*Camera motion.*?\n(.*?)(?=^## |\Z)", body, re.M | re.S | re.I)
    if cam and len(re.findall(r"\d", cam.group(1))) < 6:
        problems.append("the Camera motion section has almost no numbers: give sizes, speeds and durations")
    tags = len(re.findall(r"\b(measured|seen|inferred)\b", body, re.I))
    if tags < 8:
        problems.append(f"only {tags} values are tagged measured / seen / inferred: tag where each number comes from")
    if re.search(r"(/Users/|/home/|C:\\\\Users\\\\)", text):
        problems.append("contains a personal file path: use paths relative to the breakdown folder")
    lines = text.count("\n")
    if lines > 600:
        problems.append(f"{lines} lines: over 600. Cut repetition so an AI can read it in one go")
    if lines < 80:
        problems.append(f"only {lines} lines: too thin to edit from")
    for p in problems:
        say(f"fix  {p}")
    say("ok   the skill passes" if not problems else f"{len(problems)} thing(s) to fix in {rel(path)}")
    return not problems


def main():
    ap = argparse.ArgumentParser(description="Turn a breakdown into an editing skill.")
    ap.add_argument("cmd", choices=["check", "facts", "scaffold", "lint"])
    ap.add_argument("path")
    ap.add_argument("--name", help="skill name (scaffold only)")
    a = ap.parse_args()
    p = Path(a.path).expanduser().resolve()
    if a.cmd == "check":
        sys.exit(0 if cmd_check(p) else 1)
    if a.cmd == "facts":
        print(facts_md(facts(p)))
    elif a.cmd == "scaffold":
        cmd_scaffold(p, a.name)
    else:
        sys.exit(0 if cmd_lint(p) else 1)


if __name__ == "__main__":
    main()
