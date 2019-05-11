"""
Parse map data from the JSON produced by Google Maps.
"""
import json


def get_route_info(json_str):
    """
    Return route information from the given JSON string.

    Parameters
    ----------
    json_str : str

    Returns
    -------
    route_info : dict
    """
    # Return specific values converted to native Python objects TODO
    return json.loads(json_str)

