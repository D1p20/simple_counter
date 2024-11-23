from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# setup db
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile("settings.py")

    # initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    from counter.views import counter_app

    app.register_blueprint(counter_app)

    return app
