#!/usr/bin/python3


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
