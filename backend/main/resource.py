import json
import logging

from flask import (Blueprint, Flask, json, request, jsonify)

from . import controller

bp = Blueprint('resource', __name__, url_prefix='/resource')
expect_keys = ['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine']

logging.basicConfig(level=logging.INFO)


@bp.route("/search", endpoint='search', methods=['GET'])
def search():
    """
    Does the search by calling the search_all method

    Returns:
        A jsonified list of restaurants with 200 status code
    """
    list_of_filters = request.args.to_dict()

    results = json.loads(controller.search_all(list_of_filters))
    return jsonify(results), 200


@bp.before_request
def validate_keys_values():
    """
    Validate the keys and values sent

    Returns:
        If any key or value is invalid, it returns a message with 400 status code
    """
    logging.info('Validating parameters...')
    for k,v in request.args.to_dict().items():
        if k not in expect_keys:
            return 'Invalid parameter ' + k, 400
        if v == 'null' or v == '':
            return 'Invalid value inside key ' + k, 400
