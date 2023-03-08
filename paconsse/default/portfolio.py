from paconsse.default import bp
from flask import render_template, current_app

@bp.route("/book")
def book():
    return render_template("portfolio.html", title="Book")
