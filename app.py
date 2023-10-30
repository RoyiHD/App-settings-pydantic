from flask import Flask
from settings import ServerSettings

server = ServerSettings()

def create_app() -> Flask:

    app = Flask(__name__, static_folder=None)
    
    return app

if __name__ == "__main__":
    
    app = create_app()

    app.run(
        host=server.host,
        port=server.port,
    )
