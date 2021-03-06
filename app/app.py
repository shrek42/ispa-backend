from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import app_config


db = SQLAlchemy()


def create_app(flask_config='development', db_uri=""):
    """Create and configure an instance of the application."""
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_object(app_config[flask_config])
    app.config.update(
        SECRET_KEY="TSST",
        JWT_SECRET=2*"TSST",
        JWT_BLACKLIST_ENABLE=True,
        JWT_BLACKLIST_TOKEN_CHECKS=['access', 'refresh'],
        SQLALCHEMY_DATABASE_URI=db_uri
    )

    db.init_app(app)
    migrate = Migrate(app, db) # noqa
    from app import models # noqa

    # blueprints
    from app.views import home
    app.register_blueprint(home.bp)
    from app.views import auth
    app.register_blueprint(auth.bp)
    from app.views import test
    app.register_blueprint(test.bp)
    return app
