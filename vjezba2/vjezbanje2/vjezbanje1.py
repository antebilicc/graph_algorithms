def fun(matrica):
    if len(matrica) != len(matrica[0]):
        return ValueError("Nije kvadratna")

    for i in range(len(matrica)):
        for j in range(len(matrica[i]) -1, -1, -1):
            if matrica[i][j] == 0:
                matrica[i][j] = 1
            elif matrica[i][j] == 1:
                matrica[i][j] = 0
            elif matrica[i][j] > 3:
                matrica[i][j] *= matrica[i][j]
            elif matrica[i][j] <= 3 and matrica[i][j] >= 0:
                matrica[i][j] *= 2
            elif matrica[i][j] < 0:
                matrica[i].pop(j)

    return matrica

def main():
    matrica = [
        [1,2,1],
        [5,-2,2],
        [0,3,7]
    ]

    print(fun(matrica))

if __name__ == "__main__":
    main()