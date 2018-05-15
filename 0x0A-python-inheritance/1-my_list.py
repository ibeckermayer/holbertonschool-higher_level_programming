#!/usr/bin/python3

class MyList(list):
    """extension of list which has a print_sorted method
    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        temp = list(self)
        temp.sort()
        print(temp)
