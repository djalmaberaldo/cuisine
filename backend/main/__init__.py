import logging
import os

import flask_cors
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flask_cors import CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from . import resource
    app.register_blueprint(resource.bp)

    from . import controller
    app.register_blueprint(controller.bp)

    return app
