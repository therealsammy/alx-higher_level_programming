#!/usr/bin/python3
"""
14-pascal_triangle module
"""


def pascal_triangle(n):
    """
    function that that returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    triangle = [[0 for k in range(l + 1)] for l in range(n)]
#    print(triangle)
#    matrix = [[0 for k in range(n)] for l in range(n)]
#    print(matrix)
    if n <= 0:
        return triangle
    else:
        for i in range(n):
            for j in range(i + 1):
                if (j is 0 or j is i):
                    triangle[i][j] = 1
#                    triangle[i][j] = matrix[i][j]
                else:
                    triangle[i][j] = triangle[i - 1][j - 1] +\
                                     triangle[i - 1][j]
#                    triangle[i][j] = matrix[i][j]
        return triangle
