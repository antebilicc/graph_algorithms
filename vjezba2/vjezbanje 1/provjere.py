def kvadratna(matrica):
    return len(matrica) == len(matrica[0])        

def simetricna(matrica):
    if not kvadratna(matrica):
        return False

    for i in range(len(matrica)):
        for j in range (len(matrica)):
            if matrica[i][j] != matrica[j][i]:
                return False
    return True

def stohasticka(matrica):
    for j in range(len(matrica[0])):
        suma = 0

        for i in range(len(matrica)):
            suma += matrica[i][j]

        if round(suma) != 1:
            return False

    return True