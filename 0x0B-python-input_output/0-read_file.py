#!/usr/bin/python3

def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
       filename (str) (default ""): the file name

    """
    with open(filename, 'r') as f:
        print(f.read(), end="")
