"""
1. Initialization:
    - Build a graph with adjacency list. HashMap of vertex containing list of childs
    - inDegree hashmap to find out incoming edges for each vertex
2. Find Sources (Queue):
    - Add vertices with inDegree = 0 to the queue
3. Iterate through sources until possible:
    - Pop from queue and append to sortedOrder
    - Traverse through adjacency list of this vertex and decrement inDegree by 1 for all children
        - if inDegree = 0 append to queue
"""
from collections import deque

def topological_sort(v, edges):
    sortedOrder = []
    # 1.
    graph = {vertex:[] for vertex in range(v)}
    inDegree = {vertex:0 for vertex in range(v)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        inDegree[child] += 1

    # 2.
    sources = deque()
    for vertex in inDegree:
        if inDegree[vertex] == 0:
            sources.append(vertex)

    # 3.
    while sources:
        source = sources.popleft()
        sortedOrder.append(source)
        for child in graph[source]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)
    
    # if graph has a cycle
    if len(sortedOrder) != v:
        return []
    
    return sortedOrder

print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
print(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
print(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))