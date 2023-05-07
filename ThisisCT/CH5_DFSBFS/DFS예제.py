# DFS algorithm example

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [[1],
         [0,2],
         [1,3],
         [2]]

visited = [False] * len(graph)

dfs(graph,1,visited)