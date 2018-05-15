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
