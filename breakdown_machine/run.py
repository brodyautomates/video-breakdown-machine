"""Break down one video.

    python3 breakdown_machine/run.py <link or file> [--name NAME]     step 1: download, break down, write review tasks
    python3 breakdown_machine/run.py --finish runs/NAME               step 2: merge the review, skin the report, check

Step 1 measures the video (shots, cuts, camera, light, captions, sound) and writes a first verdict.
Between the two steps an AI that can see images (Claude Code) looks at every shot and fills in
runs/NAME/review_answers.json. That review is what makes the "filmed or AI" call reliable on videos downloaded
from Instagram or TikTok. Step 2 merges it and writes the final report and VIDEO.md.
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

from common import ROOT, RUNS, die, exe, is_link, need_engine, need_tool, rel, run, say, slugify
import theme


def fetch(link: str, out: Path, cookies: str = "") -> Path:
    ytdlp = exe("yt-dlp")
    if not ytdlp.exists():
        die("yt-dlp is not installed. Run: python3 breakdown_machine/install.py")
    out.mkdir(parents=True, exist_ok=True)
    target = out / "source.mp4"
    if target.exists():
        say(f"ok   already downloaded: {rel(target)}")
        return target
    say("     downloading the video")
    cmd = [ytdlp, "--no-playlist", "-f", "bv*+ba/b", "-S", "res,br", "--merge-output-format", "mp4",
           "--quiet", "--no-warnings", "-o", str(out / "source.%(ext)s")]
    if cookies:
        cmd += ["--cookies-from-browser", cookies]
    r = run(cmd + [link], check=False, capture=True)
    if r.returncode != 0:
        print((r.stdout or "").strip()[-600:], file=sys.stderr)
        die("the download failed. Sites like Instagram sometimes refuse a download without a login. Two ways on:\n"
            "  1. save the video yourself and pass the file:  python3 breakdown_machine/run.py my-video.mp4\n"
            "  2. let it use your browser's login:            add  --cookies-from-browser chrome  (or safari, firefox)")
    if not target.exists():
        found = sorted(out.glob("source.*"))
        if not found:
            die("the download finished but no video file was written. Private or removed videos cannot be fetched.")
        target = found[0]
    (out / "source.json").write_text(json.dumps({"link": link}, indent=1))
    say(f"ok   downloaded: {rel(target)}")
    return target


def start(args):
    need_tool("ffmpeg")
    engine = need_engine()
    src = args.video
    if is_link(src):
        name = args.name or slugify(src.rstrip("/").split("/")[-1].split("?")[0])
        out = RUNS / name
        video = fetch(src, out, args.cookies_from_browser or "")
    else:
        video = Path(src).expanduser().resolve()
        if not video.exists():
            die(f"file not found: {src}")
        name = args.name or slugify(video.stem)
        out = RUNS / name
        out.mkdir(parents=True, exist_ok=True)
    say(f"     breaking down {video.name} (about 3 minutes per minute of video, longer on the first run)")
    run([engine, "decompose", video, "-o", out, "--lang", "en"])
    run([engine, "review", out])
    answers = out / "review_answers.json"
    blank = out / "review_answers.blank.json"
    if answers.exists() and not blank.exists():
        shutil.copy(answers, blank)
    say("")
    say(f"ok   first pass written to {rel(out)}")
    say("NEXT (the review, done by the AI that is running this):")
    say(f"  1. Open {rel(out)}/storyboard.jpg, then {rel(out)}/review_tasks.json.")
    say("  2. For every shot, look at its sheet image and fill in its entry in review_answers.json.")
    say(f"  3. Run: python3 breakdown_machine/run.py --finish {rel(out)}")
    say("To skip the review (faster, less reliable on downloaded videos) run step 3 now.")


def finish(args):
    engine = need_engine()
    out = Path(args.finish).expanduser().resolve()
    if not (out / "breakdown.json").exists():
        die(f"{args.finish} is not a breakdown folder (no breakdown.json)")
    answers, blank = out / "review_answers.json", out / "review_answers.blank.json"
    reviewed = answers.exists() and (not blank.exists() or answers.read_text() != blank.read_text())
    if reviewed:
        run([engine, "apply-review", out, "--by", args.by, "--lang", "en"])
        say("ok   review merged into the verdict")
    else:
        say("note no review was filled in: the verdict is from measurements only")
    check = run([engine, "videomd", out, "--check"], check=False, capture=True)
    if check.returncode != 0:
        print(check.stdout[-2000:], file=sys.stderr)
        die("VIDEO.md did not pass the format check (details above)")
    say("ok   VIDEO.md passes the format check")
    theme.apply(out / "report.html")
    say("ok   report skinned")
    summary = run([engine, "summary", out / "breakdown.json"], check=False, capture=True).stdout.strip()
    say("")
    say(summary)
    say("")
    say(f"Report for you:   {rel(out)}/report.html")
    say(f"Breakdown for AI: {rel(out)}/VIDEO.md")
    say(f"Next: turn it into an editing skill. Ask Claude Code: \"turn {rel(out)} into an editing skill\"")


def main():
    ap = argparse.ArgumentParser(description="Break down one video into a report and a VIDEO.md package.")
    ap.add_argument("video", nargs="?", help="a link (Instagram, TikTok, YouTube, ...) or a video file")
    ap.add_argument("--name", help="folder name under runs/ (default: from the link or file name)")
    ap.add_argument("--finish", metavar="DIR", help="step 2: merge the review and write the final report")
    ap.add_argument("--cookies-from-browser", metavar="BROWSER",
                    help="use this browser's login for the download (chrome, safari, firefox)")
    ap.add_argument("--by", default="claude", help="who did the review (written into the report)")
    args = ap.parse_args()
    if args.finish:
        finish(args)
    elif args.video:
        start(args)
    else:
        ap.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()
