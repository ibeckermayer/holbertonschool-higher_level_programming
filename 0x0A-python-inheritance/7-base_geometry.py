#!/usr/bin/python3

class BaseGeometry:
    """base class for general geometry
    """

    def area(self):
        """finds the area of geometry object

        Raises:
            Exception: always

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer > 0

        Args:
           name (string): the name
           value (int): the value

        Raises:
            TypeError: if value is not a string
            ValueError: if value is not > 0

        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if not(value > 0):
            raise ValueError("{:s} must be greater than 0".format(name))
