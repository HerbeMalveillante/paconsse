from paconsse.default import bp
from flask import render_template, current_app

@bp.route("/about")
def about():
    return render_template("about.html", title="À Propos")
