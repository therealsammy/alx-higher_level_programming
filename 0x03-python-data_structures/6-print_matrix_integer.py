#!/usr/bin/python3
def print_matrix_integers(matrix=[[]]):
    for sublist in range(len(matrix)):
        for i in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if i != (len(matrix[i]) - 1):
                print(" ", end="")

        print("")
