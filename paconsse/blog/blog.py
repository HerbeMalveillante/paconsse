from paconsse.blog import bp
from flask import render_template, current_app

@bp.route("/")
def index():
    return render_template("blog.html", title="Accueil")
