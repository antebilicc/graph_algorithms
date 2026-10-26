def main():
    slova = ["P", "y", "t", "h", "o", "n"]
    rijec = "".join(slova) #samo za stringove funkcija
    print(rijec)

    podaci = "Ana,Marko,Ivan"
    imena = podaci.split(",") #samo za liste
    print(imena)


    brojevi = [4,1,6]
    print("-".join(str(broj) for broj in brojevi))
    #ili
    print("-".join(map(str, brojevi)))


    for indeks, vrijednost in enumerate(brojevi, start=2): #start je određivanje početnog indeksa dakle indeks je 2 u ovom slučaju
        print(indeks, vrijednost)

    for ime, broj in zip(imena, brojevi): #prolazak kroz dvije liste istovremeno, ali uzima duljinu manje liste
        print(ime, broj)

    d = dict(zip(imena, brojevi)) #stvaranje rječnika iz dvije liste
    print(d)


    


if __name__ == "__main__":
    main()