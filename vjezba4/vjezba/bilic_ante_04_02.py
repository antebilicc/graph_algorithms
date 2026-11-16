import graf

def fun1(names, graph, directed):
    n = len(names)
    m = 0

    if directed:
        for i in range(n):
            m += len(graph[i])
    else:
        for i in range(n):
            m += len(graph[i])
        m = m // 2

    return n, m


def fun2(names, graph):
    stupanj = []

    for i in range(len(names)):
        stupanj.append(len(graph[i]))

    return stupanj


def fun3(names, graph, weighted):
    ulazni = [0] * len(names)
    izlazni = [0] * len(names)

    for i in range(len(names)):
        for j in graph[i]:
            if weighted:
                tezina = graph[i][j]
            else:
                tezina = 1

            izlazni[i] += tezina
            ulazni[j] += tezina

    return ulazni, izlazni


def main():
    names, graph, directed  = graf.read_pajek('k5.net')

    print(fun1(names, graph, directed))
    print(fun2(names, graph))
    print(fun3(names, graph, True))

if __name__ == "__main__":
    main()