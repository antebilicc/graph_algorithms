def fun():
    f = open("prati.txt")
    dictionary = {}

    for line in f:
        l = line.split()

        if l[0] not in dictionary:
            dictionary[l[0]] = set()
        if l[1] not in dictionary:
            dictionary[l[1]] = set()
            
        dictionary[l[0]].add(l[1])

    return dictionary


def fun2():
    dictionary = fun()
    dictionary2 = {}

    for key in dictionary:
        dictionary2[key] = set()

    for key, values in dictionary.items():
        for v in values:
            dictionary2[v].add(key)

    return dictionary2


def fun3():
    dictionary = fun()
    lista = []

    for a in dictionary:
        for b in dictionary[a]:
            if a in dictionary[b] and a < b:
                lista.append((a, b))

    lista.sort()
    return lista


def fun4():
    dictionary = fun2()
    najvise = 0
    osoba = ""

    for key in dictionary:
        broj = len(dictionary[key])

        if broj > najvise:
            najvise = broj
            osoba = key

    return osoba, najvise


def fun5():
    dictionary = fun2()
    lista = []

    for osoba in dictionary:
        if len(dictionary[osoba]) == 0:
            lista.append(osoba)

    lista.sort()
    return lista


def fun6(osoba):
    lista = []
    dictionary = fun()

    for koga in dictionary[osoba]:
        if osoba not in dictionary[koga]:
            lista.append(koga)

    lista.sort()
    return lista


def main():
    print(fun())
    print()
    print(fun2())
    print()
    print(fun3())
    print()
    print(fun4())
    print()
    print(fun5())
    print()
    print(fun6("cvita"))

if __name__ == "__main__":
    main()
    