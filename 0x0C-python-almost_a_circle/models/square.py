#!/usr/bin/python3
"""for checker
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square

        Args:
           size (int): size of the square
           x (int) (default 0): x position of the square
           y (int) (default 0): y position of the square
           id (int) (default None): the id of the square

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>

        Returns:
            str

        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """getter for size
        """
        return self.width

    @size.setter
    def size(self, size):
        """setter for size

        Args:
        size (int, optional): size of the square

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is not > 0

        """

        # if not isinstance(size, int):
        #     raise TypeError("size must be an integer")
        # if not size > 0:
        #     raise ValueError("size must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute

        Args:
           *args: id, size, x, y
           *kwargs: same as args

        Returns:
            bool: True if successful, False otherwise.

        Raises:
            ValueError: If param2 is equal to param1.

        """
        if args:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square

        Returns:
            dict: the rep of the sqr

        """
        self_dict = {}
        self_dict["id"] = self.id
        self_dict["size"] = self.size
        self_dict["x"] = self.x
        self_dict["y"] = self.y
        return self_dict
