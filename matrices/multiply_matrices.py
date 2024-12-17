"""
This module provides functionality for multiplying matrices.

    multiply_matrices: Multiplies two matrices and returns the result.

    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result = multiply_matrices(matrix1, matrix2)
    print(result)  # Output: [[19, 22], [43, 50]]

    Ensure that the number of columns in the first matrix is equal to the number of rows in the second matrix.

    Guakocius

    # 12/17/2024
"""
import numpy as np
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = matrix1 @ matrix2
print(result)# Output: [[19, 22], [43, 50]]