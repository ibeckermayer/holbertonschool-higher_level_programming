#!/usr/bin/python3


class Rectangle:
    """A Rectangle
    """

    def __init__(self, width=0, height=0):
        """constructor

        Args:
           width (int, optional): the width of the rectangle
           height (int, optional): the height of the rectangle

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width

        Args:
           width (int, optional): the width of the rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is not >= 0

        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """getter for height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height

        Args:
           height (int, optional): the height of the rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is not >= 0

        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """returns the area of the rectangle

        Returns:
            int: the area of the rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle

        If either width or height is 0, returns 0

        Returns:
            int: the perimeter of the rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
