"""Rigenera HTML e PDF con lo stesso interprete, da qualunque directory."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
for script in ('genera-mappa.py', 'genera-pdf.py'):
    subprocess.run([sys.executable, str(ROOT / 'strumenti' / script)], cwd=ROOT, check=True)
