import csv

def ucitaj_udaljenosti(filename):
    with open(filename, "r") as f:
        podaci = list(csv.reader(f))

    gradovi = podaci[0][1:]
    matrica = []

    for i in range(1, len(podaci)):
        red = []
        for j in range(1, len(podaci[i])):
            if podaci[i][j] == "-":
                red.append(0)
            else:
                red.append(int(podaci[i][j]))
        matrica.append(red)

    return gradovi, matrica

def napravi_rjecnik(gradovi, matrica):
    d = {}

    for i in range(len(gradovi)):
        d[gradovi[i]] = {}

        for j in range(len(gradovi)):
            d[gradovi[i]][gradovi[j]] = matrica[i][j]

    return d

def najblizi_gradovi(grad, d, k):
    rezultat = []

    for drugi_grad, udaljenost in d[grad].items():
        if drugi_grad != grad:
            rezultat.append((udaljenost, drugi_grad))

    rezultat.sort()

    return rezultat[:k]

def najudaljeniji_gradovi(gradovi, matrica):
    najveća = 0

    for i in range(len(gradovi)):
        for j in range(i + 1, len(gradovi)):
            if matrica[i][j] > najveća:
                najveća = matrica[i][j]
                grad1 = gradovi[i]
                grad2 = gradovi[j]

    return grad1, grad2, najveća

def nesimetricni_parovi(gradovi, matrica):
    rezultat = []

    for i in range(len(gradovi)):
        for j in range(i + 1, len(gradovi)):
            if matrica[i][j] != matrica[j][i]:
                rezultat.append((gradovi[i], gradovi[j], (matrica[i][j], matrica[j][i])))

    return rezultat 

def main():
    gradovi, udaljenosti = ucitaj_udaljenosti("distance.csv")
    print(gradovi)
    for red in udaljenosti:
        print(red)
    print()
    d = napravi_rjecnik(gradovi, udaljenosti)
    print(d["Paris"]["Rome"])
    print(d)
    print(najblizi_gradovi("Vienna", d, 3))
    print()
    print(najudaljeniji_gradovi(gradovi, udaljenosti))
    print()
    print(nesimetricni_parovi(gradovi, udaljenosti))

if __name__ == "__main__":
    main()
