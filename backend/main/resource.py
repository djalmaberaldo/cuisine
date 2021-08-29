import json
import logging

from flask import (Blueprint, Flask, json, request, jsonify)

from . import controller

bp = Blueprint('resource', __name__, url_prefix='/resource')
expect_keys = ['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine']

@bp.route("/search", endpoint='search', methods=['GET'])
def search():
    list_of_filters = request.args.to_dict()

    results = json.loads(controller.search_all(list_of_filters))
    return jsonify(results), 200


@bp.before_request
def validate_keys_values():
    print('Validating parameters...')
    for k,v in request.args.to_dict().items():
        if k not in expect_keys:
            return 'Invalid parameter ' + k, 400
        if v == 'null' or v == '':
            return 'Invalid value inside key ' + k, 400
