#!/usr/bin/python3

def inherits_from(obj, a_class):
    """checks if an obj is an instance of a class that inherited from a_class

    Args:
       obj (class): the object to be checked
       a_class (object): the class you're looking for

    Returns:
        bool: True if an instance, otherwise False

    """
    return isinstance(obj, a_class) and type(obj) != a_class
