def sifriraj(tekst, k):
    rezultat = ""

    for znak in tekst:
        if 'a' <= znak <= 'z':
            novi = (ord(znak) - ord('a') + k) % 26
            rezultat += chr(novi + ord('a'))

        elif 'A' <= znak <= 'Z':
            novi = (ord(znak) - ord('A') + k) % 26
            rezultat += chr(novi + ord('A'))

        else:
            rezultat += znak

    return rezultat

def desifriraj(tekst, k):
    return sifriraj(tekst, -k)



def svi_pomaci(tekst):
    rezultati = []

    for k in range(1, 26):
        rezultati.append(desifriraj(tekst, k))

    return rezultati


def main():
    tekst = "Python je jezik za ucenje algoritama."
    k = 5
    sifra = sifriraj(tekst, k)
    print("Sifrirani tekst:", sifra)

    tekst2 = (
    'Yl gupkmlxl cupdlglxz klolevp tk lwrzctelxl, '
    'l klolnt df klytxwutgt t vzctdyt.'
    )
    
    rez = svi_pomaci(tekst2)
    for i in range(len(rez)):
        print(rez[i])


if __name__ == '__main__':
    main()