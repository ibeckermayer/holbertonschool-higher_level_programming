#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """saves an object to a text file, using a JSON representation

    Args:
       my_obj (object): an object
       filename (str): the file to save to

    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
