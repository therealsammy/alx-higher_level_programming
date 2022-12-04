#!/usr/bin/python3
def print_matrix_integers(matrix=[[]]):
    for sublist in matrix:
        for i in sublist:
            if sublist == matrix[-1]:
                print('{:d}'.format(sublist), end='')
            else:
                print('{:d}'.format(sublist), end=' ')

        print("")
