def fun(podaci):
    broj = len(podaci.keys())
    m = set()
    matrica = [[0 for _ in range(broj)] for _ in range(broj)]
    for key, values in podaci.items():
        for v in values:
            i = ord(key)-97
            j = v[0]
            k = v[1]
            
            if j + 1> broj:
                raise ValueError("Indeks izvan granica matrice")

            if (i,j) not in m:
                m.add((i,j))
                matrica[i][j] = k

    return matrica

def main():
    podaci = {
    "a": [(0, 5), (0, 8), (4, 3)],
    "b": [(1, 7), (1, 4)],
    "c": [(0, 6), (3, 9)],
    "d": [(1, 2), (3, 5), (4, 1)],
    "e": [(0, 4), (2, 6), (3, 2)]
    }

    print(fun(podaci))

if __name__ == "__main__":
    main()