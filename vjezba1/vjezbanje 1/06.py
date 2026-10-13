def analiza_recenice(recenica):
    recenica = recenica.replace(",", "").replace(".", "")
    rijeci = recenica.split()

    broj_rijeci = len(rijeci)
    najdulja = max(rijeci, key=len)

    return broj_rijeci, najdulja

def main():
    broj_rijeci, najdulja_rijec = analiza_recenice("Ovo je primjer rečenice, koja sadrži nekoliko riječi.")
    print(f"Broj riječi: {broj_rijeci}")
    print(f"Najdulja riječ: {najdulja_rijec}")

if __name__ == "__main__":
    main()