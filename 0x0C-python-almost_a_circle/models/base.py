#!/usr/bin/python3
import json

class Base:
    """Base class for shapes

    Attributes:
        __nb_objects (int): number of objects total

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the "base" of all other class in this project

        Args:
            id (int) (default None): the id of the object

        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (str): a list of dictionaries

        Returns:
            str: string representation

        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return ("[]")
