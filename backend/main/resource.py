import json
import logging

from flask import (Blueprint, Flask, json, render_template, request, jsonify)

from . import controller

bp = Blueprint('resource', __name__, url_prefix='/resource')
expect_keys = ['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine']

@bp.route("/search", endpoint='search', methods=['GET'])
def search():
    list_of_filters = request.args.to_dict()

    results = json.loads(controller.search_all(list_of_filters))
    return jsonify(results), 200


@bp.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 


@bp.before_request
def validate_keys():
    keys = request.args.to_dict().keys()
    print('Validating parameters...')
    for k in keys:
        if k not in expect_keys:
            return 'Invalid Parameters', 400