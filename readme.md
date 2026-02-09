# 📦 Projekt-Vorschlag: "Brecher Logistics GmbH" CTF
*(Ehemals "Nexus Logistics")*

Moin Leute,

hier ist der Entwurf für unser Gruppenprojekt im Modul "Erweiterte IT Angriffe". Ich habe mal ein technisches Grundgerüst aufgesetzt, damit wir sehen können, ob das machbar ist.

## 📋 To Do (Orga & Allgemein)
- [ ] Einteilung zu Lücken finalisieren (Wer macht P4-P6?)
- [x] Website schick machen (Bootstrap & Maps sind drin!)
- [x] Geileren Firmen-Namen wählen (-> "Brecher Logistics")
- [ ] Wissenschaftliche Dokumentation erstellen
- [ ] Absprechen Termine für nächste Treffen
- [ ] Präsentation vorbereiten

---

## 🚀 Schnellstart (Setup)

Ich habe uns ein Skript gebaut, damit niemand manuell Python-Kram installieren muss.

1. **Repository klonen** (falls noch nicht passiert):
   
    git clone https://github.com/dIT2023NiklasKohlmeier/brechergmbh-ctf.git

2. **Starten (Windows):**
   👉 Doppelklick auf die Datei **start_website.bat**
   *(Das Skript installiert automatisch alle Pakete und startet den Server)*

3. **Browser öffnen:**
   Gehe auf http://127.0.0.1:5000

---

## 🎯 Das Ziel
Wir bauen eine **verwundbare Webanwendung** für ein fiktives Logistik-Startup. Unsere Kommilitonen müssen darin später Sicherheitslücken finden (Capture the Flag).

## 📖 Die Story
**"Brecher Logistics GmbH"** ist ein modernes Startup, das beim Thema Security geschlampt hat.
- Es gibt einen öffentlichen Bereich (Paketverfolgung mit Live-Karte).
- Es gibt einen internen Bereich (Mitarbeiter-Login, Frachtbriefe).
- **Ziel des Angreifers:** 6 Flags finden, die wir im System verstecken.

## 🛠 Der Tech-Stack
Damit wir wenig Stress mit der Einrichtung haben:
* **Backend:** Python (Flask)
* **Datenbank:** SQLite (Lokal, keine Installation nötig)
* **Frontend:** Bootstrap 5 & LeafletJS (OpenStreetMap)
* **Tools:** Geopy (für Koordinaten-Umrechnung)

## 💀 Aufgabenverteilung (6 Lücken)
Die Idee: Jeder von uns übernimmt eine Schwachstelle und implementiert sie.

| Nr | Schwachstelle | Ort in der App | Status |
| :--- | :--- | :--- | :--- |
| **P1** | **Weak Credentials** | Admin-Login (Brute Force) | ✅ Fertig (Login geht) | Peter |
| **P2** | **SQL Injection** | Sendungsverfolgung | ✅ Fertig (Karte & DB) | Timo |
| **P3** | **Directory Traversal** | Rechnungs-Download | ✅ Fertig | - |
| **P4** | **XSS (Stored)** | Notiz-Board für Mitarbeiter | *Offen* | - |
| **P5** | **Broken Access Control** | Bestellansicht (IDOR) | *Offen* | - |
| **P6** | **Info Disclosure** | Backup-Dateien / Git-Repo | *Offen* | - |

---

### ⚠️ Wichtige Notiz (Troubleshooting)
Falls es Datenbank-Probleme gibt (z.B. Login geht nicht):
1. Server stoppen.
2. Lösche einfach die Datei **database.db**.
3. Starte **start_website.bat** neu – die Datenbank wird automatisch repariert.
