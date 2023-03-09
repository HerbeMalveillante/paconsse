from flask import Blueprint, render_template, current_app, url_for
from paconsse.utils import pprint
import os

bp = Blueprint("default", __name__, template_folder="default/templates", static_folder="static", static_url_path="/static")

from paconsse.default import homepage, about, portfolio # On importe les pages du site
