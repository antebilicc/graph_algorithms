def ucitaj_stanice(ime_datoteke):
    d = {}

    f = open(ime_datoteke)

    for line in f:
        s1, s2 = line.strip().split("-")

        s1 = s1.strip()
        s2 = s2.strip()

        if s1 not in d:
            d[s1] = set()

        if s2 not in d:
            d[s2] = set()

        d[s1].add(s2)
        d[s2].add(s1)

    f.close()

    return d


def broj_susjeda(d):
    rezultat = {}

    for stanica in d:
        rezultat[stanica] = len(d[stanica])

    return rezultat


def najvise_susjeda(d):
    najveca = None
    maksimum = -1

    for stanica in d:
        broj = len(d[stanica])

        if broj > maksimum:
            maksimum = broj
            najveca = stanica

    return najveca


def krajnje_stanice(d):
    rezultat = []

    for stanica in d:
        if len(d[stanica]) == 1:
            rezultat.append(stanica)

    return rezultat


def ispravna_ruta(d, ruta):
    for i in range(len(ruta) - 1):
        if ruta[i] not in d:
            return False

        if ruta[i+1] not in d[ruta[i]]:
            return False

    return True


def main():
    d = ucitaj_stanice("stanice.txt")

    print(d)

    print(broj_susjeda(d))

    print(najvise_susjeda(d))

    print(krajnje_stanice(d))

    ruta = ["pazar", "opcina", "sukoisanska"]

    print(ispravna_ruta(d, ruta))


if __name__ == "__main__":
    main()