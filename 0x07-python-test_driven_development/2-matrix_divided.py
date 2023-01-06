def matrix_divided(matrix, div):
    """Divides all the elements of a matrix"""
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('''
        matrix must be a matrix
        (list of lists) of integers/floats
        ''')
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

        return [[round(cell / div, 2) for cell in row] for row in matrix]