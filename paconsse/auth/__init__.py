from flask import Blueprint, render_template, current_app, redirect, url_for
from paconsse.auth.forms import LoginForm

bp = Blueprint("auth", __name__, template_folder="templates", static_folder="static", static_url_path="/static")

@bp.route("/")
def index():
    return redirect(url_for("auth.login"))


@bp.route("/login")
def login():
    return render_template("login.html", title="Connexion", form = LoginForm())
# from paconsse.auth import auth # On importe les pages du site
