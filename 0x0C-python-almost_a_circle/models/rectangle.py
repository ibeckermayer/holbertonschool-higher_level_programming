#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize Rectangle

        Args:
           width (int): width of the rectangle
           height (int): height of the rectangle
           x (int) (default 0): x position of the rectangle
           y (int) (default 0): y position of the rectangle
           id (int) (default None): the id of the rectangle

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width

        Args:
        width (int, optional): width of the rectangle

        Raises:
        TypeError: if width is not an integer
        ValueError: if width is not > 0

        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not width > 0:
            raise ValueError("width must be > 0")
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
        height (int, optional): height of the rectangle

        Raises:
        TypeError: if height is not an integer
        ValueError: if height is not > 0

        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not height > 0:
            raise ValueError("height must be > 0")
        self.__height = height


    @property
    def x(self):
        """getter for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x

        Args:
        x (int, optional): x position of the rectangle

        Raises:
        TypeError: if x is not an integer
        ValueError: if x is not >= 0

        """

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y

        Args:
        y (int, optional): y position of the rectangle

        Raises:
        TypeError: if y is not an integer
        ValueError: if y is not >= 0

        """

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of the rectangle

        Returns:
            int: the area of the rectangle

        """
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        """
        rec = ""
        if self.width == 0 or self.height == 0:
            print()
        else:
            for h in range(self.height):
                for w in range(self.width):
                    rec += str("#")
                if h < self.height - 1:
                    rec += "\n"
            print(rec)

