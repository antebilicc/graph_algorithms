import bilic_ante_04_02, graf, bilic_ante_04_01

def fun1(names, graph, directed):
    ulazni, izlazni = bilic_ante_04_02.fun3(names, graph, directed)
    return ulazni, izlazni


def authorities(names, uvezeni):
    sortirani = sorted(
        range(len(names)),
        key=lambda i: uvezeni[i],
        reverse=True
    )

    for i in sortirani[:5]:
        print(names[i], uvezeni[i])


def hubs(names, izvezeni):
    najveci = max(izvezeni)

    for i in range(len(names)):
        if izvezeni[i] == najveci:
            print(names[i], izvezeni[i])   


def samo_izvoze(names, izvezeni, uvezeni):
    rezultat = []

    for i in range(len(names)):
        if izvezeni[i] > 0 and uvezeni[i] == 0:
            rezultat.append(names[i])

    return rezultat


def izvozi_u(names, graph, drzava):
    u = names.index(drzava)

    for v in graph[u]:
        print(names[v], graph[u][v])


def main():
    names, graph, directed  = graf.read_pajek('football.net')
    ulazni, izlazni = fun1(names, graph, directed)
    print(ulazni, izlazni)

    bilic_ante_04_01.print_graph(names, graph)
    print()

    authorities(names, ulazni)
    print()
    hubs(names, izlazni)
    print()

    rez = samo_izvoze(names, izlazni, ulazni)
    print(rez)
    print()

    izvozi_u(names, graph, "CRO")

if __name__ == "__main__":
    main()