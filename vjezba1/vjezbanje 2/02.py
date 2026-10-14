def vrati_najduzu_parne(lista):
    indeks = 0
    trenutni_indeks = 0
    trenutna_duzina = 0
    najveca_duzina = 0

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            if trenutna_duzina == 0:
                trenutni_indeks = i

            trenutna_duzina += 1

            if trenutna_duzina > najveca_duzina:
                najveca_duzina = trenutna_duzina
                indeks = trenutni_indeks
        else:
            trenutna_duzina = 0

    return indeks, najveca_duzina


def main():
    lista = [1, 2, 3, 4, 6, 8, 11, 12, 15, 16, 18, 20, 22, 24, 25, 27]
    print(vrati_najduzu_parne(lista))


if __name__ == "__main__":
    main()
