from flask import Blueprint, render_template, current_app

bp = Blueprint("blog", __name__, template_folder="../default/templates")

from paconsse.blog import blog # On importe les pages du site
