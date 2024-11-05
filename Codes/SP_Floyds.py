def floyd_warshall(graph, vertices):
    vertices = sorted(vertices)
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}
    for v in vertices:
        dist[v][v] = 0
    for u in graph:
        for v, weight in graph[u]:
            dist[u][v] = weight
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for v in vertices:
        if dist[v][v] < 0:
            print("Graph contains a negative weight cycle.")
            return None
    
    return dist

def user_input():
    graph = {}
    vertices = set()
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Enter the vertex: ")
        vertices.add(vertex)
        m = int(input(f"Enter the number of edges for vertex {vertex}: "))
        neighbours = []
        for _ in range(m):
            neighbour = input(f"Enter the neighbour for vertex {vertex}: ")
            weight = int(input(f"Enter the weight for the edge {vertex} -> {neighbour}: "))
            neighbours.append((neighbour, weight))
            vertices.add(neighbour)
        
        graph[vertex] = neighbours
    
    return graph, vertices

def display_distances(dist, vertices):
    vertices = sorted(vertices)
    print("\nShortest distances between all pairs of vertices:")
    for i in vertices:
        row = [f"{dist[i][j]:>4}" if dist[i][j] != float('inf') else " inf" for j in vertices]
        print(row)

graph, vertices = user_input()
dist = floyd_warshall(graph, vertices)
if dist:
    display_distances(dist, vertices)
