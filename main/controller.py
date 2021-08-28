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

    df = build_dataframe()
    df = apply_filters(df, list_of_filters)
    df = sort_dataframe(df)

    df = df.head(current_pagination)
    js = df.to_json(orient = 'records')
    return  json.loads(js)


def build_dataframe():
    restaurantes_df = pd.read_csv(file_to_search_restaurants, index_col=False, sep=",")
    cuisines_df = pd.read_csv(file_to_search_cuisines, index_col=False, sep=",")

    print('Merging dataframes...')
    df = restaurantes_df.merge(cuisines_df, left_on='cuisine_id', right_on='id', suffixes=("_restaurant","_cuisine"))

    print('Dropping columns..')
    df = df.drop(columns=["id", "cuisine_id"])
    return df


def apply_filters(data_frame, list_of_filters):
    if list_of_filters is not {}:
        for key, value in list_of_filters.items():
            if key in ['customer_rating']:
                data_frame = data_frame.loc[data_frame[key] >= int(value)]
            elif key in ['price', 'distance']:
                data_frame = data_frame.loc[data_frame[key] <= int(value)]
            else:
                data_frame = data_frame.loc[data_frame[key].str.contains(value)]
    return data_frame
            

def sort_dataframe(data_frame):
    print('Sorting ...')
    return data_frame.sort_values(
        by=['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine'], 
        ascending=[True, False, True, True, True]
    )