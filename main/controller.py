
import json
import logging
import os
from flask import (Blueprint, Flask, Response, g, jsonify, render_template,
                   request)

import pandas as pd
bp = Blueprint('controller', __name__)

package_dir = os.path.dirname(os.path.realpath(__file__+'../'))
file_to_search_restaurants =  os.path.join(package_dir,'../restaurants.csv')

current_pagination = 5

def search_all(list_of_filters={}):

    df = pd.read_csv(file_to_search_restaurants,  index_col=False, sep=",")

    if list_of_filters is not {}:
        for key, value in list_of_filters.items():
            df = df.loc[df[key].astype(str).str.contains(value)]

    print('Sorting ...')
    df = df.sort_values(by=['distance','customer_rating', 'price'], ascending=[True, False, True])

    df = df.head(current_pagination)
    js = df.to_json(orient = 'records')
    return js


