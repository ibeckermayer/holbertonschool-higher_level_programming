#!/usr/bin/python3
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
       my_str (str): a JSON string

    Returns:
        object: an object

    """
    return json.loads(my_str)
