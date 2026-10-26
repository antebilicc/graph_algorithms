def main():
    a = [5,3,2,1,6,7,5,3]
    a.sort(reverse=True) #ova funkcija se izvršava direktno na listi a, ne vraća novu listu
    print(a)

    b = sorted(a) #ova funkcija vraća novu listu, a originalna lista ostaje nepromijenjena
    print(b)

    c = ["banana", "apple", "orangeeee", "kiwi"]
    c.sort(key=len, reverse=True) #sortira listu c po duzini stringova
    print(c)

    kvadrat = lambda x: x**2 #lambda funkcija koja vraća kvadrat broja (bez definisanja funkcije sa def)
    print(kvadrat(5))

    rez = sorted(a, key = lambda x: x%4, reverse=True) #sortira listu a po ostatku pri dijeljenju sa 3
    print(rez)


    bodovi = {"Ana": 85,"Marko": 70,"Ivan": 95,"Mia": 80}
    rez2 = sorted(bodovi, key= bodovi.get) #sortira kljuceve rjecnika bodovi po vrijednostima, vraća listu
    print(rez2)

    rez3 = sorted(bodovi.items(), key=lambda x: x[1]) #sortira listu tupleova (kljuc, vrijednost) po vrijednostima
    print(rez3)


    d = {"imena": ["Marko", "Jelena", "Petar"], "godine": [25, 30, 20]}
    for ime, g in zip(d["imena"], d["godine"]):
        if g <= 25:
            d["imena"].remove(ime)
            d["godine"].remove(g)

    print(d)

if __name__ == "__main__":
    main()