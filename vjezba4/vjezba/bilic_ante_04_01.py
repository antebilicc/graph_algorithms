import graf

def print_vertex(names, graph, vertex):
    print(names[vertex], end=': ')

    for neighbor, weight in graph[vertex].items():
        print(f'{names[neighbor]} ({weight})', end=' ')

    print()


def print_graph(names, graph):
    for vertex in graph:
        print_vertex(names, graph, vertex)


def main():
    names, graph, directed = graf.read_pajek('k5.net')

    print(names)
    print(graph)
    print(directed)

    print_graph(names, graph)
    print_vertex(names, graph, 2)

    graf.write_pajek('output.net', names, graph, directed)


if __name__ == "__main__":
    main()