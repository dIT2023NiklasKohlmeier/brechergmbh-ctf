import sqlite3
from flask import Flask, render_template

# --- IMPORTE: Hier laden wir die Module deiner Gruppe ---
from routes.p3_download import p3_blueprint # Dein Part (P3) - Directory Traversal
from routes.p1_auth import p1_blueprint     # Niklas' Mate 1 (P1) - Login
from routes.p2_tracking import p2_blueprint # Niklas' Mate 2 (P2) - Tracking

app = Flask(__name__)

# --- REGISTRIEREN: Hier sagen wir Flask, dass es diese Module nutzen soll ---
app.register_blueprint(p3_blueprint)
app.register_blueprint(p1_blueprint)
app.register_blueprint(p2_blueprint)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # User (bleibt gleich)
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (1, "admin", "secret123")') 

    # Pakete
    cursor.execute('DROP TABLE IF EXISTS packages')
    
    cursor.execute('''
        CREATE TABLE packages (
            id INTEGER PRIMARY KEY, 
            tracking_number TEXT, 
            status TEXT, 
            location TEXT, 
            sender TEXT
        )
    ''')
    
    # ECHTE STRASSEN FÜR GEOCODING
    packages = [
        # Hamburg: Mitten auf dem Kiez
        (1, 'BL-HAM-01', 'In Zustellung', 'Reeperbahn 1, Hamburg', 'Kiez Kiosk'),
        
        # Berlin: Direkt am Reichstag
        (2, 'BL-BER-02', 'Verzögert (Demo)', 'Platz der Republik 1, Berlin', 'Regierung'),
        
        # München: Marienplatz
        (3, 'BL-MUC-03', 'Zugestellt', 'Marienplatz 1, München', 'Bavaria GmbH'),
        
        # Frankfurt: Flughafen Cargo City
        (4, 'BL-FRA-04', 'Zollabfertigung', 'Cargo City Süd, Frankfurt Flughafen', 'Logistics Worldwide'),
        
        # International: New York
        (5, 'BL-NYC-05', 'Verschifft', 'Times Square, New York', 'US Imports Inc.'),
        
        # Easter Egg (SQL Injection Ziel)
        (6, 'BL-ADMIN', 'TOP SECRET', 'BND Zentrale, Berlin', 'Geheimdienst') 
    ]
    
    cursor.executemany('INSERT INTO packages VALUES (?,?,?,?,?)', packages)

    conn.commit()
    conn.close()

# Datenbank beim Start initialisieren
with app.app_context():
    init_db()

# --- HAUPT-ROUTE (STARTSEITE) ---
@app.route('/')
def index():
    # Lädt deine schicke Brecher Logistics Startseite
    return render_template('index.html')

# --- PLATZHALTER FÜR DIE RESTLICHEN AUFGABEN ---
# Diese werden später auch in eigene Dateien (Blueprints) ausgelagert.
# Bis dahin bleiben sie hier, damit keine "404 Not Found" Fehler kommen.

@app.route('/notes')
def notes():
    return "Mitarbeiter-Board (TODO: P4 - Stored XSS)"

@app.route('/order/<id>')
def order(id):
    return f"Bestelldetails für ID {id} (TODO: P5 - Broken Access Control)"

@app.route('/backup')
def backup():
    return "Backup Download (TODO: P6 - Information Disclosure)"

# --- SERVER STARTEN ---
if __name__ == '__main__':
    # host='0.0.0.0' bedeutet: Von jedem PC im Netzwerk erreichbar
    app.run(debug=True, host='0.0.0.0')