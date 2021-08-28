
import json
import logging
import os
from flask import (Blueprint, Flask, Response, g, jsonify, render_template,
                   request)

import pandas as pd
bp = Blueprint('controller', __name__)

package_dir = os.path.dirname(os.path.realpath(__file__+'../'))
file_to_search_restaurants =  os.path.join(package_dir,'../restaurants.csv')

def search_all(restaurant_name=None):

    df = pd.read_csv(file_to_search_restaurants,  index_col=False, sep=",")

    if restaurant_name is not None:
        print('Finding by name...')
        df = df.loc[df['name'] == restaurant_name]

    js = df.to_json(orient = 'records')
    return js


