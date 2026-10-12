def pascal(n):
    redak = [1]

    for i in range(n):
        print(*redak)

        novi = [1]

        for j in range(len(redak) - 1):
            novi.append(redak[j] + redak[j + 1])

        novi.append(1)
        redak = novi


def pascal_centrirano(n):
    redak = [1]
    redci = []

    for i in range(n):
        redci.append(redak)

        novi = [1]

        for j in range(len(redak) - 1):
            novi.append(redak[j] + redak[j + 1])

        novi.append(1)
        redak = novi

    #sirina = len(redci[-1]) * 2 - 1 -ne brojimo elemente, nego duljinu broja, pa da tako bude lijepše centrirano, jer brojevi nisu iste duljine

    zadnji = ""
    for broj in redci[-1]:
        zadnji += str(broj) + " "

    sirina = len(zadnji) - 1

    for redak in redci:
        tekst = ""

        for broj in redak:
            tekst += str(broj) + " "

        tekst = tekst[:-1]

        razmaci = (sirina - len(tekst)) // 2

        print(" " * razmaci + tekst)


def pascal_lik(n):
    redak = [1]

    for i in range(n):
        razmaci = n - i - 1
        print(" " * razmaci, end="")

        for broj in redak:
            if broj % 2 == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()

        novi = [1]

        for j in range(len(redak) - 1):
            novi.append(redak[j] + redak[j + 1])

        novi.append(1)
        redak = novi


def main():
    pascal(10)

    pascal_centrirano(10)

    pascal_lik(6)


if __name__ == '__main__':
    main()

