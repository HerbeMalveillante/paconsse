from paconsse.default import bp
from flask import render_template, current_app, url_for
from paconsse.utils import pprint
import os

@bp.route("/")
def index():

    return render_template("index.html", title="Accueil")
