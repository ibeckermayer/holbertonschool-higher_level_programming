#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
       my_obj (object): an object

    Returns:
        str: the JSON rep of my_obj

    """
    return json.dumps(my_obj)
