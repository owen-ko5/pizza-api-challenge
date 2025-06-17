from flask import Flask
from server.models import db, migrate
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

  
    from server.routes import api
    app.register_blueprint(api)

    return app

app = create_app()
