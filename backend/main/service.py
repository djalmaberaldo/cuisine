"""
Module to search the data and filter by the list passed on the get request
"""

import logging
import os
from flask import Blueprint

import pandas as pd

bp = Blueprint('controller', __name__)
logging.basicConfig(level=logging.INFO)
package_dir = os.path.dirname(os.path.realpath(__file__+'../'))
file_to_search_restaurants =  os.path.join(package_dir,'../restaurants.csv')


def build_dataframe():
    """
    Joins the dataframe restaurants.csv with cuisine.csv

    Returns:
        The merged dataframe
    """

    file_to_search_cuisines =  os.path.join(package_dir,'../cuisines.csv')

    restaurantes_df = pd.read_csv(file_to_search_restaurants, index_col=False, sep=";")
    cuisines_df = pd.read_csv(file_to_search_cuisines, index_col=False, sep=",")

    logging.info('Merging dataframes...')
    df = restaurantes_df.merge(
        cuisines_df,
        left_on='cuisine_id',
        right_on='id',
        suffixes=("_restaurant","_cuisine")
    )

    logging.info('Dropping columns..')
    df = df.drop(columns=["id", "cuisine_id"])
    return df


logging.info('Building dataframes ...')
data_frame = build_dataframe()


def search_all(list_of_filters):
    """
    Search the restaurants based on the filters sent

    Args:
        list_of_filters (dict, optional): The list of filters Defaults to {}.

    Returns:
       The result dataframe converted to JSON
    """

    logging.info('Applying filters ...')
    search = apply_filters(data_frame, list_of_filters)

    logging.info('Sorting datagframe ...')
    search = sort_dataframe(search)
    return search.to_json(orient = 'records')


def apply_filters(data_frame, list_of_filters):
    """
    Filters the database based on the list of filters

    Args:
        data_frame (dataframe): The current dataframe
        list_of_filters (dict): The list of filters

    Returns:
        The filtered dataframe
    """
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


def add_restaurant(listOfFilters):
    global data_frame
    listOfFilters['restaurant_id'] = data_frame['restaurant_id'].iloc[-1]
    data_frame = data_frame.append(listOfFilters, ignore_index= True)
    return 'Restaurant added'


def remove_restaurant(restaurant_id):
    global data_frame
    data_frame = data_frame[data_frame['restaurant_id'] != restaurant_id]
    return 'Restaurant removed'
