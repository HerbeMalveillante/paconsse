from flask import Blueprint, render_template, current_app

bp = Blueprint("default", __name__)

from paconsse.default import homepage # On importe la page d'accueil
