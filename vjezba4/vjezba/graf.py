def read_pajek(filename):
    names = []
    graph = {}
    directed = False

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    section = None

    for line in lines:
        line = line.strip()

        if not line or line.startswith('%'):
            continue

        if line.startswith('*'):
            parts = line.split()
            section = parts[0].lower()

            if section == '*vertices':
                n = int(parts[1])
                names = [str(i) for i in range(n)]
                graph = {i: {} for i in range(n)}

            elif section == '*arcs':
                directed = True

            continue

        if section == '*vertices':
            parts = line.split(maxsplit=1)
            vertex = int(parts[0]) - 1

            if len(parts) > 1:
                name = parts[1].strip('"')
                names[vertex] = name

        elif section == '*edges' or section == '*arcs':
            parts = line.split()

            u = int(parts[0]) - 1
            v = int(parts[1]) - 1

            if len(parts) > 2:
                weight = float(parts[2])

                if weight.is_integer():
                    weight = int(weight)
            else:
                weight = 1

            graph[u][v] = weight

            if section == '*edges':
                graph[v][u] = weight

    return names, graph, directed


def write_pajek(filename, names, graph, directed):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'*Vertices {len(names)}\n')

        for i, name in enumerate(names):
            f.write(f'{i + 1} "{name}"\n')

        if directed:
            f.write('*Arcs\n')
        else:
            f.write('*Edges\n')

        for u in graph:
            for v, weight in graph[u].items():

                if not directed and u > v:
                    continue

                if weight == 1:
                    f.write(f'{u + 1} {v + 1}\n')
                else:
                    f.write(f'{u + 1} {v + 1} {weight}\n')
