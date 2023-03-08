from flask import Flask
from rich import print
from rich.panel import Panel
from .utils import pprint

def create_app(config):
    print(
    Panel.fit(
        f"""[bold red] ▄▄▄· ▄▄▄·  ▄▄·        ▐ ▄ .▄▄ · .▄▄ · ▄▄▄ .
▐█ ▄█▐█ ▀█ ▐█ ▌▪▪     •█▌▐█▐█ ▀. ▐█ ▀. ▀▄.▀·
 ██▀·▄█▀▀█ ██ ▄▄ ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄▄▀▀▀█▄▐▀▀▪▄
▐█▪·•▐█ ▪▐▌▐███▌▐█▌.▐▌██▐█▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌
.▀    ▀  ▀ ·▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀▀  ▀▀▀▀  ▀▀▀
                                    v{config.VERSION}[/bold red]""",
        style="blue",
    )
)

    app = Flask(__name__)
    app.config.from_object(config)

    from paconsse.default import bp as default_bp
    app.register_blueprint(default_bp)

    return app
