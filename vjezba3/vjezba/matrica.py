def read_matrix(filename):
    """Cita matricu cijelih brojeva; svaki redak datoteke je jedan redak matrice."""
    matrix = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                matrix.append([int(x) for x in line.split()])
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))
