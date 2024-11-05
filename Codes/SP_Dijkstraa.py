def dijkstra(graph,source):     
    shortest = {vertex:float('inf') for vertex in graph}     
    shortest[source] = 0      
    visited = set() 
    while len(visited)<len(graph):         
        curr = None         
        curr_distance = float('inf')   
        for vertex in graph:             
            if vertex not in visited and shortest[vertex]<curr_distance: 
                curr = vertex                 
                curr_distance = shortest[vertex]             
        if curr==None:             
            break        
        visited.add(curr)         
        for neighbour,weight in graph[curr]:             
            distance = curr_distance+weight             
            if neighbour not in visited and shortest[neighbour]>distance: 
                shortest[neighbour] = distance     
    return shortest 
    
def user_input():     
    graph={}     
    n = int(input("Enter the number of vertices: "))     
    for i in range(n):         
        vertex = input("\nEnter the vertex: ")         
        neighbours = []         
        m = int(input("Enter the number of edges: "))   
        for i in range(m): 
            neighbour = input(f"Enter the neighbour for vertex {vertex}:") 
            weight = int(input(f"Enter the weight for the edge {vertex} -> {neighbour}: "))
            neighbours.append((neighbour,weight))
        graph[vertex]=neighbours     
    return graph 
 
def display_graph(graph): 
    print("\nGraph:")     
    for vertex,neighbours in graph.items():         
        for neighbour,weight in neighbours: 
            print(f"{vertex} -> {neighbour} (Weight: {weight})") 
     
     
def unreachable_vertex(shortest,source): 
    count = 0     
    for vertex,distance in shortest.items(): 
        if distance == float('inf'): 
            print(f"\nThe vertex {vertex} is unreachable from the source vertex {source}.") 
            count = 1 
    if count==0: 
        print(f"\nThere is no such vertex that is unreachable from the source {source}") 
            
graph = user_input() 
display_graph(graph) 
source = input("\nEnter the source node: ") 
shortest = dijkstra(graph, source) 
print("\nShortest distance from the source: ",source," ->",shortest) 
unreachable_vertex(shortest, source) 
