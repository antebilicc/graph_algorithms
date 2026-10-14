def drugi_najveci(lista):
    najveci = 0
    drugi = 0

    for x in lista:
        if x > najveci:
            drugi = najveci
            najveci = x
        elif x != najveci and  x > drugi: 
            drugi = x

    return drugi

def main():
    lista = [3, 5, 2, 8, 1, 7, 7, 9]
    rezultat = drugi_najveci(lista)
    print(rezultat)

if __name__ == "__main__":
    main()