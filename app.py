import sqlite3
from flask import Flask, render_template
# --- IMPORTE ---
from routes.traversal import p3_blueprint  # Deine Datei
from routes.p1_auth import p1_blueprint    # Neu
from routes.p2_tracking import p2_blueprint # Neu

app = Flask(__name__)

# --- REGISTRIEREN ---
app.register_blueprint(p3_blueprint)
app.register_blueprint(p1_blueprint)
app.register_blueprint(p2_blueprint)

# ... (Hier drunter bleibt dein Datenbank-Code und init_db wie vorher) ...

# --- ROUTEN ---
@app.route('/')
def index():
    return render_template('index.html')

# Die alten Dummy-Routen für /login und /track kannst du LÖSCHEN,
# weil die jetzt über die Blueprints oben geladen werden!

# ... (Rest wie gehabt: notes, order, app.run) ...