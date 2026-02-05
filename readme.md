# 📦 Projekt-Vorschlag: "Nexus Logistics" CTF

Moin Leute,

hier ist ein Entwurf für unser Gruppenprojekt im Modul "Erweiterte IT Angriffe". Ich habe mal ein technisches Grundgerüst aufgesetzt, damit wir sehen können, ob das machbar ist.

## 🎯 Das Ziel
Wir bauen eine **verwundbare Webanwendung** für ein fiktives Logistik-Startup. Unsere Kommilitonen müssen darin später Sicherheitslücken finden (Capture the Flag).

## 📖 Die Story
**"Nexus Logistics GmbH"** ist ein modernes Startup, das beim Thema Security geschlampt hat.
- Es gibt einen öffentlichen Bereich (Paketverfolgung).
- Es gibt einen internen Bereich (Mitarbeiter-Login, Frachtbriefe).
- **Ziel des Angreifers:** 6 Flags finden, die wir im System verstecken.

## 🛠 Der Tech-Stack (Vorschlag)
Damit wir wenig Stress mit der Einrichtung haben:
* **Python (Flask):** Simpel, wenig Code.
* **SQLite:** Keine Datenbank-Installation nötig (nur eine Datei).
* **Docker:** Läuft bei jedem gleich.
 Fabian ist ein Käfer

## 💀 Aufgabenverteilung (6 Lücken)
Die Idee: Jeder von uns übernimmt eine Schwachstelle und implementiert sie.

| Nr | Schwachstelle | Ort in der App | Status |
| :--- | :--- | :--- | :--- |
| **P1** | **Weak Credentials** | Admin-Login (Standardpasswort) | *Offen* |
| **P2** | **SQL Injection** | Sendungsverfolgung | *Timo* |
| **P3** | **Directory Traversal** | Rechnungs-Download | *Niklas* |
| **P4** | **XSS (Stored)** | Notiz-Board für Mitarbeiter | *Offen* |
| **P5** | **Broken Access Control** | Bestellansicht (IDOR) | *Offen* |
| **P6** | **Info Disclosure** | Backup-Dateien / Git-Repo | *Offen* |

To DO:
Einteilung zu Lücken (oder andere)
Website schick machen
Geileren Firmen Name wählen
Absprechen Termine

---
*Setup zum Testen:*
`pip install -r requirements.txt` -> `python app.py`
