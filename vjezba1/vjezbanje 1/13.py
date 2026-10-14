def pogodi_broj():
    donja = 1
    gornja = 100
    pokusaji = 0

    while donja <= gornja:
        sredina = (donja + gornja) // 2
        pokusaji += 1

        print("Je li tvoj broj", sredina, "?")
        odgovor = input("Upisi veći, manji ili tocno: ")

        if odgovor == "tocno":
            return pokusaji
        elif odgovor == "veci":
            donja = sredina + 1
        elif odgovor == "manji":
            gornja = sredina - 1

    return pokusaji


def main():
    broj_pokusaja = pogodi_broj()
    print("Broj pokušaja:", broj_pokusaja)


main()