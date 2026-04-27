from pathlib import Path

def walk_files(path):
    DOSSIER_IGNORES = [".venv", "__pycache__", ".git", "envguard.egg-info"]
    for fichier in Path(path).rglob("*"):
        if not any(ignore in fichier.parts for ignore in DOSSIER_IGNORES) and fichier.is_file():
            print(fichier)