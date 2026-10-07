import math 

def prosti_do(n):
   
    prost = [True] * (n + 1)
    prost[0], prost[1] = False, False

    a = 2
    while a <= int(math.sqrt(n)):
        if prost[a]:
            for i in range(a * a, n + 1, a):
                prost[i] = False
        a += 1
 
    lista = []
    for i in range (2, n + 1):
        if prost[i]: 
            lista.append(i)
    return lista



def prosti_blizanci(n):
    lista = prosti_do(n)

    lista2 = []
    for i in range(len(lista)-1):
        if lista[i] + 2 == lista[i+1]:
            lista2.append((lista[i], lista[i+1]))
    return lista2 

def goldbach(n):
    lista = prosti_do(n)

    lista2 = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] + lista[j] == n:
                lista2.append((lista[i], lista[j]))
    return lista2


def main():
    print(prosti_do(50))
    
    #print(prosti_blizanci(50))

    print(goldbach(54))
if __name__ == '__main__':
    main()
