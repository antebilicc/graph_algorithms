def citaj_rijeci(filename):
    rijeci = []
    with open(filename, "r") as file:
        for line in file:
            rijeci.append(line.strip())
    return rijeci

def anagrami(rijeci):
    grupe = {}
    for rijec in rijeci:
        key = "".join(sorted(rijec))

        if key not in grupe:
            grupe[key] = []

        grupe[key].append(rijec)

    return grupe

def anagrami_min2(rijeci):
    grupe = anagrami(rijeci)
    rezultat = {}

    for key, rijeci_grupa in grupe.items():
        if len(rijeci_grupa) >= 2:
            rezultat[key] = rijeci_grupa

    rezultat = dict(sorted(
        rezultat.items(),
        key=lambda group: (-len(group[1]), group[0])
    ))

    return rezultat

def vrati_anagrame(rijec, anagrami):
    rijeci = anagrami.get("".join(sorted(rijec)), [])
    rijeci.remove(rijec)
    return rijeci

def main():
    rijeci = citaj_rijeci("rijeci.txt")
    print(rijeci)
    print()
    anagrami_grupe = anagrami(rijeci)
    print(anagrami_grupe)
    print()
    anagrami_min2_grupe = anagrami_min2(rijeci)
    print(anagrami_min2_grupe)
    print()
    anagrami_za_rijec = vrati_anagrame("stone", anagrami_grupe)
    print(anagrami_za_rijec)


if __name__ == "__main__":
    main()