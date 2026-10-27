import random

def fun1(matrica):
    d = {}
    for i in range(len(matrica)):
        d[i] = [] #dodaj ovo da bi za kljuc zapravo stavili novi prazan list i da se moze dodavati tupleovi
        for j in range(len(matrica)):
            if matrica[i][j] != 0:
                d[i].append((j, matrica[i][j]))
    return d

def fun2(n): 
    k = random.randint(1, n)
    lista = []
    for i in range(k):
        broj = random.randint(1, n)
        lista.append(broj)
    return k, lista

def fun3(n):
    d = {}
    for i in range(n):
        d[i] = []
        k = random.randint(1, n)
        for j in range(k):
            broj = random.randint(1, n)
            d[i].append(broj) 
    return d

def fun4(d):
    d2 = {}
    for key, value in d.items():
        d2[key] = len(value)
    return d2

def main():
    matrica = [[0, 2, 3], [4, 0, 6], [0, 0, 9]]
    print(fun1(matrica))

    print(fun2(100))

    d = fun3(4)
    print(d)
    print(fun4(d))

if __name__ == "__main__":
    main()