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

# --- DATENBANK SETUP ---
# Das erstellt automatisch die Datenbank, wenn sie noch nicht da ist
def init_db():
    conn = sqlite3.connect('database.db')
    # Tabelle für User (wichtig für Login & SQL Injection später)
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    # Wir legen einen Admin an (damit P1 etwas zu hacken hat)
    conn.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (1, "admin", "secret123")') 
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