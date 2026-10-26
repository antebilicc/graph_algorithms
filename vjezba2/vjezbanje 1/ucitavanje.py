def fun(datoteka):
    podatci = []
    matrica = [] 
    f = open(datoteka) 
    for line in f: 
        i,j,w = line.split()
        podatci.append((int(i),int(j),float(w)))

    if not podatci:
        return []

    broj_redaka = max(i for i, j, w in podatci) + 1
    broj_stupaca = max(j for i, j, w in podatci) + 1

    matrica = [[0] * broj_stupaca for _ in range(broj_redaka)]

    for i, j, w in podatci:
        matrica[i][j] = w

    return matrica