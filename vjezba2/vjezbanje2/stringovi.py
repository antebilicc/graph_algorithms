def main():
    s = "AAAAAAbcdefghijklmnoprstuvwxyz"
    print(s[0]) #prvi karakter
    print(s[-3]) #odzada 3 indeks
    print(s[1:5:2]) #slicing, pocetak:kraj:korak, stime da je pocetak 1, kraj 5
    print(s[::2]) #slicing, pocetak:kraj:korak 2
    print(s[::-1]) #obrnuti string (od pocetka do kraja, korak -1)

    s1 = "Abc-asa-def"
    print(len(s1)) #dužina stringa
    print(s1.upper()) #sve pretvara u velika slova
    print(s1.lower()) #sve pretvara u mala slova
    print(s1.split("-")) #vraća listu riječi, po defaultu se dijeli po razmaku

    strip = "   Abc-asa-def   "
    print(strip.strip()) #uklanja praznine na početku i kraju stringa

    print(s1.replace("-", "")) #zamjena u stringu sa drugim characterom
    print(s1.find("asa")) #vraća indeks prvog pojavljivanja stringa, ako ne postoji vraća -1

    print(s1.count("a")) #broji koliko puta se pojavljuje character u stringu
    print(s1.startswith("Abc")) #provjerava da li string počinje sa zadanim stringom
    print(s1.endswith("de")) #provjerava da li string završava sa zadanim stringom

    #stringovi su immutable, zato treba spremati u istu varijablu s ovim dolje
    s = s.replace("A", "a")
    print(s)

if __name__ == '__main__':
    main()
