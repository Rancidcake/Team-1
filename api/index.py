import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent / "IndiaProjectTeamA"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from config.wsgi import application

__all__ = ["application"]
