#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'

    Args:
       filename (str): the file to load from

    Returns:
        (object): the object loaded

    """
    with open(filename, 'r', encoding="UTF8") as f:
        return json.load(f)
