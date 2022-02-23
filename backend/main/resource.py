"""
File where the endpoint is located along with its validation method
"""

import json
import logging

from flask import (Blueprint, json, request, jsonify)

from . import controller

bp = Blueprint('resource', __name__, url_prefix='/resource')
expect_keys = ['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine']

logging.basicConfig(level=logging.DEBUG)


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
    for key,value in request.args.to_dict().items():
        if key not in expect_keys:
            return 'Invalid parameter ' + key, 400
        if value in ('null', ''):
            return 'Invalid value inside key ' + key, 400
    return None
