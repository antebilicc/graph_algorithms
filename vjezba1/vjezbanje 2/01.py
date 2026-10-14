def izbroji(recenica):
    brojac = 0
    rijeci = recenica.split()
    for r in rijeci:
        broj = 0

        for i in r:
            if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u":
                broj += 1
        
        if broj >= 2:
            brojac += 1

    return brojac

def main():
    rez = izbroji("Ova recenica ima nekoliko riječi s više od dvije samoglasnike.")
    print(rez)

if __name__ == "__main__":
    main()
