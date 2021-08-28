
from flask import Flask, Blueprint, request, jsonify, g, Response, render_template
from flask_expects_json import expects_json
import json
import logging

bp = Blueprint('resource', __name__, url_prefix='/resource')

@bp.route("/search", endpoint='search', methods=['GET'])
def search():
    return 'TEST WORKED';

@bp.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 500
    
