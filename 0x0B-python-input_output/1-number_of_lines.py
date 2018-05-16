#!/usr/bin/python3


def number_of_lines(filename=""):
    """counts the number of lines in a text file

    Args:
       filename (str) (default ""): the file name

    Returns:
        (int): number of lines

    """
    lines = 0
    with open(filename, 'r') as f:
        for l in f:
            lines += 1
    return lines
