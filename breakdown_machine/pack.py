"""Copy a finished breakdown into the library without the heavy or private parts.

    python3 breakdown_machine/pack.py runs/NAME [breakdowns/NAME]

Left out: the source video, the separated sound (stems), logs and the review working files. Any absolute path
inside the copied files is rewritten to be relative, so nothing about your computer is published.
Only publish breakdowns of videos you have the right to show frames from.
"""
import re
import shutil
import sys
from pathlib import Path

from common import ROOT, die, rel, say

SKIP_DIRS = {"stems", "frames", "remake", "drive", "__pycache__"}
SKIP_FILES = {"run.log", "review_tasks.json", "review_answers.json", "review_answers.blank.json", "source.json"}
VIDEO = {".mp4", ".mov", ".mkv", ".webm", ".wav", ".flac"}
TEXT = {".md", ".json", ".html", ".srt", ".ass", ".txt", ".yaml", ".yml"}


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    src = Path(sys.argv[1]).expanduser().resolve()
    if not (src / "VIDEO.md").exists():
        die(f"{sys.argv[1]} has no VIDEO.md: finish the breakdown first")
    dst = Path(sys.argv[2]).expanduser().resolve() if len(sys.argv) > 2 else ROOT / "breakdowns" / src.name
    if dst.exists():
        shutil.rmtree(dst)
    n = 0
    for p in sorted(src.rglob("*")):
        r = p.relative_to(src)
        if p.is_dir() or any(part in SKIP_DIRS for part in r.parts) or r.name in SKIP_FILES or r.name.startswith("check_"):
            continue
        if p.suffix.lower() in VIDEO and "sfx" not in r.parts:
            continue
        out = dst / r
        out.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix.lower() in TEXT:
            t = p.read_text(encoding="utf-8", errors="replace")
            t = t.replace(str(src) + "/", "").replace(str(src), ".").replace(str(ROOT) + "/", "")
            t = re.sub(r"/(?:Users|home)/[^/\s\"']+/", "~/", t)
            out.write_text(t, encoding="utf-8")
        else:
            shutil.copy2(p, out)
        n += 1
    size = sum(f.stat().st_size for f in dst.rglob("*") if f.is_file()) / 1e6
    say(f"ok   {n} files, {size:.1f} MB -> {rel(dst)}")


if __name__ == "__main__":
    main()
