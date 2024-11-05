# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:03:28 2024

@author: Eeshwar
"""

def user_input():
    graph = {}
    n = int(input("Enter the number of vertices: "))
    
    for i in range(n):
        vertex = input("Enter the vertex: ")
        neighbours = []
        m = int(input(f"Enter the number of edges for {vertex}: "))
        
        for j in range(m):
            neighbour = input(f"Enter the neighbour of {vertex}: ")
            neighbours.append(neighbour)
            
        graph[vertex] = neighbours
    
    return graph


def dfs_algo(stack,visited,dfs):
    while stack:
        vertex = stack.pop()
        dfs.append(vertex)
        
        for neighbour in reversed(graph[vertex]):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
                
def dfs(graph,source):
    stack = [source]
    visited = set()
    visited.add(source)
    
    dfs = []
    
    while stack:
        dfs_algo(stack,visited,dfs)
        
    while len(visited) < len(graph):
        for vertex in graph:
            if vertex not in visited:
                stack.append(vertex)
                visited.add(vertex)
                dfs_algo(stack,visited,dfs)
                
    return dfs

graph = user_input()
source = input("Enter the source vertex: ")
dfs = dfs(graph,source)
print(dfs)