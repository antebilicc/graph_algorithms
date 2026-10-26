from provjere import kvadratna


def dijagonale(matrica):
    glavna = 0
    sporedna = 0

    if not kvadratna(matrica):
        raise Exception("Matrica nije kvadratna")

    for i in range(len(matrica)): #moze kroz jedan loop
        glavna += matrica[i][i]
        sporedna += matrica[i][len(matrica) - 1 - i]

    return round(glavna, 2), round(sporedna, 2)

def mnozenje(A, B):
    if len(A[0]) != len(B):
        raise Exception("Matrice se ne mogu množiti")

    C = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C

def transponiraj(A):
    T = []

    for j in range(len(A[0])):
        redak = []
        for i in range(len(A)):
            redak.append(A[i][j])
        T.append(redak)

    return T