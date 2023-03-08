from paconsse import create_app
from config import Config
from rich.panel import Panel

application = create_app(Config)
if __name__ == "__main__":
    application.run()
