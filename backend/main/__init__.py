"""
Module to create Flask App
"""

import logging
import os

import flask_cors
from flask import Flask


def create_app():
    """
    Creates the app

    Returns:
        The app running
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #pylint: disable=import-outside-toplevel
    from flask_cors import CORS
    #pylint: disable=unused-variable
    cors = CORS(app, resources={r"/resource/*": {"origins": "*"}})

    #pylint: disable=import-outside-toplevel
    from . import resource
    app.register_blueprint(resource.bp)

    #pylint: disable=import-outside-toplevel
    from . import service
    app.register_blueprint(service.bp)

    return app
