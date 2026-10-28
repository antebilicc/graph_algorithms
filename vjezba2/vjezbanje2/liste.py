def main():
    brojevi = [1,2,3,4,5,6,7,8,9,10]
    imena = ["Ana", "Marko", "Ivana", "Petar", "Luka"]
    mijesano = [1, "Ana", 2, "Marko", 3, "Ivana", 4, "Petar", 5, "Luka", "element"]

    mijesano.append("Novi element") #dodavanje elementa na kraj
    print(mijesano)

    mijesano.extend([6, "A"]) #dodavanje više elemenata na kraj, npr 6 i A
    print(mijesano)

    mijesano.insert(1, "element") #dodavanje elementa na indeks (k, element)
    print(mijesano)

    mijesano.remove("element") #uklanjanje prvog pojavljivanje iz liste gdje matcha "element"
    print(mijesano)

    mijesano.pop(1) #uklanjanje elementa na indeksu k
    print(mijesano)

    print(mijesano.count("Petar")) #broji ponavljanje elementa u listi

    imena.sort() #sortira listu, ali ne može miješanu listu
    brojevi.sort(reverse=True) #sortira listu obrnutim redoslijedom

    print(imena)
    print(brojevi)

    mijesano.reverse() #okreće listu
    print(mijesano)

    b = mijesano.copy() #kopira listu
    print(b)

    a = mijesano.index("Petar") #daje indeks elementa u listi
    print(a)

    print(sorted(brojevi)) #sortira listu, ali ne mijenja originalnu listu

if __name__ == "__main__":
    main()