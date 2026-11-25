"""The FounderOS Blueprint skin for the breakdown report.

    python3 breakdown_machine/theme.py runs/NAME/report.html

It adds a header, a footer and colours to the report the engine wrote. It does not change any of the report's
content. Running it twice is safe.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARK = "<!-- video-breakdown-machine skin -->"
REPO = "https://github.com/brodyautomates/video-breakdown-machine"

CSS = """
:root{--bg:#f4f7fd;--fg:#0f1b33;--muted:#5b6b88;--card:#ffffff;--line:#dbe3f3;--accent:#1659d6;--bp:#1e62d8;--bp2:#124cbb}
@media (prefers-color-scheme:dark){:root{--bg:#081226;--fg:#eaf0fb;--muted:#93a4c4;--card:#0e1c38;--line:#1d315a;--accent:#7fb0ff}}
body{padding:0 16px 24px;font-family:Geist,Inter,-apple-system,"Segoe UI",sans-serif}
main{padding-top:8px}
h1{font-size:24px;letter-spacing:-.01em;font-weight:600} h2{font-weight:600}
.card{border-radius:14px}
code,pre.prompt{font-family:"JetBrains Mono","Geist Mono",ui-monospace,Menlo,monospace}
.vbm-head{margin:0 -16px 18px;padding:26px 24px 22px;color:#fff;position:relative;overflow:hidden;
 background-color:var(--bp);
 background-image:
  linear-gradient(rgba(255,255,255,.13) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.13) 1px,transparent 1px),
  linear-gradient(rgba(255,255,255,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.055) 1px,transparent 1px),
  radial-gradient(ellipse at 50% 40%,#3a7ee5 0%,#1e62d8 55%,#154fc2 100%);
 background-size:96px 96px,96px 96px,24px 24px,24px 24px,100% 100%;background-position:-1px -1px,-1px -1px,-1px -1px,-1px -1px,0 0}
.vbm-head .in{max-width:1100px;margin:auto;display:flex;align-items:center;gap:18px;flex-wrap:wrap;position:relative}
.vbm-head svg{height:22px;width:auto;color:#fff;flex:none}
.vbm-head .t{font:500 12px/1.2 "JetBrains Mono","Geist Mono",ui-monospace,Menlo,monospace;letter-spacing:.08em;text-transform:uppercase;opacity:.9}
.vbm-head .r{margin-left:auto;font:500 12px/1.2 "JetBrains Mono","Geist Mono",ui-monospace,Menlo,monospace;opacity:.75}
.vbm-head a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.5)}
.vbm-foot{max-width:1100px;margin:28px auto 0;padding-top:14px;border-top:1px solid var(--line);color:var(--muted);font-size:12.5px;display:flex;gap:8px 18px;flex-wrap:wrap}
.vbm-foot a{color:var(--accent)}
@media print{.vbm-head{-webkit-print-color-adjust:exact;print-color-adjust:exact;margin:0 0 12px}.vbm-foot{font-size:10px}}
"""


def _logo() -> str:
    svg = (HERE / "report_theme" / "logo.svg").read_text(encoding="utf-8")
    return re.sub(r"\s+", " ", svg).strip()


def apply(report: Path) -> bool:
    """Skin one report.html in place. Returns False when it was already skinned."""
    report = Path(report)
    html = report.read_text(encoding="utf-8")
    if MARK in html:
        return False
    head = (f'{MARK}<div class="vbm-head"><div class="in">{_logo()}'
            f'<span class="t">Video Breakdown Machine</span>'
            f'<span class="r"><a href="{REPO}">github.com/brodyautomates/video-breakdown-machine</a></span></div></div>')
    foot = (f'<div class="vbm-foot"><span>Broken down with the <a href="{REPO}">FounderOS Video Breakdown Machine</a>.</span>'
            f'<span>Engine: <a href="https://github.com/JuneYaooo/rea-video">rea-video</a> (Apache-2.0).</span>'
            f'<span>Numbers are measured from the file; anything marked inferred is a reading, not a fact.</span></div>')
    if "</style>" not in html or "<body>" not in html:
        raise SystemExit(f"{report} does not look like an engine report (no <style> or <body>)")
    html = html.replace("</style>", CSS + "</style>", 1)
    html = html.replace("<body>", "<body>" + head, 1)
    html = html.replace("</main>", foot + "</main>", 1) if "</main>" in html else html.replace("</body>", foot + "</body>", 1)
    report.write_text(html, encoding="utf-8")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    print("skinned" if apply(Path(sys.argv[1])) else "already skinned")
