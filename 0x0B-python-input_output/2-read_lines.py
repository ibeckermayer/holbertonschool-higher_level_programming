#!/usr/bin/python3


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
       filename (str) (default ""): the file name

    """
    with open(filename, 'r') as f:
        print(f.read(), end="")


def read_lines(filename="", nb_lines=0):
    """reads some number of lines from a textfile and prints it to stdout

    Read the entire file if nb_lines is lower or equal to 0
    OR greater or equal to the total number of lines of the file

    Args:
       filename (str) (default ""): the file name
       nb_lines (int) (default 0): number of lines to be read

    """
    if nb_lines <= 0:
        read_file(filename)
    else:
        with open(filename, 'r') as f:
            for i, l in enumerate(f):
                if i < nb_lines:
                    print(l, end="")
                else:
                    break
