"""
P3 - Directory Traversal (Broken Defense)
==========================================
Dieses Modul simuliert ein Dokumenten-Management-System (DMS) mit einer
absichtlichen Schwachstelle: Ein unzureichender Filter gegen Path Traversal.

SCHWACHSTELLE:
Der Filter nutzt nur filename.replace("../", ""), was durch "....//"-Muster
umgangen werden kann (Nested Traversal Attack).

EXPLOIT:
/download?folder=2024&file=....//....//secrets/config.py
→ Der Filter entfernt "../", aber aus "..../" wird dann "../"!
"""

from flask import Blueprint, render_template, request, send_file, session, redirect, url_for
import os

# Blueprint für P3 (Directory Traversal)
p3_blueprint = Blueprint('p3', __name__)


@p3_blueprint.route('/documents')
def documents():
    """
    Zeigt eine Liste der verfügbaren Dokumente im DMS
    Listet nur Dateien aus static/invoices/2024

    ZUGRIFFSSCHUTZ: Nur für eingeloggte Mitarbeiter!
    """
    # Prüfen, ob User eingeloggt ist
    if not session.get('logged_in'):
        return redirect(url_for('p1.login'))
    documents_path = 'static/invoices/2024'

    try:
        # Lese alle Dateien im 2024-Ordner
        files = []
        if os.path.exists(documents_path):
            for filename in sorted(os.listdir(documents_path)):
                if filename.endswith('.pdf'):
                    # Extrahiere Rechnungsnummer für bessere Darstellung
                    files.append({
                        'name': filename,
                        'invoice_number': filename.replace('.pdf', ''),
                        'folder': '2024'
                    })

        return render_template('documents.html', files=files)

    except Exception as e:
        return f"Fehler beim Laden der Dokumente: {str(e)}", 500


@p3_blueprint.route('/download')
def download():
    """
    Download-Funktion mit ABSICHTLICH SCHWACHEM FILTER (Broken Defense)

    ZUGRIFFSSCHUTZ: Nur für eingeloggte Mitarbeiter!

    SCHWACHSTELLE:
    - Der Filter replace("../", "") ist unzureichend
    - Kann durch Nested Traversal umgangen werden: "..../" → nach Filter: "../"

    EXPLOIT-BEISPIEL:
    /download?folder=2024&file=....//....//secrets/config.py

    Nach dem Filter wird daraus:
    → ../ / ../ / secrets/config.py → ../../secrets/config.py
    """

    # Prüfen, ob User eingeloggt ist
    if not session.get('logged_in'):
        return "Zugriff verweigert! Bitte melden Sie sich an.", 403

    # Parameter aus der URL auslesen
    folder = request.args.get('folder', '2024')
    filename = request.args.get('file', '')

    # Validierung: Dateiname muss angegeben sein
    if not filename:
        return "Fehler: Kein Dateiname angegeben. Nutze ?folder=2024&file=RE-2024-001.pdf", 400

    # ============================================================
    # BROKEN DEFENSE - UNZUREICHENDER FILTER!
    # ============================================================
    # Diese Zeile soll Path Traversal verhindern, aber sie ist unsicher!
    # Problem: replace() entfernt nur einmalig "../"
    # Angreifer können "..../" nutzen → wird zu "../" nach dem Filter!
    safe_filename = filename.replace("../", "")

    # Baue den Pfad zusammen
    # Beispiel (normal):  static/invoices/2024/RE-2024-001.pdf
    # Beispiel (exploit): static/invoices/2024/../../secrets/config.py
    file_path = os.path.join('static', 'invoices', folder, safe_filename)

    # Debug-Ausgabe (in echten Apps würde man das nicht loggen!)
    print(f"[P3 DEBUG] Original filename: {filename}")
    print(f"[P3 DEBUG] Nach Filter: {safe_filename}")
    print(f"[P3 DEBUG] Finaler Pfad: {file_path}")

    # Versuche, die Datei zu senden
    try:
        # send_file liefert die Datei aus
        # as_attachment=True → Download statt Anzeige im Browser
        return send_file(file_path, as_attachment=True)

    except FileNotFoundError:
        return f"Fehler: Datei '{filename}' nicht gefunden.", 404

    except Exception as e:
        return f"Fehler beim Herunterladen: {str(e)}", 500


# Zusätzliche Route für direkten Zugriff (Kompatibilität mit alter Navbar)
@p3_blueprint.route('/download-legacy')
def download_legacy():
    """Legacy-Route für Abwärtskompatibilität mit der alten Navbar"""
    filename = request.args.get('file', '')

    if not filename:
        return "Bitte nutze ?file=dateiname", 400

    # Gleicher unsicherer Filter wie oben
    safe_filename = filename.replace("../", "")
    path = os.path.join('static', safe_filename)

    try:
        return send_file(path, as_attachment=True)
    except Exception as e:
        return f"Fehler: Datei '{filename}' nicht gefunden! ({str(e)})", 404
