from flask import Blueprint, render_template, request

p1_blueprint = Blueprint('p1', __name__)

@p1_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login-Logik noch nicht implementiert (TODO: P1)"
    return render_template('login.html')