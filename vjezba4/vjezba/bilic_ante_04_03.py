import graf

def euler(names, graph):
    neparni = []

    for i in range(len(names)):
        stupanj = len(graph[i])

        if stupanj % 2 != 0:
            neparni.append(names[i])

    if len(neparni) == 0:
        status = 'Eulerov'
    elif len(neparni) == 2:
        status = 'Polu-Eulerov'
    else:
        status = 'Nije Eulerov'

    return status, neparni
    

def ispravna_ruta(names, d, ruta, directed):
    predjeni = set()

    for i in range(len(ruta) - 1):
        u = names.index(ruta[i])
        v = names.index(ruta[i + 1])

        if v not in d[u]:
            return False

        if directed:
            brid = (u, v)
        else:
            brid = (min(u, v), max(u, v))

        if brid in predjeni:
            return False

        predjeni.add(brid)

    return True

def main():
    names, graph, directed = graf.read_pajek('stanice.net')

    print(euler(names, graph))

    ruta = ["HNK", "pazar", "trajektna luka"]
    print(ispravna_ruta(names, graph, ruta, directed))

if __name__ == "__main__":
    main()