import json
import logging
import os
from flask import (Blueprint, Flask, Response, g, jsonify, render_template,
                   request)

import pandas as pd

bp = Blueprint('controller', __name__)

package_dir = os.path.dirname(os.path.realpath(__file__+'../'))
file_to_search_restaurants =  os.path.join(package_dir,'../restaurants.csv')
file_to_search_cuisines =  os.path.join(package_dir,'../cuisines.csv')

current_pagination = 5

def search_all(list_of_filters={}):

    restaurantes_df = pd.read_csv(file_to_search_restaurants, index_col=False, sep=",")
    cuisines_df = pd.read_csv(file_to_search_cuisines, index_col=False, sep=",")

    print('Merging dataframes...')
    df = restaurantes_df.merge(cuisines_df, left_on='cuisine_id', right_on='id', suffixes=("_restaurant","_cuisine"))

    print('Dropping columns..')
    df = df.drop(columns=["id", "cuisine_id"])

    if list_of_filters is not {}:
        for key, value in list_of_filters.items():
            if key in ['customer_rating']:
                df = df.loc[df[key] >= int(value)]
            elif key in ['price', 'distance']:
                df = df.loc[df[key] <= int(value)]
            else:
                df = df.loc[df[key].str.contains(value)]

    print('Sorting ...')
    df = df.sort_values(
        by=['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine'], 
        ascending=[True, False, True, True, True]
    )

    df = df.head(current_pagination)
    js = df.to_json(orient = 'records')
    return js


