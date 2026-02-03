import sqlite3
from flask import Flask, render_template

# WICHTIG: Hier steht jetzt "from routes.traversal", weil deine Datei so heißt!
from routes.traversal import p3_blueprint

app = Flask(__name__)

# Hier melden wir deinen Teil an
app.register_blueprint(p3_blueprint)

# --- DATENBANK SETUP ---
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    conn.execute('INSERT OR IGNORE INTO users (username, password) VALUES ("admin", "password123")') 
    conn.commit()
    conn.close()

with app.app_context():
    init_db()

# --- ROUTEN ---
@app.route('/')
def index():
    # Lädt die schöne Startseite
    return render_template('index.html')

# Platzhalter für die anderen (noch in der alten Form)
@app.route('/login')
def login(): return "Login (TODO: P1)"

@app.route('/track')
def track(): return "Tracking (TODO: P2)"

# Die Route /download ist hier weg, weil sie jetzt in deiner traversal.py steckt!

@app.route('/notes')
def notes(): return "Notes (TODO: P4)"

@app.route('/order/<id>')
def order(id): return f"Order {id} (TODO: P5)"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')