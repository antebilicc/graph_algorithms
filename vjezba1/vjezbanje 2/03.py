def rotiraj_listu(lista):
    n = len(lista)
    for i in range(n // 2):
        lista[i], lista[n - i - 1] = lista[n - i - 1], lista[i]
    return lista

def main():
    rez = rotiraj_listu([1, 23, 3, 44, 5, 5])
    print(rez)

if __name__ == "__main__":
    main()