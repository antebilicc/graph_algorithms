def drugi_najveci(lista):
    najveci = None
    drugi = None

    for x in lista:
        if najveci is None or x > najveci:
            drugi = najveci
            najveci = x
        elif x != najveci and (drugi is None or x > drugi):
            drugi = x

    return drugi

def main():
    lista = [3, 5, 2, 8, 1]
    rezultat = drugi_najveci(lista)
    print(rezultat)

if __name__ == "__main__":
    main()