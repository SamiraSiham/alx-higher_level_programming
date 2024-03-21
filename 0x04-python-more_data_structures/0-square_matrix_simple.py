#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = matrix.copy()
    for i in matrix:
        for j in i:
            j = j * j
    return copy_matrix
