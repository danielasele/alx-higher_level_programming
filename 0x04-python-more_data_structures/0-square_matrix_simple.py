#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
    - matrix: A 2-dimensional array.

    Returns:
    - A new matrix with each value squared.
    """
    new_matrix = []

    for row in matrix:
        new_row = [x ** 2 for x in row]
        new_matrix.append(new_row)

    return new_matrix
