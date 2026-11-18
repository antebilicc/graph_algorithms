def read_pajek(filename):
    names = []
    directed = False
    graph = {}

    with open(filename, 'r') as f:
        lines = f.readlines()

    section = None

    for line in lines:
        line = line.strip()

        if line.startswith("*Vertices"):
            section = "vertices"
            parts = line.split()
            continue

        elif line.startswith("*EdgesList"):
            section = "edgeslist"
            continue

        elif line.startswith("*ArcsList"):
            section = "arcs"
            directed = True
            continue

        elif line.startswith("*Edges"):
            section = "edges"
            continue

        elif line.startswith("*Arcs"):
            section = "arcs"
            directed = True
            continue

        elif line.startswith("*Matrix"):
            section = "matrix"
            continue

        if section == "vertices":
            parts = line.split()
            if len(parts) == 2:
                name = parts[1].strip('"')
                names.append(name)
                graph[name] = {}

        elif section == "edges" or section == "arcs":
            parts = line.split()
            u = int(parts[0])
            v = int(parts[1])
            
            if len(parts) > 2:
                w = float(parts[2])

                if w.is_integer():
                    w = int(w)

            else:
                w = 1
            
            graph[names[u-1]][names[v-1]] = w
            if directed == False:
                graph[names[v-1]][names[u-1]] = w


        elif section == "edgeslist" or section == "arcslist":
            parts = line.split()
            u = int(parts[0])
            for v in map(int, parts[1:]):
                graph[names[u-1]][names[v-1]] = 1
                if directed == False:
                    graph[names[v-1]][names[u-1]] = 1

    return names, graph, directed

def matrica_susjedstva(graph, names):
    n = len(graph.keys())
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if names[j] in graph[names[i]]:
                matrix[i][j] = graph[names[i]][names[j]]

    return matrix


def main():
    filename = "test.net"
    names, graph, directed = read_pajek(filename)
    
    print(names)
    print(graph)
    print(directed)

    print(matrica_susjedstva(graph, names))

if __name__ == "__main__":
    main()