def add_edge(graph, u, v, w):
    graph.append((u, v, w))

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def kruskal_mst(vertices, graph):
    result = []
    graph.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = list(range(vertices))  # Initialize parent array
    rank = [0] * vertices           # Initialize rank array

    for u, v, w in graph:
        x, y = find(parent, u), find(parent, v)
        if x != y:
            result.append((u, v, w))
            union(parent, rank, x, y)
    sum = 0
    print("\nEdge \tWeight")
    for u, v, weight in result:
        print(f"{u} - {v}    {weight}")
        sum = sum + weight
    
    print("The total edge weight : ",sum)

def input_graph():
    vertices = int(input("\nEnter the number of vertices: "))
    graph = []

    print("Enter the adjacency matrix (row by row):")
    for i in range(vertices):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        for j in range(i + 1, vertices):
            if row[j] != 0:
                add_edge(graph, i, j, row[j])

    kruskal_mst(vertices, graph)

input_graph()
