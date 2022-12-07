from flask import Flask


def register_blueprints(app):
    from backend.views.core import blueprint_core
    from backend.api.api import blueprint_api

    app.register_blueprint(blueprint_core)
    app.register_blueprint(blueprint_api)


def create_app():
    app = Flask(__name__)

    register_blueprints(app)

    return app
