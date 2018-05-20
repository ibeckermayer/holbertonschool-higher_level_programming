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
            list_dictionaries (list): a list of dictionaries

        Returns:
            str: string representation

        """
        if not list_dictionaries:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instances who inherits of Base

        """
        if not list_objs:
            with open("Rectangle.json", 'w') as f:
                f.write(Base.to_json_string(None))
            return

        import models.rectangle
        import models.square
        rects = []
        sqrs = []
        for obj in list_objs:
            if isinstance(obj, models.rectangle.Rectangle):
                rects.append(obj)
            if isinstance(obj, models.square.Square):
                sqrs.append(obj)

        list_dictionaries_rect = [rect.to_dictionary() for rect in rects]
        list_dictionaries_sqr = [sqr.to_dictionary() for sqr in sqrs]

        if len(list_dictionaries_rect) > 0:
            with open("Rectangle.json", 'w') as f:
                f.write(Base.to_json_string(list_dictionaries_rect))
        if len(list_dictionaries_sqr) > 0:
            with open("Square.json", 'w') as f:
                f.write(Base.to_json_string(list_dictionaries_sqr))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string (str): a string of a list of dictionaries

        Returns:
            list: the list of the JSON string representation json_string

        """
        return json.loads(json_string)
