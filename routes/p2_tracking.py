from flask import Blueprint, render_template, request
import sqlite3

p2_blueprint = Blueprint('p2', __name__)

@p2_blueprint.route('/track')
def track():
    # Wir holen die ID aus der URL (?id=...)
    tracking_id = request.args.get('id')
    result = None
    
    # Nur wenn eine ID eingegeben wurde, fragen wir die Datenbank
    if tracking_id:
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            
            # Die SQL-Abfrage (noch unsicher programmiert für P2 Lücke später)
            query = f"SELECT * FROM packages WHERE tracking_number = '{tracking_id}'"
            print(f"DEBUG SQL: {query}") # Zeigt dir im Terminal, was passiert
            
            cursor.execute(query)
            result = cursor.fetchone() # Holt das erste Ergebnis
            
            conn.close()
        except Exception as e:
            print(f"DATENBANK FEHLER: {e}")

    # Hier übergeben wir die Daten an deine HTML-Datei
    # WICHTIG: 'result' und 'tracking_id' müssen hier stehen!
    return render_template('tracking.html', result=result, tracking_id=tracking_id)