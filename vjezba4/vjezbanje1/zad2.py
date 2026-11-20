def read_pajek(filename):
    names = []
    directed = False
    graph = {}

    with open(filename, "r") as f:
        lines = f.readlines()
    section = None

    for line in lines:
        parts = line.split()
        if not parts or line.startswith("%"):
            continue

        if parts[0].startswith("*Vertices"):
            section = "vert"
            broj = int(parts[1])
            graph = {i : {} for i in range(1, broj + 1)}
            continue

        elif parts[0].startswith("*EdgesList"):
            section = "edgeslist"
            continue

        elif parts[0].startswith("*ArcsList"):
            section = "arcslist"
            directed = True
            continue

        elif parts[0].startswith("*Edges"):
            section = "edges"
            continue

        elif parts[0].startswith("*Arcs"):
            section = "arcs"
            directed = True
            continue

        if section == "vert":
            names.append(parts[1].strip('"'))

        elif section == "edges" or section == "arcs":
            u = int(parts[0])
            v = int(parts[1])
                        
            if len(parts) == 3: #da nije težinski graf, onda ću krenit sa set() gore i onda bi dodavao sa .add
                w = float(parts[2])
            
                if w.is_integer():
                    w = int(w)
            
            else:
                w = 1
                        
            graph[u][v] = w
            if directed == False:
                graph[v][u] = w

        elif section == "edgeslist" or section == "arcslist":
            u = int(parts[0])
            for i in map(int, parts[1:]):
                graph[u][i] = 1
                if directed == False:
                    graph[i][u] = 1

    return names, graph, directed  


def matrix_susjeda(graph):
    n = len(graph)
    matrix = [[0] * n for _ in range(n)]

    for u in graph:
        for v in graph[u]:
            matrix[u - 1][v - 1] = graph[u][v]

    return matrix


def get_edges(graph, directed):
    edges = []
    for u in graph:
        for v in graph[u]:
            if directed:
                edges.append((u, v))
            else: 
                if (v, u) not in edges:
                    edges.append((u, v))
    return edges

def matrix_incidencije(graph, directed):
    n = len(graph)
    edges = get_edges(graph, directed)
    m = len(edges)
    matrix = [[0] * m for _ in range(n)]

    for j, (u, v) in enumerate(edges):
        if directed:
            matrix[u - 1][j] = -(graph[u][v])
            matrix[v - 1][j] = graph[u][v]
        else:
            matrix[u - 1][j] = graph[u][v] 
            matrix[v - 1][j] = graph[u][v] 

    return matrix

def stupnjevi_vrha(graph):
    deg = {}
    for u in graph:
        deg[u] = len(graph[u])
    return deg

def broj_vrhova(graph):
    return len(graph)

def ulazni_izlazni_stupnjevi(graph):
    in_deg = {}
    out_deg = {}
    for u in graph:
        out_deg[u] = len(graph[u])
        in_deg[u] = 0
    
    for u in graph:
        for v in graph[u]:
            in_deg[v] += 1

    return in_deg, out_deg

def main():

    names, graph, directed = read_pajek("test.net")
    print(names)
    print(graph)
    print(directed)

    m = matrix_susjeda(graph)
    for row in m:
        print(row)
    print()
    print(get_edges(graph, directed))
    print()
    matrica = matrix_incidencije(graph, directed)
    for row in matrica:
        print(row)

if __name__ == "__main__":
    main()
