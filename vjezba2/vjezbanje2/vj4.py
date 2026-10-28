def gornja_trokutasta(matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            if i > j and matrica[i][j] != 0:
                return False
    return True

def donja_trokutasta(matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            if i < j and matrica[i][j] != 0:
                return False
    return True

def lijeva_trokutasta(matrica):
    n = len(matrica)
    for i in range(n):
        for j in range(len(matrica[i])):
            if i + j < n - 1 and matrica[i][j] != 0:
                return False
    return True

def desna_trokutasta(matrica):
    n = len(matrica)
    for i in range(n):
        for j in range(len(matrica[i])):
            if i + j > n - 1 and matrica[i][j] != 0:
                return False
    return True        

def main():
    matrica = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    print(matrica)
    print(gornja_trokutasta(matrica))
    print(donja_trokutasta(matrica))
    print(lijeva_trokutasta(matrica))
    print(desna_trokutasta(matrica))

if __name__ == "__main__":
    main()