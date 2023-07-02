def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and returns a new matrix.

    :param matrix: A matrix represented as a list of lists of integers or floats.
    :param div: The number to divide the matrix elements by.

    :return: A new matrix with elements divided by div, rounded to 2 decimal places.

    :raises TypeError: If the matrix is not a list of lists of integers or floats,
                       if any row of the matrix has a different size,
                       or if div is not a number.
    :raises ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all elements of matrix are integers or floats
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # Return the new matrix
    return new_matrix
