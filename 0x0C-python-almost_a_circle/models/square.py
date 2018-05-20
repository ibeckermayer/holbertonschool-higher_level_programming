#!/usr/bin/python3
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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not size > 0:
            raise ValueError("size must be > 0")
        self.width = size
        self.height = size
