import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

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
    return "<h1>Nexus Logistics</h1><p>Willkommen! <a href='/login'>Login</a> | <a href='/track'>Tracking</a></p>"

# [P1] Weak Credentials
@app.route('/login', methods=['GET', 'POST'])
def login():
    return "<h2>Login Page (TODO: Person 1)</h2>"

# [P2] SQL Injection
@app.route('/track')
def track():
    return "<h2>Tracking (TODO: Person 2)</h2>"

# [P3] Directory Traversal
@app.route('/download')
def download():
    return "Download (TODO: Person 3)"

# [P4] XSS
@app.route('/notes')
def notes():
    return "Notes (TODO: Person 4)"

# [P5] Broken Access Control
@app.route('/order/<order_id>')
def order_details(order_id):
    return f"Order {order_id} (TODO: Person 5)"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')