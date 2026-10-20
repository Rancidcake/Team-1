"""Set up and run the Web Security Academy demo locally.

Usage: python runbook.py

This intentionally vulnerable training app must stay bound to localhost.
"""

from pathlib import Path
import subprocess
import sys
import webbrowser


ROOT = Path(__file__).resolve().parent
PYTHON = sys.executable


def run(*args: str) -> None:
    print(f"\n> {' '.join((PYTHON, *args))}", flush=True)
    subprocess.run((PYTHON, *args), cwd=ROOT, check=True)


def main() -> None:
    try:
        run("-m", "pip", "install", "-r", "requirements.txt")
        run("manage.py", "migrate")
        run("manage.py", "seed")
        url = "http://127.0.0.1:8000/"
        print(f"\nStarting locally at {url} (press Ctrl+C to stop).", flush=True)
        webbrowser.open(url)
        run("manage.py", "runserver", "127.0.0.1:8000")
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.returncode) from exc


if __name__ == "__main__":
    main()
