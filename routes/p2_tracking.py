from flask import Blueprint, render_template, request
import sqlite3
from geopy.geocoders import Nominatim # Das Tool für die Koordinaten

p2_blueprint = Blueprint('p2', __name__)

@p2_blueprint.route('/track')
def track():
    tracking_id = request.args.get('id')
    result = None
    
    # Standard-Startpunkt (Mitte von DE), falls nichts gefunden wird
    lat = 51.1657
    lon = 10.4515
    
    if tracking_id:
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            
            # Die SQL-Abfrage (Achtung: Unsicher für P2 Aufgabe!)
            query = f"SELECT * FROM packages WHERE tracking_number = '{tracking_id}'"
            cursor.execute(query)
            
            # Wir holen die Daten aus der DB
            db_row = cursor.fetchone() 
            
            if db_row:
                # Wir machen aus dem DB-Ergebnis eine bearbeitbare Liste
                result = list(db_row)
                
                # --- GEOCODING START ---
                ort_name = result[3] # Hier steht z.B. "Hamburg, Germany"
                
                # Wir fragen OpenStreetMap
                geolocator = Nominatim(user_agent="brecher_logistics_app")
                
                try:
                    location = geolocator.geocode(ort_name)
                    if location:
                        lat = location.latitude
                        lon = location.longitude
                        print(f"Gefunden: {ort_name} -> {lat}, {lon}")
                except:
                    print("Geocoding fehlgeschlagen (Kein Internet?)")
                
                # Wir hängen die Koordinaten hinten an die Liste an
                # result[5] wird lat, result[6] wird lon
                result.append(lat)
                result.append(lon)
                # --- GEOCODING ENDE ---

            conn.close()
        except Exception as e:
            print(f"Fehler: {e}")

    return render_template('tracking.html', result=result, tracking_id=tracking_id)