def fun(dictionary):
    najveci_indeks = 0
    for k , v in dictionary.items():
        a,b,c = v[0], v[1], v[2]
        d,e,g = k
        if a > najveci_indeks:
            najveci_indeks = a
        if b > najveci_indeks:
            najveci_indeks = b
        if d > najveci_indeks:
            najveci_indeks = d
        if e > najveci_indeks:
            najveci_indeks = e 

    matrica = [[0 for _ in range(najveci_indeks + 1)] for _ in range(najveci_indeks + 1)]

    for values in dictionary.values():
        matrica[values[0]][values[1]] = values[2]

    for k in dictionary.keys():
        a, b, c = k
        matrica[a][b] = c

    return najveci_indeks, matrica

def main():
    dictinary = {
        (1,2,5): [0,1,5],
        (3,5,2): [2,3,8],
        (4,3,12): [3,1,5]

    }
    print(fun(dictinary))

if __name__ == "__main__":
    main()