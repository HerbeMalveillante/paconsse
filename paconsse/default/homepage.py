from paconsse.default import bp
from flask import render_template, current_app

@bp.route("/")
def index():
    return render_template("index.html", title="Accueil")
