from paconsse.default import bp

@bp.route("/")
def index():
    return "Home Page !"
