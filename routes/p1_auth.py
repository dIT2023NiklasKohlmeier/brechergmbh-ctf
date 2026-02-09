from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3

p1_blueprint = Blueprint('p1', __name__)

@p1_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verbindung zur DB
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Prüfen, ob User und Passwort stimmen
        # (Hier nutzen wir ? Platzhalter, also KEINE SQL-Injection in P1, 
        # damit die Aufgaben getrennt bleiben. P2 ist für SQLi zuständig.)
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            # Login erfolgreich!
            # Session starten - Benutzer ist jetzt eingeloggt
            session['logged_in'] = True
            session['username'] = username
            return render_template('dashboard.html', username=username)
        else:
            error = "Ungültiger Benutzername oder Passwort."
    
    return render_template('login.html', error=error)


@p1_blueprint.route('/logout')
def logout():
    """Logout-Funktion - beendet die Session"""
    session.clear()
    return redirect(url_for('p1.login'))