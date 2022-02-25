"""
File where the endpoint is located along with its validation method
"""

from cmath import log
import json
import logging
from . import service

from flask import (Blueprint, json, request, jsonify)

from . import service

bp = Blueprint('resource', __name__, url_prefix='/resource')
expect_keys = ['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine', 'restaurant_id']

logging.basicConfig(level=logging.DEBUG)


@bp.route("/search", endpoint='search', methods=['GET'])
def search():
    """
    Does the search by calling the search_all method

    Returns:
        A jsonified list of restaurants with 200 status code

    """
    logging.info('Validating parameters...')
    for key,value in request.args.to_dict().items():
        if key not in expect_keys:
            return 'Invalid parameter ' + key, 400
        if value in ('null', ''):
            return 'Invalid value inside key ' + key, 400

    list_of_filters = request.args.to_dict()

    results = json.loads(service.search_all(list_of_filters))
    return jsonify(results), 200


@bp.route("/search/<id>", endpoint='get_restaurant', methods=['GET'])
def get_restaurant():
    """
    Does the search by calling the search_all method

    Returns:
        A jsonified list of restaurants with 200 status code

    """
    logging.info('Validating parameters...')
    for key,value in request.args.to_dict().items():
        if key not in expect_keys:
            return 'Invalid parameter ' + key, 400
        if value in ('null', ''):
            return 'Invalid value inside key ' + key, 400

    list_of_filters = request.args.to_dict()

    results = json.loads(service.search_all(list_of_filters))
    return jsonify(results), 200


@bp.route("/add", endpoint='add', methods=['POST'])
def add():
    """
    Does the search by calling the search_all method

    Returns:
        A jsonified list of restaurants with 200 status code
    """

    for key,value in request.json.items():
        if key not in expect_keys:
            return 'Invalid parameter ' + key, 400
        if value in ('null', ''):
            return 'Invalid value inside key ' + key, 400

    list_of_filters = request.json

    results = json.loads(service.add_restaurant(list_of_filters))
    return jsonify(results), 200


@bp.route("/update", endpoint='update', methods=['PUT'])
def update():
    """
    Does the search by calling the search_all method

    Returns:
        A jsonified list of restaurants with 200 status code
    """

    for key,value in request.json.items():
        if key not in expect_keys:
            return 'Invalid parameter ' + key, 400
        if value in ('null', ''):
            return 'Invalid value inside key ' + key, 400

    list_of_filters = request.json

    results = json.loads(service.update_restaurant(list_of_filters))
    return jsonify(results), 200


@bp.route("/delete/<restaurant_id>", endpoint='delete', methods=['DELETE'])
def delete(restaurant_id):
    """
    Does the search by calling the search_all method

    Returns:
        A jsonified list of restaurants with 200 status code
    """

    results = service.remove_restaurant(restaurant_id)
    return jsonify(results), 200


