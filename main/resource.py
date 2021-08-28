
import json
import logging

from flask import (Blueprint, Flask, Response, g, jsonify, render_template,
                   request)
from flask_expects_json import expects_json

from . import controller

bp = Blueprint('resource', __name__, url_prefix='/resource')

@bp.route("/search", endpoint='search', methods=['GET'])
def search():
    list_of_filters = request.args.to_dict()
    print(list_of_filters)
    return controller.search_all(list_of_filters)

@bp.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 500
    
