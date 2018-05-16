#!/usr/bin/python3


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
       filename (str) (default ""): the file name
       text     (str) (default ""): the text to be written

    """
    with open(filename, 'w') as f:
        return f.write(text)
