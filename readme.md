# 📁 File Sorter - Automatische Datei-Sortierung nach Datum

Ein Windows-Tool, das Bild-Dateien automatisch nach Jahr und Monat in Ordner sortiert.

> 🚀 **Portable Version** - Keine Python-Installation erforderlich!

## ✨ Features

✅ **Keine Installation nötig** - Einfach ausführen!  
✅ Sortiert Bilder automatisch nach **Jahr** und **Monat**  
✅ Unterstützt: **JPG, JPEG, PNG, GIF**  
✅ Erstellt automatisch Ordner-Struktur: `Jahr/MM_Monat/`  
✅ Deutsche Monatsnamen: `05_Mai`, `12_Dezember`  
✅ Verhindert Duplikate durch automatische Umbenennung  
✅ Verwendet Datei-Änderungsdatum  
✅ **Portable** - läuft von USB-Stick  
✅ **Kein Python erforderlich**

---

## 📥 Download & Installation

### Option 1: Fertige EXE herunterladen

1. **Download:** [file_sort.exe]
2. **Speichern:** Beliebiger Ordner (z.B. `C:\Tools\`)
3. **Fertig!** Keine Installation nötig

### Option 2: Selbst kompilieren
```bash
# Python-Script herunterladen
git clone https://github.com/deinuser/file-sorter.git
cd file-sorter

# PyInstaller installieren
pip install pyinstaller

# EXE erstellen
pyinstaller --onefile --name file_sort file_sort.py
