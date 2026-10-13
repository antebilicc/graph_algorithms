def bez_duplikata(lista):
    nova = []

    for x in lista:
        if x not in nova:
            nova.append(x)

    return nova

def main():
    print(bez_duplikata([3, 1, 3, 2, 1]))

if __name__ == "__main__":
    main()