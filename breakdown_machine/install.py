"""Set everything up in one go.

    python3 breakdown_machine/install.py

It makes a private Python environment in .venv, downloads the breakdown engine (rea-video, pinned to a known
good commit) into .engine, installs it, and checks ffmpeg. Safe to run again at any time.
"""
import shutil
import subprocess
import sys

from common import BIN, ENGINE_DIR, ENGINE_PIN, ENGINE_REPO, ROOT, VENV, die, exe, need_tool, run, say

# The engine's audio models need onnxruntime, which only ships for released Python versions.
GOOD = [(3, 12), (3, 11), (3, 13), (3, 10)]


def version_of(py: str):
    try:
        out = subprocess.run([py, "-c", "import sys;print(sys.version_info[0],sys.version_info[1])"],
                             capture_output=True, text=True, timeout=20).stdout.split()
        return int(out[0]), int(out[1])
    except Exception:
        return None


def pick_python():
    """A Python between 3.10 and 3.13. Returns (path, version) or (None, None)."""
    names = [f"python{a}.{b}" for a, b in GOOD] + ["python3", "python"]
    for n in names:
        p = shutil.which(n)
        if p and version_of(p) in GOOD:
            return p, version_of(p)
    return None, None


def make_venv():
    if exe("python").exists() and version_of(str(exe("python"))) in GOOD:
        say(f"ok   environment exists (.venv, Python {'.'.join(map(str, version_of(str(exe('python')))))})")
        return
    if VENV.exists():
        shutil.rmtree(VENV)
    py, ver = pick_python()
    if py:
        run([py, "-m", "venv", VENV])
    elif shutil.which("uv"):
        say("     no Python 3.10 to 3.13 found; asking uv for Python 3.12")
        run(["uv", "venv", "--python", "3.12", "--seed", VENV])
    else:
        mine = version_of(sys.executable)
        die(f"need Python 3.10 to 3.13 (found {mine[0]}.{mine[1]}). Install 3.12 from python.org or run "
            "'brew install python@3.12', then run this again.")
    if not exe("python").exists():
        die("could not create .venv")
    say(f"ok   environment created (.venv, Python {'.'.join(map(str, version_of(str(exe('python')))))})")


def pip(*args, capture=True):
    return run([exe("python"), "-m", "pip", "--disable-pip-version-check", *args], capture=capture)


def get_engine():
    need_tool("git")
    if not (ENGINE_DIR / ".git").exists():
        ENGINE_DIR.parent.mkdir(parents=True, exist_ok=True)
        say("     downloading the breakdown engine (rea-video)")
        run(["git", "clone", "--quiet", ENGINE_REPO, ENGINE_DIR])
    head = run(["git", "-C", ENGINE_DIR, "rev-parse", "HEAD"], capture=True).stdout.strip()
    if head != ENGINE_PIN:
        run(["git", "-C", ENGINE_DIR, "fetch", "--quiet", "origin"], check=False)
        run(["git", "-C", ENGINE_DIR, "checkout", "--quiet", ENGINE_PIN])
    say(f"ok   engine at pinned commit {ENGINE_PIN[:10]}")


def install_engine():
    say("     installing the engine (a few minutes the first time)")
    pip("install", "--quiet", "-e", f"{ENGINE_DIR}[ocr]")
    # The text reader can pull in a second copy of OpenCV that breaks the first. Keep one.
    r = run([exe("python"), "-m", "pip", "show", "opencv-python"], check=False, capture=True)
    if r.returncode == 0:
        pip("uninstall", "-y", "opencv-python")
        pip("install", "--quiet", "--force-reinstall", "--no-deps", "opencv-python-headless>=4.8,<5")
        say("ok   removed the duplicate OpenCV")
    pip("install", "--quiet", "-r", ROOT / "requirements.txt")
    r = run([exe("rea-video"), "--help"], check=False, capture=True)
    if r.returncode != 0:
        print(r.stdout[-3000:], file=sys.stderr)
        die("the engine installed but does not start. The lines above say why.")
    say("ok   engine runs")


def main():
    say("Video Breakdown Machine: setup")
    for tool in ("ffmpeg", "ffprobe"):
        need_tool(tool)
    say("ok   ffmpeg found")
    make_venv()
    get_engine()
    install_engine()
    say("")
    say("Ready. Break down a video with:")
    say("  python3 breakdown_machine/run.py <link or file>")
    say(f"(tools live in {BIN.relative_to(ROOT)}; nothing was installed outside this folder, except the engine's")
    say(" sound models, which download to ~/.cache/rea-video on the first run, about 220 MB)")


if __name__ == "__main__":
    main()
