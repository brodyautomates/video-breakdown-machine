"""Compare several breakdowns and write what they have in common.

    python3 breakdown_machine/compare.py breakdowns/* -o patterns/PATTERNS.md
    python3 breakdown_machine/compare.py runs/a runs/b runs/c

One row per video, then the middle value and the range of each measure. Use it on 5 or more videos that worked
for the same kind of account: the measures that barely move between them are the pattern, and the ones that
swing are taste.
"""
import argparse
import statistics
from pathlib import Path

from common import rel, say
from skillgen import facts, pct

COLS = [
    ("Length (s)", lambda f: f["duration"]),
    ("Cuts / min", lambda f: f["cuts_per_min"]),
    ("Median shot (s)", lambda f: f["median_shot"]),
    ("First cut (s)", lambda f: f["first3"]["first_cut_s"]),
    ("Cuts in first 3 s", lambda f: f["first3"]["cuts"]),
    ("Text cues / min", lambda f: f["cues_per_min"]),
    ("Words / cue", lambda f: f["cue_median_words"]),
    ("Sound effects", lambda f: f["sfx"]),
    ("Inserts", lambda f: f["insert_share"]),
]


def cell(v, name=""):
    if v is None:
        return "-"
    if name == "Inserts":
        return pct(v)
    return f"{v:g}" if isinstance(v, (int, float)) else str(v)


def main():
    ap = argparse.ArgumentParser(description="Compare breakdowns and write the shared pattern.")
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("-o", "--out", help="write the result to this file (default: print)")
    a = ap.parse_args()
    rows = []
    for d in a.dirs:
        p = Path(d).expanduser().resolve()
        if not (p / "breakdown.json").exists():
            continue
        rows.append((p.name, facts(p)))
    if len(rows) < 2:
        raise SystemExit("need at least two breakdown folders")
    L = [f"# What these {len(rows)} videos have in common", "",
         "Every number below is measured from the video files by the breakdown engine. Nothing is typed in by hand.", "",
         "| Video | Format | Made with | Music | " + " | ".join(c for c, _ in COLS) + " |",
         "|---|---|---|---|" + "---|" * len(COLS)]
    for name, f in rows:
        mix = max(f["mix"].items(), key=lambda kv: kv[1])[0].replace("_", " ") if f["mix"] else "-"
        L.append(f"| {name} | {str(f['format'] or '-').replace('_', ' ')} | {mix} | {'yes' if f['music'] else 'no'} | "
                 + " | ".join(cell(fn(f), c) for c, fn in COLS) + " |")
    L += ["", "## The middle and the spread", "", "| Measure | Middle value | Lowest | Highest | Read it as |", "|---|---|---|---|---|"]
    for c, fn in COLS:
        vals = [fn(f) for _, f in rows if isinstance(fn(f), (int, float))]
        if len(vals) < 2:
            continue
        mid, lo, hi = statistics.median(vals), min(vals), max(vals)
        spread = (hi - lo) / abs(mid) if mid else float("inf")
        read = "consistent: part of the pattern" if spread <= 0.5 else ("varies" if spread <= 1.5 else "swings widely: not a rule")
        L.append(f"| {c} | {cell(mid, c)} | {cell(lo, c)} | {cell(hi, c)} | {read} |")
    L += ["", "\"Consistent\" means the highest and lowest are within half of the middle value. With fewer than 5 videos,",
          "treat every line as a hint, not a rule.", "",
          "Two columns need care. \"Text cues\" counts captions and any other text the engine read in the picture (a filmed screen",
          "full of text scores very high). \"Sound effects\" on a platform download only counts the ones loud enough to find."]
    text = "\n".join(L) + "\n"
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(text, encoding="utf-8")
        say(f"ok   wrote {rel(Path(a.out).resolve())}")
    else:
        print(text)


if __name__ == "__main__":
    main()
