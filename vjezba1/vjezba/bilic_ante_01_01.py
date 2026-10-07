def pitagora(a, b, c):
    if a >= b and a >= c:
        najveci = a
        x = b
        y = c
    elif b >= a and b >= c:
        najveci = b
        x = a
        y = c
    else:
        najveci = c
        x = a
        y = b

    return x ** 2 + y ** 2 == najveci ** 2


def nzd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        ostatak = a % b
        a = b
        b = ostatak

    return a

def pitaj():
    while True:
        a, b, c = map(int, input("Unesite trojku: ").split())

        if a <= 0 or b <= 0 or c <= 0:
            break

        print(pitagora(a, b, c))

def pitaj2():
    N = int(input("Unesite N: "))
    print(primitivne(N))


def primitivne(N): 
    trojke = []
    for a in range(1, N + 1):
        for b in range(a, N + 1):
            for c in range(b, N + 1):
                if pitagora(a, b, c) and nzd(nzd(a, b), c) == 1:
                    trojke.append((a, b, c))
    return trojke



def main2():
    #pitaj()
    
    pitaj2()


if __name__ == '__main__':
    main2()