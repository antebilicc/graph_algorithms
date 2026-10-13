def rotiraj(lista, k):
    k = k % len(lista)
    return lista[-k:] + lista[:-k]

def main():
    print(rotiraj([1, 2, 3, 4, 5], 2))

if __name__ == "__main__":
    main()