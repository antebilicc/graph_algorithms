def fun1(matrica):
    if len(matrica) != len(matrica[0]):
        raise Exception("Matrica nije kvadratna!")

    d = {}
    for i in range(len(matrica)):
        d[chr(97 + i)] = {}
        d[chr(97 + i)]["zbroj"] = 0
        d[chr(97 + i)]["parni"] = []
        d[chr(97 + i)]["neparni"] = []
        for j in range(len(matrica)):
            d[chr(97 + i)]["zbroj"] += matrica[j][i]
            if matrica[j][i] % 2 == 0:
                d[chr(97 + i)]["parni"].append(matrica[j][i])
            else:
                d[chr(97 + i)]["neparni"].append(matrica[j][i])

    return d

def main():
    matrica = [
        [4, 0, 7, 2],
        [3, 5, 0, 8],
        [6, 2, 9, 0],
        [0, 7, 3, 4]
    ]

    print(fun1(matrica))

if __name__ == "__main__":
    main()