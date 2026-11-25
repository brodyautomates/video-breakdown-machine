"""Shared paths and helpers. Standard library only, so every script runs with any Python 3.10+."""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINE_REPO = "https://github.com/JuneYaooo/rea-video"
# The engine is pinned so an upstream change cannot break your install. To update: change this hash to a newer
# commit of rea-video, run install.py again, then run one breakdown to confirm it still works.
ENGINE_PIN = "c11f1bd8fd3edd26a40e8f45be828be685417700"
ENGINE_DIR = ROOT / ".engine" / "rea-video"
VENV = ROOT / ".venv"
RUNS = ROOT / "runs"
BIN = VENV / ("Scripts" if os.name == "nt" else "bin")


def exe(name: str) -> Path:
    return BIN / (name + (".exe" if os.name == "nt" else ""))


def say(msg: str) -> None:
    print(msg, flush=True)


def die(msg: str, code: int = 1) -> None:
    print(f"ERROR: {msg}", file=sys.stderr, flush=True)
    sys.exit(code)


def run(cmd, check=True, capture=False, cwd=None, env=None):
    cmd = [str(c) for c in cmd]
    r = subprocess.run(cmd, cwd=cwd, env=env, text=True,
                       stdout=subprocess.PIPE if capture else None,
                       stderr=subprocess.STDOUT if capture else None)
    if check and r.returncode != 0:
        if capture and r.stdout:
            print(r.stdout[-4000:], file=sys.stderr)
        die(f"command failed ({r.returncode}): {' '.join(cmd[:6])} ...")
    return r


def need_engine() -> Path:
    """The rea-video command inside this repo's own environment."""
    p = exe("rea-video")
    if not p.exists():
        die("the engine is not installed yet. Run: python3 breakdown_machine/install.py")
    return p


def need_tool(name: str) -> str:
    p = shutil.which(name)
    if not p:
        hint = {"ffmpeg": "macOS: brew install ffmpeg | Windows: winget install Gyan.FFmpeg | Linux: apt install ffmpeg"}
        die(f"{name} was not found. {hint.get(name, hint['ffmpeg'])}")
    return p


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return s[:60] or "video"


def is_link(s: str) -> bool:
    return bool(re.match(r"^https?://", s.strip()))


def load_breakdown(out_dir: Path) -> dict:
    p = Path(out_dir) / "breakdown.json"
    if not p.exists():
        die(f"{p} not found. Is {out_dir} a breakdown folder?")
    return json.loads(p.read_text(encoding="utf-8"))


def rel(p: Path) -> str:
    """A path to show to a person: relative to the repo when it is inside it."""
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except ValueError:
        return str(p)
