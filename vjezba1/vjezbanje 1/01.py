def prosjecna(temperature):
    return sum(temperature) / len(temperature)

def najdulji_rast(temperature):
    najbolji_pocetak = 0
    najbolja_duljina = 1

    pocetak = 0
    duljina = 1

    for i in range(1, len(temperature)):
        if temperature[i] > temperature[i - 1]:
            duljina += 1
        else:
            pocetak = i
            duljina = 1

        if duljina > najbolja_duljina:
            najbolji_pocetak = pocetak
            najbolja_duljina = duljina

    return najbolji_pocetak, najbolja_duljina


def najveca_promjena(temperature):
    najveci_indeks = 1
    najveca_razlika = abs(temperature[1] - temperature[0])

    for i in range(2, len(temperature)):
        razlika = abs(temperature[i] - temperature[i - 1])

        if razlika > najveca_razlika:
            najveca_razlika = razlika
            najveci_indeks = i

    return najveci_indeks           


def main():
    temperature = [12, 14, 15, 13, 16, 17, 19, 18]
    pocetak, duljina = najdulji_rast(temperature)
    print(f"({pocetak}, {duljina})")
    print(prosjecna(temperature))

    print(najveca_promjena(temperature))

if __name__ == "__main__":
    main()