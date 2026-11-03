fs = {
    'docs': {'a.txt': 3, 'b.txt': 5},
    'img': {'x.png': 10, 'raw': {'y.png': 20}},
    'notes.txt': 2
}

def velicina(fs):
    rezultat = 0

    for ime, vrijednost in fs.items():
        if isinstance(vrijednost, dict):
            rezultat += velicina(vrijednost)
        else:
            rezultat += vrijednost

    return rezultat


def putanja(fs, datoteka):
    for ime, vrijednost in fs.items():

        if ime == datoteka and not isinstance(vrijednost, dict):
            return [ime]

        if isinstance(vrijednost, dict):
            rezultat = putanja(vrijednost, datoteka)

            if rezultat is not None:
                return [ime] + rezultat

    return None


def ispisi(fs, razina=0):
    for ime, vrijednost in fs.items():

        if isinstance(vrijednost, dict):
            print("    " * razina + ime + "/")
            ispisi(vrijednost, razina + 1)

        else:
            print("    " * razina + f"{ime} ({vrijednost})")


def main():
    print("Ukupna veličina:", velicina(fs))
    print("Veličina mape img:", velicina(fs['img']))

    print("Putanja do y.png:", putanja(fs, 'y.png'))
    print("Putanja do nepostoji.txt:", putanja(fs, 'nepostoji.txt'))

    print("\nSadržaj datotečnog sustava:")
    ispisi(fs)


if __name__ == "__main__":
    main()