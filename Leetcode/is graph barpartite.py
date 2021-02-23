# from collections import deque

# def isBipartite(graph):
#     node_colors = [-1 for i in range(len(graph))]
#     queue = deque()
#     queue.append(0)
#     node_colors[0] = 1
#     while queue:
#         curr_node = queue.pop()
#         curr_color = node_colors[curr_node]
#         for i in range(len(graph[curr_node])):
#             adjacent_node = graph[curr_node][i]
#             if node_colors[adjacent_node] == curr_color:
#                 # print(curr_node, i, node_colors)
#                 return False
#             elif node_colors[adjacent_node] == -1:
#                 node_colors[adjacent_node] = 1 - curr_color
#                 queue.append(graph[curr_node][i])
#     return True

# print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
# print(isBipartite([[1,3],[0,2],[1,3],[0,2]]))


from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
      # node_colors = [-1 for i in range(len(graph))]
      # queue = deque()
      # queue.append(0)
      # node_colors[0] = 1
      # while queue:
      #     curr_node = queue.pop()
      #     curr_color = node_colors[curr_node]
      #     for i in range(len(graph[curr_node])):
      #         adjacent_node = graph[curr_node][i]
      #         if node_colors[adjacent_node] == curr_color:
      #             # print(curr_node, i, node_colors)
      #             return False
      #         elif node_colors[adjacent_node] == -1:
      #             node_colors[adjacent_node] = 1 - curr_color
      #             queue.append(graph[curr_node][i])
      # return True
      
        color = {}
        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True