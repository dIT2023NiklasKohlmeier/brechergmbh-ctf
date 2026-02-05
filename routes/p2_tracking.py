from flask import Blueprint, render_template, request

p2_blueprint = Blueprint('p2', __name__)

@p2_blueprint.route('/track')
def track():
    tracking_id = request.args.get('id')
    if tracking_id:
        return f"Suche nach {tracking_id}... (SQL Injection hier einfügen -> TODO: P2)"
    return render_template('tracking.html')