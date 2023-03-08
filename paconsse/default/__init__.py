from flask import Blueprint, render_template, current_app

bp = Blueprint("default", __name__, template_folder="templates")

from paconsse.default import homepage, about, portfolio # On importe les pages du site
