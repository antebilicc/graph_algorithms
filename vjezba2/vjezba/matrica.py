def read_matrix(filename):
    matrix = []

    with open(filename, "r") as file:
        for line in file:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)