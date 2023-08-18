#!/usr/bin/python3
"""
A simple function that rotates a matrix 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    Rotator method
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            tem = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tem

    for i in range(n):
        for j in range(int(n / 2)):
            tem = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = tem
