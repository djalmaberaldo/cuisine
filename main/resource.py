
import json
import logging

from flask import (Blueprint, Flask, Response, g, jsonify, render_template, json,
                   request)
from flask_expects_json import expects_json

from . import controller

bp = Blueprint('resource', __name__, url_prefix='/resource')
expect_keys = ['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine']

@bp.route("/search", endpoint='search', methods=['GET'])
def search():
    list_of_filters = request.args.to_dict()

    keys = list_of_filters.keys()

    print('Validating parameters...')
    for k in keys:
        if k not in expect_keys:
            return {
                "message": "Invalid Parameters",
                "status": 403
            }

    return controller.search_all(list_of_filters)

@bp.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 500
    
