from collections import deque

def user_input():
   
    graph = {}  
    n = int(input("Enter the number of vertices: ")) 
    
    for i in range(n):
        vertex = input("\nEnter the vertex: ") 
        neighbours = []
        m = int(input(f"Enter the number of edges for {vertex}: "))  
        
        for j in range(m):
            neighbour = input(f"Enter neighbour of {vertex}: ")  
            neighbours.append(neighbour)  
            
        graph[vertex] = neighbours 
    
    return graph  


def bfs_algo(q, bfs_result, visited, graph):
 
    while q:  
        vertex = q.popleft()  
        bfs_result.append(vertex) 
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:  
                visited.add(neighbour) 
                q.append(neighbour)  

def BFS(graph, source):
    q = deque([source])  
    visited = set([source])  
    
    bfs_result = []  
    
    bfs_algo(q, bfs_result, visited, graph)

    for vertex in graph:
        if vertex not in visited:  
            q.append(vertex) 
            visited.add(vertex)
            bfs_algo(q, bfs_result, visited, graph)
    
    return bfs_result  

graph = user_input()

source = input("Enter the source node: ")

bfs_result = BFS(graph, source)

print("BFS Traversal:", bfs_result)