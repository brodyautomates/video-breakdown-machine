"""Break down one video.

    python3 breakdown_machine/run.py <link or file> [--name NAME]     step 1: download, break down, write review tasks
    python3 breakdown_machine/run.py --finish runs/NAME               step 2: merge the review, skin the report, check
    python3 breakdown_machine/run.py --correct runs/NAME --shots 4,18 --label live_action    fix a verdict you are sure of

Step 1 measures the video (shots, cuts, camera, light, captions, sound) and writes a first verdict.
Between the two steps an AI that can see images (Claude Code) looks at every shot and fills in
runs/NAME/review_answers.json. That review is what makes the "filmed or AI" call reliable on videos downloaded
from Instagram or TikTok. Step 2 merges it and writes the final report and VIDEO.md.
"""
import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path

from common import ROOT, RUNS, die, exe, is_link, need_engine, need_tool, rel, run, say, slugify
import theme

LABELS = ["live_action", "ai_video", "avatar", "cg_3d", "code_render", "screen_capture", "still_motion", "static_hold",
          "anim_2d", "stop_motion", "film_footage"]


def engine_env() -> dict:
    """The engine keeps its notes inside this repo, not in your home folder."""
    env = dict(os.environ)
    env.setdefault("REA_VIDEO_HOME", str(ROOT / ".engine" / "home"))
    return env


def fetch(link: str, out: Path, name: str, cookies: str = "") -> Path:
    ytdlp = exe("yt-dlp")
    if not ytdlp.exists():
        die("yt-dlp is not installed. Run: python3 breakdown_machine/install.py")
    out.mkdir(parents=True, exist_ok=True)
    target = out / f"{name}.mp4"
    if target.exists():
        say(f"ok   already downloaded: {rel(target)}")
        return target
    say("     downloading the video")
    cmd = [ytdlp, "--no-playlist", "-f", "bv*+ba/b", "-S", "res,br", "--merge-output-format", "mp4",
           "--quiet", "--no-warnings", "-o", str(out / f"{name}.%(ext)s")]
    if cookies:
        cmd += ["--cookies-from-browser", cookies]
    r = run(cmd + [link], check=False, capture=True)
    if r.returncode != 0:
        print((r.stdout or "").strip()[-600:], file=sys.stderr)
        die("the download failed. Sites like Instagram sometimes refuse a download without a login. Two ways on:\n"
            "  1. save the video yourself and pass the file:  python3 breakdown_machine/run.py my-video.mp4\n"
            "  2. let it use your browser's login:            add  --cookies-from-browser chrome  (or safari, firefox)")
    if not target.exists():
        found = [p for p in sorted(out.glob(f"{name}.*")) if p.suffix.lower() in (".mp4", ".mov", ".mkv", ".webm")]
        if not found:
            die("the download finished but no video file was written. Private or removed videos cannot be fetched.")
        target = found[0]
    (out / "source.json").write_text(json.dumps({"link": link}, indent=1))
    say(f"ok   downloaded: {rel(target)}")
    return target


def logged(cmd, log: Path, what: str):
    """Run an engine step with its output in a log file; show the end of the log if it fails."""
    with open(log, "a", encoding="utf-8") as fh:
        fh.write(f"\n$ {' '.join(str(c) for c in cmd)}\n"); fh.flush()
        import subprocess
        r = subprocess.run([str(c) for c in cmd], stdout=fh, stderr=subprocess.STDOUT, env=engine_env())
    if r.returncode != 0:
        tail = log.read_text(encoding="utf-8", errors="replace")[-2500:]
        print(tail, file=sys.stderr)
        die(f"{what} failed. The full log is {rel(log)}")


