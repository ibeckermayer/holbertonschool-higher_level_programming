#!/usr/bin/python3


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8)

    Args:
       filename (str) (default ""): the file name
       text     (str) (default ""): the text to be appended

    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
