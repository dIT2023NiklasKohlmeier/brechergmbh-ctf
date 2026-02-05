from flask import Blueprint, render_template, request
import sqlite3

p2_blueprint = Blueprint('p2', __name__)

@p2_blueprint.route('/track')
def track():
    tracking_id = request.args.get('id')
    result = None
    
    if tracking_id:
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        try:
            # --- HIER IST DIE LOGIK (UND DIE LÜCKE) ---
            # Wir suchen genau die Nummer, die der User eingegeben hat.
            # (Das f-string Format ermöglicht später SQL-Injection für P2)
            query = f"SELECT * FROM packages WHERE tracking_number = '{tracking_id}'"
            print(f"Debug SQL: {query}") # Damit du im Terminal siehst, was passiert
            
            cursor.execute(query)
            result = cursor.fetchone() # Wir holen das erste Ergebnis
            
        except Exception as e:
            print(f"Datenbank Fehler: {e}")
        finally:
            conn.close()

    # Wir geben das Ergebnis an die HTML-Seite weiter
    return render_template('tracking.html', result=result, tracking_id=tracking_id)