def start(args):
    need_tool("ffmpeg")
    engine = need_engine()
    src = args.video
    if is_link(src):
        name = slugify(args.name or src.rstrip("/").split("/")[-1].split("?")[0])
        out = RUNS / name
        video = fetch(src, out, name, args.cookies_from_browser or "")
    else:
        video = Path(src).expanduser().resolve()
        if not video.exists():
            die(f"file not found: {src}")
        name = slugify(args.name or video.stem)
        out = RUNS / name
        out.mkdir(parents=True, exist_ok=True)
    log = out / "run.log"
    say(f"     breaking down {video.name}")
    say("     this is the slow part: about 15 to 20 minutes for a 60 second video on a laptop")
    t0 = time.time()
    logged([engine, "decompose", video, "-o", out, "--lang", "en"], log, "the breakdown")
    logged([engine, "review", out], log, "writing the review tasks")
    answers, blank = out / "review_answers.json", out / "review_answers.blank.json"
    if answers.exists() and not blank.exists():
        shutil.copy(answers, blank)
    shots = len(json.loads((out / "review_tasks.json").read_text(encoding="utf-8")).get("shots", [])) if (out / "review_tasks.json").exists() else "?"
    say(f"ok   first pass written to {rel(out)} in {round((time.time() - t0) / 60)} min ({shots} shots)")
    say("")
    say("NEXT (the review, done by the AI that is running this):")
    say(f"  1. Look at {rel(out)}/storyboard.jpg, then read {rel(out)}/review_tasks.json.")
    say(f"  2. For every shot, look at its sheet image and fill in its entry in {rel(out)}/review_answers.json.")
    say(f"  3. Run: python3 breakdown_machine/run.py --finish {rel(out)}")
    say("To skip the review (faster, less reliable on downloaded videos) run step 3 now.")


def finish(args):
    engine = need_engine()
    out = Path(args.finish).expanduser().resolve()
    if not (out / "breakdown.json").exists():
        die(f"{args.finish} is not a breakdown folder (no breakdown.json)")
    log = out / "run.log"
    answers, blank = out / "review_answers.json", out / "review_answers.blank.json"
    reviewed = answers.exists() and (not blank.exists() or answers.read_text() != blank.read_text())
    if reviewed:
        logged([engine, "apply-review", out, "--by", args.by, "--lang", "en"], log, "merging the review")
        say("ok   review merged into the verdict")
    else:
        say("note no review was filled in: the verdict is from measurements only")
    wrap_up(engine, out)


def correct(args):
    engine = need_engine()
    out = Path(args.correct).expanduser().resolve()
    if not args.shots or args.label not in LABELS:
        die("use: --correct runs/NAME --shots 4,18 --label <one of: " + ", ".join(LABELS) + ">")
    cmd = [engine, "correct", out, "--shots", args.shots, "--label", args.label]
    if args.note:
        cmd += ["--note", args.note]
    logged(cmd, out / "run.log", "the correction")
    say(f"ok   shots {args.shots} set to {args.label.replace('_', ' ')}")
    wrap_up(engine, out)


def wrap_up(engine, out: Path):
    check = run([engine, "videomd", out, "--check"], check=False, capture=True, env=engine_env())
    if check.returncode != 0:
        print(check.stdout[-2000:], file=sys.stderr)
        die("VIDEO.md did not pass the format check (details above)")
    say("ok   VIDEO.md passes the format check")
    theme.apply(out / "report.html")
    say("ok   report skinned")
    b = json.loads((out / "breakdown.json").read_text(encoding="utf-8"))
    s = b.get("summary", {})
    mix = ", ".join(f"{m.get('label', '?').replace('_', ' ')} {round(100 * m.get('ratio', 0))}%" for m in s.get("production_mix", []))
    say("")
    say(f"Verdict:    {mix}")
    say(f"Shots:      {s.get('shots')} ({s.get('avg_shot_s')} s average)")
    say(f"Confidence: {s.get('confidence')}")
    say("")
    say(f"Report for you:   {rel(out)}/report.html")
    say(f"Breakdown for AI: {rel(out)}/VIDEO.md")
    say("If a shot's verdict is wrong and you are sure (you can see it, or you filmed it), fix it with --correct.")
    say(f"Next: ask Claude Code to \"turn {rel(out)} into an editing skill\"")


def main():
    ap = argparse.ArgumentParser(description="Break down one video into a report and a VIDEO.md package.")
    ap.add_argument("video", nargs="?", help="a link (Instagram, TikTok, YouTube, ...) or a video file")
    ap.add_argument("--name", help="folder name under runs/ (default: from the link or file name)")
    ap.add_argument("--finish", metavar="DIR", help="step 2: merge the review and write the final report")
    ap.add_argument("--correct", metavar="DIR", help="set the verdict of some shots by hand")
    ap.add_argument("--shots", help="with --correct: shot numbers, for example 4,18,29")
    ap.add_argument("--label", help="with --correct: " + ", ".join(LABELS))
    ap.add_argument("--note", help="with --correct: why (kept in the report)")
    ap.add_argument("--cookies-from-browser", metavar="BROWSER",
                    help="use this browser's login for the download (chrome, safari, firefox)")
    ap.add_argument("--by", default="claude", help="who did the review (written into the report)")
    args = ap.parse_args()
    if args.correct:
        correct(args)
    elif args.finish:
        finish(args)
    elif args.video:
        start(args)
    else:
        ap.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()
