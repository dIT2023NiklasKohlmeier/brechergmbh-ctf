from flask import Blueprint, request, send_file
import os

# Das hier definiert die Variable "p3_blueprint", die wir eben importiert haben
p3_blueprint = Blueprint('p3', __name__)

@p3_blueprint.route('/download')
def download():
    # ... (Rest deines Codes) ...
    filename = request.args.get('file')
    if not filename:
        return "Bitte nutze ?file=dateiname.txt"
    try:
        path = os.path.join('static', filename)
        return send_file(path, as_attachment=True)
    except Exception as e:
        return f"Fehler: Datei '{filename}' nicht gefunden!"