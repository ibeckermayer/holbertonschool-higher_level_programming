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
