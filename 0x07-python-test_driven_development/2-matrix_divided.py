#!/usr/bin/python3
def is_matrix(matrix):
    """checks if matrix is a list of lists of int/float

    Args:
       matrix (list of list of int/float): a matrix

    Returns:
        bool: True if successful, False otherwise.

    """
    if not isinstance(matrix, list):
        return False
    for row in matrix:
        if not isinstance(row, list):
            return False
        if len(row) == 0:
            return False
        for i in row:
            if not isinstance(i, (int, float)):
                return False
    return True


def has_equal_rows(matrix):
    """checks if a matrix has equal sized rows

    Args:
       matrix (list of list of int/float): a matrix

    Returns:
        bool: True if successful, False otherwise.

    """
    first = True
    for row in matrix:
        if first:
            first = False
            row_len = len(row)
            continue
        if len(row) != row_len:
            return False
    return True


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
       matrix (list of list of int/float): a matrix of equal
           length rows
       div (int, float): the divisor

    Returns:
        [[float]]: a new matrix divided by div, rounded to 2 decimal places

    Raises:
        TypeError: Must be a list of lists of integers or floats
        TypeError: Each row of the matrix must be of the same size
        TypeError: div must be a number
        ZeroDivisionError: div must not be 0
    """
    if not is_matrix(matrix):
        s = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(s)
    if not has_equal_rows(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []
        for row in matrix:
            new_row = []
            for i in row:
                new_row.append(round(i/div, 2))
            new_matrix.append(new_row)
        return new_matrix
