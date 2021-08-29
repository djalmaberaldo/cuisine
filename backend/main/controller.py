import json
import logging
import os
from flask import (Blueprint, Flask, Response, jsonify, request)

import pandas as pd

bp = Blueprint('controller', __name__)

package_dir = os.path.dirname(os.path.realpath(__file__+'../'))
file_to_search_restaurants =  os.path.join(package_dir,'../restaurants.csv')
file_to_search_cuisines =  os.path.join(package_dir,'../cuisines.csv')

logging.basicConfig(level=logging.INFO)

current_pagination = 5

def search_all(list_of_filters={}):
    """
    Search the restaurants based on the filters sent

    Args:
        list_of_filters (dict, optional): The list of filters Defaults to {}.

    Returns:
       The result dataframe converted to JSON
    """

    logging.info('Building dataframes ...')
    df = build_dataframe()

    logging.info('Applying filters ...')
    df = apply_filters(df, list_of_filters)

    logging.info('Sorting datagframe ...')
    df = sort_dataframe(df)

    logging.info('Retrieving the first ' + str(current_pagination) + ' rows...')
    df = df.head(current_pagination)
    js = df.to_json(orient = 'records')
    return js


def build_dataframe():
    """
    Joins the dataframe restaurants.csv with cuisine.csv 

    Returns:
        The merged dataframe
    """
    restaurantes_df = pd.read_csv(file_to_search_restaurants, index_col=False, sep=",")
    cuisines_df = pd.read_csv(file_to_search_cuisines, index_col=False, sep=",")

    logging.info('Merging dataframes...')
    df = restaurantes_df.merge(cuisines_df, left_on='cuisine_id', right_on='id', suffixes=("_restaurant","_cuisine"))

    logging.info('Dropping columns..')
    df = df.drop(columns=["id", "cuisine_id"])
    return df


def apply_filters(data_frame, list_of_filters):
    """
    Filters the database based on the list of filters

    Args:
        data_frame (dataframe): The current dataframe
        list_of_filters (dict): The list of filters

    Returns:
        The filtered dataframe 
    """
    if list_of_filters is not {}:
        for key, value in list_of_filters.items():
            if key in ['customer_rating']:
                data_frame = data_frame.loc[data_frame[key] >= int(value)]
            elif key in ['price', 'distance']:
                data_frame = data_frame.loc[data_frame[key] <= int(value)]
            else:
                data_frame = data_frame.loc[data_frame[key].str.contains(value, case=False)]
    return data_frame
            

def sort_dataframe(data_frame):
    """
    Sorts the dataframe by the following order

    distance -> Ascending
    customer_rating -> Descending
    price -> Ascending
    name_restaurant -> Ascending
    name_cuisine -> Ascending

    Args:
        data_frame: The current panda dataframe

    Returns:
        The dataframe sorted
    """

    logging.info('Sorting ...')
    return data_frame.sort_values(
        by=['distance','customer_rating', 'price', 'name_restaurant', 'name_cuisine'], 
        ascending=[True, False, True, True, True]
    )