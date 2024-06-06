import logging

from flask import Flask

from starter.health_api import health_api

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(health_api())

    return app
