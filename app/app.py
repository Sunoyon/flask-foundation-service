from flask import Flask
from flask_rebar import Rebar

rebar = Rebar()
v1_registry = rebar.create_handler_registry(
                    prefix='/v1',
                    swagger_path='/apidocs',
                    swagger_ui_path='/apidocs-ui')


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_envvar("APP_CONFIG")
    rebar.init_app(app)

    from app.entities.db import db
    db.init_app(app)
    return app
