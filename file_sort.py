from pathlib import Path
from datetime import datetime
import shutil
import sys

def file_sort(path):
    path = Path(path)
    
    monate = {
        1: "Januar", 2: "Februar", 3: "März", 4: "April",
        5: "Mai", 6: "Juni", 7: "Juli", 8: "August",
        9: "September", 10: "Oktober", 11: "November", 12: "Dezember"
    }
    
    for file in path.iterdir():
        if not file.is_file():
            continue
            
        suffix = file.suffix.lower().strip('.')
        if suffix in ["jpg", "jpeg", "png", "gif"]:
            # Datum aus Datei
            timestamp = file.stat().st_mtime
            date = datetime.fromtimestamp(timestamp)
            
            # Zielordner
            jahr = str(date.year)
            monat = f"{date.month:02d}_{monate[date.month]}"
            destination = path / jahr / monat
            
            # Ordner erstellen (mit parents=True!)
            destination.mkdir(parents=True, exist_ok=True)
            
            # Zieldatei
            ziel_datei = destination / file.name
            
            # Falls Datei existiert, umbenennen
            counter = 1
            while ziel_datei.exists():
                ziel_datei = destination / f"{file.stem}_{counter}{file.suffix}"
                counter += 1
            
            print(f"Verschiebe: {file.name} → {jahr}/{monat}/{ziel_datei.name}")
            shutil.move(str(file), str(ziel_datei))

file_sort(Path(sys.executable).parent)
