import sys

def print_mst(parent, graph):
    sum = 0
    print("\nEdge \tWeight")
    for i in range(1, len(graph)):
        print(f"{parent[i]} - {i} \t {graph[i][parent[i]]}")
        sum = sum + graph[i][parent[i]]
    print("The total edge weight : ",sum)

def prim_mst(graph, vertices):
    key = [sys.maxsize] * vertices
    parent = [-1] * vertices
    key[0] = 0
    mst_set = [False] * vertices

    for _ in range(vertices):
        u = min((key[i], i) for i in range(vertices) if not mst_set[i])[1]
        mst_set[u] = True

        for v in range(vertices):
            if graph[u][v] and not mst_set[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    print_mst(parent, graph)

def input_graph():
    vertices = int(input("\nEnter the number of vertices: "))
    graph = []

    print("Enter the adjacency matrix (row by row):")
    for i in range(vertices):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        graph.append(row)

    prim_mst(graph, vertices)

input_graph()
