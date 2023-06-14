#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        square_matrix = []
        for j in i:
            square_matrix.append(j ** 2)
        result.append(square_matrix)
    return result
