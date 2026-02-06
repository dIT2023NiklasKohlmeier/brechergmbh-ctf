import sqlite3
from flask import Flask, render_template

# --- IMPORTE: Hier laden wir die Module deiner Gruppe ---
from routes.traversal import p3_blueprint   # Dein Part (P3) - Directory Traversal
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
    
    # 1. Tabelle für User (für Login / P1)
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    # Ein Admin und ein normaler User
    cursor.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (1, "admin", "secret123")') 
    cursor.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (2, "hans", "passwort")') 

    # 2. NEU: Tabelle für Pakete (für Tracking / P2)
    cursor.execute('CREATE TABLE IF NOT EXISTS packages (id INTEGER PRIMARY KEY, tracking_number TEXT, status TEXT, location TEXT, sender TEXT, comment TEXT)')
    
    # Wir füllen die DB mit "echten" Daten, damit man was findet
    packages = [
        (1, 'BL-12345', 'In Zustellung', 'Hamburg Verteilzentrum', 'Amazon'),
        (2, 'BL-55555', 'Verzögert (Zoll)', 'Frankfurt Flughafen', 'China Gadgets GmbH'),
        (3, 'BL-99999', 'Zugestellt', 'München', 'Oma Erna'),
        # Das hier ist ein Easter-Egg, das man nur per SQL-Injection sieht ;)
        (4, 'BL-ADMIN', 'TOP SECRET', 'Bunker Berlin', 'BND', 'Banger Easteregg') 
    ]
    
    # Daten einfügen (nur wenn sie noch nicht da sind)
    for p in packages:
        cursor.execute('INSERT OR IGNORE INTO packages (id, tracking_number, status, location, sender, comment) VALUES (?, ?, ?, ?, ?, ?)', p)

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