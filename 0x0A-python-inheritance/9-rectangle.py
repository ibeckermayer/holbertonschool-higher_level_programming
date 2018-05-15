#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class
    """

    def __init__(self, width, height):
        """initializes Rectangle

        Attributes:
            self.__width: width of instance
            self.__height: height of instance

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle

        Returns:
            int: the area of the rectangle

        """
        return self.__width * self.__height

    def __str__(self):
        """rectangle description

        Returns:
            str: [Rectangle] <width>/<height>

        """
        rec = "[Rectangle] "
        rec += "{:d}".format(self.__width)
        rec += "/"
        rec += "{:d}".format(self.__height)
        return rec
