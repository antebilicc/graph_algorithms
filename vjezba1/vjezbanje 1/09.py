def rotiraj(lista, k):
    return lista[-k:] + lista[:-k]

def main():
    print(rotiraj([1, 2, 3, 4, 5, 22, 55, 56], 2))

if __name__ == "__main__":
    main()